#!/usr/bin/env python3
"""Unit tests plus actual CLI corruption refusals for the bounded BG26 packet."""
from __future__ import annotations

import copy
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import replay as r


def seal(root: Path) -> None:
    (root/"SHA256SUMS").write_text("".join(
        hashlib.sha256((root/name).read_bytes()).hexdigest()+"  "+name+"\n"
        for name in sorted(r.FILES)), encoding="utf-8")


class Tests(unittest.TestCase):
    def test_parent_pins(self):
        r.authenticate_parent()

    def test_strict_numbers(self):
        for bad in (True, False, 3.0, "3", 0, 193):
            with self.assertRaises((ValueError, TypeError)):
                r.mu(bad)
        for bad in (True, 2.0, 3, 16):
            with self.assertRaises(ValueError):
                r.stage(bad)

    def test_odd_coverage(self):
        self.assertEqual(r.odds(16), [1,3,5,7,9,11,13,15])
        self.assertEqual(r.mu(9), 0)
        self.assertEqual(r.mu(15), 1)

    def test_detail_inverse(self):
        keys = r.odds(15)
        t = r.rational_detail_solution(15)
        for k in keys:
            self.assertEqual(r.fdot([r.r_detail(k,l) for l in keys],t), int(k==1))

    def test_jordan_positive(self):
        for n in range(1,65):
            self.assertGreater(r.jordan(n), 0)

    def test_json_lexical(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/"data.json"
            for text in ('{"x":1,"x":2}', '{"x":1.0}', '{"x":NaN}', '{"x":Infinity}'):
                path.write_text(text,encoding="utf-8")
                with self.assertRaises(r.Refusal):
                    r.strict_json(path)

    def test_exact_interval_refusals(self):
        for value in (True, 0.5, "1"):
            with self.assertRaises(TypeError):
                r.I.of(value)
        with self.assertRaises(ZeroDivisionError):
            r.I.of(1)/r.I.bounds(-1,1)
        with self.assertRaises(r.p.CheckFailure):
            r.p.solve([[r.I.of(0)]],[r.I.of(1)])

    def test_nonempty_manifest_inventory(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            for name in r.FILES:
                p=root/name
                p.parent.mkdir(parents=True,exist_ok=True)
                p.write_text("fixture\n",encoding="utf-8")
            seal(root)
            r.check_manifest(root)
            (root/"SHA256SUMS").write_text("",encoding="utf-8")
            with self.assertRaises(r.Refusal):
                r.check_manifest(root)

    def test_manifest_extra_and_duplicate(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            for name in r.FILES:
                path=root/name
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_text("fixture\n",encoding="utf-8")
            seal(root)
            manifest=root/"SHA256SUMS"
            saved=manifest.read_text()
            manifest.write_text(saved+saved.splitlines()[0]+"\n",encoding="utf-8")
            with self.assertRaises(r.Refusal):
                r.check_manifest(root)
            manifest.write_text(saved,encoding="utf-8")
            (root/"unexpected.txt").write_text("unexpected\n")
            with self.assertRaises(r.Refusal):
                r.check_manifest(root)

    def test_semantic_header_refusals(self):
        good=r.strict_json(r.ROOT/"verification.json")
        r.preflight(good)
        for key,value in (("rh_proved",True),("uniform_full_gain_proved",True),
                          ("parent_commit","0"*40),("config",{})):
            changed=copy.deepcopy(good)
            changed[key]=value
            with self.assertRaises(r.Refusal):
                r.preflight(changed)

    def test_actual_cli_refusals(self):
        cases=("rh", "full_gain", "float", "duplicate_key", "omit_nine",
               "changed_scalar", "proof_bytes", "parent_bytes", "empty_inventory")
        results=[]
        for case in cases:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as td:
                base=Path(td)/"standalone"
                root=base/r.ROOT.name
                parent=base/r.PARENT.name
                shutil.copytree(r.ROOT,root,ignore=shutil.ignore_patterns("__pycache__"))
                # Only explicitly consumed source files are needed for the new checker.
                for name in r.PINS:
                    dst=parent/name
                    dst.parent.mkdir(parents=True,exist_ok=True)
                    shutil.copyfile(r.PARENT/name,dst)
                verification=root/"verification.json"
                obj=r.strict_json(verification)
                if case in ("rh","full_gain"):
                    obj["rh_proved" if case=="rh" else "uniform_full_gain_proved"]=True
                    verification.write_bytes(r.canonical(obj))
                    seal(root)
                elif case=="float":
                    verification.write_text(verification.read_text().replace('"max_gram_index": 16',
                                                                          '"max_gram_index": 16.0',1))
                    seal(root)
                elif case=="duplicate_key":
                    verification.write_text('{"rh_proved": false,'+verification.read_text()[1:])
                    seal(root)
                elif case=="omit_nine":
                    obj["stages"][2]["odd_detail_indices"].remove(9)
                    verification.write_bytes(r.canonical(obj))
                    seal(root)
                elif case=="changed_scalar":
                    obj["stages"][2]["values"]["full_gain"]["lo"]="0"
                    verification.write_bytes(r.canonical(obj))
                    seal(root)
                elif case=="proof_bytes":
                    with (root/"PROOF.md").open("a",encoding="utf-8") as f:
                        f.write("\nmutated proof\n")
                elif case=="parent_bytes":
                    with (parent/"scripts/intervals.py").open("a",encoding="utf-8") as f:
                        f.write("\n# modified source\n")
                else:
                    (root/"SHA256SUMS").write_text("",encoding="utf-8")
                command=[sys.executable,"-I","-S"]
                if sys.flags.optimize:
                    command.append("-O")
                command += [str(root/"scripts/replay.py"),"--check"]
                run=subprocess.run(command,capture_output=True,text=True,timeout=25,
                                   cwd=td,env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1"})
                self.assertNotEqual(run.returncode,0,case)
                self.assertNotIn("PASS_BG26_BOUNDED_FULL_SOURCE_REPLAY",run.stdout)
                results.append(case)
        print("CLI_REFUSALS="+",".join(results),flush=True)


if __name__=="__main__":
    unittest.main(verbosity=2)
