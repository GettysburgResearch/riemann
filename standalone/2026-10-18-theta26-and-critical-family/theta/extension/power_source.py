"""Read standardized power targets from the complete directed theta26 source.

Returned midpoint values are for exploratory producers only. A directed
checker must consume the complete interval endpoints separately.
"""
from decimal import Decimal as D
from pathlib import Path
from math import factorial
import json
from exact_polynomial import unit_cumulants

DEFAULT_SOURCE=Path(__file__).resolve().parent.parent/'theta26_source.json'


def targets(degree,source=DEFAULT_SOURCE):
    if degree%2 or not 4<=degree<=26:raise ValueError('supported even source degree is4 through26')
    data=json.loads(source.read_text())
    scale=D(2)**data['bits']
    ratios=[D(lo+hi)/(2*scale) for lo,hi in data['standardized_cumulant_ratios'][:degree//2]]
    unit=unit_cumulants(degree)
    return [D((-1)**(r+1)*r*unit[2*r])*ratios[r-1]/factorial(2*r)
            for r in range(2,degree//2+1)]
