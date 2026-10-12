# Volterra-square control of the complete second derivative payment

Status: proposed native operator refinement, pending independent full review.
Scope: the complete xi source and arbitrary distinct positive nodes. It gives
classical-strip global Pick order 1,462,000, and order 1,536,000 under the
additional complete `3/8` displacement hypothesis. These remain finite-order
results; RH remains open.
Dependencies: the frozen complete rational class and weighted endpoint
identity V2–V7 in [VOLTERRA_RATIONAL_REFINEMENT.md](../VOLTERRA_RATIONAL_REFINEMENT.md),
W12–W19 in [WEIGHTED_RATIONAL_DILATION.md](../WEIGHTED_RATIONAL_DILATION.md),
and the independently reviewed optimized primitive/strip proof
[OPTIMIZED_DOUBLE_COUNT.md](OPTIMIZED_DOUBLE_COUNT.md), SHA-256
`4a760969f52d03199ce38fcd29ad787382d9c61e4009f6f3cd79dd7e19d9c5c9`.
All classical/published source, Turing and critical-line verification inputs
of that packet remain unchanged. The optional narrower strip retains its
explicit additional imported hypothesis. No older frozen packet is modified.
What was run: exact compressed-kernel identities, uniform rational operator
constants, complete exponential tails and strict complete-source gap guards
in verify_volterra_square.py, normal and optimized Python.
Smallest remaining gap: independent review of this new operator composition.

## VS1. Square the endpoint matrix before taking its norm

Let `U` be the strictly upper triangular part of `e e*`. Diagonal unitary
conjugation makes every nonzero e_i positive; zero rows and columns may be
removed. Put `m_i=e_i^2` and `L=sum_i m_i`. Partition `[0,L]` into consecutive
intervals I_i of lengths m_i, and embed the vector space isometrically into
the normalized constant functions on these intervals. Let
`Vf(t)=integral_t^L f(s)ds`. Its square has the positive kernel
`(s-t)*1_(s>t)`.

The matrix C of the compression of `V^2` is exactly

\[
 C_{ij}=\begin{cases}
 e_ie_j[\sum_{i<k<j}m_k+(m_i+m_j)/2],&i<j,\\
 m_i^2/6,&i=j,\\
 0,&i>j.
 \end{cases}
\tag{VS1}
\]

For i<j, this is the distance between the two interval centers multiplied
by e_i e_j. For i=j, direct integration gives
`m_i^-1*integral_0^m_i integral_t^m_i(s-t)dsdt=m_i^2/6`.
On the other hand,

`(U^2)ij=e_i e_j*sum_(i<k<j)m_k` for i<j, and zero otherwise.

Thus `0<=U^2<=C` entrywise. For every complex vector v,
`|U^2 v|<=C|v|` entrywise, so norm domination follows without a matrix
positive-semidefinite comparison. Compression and the Hilbert–Schmidt
bound give

\[
 \boxed{\|U^2\|\le\|C\|\le\|V^2\|
 \le\left(\int_0^L\int_t^L(s-t)^2dsdt\right)^{1/2}
 =L^2/\sqrt{12}.}
\tag{VS2}
\]

The zero-trace case is immediate. This bound is substantially smaller than
squaring the separate `||U||<=2L/pi` estimate; that separate estimate remains
available for mixed terms below.

## VS2. The complete weighted dilation square

In the original weighted polynomial model of denominator dimension n,
D is upper triangular with diagonal `0,...,n-1` and

`D+D*=E-M`, `E=W(1)e e*`, `tr E<=n^2`,
`M=M*`, `||M||F<=(2n+1/28)*sqrt(n)`.

After diagonal unitary conjugation, let U be the strictly upper part of E.
The exact upper-triangular identity gives

`D=U+B`, `B=diag(0,...,n-1)-strict_upper(M)`.

The Hermitian Frobenius bound therefore yields

\[
 \|B\|\le n+(2n+1/28)\sqrt{n/2},\quad
 \|U\|\le(2/\pi)n^2,\quad
 \|U^2\|\le n^4/\sqrt{12}.
\tag{VS3}
\]

At every `n>=N0=850000`, use `sqrt(2n)>1300` and the inherited strict
`pi>314159/100000` to define the uniform exact rational constants

