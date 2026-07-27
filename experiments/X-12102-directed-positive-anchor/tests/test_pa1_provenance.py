from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT,):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

SPEC = importlib.util.spec_from_file_location(
    "pa1_provenance", ROOT / "verify_pa1_provenance.py"
)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class ProvenanceTests(unittest.TestCase):
    def write_pair(self, declared_sha: str, blob: str | None):
        directory = tempfile.TemporaryDirectory()
        root = Path(directory.name)
        certificate = root / "certificate.json"
        basis = root / "basis.json"
        certificate.write_text(
            json.dumps({"certificate_sha256": "1" * 64}) + "\n",
            encoding="utf-8",
        )
        actual_blob = module.git_blob_sha1(certificate)
        payload = {"source_certificate_sha256": declared_sha}
        if blob == "ACTUAL":
            payload["source_certificate_git_blob_sha1"] = actual_blob
        elif blob is not None:
            payload["source_certificate_git_blob_sha1"] = blob
        basis.write_text(json.dumps(payload) + "\n", encoding="utf-8")
        return directory, certificate, basis

    def test_git_blob_compatibility(self):
        holder, certificate, basis = self.write_pair("2" * 64, "ACTUAL")
        with holder:
            patched, audit = module.prepare_basis(certificate, basis)
            self.assertEqual(audit["binding_mode"], "GIT_BLOB_SHA1")
            self.assertEqual(patched["source_certificate_sha256"], "1" * 64)

    def test_internal_digest_compatibility(self):
        holder, certificate, basis = self.write_pair("1" * 64, None)
        with holder:
            patched, audit = module.prepare_basis(certificate, basis)
            self.assertEqual(
                audit["binding_mode"], "INTERNAL_CERTIFICATE_SHA256"
            )
            self.assertEqual(patched["source_certificate_sha256"], "1" * 64)

    def test_mismatch_rejected(self):
        holder, certificate, basis = self.write_pair("2" * 64, "3" * 40)
        with holder:
            with self.assertRaises(module.legacy.CertificateError):
                module.prepare_basis(certificate, basis)

    def test_boolean_or_malformed_digest_rejected(self):
        holder, certificate, basis = self.write_pair("not-a-digest", None)
        with holder:
            with self.assertRaises(module.legacy.CertificateError):
                module.prepare_basis(certificate, basis)


if __name__ == "__main__":
    unittest.main()
