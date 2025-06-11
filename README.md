## Requirements

1. Make sure you have all libs and dependecies installed if not run this command:
   'pip install -r requirements.txt'

2. Sometimes you have to install flask manually with the following command:
   "pip install flask-cors python-dotenv langchain langchain-together PyPDF2"


---

## How to Run

1. Run this command as administrator first:
"Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned"

2.Start Venv Folder (if needed , if you see a venv folder then just skip this step)
"python -m venv venv"

3. Now open a new powershell/terminal and run this command:
".\venv\Scripts\Activate.ps1"

4. After venv is running in that same powershell/terminal run the app
"python main.py"

5. After Flask is up and running simply open/run the index.html file and you're good to go

6. Ctrl + C on the terminal to stop Flask if needed

To test the Agent use one of the 2 files that are in this repository inside the folder /uploads


