import subprocess

# List of dependencies
dependencies = [
    'moviepy', 
    'tk', 

]

def install_dependencies():
    for dependency in dependencies:
        subprocess.check_call(['pip', 'install', dependency])

def main():
    print("Installing dependencies...")
    install_dependencies()
    print("Dependencies installed successfully.")

if __name__ == '__main__':
    main()