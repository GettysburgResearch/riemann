# Off-central numerator moments with complete columns

Status: PROPOSED deductions from the stated unconditional de Faveri large sieve
and classical Hecke functional equation. Independent mathematical review is
required. These are moments of numerator L-functions, NOT moments of 1/L or of
the native signed source. All orders below are FIXED; constants are not claimed
uniform when the order grows. No literature-priority claim is made.

## 1. Family and exact large-sieve input

Fix F containing mu_6, de Faveri's permissible S and generator choices, and one
of the fixed finite S-ray twists psi used by the CT adapter. Write q_a=N a.
A flat ideal has valuations 0,...,5 and is coprime to S. Both indices are ordered
by FULL ideal norm. De Faveri (DF), arXiv:2610.04045v1, Theorem 1.1, gives

    sum_(q_a<=U)^flat |sum_(q_b<=V)^flat lambda_b chi_a(b)|^2
       <<_eta (UV)^eta Theta(U,V) sum_b |lambda_b|^2,
    Theta(U,V)=U+V+U^(5/6)V^(1/3)+U^(1/3)V^(5/6).          (1)

Multiplication by psi(b) changes only the common column coefficients. An
arbitrary restriction on rows can be dropped AFTER fixing all column data,
by positivity. For the conjugate family, conjugate the common coefficients
and the whole sum; do not reindex a as a^5 and change its norm.

DF Section 2.5.1 identifies the primitive conductor outside S as rad(a) for a
flat row. Twisting at S does not change that exterior conductor. Thus the full
conductor Q_a satisfies 1<=Q_a<<q_a, with finitely many S/gamma types. The
characters' original zeros on common exterior primes are retained. L^S differs
from the inducing primitive L only at the fixed S; these Euler factors and
their inverses are bounded on every fixed positive real strip used below.
The finitely many principal rows can be estimated separately on those lines.

## 2. A complete-column dyadic lemma

Let k>=1 be fixed. Let d_k(v) count ordered k-tuples of integral ideals with
product v. For a common coefficient array satisfying

    |c_v| <= C_delta d_k(v) q_v^(-p)

on V<=q_v<2V, where p is fixed, the following consequence of (1) holds:

    sum_(q_a<=U)^flat |sum_(v~V) c_v psi(v) chi_a(v)|^2
       <<_(delta,k,p) (UV)^O(delta) V^(1-2p) Theta(U,V).    (2)

Smooth common bounded weights and imaginary norm powers are permitted. The
column v is NOT required to be flat. Decompose it uniquely as v=b c^6 with b
flat. Shared prime divisors of b and c are allowed. Complete multiplicativity,
including nonunit zeros, gives exactly

    chi_a(b c^6)=chi_a(b) 1_((a,c)=1).                     (3)

The fixed twist contributes psi(b)psi(c)^6, a common coefficient factor.
For fixed c, apply (1) to the b sum after retaining the row mask in (3).
The ideal divisor bound d_k(v)<<_(k,delta)q_v^delta and ideal counting imply

    sum_(b~V/q_c^6) |c_(b c^6)|^2
       << V^(1-2p+O(delta)) q_c^(-6).                    (4)

If V/q_c^6<1/2 this sum is empty. In the remaining subunit range the same
estimate holds with an absolute constant, since V/q_c^6>=1/2. This addresses
small effective lengths rather than deleting them by an asymptotic convention.
Minkowski in the row l2 norm, monotonicity of Theta, and
sum_c q_c^(-3)<infinity prove (2). The power q_c^(-3) in this step comes from
DYADIC coefficient-square counting; it is not an incorrect p-dependent
summability assumption at p=1/4. All common-prime columns and c tails remain.

## 3. The functional equation before taking the moment

**Proposed moment theorem.** For fixed k>=1, 1/2<=sigma<1, and eta>0,

    sum_(q_a<=U)^flat |L_F^S(sigma+it,psi chi_a)|^(2k)
       <<_(F,S,psi,k,sigma,eta) U^(m_k(sigma)+eta)(2+|t|)^C,
    m_k(sigma)=max(1, k(1-sigma),
                    5/6+k(2/3-sigma), 1/3+k(11/12-sigma)). (5)

For 0<eta<=1 the height exponent C may be fixed in terms of F,S,psi,k,sigma;
the implied constant may depend on eta. C is not optimized. In particular define

    sigma_k=max(1/2, 1-1/k, 2/3-1/(6k), 11/12-2/(3k)).     (6)

Then the moment at sigma_k has exponent 1. Explicitly sigma_1=1/2,
sigma_2=7/12, sigma_3=25/36, and sigma_k=1-1/k for k>=4.

**Proof.** Apply the smooth approximate functional equation to the kth POWER
of the primitive L-function, not an unweighted central polynomial extrapolated
to sigma. Its coefficients are d_k(v)chi_a(v), its conductor is Q_a^k, and its
two sums have length Q_a^(k/2) times a fixed polynomial height factor. The dual
sum has coefficients at real part 1-sigma and a prefactor of modulus

    << Q_a^(k(1/2-sigma))(2+|t|)^C.                        (7)

The primitive functional equation and finite fixed-S factors justify this
statement; fixed principal rows are treated separately because of their pole.

