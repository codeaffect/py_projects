@echo off

set fn=%1
cd /d %~dp0

If "%1"=="" (
    echo "error"
) else ( 
    python createrepo.py %fn%    
)