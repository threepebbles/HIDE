# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['E:\\workspace\\github\\HIDE\\HIDE_GUI\\HIDE_GUI_exe\\modules'],
             binaries=[],
             datas=[('../image/background.png', '.'), ('../image/filelist.png', '.'), ('../image/lock_c.png', '.'), ('../image/lock.png', '.'), ('../image/login_bt.png', '.'), ('../image/login.png', '.'), ('../image/logout_bt.png', '.'), ('../image/ok1.png', '.'), ('../image/ok2.png', '.'), ('../image/path.png', '.'), ('../image/pwset.png', '.'), ('../image/quit_c.png', '.'), ('../image/quit.png', '.'), ('../image/refresh_1.png', '.'), ('../image/refresh_2.png', '.'), ('../image/select_b.png', '.'), ('../image/select.png', '.'), ('../image/trash.png', '.'), ('../image/unlock_c.png', '.'), ('../image/unlock.png', '.'), ('../image/view_b.png', '.'), ('../image/view.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