Here are the required separation and convergence details. Divide Q_a into
dyadic blocks Q<=Q_a<2Q, with 1<=Q<<U. Subdivide the finite gamma/S types.
On each dyadic column interval use Mellin inversion of the AFE weights to
separate Q_a from q_v. Their Mellin lines have fixed small positive real parts;
the conductor moduli cost Q^O(delta), and their imaginary factors are row
phases. The common coefficient arrays are therefore independent of a. The
polynomially weighted absolute Mellin norms are finite by the standard gamma
ratio estimates and the Gaussian auxiliary AFE weight. Its dyadic tails decay
as an arbitrarily high power of q_v/[Q^(k/2)(2+|t|)^C]. Consequently (2) sums
over ALL columns and over both AFE tails. There is no rowwise choice of an
arbitrary coefficient vector. Fixed-S factors may be expanded into their
finite polynomial factors and convergent fixed-prime geometric sums; their
constants and finite types do not grow with U. Bounding the two AFE sums
separately removes dual root-number phases legitimately.

The height-power choice can be made before the small norm losses: keep the
Mellin real parts in one fixed compact strip and the tail decay order larger
than the finitely many polynomial column powers, in terms of k and sigma. Sum
the full dyadic tail rather than demanding a fixed inverse-U error from an
U^delta truncation. Gamma-ratio powers on those compact strips are bounded
uniformly for 0<delta<=delta_0. Divisor-bound constants may deteriorate with
delta but introduce no new t power. This gives the asserted fixed C as eta
shrinks, which is sufficient for the later ordering of zero-free rectangles.

For clarity first suppress the arbitrary small losses and height powers.
A monomial U^u V^v in Theta gives original and dual block bounds

    U^u V^(v+1-2sigma),
    U^u Q^(k(1-2sigma)) V^(v+2sigma-1),                  (8)

for 1<=V<=Q^(k/2). The pairs (u,v) are
(1,0),(0,1),(5/6,1/3),(1/3,5/6). This retains the squared dual prefactor.
At the large-column endpoint, the last three terms in BOTH sums are bounded
by the corresponding three nonconstant exponents in (5). For the original
sum, a negative V exponent is instead maximized at V=1 and is <=U. For the
dual sum the V exponents are nonnegative; its first term is
U Q^(k(1/2-sigma))<=U. A negative remaining Q exponent is bounded using Q>=1,
not the invalid substitution Q=U. Positive Q powers use Q<<U. Thus every
conductor size, including bounded conductors, is covered by (5).

Equivalently set q=log_U Q and l=log_U V. Apart from fixed multiplicative
constants and harmless losses, (q,l) lies in the triangle with vertices
(0,0),(1,0),(1,k/2). Each exponent in (8) is affine on that triangle. Evaluating
these vertices gives exactly the same inequalities, including the small-Q
and short-column regimes. The checker performs this calculation for the three
orders used in PROOF.md; the algebra above establishes (5) for each fixed k.
Dyadic logarithms and the earlier Q^O(delta) and polynomial height factors are
absorbed by choosing delta small for the prescribed eta. This proves (5).

Solving its four affine inequalities for m_k<=1 yields (6). For k>=4, the
first nonconstant threshold dominates: its differences from the other two
are (2k-5)/(6k) and (k-4)/(12k), both nonnegative. QED.

## 4. Reflect to the useful numerator contours, then select rows

Apply the primitive functional equation to each numerator at y=1-sigma_k.
Its modulus costs at most U^(sigma_k-1/2) times a polynomial in height. The
same fixed-S and conjugation conventions apply. Therefore

    sum_(q_a<=U)^flat |L_F^S(1-sigma_k+it,psi chi_a)|^(2k)
       << U^(1+2k(sigma_k-1/2)+eta)(2+|t|)^C.             (9)

We use only these three exact instances:

| moment | right line | right exponent | reflected line | reflected exponent |
|---|---|---|---|---|
|2|1/2|1|1/2|1|
|4|7/12|1|5/12|4/3|
|8|3/4|1|1/4|3|

For ANY selected subset of at most U^nu rows, Holder gives first absolute
numerator-sum exponents

    r_2(nu)=(nu+1)/2             at y=1/2,
    r_4(nu)=3nu/4+1/3            at y=5/12,
    r_8(nu)=7nu/8+3/8            at y=1/4.                (10)

The subset may be selected by zeros of a different L-value of the same row.
We bound its reciprocal and correction UNIFORMLY first, then apply (10).
No independence assumption or inverse-L moment occurs. We also retain the
individual convexity cost nu+(1-y)/2 for other 0<y<=1.

## 5. Relation to the concurrent fourth-moment packet

PR #966 at 8d94494698ee447711a53dec922986586418e398 already proposes the
central fourth moment U^(7/6), a selected-count density improvement, and a
109/120 all-field composition. Its complete PROOF.md was read in this pass.
Those are not claimed as new here. Formula (5) includes that central fourth
exponent, but our gain is to choose the REAL PART before Holder, and to use the
reflected eighth moment as well. PROOF.md uses DF's original density, not
#966's improved selected-count theorem or its proposed global conclusion.

The theorem here does not bound a cofinal native critical moment. It makes
no growing-k uniformity claim and cannot be iterated to RH merely by increasing
k. MODEL.md explains the exact remaining limitation of these positive bounds.

A later live check also found #968, 14f544fb4293ffb59942ff8d345ab9d6da67025c.
Its complete NUMERATOR_MOMENTS.md was read. It already supplies the general
CENTRAL exponent kappa_k=m_k(1/2), and proposes 10/11 with central moments.
The present extension in sigma, its dual conductor weight, and off-central
contour use are distinct; central powering and its fixed-order formula are
not claimed anew. We do not adopt #968's conclusion as an input.
