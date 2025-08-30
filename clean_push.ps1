Write-Host "Setting up new repository..."

# Update remote to new repo
git remote set-url origin https://github.com/SyntaxisGlobal/Syntaxis.git

# Create new orphan branch with clean history
git checkout --orphan clean_main
git add .

# Commit with correct message
git commit -m "Syntaxis Upload"

# Delete old main branch and rename
git branch -D main
git branch -m main

# Force push to new repo
git push -f origin main

Write-Host "Done! Clean repository pushed to new repo."

