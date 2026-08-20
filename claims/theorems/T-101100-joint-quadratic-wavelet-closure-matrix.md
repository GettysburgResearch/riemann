# T-101100 — Joint quadratic–wavelet closure matrix

## Fixed detector

Use the notation of L-101101 and define

\[
 \mathcal C=\frac{C_2}{3}JP_2\delta_0,
 \qquad
 \mathcal A=-\frac13JP_2\mathcal A_\beta,
 \qquad
 \mathcal Q=-\frac13JP_2(D-1)E_2.
\]

Then

\[
 \boxed{G_\beta=\mathcal C+\mathcal A+\mathcal Q,}
\]

and `C` has compact support in `1<=X<=8`.

Put

\[
 A(Y)=\int_1^Y(\mathcal A(X))_-\frac{dX}{X},
 \qquad
 Q(Y)=\int_1^Y(\mathcal Q(X))_-\frac{dX}{X}.
\]

## Joint closure statement

Assume there is a fixed nonnegative matrix

\[
 M=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]

with

\[
 a<1,\qquad d<1,\qquad bc<(1-a)(1-d),
\]

such that for every `epsilon>0`, all sufficiently large `Y` satisfy

\[
 \begin{pmatrix}Q(Y)\\A(Y)\end{pmatrix}
 \le
 M\begin{pmatrix}Q(Y)\\A(Y)\end{pmatrix}
 +O_\epsilon(Y^\epsilon)\begin{pmatrix}1\\1\end{pmatrix}.
\]

Then

\[
 Q(Y)+A(Y)=Y^{o(1)},
\]

\[
 \int_1^Y(G_\beta(X))_-\frac{dX}{X}=Y^{o(1)},
\]

and the Riemann Hypothesis follows.

## Proof

The two-channel criterion in L-101100 says `rho(M)<1`.  Hence

\[
 \begin{pmatrix}Q(Y)\\A(Y)\end{pmatrix}
 \le(I-M)^{-1}O_\epsilon(Y^\epsilon)
 \begin{pmatrix}1\\1\end{pmatrix}.
\]

The inverse is a fixed nonnegative matrix, so both entries are
`O_epsilon(Y^epsilon)` for every epsilon.

The elementary inequality `(u+v+w)_-<=u_-+v_-+w_-`, together with compact
support of `C`, yields

\[
 \int_1^Y(G_\beta)_-\frac{dX}{X}
 \le Q(Y)+A(Y)+O(1)=Y^{o(1)}.
\]

The Mellin transform in L-101101 has every off-critical zeta zero as a genuine
pole and no positive-real obstruction.  The frozen negative-mass
Mellin–Landau theorem therefore excludes zeros with real part greater than
one half; the functional equation excludes those with real part less than
one half.

## Exact scientific status

The bridge, matrix theorem, and implication to RH are proved.  The displayed
two arithmetic matrix rows are **not** proved in this packet.  Existing
adaptive-squaring and zero-moment/largest-prime results provide the correct
candidate mechanisms, but their source-faithful cross-core constants have not
yet been shown to form a subcritical Perron matrix.

```text
joint matrix theorem                     PROVED
quadratic--wavelet bridge                PROVED
subcritical arithmetic matrix            OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVED
```
