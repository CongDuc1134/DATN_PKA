<#
.SYNOPSIS
Registers the canonical DATN skills for Codex and Claude Code on Windows.
.DESCRIPTION
Run again after cloning DATN to a new location. Existing correct junctions are
kept; conflicting paths are reported and never replaced. No user-global setup.
#>
[CmdletBinding()]
param()

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

foreach ($datnAgentName in @('.agents', '.claude')) {
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
