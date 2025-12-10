cd .kiro
type nul > README.md  # Windows
echo "# Kiro folder for project configs" > README.md
cd ..
git add .
git commit -m "Add .kiro folder with README"
git push
