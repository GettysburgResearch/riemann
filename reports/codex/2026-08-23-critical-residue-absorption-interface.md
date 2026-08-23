# Critical-residue absorption interface

Status: **EXACT CONDITIONAL HANDOFF; XI INPUT OPEN**

Proof-object head: `2e8f971bd381d6c674290dc5fdb6f27feec3ac81`.

This report composes T-105113 through T-105116 into the smallest explicit
cofinal inequality that a future Xi programme must prove.  It introduces no
new Xi input and changes no frozen proof object.

## 1. Optimized second-carrier envelope

At stage (n), let (N_n) be the core target count and (A_n,B_n) the
first and second residue moments.  For the second raw carrier, define the
authenticated-anchor ratio

\[
\mathfrak a_{2,n}=
\frac{|F_n(a_n)|^2}{|F_n'(a_n)F_n''(a_n)|}.
\]

Write the T-105114 growth loads as (G_{j,n}), put

\[
D_{j,n}=\frac{2r_{1,j,n}}{r_{2,j,n}-r_{1,j,n}}G_{j,n},
\qquad
\alpha_{j,n}=\frac{G_{j,n}}{\beta_{j,n}},
\]

and optimize the two denominator-disk parameters through T-105116:

\[
\mathcal P_{2,n}^*=
\min_{\substack{0<\varepsilon_{j,n}\le1\\
\sum_{j=1}^2c_{j,n}\varepsilon_{j,n}\le S_{\star,n}}}
\sum_{j=1}^2\alpha_{j,n}\log\frac{2}{\varepsilon_{j,n}},
\qquad
c_{j,n}=\frac{r_{2,j,n}G_{j,n}}{\beta_{j,n}}.
\]

The complete raw exponent is

\[
\mathcal X_{2,n}^*=2G_{0,n}+D_{1,n}+D_{2,n}+\mathcal P_{2,n}^*.
\]

T-105114 then gives on every authenticated safe boundary (E_n)

\[
\left\|\frac{F_n^2}{F_n'F_n''}\right\|_{E_n}
\le\mathfrak a_{2,n}e^{\mathcal X_{2,n}^*}.
\tag{H.1}
\]

## 2. Actual selector load

For the fixed outer selector (W_{2,n}), retain its actual edge integral

\[
I_{2,n}(T,\eta)=
\int_{\partial\Omega_{T,\eta}}|W_{2,n}|\,|dz|,
\]

its full parameter mean (\overline I_{2,n}), its actual outer norm
(b_{2,n}^{\rm out}), and the outer perimeter bound
(L_n=4(T_{1,n}+\eta_{1,n})).  T-105115 supplies a safe boundary with

\[
I_{2,n}(E_n)\le
\mathscr S_{2,n}:=
\min\{\kappa_n\overline I_{2,n},L_nb_{2,n}^{\rm out}\}.
\tag{H.2}
\]

The first alternative requires a globally integrable full-shell cost; the
second does not.  No intermediate-edge constant-modulus equality is used.

Under the complete-manifest and fixed-carrier hypotheses of T-105113,
(H.1)--(H.2) give the exact finite absorption chain

\[
2\pi B_n
\le
\mathfrak a_{2,n}e^{\mathcal X_{2,n}^*}\mathscr S_{2,n}.
\tag{H.3}
\]

## 3. Cofinal closure criterion

A sufficient second-moment absorption input is

\[
\limsup_{n\to\infty}
\frac{\mathfrak a_{2,n}e^{\mathcal X_{2,n}^*}\mathscr S_{2,n}}
{2\pi N_n}
\le\nu.
\tag{H.4}
\]

Equivalently, the complete logarithmic debt is

\[
\log\mathfrak a_{2,n}+\mathcal X_{2,n}^*
+\log\mathscr S_{2,n}-\log(2\pi N_n)
\le\log\nu+o(1).
\tag{H.5}
\]

The independent signed first-moment input is

\[
A_n\ge\mu N_n(1+o(1)),\qquad\mu>0.
\tag{H.6}
\]

Together, (H.4) and (H.6) imply

\[
\liminf_{n\to\infty}\frac{A_n^2}{N_nB_n}
\ge\frac{\mu^2}{\nu}.
\tag{H.7}
\]

The strict coherence threshold is reached conditionally only when
(\mu^2/\nu>1/2).  Neither (H.4) nor (H.6) is presently authenticated for
Xi.

## 4. Conditional generic-growth barrier

Assume, explicitly and two-sidedly, for finitely many derivative factors,

\[
G_{j,n}\asymp X_n\log X_n,
\qquad
\beta_{j,n}\asymp1,
\qquad
r_{2,j,n}\asymp X_n.
\]

For fixed-width safe shells and fixed fractional slack, the T-105116
optimizer is interior and

\[
\varepsilon_{j,n}^*\asymp\frac1{X_n^2\log X_n},
\qquad
\mathcal P_{2,n}^*=\Theta(X_n(\log X_n)^2).
\tag{H.8}
\]

Thus retuning equal-disk radii cannot remove the (X_n(\log X_n)^2)
penalty within this declared ledger.  Absorption would need compensating
anchor-ratio or selector decay, exact projection overlap, authenticated
cancellation, a non-equal-disk improvement, or a stronger minimum-modulus
mechanism.  Equation (H.8) is conditional on the displayed two-sided
growth hypotheses; a one-sided (O(X_n\log X_n)) bound does not prove it.

## 5. Remaining Xi inputs

The reusable finite machinery is complete through the optimized envelope.
The following remain independent obligations:

1. cofinal off-center anchors and anchor ratios (\mathfrak a_{2,n});
2. quantitative fixed-order growth loads (G_{j,n});
3. complete actual-pole manifests and common-event decisions;
4. fixed outer selectors with actual (\overline I_{2,n}) or
   (b_{2,n}^{\rm out}) bounds;
5. full-shell integrability when the (\kappa_n\overline I_{2,n}) route is
   used;
6. absorption (H.4) and the positive signed lower bound (H.6);
7. target-count, multiplicity-defect, and simple-stratum comparisons;
8. strict Xi jet coherence, RCMV104530, and RH.

### Cross-program anchor candidate

The unmerged `origin/pr-720` head
`beb9d8a4e10fb8c8deb74bb0505a32fe55cddd14` contains
`L-104513-xi-derivative-strip-invariance.md`.  It proves, in the same
(t)-plane normalization, that

\[
\Xi_t^{(m)}(z)\ne0
\qquad(|\Im z|>1/2, m\ge0).
\]

After import, this would authenticate the single explicit common anchor
(a=-i) for all three consecutive derivatives used by T-105114.  The
current proof object does not import it.  Before freezing the bridge, repair
one omitted canonical-product term: if the real entire function has a zero
of multiplicity (q) at the origin, its logarithmic derivative also
contains (q/z).  For (\Im z>0), this term has negative imaginary part,
so the strip-invariance conclusion survives unchanged.

The same PR contains L-104531, an exact positive theta-orbit formula for
the Riemann Fourier kernel.  It is a promising source for a new
fixed-derivative complex-disk growth corollary, but no checked-in claim yet
supplies the required cofinal (G_{j,n}) bound.  In particular, the
conditional (O_k(R\log R)) sentence in T-105114 is not a source-locked Xi
input.

### Candidate combined anchor-growth import

There is a short exact corollary of PR #720's theta-orbit formula after one
source-normalization repair.  Under the standard
(\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)) convention, the
L-104531 kernel satisfies

\[
\int_{\mathbb R}\Phi(u)e^{itu}\,du=\Xi_t(t)/2,
\]

not the unscaled identity displayed in L-104528.  Thus the standard Xi
kernel is (2\Phi).  For fixed (m\ge0), set (Y=|\Im z|) and
(q=Y+11/2).  Then

\[
\boxed{
|\Xi_t^{(m)}(z)|
\le
4\pi^2m!\,\zeta(3/2)\,
\pi^{-q/2}\Gamma(q/2).
}
\tag{H.9}
\]

Indeed, for (u\ge0), L-104531 gives

\[
\Phi(u)\le
2\pi^2\sum_{n\ge1}n^4
e^{9u/2-\pi n^2e^{2u}}.
\]

Use twice the L-104531 kernel in the two-sided Fourier representation, the
bound (u^m\le m!e^u), and substitute (x=\pi n^2e^{2u}).  The
resulting incomplete gamma integral is at most

\[
\frac12\pi^{-q/2}n^{-q}\Gamma(q/2),
\]

while (\sum n^{4-q}\le\zeta(3/2)).  This proves (H.9).  Stirling then
gives, uniformly in (\Re z),

\[
\log^+|\Xi_t^{(m)}(z)|
=O_m((Y+1)\log(Y+2)).
\tag{H.10}
\]

The same positive kernel also supplies the anchor without the Hadamard
bookkeeping: pairing (u) and (-u) shows

\[
i^{-m}\Xi_t^{(m)}(-iy)>0
\qquad(y>0),
\tag{H.11}
\]

using a positive cosh moment for even (m) and a positive sinh moment for
odd (m).  Thus (a=-i) is simultaneous for every fixed derivative
triple, and (H.10) gives (O_k(R\log R)) growth on expanded disks centered
there.

Equations (H.9)--(H.11) are a reviewed derivation in this handoff, not yet a
hashed theorem on the current branch because their source claims remain on
unmerged PR #720.  The next programme should import the exact source blobs,
repair the L-104528/L-104531 factor-two mismatch, freeze this corollary, and
then update the T-105114 Xi-input flags.

The smallest defensible next theorem is therefore to import L-104531 with
the standard-kernel factor two and freeze (H.9)--(H.11), or import and
repair L-104513 for the anchor half.  Manifests/selectors and (H.4) remain
separate theorems.  No
numerical Xi scan or heavy computation is needed to review this interface.
