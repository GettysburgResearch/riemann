# Two quantitative checks for further consumers

Status: exact exponent checks within the stated estimates. These are
limitations of those estimates, not impossibility theorems for the
underlying moments. No boundary improvement is asserted.

Sources: the quasi-Riemann source at
`openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`, labels
`old-eq:3.5`, `old-eq:2.13`, `old-eq:2.14`, `old-eq:3.16`,
`eq:first-poisson-bridge`, and `eq:detector-note`; the frozen and
fourth-pass structured cubic moments cited in the companion notes.

## 1. The exact capacity-limiting M2 edge

Let $\kappa_0=2\beta-1$ be the available pointwise prime exponent:
$|Q|^2\ll Z^{\kappa_0 z+\epsilon}$ for total slot length $z$.
Suppose one tries to prove M2 with a smaller positive capacity parameter
$0<\kappa'<\kappa_0$, so its admissibility boundary is

\[
A+(6\kappa'-1)z=M.                                         \tag{1}
\]

Take the source's amplified main two-transform edge with both common
supports trivial, $K=K_0$, and every common-support or extracted-length
parameter zero. Choose a positive live slot length $z$ on this boundary,
and choose the amplifier-prime norm exponent $\ell>0$ sufficiently
small that $z>\ell/\kappa'$. Such edges exist with nonnegative plain
lengths by taking $0<z<M/(6\kappa')$ first. The source definitions
give exactly

\[
g=6\ell,\qquad M'=M-6\ell,\qquad A'=A,\qquad z'=z,
\qquad\Delta_{\mathrm{child}}=\ell.                         \tag{2}
\]

Thus the child's defect in (1) is $F=6\ell$. While a live slot remains,
removing slots restores the proposed affine capacity only after deleting
total prime length at least
$\ell/\kappa'$. The present pointwise estimate charges that procedure
the exponent $\kappa_0 d$ for deleted length $d$, hence at least
$\kappa_0\ell/\kappa'$, while the permitted child allowance is only $\ell$.
Deleting all slots instead reaches the unrestricted zero-slot theorem,
but costs $\kappa_0z>\kappa_0\ell/\kappa'>\ell$ on the selected edge.
Thus the zero-slot alternative does not avoid this deficit. The affine
bookkeeping closes by the indicated removal operation exactly when

\[
\kappa'\ge\kappa_0.                                       \tag{3}
\]

This edge is nonexceptional and has no common prime support. The
signed exceptional rectangle cancellation does not change (2).
At the first transform its live coefficient is the allocated
convolution of two plain polynomials and the prime slots, multiplied
by the full sextic Gauss sum $G(\Pi l_1l_2,h)$. There is no live
$\mu(\Pi l_1l_2)$ coefficient. The Möbius signs on auxiliary
coprimality divisors do not turn it into the newly controlled
$\mu\gamma_2$ column.

A capacity improvement therefore needs a new estimate on this edge,
or an alternate complete representation such as the signed
root-number fourth moment. Making the amplifier step smaller does
not erase the deficit: the finite descent then requires proportionally
more steps.

## 2. A pure cubic reciprocal model and its truncation cost

This subsection is deliberately a pure cubic model; the actual high
quotient has sextic characters and additionally needs its square-core
analysis. Let the outer column length be $B$, with the actual
$\mu G$ coefficient, and suppose a reciprocal Dirichlet block of
length $N$ is paired with it at real part $\sigma>2/3$.
For $N\le B$, Cauchy and the rectangular extension give

\[
\left|\sum_{Nn\asymp N}\frac{a_n}{(Nn)^\sigma}
       \sum_{Nb\asymp B}\mu(b)\theta(b)G(b)\overline{\chi_b(n)}\right|
 \ll B^{1-\eta+\epsilon}N^{2/3-\sigma},                    \tag{4}
\]

for bounded/divisor-bounded $a_n$, with common smooth profiles.
The short $N$ dyads are summable. For $N\ge B$, the original
$A\ge B$ moment instead gives the two terms

\[
B^{1/2+\epsilon}N^{1-\sigma}
 +B^{5/6-\eta/2+\epsilon}N^{5/6-\sigma-\eta/2}.             \tag{5}
\]

At $\sigma=\beta+e$ with $\beta>5/6$, the second term decays in
$N$, but the first grows for $\sigma<1$. Therefore (4) does not
justify absolute summation of the entire reciprocal series.

To make the obstruction numerical, request a retained outer saving
$B^{-\gamma}$, where $0<\gamma\le\eta$, and truncate the reciprocal
at $D=B^r$. A conductor-uniform Mellin truncation on
$\sigma=\beta+e$ has error
$B^\epsilon D^{-e+\delta}$ for every fixed $0<\delta<e$.
Bounding the outer root-number coefficients absolutely therefore
requires, up to strict margins,

\[
r\ge\gamma/e.                                             \tag{6}
\]

If this forces $D>B$, the volume term in (5) stays below
$B^{1-\gamma}$ only when

\[
r\le\frac{1/2-\gamma}{1-\beta-e}.                           \tag{7}
\]

Combining (6)--(7), in the limit of arbitrarily small subsidiary
losses, requires

\[
e\ge2\gamma(1-\beta).                                     \tag{8}
\]

For $\beta=0.874886647039964\ldots$, the coefficient of $\gamma$
is $0.250226705920072\ldots$. Thus this positive-norm/truncation
argument cannot keep a fixed saving as the available buffer
$e\downarrow0$. It supplies neither a continuation below $\beta$
nor an all-row sextic quotient bound by itself.

## 3. The actual global-contour size requirement

The active scalar geometry supplied for this investigation is

\[
\ell=.16712007850681014\ldots,\quad
l_y=.45970744037451584\ldots,\quad
h=d=.79394759738813613\ldots,
\quad\theta=.05216519695620036\ldots.
\]

These displayed decimals are ordinary evaluation data, not interval
certificates. Put the reciprocal on a genuinely global line
$s=\beta+e$ so no detected-class mask is introduced. Let $U^r$
bound the whole signed reflected numerator/reciprocal row sum,
**including** its normalized prime product but excluding the
functional-equation factor $U^\theta$.
At $d=h$, the source high-exponent comparison requires, as $e\to0$,

\[
r<\frac{l_y(1/2+\theta)+h/6+\ell/2}{h}-\theta
 =.53945960261490879\ldots.                                 \tag{9}
\]

At $\theta=0$ the analogous threshold is
$.56142037644764711\ldots$. In contrast the short pure cubic
reciprocal calculation (4) supplies exponent $1-\eta$, and the
actual sextic quotient has further coupling. Consequently an
arbitrarily small saving in an unbinned full root-number sum is not
automatically enough at this geometry. The existing detected-class
numerator bound has exponent $2/3$ on its smaller class and uses the
lower reciprocal line $s=a<\beta$; that lower-line benefit cannot
be retained while simply removing the class indicator.

There is an additional orientation requirement for the single-numerator
route. The frozen matrix is $\mu\gamma_2\overline{\chi_3}$ and
its whole conjugate is $\mu\overline{\gamma_2}\chi_3$.
Reflecting one positive-orientation numerator introduces
$\gamma_1\overline{\chi_6}$, hence
$\mu\overline{\gamma_2}\overline{\chi_3}$ on square indices,
up to the fixed angular/ray factors. This opposite pairing is not
the whole conjugate of the frozen matrix. The central fourth-power
representation has $\gamma_1^{-2}\chi_6$, and on square indices
gives exactly the matching $\mu\overline{\gamma_2}\chi_3$.

Equation (9) is a target for a different complete signed argument,
not an upper bound proved here. The small-core fourth-moment theorem
in the companion note avoids claiming such a global quotient estimate.
