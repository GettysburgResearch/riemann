"""Delivery integrity checks, not a source quadrature or mathematical proof."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    certificates = []
    for name in ('dimer-certificate.json', 'dimer-certificate-mesh160.json'):
        data = json.loads((HERE / 'ising-computation' / name).read_text())
        radius = F(data['radius'])
        beta, contraction = F(data['beta_upper']), F(data['contraction_upper'])
        require(beta + contraction * radius < radius, name + ': contraction')
        require(beta < F('7.63e-22'), name + ': residual display bound')
        require(contraction < F('1.252e-7'), name + ': contraction display bound')
        lo, hi = map(F, data['degree_ten_standardized_mismatch'])
        require(F('.03321148056') < lo < hi < F('.03321163717'),
                name + ': tenth-moment display bounds')
        require(not data['all_order_realization_proved'], 'all-order scope')
        require(not data['positive_background_q_radius_certified'], 'q scope')
        certificates.append(data)
    require(certificates[0]['centers'] == certificates[1]['centers'], 'same centers')
    require(certificates[0]['radius'] == certificates[1]['radius'], 'same radius')

    provenance = json.loads((HERE / 'ising-computation' /
                             'predecessor-provenance.json').read_text())
    for entry in provenance['files']:
        path = HERE / 'ising-computation' / 'predecessor' / Path(entry['path']).name
        require(hashlib.sha256(path.read_bytes()).hexdigest() == entry['sha256'],
                'copied-source hash: ' + path.name)

    files = sorted(p for p in HERE.rglob('*') if p.is_file()
                   and '__pycache__' not in p.parts
                   and p.name not in ('MANIFEST.json', 'pr-inventory.json'))
    links = 0
    for path in files:
        if path.suffix != '.md':
            continue
        content = path.read_text(encoding='utf-8')
        require(all(ord(c) >= 32 or c in '\n\r\t' for c in content),
                'control character: ' + path.name)
        for target in re.findall(r'\]\(([^\s)]+)\)', content):
            if target.startswith(('https://', 'http://', '#')):
                continue
            target = target.split('#')[0].strip('<>')
            require((path.parent / target).exists(),
                    'local link: ' + str(path.relative_to(HERE)) + ' -> ' + target)
            links += 1
    manifest = {
        'scope': 'Delivery integrity only; no mathematical theorem certified.',
        'saved_exact_contraction_receipts_checked': 2,
        'copied_source_hashes_checked': len(provenance['files']),
        'local_markdown_links_checked': links,
        'files': [{'path': str(p.relative_to(HERE)).replace('\\', '/'),
                   'bytes': p.stat().st_size,
                   'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                  for p in files],
    }
    (HERE / 'MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n',
                                       encoding='utf-8')
    print(json.dumps({k: v for k, v in manifest.items() if k != 'files'}))
    print(f'Hashed {len(files)} delivery files.')


if __name__ == '__main__':
    main()
