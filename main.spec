# -*- mode: python -*-

block_cipher = None


added_files = [
     ( 'img', 'img' ),
	 ('music', 'music'),
	 ('tiles_map', 'tiles_map'),
	 ('Sprite', 'Sprite'),
	 ('LDEngine', 'LDEngine')
     ]

a = Analysis(['main.py'],
             pathex=['C:\\Users\\Bobsleigh\\Documents\\PythonProjects\\LD40'],
             binaries=None,
             datas=added_files,
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
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=False )
