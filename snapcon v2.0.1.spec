# -*- mode: python -*-

block_cipher = None


a = Analysis(['snapcon 2.1.1.py'],
             pathex=['C:\\Users\\Eivind\\Desktop\\AoE\\Snapcon 2.0'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='snapcon 2.1.1',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='icon.ico')
