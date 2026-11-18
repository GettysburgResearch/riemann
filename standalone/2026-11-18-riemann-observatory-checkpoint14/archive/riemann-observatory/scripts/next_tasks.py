#!/usr/bin/env python3
"""Show unfinished work, including live and review-pending tasks."""
import json
from pathlib import Path
r=Path(__file__).resolve().parents[1]
a=[json.loads(line) for line in (r/'corpus/research_queue.jsonl').read_text().splitlines() if line.strip()]
for t in sorted(a,key=lambda x:(x['priority'],x['id'])):
 if not t['status'].startswith('completed'):
  print(f"{t['priority']:02d} {t['id']} [{t['status']}] {t['title']}\n   {t['next_action']}\n   Sources: {t['sources']}")
