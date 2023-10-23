"""Script to install dependencies for the application"""
import subprocess
dependencies = [
    'tk' 

]

def install_dependencies():
    """Function to install dependencies"""
    for dependency in dependencies:
        subprocess.check_call(['pip', 'install', dependency])

def main():
    """Main function"""
    print("Installing dependencies...")
    install_dependencies()
    print("Dependencies installed successfully.")

if __name__ == '__main__':
    main()
