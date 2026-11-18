#!/usr/bin/env python3
"""Explicit work-identity, source-reading and journal-audit decisions for round 13."""
import hashlib
import json
from pathlib import Path

R=Path(__file__).resolve().parents[1]
A='audits/adversarial_reviews/'
NOTE=A+'director_baez_whole_round13.md'
JOURNAL='sources/analytic74_baez/lincei_2003.pdf'
SHA='9bfb3943ec8d7690d452b8ac7d50fb10614b4e814738dc091390e6ab4994f0b8'
VERSION='2003 Lincei journal scan, pp. 5–11, with two BDIM front sheets'


def read(path):
 p=R/path
 return [json.loads(s) for s in p.read_text().splitlines() if s.strip()] if p.exists() else []


def write(path,rows):
 (R/path).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))


def upsert(path,rows,key='id'):
 current={r[key]:r for r in read(path)}
 current.update({r[key]:r for r in rows});write(path,list(current.values()))


assert (R/NOTE).exists()
if (R/JOURNAL).exists():assert hashlib.sha256((R/JOURNAL).read_bytes()).hexdigest()==SHA
may=next(r for r in read('papers/equivalence_records.jsonl') if r['id']=='PAPER-E001')
feb=next(r for r in read('papers/ratio62_weightedprior_records.jsonl') if r['id']=='PAPER-E014')
upsert('quality/paper_aliases.jsonl',[dict(alias='PAPER-E001',canonical='PAPER-E014',
 evidence=NOTE,identity_status='one_work_with_expanded_second_arxiv_deposit_and_journal_version',
 version_note='May abstract calls February the first version; author self-citation math/0305191v1 p2 reference1 identifies May as the preprint of this journal article. Keep document-specific numbering and hashes.',
 independent_reviews=[A+'analytic87_baez_identity_review.md',A+'uniform87_baez_identity_review.md'],verified_at='2026-11-18')],key='alias')

manifestations=[
 dict(version='arXiv:math/0202141v1, 15 February 2002',arxiv='math/0202141v1',source_path='sources/analytic74_baez/math_0202141v1.pdf',source_sha256='a0b876c54be79af5d1af53d181c6cd6fc94d94cc35d32b22697a97b15c99f589',audit_level=1,whole_work_read=True,read_scope='Complete preprint compared by both whole-work reviewers. No quantitative theorem in this version.'),
 dict(**feb,original_paper_id='PAPER-E014',work_id='PAPER-E014',manifestation_role='February revision, with original record preserved'),
 dict(**may,original_paper_id='PAPER-E001',work_id='PAPER-E014',manifestation_role='Expanded May deposit; original Level 1 source record preserved',source_path='sources/equivalences/baez_duarte.pdf'),
]
(R/'quality/baez_manifestation_identity_round13.json').write_text(json.dumps(dict(canonical_work='PAPER-E014',alias='PAPER-E001',preferred_version=VERSION,preferred_sha256=SHA,mathematical_result_identity='May Proposition3.1 and journal Theorem2 are the same quantitative result, not two independent proofs.',evidence=NOTE,original_manifestations=manifestations),ensure_ascii=False,indent=2)+'\n')
reviews=[A+'analytic74_baez_whole_advocate.md',A+'weighted74_baez_whole_skeptic.md']
upsert('quality/whole_work_audit_promotions.jsonl',[dict(
 id='PAPER-E014',level=3,version=VERSION,source_sha256=SHA,evidence=NOTE,independent_reviews=reviews,
 whole_work_coverage_checklist=['All seven journal article pages and two archive front sheets; exact February/May/journal version map',
 'Integer generator endpoint, strict closure comparison, pointwise formulas and both technical lemmas',
 'Mellin normalization, gamma signs, all fixed-epsilon domains, majorant range and exact scalar tail',
 'Both ordered norm limits, continuous functional converse and the off-line pole obstruction',
 'Both quantitative error terms and the previously adjudicated shrinking-gap Perron supplement',
 'Corollary, acknowledgments, all eighteen reference roles, published/preprint correction boundaries and work-identity alias'],
 external_inputs='Matched classical zero count, local logarithmic derivative, RH near-line bounds and Stirling. Balazard–Saias is available as degraded primary text and exact journal quotation; its fixed-gap and stronger uniform supplement have independent reconstructions. Burnol relevant original passages and revised Titchmarsh were checked. Complete ancestry and all original book editions not audited.')])

