# PyInstaller spec for DokiDoki (pygame)
# Builds on both Windows and macOS (onedir). Includes assets and scene modules.

import sys
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

# Explicitly list scene modules to avoid dynamic import issues
hiddenimports = [
    'scenes.opening',
    'scenes.classroom',
    'scenes.cafe',
    'scenes.disneyland',
    'scenes.theater',
    'scenes.park',
]

# Data assets to bundle (directories are copied recursively)
datas = [
    ('sprites', 'sprites'),
    ('font', 'font'),
    ('icon.png', '.'),
]

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='DokiDoki',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll_targets = [exe]

# On macOS you can optionally wrap into an .app by enabling the BUNDLE block below.
# from PyInstaller.building.osx import BUNDLE
# if sys.platform == 'darwin':
#     app = BUNDLE(
#         exe,
#         name='DokiDoki.app',
#         icon=None,  # Provide an .icns if available
#         bundle_identifier=None,
#     )
#     coll_targets = [app]

coll = COLLECT(
    *coll_targets,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='DokiDoki',
)

