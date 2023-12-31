$VENV_DIRECTORY = "venv"
if (-Not $(Test-Path $VENV_DIRECTORY)) {
    Write-Host "Creating environment VENV_DIRECTORY"
    python.exe -m venv $VENV_DIRECTORY
} else {
    Write-Host "venv already exists"
}

# Activate the virtual environment
.\venv\Scripts\Activate.ps1

# Install the requirements
pip install -r requirements.txt

# Setup session ID
$session_id = Read-Host -Prompt 'Enter session ID'
New-Item -Path Env:\AOC_SESSION -Value $session_id