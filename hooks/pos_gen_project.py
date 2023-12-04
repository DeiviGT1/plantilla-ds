import sys
import os

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

project_slug = "{{cookiecutter.project_slug}}"
non_alphanumeric = any(not char.isalnum() for char in project_slug)

if non_alphanumeric and non_alphanumeric != None:
    print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template.{RESET_ALL}")
    sys.exit()

print(f"{MESSAGE_COLOR}Let's do it! You're are going to create something awesome!") 
print(f"Creating project at { os.getcwd()}")