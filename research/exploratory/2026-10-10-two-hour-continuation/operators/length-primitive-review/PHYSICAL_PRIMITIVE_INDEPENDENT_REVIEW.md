# Independent physical primitive synthesis audit

Status: ACCEPT the analytic adapter and its directed complete synthesis bound;
the native positivity consequence remains conditional on the owner's completed
full-R artifact and accepted fresh weighted lower gate.
Scope: the exact physical length L=21/20, ten exact native Galerkin columns,
and the quantitative consequence for all shorter intervals by zero extension.
This review performs no continuum integration and certifies no new form sign.

## Frozen sources

Read in full, with SHA-256 checked against the frozen bytes:

- `../PHYSICAL_LENGTH_PRIMITIVE_COMPLETION.md`:
  `cdceae6052114119e13c5d9d6919847f339603a0109b279bb85a26bd989e7a7d`.
- `../enclose_length_primitive.py`:
  `2fc80bfd130ea59bb413209cd8dd092a71e4de80cc7f387c14778626cc1e560a`.
- `../physical_length_source.py`:
  `b15da7904f2bdf4f4bc7e68b8dfe2f1de808bb0bac47a905d684c513dba24f1e`.
- `../enclose_length_weighted.py`:
  `aed3e21e0784f387fb371b871389514c60671bd4f29449b07791d97ab9b77b16`.

The old native analytical source/basis helper is explicitly bound to
`b3832a0cddc8bc1e2603c40240b608d1f06a868bda9436d8e88a146393fe007b`.
The prior-wave `EXACT_PRIMITIVE_SYNTHESIS.md` and
`QUANTITATIVE_PRIMITIVE_COMPLETION.md` were reread. The separate accepted
`literature/PHYSICAL_LENGTH_SOURCE_REVIEW.md` supplies the full-source
physical adapter, residual and primitive-line scope; its continuation proof
does not claim a completed R gate.

## Analytic and implementation audit

The source basis has rows 0 through 6 equal to sin(n*pi*t/L), n=1,...,7;
rows 7,8,9 are exp(t/2), exp(-t/2), cosh(3t/2); rows 10 through 109 are
all one hundred sines with n=8,...,107. The helper's row-to-frequency map
agrees with the exact native basis. Every coefficient ball in all ten
columns is retained. No midpoint substitution is used.

Writing c=1/2, the physical Volterra operator is
G h(t)=integral_0^t cosh(c*(t-u))*h(u) du. For an exponential with a!=+-c,

    G exp(a*t) = a exp(a*t)/(a^2-c^2)
                 - exp(c*t)/(2*(a-c)) - exp(-c*t)/(2*(a+c)).

At a=+-c, its removable limit is
t exp(a*t)/2+[exp(c*t)-exp(-c*t)]/2. Combining conjugate imaginary
exponentials gives the stated sine primitive with nu=n*pi/L; combining
a=+-3/2 gives 3*sinh(3t/2)/4-sinh(t/2)/4. These identities use physical
t and require no extra scaling of G. They also follow from the Volterra
initial-value equations G(0)=0, G'(0)=h(0), G''-G/4=h'.

The helper uses precisely these complete transformations. Its six soft
functions have degrees at most one, so their full product Gram requires
degrees at most two. For all real a,
integral_0^L t^p exp(a*t) dt=L^(p+1) f^(p)(a*L); at a=0 the exact value
is L^(p+1)/(p+1). The explicit second derivative and all removable cases
are correct. Mixed cosine products use a*L+i*n*pi, with the same L or
L^2 factors. The pure cosine Gram has diagonal L/2 and zero off diagonal.
Both ordered soft product indices and the factor two on every soft/cosine
cross term are present. No normalization or mixed contribution is lost.

Hilbert-space Cauchy--Schwarz gives
||sum_i x_i G z_i||^2 <= (sum_i ||G z_i||^2)*sum_i |x_i|^2 for complex x.
It does not require the G z_i to be orthogonal. The finite native frame is
the exact L2-orthonormal frame from the source construction, unchanged in
the quantitative argument.

For B positive semidefinite, trace B<1 supplies M=1. With epsilon=10^-11,
kappa=1/2 and K=1, the independently reviewed square completion gives
theta=1/200000000001 and
min(epsilon/[2*(1+2*K)],theta*kappa/2)=1/800000000004 exactly.
Literal-kernel zero extension preserves q on shorter native intervals;
the full longer G norm dominates its restriction. Thus the asserted
conditional primitive-norm bound has the correct direction. Injectivity
gives strict positivity of nonzero tests, without a native L2 spectral gap.

The extractor hardbinds the weighted checker, invokes its fresh full
source/moment/coefficient reconstruction, checks the entire saved receipt
for equality, and only then reads any synthesis coefficient. The weighted
checker hardbinds the physical R producer, adapter and old helpers, checks
all three segments' exact panel adjacency and all 636 panels, pays the
error totals, rebuilds exact U and coefficients, retains every finite
weight correction and the complete tail, and requires strict shifted LDL.
Every guard uses explicit raises and remains active under Python -O.
This source audit does not replace the outstanding completed artifact.

## Independent directed replay

`check_physical_primitive_oracle.py`, SHA-256
`db7041952c6d811ab01256dbec8f9bf6ceb03c12b5ab859c6796e3a84ac07c44`,
freshly rebuilds the native 110-by-10 exact coefficient balls at 256 bits.
It expands each native source exponential using the general Volterra
formula above, producing the complete 220 complex exponential/soft terms.
It integrates their full pair products by the independent physical
recurrence J_0=(exp(aL)-1)/a and
J_p=(L^p exp(aL)-p J_(p-1))/a, with exact zero-rate limits. This uses
1727 whole product-moment keys and no quadrature, sampled values or
six-soft/cosine coefficient transformation from the owner's helper.

All ten real positive squared-norm balls overlap the owner's individual
balls. The independently enclosed complete synthesis trace is

    [0.56404002429815044767191707549966505459175022907590868247572051061
     +/- 1.12e-19] < 1.

The frozen owner's trace-only artifact also overlaps. Hence K=1 is accepted
for these exact source-defined columns even while the R gate is pending.
The source coefficient reconstruction remains the reviewed native source
dependency; this is an independent primitive transform/product calculation,
not an independent derivation of the entire source form.

From `/workspace/riemann`, both commands exited 0:

    /workspace/.riemann-tools/python/bin/python3 -B research/exploratory/2026-10-10-two-hour-continuation/operators/length-primitive-review/check_physical_primitive_oracle.py --output /tmp/physical-primitive-oracle.final.normal.json
    /workspace/.riemann-tools/python/bin/python3 -B -O research/exploratory/2026-10-10-two-hour-continuation/operators/length-primitive-review/check_physical_primitive_oracle.py --output /tmp/physical-primitive-oracle.final.optimized.json

The frozen `results/primitive-oracle.normal.json` and optimized twin are
byte-identical, SHA-256
`d7e64b7461417165fa6e5bed4cefbc75c34f268c120b23cbb4035c6241e93717`.
No full-R integration, completed weighted gate, new form sign, sign at
log 3, all-window positivity or RH conclusion is claimed by this receipt.
No previous wave bytes or Git state were changed.
