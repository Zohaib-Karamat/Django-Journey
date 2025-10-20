# Django Journey

This repository documents my Django learning journey. The repository root (this folder) is the main workspace for Django work. It may contain one or more Django projects and many small tasks or exercises. Each task/project should be self-contained and documented so the repo doubles as a learning diary.

Important clarification: the folder `practice_project/` in this workspace is a specific task/project inside the repo — it is not the repository root project. The repository root is the primary workspace and may host multiple other tasks and projects.

## Recommended repository layout

Example layout you can follow as this repo grows:

- / (repo root) — primary Django workspace (contains `manage.py`, project-level settings if this is a Django project)
- /practice_project/ — one specific task or mini-project (examples, exercises, or a single Django app)
- /projects/ — (optional) collect additional tasks/projects here, e.g. `projects/auth-demo`, `projects/api-demo`
- /templates/ — shared templates used by demo tasks
- /db.sqlite3 — local development database (consider removing from VCS for public repos)
- /.venv/ or /venv/ — local virtual environment (do not commit)

Each task folder should ideally contain its own small README describing the task's purpose and how to run it.

## How this repo is organized now

- `practice_project/` — current example task included with the workspace. Treat this as one of many possible tasks.
- `templates/` — example templates used by tasks.

If you prefer to make each task a standalone Django project, use `projects/` and give each project its own folder and README.

## How to run (Windows - cmd.exe)

These steps assume the repository root contains the Django project you want to run (if the runnable Django project lives inside a subfolder, `cd` there first).

1. Create and activate a virtual environment (recommended):

```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies. If you have a `requirements.txt` at the repo root, use it. Otherwise install Django for now:

```cmd
pip install -r requirements.txt
# or, if you don't have requirements.txt
pip install django
```

3. If the Django project is in a subfolder (for example `practice_project/`) change into that folder before running management commands:

```cmd
cd practice_project
```

4. Run migrations (creates local SQLite schema):

```cmd
python manage.py migrate
```

5. (Optional) Create a superuser for the admin site:

```cmd
python manage.py createsuperuser
```

6. Run the development server:

```cmd
python manage.py runserver
```

7. Open your browser and visit http://127.0.0.1:8000/ (or the URL shown in the terminal).

## Adding a new task or project

- Create a new folder under `projects/` (recommended) or at the repo root for a larger project.
- Add a `README.md` inside that folder describing the task, routes, and how to run it.
- If the task requires unique dependencies, either document them in the per-project README or use a shared `requirements.txt` at the repo root.

Per-task README template (small):

```
Project: <short name>
Purpose: <what you'll learn/do>
How to run:
	1. cd into the folder
	2. activate venv
	3. pip install -r requirements.txt
	4. python manage.py migrate
	5. python manage.py runserver
```

## Version control & housekeeping

- Do not commit your virtual environment or local SQLite database for public repos. Add a `.gitignore` with at least:

```
# Virtual env
.venv/
venv/

# Python cache
__pycache__/

# SQLite DB
db.sqlite3
```

- Add `requirements.txt` (run `pip freeze > requirements.txt`) to lock dependencies.

## Suggested next steps

- Add `requirements.txt` at the repo root.
- Add a `.gitignore` to exclude `.venv/`, `db.sqlite3`, and other local artifacts.
- Add per-project `README.md` files under `practice_project/` and any new folders under `projects/`.
- Add a `CONTRIBUTING.md` if you plan to accept contributions or follow a consistent workflow.
- Add tests and a lightweight CI workflow (GitHub Actions) to run them on push.

---

This README is a short reference for organizing and running the projects in this workspace. If you'd like, I can:

- create a `.gitignore` and `requirements.txt` now
- add a `projects/` folder and move `practice_project/` there (or leave it where it is)
- create a per-project README template and add it to `practice_project/`

Tell me which of those you'd like me to do next.
