"""Copy authenticated pinned primitive arithmetic; Git operations are read-only."""
from pathlib import Path
import argparse,json
from source_provenance import (EXPECTED_SHA256, authenticate_bytes,
                               expected_receipt, find_repository, read_pinned_file)

HERE=Path(__file__).resolve().parent
DEST=HERE/'predecessor'

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--repo',type=Path,help='Git checkout containing the pinned #875 commit')
 args=parser.parse_args()
 repo=find_repository(args.repo)
 # Verify the entire incoming set before changing any copied source file.
 sources={name:authenticate_bytes(name,read_pinned_file(repo,name)) for name in EXPECTED_SHA256}
 DEST.mkdir(exist_ok=True)
 for name,raw in sources.items():
  (DEST/name).write_bytes(raw)
 (HERE/'predecessor-provenance.json').write_text(json.dumps(expected_receipt(),indent=2)+'\n',encoding='utf-8')
 print('Extracted four authenticated source files into this packet; no checkout, commit or fetch.')

if __name__=='__main__':main()
