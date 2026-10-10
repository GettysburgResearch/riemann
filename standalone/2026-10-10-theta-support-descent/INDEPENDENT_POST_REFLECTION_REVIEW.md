# Independent review of the reflected Euler continuation

**Verdict:** no load-bearing gap found in
`POST_REFLECTION_EULER_CONTINUATION.md` at SHA-256
`7ddcaf96aba2f109fb5696880ed9098e435712e2075613e72474b76fc00a3072`.
The good-prime phase calculation, exact Mellin scalar, finite-ray
decomposition, signed Euler extraction, normally convergent cusp series,
polar statement, and residue formula check at the stated
source-conditional scope. The joint polynomial bound in the zero-free
refinement also checks.

**Independence:** the reviewer is a separate agent that did not author
the post-reflection proof. The review independently reconstructed the
source character exponents, Gauss identities, CRT signs, Mellin
normalization, and analytic domains. An exposition clarification about
the order of chi_p(-1) was identified, corrected by the author, and
checked in the final source; no formula changed. The proof file was not
edited by this reviewer. This is an independent AI-agent review, not an external
human review or a formal proof certificate.

**Scope and dependency boundary:** the source theta automorphy, cusp
coefficient formulas and bounds, and exact finite local transformations
are assumed from the retained October 5 paper. The review checks their
application and the new deductions. The meromorphic continuation uses
ordinary continuation of fixed finite-order Hecke L-functions. The
pole-free refinement additionally assumes the stated common finite-order
zero-free half-plane. No angular reciprocal theorem is required for this
post-reflection result. There is no higher-moment or RH conclusion.

This is a distinct review object from
`INDEPENDENT_JOINT_SERIES_REVIEW.md`: the earlier report covers the
normally convergent completed-divisor representation on its original
domain to the right of v=1. The present report covers the new signed
Euler argument through that boundary. Neither result is silently
strengthened by the other.

## 1. Exact content and source identities

The repository base at review was PR #915 at
`9959364671f89b86f3992ec5ed5e19f804eb607b`. The new work was reviewed
by content hash before its new source commit was frozen. An exact-head
receipt must subsequently compare committed blobs with these contents.

| File, relative to this packet | SHA-256 |
| --- | --- |
| `POST_REFLECTION_EULER_CONTINUATION.md` | `7ddcaf96aba2f109fb5696880ed9098e435712e2075613e72474b76fc00a3072` |
| `DEFORMED_GAUSS_CONTINUATION.md` | `b01b17194884b3e2331d9f668ee71abb33a5e2f1e047d16cb2e906a1c5b32c81` |
| `HIGHER_ANGULAR_SECOND_MOMENT.md` | `82edbaed050710fcdbfa65c20a39cc83338e9f283473462c1756ea717f035959` |
| `EULER_DOMAIN_EXTENSION.md` | `56ab7e05b0fde19c82eeea5f274da212bf63f07ac084de1b08c3d8c48aa78a2a` |

