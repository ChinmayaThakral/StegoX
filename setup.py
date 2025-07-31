#!/usr/bin/env python3
"""
StegoX Setup and Test Script
Helps users install dependencies and verify the system works
"""

import subprocess
import sys
import os
import importlib.util

def check_python_version():
    print("Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"Python 3.8+ required, you have {version.major}.{version.minor}")
        return False
    print(f"Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def check_package(package_name, pip_name=None):
    try:
        spec = importlib.util.find_spec(package_name)
        if spec is not None:
            print(f"{package_name} is installed")
            return True
        else:
            print(f"{package_name} is missing")
            return False
    except ImportError:
        print(f"{package_name} is missing")
        return False

def install_dependencies():
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("Failed to install dependencies")
        return False

def test_modules():
    print("Testing custom modules...")
    try:
        from encryptor import encrypt_message, decrypt_message
        test_msg = "Hello World!"
        test_pwd = "test_password_123"
        encrypted = encrypt_message(test_msg, test_pwd)
        decrypted = decrypt_message(encrypted, test_pwd)
        assert test_msg == decrypted
        print("Encryption module works!")
    except Exception as e:
        print(f"Encryption test failed: {e}")
        return False
    try:
        from stego_engine import get_image_capacity
        print("Steganography module imported successfully!")
    except Exception as e:
        print(f"Steganography test failed: {e}")
        return False
    return True

def main():
    print("StegoX Setup and Test")
    print("=" * 40)
    if not check_python_version():
        return False
    if not os.path.exists("requirements.txt"):
        print("requirements.txt not found!")
        return False
    if not install_dependencies():
        return False
    if not test_modules():
        return False
    print("\nSetup completed successfully!")
    print("\nNext steps:")
    print("1. Run: streamlit run stegox_app.py")
    print("2. Upload a PNG image from the dataset")
    print("3. Test the voice authentication features")
    print("\nFor demo:")
    print("- Use sample images from 'Dataset/Sample images (.png)/'")
    print("- Record clear voice messages for authentication")
    print("- Have backup text passwords ready")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)