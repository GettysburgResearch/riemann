#!/usr/bin/env python3
"""Verify a saved rational witness; no floating-point optimization is required."""
import argparse
import json
from pathlib import Path
import mpmath as mp
from rh_gram_followup import Certificate

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    args = parser.parse_args()
    stored = json.loads(args.certificate.read_text())
    c = Certificate(bits=int(stored['cot_fixed_point_bits']), dps=int(stored['interval_decimal_digits']))
    fresh = c.run(stored['coefficient_numerators'], int(stored['coefficient_denominator']))
    bound = mp.iv.mpf(stored['proved_D_less_than'])
    # run() already checks the independently recomputed outward enclosure.
    assert mp.iv.mpf(fresh['proved_D_less_than']).b <= bound.b
    print(json.dumps({k: v for k, v in fresh.items() if k != 'coefficient_numerators'}, indent=2))

if __name__ == '__main__':
    main()
