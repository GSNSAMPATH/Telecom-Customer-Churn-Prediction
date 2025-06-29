import subprocess
import sys

def install_dependencies():
    requirements = [
        'streamlit>=1.0.0',
        'pandas>=1.5.0',
        'scikit-learn>=1.0.0',
        'joblib>=1.2.0',
        'markdown-it-py>=3.0.0',
        'Pygments>=2.19.2',
        'rich>=14.0.0'
    ]
    
    print("Upgrading pip...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    
    print("Installing packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + requirements)

if __name__ == "__main__":
    install_dependencies()