# L-105482 — The F1 Gram is the compact Mellin–Plancherel/Nyman norm of the physical source polynomial

Claim ID: `L-105482`

Status: **PROVED EXACT FINITE MELLIN–PLANCHEREL IDENTITY**

Let

\[
k(u)=K_L(e^u),
\qquad
\widehat k(t)=\int_{\mathbb R}k(u)e^{-itu}\,du.
\]

The kernel is supported in `[0,log 8)` and has zero logarithmic mean,

\[
\widehat k(0)=\int_1^8K_L(y)\frac{dy}{y}=0.
\tag{L-105482.1}
\]

For any finite coefficient packet `(a_n)`, put

\[
H(e^x)=\sum_na_nk(x-\log n),
\qquad
A(t)=\sum_na_nn^{-it}.
\tag{L-105482.2}
\]

Finite Fubini gives

\[
\widehat H(t)=\widehat k(t)A(t).
\]

Plancherel therefore yields

\[
\boxed{
\int_0^\infty|H(X)|^2\frac{dX}{X}
=\frac1{2\pi}
\int_{\mathbb R}|\widehat k(t)|^2|A(t)|^2dt.
}
\tag{L-105482.3}
\]

Equivalently, with

\[
R_K(h)=\int_{\mathbb R}k(u)\overline{k(u+h)}\,du,
\]

one has

\[
\boxed{
\int_0^\infty|H(X)|^2\frac{dX}{X}
=\sum_{n,r}a_n\overline{a_r}
R_K(\log(n/r)).
}
\tag{L-105482.4}
\]

Since `supp(k) subset [0,log8)`,

\[
\boxed{R_K(h)=0\quad(|h|\ge\log8).}
\tag{L-105482.5}
\]

For a frozen dyadic physical packet, the support of `H` meets only a fixed
number of neighboring dyadic `X`-blocks.  Thus the full norm (L-105482.3) and
the corresponding finite collection of block Gram energies are equivalent at
subpower scale.

## Canonical-source meaning

For the equal-pair Boolean source, `A(t)` is the literal physically recombined
Dirichlet polynomial.  By `L-106133--L-106134`, before the inherited closed
contractions it is the differential multiplier applied to the Beta average of
one normal-ordered owner--core half-source square.

Hence (L-105482.3) is the exact compact multiplicative Nyman coordinate of the
same F1 source.  It is not an independent random Dirichlet polynomial and it
is not controlled by coefficient energy alone.
