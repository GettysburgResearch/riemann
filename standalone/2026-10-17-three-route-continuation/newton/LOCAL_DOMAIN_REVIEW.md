# Cross-review: exact local correction and diagonal extraction

Status: **No mathematical defect found in the stated local component.**
This review checks the source specialization, the complete valuation
enumeration, the analytic product estimates and the fixed-order derivative
argument. It does not authorize or establish a new global theta contour
comparison, a new zero-free boundary, or a bound for a signed physical
finite part.

## Reviewed contents

The stable files under `research_work/critical/` are:

| File | SHA-256 |
|---|---|
| `LOCAL_DOMAIN.md` | `42a501853f5ded88ef3d2f601306a4a377d0995974c5a65452537fab884f8f78` |
| `verify_local_domain.py` | `2f8130097b533a4860cafb08f93403fe4e30e7dfba65e3e510162274c84a10e2` |

I compared the load-bearing formulas against the independently fetched
primary source, OpenAI/math commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/05-poisson.tex`,
Git blob `c8526f74b281d37fda034c17195c4bb5afd5f79b`. The relevant source
labels are `eq:exact-Euler-factor`, `eq:C-local-values`,
`eq:Euler-good-exact`, and the following definition of the correction.
The source was fetched during the earlier principal-diagonal review and
its exact local formulas were reread for this review.

## 1. Source specialization and valuation table

The principal-target specialization is correct. It gives
gamma Phi tau_1=-sqrt(Q), while retaining the angular phase Phi. The
unit phase alpha=chi_p(u/p^j) remains defined at a bad prime, although
the two extracted L-function Euler variables both vanish there. These
are distinct conventions and the proof keeps them distinct.

The t=0 absent-modulus convention and the tau_0=-1 unit-mask convention
are both retained. The latter is necessary for the positive DP boundary
term at j=1 and the negative -rA boundary term at j=5.

All four positive-t residue classes are covered. For k=0, the only
interior residue is t=0 modulo six and the boundary pairs are
(t modulo six,j)=(0,5),(1,0),(3,2),(4,3). For k=1, the only interior
residue is t=1 modulo six and the boundary pairs are
(0,0),(1,1),(3,3),(4,4). The t=0 tail accounts separately for k>0 at
j=0,m=0; no positive-t k>=2 term survives.

Direct substitution into the source coefficients gives every displayed
T_j. In particular, the j=3 terms have respectively Q^(3/2)tau_4 and
Q tau_1 tau_2 before their common phase and D/P factors. The j=4 term
has Q^(3/2)tau_1 tau_3. The j=5 term is -Phi^6 Q^3 D^6=-rA. The interior
k=1 term is -(Q-1)DP, with an additional V exactly for j=0,1. These
checks confirm both the signs and the square-root powers behind the
improved estimates.

Increasing t by six, l by two and m by one multiplies each surviving
branch by E=Phi^6 Q^4 D^6 V. The initial indices stated in the proof
account for the exceptions EW at the good-prime k=1 boundary and -rA
at j=5. Together with the additional V progression in each interior
sum, this is a complete infinite enumeration. Summing it gives the
displayed F_j and H_j, including

    H_1=(1-rE+(1-QV)DP)/(1-E).

No shared-prime cell or nonunit zero has been dropped.

## 2. Enlarged domain for the original correction

The five good-prime error exponents in equation (13) are summable on
the domain D. Its strict inequalities also keep all local denominators
away from zero, uniformly on each fixed-margin subdomain. For the bad
primes, the exact T_j sizes in (14) are correct. The two potentially
problematic mixed exponents are controlled by

    3x+y-2=(2x-1)+(x+y-1),
    4x+y-5/2=(3x-3/2)+(x+y-1).

Both are positive from x>1/2 and x+y>1. Thus the two old additional
conditions 3x>2 and 3x+y>5/2 are unnecessary for this local correction
bound. No new cancellation between different terms is assumed.

The infinite good-prime product converges normally and uniformly. Only
finitely many primes are bad for each row, and their majorants need not
be summable over every prime: the cutoff argument absorbs the product
into (Nu)^eta. The proof uses the full ideal norm, since the product of
the distinct bad norms is at most Nu. This proves the stated holomorphy
and row-norm estimate on D, with uniform imaginary-part bounds.

For fixed z=2/5 or z=1/2, the simplification to x>1/2, y>0, x+y>1
is valid. This conclusion concerns the correction factor's domain.
It does not supply the separate reciprocal, numerator, residue or
tail estimates needed to move a global comparison.

## 3. Common diagonal factor and its exact cost

At good primes, D1W=DP for every row. The algebraic identity

    (1-D1W)(1+D1W/(1-D1))-1
        =D1^2 W(1-W)/(1-D1)

removes the leading mixed Euler term and gives the good-prime bound
(22). The remaining first exponent 2x+y exceeds one throughout D_star.
The four V/E exponents are controlled by the other retained inequalities.
Consequently the good-prime product for K_u is normally convergent on
the larger domain without x+y>1.

The j=1 simplification is important: it is bounded on D_star and does
not pay a factor Q^(1-x-y). At j=2,...,5 the stated bound
Q^((1-x-y)_+) follows from the explicit table. The mixed T_j terms
are smaller than this possible loss because x>1/2. Only primes whose
row valuations are at least two incur the power, so their total cost
is at most (Nu)^((1-x-y)_+/2). Constants per bad prime are absorbed
into (Nu)^eta. Multiplication by 1-DP is bounded because x+y>0.

This proves the meromorphic factorization
H_u=zeta_F^S(xi+w)K_u and the stated holomorphic K_u bound. It does not
prove nonvanishing of arbitrary K_u. The j=2 local formula confirms why
the power cost across the diagonal cannot simply be suppressed: if
x+y<1, its -(Q-1)DP term has strictly larger magnitude than the other
terms as Q grows. The proof correctly states this only as a local
observation, rather than a lower bound for the entire Euler product.

## 4. Transverse derivatives and replay scope

The fixed-order derivative estimate is sound. A common fixed analytic
neighborhood is established first. On the smaller circle of radius
min(r0,1/log(2+Nu)), the possible crossing loss is bounded by exp(1/2).
Cauchy's formula then costs at most a fixed power of log(2+Nu), absorbed
into the remaining arbitrarily small norm loss. This is a bound for
derivatives of K_u on the diagonal, after extracting its common pole;
it is not a bound for H_u itself there or for a renormalized physical
theta projection.

I ran `python3 research_work/critical/verify_local_domain.py` once at
the hashes above. It passed 1161 exact checks. I inspected the Laurent
polynomial arithmetic, the imposed phase relations, the source coefficient
function, the branch list, the assembled numerators and the negative
controls. Explicit `require` checks remain active under optimized Python.
The finite support representatives alone do not prove infinite coverage;
the written residue enumeration and common-period argument provide that
step. The checker does not verify the metaplectic construction or global
Poisson identity, and this review makes no such replay claim.

No change to the existing theta comparison domain or boundary follows
automatically from this component. Any such new composition must receive
its own complete contour and source review.
