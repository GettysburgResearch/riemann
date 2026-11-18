"""Independently enclose the nine earlier numerical ordinates reported by Zeraoulia.

Version 1.0 (31 August 2026), Table 1 and first-zero refinement.
https://doi.org/10.5281/zenodo.22183396
"""
from flint import arb, ctx
from check_scalar_signs import hardy_sign

ORDINATES = (
    "3000175333800.085251712406949530813839286930293799562",
    "3000175333800.452866387302961315260307883555",
    "3000175333800.578570442636947000296206715334",
    "3000175333800.872414134722930254412480291284",
    "3000175333801.181718403428891949229491391586",
    "3000175333801.325424338894006942938759814865",
    "3000175333801.599256283960782009414187862974",
    "3000175333801.715321419051705158163513391566",
    "3000175333801.886566436154954572966258538849",
)


def main():
    ctx.prec = 320
    first = 12_363_153_441_418
    lower, upper = arb(3000175333800), arb(3000175333802)
    for point, expected in ((lower, first-1), (upper, first+8)):
        n = point.zeta_nzeros()
        if not n.is_exact() or n != expected:
            raise ArithmeticError("Global counts disagree")
    previous = lower
    for j, text in enumerate(ORDINATES):
        radius = arb(10)**(-len(text.split(".")[1]))
        center = arb(text)
        a, b = center-radius, center+radius
        if not previous < a < b < upper or hardy_sign(a) == hardy_sign(b):
            raise ArithmeticError(f"No disjoint rigorous crossing for {first+j}")
        print(first+j, text, "error <", radius, flush=True)
        previous = b


if __name__ == "__main__":
    main()
