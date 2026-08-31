# Independent review: proper native theta-source real zeros

Verdict: **PASS** on exact scientific commit
`0d1f90323c8d61abefee077b7bcaa4c024596a55`, immediate parent
`628f3c1672afaf1e2c3c8eb2e94ed7b78022c447`.
Review date: 2026-08-31.

This is a non-author mathematical review of the complete 196-line
[corollary](PROPER_THETA_SOURCE_REAL_ZERO_COROLLARY.md). This reviewer did
not contribute its argument or its pre-freeze critique. The science has
not been edited. Acceptance is an analytic deduction from the two exact
accepted parents below, not an extrapolation from finite tests.

## 1. Exact source and inherited theorem identities

The corollary's Git blob is
`efdbb5869803d0876b0cc41b92cae6cbce870d6d`.
Its complete normalized-LF SHA256 is
`22cbe2797ac06ae37468e4da93d17b261d99675f50255fd6a2c67bf53ca1f70f`.

The two science/review pairs are:

| Parent | Scientific commit | Independent review commit |
|---|---|---|
| MP theta-source completion | `fdd349dcf6ba1b104e27866ae66b4c89752d5f05` | `8b2bb44f3b82059b6e3721aba9b2cff2a70fd7d0` |
| DL fixed-depth native norm | `070751bf7e96c1dbd6d4b3cfbb05dc70f5a2aa22` | `c29ae6f3d134e076fa41aef9ae39920478f16ac0` |

The complete MP and DL proofs and their complete independent reviews were
read. The load-bearing imports are MP Sections 1--2, especially MP5--MP12,
and DL Section 2, DL5--DL10 and its final Petersson norm conclusion.
No period-side divisor-cluster theorem is needed for this corollary.

The following resident files agree byte-for-byte after LF normalization
with their exact frozen source or review commits:

| File | Normalized-LF SHA256 |
|---|---|
| [MP proof](CUSP_MATRIX_PERIOD_POSITIVITY.md) | `fabb13f35e0f6a45ddbc3b5f54f0376e9c0aec5d75b44ae9b4ae10cf17136c0c` |
| [MP review](CUSP_MATRIX_PERIOD_POSITIVITY_REVIEW_FDD349DC.md) | `d4340708d1e349e52f5138d55624c1b5ced53edee06f66660a4143f1fb97d335` |
| [DL proof](CUSP_FLAG_FIXED_DEPTH_DIVISOR_LADDER.md) | `be346d4cb35af90ac3f6e3b298d0e40e743d59d48688d3f4da42e50f2b3a812e` |
| [DL review](CUSP_FLAG_FIXED_DEPTH_DIVISOR_LADDER_AUDIT.md) | `92bd1e1c7fb26a2bce9a6264f0dbe792ea4f6cf46f4d3229025a575b785aab98` |

All four commits are ancestors of the corollary science. Each parent
review descends from its paired scientific commit. The corollary's entire
parent-to-science delta is its one new Markdown file.

## 2. The quotient and the uniform cusp bound

For d=dim S_k and d>=j+1, the native coefficient chart proves that
V_(k,j) has dimension d-j+1 and its coefficient kernel W_(k,j) has
dimension d-j>=1. The functional ell_j is surjective, with the actual
modular lift h_j satisfying ell_j(h_j)=1. Thus V/W is one-dimensional
and W is genuinely nonzero. This is not a one-dimensional restriction
disguised as a quotient. The quotient coordinate, Petersson form and
Fourier coordinate are fixed independently of s and t.

The source is H(t)=G+2B(t), including the Petersson vacuum. MP gives
H(t)=t^(-1)H(1/t). Quotient homogeneity gives the corresponding law for
H_Q, and C_Q=(H_Q-G_Q)/2 is strictly positive and rapidly decaying.
Consequently MP12 supplies TQ1 with exactly G_Q/[2s(s-1)], not a
different half-factor or a separately transformed divergent vacuum.
This construction occurs before Mellin observation; it is not I(s)/W.

On the full cusp rectangle y>=1, retaining only the m=0 lattice line
and applying Gaussian Poisson summation gives Theta_z(t)>=sqrt(y/t).
Its independence of x is essential. For every complex-valued admissible
modular form, Parseval on the full unit x interval gives

    integral_x |f(x+iy)|^2 dx
      = sum_(n>=j) |a_f(n)|^2 exp(-4pi n y)
      >= exp(-4pi j y).

Multiplication by the Petersson density y^(k-2) therefore gives the
power y^(k-3/2), and hence exactly

    H(t)[f] >= t^(-1/2) Gamma(k-1/2,4pi j)/(4pi j)^(k-1/2).

