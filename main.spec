# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import shutil
import os
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

PROGRAM_NAME = "WalletScannerV4"
PROGRAM_FILE = "main.py"
ICON_FILE = "icon.ico"
COIN_SPECIFIC = "coinspecific"

# Function to copy additional files to the output directory
def copy_files():
    dest = os.path.join("dist", PROGRAM_NAME)
    support_data = [ICON_FILE, "zalo.gif", "discord.gif", "telegram.png"]
    coin_specific_data = [os.path.join(COIN_SPECIFIC, "demo.pyc"), os.path.join(COIN_SPECIFIC, "example.py")]

    for d in support_data:
        shutil.copy(d, dest)

    shutil.copy("config.json.example", os.path.join(dest, "config.json"))

    coinspecificdir = os.path.join(dest, COIN_SPECIFIC)
    os.makedirs(coinspecificdir, exist_ok=True)
    for d in coin_specific_data:
        shutil.copy(d, coinspecificdir)

a = Analysis(
    [PROGRAM_FILE],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=['eth_hash'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=PROGRAM_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=ICON_FILE
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=PROGRAM_NAME,
    icon=ICON_FILE
)

copy_files()  # Call the function to copy additional files