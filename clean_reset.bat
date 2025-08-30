@echo off
echo Cleaning up git history...

REM Remove all old commits and create one new one
git checkout --orphan temp_branch
git add .
git commit -m "Syntaxis Upload"

REM Delete the old main branch and rename temp to main
git branch -D main
git branch -m main

echo Done! Now force push with: git push origin main --force
pause

