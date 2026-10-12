# An off-real occurrence gives a finite Hankel witness with its entire tail paid

Status: complete proposed analytic theorem; no actual-Xi negative witness.
Scope: a complete paired zero source with summable inverse-square nodes,
integer multiplicities and conjugate symmetry. No simplicity is assumed.
Exact dependencies: the complete paired product and summability established
in [HAUSDORFF_LOG_MOMENT_CRITERION.md](HAUSDORFF_LOG_MOMENT_CRITERION.md),
and the actual theta-source exclusion of imaginary-axis zeros when the final
RH equivalence is applied. The argument below is independent of a moment
representation theorem or a finite zero-count routine.
What was actually run: analytic derivation; no new native numerical experiment.
Smallest remaining gap for RH: prove that every complete native Hankel matrix
is positive semidefinite. This theorem supplies no such positivity assertion.

## FW1. Exact complete moment functional

Let the positive-real-part paired representatives of an even real entire
source be `rho`, with positive integer multiplicities `m_rho`, and assume

\[
 \sum_\rho m_\rho|\rho|^{-2}<\infty.
 \tag{FW1}
\]

The representatives are closed under conjugation; corresponding
multiplicities agree. Imaginary-axis roots are excluded. Put `x_rho=rho^-2`.
Merge identical nodes if necessary. The complete node set is conjugation
invariant, bounded, and has no accumulation point except possibly zero.
For every real polynomial P define

\[
 \mathcal L(P^2)=\sum_\rho m_\rho x_\rho P(x_\rho)^2.
 \tag{FW2}
\]

This series is absolutely convergent: P is bounded on the bounded complete
node set and FW1 pays the absolute weights. Conjugate grouping makes FW2
real. If `p_j=sum m_rho x_rho^j` and `P(x)=sum_(j=0)^d c_j x^j`, then

\[
 \mathcal L(P^2)=\sum_{i,j=0}^d c_i c_j p_{i+j+1}.
 \tag{FW3}
\]

Thus a negative value is a finite negative contraction of the complete
Hankel matrix `(p_(i+j+1))_(0<=i,j<=d)`. No finite-head proxy replaces p.

## FW2. Finite interpolation isolates a complex node

Assume an off-real representative exists. Choose one, denote it by rho,
and put `beta=rho^-2=u+iv`. Because `Re rho>0` and `Im rho!=0`, `v!=0`.
Let its merged multiplicity be m. Fix any `0<eta<|beta|`, and partition all
distinct complete nodes into

\[
 \mathcal H=\{x:|x|>\eta\},\qquad
 \mathcal T=\{x:|x|\le\eta\}.
 \tag{FW4}
\]

The head is finite by FW1 and is closed under conjugation. It contains beta
and its distinct conjugate. Form

\[
 Z(x)=\prod_{\alpha\in\mathcal H\setminus\{\beta,\bar\beta\}}
                    (x-\alpha).
 \tag{FW5}
\]

The empty product is one. Conjugate closure makes Z a real polynomial, and
`Z(beta)!=0`. Each other head node is annihilated, independently of its
multiplicity. A simple zero of Z suffices for that node's contribution to
FW2 to vanish.

For any integer M>=0 set

\[
 R_M=\frac{i\rho}{Z(\beta)\beta^M},\qquad
 B_M=\frac{\operatorname{Im}R_M}{v},\qquad
 A_M=\operatorname{Re}R_M-uB_M,
 \qquad P_M(x)=Z(x)x^M(A_M+B_Mx).
 \tag{FW6}
\]

Both coefficients are real, the determinant v is nonzero, and
`P_M(beta)=i rho`. Reality also gives
`P_M(conj beta)=conj(i rho)`. Therefore the two target contributions are
exactly

\[
 m\beta P_M(\beta)^2=-m,\qquad
 m\bar\beta P_M(\bar\beta)^2=-m.
 \tag{FW7}
\]

All remaining head contributions are zero. The target pair contributes
`-2m` for every M. No approximation or eigenvalue separation is used here.

## FW3. An explicit complete tail price

Put

