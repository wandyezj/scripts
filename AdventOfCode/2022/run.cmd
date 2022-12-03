@setlocal
@echo off

REM runs the current session day python script

set THISDIR=%~dp0
set THISDIR=%THISDIR:~,-1%

call %THISDIR%\session.cmd

set name=%day%.py

set switch=%1

python.exe %THISDIR%\%name% %*