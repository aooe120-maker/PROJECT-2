param(
    [switch]$OneFile
)

$ErrorActionPreference = 'Stop'

python -m pip install --upgrade pip wheel
python -m pip install pyinstaller pygame-ce

$args = @('-y', 'pyinstaller.spec')
if ($OneFile) { $args = @('--onefile') + $args }

pyinstaller @args

Write-Host "\nBuild complete. Output: dist\\DokiDoki\n"

