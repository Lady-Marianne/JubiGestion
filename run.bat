This batch file is used to run the JubiGestion application.
REM It activates the virtual environment and starts the application.

@echo off
cd /d "%~dp0"
call jubi_gestion\Scripts\activate.bat
python app.py
pause