#!/usr/bin/env python3
"""Persist explicit director decisions; never infer reading from access."""
import hashlib
import json
from pathlib import Path

R = Path(__file__).resolve().parents[1]
A = 'audits/adversarial_reviews/'
NOTE = A + 'director_li_whole_round12.md'
LI_VERSION = '1997 journal-typeset manifestation, pp. 325–333, recovered from Paperzz mirror'
LI_PATH = 'sources/li_original_round2/li1997_journal_typeset_mirror.pdf'
LI_SHA = '8f5719751f869d71907c9da75270cb8c012b54f1453f54179461dbc331d255a1'


def read(path):
    p = R / path
    return [json.loads(s) for s in p.read_text().splitlines() if s.strip()] if p.exists() else []


def write(path, rows):
    (R / path).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))


def upsert(path, rows):
    current = {r['id']: r for r in read(path)}
    current.update({r['id']: r for r in rows})
    write(path, list(current.values()))


# Private source bytes are optional in the distributable archive. When present,
# verify them before writing the decision pinned to that exact manifestation.
if (R / LI_PATH).exists():
    assert hashlib.sha256((R / LI_PATH).read_bytes()).hexdigest() == LI_SHA
assert (R / NOTE).exists()
reviews = [A + 'uniform74_li_whole_advocate.md', A + 'prime74_li_whole_skeptic.md']
assert all((R / p).exists() for p in reviews)

promotion = dict(
    id='PAPER-E008', level=3, version=LI_VERSION, source_sha256=LI_SHA,
    evidence=NOTE, independent_reviews=reviews,
    whole_work_coverage_checklist=[
        'All nine journal-typeset pages 325–333, both theorems and all four reference roles',
        'Paired Hadamard convergence, derivative reflection, branches, and zero multiplicities',
        'Classical theta kernel, boundary constants, both coefficient centers, and the initial radius',
        'Dedekind gamma and residue conventions, exact Q(i) normalization witness and Mellin repair',
        'Both Dedekind lemmas, coefficient recurrence, analytic continuation, both converses and closing remark',
        'Old apparent sign objection withdrawn; publisher-byte and original-edition dependency limitations retained',
    ],
    external_inputs='Matched classical functional equations, residues, fixed-strip growth, Gaussian Poisson and Hadamard theory. Barner original passages and later primary editions of Lang/Weil checked in their exact use; Edwards product independently reconstructed. Entire proof ancestry and present publisher-byte identity not audited.',
)
upsert('quality/whole_work_audit_promotions.jsonl', [promotion])

write('quality/zzzzzzz_round12_source_scope_updates.jsonl', [
    dict(id='PAPER-E008', evidence=NOTE, fields=dict(
        audit_level=3, whole_work_read=True, substantive_reading=True,
        version=LI_VERSION, source_path=LI_PATH, source_file=LI_PATH, source_sha256=LI_SHA,
        publication_status='published; journal-typeset manifestation accessed through a public mirror',
        available_formats=['journal-typeset PDF from mirror', 'older degraded primary-text reproduction'],
        additional_manifestations=[dict(version='Previously inspected degraded primary-text reproduction', source_file='sources/li_original_round2/li1997_paperzz_tool_response.json', source_sha256='845a2d9b2c86da1acf3502f9ed2f7f17ae5e922f87761d42c34f321708ba6f2c')],
        accessed_at='2026-11-18',
        read_scope='Complete nine-page journal-typeset manifestation read by advocate, skeptic and director. Both main criteria reconstructed; exact Dedekind normalization and nonvanishing-symbol repairs preserve them. All equations, coefficient centers, branches, convergence, endpoint constants and reference roles inspected. Publisher-byte identity and complete upstream ancestry remain unverified.',
        claim_verification_status='Whole-work Level 3 for the registered mirror manifestation, with explicit local corrections; neither main criterion is refuted.',
        limitations=['Every positive integer coefficient is required; a finite prefix does not imply RH.', 'Zero sums use reflected pairing rather than arbitrary absolute reordering.', 'Current publisher PDF bytes and all original cited book editions were not obtained; matched inputs and independent replacements are documented.'],
        research_questions=['What arithmetic information can control the unseen Li-coefficient tail?', 'Can stable finite coefficient information be coupled to an independently proved global growth or positivity constraint?'],
        correction_history='Bounded correction search found no verified separate corrigendum. The pinned typeset text has a local zeta/Xi nonvanishing-symbol slip and a missing positive complex-place factor in equations (3.4), (3.7); exact repairs and witnesses are director adjudicated.'
    )),
    dict(id='PAPER-E014', evidence=A + 'analytic74_baez_whole_advocate.md', fields=dict(
        audit_level=1, whole_work_read=True, substantive_reading=True,
        read_scope='Two independent agents read all seven pages of arXiv math/0202141v2 and the complete seven-page 2003 journal article, with v1 and separate sequel comparison. Complete reading is recorded at Level 1; whole-work Level 3 adjudication remains pending. Existing scoped criteria and quantitative repairs retain their prior statuses.',
        journal_relation_scope='Full original BDIM journal scan recovered through plain HTTP and read by two agents. Seven article pages 5–11 plus two PDF front sheets; source SHA-256 9bfb3943ec8d7690d452b8ac7d50fb10614b4e814738dc091390e6ab4994f0b8. Journal adds the quantitative section and corrects the preprint gamma denominator.',
        additional_manifestations=[dict(version='2003 Lincei journal scan, pp. 5–11 with two PDF front sheets', source_path='sources/analytic74_baez/lincei_2003.pdf', source_sha256='9bfb3943ec8d7690d452b8ac7d50fb10614b4e814738dc091390e6ab4994f0b8', source_url='http://www.bdim.eu/item?fmt=pdf&id=RLIN_2003_9_14_1_5_0')],
        independent_whole_reading_reviews=[A + 'analytic74_baez_whole_advocate.md', A + 'weighted74_baez_whole_skeptic.md']
    )),
    dict(id='PAPER-DM63-HLZ2022', evidence=A + 'release75_hlz_whole_skeptic.md', fields=dict(
        audit_level=1, whole_work_read=True, substantive_reading=True,
        read_scope='Two independent agents read all 37 journal pages, sections 1–6, acknowledgments and references, with arXiv v1 comparison. Complete reading is Level 1; the director has adjudicated the scoped Theorem 5 and sharp continuous interface and polynomial-band consequences. Whole-paper Level 3 adjudication, including source smoothing corrections and the complete negative-moment reconstruction, remains pending.',
        claim_verification_status='Complete reading at Level 1. Published Theorem 5 with explicit primary formula and independently repaired sharp interface is separately adjudicated. Literal arbitrary-smoothing-kernel claims are not endorsed by that scoped decision.',
        independent_whole_reading_reviews=[A + 'geometry75_hlz_whole_advocate.md', A + 'release75_hlz_whole_skeptic.md']
    )),
])

