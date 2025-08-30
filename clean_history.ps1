Write-Host "Cleaning git history..."

# Create new orphan branch
git checkout --orphan temp_branch

# Add all files
git add .

# Create single commit
git commit -m "Syntaxis Upload"

# Delete old main branch
git branch -D main

# Rename temp branch to main
git branch -m main

Write-Host "Done! Now force push with: git push origin main --force"

