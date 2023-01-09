# Schedule a Python script with GitHub Actions

> Summary

This example shows how to run a Python script as cron job with GitHub Actions. It calls an API once a day (could be any schedule you want), logs the response in `status.log`, and automatically pushes the changes to this repo.

- Implement your script in `main.py`
- Inspect and configure cron job in GitHub Action `.github/workflows/actions.yml`
- It can install and use third party packages from `requirements.txt`
- Secret environment variables can be used. Set secrets in Settings/Secrets/Actions -> 'New repository secret'. Use the same secret name inside `actions.yml` and `main.py`

> Python version: code tested for Python version 3.7.6

> Venv shortcuts
- Create environment `python -m venv venv`
- Activate environment `venv\Scripts\activate`
- Install from file `pip install -r requirements.txt`  
- Freeze to file `pip freeze -> requirements.txt`
- Deactivate `exit`

> Tutorial: https://www.youtube.com/watch?v=PaGp7Vi5gfM