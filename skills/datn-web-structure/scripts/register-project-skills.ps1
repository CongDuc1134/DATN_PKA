<#
.SYNOPSIS
Registers the canonical DATN skills for Codex, Antigravity, and Claude Code on Windows.
.DESCRIPTION
Run again after cloning DATN to a new location. Existing correct junctions are
kept; conflicting paths are reported and never replaced.
Can register for local project (.agents, .claude, .codex) and user global (~/.codex/skills, ~/.gemini/config/skills).
#>
[CmdletBinding()]
param(
    [switch]$Global
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$datnProjectRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..\..'))
$datnCanonicalRoot = Join-Path $datnProjectRoot 'skills'
if (-not (Test-Path -LiteralPath (Join-Path $datnProjectRoot 'AGENTS.md'))) {
    throw 'Expected a DATN project with AGENTS.md.'
}
$datnSkillFolders = @(Get-ChildItem -LiteralPath $datnCanonicalRoot -Directory |
    Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') })
if ($datnSkillFolders.Count -eq 0) {
    throw 'No canonical skills were found.'
}

# 1. Register for local project agent directories
foreach ($datnAgentName in @('.agents', '.claude', '.codex')) {
    $datnDiscoveryRoot = Join-Path $datnProjectRoot "$datnAgentName\skills"
    $null = New-Item -ItemType Directory -Path $datnDiscoveryRoot -Force
    foreach ($datnSkillFolder in $datnSkillFolders) {
        $datnTargetPath = [System.IO.Path]::GetFullPath($datnSkillFolder.FullName)
        $datnLinkPath = Join-Path $datnDiscoveryRoot $datnSkillFolder.Name
        if (-not $datnTargetPath.StartsWith($datnCanonicalRoot + '\', [System.StringComparison]::OrdinalIgnoreCase)) {
            throw "Skill target is outside the canonical folder: $datnTargetPath"
        }
        $datnExisting = Get-Item -LiteralPath $datnLinkPath -Force -ErrorAction SilentlyContinue
        if ($null -ne $datnExisting) {
            if ($datnExisting.LinkType -ne 'Junction') {
                throw "Existing registration is not a junction; refusing to replace: $datnLinkPath"
            }
            $datnExistingTargets = @($datnExisting.Target)
            if ($datnExistingTargets.Count -ne 1 -or
                -not [string]::Equals([System.IO.Path]::GetFullPath($datnExistingTargets[0]), $datnTargetPath, [System.StringComparison]::OrdinalIgnoreCase)) {
                throw "Existing junction points elsewhere; refusing to replace: $datnLinkPath"
            }
        } else {
            $null = New-Item -ItemType Junction -Path $datnLinkPath -Target $datnTargetPath
        }
        if (-not (Test-Path -LiteralPath (Join-Path $datnLinkPath 'SKILL.md'))) {
            throw "Registration is unreadable: $datnLinkPath"
        }
        Write-Output "$datnAgentName/skills/$($datnSkillFolder.Name) -> skills/$($datnSkillFolder.Name)"
    }
}

# 2. Ensure .agents/skills.json exists for Antigravity explicit discovery
$skillsJsonPath = Join-Path $datnProjectRoot '.agents\skills.json'
$skillsJsonContent = @'
{
  "entries": [
    {
      "path": "skills"
    }
  ]
}
'@
if (-not (Test-Path -LiteralPath $skillsJsonPath)) {
    Set-Content -LiteralPath $skillsJsonPath -Value $skillsJsonContent -Encoding UTF8
    Write-Output ".agents/skills.json created for Antigravity"
}

# 3. If -Global is specified, also register to user home directories for Codex and Antigravity
if ($Global) {
    $userProfile = [System.Environment]::GetFolderPath('UserProfile')
    $globalDestinations = @(
        (Join-Path $userProfile '.codex\skills'),
        (Join-Path $userProfile '.gemini\config\skills')
    )
    foreach ($gRoot in $globalDestinations) {
        $null = New-Item -ItemType Directory -Path $gRoot -Force
        foreach ($datnSkillFolder in $datnSkillFolders) {
            $datnTargetPath = [System.IO.Path]::GetFullPath($datnSkillFolder.FullName)
            $datnLinkPath = Join-Path $gRoot $datnSkillFolder.Name
            $datnExisting = Get-Item -LiteralPath $datnLinkPath -Force -ErrorAction SilentlyContinue
            if ($null -ne $datnExisting) {
                if ($datnExisting.LinkType -ne 'Junction') {
                    Write-Warning "Global path exists and is not a junction, skipping: $datnLinkPath"
                    continue
                }
            } else {
                $null = New-Item -ItemType Junction -Path $datnLinkPath -Target $datnTargetPath
            }
            Write-Output "Global: $gRoot\$($datnSkillFolder.Name) -> skills/$($datnSkillFolder.Name)"
        }
    }
}
