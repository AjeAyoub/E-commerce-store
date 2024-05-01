@echo off
cd .\E-commerce-store
start cmd /c "python manage.py runserver >nul 2>&1"
start http://127.0.0.1:8000/

