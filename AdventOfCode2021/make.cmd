@setlocal
@echo off

set THISDIR=%~dp0
set THISDIR=%THISDIR:~,-1%

call %THISDIR%\session.cmd

python.exe %THISDIR%\make.py %day%