# Which source identity detects the theta-quartet modification?

Status: proposed exact source audit and local quantitative transport lemma.
Scope: identifies preserved and broken identities. No low-order actual-xi
signed estimate is claimed to follow from the surviving identities.

## 1. Normalized Jacobi reflection survives

Put `psi(v)=sum_(n>=1) exp(-pi n^2 v)` and

\[
A(u)=e^{u/2}\psi(e^{2u}),\qquad
A(-u)=A(u)+\sinh(u/2),\qquad
\Phi_\theta=(D^2-1/4)A.
\]

These are the exact inherited theta identities in the real-zero Xi convention.
For the quartet parameters in `POSITIVE_THETA_QUARTET.md`, let

\[
L(D)=D^4+2(R^2-d^2)D^2+(R^2+d^2)^2,
\quad C=L(1/2)=Q_{R,d}(i/2)>0.
\]

Since L is even, it commutes with reflection. Since
`L(D)sinh(u/2)=C sinh(u/2)`, the modified primitive

\[
\widetilde A=L(D)A/C
\]

has the **same exact** additive Jacobi identity

\[
\widetilde A(-u)=\widetilde A(u)+\sinh(u/2).          \tag{M1}
\]

Also `tilde A'(0)=-1/4`, and
`tilde Phi=(D^2-1/4)tilde A=L(D)Phi_theta/C` is strictly positive by the
complete certificate already proved. Its transform is

\[
\widetilde G(z)=Q_{R,d}(z)\Xi(z)/Q_{R,d}(i/2).       \tag{M2}
\]

Thus `tilde G(+/-i/2)=Xi(+/-i/2)=1/2`: the genuine removable endpoint
normalization of xi survives as well. This differs from the optional
center-value normalization `Q(0)` used in (P1); the zeros and source
positivity are unchanged. One should not call the bare modular reflection
the broken identity. It is insufficient to distinguish this modification.

## 2. The literal lattice Gaussian source and Euler normalization break

Write `v=exp(2u)`. The modified primitive is

\[
\widetilde\psi(v)
 =\frac1C L(2v\partial_v+1/2)\psi(v).               \tag{M3}
\]

In place of each lattice atom with coefficient one, this operator supplies a
degree-four polynomial in `pi n^2 v` multiplying that atom. In particular,

\[
\widetilde\psi(v)/\psi(v)
 \sim16(\pi v)^4/C\quad(v\to\infty).               \tag{M4}
\]

It is not the literal constant-coefficient lattice Gaussian sum. It also
cannot be any normally convergent constant-coefficient expansion
`sum a_n exp(-pi n^2 v)` with finite first coefficient: such an expansion
has `exp(pi v) times its value ->a_1`.

The Mellin transform makes the arithmetic failure especially explicit.
For `Re s>1`, repeated integration by parts gives

\[
\int_0^\infty\widetilde\psi(v)v^{s/2}\,\frac{dv}{v}
 =\frac{L(s-1/2)}C
   \pi^{-s/2}\Gamma(s/2)\zeta(s).                  \tag{M5}
\]

The boundaries vanish in this half-plane; the small-v modular asymptotic is
unchanged, and the large-v tail is exponential times a polynomial. The
putative zeta factor is therefore

\[
\widetilde\zeta(s)=\frac{L(s-1/2)}C\zeta(s).         \tag{M6}
\]

It has the same completed reflection and preserved xi endpoints, but
`tilde zeta(sigma)~sigma^4/C` as real sigma tends to infinity. Every ordinary
Dirichlet series absolutely convergent somewhere in a right half-plane has
a finite limiting first coefficient as sigma tends to infinity. Thus (M6)
fails the native Dirichlet/Euler source normalization. Its extra zeros are
exactly `s=1/2+/-d+/-iR`.

The native identities to retain in any transport argument are the actual
constant-coefficient lattice source or its exact Mellin–Euler binding.
Reflection, endpoint repair, positive source mass, growth and zero counts
alone leave the signed obstruction intact.

## 3. Compact-domain invisibility has an exact bound

The multiplier difference in (M6) factors as

\[
\frac{L(s-1/2)}C-1
 =\frac{s(s-1)[(s-1/2)^2+1/4+2(R^2-d^2)]}{C}.       \tag{M7}
\]

For `|s-1/2|<=B` and `R>=10`, `0<d<1/2`, this implies

\[
\left|\frac{L(s-1/2)}C-1\right|
 \le\varepsilon_B(R):=
 \frac{(B^2+1/4)(B^2+1/4+2R^2)}{R^4}.               \tag{M8}
\]

For every fixed compact domain this tends to zero as R grows, while the
modified function always retains the nonreal quartet at height R. The same
estimate holds for `Q(z)/Q(i/2)-1` on `|z|<=B` in the Xi coordinate.
This precisely states why matching a finite collection of analytic controls
cannot replace an unbounded source-binding estimate.

## 4. A forward local companion-transport estimate

There is a useful rigorous local direction, though it requires protecting
the actual companion denominators. Let F,q be holomorphic near a point, and
fix `lambda>0`. Write `E=F-i lambda F'`, and assume `q,E,E'` are nonzero.
For the source-modified function qF, exact differentiation gives

\[
E[qF]=qE-i\lambda q'F,
\quad E'[qF]=qE'+q'(F-2i\lambda F')-i\lambda q''F.    \tag{M9}
\]

Define

\[
a=\lambda|q'/q|\,|F/E|,
\qquad
b=|q'/q|\,|(F-2i\lambda F')/E'|
  +\lambda|q''/q|\,|F/E'|.
\]

If `b<1`, then the modified derivative companion is nonzero and

\[
\left|
 \frac{iE[qF]/E'[qF]}{iE/E'}-1\right|
 \le\frac{a+b}{1-b}.                              \tag{M10}
\]

If additionally `a<1`, the modified companion itself is nonzero. This is the
same exact ratio estimate used in the positive-source certificate, applied
to a multiplicative source correction rather than to reflected terms.

For the polynomial correction `q=Q/Q(i/2)`, on `|z|<=B` with
`epsilon_B(R)<1`, (M8) and the literal derivatives of Q give

\[
|q'/q|\le
 \frac{4B(B^2+R^2)}{R^4(1-\varepsilon_B(R))},\quad
|q''/q|\le
 \frac{12B^2+4R^2}{R^4(1-\varepsilon_B(R))}.          \tag{M11}
\]

These are quantified forward source-to-companion bounds on any domain where
the displayed original ratios are bounded. They cannot be promoted to a
descent theorem by omitting those ratios: poles or near-zeros of E or E'
can amplify a tiny source correction. The exact lower-ray obstruction in
`DERIVATIVE_COUNTEREXAMPLE.md` exhibits that signed failure.

Our attempted deduction of low-order signed descent from Jacobi symmetry
alone therefore fails for a precise reason: (M1) is preserved by a strictly
positive-source counterexample. A viable source-specific continuation must
use the native lattice/Mellin identity and quantify its interaction with the
companion denominators or the full residue/winding ledger. This packet proves
the local transport inequality and identifies the remaining estimate; it
does not silently assume that estimate.
