#!/usr/bin/env python3
"""
Setup script for Twitter Bot
"""

import os
import sys
import subprocess

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def create_env_file():
    """Create .env file from example"""
    if os.path.exists('.env'):
        print("✅ .env file already exists")
        return True
    
    if os.path.exists('env_example.txt'):
        try:
            with open('env_example.txt', 'r') as src:
                content = src.read()
            with open('.env', 'w') as dst:
                dst.write(content)
            print("✅ Created .env file from example")
            print("⚠️  Please edit .env file with your Twitter API credentials")
            return True
        except Exception as e:
            print(f"❌ Error creating .env file: {e}")
            return False
    else:
        print("❌ env_example.txt not found")
        return False

def test_configuration():
    """Test the configuration"""
    print("🔧 Testing configuration...")
    try:
        from config import Config
        Config.validate()
        print("✅ Configuration is valid")
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        print("Please check your .env file and ensure all required variables are set.")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up Twitter Bot...")
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        sys.exit(1)
    
    # Test configuration
    if not test_configuration():
        print("\n📝 Next steps:")
        print("1. Edit the .env file with your Twitter API credentials")
        print("2. Run: python main.py --config-test")
        print("3. Run: python main.py --test")
        print("4. Run: python main.py (to start the bot)")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📝 Next steps:")
    print("1. Run: python main.py --test (to test all components)")
    print("2. Run: python main.py (to start the bot)")

if __name__ == "__main__":
    main()
