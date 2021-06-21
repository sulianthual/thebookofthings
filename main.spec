# -*- mode: python ; coding: utf-8 -*-

# Use this spec file to compile code using pyinstaller:
# $pyinstaller main.spec
# (compiled code to distribute is the folder dist/thebookofthings. executable is _!THEBOOKOFTHINGS_LAUNCHER within)
# when finished can use mainicon.png to change folder icon manually
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
          name='_!THEBOOKOFTHINGS_LAUNCHER',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon='mainicon.ico',
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='thebookofthings',icon='mainicon.ico')

               # if compiling for MAC OS X need this too
app = BUNDLE(exe,
         name='thebookofthings.app',
         icon='mainicon.ico',
         bundle_identifier=None)
