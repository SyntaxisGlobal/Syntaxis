@echo off
echo Creating clean August history...

git checkout --orphan clean_august
git rm -rf .

git add README.md
git commit -m "Syntaxis Upload" --date="2025-08-01T10:00:00"

git add espanol/
git commit -m "Syntaxis Upload" --date="2025-08-05T14:30:00"

git add francais/
git commit -m "Syntaxis Upload" --date="2025-08-10T16:45:00"

git add .
git commit -m "Syntaxis Upload" --date="2025-08-15T11:20:00"

echo Done! Now you can force push this branch.
pause

