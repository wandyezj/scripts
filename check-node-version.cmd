@echo OFF
SETLOCAL EnableDelayedExpansion
::Note: ability to output to console with formatting is from https://stackoverflow.com/a/38617204/678505

echo.
echo check that minimum required node version is present.
echo.

:: Configure the minimum required Node version
set minimum_required_version=v16.13.0
set minimum_required_version_major=16
set minimum_required_version_minor=13

::variables to assess the installed node version
set version_major=
set version_minor=
set version_revision=

:: Get the result of the command and parse it into the version parts.
FOR /F "tokens=1,2,3 delims=." %%i IN ('node -v') DO (
    set version_major=%%i
    set version_minor=%%j
    set version_revision=%%k
)

:: It's possible no version was installed in which case the version variables will not be defined.
if not defined version_major (
    goto :not_installed
)

if not defined version_minor (
    goto :not_installed
)

if not defined version_revision (
    goto :not_installed
)


:: Clean up v prefix from the major version
set version_major=%version_major:~1%

echo.
echo Node Version:
echo.
echo     Current Installed: v%version_major%.%version_minor%.%version_revision%
echo.
echo     Minimum Required:  %minimum_required_version%
echo.

:: debugging variables
@REM echo Major: [%version_major%]
@REM echo Minor: [%version_minor%]
@REM echo Revision: [%version_revision%]

IF %version_major% LSS %minimum_required_version_major% (
    goto :upgrade
)

IF %version_minor% LSS %minimum_required_version_minor% (
    goto :upgrade
)


echo.
echo Minimum Required node version is present.
echo.
exit /B 0

:upgrade
echo [45m Please upgrade the node version on your machine [0m
echo.
echo Please install the latest LTS node version from: https://nodejs.org/en/
exit /B 1


:not_installed
echo.
echo [45m Node is not installed.[0m
echo.
echo Please install the latest Node LTS version: https://nodejs.org/en/
echo.
echo. Make sure you install a node LTS version greater than: %minimum_required_version%
echo.
echo Recommended install: Node %minimum_required_version_major% LTS
echo.
exit /B 1