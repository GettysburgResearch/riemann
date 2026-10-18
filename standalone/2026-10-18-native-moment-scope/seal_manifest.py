"""Explicitly seal the final local payload. Never run implicitly during verification."""
import argparse
import json
from pathlib import Path

from verify_manifest import identity


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', required=True)
    parser.parse_args()
    here = Path(__file__).resolve().parent
    files = {p.name: identity(p.read_bytes()) for p in sorted(here.iterdir())
             if p.is_file() and p.name != 'MANIFEST.json'}
    manifest = {'schema_version': 1,
                'base_commit': 'bf845aa1d9d06b0ce62440edc5726de997a888db',
                'status': 'PROPOSED mathematics; finite evidence only', 'files': files}
    (here/'MANIFEST.json').write_text(json.dumps(manifest, sort_keys=True, indent=2)+'\n',
                                     encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
