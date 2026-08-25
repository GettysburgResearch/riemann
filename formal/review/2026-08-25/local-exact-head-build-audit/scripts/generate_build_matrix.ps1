$ErrorActionPreference = 'Stop'
$auditDir = Split-Path -Parent $PSScriptRoot
$outputs = Join-Path $auditDir 'outputs'
$lines = [System.Collections.Generic.List[string]]::new()
$lines.Add("reviewer`tsequence`tscope`tworking_directory`tcommand`texit_code`tclassification`tlog`tfirst_result")

foreach ($reviewer in @('A', 'B', 'C')) {
  $ledger = Join-Path $outputs "${reviewer}_COMMANDS.tsv"
  if (-not (Test-Path -LiteralPath $ledger)) { throw "missing command ledger: $ledger" }
  Import-Csv -LiteralPath $ledger -Delimiter "`t" |
    Where-Object { $_.exit_code -ne 'NA' } |
    ForEach-Object {
    $scope = if ($_.PSObject.Properties.Name -contains 'scope') {
      $_.scope
    } else {
      'exact-head-or-diagnostic'
    }
    $firstResult = if ($_.PSObject.Properties.Name -contains 'first_result') {
      $_.first_result
    } else {
      $_.first_causal_result
    }
    $values = @(
      $reviewer,
      $_.sequence,
      $scope,
      $_.working_directory,
      $_.command,
      $_.exit_code,
      $_.classification,
      $_.log,
      $firstResult
    ) | ForEach-Object { ("$_" -replace "`t", ' ' -replace "`r?`n", ' ') }
    $lines.Add($values -join "`t")
  }
}

$utf8NoBom = [Text.UTF8Encoding]::new($false)
[IO.File]::WriteAllText(
  (Join-Path $auditDir 'LOCAL_BUILD_MATRIX.tsv'),
  (($lines -join "`n") + "`n"),
  $utf8NoBom
)
