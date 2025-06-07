# How I Built My Password Generator 🏗️

## Step 1: Writing the Python Code
- Used **Tkinter** to create a simple GUI.
- Designed a function to generate passwords with random characters.
- Tested different variations for security.

## Step 2: Creating a Standalone Executable
- Installed `pyinstaller` using:
  ```sh
  pip install pyinstaller
-`cd` to the folder where your script is saved
- Converted the `.py` script into a single `.exe` file with:
  ```sh
  pyinstaller --onefile --windowed password_generator.py
- A folder named dist will be created in the same directory. Inside it, you'll find `.exe` file.

## Step 3: Packaging with Inno Setup
- Downloaded and installed **Inno Setup**.
- Created a **script file** that installs the `.exe` properly.
- Added shortcuts
