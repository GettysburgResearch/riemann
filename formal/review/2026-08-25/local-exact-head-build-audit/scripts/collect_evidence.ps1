param(
  [Parameter(Mandatory = $true)]
  [string] $RawRoot
)

$ErrorActionPreference = 'Stop'
$auditDir = Split-Path -Parent $PSScriptRoot
$outputs = Join-Path $auditDir 'outputs'
$patches = Join-Path $auditDir 'patches'
New-Item -ItemType Directory -Force -Path $outputs | Out-Null
New-Item -ItemType Directory -Force -Path $patches | Out-Null

foreach ($reviewer in @('A', 'B', 'C')) {
  foreach ($suffix in @('COMMANDS.tsv', 'AGENT_SUMMARY.md')) {
    $source = Join-Path $RawRoot "${reviewer}_${suffix}"
    if (-not (Test-Path -LiteralPath $source)) {
      throw "missing required agent evidence: $source"
    }
    Copy-Item -LiteralPath $source -Destination (Join-Path $outputs "${reviewer}_${suffix}") -Force
  }
}

Get-ChildItem -LiteralPath (Join-Path $RawRoot 'patches') -File -Filter '*.patch' |
  ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $patches $_.Name) -Force
  }

$selectors = @{
  A = '^(10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|99).*\.log$'
  B = '^(11|12|13|14|15|16|17|20|21|22|23|24|25|3[0-5]|4[1-9]|5[0-7]).*\.log$'
  C = '^(001|021|023|033|034|036|038|039|040|041|042|043|044|045|050|051|052|053|054|055|056|057|060|061|062|063|064|065|066|067|068|069).*\.log$'
}

foreach ($reviewer in @('A', 'B', 'C')) {
  $sourceDirectory = Join-Path $RawRoot "raw/$reviewer"
  Get-ChildItem -LiteralPath $sourceDirectory -File |
    Where-Object { $_.Name -match $selectors[$reviewer] } |
    ForEach-Object {
      Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $outputs "${reviewer}_$($_.Name)") -Force
    }
}

$index = [System.Collections.Generic.List[string]]::new()
$index.Add("reviewer`trelative_path`tbytes`tsha256")
foreach ($reviewer in @('A', 'B', 'C')) {
  $sourceDirectory = Join-Path $RawRoot "raw/$reviewer"
  Get-ChildItem -LiteralPath $sourceDirectory -File -Recurse |
    Sort-Object FullName |
    ForEach-Object {
      $relative = [IO.Path]::GetRelativePath($RawRoot, $_.FullName).Replace('\', '/')
      $hash = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
      $index.Add("$reviewer`t$relative`t$($_.Length)`t$hash")
    }
}

$utf8NoBom = [Text.UTF8Encoding]::new($false)
[IO.File]::WriteAllText(
  (Join-Path $auditDir 'RAW_LOG_INDEX.tsv'),
  (($index -join "`n") + "`n"),
  $utf8NoBom
)
