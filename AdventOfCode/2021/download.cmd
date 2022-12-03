REM download input for a year day session
@setlocal
@echo off

set THISDIR=%~dp0
set THISDIR=%THISDIR:~,-1%

REM session.cmd sets variables
REM set day=
REM set year=
REM set session=
call %THISDIR%\session.cmd

python.exe %THISDIR%\download.py %year% %day% %session%