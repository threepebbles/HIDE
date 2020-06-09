# coding=<utf-8>

import struct, hashlib, os, encrypt
from Cryptodome.Cipher import AES
from Cryptodome import Random
import encrypt


# _directory 경로가 이미 생성되어있어야 함
# main 파일에서 생성시켜놔야함
_directory = os.path.abspath(os.path.join('C:/Users/이은영', 'Links/link.{59031a47-3f72-44a7-89c5-5595fe6b30ee}'))
_pwfile = hashlib.sha256('HIDE:password_for_program'.encode()).hexdigest()
_key = encrypt.make_pass(_pwfile, 'capstone2HIDE')


def chk_set_before():
    return os.path.isfile(os.path.join(_directory, _pwfile))


def _rm_pw():
    os.remove(os.path.join(_directory, _pwfile))


def _get_program_pw():
    try:
        fp = os.path.join(_directory, _pwfile)
        encrypt.decrypt_file(_key, fp)

        f = open(fp, 'r')
        pw = f.readline()
        f.close()

        encrypt.encrypt_file(_key, fp)
        return pw.rstrip()
    except Exception as e:
        print(e)
        return False


def cmp_program_pw(password):
    stored = _get_program_pw()
    if not _get_program_pw: return False

    if password == _get_program_pw(): return True
    else: return False


def set_program_pw(password):
    try:
        fp = os.path.join(_directory, _pwfile)
        f = open(fp, 'w')
        f.write(password)
        f.close()

        encrypt.encrypt_file(_key, fp)
        return True
    except Exception as e:
        print(e)
        return False