write('quality/zzzzzzzz_round13_source_scope_updates.jsonl',[
 dict(id='PAPER-E014',evidence=NOTE,fields=dict(
 title='A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis',authors=['Luis Báez-Duarte'],
 date='2003',year=2003,publication_year=2003,first_preprint_date='2002-02-15',preprint_year=2002,
 venue='Rendiconti Lincei, Series 9, 14(1) (2003), 5–11',publication_status='published; original BDIM journal scan inspected',
 version=VERSION,arxiv='math/0202141',arxiv_id='math/0202141',arxiv_ids=['math/0202141','math/0205003'],
 doi=None,doi_scope='No journal-specific DOI verified; both arXiv deposit identifiers retained separately.',
 preprint_dois=['10.48550/arXiv.math/0202141','10.48550/arXiv.math/0205003'],journal_doi=None,
 source_url='http://www.bdim.eu/item?fmt=pdf&id=RLIN_2003_9_14_1_5_0',canonical_url='https://www.bdim.eu/item?id=RLIN_2003_9_14_1_5_0',
 source_path=JOURNAL,source_file=JOURNAL,source_sha256=SHA,pdf_pages=9,article_pages=7,
 record_path='papers/PAPER-E014.md',audit_file=NOTE,preferred_manifestation_track='papers/ratio62_weightedprior_records.jsonl',
 additional_manifestations=manifestations,manifestation_records=manifestations,related_sequel=None,
 related_deposit='PAPER-E001 is a stable work alias for the expanded May preprint, not a separate selected work.',
 main_result='Journal Theorem 1 (p5, proof pp6–9): in H=L²(0,infinity), RH iff chi=1_(0,1] belongs to the closure of the span of rho_n(x)={1/(nx)} for every integer n≥1. Journal Theorem 2 (pp9–10), the same result as expanded May Proposition3.1: under RH, for some fixed c>0 the damped Möbius approximants with exponent c/loglog n have norm error O((loglog n)^(−1/3)).',
 reusable_lemma='Journal Lemma 2 (pp6–7), expanded May Lemma2.2 and February Lemma2.2 with a version-specific gamma typo: the symmetric zeta quotient has modulus at most C_(epsilon0)(1+|t|)^epsilon for 0≤epsilon≤epsilon0<1/2, by the functional equation and uniform Stirling, with removable common zero values.',
 original_notation='rho_a denotes fractional-part dilations, chi the target indicator, H the full-half-axis L2 space. Historical E001 identifies the expanded May deposit; theorem numbering remains manifestation-specific.',
 audit_level=3,whole_work_read=True,substantive_reading=True,
 read_scope='Complete pinned journal, seven article pages, independently reconstructed by two agents and director. The integer criterion, corollary and RH-conditional rate survive local normalization/range/tail repairs and the separately established shrinking-gap supplement. The May and February deposits retain distinct manifestations and original reading scopes.',
 claim_verification_status='Whole-work Level 3 for the exact journal manifestation; original printed hypotheses and repaired deductions are distinguished. No RH proof or new rate claimed.',
 limitations=['All positive integer dilations including 1 are required.','Norm limits are ordered; unconditional analytic-kernel convergence does not identify the actual damped functions off RH.','The particular printed majorant needs epsilon<1/4; a free subpower exponent proves the fixed weighted range epsilon<1/2.','Uniform shrinking-gap constants require the reconstructed supplement; no practical onset or optimality claimed.'],
 journal_relation_scope='The original 2003 journal incorporates the quantitative theorem of the expanded May deposit; the author confirms this preprint relation in a contemporary self-citation.',
 version_history='February v1/v2, expanded May deposit under a second arXiv ID, then 2003 journal. Exact hashes, dates and equation numbering preserved in quality/baez_manifestation_identity_round13.json.',
 correction_history='Journal fixes February gamma denominator and transform interval. Local Mellin normalization, particular majorant range, tail exponent and conditional-identification qualifications have existing finding handles. Bounded search found no separately verified corrigendum.'
 )),
 dict(id='PAPER-GEO82-MANGOLDT1905',evidence=A+'geometry85_mangoldt1905_whole.md',fields=dict(
 audit_level=1,whole_work_read=True,substantive_reading=True,
 read_scope='Complete original German article, nineteen printed pages plus archive cover, read and reconstructed by the historical agent. Adjacent-argument kernel, one-sided maximum, multiplicities and endpoints independently checked at their source passages. Original decimal bound retained as published rather than fully recertified; no whole-work Level 2/3 promotion.',
 claim_verification_status='Complete Level 1 reading. The published O(log T) count and the scoped kernel comparisons retain separate evidence. The improved historical coefficient is not a modern best bound or weighted-tail advance.'
 )),
 dict(id='PAPER-LF63-GONEK1984',evidence=A+'geometry88_gonek_whole_advocate.md',fields=dict(
 audit_level=1,whole_work_read=True,substantive_reading=True,
 read_scope='Two independent agents read the complete nineteen-page journal paper, all headline claims, sections and lemmas. The unconditional shifted theorem and RH derivative Corollary 1, multiplicities, arbitrary-height prefix and strict tail are reconstructed. Local print and gap-coverage findings await director adjudication; whole-work Level 3 not yet claimed.',
 claim_verification_status='Complete reading at Level 1. Existing scoped derivative-prefix input remains supported; alleged local auxiliary issues do not automatically change the canonical findings ledger.',
 independent_whole_reading_reviews=[A+'geometry88_gonek_whole_advocate.md',A+'prime88_gonek_whole_skeptic.md']
 )),
])

