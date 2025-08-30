@echo off
echo Setting up new repository...

REM Update remote to new repo
git remote set-url origin https://github.com/SyntaxisGlobal/Syntaxis.git

REM Create new orphan branch with clean history
git checkout --orphan clean_main
git add .

REM Commit with correct message
git commit -m "Syntaxis Upload"

REM Delete old main branch and rename
git branch -D main
git branch -m main

REM Force push to new repo
git push -f origin main

echo Done! Clean repository pushed to new repo.
pause

