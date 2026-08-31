# The native homotopy gauge requires a connection term

Status: **exact source operator and coefficient transport, with a nonvanishing
connection term, observed cancellation, and a repaired first-jet norm**.

This concerns the Euler and half-divisor homotopies already fixed in L-102706
at ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc. It is a continuation of the Euler
activation adapter at5ef9a0800e7d0f03bfef1ad4ba467f8843a90058. The derivative
below is with respect to the homotopy parameter, not the Mellin variable or
an xi-function derivative. No identification with the full T-106140 retained
principal/Wick assembly is asserted.

## 1. The exact named source gauge

On the finite labelled prime horizon let

\[
 e_\tau(x)=1-\tau x-(1-\tau)x^2,
 \quad h_\tau(x)=
 [\tau\sqrt{1-x}+(1-\tau)\sqrt{1-x^2}]^2,
\]

and E_tau=product e_tau, H_tau=product h_tau. The frozen gauge is

\[
 g_\tau(x)=
 { [\tau+(1-\tau)\sqrt{1+x}]^2\over1+(1-\tau)x},
 \quad G_\tau=\prod_rg_\tau(x_r),
 \quad H_\tau=G_\tau E_\tau.                    \tag{1}
\]

All series are finite after physical-index horizon truncation, which makes
each positive prime shift nilpotent. G_0=G_1=I, but G_tau need not
be constant inside the path. Differentiating the actual identity gives

