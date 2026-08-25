param(
  [Parameter(Mandatory = $true)]
  [ValidateSet('A', 'B', 'C')]
  [string] $Reviewer,

  [string] $LogDirectory = ''
)

$ErrorActionPreference = 'Stop'
$expectedHeads = @{
  A = '9ed8988218fd9c3e1da33bde81361262fc0aa747'
  B = '072b4dbd0e4e407728a59110eb4f7214e23f8f8d'
  C = 'b20ee9b3678e5d8fa32b04b156bc02cec782a97b'
}

foreach ($tool in @('git', 'lake', 'python3', 'bash')) {
  if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) {
    throw "required command is not on PATH: $tool"
  }
}

$repoRoot = (& git rev-parse --show-toplevel).Trim()
if ($LASTEXITCODE -ne 0) { throw 'not inside a Git worktree' }
$actualHead = (& git rev-parse HEAD).Trim()
if ($actualHead -ne $expectedHeads[$Reviewer]) {
  throw "Reviewer $Reviewer requires $($expectedHeads[$Reviewer]); found $actualHead"
}
$dirty = (& git status --porcelain=v1)
if ($LASTEXITCODE -ne 0 -or $dirty) {
  throw 'source worktree must be clean before the audit'
}

if (-not $LogDirectory) {
  $LogDirectory = Join-Path $repoRoot "audit-raw-$Reviewer"
}
New-Item -ItemType Directory -Force -Path $LogDirectory | Out-Null
$formal = Join-Path $repoRoot 'formal'
Set-Location $formal

$rows = [System.Collections.Generic.List[object]]::new()
function Invoke-AuditStep {
  param(
    [string] $Id,
    [string] $Executable,
    [string[]] $Arguments
  )
  $safeId = $Id -replace '[^A-Za-z0-9_.-]', '_'
  $log = Join-Path $LogDirectory "$safeId.log"
  $display = @($Executable) + $Arguments -join ' '
  $started = Get-Date
  $previousPreference = $ErrorActionPreference
  $ErrorActionPreference = 'Continue'
  & $Executable @Arguments 2>&1 | Tee-Object -FilePath $log
  $code = $LASTEXITCODE
  $ErrorActionPreference = $previousPreference
  "EXIT_CODE=$code" | Out-File -FilePath $log -Append -Encoding utf8NoBOM
  $ended = Get-Date
  $rows.Add([pscustomobject]@{
      reviewer = $Reviewer
      id = $Id
      command = $display
      exit_code = $code
      started_at = $started.ToString('o')
      ended_at = $ended.ToString('o')
      log = [IO.Path]::GetFileName($log)
    })
}

if ($Reviewer -eq 'C') {
  Invoke-AuditStep '000_run_c_repair_validation' 'bash' @('scripts/run_c_repair_validation.sh')
}

$common = @(
  @('010_cache_get', 'lake', @('exe', 'cache', 'get')),
  @('011_lake_build', 'lake', @('build')),
  @('012_generate_registry', 'python3', @('scripts/generate_registry.py')),
  @('013_validate_registry', 'python3', @('scripts/validate_registry.py')),
  @('014_verify_source_locks', 'python3', @('scripts/verify_source_locks.py')),
  @('015_validate_blueprint', 'python3', @('scripts/validate_blueprint.py')),
  @('016_check_no_sorry', 'bash', @('scripts/check_no_sorry.sh')),
  @('017_check_axioms', 'bash', @('scripts/check_axioms.sh'))
)
foreach ($step in $common) {
  Invoke-AuditStep $step[0] $step[1] $step[2]
}

switch ($Reviewer) {
  'A' {
    Invoke-AuditStep '020_build_Challenge_MellinAPI' 'lake' @('build', 'Challenge.MellinAPI')
    Invoke-AuditStep '021_build_Solution_MellinAPI' 'lake' @('build', 'Solution.MellinAPI')
    Invoke-AuditStep '022_validation_replay' 'bash' @('RiemannFormal/Analysis/replay/run_validation.sh')
    Invoke-AuditStep '023_axioms_Analysis' 'lake' @('env', 'lean', 'RiemannFormal/Analysis/AxiomAudit.lean')
    Invoke-AuditStep '024_axioms_MellinAPI' 'lake' @('env', 'lean', 'comparator/PrintAxioms/MellinAPI.lean')
    Invoke-AuditStep '025_axioms_RH' 'lake' @('env', 'lean', 'comparator/PrintAxioms/RH.lean')
  }
  'B' {
    Invoke-AuditStep '020_build_Challenge_ArithmeticRows23' 'lake' @('build', 'Challenge.ArithmeticRows23')
    Invoke-AuditStep '021_build_Solution_ArithmeticRows23' 'lake' @('build', 'Solution.ArithmeticRows23')
    Invoke-AuditStep '022_build_Challenge_FixedDetectorFiveThree' 'lake' @('build', 'Challenge.FixedDetectorFiveThree')
    Invoke-AuditStep '023_build_Solution_FixedDetectorFiveThree' 'lake' @('build', 'Solution.FixedDetectorFiveThree')
    Invoke-AuditStep '024_axioms_Arithmetic' 'lake' @('env', 'lean', 'RiemannFormal/Arithmetic/AxiomAudit.lean')
    Invoke-AuditStep '025_axioms_ArithmeticFixedRows' 'lake' @('env', 'lean', 'comparator/PrintAxioms/ArithmeticFixedRows.lean')
  }
  'C' {
    foreach ($topic in @('XiPickThreeNode', 'OperatorPositiveSchurRescue', 'XiPickOrderThreeConditional')) {
      Invoke-AuditStep "020_build_Challenge_$topic" 'lake' @('build', "Challenge.$topic")
      Invoke-AuditStep "021_build_Solution_$topic" 'lake' @('build', "Solution.$topic")
    }
    Invoke-AuditStep '030_verify_declaration_map' 'python3' @('scripts/verify_declaration_map.py')
    Invoke-AuditStep '031_check_statement_sources' 'python3' @('scripts/check_statement_sources.py')
    foreach ($module in @('OperatorPositiveSchurRescue', 'XiPickOrderThreeConditional', 'XiPickThreeNode')) {
      Invoke-AuditStep "032_axioms_$module" 'lake' @('env', 'lean', "comparator/PrintAxioms/$module.lean")
    }
  }
}

$rows | Export-Csv -Path (Join-Path $LogDirectory 'COMMANDS.tsv') -Delimiter "`t" -NoTypeInformation -Encoding utf8NoBOM
(& git -C $repoRoot status --porcelain=v1) | Out-File -FilePath (Join-Path $LogDirectory 'FINAL_GIT_STATUS.txt') -Encoding utf8NoBOM
if ($rows.Where({ $_.exit_code -ne 0 }).Count -gt 0) { exit 1 }
