@Rem run this file with cmd with command (while in this folder): compile_win10
@Rem runs pyinstaller to compile program, zip it and move it around
Rem XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Rem Starting
Rem XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ECHO OFF
SET appnamepre=thebookofthings
Rem XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

@Rem make pyinstaller with output in dist
COPY  forpyinstaller\main.spec ..
CD ..
pyinstaller main.spec
SET appname=%appnamepre%_win10
@Rem XCOPY  /S compile\forpyinstaller\launcher.bat dist

@Rem delete remake output game folder
@RD /S /Q dist\%appname%
MKDIR dist\%appname%
MKDIR dist\%appname%\code
ROBOCOPY /E /MOVE dist\code dist\%appname%\code 
XCOPY  /S compile\forpyinstaller\launcher.bat dist\%appname%

@Rem zip the folder (you need 7zip installed)
CD dist
"C:\Program Files\7-Zip\7z.exe" a -tzip %appname%.zip %appname%
@RD /S /Q %appname%
MOVE %appname%.zip ..\..

@Rem cleanup (move zip file along top of folder)
CD ..
DEL main.spec
@RD /S /Q build
@RD /S /Q dist
@RD /S /Q __pycache__

@Rem return to compile folder for next execution
CD compile