The primary source is OpenAI/math commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`, physically retained at

`standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex`.

Its SHA-256 was independently recomputed as
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
The relevant source passages were read directly, including
`eq:ray-local-transform`, `eq:ray-multiplier`,
`eq:ray-additive-crt`, `eq:theta-cusp-coordinates`,
`eq:ray-mellin`, `eq:theta-mellin-functional-equation`,
`eq:dual-cusp-mellin-series`, the Gauss–Jacobi identities, and the
three-cusp Fourier support and coefficient estimates.

The inherited definition files and their hashes are also recorded in
the joint-series review. This pass does not reverify the entire upstream
paper, its second-moment induction, or its Lean implementation.

## 2. The exact theorem that survives review

Put sigma=Re(s), nu=Re(v), and w=v-3s+3/2. The new domain is

\[
\nu>\tfrac12,\qquad \sigma<0,\qquad \sigma<\nu-1.
\]

The complete original standard-face object has the meromorphic
representation (4.12) on this domain. Its possible poles are confined
to zeros of finitely many fixed finite-order functions L_S(v,zeta),
and to v=1 if the original kappa is principal. The moving Euler
deletions at k introduce no zeros at these positive real parts.

If every zeta in the fixed finite family has the inherited common
zero-free boundary beta<1, the representation is holomorphic for
nu>beta except for a possible simple principal-kappa pole at v=1.
The residue formula in (5.2) is a normally convergent expression and
may be zero. On closed bounded real subregions with strict margins,
the pole-removed function has the claimed polynomial vertical bound
and conductor cost `Q^(1-2 sigma+epsilon)`.

The object starts on the standard infinity-cusp face. Its continuation
contains all three reflected cusp sequences. This does not claim an
estimate for every original face or for a full higher moment.

## 3. Independent good-prime scalar reconstruction

For the local exponent j=3, substitute
`sigma_p=lambda^2(c/p)` and
`epsilon_p=-lambda^(-5)(c/p)^(-2)` in the source local transform.
The character exponents before simplification are:

| Character value | Exponent | Simplification |
| --- | --- | --- |
| chi_p(-1) | 3-5=-2 | one, because chi_p(-1)^2=1 |
| chi_p(lambda) | -4+25=21 | exponent 3 modulo six |
| chi_p(c/p) | -2+10=8 | exponent 2 modulo six |

Thus the first line of equation (2.4) is correct. The final proof names
the separate order-two fact in the first row before reducing the other
two exponents modulo six. This corrected exposition changes neither
the formula nor its hypotheses. Reversing exactly that sentence
restored the previously reviewed content hash
`53aa1b5b747688cd2dd1aa313f8c984984571d05db2f7074a38d9aa1873552be`,
independently confirming that no other source text changed in the
final revision.

The prime Gauss identities imply

\[
\gamma_3(p)\gamma_5(p)
 =-\overline{\alpha(p)}\chi_p(-4)\gamma_2(p).
\]

In particular the minus sign in that formula is required. The
normalized CRT formula uses the positive character power
`product_(p|a) chi_p(a/p)^j`; it does not use its inverse. One can
check the sign by the substitution x=b y+a z in the finite Gauss sum
for two coprime moduli a,b.

Applying that CRT formula gives the k product in (2.7). For the d
product the exponent -2 is congruent to 4 modulo six, giving exactly
`gamma_4(d) chi_d(t0 k)^(-2)`. Cubic reciprocity cancels the cross
symbols `chi_k(d)^2 chi_d(k)^(-2)`. Multiplication by the plus
derivative scalar alpha(c) squared leaves precisely the displayed
unit-modulus row factor Gamma_(c0)(k), together with
`alpha(d)^2 gamma_4(d) chi_d(t0)^(-2)`.

The exterior d coefficient contains
`gamma_2(d) alpha(d)^(-2)`. Its angular part cancels against
alpha(d) squared, and `gamma_2(d) gamma_4(d)=1` cancels the remaining
Gauss factor. This latter identity is valid for squarefree composite d
as well as for a prime: the CRT character powers add to six, and the
cubic character is one at -1.

The residual d phase is the fixed finite character in (2.12). It is
not automatically eta rho cubed. The quadratic row factors in the
exterior coefficient cancel only to their literal coprimality mask;
the restriction (d,kS)=1 was retained throughout.

The unabsorbed j=4 dual factor remains

\[
q^{-1/2}(-1+q\mathbf1_{p\mid m}).
\]

Therefore d coprime to m carries mu(d). That sign is not canceled by
the preceding Gauss identity. It is exactly the sign that produces
the reciprocal finite-order L-function below. The surviving row
character is the sextic `chi_k(m)`, as equation (2.13) states.

Finally, the three d norm contributions are

\[
(Nd)^{-(w+s-1)}(Nd)^{1-2s}(Nd)^{-1/2}
 =(Nd)^{-v}.
\]

This confirms both the argument v of the reflected divisor series
and the absence of any unrecorded norm factor in its coefficients.

## 4. Finite labels and the Mellin constant

The original finite multiplier is rho on good primary elements. The
supplementary cubic factor is already present in the standard theta
coefficient, so inserting vartheta a second time in the finite
multiplier would be wrong. The normalized Fourier coefficient in
(3.1) matches the source convention.

After fixing h0 and the appropriate bad-modulus residue of d, the
source cusp sequence, additive character, reduced bad denominator,
and bad multiplier belong to a fixed finite family. Their dependence
on the residue of k is retained. Expanding the d residue condition
by the full finite group character identity is exact. Restricting to
the nonempty primary residue classes does not change that identity.
On the chosen unique primary generators these character restrictions
are completely multiplicative ideal characters of a fixed finite ray
modulus, enlarged by the fixed primary modulus if necessary.

Consequently the zeta labels have fixed finite order and conductors
independent of k. They are independent of the dual Fourier index m,
which is essential for taking 1/L(v,zeta) outside the cusp sum. The
row scalar Gamma_(c0)(k) has modulus one. The remaining norm factor
in K_b(s,k) involves only the fixed bad denominator.

I independently checked the sign and the powers of 27 and 2 pi in
H(s). The primal plus Mellin integral is the negative of its positive
normalizing factor times T_(k,d). The plus derivative functional
equation also has a minus sign. These cancel, and the dual minus
Mellin series contributes i. Dividing the two Mellin normalizations
gives exactly

\[
\frac{i}{3^{5/2}}27^{-s}(2\pi)^{4s-2}
\frac{\Gamma(4/3-s)\Gamma(5/3-s)}
     {\Gamma(s+1/3)\Gamma(s+2/3)}.
\]

This is holomorphic on Re(s)<0. Its denominator gamma factors create
zeros, and its numerator has no poles there. On a fixed closed left
strip the exponential parts of Stirling's formula cancel, giving
polynomial vertical growth of order `2-4 Re(s)`.

The reflected identity first holds in sigma<0, nu>1. Fubini in that
overlap is legitimate: the previous theorem's absolute dual-cusp
majorant is `(Nd)^(-1/2+epsilon)`, and the remaining exterior norm
powers turn the d majorant into `(Nd)^(-nu+epsilon)`. Choose epsilon
smaller than nu-1 on a fixed compact subset. This establishes absolute
convergence of the double series before its sums are interchanged.

## 5. The signed Euler product and normal cusp sum

Let D_p=1-x_p+z_p and u_p=zeta(p)q^(-v). For p not dividing m the
local divisor series is `1-u_p/D_p`; for p dividing m it is
`1+(q-1)u_p/D_p`. Factoring out 1-u_p gives the two exact factors
in (4.2). In particular,

\[
E_{p,m}-1=\frac{u_p(-x_p+z_p)}{D_p(1-u_p)}
\quad (p\nmid m).
\]

The negative sign in the generic divisor term is essential. Replacing
this factor by 1+u_p/D_p would extract a different L-function and
would invalidate the continuation and pole analysis.

The new domain implies Re(w)>2. Consequently

\[
|x_p|+|z_p|<\tfrac14+\tfrac1{\sqrt2}<1.
\]

This proves that no D_p denominator vanishes in the claimed domain.
Also |u_p|<1. The prime error is therefore uniformly
`O(q^(-Re(w)-Re(v))+q^(-2 Re(v)))`, which is normally summable
for Re(v)>1/2. The proof never divides by a possibly vanishing
remainder factor.

At an m-prime the local factor costs at most a fixed constant times
`q^max(0,1-Re(v))`. Its product is bounded by
`(Nm)^(max(0,1-Re(v))+epsilon)`, also when m has repeated prime
factors. Only its radical enters the finite product. Removing primes
of k or m from the infinite majorant does not enlarge that majorant.

Write a=max(0,1-nu). Since m=lambda^4 ell has norm 81 Nell, the
absolute cusp series is controlled by the source theta coefficient
sum at exponent `1-sigma-a-epsilon`. This is greater than one
precisely with a strict margin in

\[
\sigma<0,\qquad \sigma<\nu-1.
\]

The ramified and unit faces are included in this argument. Normal
convergence gives joint holomorphy of every B_b, uniformly in k and
the two imaginary parts on the specified real subregions. Extracting
the finite reciprocal L-functions after this holomorphic summation
establishes (4.12). The new domain and its overlap with the previous
continuation are connected, so the identity continues the same
original object.

## 6. Poles, vertical growth, and the residue

There are no missing polar factors in (4.12). The angular reciprocal
at w remains in its absolute Euler half-plane. The old remainder,
the new cusp sums, H, and the finite bad-denominator factors are
holomorphic. The moving k Euler factors of L(v,zeta) can vanish
only at real part zero. Thus only the fixed finite-order reciprocal
zeros and the possible original principal-kappa pole remain.

The polynomial reciprocal bound used in the beta refinement is
valid. In the principal case the function
`F(v)=(v-1)L_S(v,1)/(v+1)` is holomorphic and nonzero on the stated
half-plane, including its nonzero removable value at one. For the
nonprincipal case take F=L_S(v,zeta). A zero-free disk extending
from the Euler half-plane to a fixed interior target has a logarithm
with bounded central value. The polynomial upper bound for F gives
an upper bound for the real part of that logarithm; Borel–Caratheodory
then controls the entire logarithm on an inner disk. Exponentiating
its negative yields the claimed polynomial reciprocal estimate.
No lower bound for L is assumed in that argument.

The finite family makes these constants uniform across the labels.
The moving Euler masks and their reciprocals cost Q^epsilon, while
the absolute remainder and cusp-sum bounds are independent of both
imaginary parts. Stirling's estimate for H supplies the only necessary
growth in Im(s) apart from fixed normalizations. This proves the
joint bound (4.15), after removing the possible simple pole with
v-1. The raw meromorphic statement alone would not give such a
bound near its allowed reciprocal poles; the proof correctly confines
this vertical assertion to the zero-free refinement.

For fixed Re(s)<0, a neighborhood of v=1 lies in the new domain.
The cusp sums converge normally there, so multiplication by v-1 and
passage to the limit inside them is valid. All the factors in (5.2)
then follow directly from (4.12). The principal reciprocal has value
zero at v=1. Nonprincipal terms use their ordinary nonzero L-values
there, with every k and S mask retained. The product of local residue
factors counts each prime in kS only once.

The residue can vanish because of a principal reflected label or
because of cancellations among the remaining labels. The special
case zeta=kappa gives combined local factors 1-x away from m and
1-x+qz at m. Those identities check, but they do not identify every
finite label with kappa. The proof makes no unsupported nonvanishing
or diagonal-identification claim.

## 7. Scope of the advance and checks performed

The result crosses the former v=1 summability boundary by a new
signed Euler argument. It does not obtain a conductor saving. The
literal scalar still cancels the reflected row factor
`Q^(1-2 sigma)` to leave balanced cost `D^(nu-2 sigma)`.
For nu<=1 the allowed sigma satisfies
`nu-2 sigma>2-nu>=1`; for nu>1 the cost exceeds D^nu. Thus the
absolute estimate is worse than D throughout this domain. The
remaining sextic row character cannot be replaced by a quadratic
one to claim a stronger subsequent row bound.

The final weight paragraph correctly distinguishes the standalone
Mellin convergence domain from the product after multiplication by
H(s), whose zeros can cancel gamma poles. The example crossing with
`-1/3<sigma<nu-1` is nonempty for
`max(beta,2/3)<nu<1`. It is a legitimate domain observation,
not a favorable moment contour estimate.

Independent inline standard-library Python checks, using exact sparse
polynomial arithmetic with `Fraction` coefficients, verified the
generic and exceptional Euler remainder identities and both matched
zeta=kappa local identities. Exact modular arithmetic checked the
exponent-3 character reductions and the exponent-4 CRT power. Exact
rational arithmetic checked the d norm exponent and the balanced
boundary exponent. All residual checks passed. These are algebra
checks; they neither authenticate the imported theta source nor
prove a higher moment.

**Accepted review scope:** the exact scalar and reflected identity,
the specified meromorphic continuation, its conditional zero-free
refinement and joint vertical estimate, and the convergent possible
residue formula. The source theta inputs and the finite-order
zero-free theorem remain explicit dependencies. The full fourth
moment, generalized moment hierarchy, and RH remain open.
