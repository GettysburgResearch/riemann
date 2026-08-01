# R-19803 — Euler orthogonality plus a contractive lifted multiplier does not imply Green compression contractivity

Claim ID: `R-19803`  
Title: The Appendix-C contraction shortcut fails without a coisometric or accretive intertwining identity  
Status: `PROVED EXACT FINITE COUNTEREXAMPLE`  
Authoring agent: `gpt56-pro-09-k`  
Created: 2026-08-01  
Dependencies: elementary rational linear algebra; `L-19815`  
Scope: the inference used to claim `||CKE||<=1`

## 1. Claimed implication being tested

The proposed continuum shortcut uses the following ingredients:

1. a Hermitian difference-of-squares form
   \[
   Q(f)=\|G_+f\|^2-\|G_-f\|^2;
   \]
2. a trace map `R` and Green minimizers `f_x` satisfying
   \[
   Q(f_x,h)=0\quad(h\in\ker R);
   \]
3. positivity of `Q` on `ker R`;
4. a lifted right inverse and compression
   \[
   G_-f_x=CKE(G_+f_x),
   \qquad CE=I;
   \]
5. a contractive lifted multiplier `||K||<=1`.

These facts do not imply `||CKE||<=1`.

## 2. Exact rational model

Let

\[
 V=\mathbb R^2,
 \qquad R(x,n)=x,
 \qquad N=\ker R=\operatorname{span}\{e_2\}.
 \tag{R-19803.1}
\]

Define scalar plus and minus features by

\[
 \boxed{
 G_+(x,n)=x+\frac32n,
 \qquad
 G_-(x,n)=\frac32x+n.}
 \tag{R-19803.2}
\]

Then

\[
 \begin{aligned}
 Q(x,n)
 &=G_+(x,n)^2-G_-(x,n)^2\\
 &=\frac54(n^2-x^2).
 \end{aligned}
 \tag{R-19803.3}
\]

In the decomposition `V=span(e1) direct-sum N`, the form matrix is exactly

\[
 \boxed{
 [Q]=\begin{pmatrix}-5/4&0\\0&5/4\end{pmatrix}.}
 \tag{R-19803.4}
\]

Hence `Q|N` is strictly positive.

For the fibre `Rf=x`, the Green minimizer is

\[
 \boxed{f_x=(x,0).}
 \tag{R-19803.5}
\]

Indeed, for every `h=(0,n) in N`,

\[
 Q(f_x,h)=0,
 \tag{R-19803.6}
\]

and

\[
 Q(f_x+h)-Q(f_x)=\frac54n^2\ge0.
 \tag{R-19803.7}
\]

Thus both the Euler equation and the exact fibre-minimality identity hold.
Nevertheless

\[
 G_+f_x=x,
 \qquad
 G_-f_x=\frac32x,
 \tag{R-19803.8}
\]

so the Green range map has norm `3/2`.

## 3. Strictly contractive diagonal lifted multiplier

Let the lifted Hilbert space be `H=R^2`. Define

\[
 C(a,b)=a+b,
 \tag{R-19803.9}
\]

\[
 \boxed{
 Ey=\left(\frac43y,-\frac13y\right),}
 \tag{R-19803.10}
\]

and

\[
 \boxed{
 K=\begin{pmatrix}9/10&0\\0&-9/10\end{pmatrix}.}
 \tag{R-19803.11}
\]

Then

\[
 CE=I,
 \tag{R-19803.12}
\]

and

\[
 \|K\|=\frac9{10}<1.
 \tag{R-19803.13}
\]

But

\[
 \begin{aligned}
 CKEy
 &=C\left(\frac65y,\frac3{10}y\right)\\
 &=\frac32y.
 \end{aligned}
 \tag{R-19803.14}
\]

Therefore

\[
 \boxed{
 \|CKE\|=\frac32>1}
 \tag{R-19803.15}
\]

although the lifted multiplier is a strict diagonal contraction and every
Green/Euler premise above holds exactly.

The diagonal signs in (R-19803.11) are not an artificial feature relative to the
Volterra multiplier: `kappa=(1-r)/(1+r)` also changes sign when `r>1`.

## 4. Exact location of the failure

The lifted inequality is

\[
 K^*K\preceq I.
 \tag{R-19803.16}
\]

The observed inequality required after compression is

\[
 E^*K^*C^*CKE\preceq E^*C^*CE.
 \tag{R-19803.17}
\]

These are different unless `C`, `E`, and `K` satisfy an additional
intertwining/coisometry relation. In the counterexample,

\[
 C^*C=\begin{pmatrix}1&1\\1&1\end{pmatrix}
 \tag{R-19803.18}
\]

and it does not commute with the diagonal `K`. Cancellation in `CE` becomes
reinforcement in `CKE`.

The same noncommutation is the theta-Hankel double commutator appearing in
`L-19814/L-19815`.

## 5. Correct replacement theorem

By `L-19815`, the observed transfer is the Cayley transform of the Green moment
operator `A` and

\[
 I-(CKE)^*(CKE)
 =2(I+A)^{-*}(A+A^*)(I+A)^{-1}.
 \tag{R-19803.19}
\]

Therefore the missing hypothesis is not another boundary orthogonality
statement. It is the theta-specific accretivity inequality

\[
 \boxed{
 \operatorname{Re}\langle\mathcal Mx,\mathcal Nx\rangle
 =D_{\rm trace}(x,x)\ge0.}
 \tag{R-19803.20}
\]

Equivalently, one must prove the compressed commutator/Hardy estimate in
`L-19815.18` or construct a genuine coisometric Green lift giving the
sum-of-squares identity `L-19815.21`.

## 6. Consequence for the current proof stack

The exact quotient-to-original lift remains a valid conditional transport. This
refutation concerns only the proposed proof of the internal contraction. The
line

```text
Euler orthogonality + |kappa|<=1 => ||CKE||<=1
```

must not be used without an additional theta-specific compression theorem.
Finite generalized eigenvalues below one are evidence for that theorem, not a
proof of it.

## 7. Proof boundary

All assertions are exact rational finite-dimensional identities. No zeta zero,
asymptotic estimate, floating-point computation, or normalization convention is
involved.