Write-Host "Starting clean August history creation..."

# Create new branch
git checkout --orphan clean_august

# Remove all files
git rm -rf .

# Add README first
git add README.md
git commit -m "Syntaxis Upload" --date="2025-08-01T10:00:00"

# Add Spanish programs
git add espanol/
git commit -m "Syntaxis Upload" --date="2025-08-05T14:30:00"

# Add French programs
git add francais/
git commit -m "Syntaxis Upload" --date="2025-08-10T16:45:00"

# Add remaining files
git add .
git commit -m "Syntaxis Upload" --date="2025-08-15T11:20:00"

Write-Host "Done! Now you can force push this branch."

