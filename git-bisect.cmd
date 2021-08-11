@setlocal
@echo off

set THISDIR=%~dp0
set THISDIR=%THISDIR:~,-1%
set SCRIPT=%0
rem change to repository
cd test-git

set command=%1



if "%command%"=="" (
    rem NOTE set this hash
    set last_good_commit_hash=hash

    echo "bisect - start"

    rem start bisect
    git bisect start

    rem label current commit as bad
    git bisect bad

    rem label specific previous commit as good
    git bisect good %last_good_commit_hash% 

    rem run test and mark git bisect good or git bisect bad

    git bisect run %SCRIPT% %THISDIR% test

    
    rem reset to original state
    git bisect reset
    
    echo "bisect - complete"
)

if "%command%"=="test" (
    echo "TEST"
    
    rem return
    rem 125 - code is not testable
    rem 0 - code is good
    rem 1 - code is bad
    
    rem Test script to determine if code is good or bad
    
    
    exit /b 125
)