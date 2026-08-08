# L-30501 — The first aggregated cutoff boundary has linear atomic source norm

Claim ID: `L-30501`  
Title: The complete first-generation boundary produced by the stopped-power analytic split has an explicit fixed-annulus source and therefore cannot have polylogarithmic square-root atomic norm  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Dependencies: PR #286 `L-28401/L-28402`; PR #301 `L-29801`  
Scope: the first boundary generation only; no assertion about the optimal Cycle-Debt flow

## 1. Exact aggregate boundary

Let

\[
p(q)=q^{-1/2},
\qquad
w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X}.
\]

Use the shifted central analytic operator

\[
(\mathscr Cp)(q)
=
\sum_{k\ge1}
\left[(2kq-1)^{-1/2}-((2k+1)q)^{-1/2}\right].
\tag{L-30501.1}
\]

Let

\[
(\mathscr C_Xw_X)(q)
=
\sum_{k\ge1}
\left[w_X(2kq-1)-w_X((2k+1)q)\right].
\tag{L-30501.2}
\]

PR #301 writes

\[
w_X=
\sum_{Y=1}^{X-1}\ell_Yp_Y,
\qquad
\ell_Y=\log\frac{Y+1}{Y},
\qquad
p_Y(q)=q^{-1/2}\mathbf1_{q\le Y}.
\tag{L-30501.3}
\]

At output column `q`, a stopped layer with endpoint `Y` is active after one
central step exactly when

\[
q\le\left\lfloor\frac{Y+1}{2}\right\rfloor,
\qquad\text{equivalently}\qquad Y\ge2q-1.
\]

Consequently the complete first aggregated cutoff boundary is

\[
\boxed{
b_X(q)
=
\log\frac{X}{2q-1}\,\mathscr Cp(q)
-
\mathscr C_Xw_X(q).
}
\tag{L-30501.4}
\]

Indeed, the active analytic weights telescope as

\[
\sum_{Y=2q-1}^{X-1}\ell_Y
=
\log\frac{X}{2q-1},
\]

while finite linearity gives the second term in (L-30501.4). This is the
complete common-destination recombination of all first-generation stopped-power
boundaries.

## 2. Exact transition-annulus formula

Let

\[
I_X=
\left[
\left\lceil\frac{2X}{5}\right\rceil,
\left\lfloor\frac{9X}{20}\right\rfloor
\right]\cap\mathbb Z.
\tag{L-30501.5}
\]

For `q in I_X`, one has

\[
2q-1\le X,
\qquad
3q>X.
\]

Every finite term except the first shifted-even term vanishes. Hence

\[
\boxed{
\mathscr C_Xw_X(q)
=
(2q-1)^{-1/2}
\log\frac{X}{2q-1}.
}
\tag{L-30501.6}
\]

Substitution into (L-30501.4) gives

\[
\boxed{
b_X(q)
=
\log\frac{X}{2q-1}
\left[
\mathscr Cp(q)-(2q-1)^{-1/2}
\right].
}
\tag{L-30501.7}
\]

## 3. Uniform negative moat

`L-28401` gives at `s=1/2`

\[
\mathscr Cp(q)
=
q^{-1/2}
\left[
1-\eta(1/2)+R(q)
\right],
\tag{L-30501.8}
\]

where

\[
R(q)
=
\sum_{\ell\ge1}
\frac{(1/2)_\ell}{\ell!}
2^{-1/2-\ell}
\zeta(\ell+1/2)q^{-\ell}.
\]

### Eta coefficient

Euler transformation of the completely monotone sequence `n^{-1/2}` gives

\[
\eta(1/2)
>
\frac{29}{32}
-
\frac{11}{16\sqrt2}
+
\frac{5}{16\sqrt3}.
\tag{L-30501.9}
\]

The rational square bounds

\[
\frac1{\sqrt2}<\frac{7072}{10000},
\qquad
\frac1{\sqrt3}>\frac{5773}{10000}
\]

