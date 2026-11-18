#!/usr/bin/env python3
"""Integrate explicitly adjudicated band results, without promoting source papers."""
import json
from pathlib import Path

R = Path(__file__).resolve().parents[1]
A = 'audits/adversarial_reviews/'
N = A + 'director_band_laws_round12.md'
J = A + 'director_joint_process_round12.md'


def read(path):
    p = R/path
    return [json.loads(s) for s in p.read_text().splitlines() if s.strip()] if p.exists() else []


def write(path, rows):
    (R/path).write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in rows))


def upsert(path, rows):
    current = {r['id']:r for r in read(path)}
    current.update({r['id']:r for r in rows})
    write(path,list(current.values()))


claims=[]
def claim(ident,note,statement,hypotheses,kind):
    claims.append(dict(id=ident, paper_id=None, locator=note,
                       statement=statement,hypotheses=hypotheses,claim_kind=kind,
                       status='adjudicated_scoped',novelty_claim=False))


claim('THM-SHRINKING-EXPONENT-SCALAR-GAUSSIAN',N,
      'Under RH, if b(Y)→0, a(Y)/b(Y)→r in (0,1), and a(Y)logY→infinity, the cosine prime band Y^a<p≤Y^b, centered by sum 1/p or its actual mean, converges in law and every fixed moment to N(0,(1/2)log(1/r)).',
      'Symmetric strict derivative-square tail. Uses bounded aggregate polynomial powers at each fixed degree and the reconstructed sharp interface. Effective parameter estimates require effective cutoff moduli and the audited effective exceptional-prime estimate. This record alone is scalar.',
      'conditional_shrinking_band_limit')
claim('THM-ROOTED-CUE-FULL-BAND-LAW',N,
      'For any fixed 0<a<b<infinity, globally derivative-square tilted rooted CUE Fourier bands converge jointly in law and every fixed moment to the one-root-reinserted rank-two-removed sine-projection linear statistics. The centered statistic is defined in L2 and has the regularized determinant in the director note.',
      'Global Haar-matrix/root-label tilt, not per-matrix root normalization. Positive lower frequency, a fixed finite family, and centered L2 or symmetric summation. Absolute point sums diverge for the nontrivial individual cosine band. The quadratic trace correction in det2 is required. No RH or arithmetic law transfer.',
      'intrinsic_random_matrix_limit')
claim('THM-HLZ-FINITE-BAND-MOMENT-WINDOW',N,
      'For every fixed integer r≥0 with rb<1/2, the raw rth moment of the RH derivative-weighted cosine band converges to r! times [z^r] exp(H z+H z²/4)[(1−d z)^4+q z(1−d z)], where H=log(b/a), d=b−a and q=2(b³−a³)/3.',
      'One fixed 0<a<b and the exact symmetric strict tail. Each degree r uses aggregate arms through Y^(rb) and fixed declared exponent below 1/2. Only the source-admissible finite coefficient window is evaluated; growing r or all orders at fixed b are not justified.',
      'conditional_finite_moment_formula')
claim('OBS-HLZ-ALL-ORDER-EXTRAPOLATION-BARRIER',N,
      'For every fixed 0<a<b, the formal all-order coefficient sequence of exp(H z+H z²/4)[(1−d z)^4+q z(1−d z)] cannot be the moments of a positive probability. Its entire formal MGF vanishes at 1/d; Gaussian-polynomial even-moment domination makes this a rigorous contradiction. A degree-70 negative Gram witness at [1/20,1/10] is independently interval-verified.',
      'Pure unconditional statement about the formal sequence, not about source validity or actual higher arithmetic moments. The witness uses formal orders through 140, while that arithmetic band supplies only orders 0–4. All genuine source-window Hankel tests remain positive.',
      'formal_extrapolation_positivity_obstruction')
claim('LEM-SUBPOWER-SUBSET-TWO-SCALE-FOURTH',J,
      'Under RH, for every prime subset I of (Y^(r0 b),Y^b], h=sum_I 1/p, one has E_Y|sum_I(cos(gamma logp)/sqrt p−1/p)|^4≤C_M min(h²+(logY)^−M,(logY)²h²), hence ≤C h^(3/2) for M≥6.',
      'Fixed 0<r0<1, b→0 and b logY→infinity, same symmetric strict derivative-square tail, all subsets uniformly at sufficiently large Y. The exact local-mass bound uses analytic disks for zeta D_I² and the classical continuous fourth moment. A full-range Ch² bound is not asserted.',
      'conditional_uniform_subset_lemma')
claim('THM-SHRINKING-BAND-BROWNIAN-PROCESS',J,
      'Under RH, X_Y(r)=sum_(Y^(r0 b)<p≤Y^(r b))[cos(gamma logp)/sqrt p−1/p] converges in D([r0,1]), J1, to B_((1/2)log(r/r0)).',
      'Fixed 0<r0<1, b(Y)→0, b(Y)logY→infinity and the symmetric strict derivative-square tail. Uses the two-scale fourth lemma, exact reciprocal-clock interpolation, vanishing jumps, and fixed-dimensional Gaussian projections. In-principle effective onset needs computable r0, effective cutoff moduli and the audited effective aggregate input; no numerical onset.',
      'conditional_functional_limit')
