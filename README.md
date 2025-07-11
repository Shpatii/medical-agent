
## Requirements

1. Make sure Python is installed in your machine

2. Make sure you have all libs and dependecies installed if not run this command:
   'pip install -r requirements.txt'

3. Sometimes you have to install some dependicies manually with the following command:
   "pip install python-dotenv langchain langchain-together PyPDF2"


---

## How to Run

1. Run this command on terminal first:
"Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned"

2.Start Venv Folder (if needed , if you see a venv folder then just skip this step)
"python -m venv venv"

3. Now run this command:
".\venv\Scripts\Activate.ps1"

4. After venv is running in that same powershell/terminal run the app
"python manage.py runserver"

5. After Django is up and running simply go to your browser and go at https://www.news-medical.net/health/What-is-Viral-Pneumonia.aspx

6. Ctrl + C on the terminal to stop Flask if needed

To test the Agent use one of the 2 files that are in this repository inside the folder /uploads
