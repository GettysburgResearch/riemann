#!/usr/bin/env python3
"""Small exact unit/rejection suite; no network, no third-party packages."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import replay as r
from intervals import I, SCALE, log_q, psi_q


class ArithmeticTests(unittest.TestCase):
    def test_types(self):
        for x in [1.0, True, "1"]:
            with self.assertRaises(TypeError):
                I.of(x)
        # Caching must not bypass exact-type validation.
        for fun in [log_q,psi_q]:
            fun(F(2))
            with self.assertRaises(TypeError):
                fun(2.0)
        r.gram(2,3)
        with self.assertRaises(ValueError):
            r.gram(2.0,3)

    def test_refusals(self):
        with self.assertRaises(ValueError):
            I(2,1)
        with self.assertRaises(ZeroDivisionError):
            I.of(1)/I(-1,1)
        with self.assertRaises(ValueError):
            I.of(-1).sqrt()
        with self.assertRaises(ValueError):
            log_q(F(0))
        with self.assertRaises(ValueError):
            psi_q(F(-1))
        with self.assertRaises(ValueError):
            r.gram(2,17)

    def test_signed_division(self):
        for a in [F(-7,3),F(0),F(5,7)]:
            for b in [F(-5,4),F(3,7)]:
                self.assertTrue((I.of(a)/b).contains(a/b))

    def test_negative_square(self):
        x=I.bounds(-2,3).square()
        self.assertEqual(x.lo,0)
        self.assertTrue(x.contains(9))

    def test_exact_elimination(self):
        a=[[I.of(2),I.of(1)],[I.of(1),I.of(3)]]
        x,p=r.solve(a,[I.of(1),I.of(2)])
        self.assertTrue(x[0].contains(F(1,5)))
        self.assertTrue(x[1].contains(F(3,5)))
        self.assertTrue(all(t.lo>0 for t in p))

    def test_bad_pivot(self):
        with self.assertRaises(r.CheckFailure):
            r.solve([[I.of(1),I.of(1)],[I.of(1),I.of(1)]],[I.of(1),I.of(1)])

    def test_dual_overlap(self):
        self.assertEqual(r.dual(2),{1:4,2:-6})
        self.assertEqual(sum(F(v*v,n*(n+1)) for n,v in r.dual(2).items()),14)

    def test_five_witness(self):
        self.assertEqual(r.dual(5),{1:2,4:20,5:-30})
        for k in [2,3,4,6,8,9,12,16,18,27,81]:
            self.assertEqual(sum(r.h(k,n)*F(v,n*(n+1)) for n,v in r.dual(5).items()),0)

    def test_decimal_enclosure(self):
        self.assertEqual(I.of(F(-1,3)).decimal_bounds(3),["-0.334","-0.333"])
        self.assertEqual(I.of(2).decimal_bounds(3),["2.000","2.000"])

    def test_json_duplicate(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/"a.json"; p.write_text('{"x":1,"x":2}')
            with self.assertRaises(ValueError):
                r.strict_json(p)

    def test_json_nonexact(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/"a.json"
            for text in ['{"x":1.0}','{"x":NaN}','{"x":Infinity}']:
                p.write_text(text)
                with self.assertRaises(ValueError):
                    r.strict_json(p)

    def test_boolean_not_integer_alias(self):
        self.assertNotEqual(r.canonical({"n":True}),r.canonical({"n":1}))


class PublicationContractTests(unittest.TestCase):
    def test_manifest(self):
        r.check_hashes()

    def test_source_mutation_refused(self):
        # Test in a temporary minimal packet; do not mutate the deliverable.
        old=r.ROOT
        with tempfile.TemporaryDirectory() as t:
            r.ROOT=Path(t)
            p=r.ROOT/"proof.md"; p.write_text("original\n")
            (r.ROOT/"SHA256SUMS").write_text(hashlib.sha256(p.read_bytes()).hexdigest()+"  proof.md\n")
            try:
                r.check_hashes()
                p.write_text("changed\n")
                with self.assertRaises(r.CheckFailure):
                    r.check_hashes()
            finally:
                r.ROOT=old

    def test_extra_file_refused(self):
        old=r.ROOT
        with tempfile.TemporaryDirectory() as t:
            r.ROOT=Path(t)
            p=r.ROOT/"proof.md"; p.write_text("original\n")
            (r.ROOT/"SHA256SUMS").write_text(hashlib.sha256(p.read_bytes()).hexdigest()+"  proof.md\n")
            try:
                (r.ROOT/"unexpected.txt").write_text("new")
                with self.assertRaises(r.CheckFailure):
                    r.check_hashes()
            finally:
                r.ROOT=old


if __name__ == "__main__":
    unittest.main()
