import subprocess
import os

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Let's do it! You're are going to create something awesome!")
print(f"Initializating a git repostory...{RESET_ALL}")

subprocess.run(["git", "init"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial commit"])

#if exists requirements.txt then install dependencies
if os.path.exists("requirements.txt"):
    print(f"{MESSAGE_COLOR}Installing dependencies...{RESET_ALL}")
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    
print(f"{MESSAGE_COLOR}Done!{RESET_ALL}")