Positivity justifies both the domain restriction and the retained theta
summands. Crucially this is a common lower bound for EVERY member of the
affine space ell_j=1. Taking its minimum proves H_Q(t)>=J/sqrt(t).
There is no interchange of an integral and a minimum, and no need for
one minimizing lift to work at every t. Increasing ambient dimension
introduces no factor into this lower bound.

## 3. Native norm asymptotic, with the complete tails retained

The same Parseval bound without theta gives
G_Q>=A_j Gamma(k-1,4pi j)/Gamma(k-1). For the opposite bound, take
DL's fixed partial chart with J=j; its h_j is the actual modular g_j,
not a free Fourier vector. It belongs to the required affine space.

Here is an independent reconstruction of the norm step used in TQ9.
Put N=j+1 and take DL's Y=k/(10000N). Eventually Y>=1 and the entire
q-tail estimate applies on the full high rectangle. Writing
h_j=q^j+u, the first Fourier index of u is at least N. Parseval therefore
eliminates the cross term with q^j EXACTLY on that rectangle. DL7 gives

    integral_high y^(k-2)|u|^2 <= B_j^2 k^(2j) A_N.

DL8--DL9 bound the complete low-domain h_j norm and the omitted low
pure-q integral by a polynomial in k times 10^(-k) A_N. Consequently

    G[h_j]=A_j+O_j(polynomial(k) A_(j+1))=A_j(1+o(1)),

because A_(j+1)/A_j=(j/(j+1))^(k-1). This uses the convergent full
complex-q-disc bound and Cauchy estimate in DL, not a sampled prefix.
The constants may depend on fixed j but not on growing d.
The six residues r=0,4,6,8,10,14 cover all sufficiently large even
weights; the class 2 modulo 12 correctly uses r=14. Finitely many
class-dependent thresholds can be replaced by their maximum.

For a fixed cutoff x=4pi j and a positive real p tending to infinity,

    0 <= Gamma(p)-Gamma(p,x) <= x^p/p.

Dividing by Gamma(p) and using its factorial-scale growth proves the
two incomplete/full Gamma limits required here. Squeezing between the
native lower and upper norm bounds yields G_Q/A_j->1. Finally
[DLMF 5.11.12](https://dlmf.nist.gov/5.11.E12), personally checked in
its positive-real large-argument domain, gives

    J/G_Q ~ Gamma(k-1/2)/(sqrt(4pi j) Gamma(k-1))
          ~ sqrt(k/(4pi j)) -> infinity.

The Gamma asymptotic is a classical analytic input, not an offline
machine-certified source or an effective numerical threshold.

## 4. The central inequality and the actual zeros

At s=1/2 the endpoint term equals -2G_Q. For B>1, positivity of the
ACTUAL C_Q permits discarding the tail beyond B. Only on [1,B] is the
possibly negative lower bound (J/sqrt(t)-G_Q)/2 substituted. Thus

    L(1/2) >= -2G_Q + integral_1^B (J/t-G_Q/sqrt(t)) dt
             = J log B - 2G_Q sqrt(B).

The constants cancel exactly; no residual +2G_Q is missing. With
R=J/G_Q>1, B=R^2 gives L(1/2)/G_Q>=2R(log R-1). Therefore R>e is a
valid sufficient condition, and the fixed choice B=e^2 gives the same
strict-positivity criterion. It is not asserted to be necessary.
The native norm asymptotic proves this condition eventually for each
fixed j. In particular an asymptotic scale is not a certified onset.

MP's continuation makes L real analytic on (0,1), with no poles there.
Its nonzero residue +G_Q/2 at one makes L(s) tend to negative infinity
from the left. A positive central value and this negative endpoint
behavior force a sign-changing zero in (1/2,1). Analyticity and
nonidentity imply isolation, and at least one such zero has odd order.
Reflection supplies the distinct zero in (0,1/2), with the same order.
The factor s(s-1) is nonzero at both, so pole clearing preserves them.
No reduced denominator or period-Schur cancellation is being presumed.

## 5. Accepted scope and verification boundary

PASS is for every fixed j followed by all sufficiently large even k:
positive central value and a reflected pair of genuine odd-order real
off-central zeros of the proper theta-source quotient and its entire
pole-cleared completion. Its positive Mellin feature kernel retains
the MP domain Re z,Re w>1/2; that property does not prohibit these zeros.

This proves no simplicity, uniqueness, 12j/k location law, effective
weight threshold, proper weight-24 statement, or uniform result for
j growing with k. It supplies neither a Hecke-stable flag nor an Euler
product or new automorphic L-function, and is not an RH/GRH counterexample.
The prior period-side divisors remain different objects.

This review adds one Markdown note only. No numerical search, new test
module, producer or finite certificate is introduced. The existing G
computational panel counts do not increase; those suites were not rerun
for this analytic-only review. The byte/ancestry checks above are
provenance checks, not a machine proof of the infinite analytic theorem.
No source, programme front, remote ref, PR or main branch was modified.
