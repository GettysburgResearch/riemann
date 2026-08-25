$ErrorActionPreference = 'Stop'
$auditDir = Split-Path -Parent $PSScriptRoot
$utf8NoBom = [Text.UTF8Encoding]::new($false)

$combinedNames = @(
  'COMBINED_AXIOM_AUDIT.tsv',
  'COMBINED_BUILD_REPORT.md',
  'COMBINED_MERGE_CONFLICTS.tsv',
  'COMBINED_REGISTRY_REPORT.md'
)
$combinedLines = foreach ($name in $combinedNames) {
  $path = Join-Path $auditDir $name
  if (-not (Test-Path -LiteralPath $path)) { throw "missing combined evidence: $name" }
  $hash = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
  "$hash  $name"
}
[IO.File]::WriteAllText(
  (Join-Path $auditDir 'COMBINED_REHEARSAL_SHA256SUMS'),
  (($combinedLines -join "`n") + "`n"),
  $utf8NoBom
)

$allLines = Get-ChildItem -LiteralPath $auditDir -File -Recurse |
  Where-Object { $_.Name -ne 'SHA256SUMS' } |
  Sort-Object FullName |
  ForEach-Object {
    $relative = [IO.Path]::GetRelativePath($auditDir, $_.FullName).Replace('\', '/')
    $hash = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    "$hash  $relative"
  }
[IO.File]::WriteAllText(
  (Join-Path $auditDir 'SHA256SUMS'),
  (($allLines -join "`n") + "`n"),
  $utf8NoBom
)
