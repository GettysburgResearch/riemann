#!/usr/bin/env python3
from pathlib import Path
import importlib.util

HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('verify',HERE/'verify.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

def test_classification():
    assert mod.build()['classification'].startswith('PASS_T97500')

def test_two_node_separator():
    from fractions import Fraction
    f=mod.raw_chain_solution([Fraction(1,5)],[Fraction(0),Fraction(1)])
    g=mod.contracted_current([Fraction(1,25)],f)
    assert g[0] == Fraction(-4,25)

def test_exposure_threshold():
    x=mod.exposure_checks()
    assert x['critical_raw_child_fraction']=='4/21'
