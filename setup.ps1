$VENV_DIRECTORY = "venv"
if (-Not $(Test-Path $VENV_DIRECTORY)) {
    Write-Host "Creating environment VENV_DIRECTORY"
    python.exe -m venv $VENV_DIRECTORY
} else {
    Write-Host "venv already exists"
}
.\venv\Scripts\activate.ps1