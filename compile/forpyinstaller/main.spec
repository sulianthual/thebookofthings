# -*- mode: python ; coding: utf-8 -*-

# Use this spec file to compile code using pyinstaller:
# 0) be sure to install pyinstaller from outside anaconda env (or executables will be much bigger), e.g. with pip3
# 1) $pyinstaller main.spec
# 2) move dist/code/data/forpyinstaller/launcher to dist/code
# 3) zip and distribute the dist (with code/ and launcher inside)
# 4) can manually change folder/app icons using data/mainicon.png or data/mainicon.ico
#
# alternatively one can compile for a single file ($pyinstaller --onefile main.py with extra steps...) but doesnt work well
#
# 
block_cipher = None


a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[('book','book'),('data','data')],
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
          [],
          exclude_binaries=True,
          name='_!launcher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='code')