claim('THM-POLYNOMIAL-BAND-JOINT-THIRD-TENSOR',J,
      'Under RH, for bounded real Riemann-integrable cosine/sine weights supported in [a,b] with 0<a<b<1/6, the centered third tensor matches globally derivative-square rooted CUE. The CSS entry is 12 integral f(x)(x²−2)dx integral g(y)y dy integral h(z)z dz. Odd-sine entries vanish. Same-band CSS is (Delta3−6Delta1)Delta2².',
      'Signed primary HLZ extraction, aggregate length Y^(3b), repeated-prime cancellation, exact strict tail, and one deterministic root on the CUE side. Fourth moments are uniformly bounded. This adds the mixed tensor to the prior pure cosine cubic, not a full arithmetic law. At [1/20,1/10] CSS=−21537/1280000000.',
      'conditional_cross_framework_joint_cumulant_match')
claim('OBS-POLYNOMIAL-BAND-UNCORRELATED-DEPENDENCE',J,
      'For nonnegative bounded Riemann-integrable cosine and sine weights with positive integrals, supported in a common [a,b]⊂(0,1/6), any arithmetic weak subsequential vector limit has dependent cosine/sine coordinates despite exact zero covariance. The supports may be disjoint.',
      'Assumes RH and the same strict tail. Uniform fourth moments transfer the nonzero centered CSS entry; independence would force it to vanish. Pointwise nonzero weights confined to null sets are excluded. Existence or uniqueness of a full vector limit and Gaussianity of the sine marginal are not asserted.',
      'conditional_dependence_obstruction')
write('theorems/band_laws_round12_claims.jsonl',claims)

deps=[
 ('THM-SHRINKING-EXPONENT-SCALAR-GAUSSIAN','THM-SCALAR-PRIME-SUBPOWER-POLYNOMIAL',N),
 ('THM-HLZ-FINITE-BAND-MOMENT-WINDOW','THM-HLZ-JOURNAL5-REAL-COEFFICIENTS',N),
 ('THM-HLZ-FINITE-BAND-MOMENT-WINDOW','THM-SHARP-AGGREGATE-CONTINUOUS-J',N),
 ('OBS-HLZ-ALL-ORDER-EXTRAPOLATION-BARRIER','THM-HLZ-FINITE-BAND-MOMENT-WINDOW',N),
 ('THM-ROOTED-CUE-FULL-BAND-LAW','THM-ROOTED-CUE-PRIME-BAND-MOMENT-MATCH',N),
 ('LEM-SUBPOWER-SUBSET-TWO-SCALE-FOURTH','THM-HLZ-JOURNAL5-REAL-COEFFICIENTS',J),
 ('THM-SHRINKING-BAND-BROWNIAN-PROCESS','LEM-SUBPOWER-SUBSET-TWO-SCALE-FOURTH',J),
 ('THM-SHRINKING-BAND-BROWNIAN-PROCESS','THM-SHRINKING-EXPONENT-SCALAR-GAUSSIAN',J),
 ('THM-POLYNOMIAL-BAND-JOINT-THIRD-TENSOR','THM-POLYNOMIAL-PRIME-BAND-NONGAUSSIAN',J),
 ('THM-POLYNOMIAL-BAND-JOINT-THIRD-TENSOR','THM-HLZ-JOURNAL5-REAL-COEFFICIENTS',J),
 ('OBS-POLYNOMIAL-BAND-UNCORRELATED-DEPENDENCE','THM-POLYNOMIAL-BAND-JOINT-THIRD-TENSOR',J),
]
write('theorems/band_laws_round12_proof_edges.jsonl',[
    dict(**{'from':a,'to':b},relation=('is_formal_extension_of_valid_finite_window' if a.startswith('OBS-HLZ') else 'uses_exact_scoped_input'),locator=n,evidence=n,status='adjudicated_scoped')
    for a,b,n in deps])

groups=[
 ('SCALAR',N,['analytic78_shrinking_band.md','weighted78_shrinking_band_review.md']),
 ('CUELAW',N,['prime77_rooted_cue_band_limit.md','uniform77_rooted_cue_full_law.md','geometry80_full_cue_adjudication_input.md']),
 ('CUEFINITE',N,['prime78_rooted_cue_band_moment_experiment.md','uniform78_rooted_cue_finite_n_review.md']),
 ('FORMAL',N,['prime79_hlz_formal_moment_obstruction.md','weighted79_formal_band_obstruction_review.md']),
 ('JOINTTHIRD',J,['prime81_joint_third.md','weighted81_joint_third_review.md']),
 ('PROCESS',J,['uniform81_shrinking_band_process.md','analytic82_shrinking_process_skeptic.md']),
]
upsert('audits/reviewed_claim_groups.jsonl',[
    dict(id='REVIEW-GROUP-R12-'+k,title=k+' band-law reconstruction',status='adjudicated_scoped',director_adjudication=n,independent_reviews=[A+p for p in refs])
    for k,n,refs in groups])

