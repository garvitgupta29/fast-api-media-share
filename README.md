### This shows a project where people can share and view media.

To run this project without issues:
* Add imagekit.io private key in .env file.
* Change secret value if you want in users.py file.
* Run the following commands in two terminals:
  * uv run main.py
  * uv run streamlit run frontend.py

Used command below to avoid mistakenly pushing the changes to github for .env file.
git update-index --skip-worktree .env 
(In case if we want to rollback this change: git update-index --no-skip-worktree .env)