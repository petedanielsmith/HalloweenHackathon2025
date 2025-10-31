# Hackathon Halloween 2025

<details>
<summary>How to use this repo (Click to show)</summary>

**Make sure you have:**
- Python installed, this project used V3.12,

**From the terminal:**

Open the folder in a terminal where you want the project to be saved
#### Run git clone:
```
git clone https://github.com/petedanielsmith/HalloweenHackathon2025.git
```
#### Navigate in to the new folder:
```
cd HalloweenHackathon2025
```
#### Setup a virtual enviroment:
Create a virtual enviroment for the project.

Linux / Mac:
```
python3 -m venv .venv
source .venv/bin/activate
```
Windows CMD:
```
python3 -m venv .venv
.venv\Scripts\activate
```
Windows PowerShell:
```
python3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```
#### Install the dependancies:
This will install all the dependancies needed for the project in to the virtual enviroment if it is setup, rather than globally
```
pip install -r requirements.txt
```
#### Add `.env` file
Add a file in the root of the project called .env and add this to the file for local dev:
```
DEBUG=True
SECRET_KEY=dev-secret-key-change-this
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
```
#### Run the migration to create local db
```
python3 manage.py migrate
```
#### Create a local admin user
Run this and enter user, email and passowrds when asked
```
python manage.py createsuperuser
```
#### To launch the server
Run this and then open the url (probably http://127.0.0.1:8000/)
```
python3 manage.py runserver 
```

---

</details>