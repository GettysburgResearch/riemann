"""Bound the finite all-shift Jensen hyperbolicity range using a verified RH height."""
import argparse
import json
from pathlib import Path

from flint import arb, ctx


def sector_degree(height):
    if height < 100:
        raise ValueError("The elementary angle monotonicity check here assumes H>=100")
    t = arb(height)
    constant = arb(5558691) / 1000000
    width = arb(1) / 2 - 1 / (constant * t.log())
    slope = width / t
    upper_degree = ((1 + slope * slope) / (2 * slope))**2
    lower = int(upper_degree.lower().floor().fmpz())
    upper = int(upper_degree.upper().floor().fmpz())
    if lower != upper:
        raise ArithmeticError("The directed ball does not determine a unique floor")
    return lower


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkpoint", type=Path)
    args = parser.parse_args()
    data = json.loads(args.checkpoint.read_text())
    height, old = data["verified_integer_height"], data["published_height"]
    if "independent_integer_height_count" not in data:
        raise ValueError("An independently counted census checkpoint is required")
    ctx.prec = 256
    new, previous = sector_degree(height), sector_degree(old)
    print(json.dumps({"verified_height": height, "simple_degree_range": height**2,
                      "sector_degree_range": new, "published_height_sector_range": previous,
                      "sector_extension_from_census": new-previous}, indent=2))


if __name__ == "__main__":
    main()