\[
 b_0=(2+1/(28N_0))/1300+1/N_0,\quad
 u_0=200000/314159,\quad h_0=288676/1000000>1/\sqrt{12}.
\]

Expand `D^2=U^2+UB+BU+B^2` before bounding. This gives

\[
 \|D^2\|\le(h_0+2u_0b_0+b_0^2)n^4
 <\boxed{e_0 n^4,\quad e_0=2907/10000.}
\tag{VS4}
\]

The normalized B bound decreases with n; exact endpoint inequalities pay
its whole range. No assumption that U and B commute is made.

## VS3. Use the square bound in every complete derivative estimate

Keep the original first dilation bound `||D||<=d*n^2`, `d=3191/5000`.
For every complex numerator P, VS4 gives
`||D^(j+2)P||<=||D||^j*||D^2P||<=d^j*n^(2j)*e0*n^4*||P||`.
D commutes with its own powers, so the original variable-path Minkowski
series for `exp(gamma_b D)D^2P` preserves this stronger estimate. It does
not require the path displacements gamma_b to be constant. The signed-pole
prefactor bounds are unchanged.

In the exact W14 second derivative formula replace only the former bound
`||D^2||<=d^2*n^4` by VS4. The remaining rational multipliers have the
same bounds `|B|<=3n`, `|DB|<=4n`. Both unshifted continuous and displaced
discrete norms therefore have the improved uniform coefficient

\[
 C_2'=291/1000,
\qquad
 e_0+(6/n+1/n^2)d+9/n^2+7/n^3<C_2'
 \quad(n\ge850000).
\tag{VS5}
\]

The first derivative coefficient remains `C1=6383/10000`. This applies
to every proper rational numerator in either signed-pole class and to all
displacement paths `tau*a_b`. It is not a finite compression substitute
for the complete source norms.

## VS4. Repay quadrature and Taylor loss with the sharper coefficient

Keep `cA'=3762011/28729000`, `m*=(113/355)(1-1838/28729)` and
`U*=106/333` from the reviewed optimized count proof. Put

`C'=C2'+C1^2` and `J'=4*cA'*C'`.

The two integrations by parts give complete quadrature cost `J'*q^2 B`.
The full arbitrary-displacement amplification is still
`kappa>exp[2A(d+2/n)q]`. The same product-rule and conjugate Taylor proof
now gives the exact complete-source reserve

\[
 m_*-J'q^2-A^2 C'\kappa^2q^2(U_*+J'q^2).
\tag{VS6}
\]

All its subtracted coefficients are positive, so it decreases with q>=0.
The following two exact choices have a strict positive endpoint reserve:

| Complete A bound | q0 | kappa | Exponent upper | Endpoint reserve |
| --- | --- | --- | --- | --- |
| 1/2 | 713/1000 | 1577/1000 | 4551/10000 | 4375993412166867933228645792648959018712823 / 6792397470000000000000000000000000000000000000 |
| 3/8 | 787/1000 | 729/500 | 3767/10000 | 2707828754395387643273072991404578154931367 / 3018843320000000000000000000000000000000000000 |

The exponent bounds are strict at n=N0 and q=q0; complete positive
exponential Taylor tails prove `exp(exponent upper)<kappa`.
The endpoint reserves are about 0.000644249 and 0.000896976; only their
exact rational values are acceptance guards.

At any node-independent good cutoff `T>=H0=3000000000000`, the complete
tail is strictly positive for every even `n>=850000` satisfying

`1000*n^2<=713*T` (classical A=1/2), or
`1000*n^2<=787*T` (additional complete A<=3/8).

Principal submatrices give all smaller orders. Cofinal good cutoffs supply
the corresponding selectable orders for changing tail kernels. Adding the
entire verified critical source below or at the common cutoff in
`[H0,H0+20]` gives global orders **1,462,000** and **1,536,000**. At H0
the largest allowed even orders are **1,462,532** and **1,536,554**.
The common cutoff is inside the imported published critical-line verification;
no new cutoff or zero census is computed. The second result also retains
its separately supplied uniform narrower strip. No result yields global
all-order positivity or RH.