upsert('quality/claim_status_updates.jsonl',[
 dict(id='THM-E001',evidence=NOTE,fields=dict(locator='Expanded arXiv:math/0205003v1 Theorem1.1, pp1–2; journal Theorem1, p5, proof pp6–9',source_manifestation='VERSION-BAEZ-MAY',verification='Complete journal and preprint comparison; main equivalence reconstructed in the version-pinned whole-work audit. Work alias does not alter historical theorem numbering.',director_evidence=NOTE)),
 dict(id='THM-E-D204',evidence=NOTE,fields=dict(locator='Expanded arXiv:math/0205003v1 Proposition3.1, pp6–8; same result as journal Theorem2, pp9–10; reconstructed uniform supplement in the director note',source_manifestation='VERSION-BAEZ-JOURNAL',verification='Complete journal reconstruction with the previously adjudicated uniform shrinking-gap dependency. This is one quantitative result across manifestations.',director_evidence=NOTE)),
])
upsert('quality/finding_status_updates.jsonl',[
 dict(id='FIND-008',evidence=NOTE,fields=dict(classification='Missing or insufficiently stated hypothesis',status='adjudicated_exact_envelope_range_with_valid_repair',sources=['PAPER-E014'],director_adjudication=NOTE,independent_reviews=reviews,verified_author_error=False,
 scope='Expanded May preprint p5 and journal p8 use the displayed envelope (1+|t|)^(−1+2epsilon) beyond its L2 range epsilon<1/4. Journal primary text now recovered. Retaining the free antecedent growth exponent gives fixed-epsilon convergence for epsilon<1/2, and sufficiently small epsilon proves the main criterion. No fatal theorem error or new duplicate finding group.')),
 dict(id='FIND-R207',evidence=NOTE,fields=dict(status='adjudicated_journal_and_preprint_scope',sources=['PAPER-E014'],director_adjudication=NOTE,independent_reviews=reviews,verified_author_error=False,
 scope='The February, May and journal manifestations are one work with version-specific gamma and normalization text. The free-exponent majorant repair, ordered norm limits, RH-dependent function identification and separately reconstructed shrinking-gap input preserve the criterion and rate. Whole journal audit and exact edition map now complete.')),
])

versions=[('VERSION-BAEZ-FEB1','arXiv:math/0202141v1','a0b876c54be79af5d1af53d181c6cd6fc94d94cc35d32b22697a97b15c99f589'),('VERSION-BAEZ-FEB2','arXiv:math/0202141v2','3ce4aff466443c71094affc1f8b6f5f0dd36cb4377dc5d2ceddbd2537c1d1819'),('VERSION-BAEZ-MAY','arXiv:math/0205003v1','13a2dcc763d3fdd5b52afc87845c6d77c83764a56aab06f574a91ee43c8a152b'),('VERSION-BAEZ-JOURNAL',VERSION,SHA)]
graph=[]
for ident,label,digest in versions:
 graph.append(dict(record_type='node',id=ident,type='paper_version',label=label,evidence=NOTE,source_sha256=digest,status='exact_manifestation_identity; audit scope specified separately'))
 graph.append(dict(record_type='edge',**{'from':'PAPER-E014','to':ident},relation='has_source_manifestation',provenance=NOTE,status='adjudicated_bibliographic_identity'))
for claim,version in [('THM-E001','VERSION-BAEZ-MAY'),('THM-E-D204','VERSION-BAEZ-JOURNAL')]:
 graph.append(dict(record_type='edge',**{'from':claim,'to':version},relation='has_exact_source_manifestation',provenance=NOTE,status='versioned_source_locator; no automatic renumbering'))
write('graphs/baez_versions_round13.jsonl',graph)
print(json.dumps(dict(work_alias='PAPER-E001→PAPER-E014',whole_promotion='PAPER-E014 journal',new_complete_readings=['PAPER-GEO82-MANGOLDT1905','PAPER-LF63-GONEK1984'],new_finding_groups=0)))