\[
 \boxed{H'_\tau=G_\tau E'_\tau+G'_\tau E_\tau.} \tag{2}
\]

Call A_tau=G_tau E'_tau the transported Euler derivative, and B_tau=G'_tau
E_tau the connection term. A norm bound for the values G_tau does not delete
B_tau. It is not a new optional source reserve: it is part of the derivative
of the original gauge identity.

## 2. GC-1: the complete mixed-coefficient connection

Fix the labelled monomial m=x_p x_q product_(r|a)x_r^2 from the Euler adapter,
with k=omega(a)>=1, N=pq a^2, and distinct physical prime values. Keep the
two labelled67 aliases separate; exclude67 from pq a for a statement about
the entire physical coefficient after label collapse.

The local coefficients obtained directly from (1) are

\[
 [x]h_\tau=-\tau,\quad
 [x^2]h_\tau=-v(\tau),\quad
 v(\tau)=(1-\tau)(1+\tau/4),
\]
\[
 [x]g_\tau=0,\qquad[x^2]g_\tau=-\tau(1-\tau)/4.
                                                               \tag{3}
\]

For example the first identity for h follows by squaring the two displayed
square-root series through degree2; it does not import a fitted coefficient.
The product rule at every derivative site now gives

\[
 \begin{aligned}
 [m]A_\tau&=\mu(a)
       [2\tau v^k-k\tau^2v^{k-1}],\\
 [m]B_\tau&={\mu(a)k\over4}
       \tau^2(1-2\tau)v^{k-1},\\
 [m]H'_\tau&={d\over d\tau}[\mu(a)\tau^2v^k].
 \end{aligned}                                  \tag{4}
\]

The sum of the first two lines is the third because
v'=-1+(1-2tau)/4. Thus their integrated mixed coefficients obey

\[
 A_k+B_k=0,
 \quad B_k={\mu(a)k\over4}
        \int_0^1\tau^2(1-2\tau)v^{k-1}\,d\tau.  \tag{5}
\]

Already at k=1,

\[
 \boxed{A_1=-1/24,\qquad B_1=+1/24.}             \tag{6}
\]

Both complete endpoint coefficients are zero, while transporting the Euler
derivative without its connection gives a nonzero coefficient. Hence there
is no finite relative bound of this omitted-connection output by the endpoint
output, even at a single legal native monomial. The witness uses the actual
frozen source gauge and retains the exact same physical Mellin label.

### All cores at once

After multiplying the local series, apply the linear coefficient projection
onto exponent0 or2 on the cofactor labels; this is not an algebra quotient.
Put
Phi_tau=product_(r notin{p,q})(1-v(tau)x_r^2). The complete pair sector has

\[
 \begin{aligned}
 \Pi_P A_\tau
 &=x_px_q\left[2\tau\Phi_\tau+
     \tau^2\sum_r x_r^2\!\prod_{s\ne r}(1-vx_s^2)\right],\\
 \Pi_P B_\tau
 &=x_px_q{2\tau-1\over4}\tau^2
       \sum_r x_r^2\!\prod_{s\ne r}(1-vx_s^2).
 \end{aligned}                                  \tag{7}
\]

Their sum is x_p x_q d(tau^2 Phi_tau)/dtau. Its integral is exactly x_p x_q:
all nonempty mixed cores cancel and the empty-core semiprime terminal remains.
Thus (4) is the coefficient formula of a complete finite-horizon pair-source
identity, not a statement about only one selected core.

## 3. GC-2: owner activation changes under this gauge

In the actual half-divisor derivative the two owner sites have integrated
coefficient

\[
 O_k^H=2\mu(a)\int_0^1\tau(1-\tau)^k(1+\tau/4)^k\,d\tau.
                                                               \tag{8}
\]

The Euler owner coefficient was O_k^E=2mu(a)/((k+1)(k+2)). The coefficients
are not equal merely because both complete homotopies have equal endpoints.
At the subcritical block's depth k=3,

\[
 \boxed{O_3^H=-229/1792,\qquad O_3^E=-1/10.}      \tag{9}
\]

The other half-divisor derivative sites supply the exact opposite of O_k^H.
Consequently the full source still cancels on this mixed sector. This proves
that the owner-activation projection need not commute with gauge transport.
Equal complete endpoint sources do not make their selected activation
coefficients equal.

This effect persists cofinally in core depth. Since
v(tau)=1-3tau/4-tau^2/4, substituting s=k tau and using dominated convergence
gives

\[
 {k^2O_k^H\over\mu(a)}\longrightarrow{32\over9},
 \qquad {k^2B_k\over\mu(a)}\longrightarrow{32\over27}.
                                                               \tag{10}
\]

For the first limit, the integrand after scaling is2s v(s/k)^k and converges
to2s exp(-3s/4). For the second it is
s^2(1-2s/k)v(s/k)^(k-1)/4 and converges to s^2 exp(-3s/4)/4. Extend each by
zero beyond s=k. The bounds v(tau)<=exp(-3tau/4) and k>=2 give an integrable
polynomial times exp(-3s/8). The gamma integrals give the constants in (10).
In particular B_k/O_k^H tends to1/3, while O_k^H/O_k^E tends to16/9.

These are coefficient ratios, not an assertion of a growing physical moment.
The activity N^-1/2 remains present. An actual cofinal family is obtained by
letting a contain successively more distinct primes and increasing the finite
horizon accordingly.

## 4. GC-3: physical observation and the centered correction

The two integrated coefficients in (5) multiply the identical primitive
phase and N^-1/2 U_N. Under the native Mellin observation their fields are
A_k N^-1/2 N^(-it) and B_k N^-1/2 N^(-it), with the same measure
|kappa_hat(t)|^2 dt/(2pi). Write Gamma(0) for its positive total mass. Their
uncentered observed Gram matrix is exactly

\[
 {\Gamma(0)B_k^2\over N}
 \begin{pmatrix}1&-1\\-1&1\end{pmatrix}.         \tag{11}
\]

At k=1 its coefficient is Gamma(0)/(576N), so the missing mixed term is
physically observable. The full summed field has norm zero. The two-sector
counting diagonal is2Gamma(0)B_k^2/N; centering by that specific diagonal
therefore gives its negative, not zero.

There is also an exact correction before parameter integration. Resolve the
derivative by its site and use counting measure on sites and Lebesgue d tau.
In the expanded (A,B) source, the density of the diagonal, with the common
factor1/N suppressed, is

\[
 d_{A,B}=2\tau^2v^{2k}
       +k\tau^4v^{2k-2}\left[1+{(1-2\tau)^2\over16}\right].
\]

In the original H' derivative-site resolution, A and B at one core site are
recombined first. Its density is

\[
 d_H=2\tau^2v^{2k}+k\tau^4(v')^2v^{2k-2},
 \quad
 \boxed{d_H-d_{A,B}=-{k\over2}\tau^4(1-2\tau)v^{2k-2}.}        \tag{12}
\]

This is the precise core-site cross term. Integrating (12), and multiplying
by Gamma(0)/N if observed, transfers the diagonal between these declared
resolutions. It cannot be replaced by a claim that polylogarithmic gauge
values preserve a literal Wick diagonal. The Boolean-history and T-106140
atomizations require their own explicit adapter; (12) does not identify them.

## 5. GC-4: the source norm repaired by retaining the connection

Let the source Hilbert space have the literal multiplicative shifts U_p as
contractions and x_p=p^-1/2 exp(-i theta_p)U_p, as in the frozen gauge. For
each fixed finite horizon H, uniformly in tau,

\[
 \|G_\tau\|+\|G_\tau^{-1}\|+
 \|G'_\tau\|+\|(G_\tau^{-1})'\|
 \ll(\log(2H))^C.                              \tag{13}
\]

The first two bounds are the frozen source theorem. For the derivative
bounds, g_tau, g_tau^-1 and their tau derivatives are analytic uniformly in
tau on every fixed disk |x|<=r<1. The displayed denominators stay away from
zero there; sqrt(1+x) has positive real part. The derivative series also
start at x^2, since their constant and linear coefficients are independent
of tau. Choose r>2^-1/2. Their weighted local coefficient sums are O(1/p).
The product rule gives the frozen product bound times sum_(p<=H)O(1/p),
which is again polylogarithmic. The second labelled67 changes only a constant.

For an arbitrary source vector u, retain both the field and its homotopy
derivative. The exact first-jet transport is

\[
 \begin{pmatrix}H_\tau u\\H'_\tau u\end{pmatrix}
 =\begin{pmatrix}G_\tau&0\\G'_\tau&G_\tau\end{pmatrix}
  \begin{pmatrix}E_\tau u\\E'_\tau u\end{pmatrix}.              \tag{14}
\]

The inverse matrix has entries G^-1 on the diagonal and
-G^-1 G' G^-1 in its lower-left corner. Therefore the two integrated
first-jet norms, integral(||field||^2+||derivative||^2)d tau, are comparable
with polylogarithmic factors. The endpoint observable is preserved exactly,
because G_0=G_1=I.

This identifies the missing term in a derivative-only gauge argument: its
natural estimate also needs the undifferentiated field. At the coefficient
level (6) already prevents bounding the connection-free integrated output by
the complete endpoint output. The first-jet statement repairs that source
norm defect; it is not an estimate for the conductor-amplified principal
moment. Its g^2 ell rho weights, regional masks and inherited diagonal need
not commute with this physical source gauge.

## 6. The remaining full-principal interface

A claimed binding of the completed Boolean coefficient model to the complete
retained principal/Wick source must now answer three concrete questions:
does it retain G'E or the equivalent connection contribution; which
activation and gauge labels remain inside gamma; and which precise diagonal
is transported by their recombination? The fixed T-106140 formulas retain
those labels but do not themselves specify this Euler-to-half-divisor adapter.

The present theorem supplies the primitive operator identity, a complete
all-core test, an observed counterexample to omitting its connection, the
exact resolution correction, and a sufficient source norm including the
missing field component. It does not prove the amplified principal bound or
claim that the repository's complete assembly actually omitted that term.
