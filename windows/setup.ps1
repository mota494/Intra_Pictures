# Define colors
$Host.UI.RawUI.ForegroundColor = 'White'  # Default color

function Write-Color {
    param(
        [string]$Text,
        [string]$Color = 'White'
    )
    $oldColor = $Host.UI.RawUI.ForegroundColor
    $Host.UI.RawUI.ForegroundColor = $Color
    Write-Host $Text
    $Host.UI.RawUI.ForegroundColor = $oldColor
}

# Check if python3 is installed
try {
    $pythonVersion = & python3 --version 2>$null
    if (-not $?) {
        throw "Python3 not found"
    }
    Write-Color "Python is installed" "Green"
} catch {
    Write-Color "Python's not installed`nPlease install the latest version of python3 with your package manager" "Red"
    exit 1
}

# Run test.py
& python3 test.py
$lastExitCode = $LASTEXITCODE

switch ($lastExitCode) {
    0 {
        Write-Color "Every package necessary is installed" "Green"
    }
    30 {
        Write-Color "Both packages are missing" "Red"
        & pip3 install selenium
        & pip3 install beautifulsoup4
    }
    10 {
        Write-Color "Selenium is missing" "Red"
        & pip3 install selenium
    }
    20 {
        Write-Color "BeautifulSoup is missing" "Red"
        & pip3 install beautifulsoup4
    }
}

# Check if users.csv exists
$first_file = ".\users.csv"
if (Test-Path $first_file) {
    Write-Color "Found users.csv, compiling C program" "Green"
} else {
    Write-Color "No users.csv found" "Red"
    exit 1
}

# Compile and run C program
gcc main.c -o main.exe
if ($LASTEXITCODE -eq 0) {
    & .\main.exe
} else {
    Write-Color "Compilation failed" "Red"
    exit 1
}

# Run soup.py
& python3 soup.py

# Clean up
Remove-Item -Force .\users.csv, .\main.exe, .\output.csv -ErrorAction SilentlyContinue

Write-Color "Done" "Green"

