import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "TechXpose",
    version = "1.0",
    description = "A tool for image & video processing",
    author = "刘文斌",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
