#!/usr/bin/env python3
import json,sys
from pathlib import Path
r=Path(__file__).resolve().parents[1]
if len(sys.argv)!=2:raise SystemExit('Usage: python scripts/query_graph.py NODE_ID')
q=sys.argv[1]
for line in (r/'graphs/knowledge_graph.jsonl').read_text().splitlines():
 x=json.loads(line)
 if x.get('id')==q or x.get('from')==q or x.get('to')==q:print(json.dumps(x,ensure_ascii=False,indent=2))