\[
 K=\frac{|\rho|}{|Z(\beta)|},\qquad
 Z_\eta=\prod_{\alpha\in\mathcal H\setminus\{\beta,\bar\beta\}}
                         (\eta+|\alpha|),
 \qquad
 C_0=K Z_\eta\left(1+\frac{|u|+\eta}{|v|}\right),
 \qquad q=\frac\eta{|\beta|}<1.
 \tag{FW8}
\]

For every `|x|<=eta`, FW6 gives

\[
 |B_M|\le\frac K{|v|}|\beta|^{-M},\quad
 |A_M|\le K\left(1+\frac{|u|}{|v|}\right)|\beta|^{-M},\quad
 |Z(x)|\le Z_\eta,
 \qquad |P_M(x)|\le C_0q^M.
 \tag{FW9}
\]

Let `S_tail=sum_(x in T) m_x |x|`, finite by FW1. Every tail term, including
all complex blocks and all multiplicities, then satisfies the complete bound

\[
 \left|\sum_{x\in\mathcal T}m_x xP_M(x)^2\right|
 \le S_{\rm tail}C_0^2 q^{2M}.
 \tag{FW10}
\]

Choose a finite M with `S_tail C_0^2 q^(2M)<m`; such M exists since q<1.
An authenticated upper bound for the total sum in FW1 may replace S_tail.
Combining the exact head identity FW7 with FW10 yields

\[
 \mathcal L(P_M^2)\le-2m+S_{\rm tail}C_0^2q^{2M}<-m<0.
 \tag{FW11}
\]

The degree is at most `|H|-2+M+1`. This is a finite complete-moment witness
whose entire unselected tail is paid. There is no assumption that the target
is a largest-modulus complex node, no lower bound on its imaginary part,
and no simplicity requirement. A small `|v|` enlarges the finite constant
C0 and can increase M, but does not invalidate the argument.

## FW4. Equivalence and computable refutation boundary

If every source root is real, all inverse-square nodes are positive, and
FW2 is a sum of nonnegative terms. Every complete Hankel matrix is then
positive semidefinite. Conversely, any off-real positive-half-plane root
would give FW11, contradicting that all-order positivity. Hence, under the
imaginary-axis exclusion and FW1,

\[
 \text{every complete Hankel matrix is positive semidefinite}
 \quad\Longleftrightarrow\quad
 \text{all source zeros are real}.
 \tag{FW12}
\]

This proves the same location criterion as the bounded-GNS/pole argument
in the independently reviewed operator packet, by a direct finite filter.
Repeated real zeros still give positive weights, so simplicity is not part
of this equivalence. The imaginary-axis exclusion is essential to this
particular representative convention and RH application; it is supplied
for actual Xi by the positive theta source.

The coefficient vector in FW11 can be approximated by rational vectors:
the finite quadratic form FW3 is continuous, so strict negativity persists
for a sufficiently close rational polynomial. If all actual complete moments
admit convergent directed evaluation, an enumeration of rational coefficient
vectors, degrees and precisions therefore has a finite successful native
negative witness whenever an off-real root exists. This is a semidecision
statement conditional on such a root, not an effective RH proof or a known
actual-source counterexample. The interpolation proof itself uses the
complete spectral head as mathematical data; no claim is made that a native
zero-search has already authenticated that head.

After any finite removal of known real occurrences, FW1, conjugation and the
target pair remain intact. The same proof applies to that complete residual
moment functional. Likewise, at a fixed `t>A`, the shifted nodes
`lambda=(rho^2+t^2)^-1` satisfy the required summability and are nonreal for an
off-real positive-half-plane root. Choosing the target value `i sqrt(1/beta)`
in FW6 gives the identical shifted weighted pair contribution `-2m` and the
same complete-tail construction. This shifted Hankel criterion is stronger
than positivity of its scalar moments and distinct from the finite mixed
Hausdorff tests.

No all-order positivity premise is supplied here for the actual xi source.
The positive-Fourier and exact scalar countermodels in the cofinal obstruction
and Hausdorff notes remain compatible with this theorem: they necessarily
have a negative complete Hankel form at some finite degree.
