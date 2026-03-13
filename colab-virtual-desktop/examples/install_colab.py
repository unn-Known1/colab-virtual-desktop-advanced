#!/usr/bin/env python3
"""
Quick install script for Colab Virtual Desktop

Run this in a Colab cell to set up everything:

    !pip install -q colab-virtual-desktop
    from colab_desktop import start_virtual_desktop
    desktop = start_virtual_desktop("YOUR_NGROK_TOKEN")
"""

import sys
import subprocess
import os

def install_colab_desktop():
    """Install colab-virtual-desktop in Colab"""
    print("🚀 Installing Colab Virtual Desktop...")

    # Check if in Colab
    if 'google.colab' not in sys.modules:
        print("⚠️  This script is designed for Google Colab")
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            sys.exit(1)

    # Install package
    print("📦 Installing Python package...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "colab-virtual-desktop"], check=True)

    print("✅ Installation complete!")
    print("\n📖 Next steps:")
    print("1. Get your ngrok token from https://ngrok.com")
    print("2. Run the following in a new cell:")
    print("")
    print("    from colab_desktop import start_virtual_desktop")
    print("    desktop = start_virtual_desktop('YOUR_NGROK_TOKEN')")
    print("")
    print("3. Open the printed URL in your browser")
    print("")
    print("💡 For more examples, see the examples/ directory")

def check_environment():
    """Check if Colab environment is ready"""
    print("🔍 Checking environment...")

    # Python version
    print(f"   Python: {sys.version.split()[0]}")

    # Colab detection
    if 'google.colab' in sys.modules:
        print("   ✅ Running in Google Colab")
    else:
        print("   ⚠️  Not running in Google Colab")

    # Disk space
    import shutil
    total, used, free = shutil.disk_usage("/")
    print(f"   Disk: {free // (2**30)} GB free")

    # RAM
    import psutil
    ram_gb = psutil.virtual_memory().total / (1024**3)
    print(f"   RAM: {ram_gb:.1f} GB")

    print("\n✅ Environment check complete")

if __name__ == "__main__":
    check_environment()
    print("")
    install_colab_desktop()
