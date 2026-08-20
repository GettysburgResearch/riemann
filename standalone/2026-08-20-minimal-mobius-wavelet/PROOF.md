# Minimal ratio-eight ordinary-Möbius wavelet — complete proof packet

**Scientific status:** exact structural reduction; `MWOC99910` and RH remain unproved.

## 1. The minimal dyadic annihilator has ratio eight

Let `S_2 f(y)=f(y/2)`, with zero extension below one, and let

\[
P(S_2)=\sum_{j=0}^{d}c_jS_2^j
\]

be a causal dyadic scale filter. On either open local regime of the factor-67
box, the unnormalized kernel belongs to

\[
\operatorname{span}\{\sqrt y,1,\log y\}.
\]

Write `P(z)=sum c_j z^j`. Then

\[
P(S_2)\sqrt y=P(2^{-1/2})\sqrt y,
\]

\[
P(S_2)1=P(1),
\]

and

\[
P(S_2)\log y=P(1)\log y-(\log2)P'(1).
\]

Consequently a nonzero causal dyadic filter annihilates all three local modes
if and only if

\[
P(2^{-1/2})=0,\qquad P(1)=P'(1)=0.
\]

The roots have total multiplicity three, so `deg P>=3`. After the normalization
`P(0)=1`, the unique degree-three choice is

\[
\boxed{P(z)=(1-\sqrt2 z)(1-z)^2.}
\]

Thus

\[
\boxed{\mathscr D=(I-\sqrt2 S_2)(I-S_2)^2}
\]

is the minimal annihilator and its largest dyadic shift is eight.

## 2. Exact two-shell anti-symmetry

Put `R=67` and

\[
W(y)=
\begin{cases}
0,&0<y<1,\\
8\sqrt y-8-3\log y,&1\le y<R,\\
8(1-R^{-1/2})\sqrt y-3\log R,&y\ge R.
\end{cases}
\]

Let

\[
\Psi(y)=(\mathscr DW)(y)
=W(y)-(\sqrt2+2)W(y/2)+(2\sqrt2+1)W(y/4)-\sqrt2W(y/8).
\]

If `8<=y<R`, all active arguments lie in the collar formula and are
annihilated. If `y>=8R=536`, all arguments lie in the deep formula and are
annihilated. Hence

\[
\operatorname{supp}\Psi\subset[1,8]\cup[R,8R].
\]

For every `z in [R^{-1},R)`, direct substitution gives

\[
W(Rz)+W(z)=8\sqrt R\sqrt z-8-3\log(Rz).
\]

The right side belongs to the annihilated three-mode span. For `1<=y<=8`,
every `y/2^j` lies in `[R^{-1},R)`, so

\[
\boxed{\Psi(Ry)=-\Psi(y).}
\]

Define `K_0` to be the lower-shell restriction. Then

\[
\boxed{\Psi=(I-S_R)K_0,\qquad \operatorname{supp}K_0\subset[1,8].}
\]

The exact three bands are

\[
K_0(y)=
\begin{cases}
8\sqrt y-8-3\log y,&1\le y<2,\\
-8\sqrt2\sqrt y+8(1+\sqrt2)+3(1+\sqrt2)\log y
-3(2+\sqrt2)\log2,&2\le y<4,\\
4\sqrt y-8\sqrt2+9\sqrt2\log2-3\sqrt2\log y,&4\le y<8,\\
0,&\text{otherwise}.
\end{cases}
\]

## 3. Two exact positive resolvents

Let

\[
\beta(n)=\mu(n)-\mathbf1_{R\mid n}\mu(n/R)
\]

and

\[
B(X)=\sum_{n\le X}\frac{\beta(n)}{\sqrt n}W(X/n).
\]

Define

\[
G_\beta(X)=\sum_{n\le X}\frac{\beta(n)}{\sqrt n}K_0(X/n),
\qquad
G_\mu(X)=\sum_{n\le X}\frac{\mu(n)}{\sqrt n}K_0(X/n).
\]

Scale filters commute with finite source convolution, so

\[
\boxed{\mathscr DB=(I-S_R)G_\beta.}
\]

The inverse is finite and positive at every endpoint:

\[
\boxed{G_\beta(X)=\sum_{0\le j\le\log_R X}(\mathscr DB)(X/R^j).}
\]

