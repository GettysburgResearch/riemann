# L-30501 — The first aggregated cutoff boundary has linear atomic source norm

Claim ID: `L-30501`  
Title: The complete first-generation boundary produced by the stopped-power analytic split has an explicit positive top-annulus source and therefore cannot have polylogarithmic square-root atomic norm  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Dependencies: PR #286 `L-28401/L-28402`; PR #301 `L-29801`  
Scope: the first boundary generation only; no assertion about the optimal Cycle-Debt flow

## 1. Analytic and finite central residuals

Let

\[
p(q)=q^{-1/2},
\qquad
w_X(q)=q^{-1/2}\log(X/q)\mathbf 1_{q\le X}.
\]

Use the shifted central analytic operator

\[
(\mathscr Cp)(q)
=
\sum_{k\ge1}
\left[(2kq-1)^{-1/2}-((2k+1)q)^{-1/2}\right].
\tag{L-30501.1}
\]

The series is positive termwise. `L-28401` gives

\[
\mathscr Cp(q)
=
[1-\eta(1/2)]q^{-1/2}
+
\sum_{\ell\ge1}c_\ell q^{-1/2-\ell},
\qquad c_\ell>0.
\tag{L-30501.2}
\]

Let

\[
(\mathscr C_Xw_X)(q)
=
\sum_{k\ge1}
\left[w_X(2kq-1)-w_X((2k+1)q)\right].
\tag{L-30501.3}
\]

The complete first aggregated cutoff boundary in the stopped-power
decomposition is

\[
\boxed{
b_X(q)
=
\log(X/q)\,\mathscr Cp(q)-\mathscr C_Xw_X(q).
}
\tag{L-30501.4}
\]

Indeed, `L-29801` writes

\[
w_X=\sum_{Y=1}^{X-1}\ell_Yp_Y,
\qquad
\ell_Y=\log\frac{Y+1}{Y},
\]

and finite linearity gives exactly

\[
b_X
=
\sum_Y\ell_Y(\mathscr Cp-\mathscr C_Yp_Y)
\]

on the next endpoint. Thus (L-30501.4) is the complete common-destination
recombination of all first-generation stopped-power boundaries, not a
termwise upper bound.

## 2. Exact top-annulus formula

Let

\[
I_X=
\left[
\left\lceil\frac{49X}{100}\right\rceil,
\left\lfloor\frac X2\right\rfloor
\right]\cap\mathbb Z.
\]

For \(q\in I_X\), one has

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
\tag{L-30501.5}
\]

## 3. Uniform positive moat

The alternating-series pairs give

\[
1-\eta(1/2)
=
\sum_{k\ge1}
\left[(2k)^{-1/2}-(2k+1)^{-1/2}\right]
\ge
2^{-1/2}-3^{-1/2}.
\tag{L-30501.6}
\]

For \(q\le X/2\),

\[
q^{-1/2}\ge\sqrt{2/X},
\qquad
\log(X/q)\ge\log2.
\]

Therefore the analytic term in (L-30501.4) is larger than

\[
\frac{(1-\sqrt{2/3})\log2}{\sqrt X}
>
\frac1{9\sqrt X}.
\tag{L-30501.7}
\]

The last inequality follows from

\[
\sqrt{2/3}<5/6,
\qquad
\log2>2/3.
\]

For \(X\ge100\) and \(q\ge49X/100\),

\[
2q-1\ge97X/100.
\]

Consequently

\[
(2q-1)^{-1/2}
<
\frac{51}{50\sqrt X},
\]

and

\[
\log\frac{X}{2q-1}
\le
\log\frac{100}{97}
<
\frac3{97}
<
\frac1{32}.
\]

Combining this with (L-30501.5),

\[
\mathscr C_Xw_X(q)
<
\frac{51}{1600\sqrt X}.
\tag{L-30501.8}
\]

Since

\[
\frac19-\frac{51}{1600}
=
\frac{1141}{14400}
>
\frac1{13},
\]

one obtains the explicit source moat

\[
\boxed{
b_X(q)>\frac1{13\sqrt X}
\qquad
(X\ge100,\ q\in I_X).
}
\tag{L-30501.9}
\]

## 4. The divisor source is unique on the next endpoint

Put

\[
M=\left\lfloor\frac{X+1}{2}\right\rfloor.
\]

Let \(\sigma_X\), supported on \(2\le m\le M\), be the divisor source consumed
by the adjacent-tree map:

\[
b_X(q)
=
\sum_{\substack{m\le M\\q\mid m}}\sigma_X(m).
\tag{L-30501.10}
\]

This source is unique by triangular inversion over multiples.

Every \(q\in I_X\) satisfies \(q>M/2\). Thus the only multiple of \(q\) not
exceeding \(M\) is \(q\) itself, and

\[
\boxed{
\sigma_X(q)=b_X(q)
\qquad(q\in I_X).
}
\tag{L-30501.11}
\]

## 5. Linear atomic-norm lower bound

Use the source norm of `L-30403`:

\[
\|\sigma_X\|_{\rm at}
=
\sum_{m\le M}\sqrt m\,|\sigma_X(m)|.
\]

For \(X\ge200\),

\[
|I_X|\ge X/200,
\qquad
\sqrt q\ge\frac7{10}\sqrt X
\quad(q\in I_X).
\]

Equations (L-30501.9)--(L-30501.11) give

\[
\begin{aligned}
\|\sigma_X\|_{\rm at}
&\ge
\sum_{q\in I_X}\sqrt q\,b_X(q)\\
&>
\frac X{200}\cdot\frac7{10}\cdot\frac1{13}.
\end{aligned}
\]

Therefore

\[
\boxed{
\|\sigma_X\|_{\rm at}>\frac{X}{4000}
\qquad(X\ge200).
}
\tag{L-30501.12}
\]

The bound is deliberately conservative.

## 6. Proof boundary

Closed here:

1. exact identification of the aggregate first boundary;
2. its one-term finite formula on a fixed top annulus;
3. a uniform positive \(X^{-1/2}\) moat;
4. uniqueness of the next-endpoint divisor source;
5. a linear lower bound in the exact atomic norm used by PR #304.

Not claimed:

1. a lower bound for the **optimized** Cycle Debt;
2. impossibility of cancellations with the retained analytic positive flow;
3. RH or its negation.
