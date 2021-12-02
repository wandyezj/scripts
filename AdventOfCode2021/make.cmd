setlocal
set n=%1
if not defined n (
    echo usage make.cmd number
    goto :eof
)

echo. > %n%.data.sample.txt
echo. > %n%.data.txt
echo. > %n%.puzzle.txt
echo. > %n%.py