$ErrorActionPreference = 'Stop'
$auditDir = Split-Path -Parent $PSScriptRoot
$utf8NoBom = [Text.UTF8Encoding]::new($false)
$textExtensions = @('.md', '.tsv', '.patch', '.ps1', '.log', '')

Get-ChildItem -LiteralPath $auditDir -File -Recurse |
  Where-Object { $textExtensions -contains $_.Extension } |
  ForEach-Object {
    $content = [IO.File]::ReadAllText($_.FullName)
    $normalized = $content.Replace("`r`n", "`n").Replace("`r", "`n")
    if ($normalized -ne $content) {
      [IO.File]::WriteAllText($_.FullName, $normalized, $utf8NoBom)
    }
  }
