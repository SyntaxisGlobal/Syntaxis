@echo off
echo Starting clean git history creation...

REM from a clean working tree on main
git fetch origin
git checkout main

REM create a new history with the same files
git checkout --orphan fresh-start
git add -A
git commit -m "Syntaxis Upload"

REM replace main with this new, 1-commit history
git branch -D main
git branch -m main
git push -f origin main

echo Done! Clean history created.
pause

