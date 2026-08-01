from __future__ import annotations
import copy, importlib.util, json, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('x16207_verify',ROOT/'verify.py')
assert SPEC and SPEC.loader
mod=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=mod; SPEC.loader.exec_module(mod)
BASE=json.loads((ROOT/'certificate.json').read_text())

class Tests(unittest.TestCase):
    def test_source_fields_close_but_alias_stays_open(self):
        out=mod.verify(copy.deepcopy(BASE))
        self.assertEqual(out['classification'],'SOURCE_FIELDS_CLOSED_COMPLETE_ALIAS_GRAM_OPEN')
        self.assertIsNone(out['profile_gram']['complete_lower'])
    def test_complete_alias_can_close_only_with_explicit_moat(self):
        x=copy.deepcopy(BASE); x['complete_arithmetic_alias']['cross_error_upper']='1/10'
        out=mod.verify(x)
        self.assertEqual(out['classification'],'PRODUCTION_PROFILE_GRAM_CLOSED')
        self.assertIsNotNone(out['profile_gram']['complete_lower'])
    def test_radial_understatement_rejected(self):
        x=copy.deepcopy(BASE); x['source_derived_replacements']['tail_l2_sq_upper']='0'
        with self.assertRaises(mod.CertificateError): mod.verify(x)
    def test_derivative_understatement_rejected(self):
        x=copy.deepcopy(BASE); x['source_derived_replacements']['derivative_tail_l2_sq_upper']='0'
        with self.assertRaises(mod.CertificateError): mod.verify(x)
    def test_f4_understatement_rejected(self):
        x=copy.deepcopy(BASE); x['source_derived_replacements']['source_fourth_derivative_l1_upper']='1'
        with self.assertRaises(mod.CertificateError): mod.verify(x)
    def test_endpoint_understatement_rejected(self):
        x=copy.deepcopy(BASE); x['source_derived_replacements']['poisson_endpoint_point_upper']='0'
        with self.assertRaises(mod.CertificateError): mod.verify(x)
    def test_deterministic_not_separate_declaration(self):
        x=copy.deepcopy(BASE); x['source_derived_replacements']['deterministic_error_upper']='0'
        with self.assertRaises(mod.CertificateError): mod.verify(x)
    def test_first_alias_understatement_rejected(self):
        x=copy.deepcopy(BASE); x['first_alias_profile_gram']['lower']='1'
        with self.assertRaises(mod.CertificateError): mod.verify(x)
    def test_nonpositive_complete_gram_rejected(self):
        x=copy.deepcopy(BASE); x['complete_arithmetic_alias']['cross_error_upper']='2'
        with self.assertRaises(mod.CertificateError): mod.verify(x)
    def test_digest_mutation_rejected(self):
        x=copy.deepcopy(BASE); x['source']['actual_primitive_sha256']='bad'
        with self.assertRaises(mod.CertificateError): mod.verify(x)

if __name__=='__main__': unittest.main()
