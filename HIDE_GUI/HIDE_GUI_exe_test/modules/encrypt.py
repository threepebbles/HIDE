# coding=<utf-8>

"""
aes256-cbc
"""

import struct, hashlib, os
from Cryptodome.Cipher import AES
from Cryptodome import Random


def decrypt_file(key, input_file, chunksize=24 * 1024):
    output_file = input_file + '.dec'
    try:
        with open(input_file, 'rb') as infile:
            origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
            iv = infile.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, iv)
            with open(output_file, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))
                outfile.truncate(origsize)

        os.remove(input_file)
        os.rename(output_file, input_file)
        return True
    except Exception as e:
        print(e)
        return False


def encrypt_file(key, input_file, chunksize=65536):
    output_file = input_file + '.enc'
    try:
        iv = Random.new().read( AES.block_size )
        encryptor = AES.new(key, AES.MODE_CBC, iv) # encode추가
        filesize = os.path.getsize(input_file)
        with open(input_file, 'rb') as infile:
            with open(output_file, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv)
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += ' '.encode() * (16 - len(chunk) % 16)
                    outfile.write(encryptor.encrypt(chunk))
                    
        os.remove(input_file)
        os.rename(output_file, input_file)
        return True
    except Exception as e:
        print(e)
        if os.path.isfile(output_file): os.remove(outfile)
        return False


# key generator
def make_pass(path, key):
    tmp = key + path
    return hashlib.sha256(tmp.encode()).digest()