upsert('quality/claim_status_updates.jsonl', [
    dict(id=ident, evidence=NOTE, fields=dict(
        verification='Complete journal-typeset source reconstructed by two independent agents and director; exact local Dedekind normalization repair and source-access boundaries documented.',
        director_evidence=NOTE, verification_scope='Whole-work Level 3 for the pinned manifestation; upstream inputs explicitly bounded.'
    )) for ident in ['THM-LI97-01', 'THM-LI97-02', 'THM-LI97-03', 'THM-LI97-04']
])

write('theorems/director_round12_claims.jsonl', [dict(
    id='OBS-LI97-DEDEKIND-NORMALIZATION', paper_id='PAPER-E008',
    locator=NOTE, status='adjudicated_exact_versioned_local_correction', novelty_claim=False,
    statement='For the literal kernel, product differential and G2=(2π)^(1−s)Γ(s) of Li 1997, equation (3.4) needs multiplier (2π)^r2/c_k rather than 1/c_k; (3.7) inherits the same positive factor. Both main criteria survive.',
    hypotheses='Pinned 1997 journal-typeset mirror pp. 328–331. Ordinary product logarithmic measure as printed; exact Q(i) Jacobi-theta witness gives true multiplier 4 rather than 2/π.'
)])
write('audits/director_round12_findings.jsonl', [dict(
    id='FIND-LI97-LOCAL-DEDEKIND-NORMALIZATION', classification='Verified mathematical error',
    title='Local nonvanishing-symbol and complex-place normalization slips in the pinned Li manifestation',
    sources=['PAPER-E008', 'OBS-LI97-DEDEKIND-NORMALIZATION'],
    scope='Only the p. 329 assertion that zeta_k is nonvanishing at zero and the positive multiplier in (3.4), inherited in (3.7). The normalized Xi_k is nonvanishing at zero and the corrected positive multiplier preserves Lemma 3.2 and both main criteria. Publisher-byte identity is unverified.',
    evidence=NOTE, director_adjudication=NOTE, independent_reviews=reviews,
    explicit_witness='For Q(sqrt5), zeta_k has a simple zero at zero. For Q(i), Jacobi inversion gives Xi_k(s)=1+4s(s−1)K(s), K(2)>0, whereas the printed (3.4) coefficient is 2/π. Both are exact symbolic witnesses.',
    verified_author_error=True, status='adjudicated_versioned_local_assertions_with_repairs', date='2026-11-18'
)])
print(json.dumps(dict(whole_promotion='PAPER-E008', complete_reading_events=['PAPER-E014', 'PAPER-DM63-HLZ2022'], new_claims=1, new_findings=1)))
