"""Authenticate a separately downloaded CT v2 TeX source and locate contracts.

Reads untrusted TeX as text only. Does not compile or execute it. A matching
hash and located formula are provenance checks, not a proof of the formula.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

from ideals import require

SOURCE_URL = 'https://hexagonmath.org/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex'
SOURCE_SHA256 = 'f54808ad0f967b5429c7ac30d7b27ff25671e02d7fb43cf753b2b826c9d35df4'
LABELS = {
    'thm:dedekind': ('theorem', 'Printed all-field 31/32 zero-free input'),
    'cor:Hecke': ('corollary', 'Printed finite-order Hecke 31/32 zero-free input'),
    'eq:B': ('equation', 'Original theta source; full c,n sum and Gaussian'),
    'eq:reflection': ('proposition', 'Unrestricted reflection and full profile contract'),
    'eq:separated-reflection': ('equation', 'Separated ideal source and norm powers'),
    'eq:beta': ('equation', 'All ramified local majorant branches'),
    'eq:quadratic-sieve': ('equation', 'Both squarefree indices and Q2 norm'),
    'eq:localized-fourier-bound': ('equation', 'Two-derivative localized Fourier mass'),
    'eq:moment': ('proposition', 'Printed second moment at its fixed long support'),
}


def audit(path):
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    require(digest == SOURCE_SHA256, 'CT source bytes do not match the pinned v2 source.')
    source = data.decode('utf-8')
    contracts = []
    for label, (environment, scope) in LABELS.items():
        pattern = r'\\begin\{'+environment+r'\}(.*?)\\end\{'+environment+r'\}'
        blocks = [match for match in re.finditer(pattern, source, re.S)
                  if r'\label{'+label+'}' in match.group(0)]
        require(len(blocks) == 1, 'Missing or duplicated CT contract: '+label)
        block = blocks[0]
        contracts.append({'label': label, 'environment': environment, 'scope': scope,
                          'first_line': source.count('\n', 0, block.start())+1,
                          'last_line': source.count('\n', 0, block.end())+1,
                          'utf8_block_sha256': hashlib.sha256(block.group(0).encode()).hexdigest()})
    return {'status': 'AUTHENTICATED SOURCE INTERFACE; not analytic certification',
            'source_url': SOURCE_URL, 'version': '2610.00200v2',
            'source_bytes': len(data), 'source_sha256': digest,
            'contracts': contracts,
            'boundary': 'The handwritten comparison is in CT_INTERFACE_REVIEW.md. No Lean build or reconstruction of Kazhdan-Patterson/OpenAI local theory is claimed.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(audit(args.source), sort_keys=True, indent=2)+'\n'
    if args.output:
        args.output.write_text(text, encoding='utf-8', newline='\n')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
