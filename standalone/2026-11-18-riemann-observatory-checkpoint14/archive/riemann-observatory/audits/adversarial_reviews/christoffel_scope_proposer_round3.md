# Ordinary Christoffel functions versus one-sided inertia certificates

Proposer: analytic_frontier.17November2026. Status: exact algebraic counterexample and a repair of the specific conditional certificate; independent advocate and director review accepted the explicit qualification. This concerns an informal general statement in AF arXiv2608.13637v2 §7.2(d), PDFp13. It does not challenge TheoremsA/B, establish an actual zeta matrix counterexample, or refute the later specific four-moment conditional calculation.

## Precise source question

The source says that when normalized moments d^(-1)trG^k through2m are known, the sharp lower bound for n_+(G)/d is1−Lambda_m(0), calling Lambda_m the Christoffel function of the moment sequence at0. For the ordinary definition

Lambda_m(0)=inf{integral p(x)^2 dmu(x):deg p<=m,p(0)=1},

this is not a general bound on an arbitrary Hermitian matrix's positive inertia. It bounds an atom at0; a negative-halfline bound needs the additional property that the selected polynomial square majorizes1 on that halfline. The source introduces these observations as informal, and could intend a narrower moment class. The exact intended hypothesis should be resolved before recording a source error.

## Explicit nonsingular example with the same first two main moments

Let G be66-by66 diagonal, with eigenvalues−1 repeated5times,1 repeated11times, and6/5 repeated50times. Its normalized spectral moments are

m0=1,m1=1,m2=4/3,m3=7/5,m4=136/75.

The positive inertia fraction is61/66. Its degree2 moment Gram matrix is positive definite: a nonzero degree2 polynomial cannot vanish on all three distinct support points with positive weights.

Put p_*(x)=1+(12/103)x−(85/103)x². Exact moment arithmetic gives

integral x p_* dmu=0,

integral x²p_* dmu=0,

integral p_*²dmu=5/309.

For any other polynomialp of degree<=2 withp(0)=1, p−p_* lies inspan{x,x²}. Orthogonality therefore gives integral p²=integral p_*²+integral(p−p_*)², proving the exact ordinary Christoffel valueLambda_2(0)=5/309. Consequently

1−Lambda_2(0)=304/309>61/66=n_+(G)/66,

with difference135/2266. The purported unrestricted one-sided bound fails. In particular m1=1 andm2=4/3, the source's first two leading normalized moments, are not enough to repair the general assertion. This example is only a Hermitian moment counterexample; the full zeta sampling/block/prime hypotheses have not been modeled and are not claimed to hold.

The mechanism is visible directly: p_*(-1)=6/103, so p_*² is much less than1 on a negative spectral point. It is not a majorant of1_{x<=0}. Ordinary Christoffel minimization imposes no such constraint.

## The source's specific four-moment consequence survives

For the particular moments subsequently proposed underHL*(4),

(m0,m1,m2,m3,m4)=(1,1,4/3,2,13/4),

the minimum polynomial is

p(x)=1−7x/4+2x²/3.

Its moment orthogonality to x,x² is exact, and integral p²=5/36. Unlike the counterexample polynomial, p(x)>=1 for everyx<=0, because both−7x/4 and2x²/3 are nonnegative there. Thus p² is a valid negative-halfline majorant and gives

n_+(G)/d>=31/36

for these exact moments. With the source's asymptotic moment errors it gives31/36−o(1). The same source counting step n_+(G)<=s1+s2+pairs andN>=s1+2s2+2pairs yields s1/N>=13/18−o(1), provided d/N->1 and the separately stated moment/identification assumptions hold. This independently validates the finite polynomial arithmetic of that conditional consequence, not its conjectural analytic premise.

## Sufficient correction and next step

Replace the unrestricted Christoffel sentence with an explicit one-sided polynomial optimization: choose a real polynomialq of degree<=2m withq(x)>=1 forx<=0 andq(x)>=0 forx>0. Then (d−n_+(G))/d<=sum_k q_k m_k. A squared Christoffel minimizer supplies such a certificate only if its halfline majorization is separately checked; positive roots of its normalized factor are a sufficient condition in the usual positive-Radau situation. Establishing sharpness requires its own moment-problem hypotheses and is not inferred from the certificate alone.

The ordinary Christoffel-versus-halfline distinction is classical, with no novelty claim. The reusable knowledge here is the exact witness and the explicit preservation of the source's later special-case bound. Arithmetic is reproducible via experiments/code/christoffel_one_sided_scope.py; observed exact output is experiments/results/christoffel_one_sided_scope.json. No numerical agreement is used as proof. The director accepted this scoped qualification after checking this witness and an independently derived different8-point witness. It is classified as an insufficiently stated hypothesis/ambiguity in the informal generic remark, not a false main theorem.

Independent different-witness review and further regular-quadrature analysis: audits/adversarial_reviews/christoffel_independent_third_round3.md. Those additional general sharpness claims have their own stated regularity conditions; they are not silently included in the elementary one-sided certificate above.
