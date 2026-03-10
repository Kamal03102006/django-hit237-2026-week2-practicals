# project_blog (Django project)

This repository contains a minimal Django project named `project_blog`.

Prerequisites
- Python 3.11+ installed and available on PATH (or use the `py` launcher on Windows).

Quick setup (PowerShell)

```powershell
# create virtual environment
py -3 -m venv venv

# upgrade pip and install latest Django inside the venv
.\venv\Scripts\python -m pip install --upgrade pip
.\venv\Scripts\python -m pip install "django"

# create the Django project (already created in this repo as `project_blog`)
.\venv\Scripts\python -m django startproject project_blog .

# run initial migrations
.\venv\Scripts\python manage.py migrate

# freeze installed packages
.\venv\Scripts\python -m pip freeze > requirements.txt

# start the development server
.\venv\Scripts\python manage.py runserver
```

Quick setup (Command Prompt)

```bat
py -3 -m venv venv
venv\Scripts\python -m pip install --upgrade pip
venv\Scripts\python -m pip install "django"
venv\Scripts\python -m django startproject project_blog .
venv\Scripts\python manage.py migrate
venv\Scripts\python -m pip freeze > requirements.txt
venv\Scripts\python manage.py runserver
```

Notes
- If PowerShell prevents activation due to execution policy, you can either run the commands using the venv Python executable (as shown above) or adjust the policy for the current session:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

- The default database is SQLite (`db.sqlite3`) created after migrations.
- Do not add Django apps inside this project unless requested.

If you want a different virtual environment name (for example `.venv`) or a pinned Django version, update `requirements.txt` or ask and I will adjust the setup.