The literal duplicate-67 source gives independently

\[
\boxed{G_\beta=(I-R^{-1/2}S_R)G_\mu,}
\]

with the positive inverse

\[
\boxed{G_\mu(X)=\sum_{0\le j\le\log_R X}R^{-j/2}G_\beta(X/R^j).}
\]

The second inverse has total coefficient mass `1/(1-R^{-1/2})`. No source
coefficient is changed or duplicated.

## 4. Mellin transform and RH equivalence

For `Re s>1/2`,

\[
\boxed{
\int_1^\infty G_\mu(X)X^{-s-1}dX
=
\frac{(s+\tfrac32)(1-\sqrt2 2^{-s})(1-2^{-s})^2}
{s^2(s-\tfrac12)\zeta(s+\tfrac12)}.
}
\]

The point `s=0` is removable because `(1-2^{-s})^2` has a double zero. The
point `s=1/2` is removable because `1-sqrt(2)2^{-s}` vanishes there and
`1/zeta(s+1/2)` also vanishes at the zeta pole. The added factors vanish only
on `Re s=0` or `Re s=1/2`.

A nontrivial zero `rho` with `1/2<Re rho<1` gives a noncancelled pole at
`s=rho-1/2`. The negative-mass Landau theorem therefore yields

\[
\int_1^X(G_\mu(t))_-\frac{dt}{t}=X^{o(1)}\Longrightarrow RH.
\]

Conversely RH gives `M(x)=O_epsilon(x^{1/2+epsilon})`; partial summation on the
three compact cells gives `G_mu(X)=O_epsilon(X^epsilon)`. Hence

\[
\boxed{RH\iff\int_1^X(G_\mu(t))_-\frac{dt}{t}=X^{o(1)}.}
\]

## 5. Exact three-band Hardy compression

Put

\[
A_\mu(t)=\sum_{n\le t}\frac{\mu(n)}n,\quad
C_\mu(t)=\sum_{n\le t}\frac{\mu(n)}{\sqrt n},\quad
L_\mu(t)=\sum_{n\le t}\frac{\mu(n)\log n}{\sqrt n}.
\]

On a band with `K_0(y)=a_r sqrt(y)+b_r+c_r log(y)`, one has exactly

\[
\begin{aligned}
\sum_{M<n\le N}\frac{\mu(n)}{\sqrt n}K_0(X/n)
={}&a_r\sqrt X[A_\mu(N)-A_\mu(M)]\\
&+(b_r+c_r\log X)[C_\mu(N)-C_\mu(M)]\\
&-c_r[L_\mu(N)-L_\mu(M)].
\end{aligned}
\]

Every suffix therefore uses at most three band contributions and nine state
evaluations. The packet is supported on `[X/8,X]` and has uniformly bounded
coefficient diagonal.

For the coefficient packet `d_X(n)=mu(n)n^{-1/2}K_0(X/n)`, the exact Hardy
square is

\[
Q_{\tau,X}=|\sum_nd_X(n)|^2+2\tau\int_{X/8}^{X}
|\sum_{n\ge v}d_X(n)|^2v^{2\tau-1}dv.
\]

At `tau=1`, support-shifted point evaluation and the diagonal have absolute
cost. The remaining theorem is the signed off-diagonal three-band packing.

## 6. Pointwise positivity is false

At `X=4`, only `n=1,2,3` contribute and exact substitution gives

\[
\begin{aligned}
G_\mu(4)={}&-4\sqrt2-\frac{16}{3}+\frac{8\sqrt3}{3}\\
&+\left(2\sqrt3+\frac{9\sqrt2}{2}\right)\log2-\sqrt3\log3.
\end{aligned}
\]

Exact rational radical bounds and the positive atanh series give

\[
\boxed{-1.4620<G_\mu(4)<-1.4618.}
\]

Thus pointwise positivity is not the missing theorem.

## 7. Exact frontier

Define `MWOC99910` by

\[
\int_2^Y\frac{\sqrt{Q_{1,X}}}{X/8}\frac{dX}{X}=Y^{o(1)}.
\]

Then `MWOC99910 -> RH`. The diagonal and all transfer interfaces are closed;
the signed ordinary-Möbius near-collision packing remains open and RH-equivalent.