def connection(ident,sources,statement,hypotheses,proved,conjectural,next_step,counterexamples,tests,significance,note):
    return dict(id=ident,sources=sources,statement=statement,hypotheses=hypotheses,already_proved=proved,conjectural=conjectural,next_step=next_step,counterexamples=counterexamples,tests=tests,significance=significance,difficulty='Exact next-step estimate stated in the director note; publication priority remains unassessed.',status='adjudicated_scoped',evidence=note)

write('connections/band_laws_round12_connections.jsonl',[
 connection('CONN-CUE-CANDIDATE-ARITHMETIC-BAND-LAW',['THM-ROOTED-CUE-FULL-BAND-LAW','THM-POLYNOMIAL-BAND-JOINT-THIRD-TENSOR'],
 'The intrinsic compensated Palm-sine law gives a precise candidate arithmetic characteristic function, beyond the matched low moments.',
 'Identical global derivative tilt, negative Fourier observable, one root and declared band; arithmetic assertions assume RH.',
 'Intrinsic full RMT law and the arithmetic means, covariance and full third tensor in their ranges.',
 'Existence and identification of the full arithmetic band law.',
 'Prove a fixed-band characteristic-function comparison or new higher-support arithmetic estimates.',
 'Finite moment agreement and kernel analogy cannot identify a law; per-matrix root normalization gives a different model.',
 'Independent kernel limits, regularized determinant and finite exact trace checks.',
 'Replaces a vague RMT analogy with an explicit law and a precise missing arithmetic input.',N),
 connection('CONN-FINITE-WINDOW-MOMENT-POSITIVITY-BARRIER',['THM-HLZ-FINITE-BAND-MOMENT-WINDOW','OBS-HLZ-ALL-ORDER-EXTRAPOLATION-BARRIER'],
 'The exact low-support moment polynomial supplies its own obstruction to unchanged all-order extrapolation.',
 'Arithmetic coefficients only when rb<1/2; the all-order obstruction is an unconditional formal statement.',
 'Explicit quartic factor, real MGF zero, signed inverse and finite negative Gram witness beyond the true window.',
 'Actual higher moments and the first new arithmetic frequency chambers.',
 'Compute a genuine main term outside the old length window and compare the first required corrective term to rooted CUE.',
 'All admissible Hankel tests remain positive; a formal witness outside the range is no source contradiction.',
 'Two independent source extractions and three exact/interval Gram methods.',
 'Eliminates a specific tempting route from a finite moment formula to a full law.',N),
 connection('CONN-LOG-REMAINDER-ANALYTIC-SAMPLING-TIGHTNESS',['LEM-SUBPOWER-SUBSET-TWO-SCALE-FOURTH','THM-SHRINKING-BAND-BROWNIAN-PROCESS'],
 'A separate analytic-sampling bound with exact local mass repairs the small-scale limitation of an aggregate logarithmic remainder.',
 'RH, shrinking subpower band, fixed reciprocal clock and classical continuous fourth moment.',
 'The minimum of h²+L^−M and L²h² yields h^(3/2) at every subset scale and a Brownian process.',
 'A uniform Ch² bound across the full range and useful numerical path onsets.',
 'Track constants or extend the two-bound method to other weighted zero processes.',
 'An interval-independent o(1) error alone cannot imply tightness; random shrinking pulses supply a countermodel.',
 'Independent disk factor, overlap, strip interpolation, Stieltjes signs and dyadic chaining.',
 'A reusable method for turning qualitative aggregate estimates into a genuine process theorem.',J),
 connection('CONN-CSS-CROSSBAND-DEPENDENCE',['THM-POLYNOMIAL-BAND-JOINT-THIRD-TENSOR','OBS-POLYNOMIAL-BAND-UNCORRELATED-DEPENDENCE'],
 'The signed third tensor detects cross-band cosine/sine dependence invisible to their exact zero covariance.',
 'Common positive exponent range below 1/6; nonnegative weights have positive integrals, not merely pointwise nonzero values.',
 'A negative mixed cubic survives weak limits by uniform fourth moments, including disjoint supports.',
 'The joint full arithmetic law and sine-marginal distribution.',
 'Test the full candidate DPP mixed characteristic function against new arithmetic estimates.',
 'Uncorrelated components need not be independent; null-set test weights do not give strict negativity.',
 'Two signed HLZ derivations and two chamberwise projection trace calculations.',
 'Gives a precise failure of independent polynomial-band phase models.',J),
])
print(json.dumps(dict(new_claims=len(claims),new_scoped_groups=len(groups),new_connections=4)))
