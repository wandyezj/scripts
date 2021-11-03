@echo OFF
setlocal EnableDelayedExpansion
::Note: ability to output to console with formatting is from https://stackoverflow.com/a/38617204/678505

echo.
echo check that minimum required npm version is present.
echo.

:: Configure the minimum required NPM version
set minimum_required_version=8.1.0
set minimum_required_version_major=8
set minimum_required_version_minor=1

::variables to assess the installed node version
set version_major=
set version_minor=
set version_revision=

:: Get the result of the command and parse it into the version parts.
FOR /F "tokens=1,2,3 delims=." %%i IN ('npm --version') DO (
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


echo.
echo NPM Version:
echo.
echo     Current Installed: %version_major%.%version_minor%.%version_revision%
echo.
echo     Minimum Required:  %minimum_required_version%
echo.

:: debugging variables
@REM echo Major: [%version_major%]
@REM echo Minor: [%version_minor%]
@REM echo Revision: [%version_revision%]

if %version_major% LSS %minimum_required_version_major% (
    goto :upgrade
)

if %version_minor% LSS %minimum_required_version_minor% (
    goto :upgrade
)



echo.
echo Minimum Required npm version is present.
echo.

exit /B 0

:upgrade
echo [45m Please upgrade the npm version on your machine [0m
echo.
echo Please install the latest node LTS version from: https://nodejs.org/en/
exit /B 1

:not_installed
echo.
echo [45m NPM is not installed.[0m
echo.
echo Please install a Node LTS version from: https://nodejs.org/en/
echo.
echo. Make sure you install a node LTS version greater than: %node_minimum_required_version%
echo.
echo Recommended install: Node %node_minimum_required_version_major% LTS
echo.

exit /B 1