show that the right side is greater than `3/5`. Therefore

\[
1-\eta(1/2)<\frac25.
\tag{L-30501.10}
\]

### Faster-power tail

For `q>=100`, use `zeta(ell+1/2)<3` and the binomial series:

\[
R(q)
<
\frac3{\sqrt2}
\left[
\left(1-\frac1{2q}\right)^{-1/2}-1
\right].
\]

If `x=1/(2q)<=1/200`, then `sqrt(1-x)>199/200`, and hence

\[
(1-x)^{-1/2}-1
=
\frac{x}{\sqrt{1-x}(1+\sqrt{1-x})}
<
\frac{200}{79401}.
\]

Thus

\[
R(q)<\frac{600}{79401}<\frac1{132}.
\tag{L-30501.11}
\]

Combining (L-30501.8)--(L-30501.11),

\[
\mathscr Cp(q)
<
\frac{269}{660\sqrt q}.
\tag{L-30501.12}
\]

On the other hand,

\[
(2q-1)^{-1/2}
>
(2q)^{-1/2}
>
\frac7{10\sqrt q}.
\]

Therefore

\[
\mathscr Cp(q)-(2q-1)^{-1/2}
<
-\frac{193}{660\sqrt q}.
\tag{L-30501.13}
\]

For `q<=9X/20`,

\[
\frac{X}{2q-1}>\frac{10}{9},
\qquad
\log\frac{10}{9}>\frac1{10}.
\]

Equations (L-30501.7) and (L-30501.13) yield

\[
\boxed{
b_X(q)<-\frac1{35\sqrt X}
\qquad
(X\ge250,\ q\in I_X).
}
\tag{L-30501.14}
\]

## 4. The divisor source is unique on the next endpoint

Put

\[
M=\left\lfloor\frac{X+1}{2}\right\rfloor.
\]

Let `sigma_X`, supported on `2<=m<=M`, be the divisor source consumed by the
adjacent-tree map:

\[
b_X(q)
=
\sum_{\substack{m\le M\\q\mid m}}\sigma_X(m).
\tag{L-30501.15}
\]

This source is unique by triangular inversion over multiples.

Every `q in I_X` satisfies `q>M/2`. Thus the only multiple of `q` not exceeding
`M` is `q` itself, and

\[
\boxed{
\sigma_X(q)=b_X(q)
\qquad(q\in I_X).
}
\tag{L-30501.16}
\]

## 5. Linear atomic-norm lower bound

Use the source norm of `L-30403`:

\[
\|\sigma_X\|_{\rm at}
=
\sum_{m\le M}\sqrt m\,|\sigma_X(m)|.
\]

For `X>=250`,

\[
|I_X|\ge\frac X{25},
\qquad
\sqrt q>\frac35\sqrt X
\quad(q\in I_X).
\]

Equations (L-30501.14)--(L-30501.16) give

\[
\begin{aligned}
\|\sigma_X\|_{\rm at}
&\ge
\sum_{q\in I_X}\sqrt q\,|b_X(q)|\\
&>
\frac X{25}\cdot\frac35\cdot\frac1{35}
=
\frac{3X}{4375}.
\end{aligned}
\]

Therefore

\[
\boxed{
\|\sigma_X\|_{\rm at}>\frac{X}{1500}
\qquad(X\ge250).
}
\tag{L-30501.17}
\]

The bound is deliberately conservative.

## 6. Proof boundary

Closed here:

1. exact active-layer identification of the aggregate first boundary;
2. its one-term finite formula on a fixed transition annulus;
3. a uniform negative `X^{-1/2}` moat;
4. uniqueness of the next-endpoint divisor source;
5. a linear lower bound in the exact atomic norm used by PR #304.

Not claimed:

1. a lower bound for the **optimized** Cycle Debt;
2. impossibility of cancellations with the retained finite/analytic flow bank;
3. RH or its negation.
