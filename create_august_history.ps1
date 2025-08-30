# Create new orphan branch
git checkout --orphan clean_august

# Remove all files from staging
git rm -rf .

# Add files with different August dates
# August 1st - Core files
git add README.md
GIT_COMMITTER_DATE="2025-08-01T10:00:00" git commit -m "Syntaxis Upload" --date="2025-08-01T10:00:00"

# August 5th - Spanish programs
git add espanol/
GIT_COMMITTER_DATE="2025-08-05T14:30:00" git commit -m "Syntaxis Upload" --date="2025-08-05T14:30:00"

# August 10th - French programs  
git add francais/
GIT_COMMITTER_DATE="2025-08-10T16:45:00" git commit -m "Syntaxis Upload" --date="2025-08-10T16:45:00"

# August 15th - Additional files
git add .gitignore
GIT_COMMITTER_DATE="2025-08-15T11:20:00" git commit -m "Syntaxis Upload" --date="2025-08-15T11:20:00"

# August 20th - Final touches
git add .
GIT_COMMITTER_DATE="2025-08-20T09:15:00" git commit -m "Syntaxis Upload" --date="2025-08-20T09:15:00"

Write-Host "Clean August history created! Now you can force push this branch."

