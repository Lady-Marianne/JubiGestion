@echo off
cd /d "%~dp0"
call jubi_gestion\Scripts\activate.bat
python app.py
pause