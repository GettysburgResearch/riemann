#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
echo '0825f3949f4100c78d1723e2a5c81c6ba451ee65243801cca9d0ea598d6ad21d  t97701-c4mbi67-critical-core.pdf' | sha256sum -c -
python /home/oai/skills/pdfs/scripts/pdf_preflight.py t97701-c4mbi67-critical-core.pdf > PDF_PREFLIGHT.txt
python /home/oai/skills/pdfs/scripts/pdf_inspect.py t97701-c4mbi67-critical-core.pdf > PDF_INSPECT.txt
