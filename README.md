# Test ADO Deployment

Small Flask + React demo. Contains:

- `main.py` - Flask app serving an API and static files from `frontend/dist`.
- `frontend/` - place for the Vite React app (not included yet in this repo).
- `.env` - local environment file (ignored by git).

How to push to GitHub

1) Create a new remote repo on GitHub (manual):
   - Go to https://github.com/new, enter a name and click Create repository.

   OR create it with the GitHub CLI:
   ```bash
   gh repo create <your-username>/<repo-name> --public --source=. --remote=origin
   ```

2) Push your code (if you haven't already initialized a git repo locally):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```

Notes
- Replace `<your-username>` and `<repo-name>` with your GitHub username and desired repo name.
- If you use SSH, use the SSH remote URL instead of HTTPS.

Extra Notes
https://docs.astral.sh/uv/getting-started/features/#python-versions
curl -LsSf https://astral.sh/uv/install.sh | sh
uv -V

uv init
source .venv/bin/activate
uv add <package name>

cd frontend
npm i
cd..
python main.py