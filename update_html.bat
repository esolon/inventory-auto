@echo off

:: Wait for OneDrive to sync .xlsx updates
timeout /t 10 >nul

:: === Run Python HTML generator ===
cd "C:\Users\esolon\OneDrive - Boston Semi Equipment LLC\Github Projects\Inventory"
echo Running update_html.py...
"C:\Users\esolon\AppData\Local\Programs\Python\Python313\python.exe" update_html.py

:: === Git Commit and Push ===
echo Committing changes to GitHub...

git add .
git commit -m "✅ Auto-update via E-Watch export on %DATE% %TIME%"
git push origin main

pause