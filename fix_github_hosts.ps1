# fix_github_hosts.ps1
# Removes the leftover Steam++ (Watt Toolkit) block from the Windows hosts file.
# Those entries redirect github.com and 40+ other domains to 127.0.0.1,
# which breaks all GitHub access once Steam++ is not running.

$ErrorActionPreference = 'Stop'
$hostsPath = Join-Path $env:SystemRoot 'System32\drivers\etc\hosts'

# ---------- 1. require administrator ----------
$identity  = [Security.Principal.WindowsIdentity]::GetCurrent()
$principal = New-Object Security.Principal.WindowsPrincipal($identity)
if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "ERROR: administrator rights are required." -ForegroundColor Red
    exit 1
}

Write-Host "Windows hosts file: $hostsPath"
Write-Host ""

# ---------- 2. backup ----------
$stamp  = Get-Date -Format 'yyyyMMdd_HHmmss'
$backup = "$hostsPath.backup_$stamp"
Copy-Item $hostsPath $backup -Force
Write-Host "[1/4] Backup created: $backup"

# ---------- 3. remove the Steam++ block ----------
$lines    = Get-Content $hostsPath
$result   = New-Object System.Collections.Generic.List[string]
$skipping = $false
$removed  = 0

foreach ($line in $lines) {
    if ($line -match 'Steam\+\+\s*Start') { $skipping = $true;  $removed++; continue }
    if ($line -match 'Steam\+\+\s*End')   { $skipping = $false; $removed++; continue }
    if ($skipping)                        { $removed++; continue }
    $result.Add($line)
}

Set-Content -Path $hostsPath -Value $result -Encoding ASCII
Write-Host "[2/4] Removed $removed lines."

# ---------- 4. flush DNS ----------
ipconfig /flushdns | Out-Null
Write-Host "[3/4] DNS cache flushed."

# ---------- 5. verify ----------
Start-Sleep -Seconds 1
$ip = (Resolve-DnsName github.com -Type A -ErrorAction SilentlyContinue |
        Where-Object { $_.IPAddress } | Select-Object -First 1).IPAddress

Write-Host "[4/4] github.com now resolves to: $ip"
Write-Host ""

if ($ip -eq '127.0.0.1' -or [string]::IsNullOrWhiteSpace($ip)) {
    Write-Host "WARNING: still not resolved correctly." -ForegroundColor Yellow
    Write-Host "There may be another hosts entry or a DNS problem." -ForegroundColor Yellow
    exit 2
}

Write-Host "SUCCESS - GitHub domains are reachable again." -ForegroundColor Green
Write-Host "You can now run:  git push"
exit 0
