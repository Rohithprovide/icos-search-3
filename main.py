#!/usr/bin/env python3
"""
IcosSearch - Main application entry point
A privacy-focused search engine based on Whoogle Search
"""

import os
import sys
import subprocess
from pathlib import Path

def setup_environment():
    """Setup the application environment"""
    # Add whoogle-search to Python path
    whoogle_path = Path(__file__).parent / "whoogle-search"
    sys.path.insert(0, str(whoogle_path))
    
    # Set environment variables
    os.environ.setdefault('WHOOGLE_CONFIG_URL', 'https://www.google.com')
    os.environ.setdefault('WHOOGLE_CONFIG_LANGUAGE', 'en')
    os.environ.setdefault('WHOOGLE_CONFIG_COUNTRY', 'US')
    os.environ.setdefault('WHOOGLE_CONFIG_THEME', 'dark')
    os.environ.setdefault('WHOOGLE_CONFIG_SAFE', 'off')
    os.environ.setdefault('WHOOGLE_CONFIG_DISABLE', 'false')
    os.environ.setdefault('WHOOGLE_CONFIG_VIEW_IMAGE', 'true')
    os.environ.setdefault('WHOOGLE_CONFIG_GET_ONLY', 'false')
    os.environ.setdefault('WHOOGLE_CONFIG_ANON_VIEW', 'false')
    os.environ.setdefault('WHOOGLE_CONFIG_NEAR', '')
    os.environ.setdefault('WHOOGLE_CONFIG_NEW_TAB', 'false')
    
def run_setup():
    """Run the setup script if it exists"""
    setup_script = Path(__file__).parent / "setup.sh"
    if setup_script.exists():
        try:
            subprocess.run(["bash", str(setup_script)], check=True)
            print("Setup script executed successfully")
        except subprocess.CalledProcessError as e:
            print(f"Setup script failed: {e}")
        except FileNotFoundError:
            print("Bash not found, skipping setup script")

def main():
    """Main application entry point"""
    print("Starting IcosSearch...")
    
    # Setup environment
    setup_environment()
    
    # Run setup if needed
    run_setup()
    
    try:
        # Import and run the Whoogle search app
        sys.path.insert(0, str(Path(__file__).parent / "whoogle-search"))
        from app import app
        
        # Configure the app
        app.config['DEBUG'] = os.getenv('DEBUG', 'false').lower() == 'true'
        
        # Start the application
        print("IcosSearch is running on http://0.0.0.0:5000")
        app.run(
            host='0.0.0.0',
            port=int(os.getenv('PORT', 5000)),
            debug=app.config['DEBUG']
        )
        
    except ImportError as e:
        print(f"Error importing Whoogle search: {e}")
        print("Please ensure all dependencies are installed")
        sys.exit(1)
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
