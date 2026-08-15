# L-93921 — A moving top anchor makes the single retained-cell mismatch subordinate in every native column

Claim ID: `L-93921`  
Status: **PROPOSED COMPLETE ALL-COLUMN ESTIMATE ON THE FROZEN ADJACENT-CELL ERROR BOUND — REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-93920`; the retained-cell estimate `|epsilon_X(m)|<(19/2)m^(-3/2)` from `L-91733`  
RH status: **unproved**

Let

\[
\varepsilon_X(m)
=d_X^\star(m)-\int_m^{m+1}d_X^\star(t)\,dt
\]

on `m in \mathcal I_X` and zero otherwise. The exact carry telescope gives

\[
v_q(E_X^I)=\sum_{j\ge1}\varepsilon_X(jq).
\tag{L-93921.1}
\]

## 1. Uniform ordinary and detail bounds

Because every active multiple satisfies `jq>K`,

\[
\begin{aligned}
|v_q(E_X^I)|
&<\frac{19}{2}q^{-3/2}
  \sum_{j\ge\lceil K/q\rceil}j^{-3/2}\\
&<\frac{57}{2q\sqrt K}.
\end{aligned}
\tag{L-93921.2}
\]

Therefore

\[
\boxed{
|\mathcal D_4v_q(E_X^I)|
<\frac{171}{4q\sqrt K}
\qquad(q\ge2).
}
\tag{L-93921.3}
\]

This includes every small column `2<=q<K`.

## 2. Nonterminal relative bound

For `q<=X/4`,

\[
\Omega_X(q)=\frac{\log4}{\sqrt q}
>\frac4{3\sqrt q}.
\]

Hence

\[
\frac{|\mathcal D_4v_q(E_X^I)|}{\Omega_X(q)}
<\frac{513}{16\sqrt{qK}}
\le\frac{513}{16\sqrt{2K}}
<\frac{23}{\sqrt K}.
\tag{L-93921.4}
\]

The last inequality is exact because

\[
513^2<2\cdot368^2.
\]

## 3. Terminal relative bound

For `q>X/4`, `v_(4q)(E_X^I)=0`. If `v_q(E_X^I)` is nonzero, then only `j=1,2,3` occur and `q<=X-W_X-3`. Using

\[
1+\frac1{2\sqrt2}+\frac1{3\sqrt3}<\frac85
\]

gives

\[
|v_q(E_X^I)|
<\frac{608}{5}X^{-3/2}.
\tag{L-93921.5}
\]

Moreover

\[
\log\frac Xq
\ge\frac{X-q}{X}
\ge\frac{W_X+3}{X},
\]

so

\[
\Omega_X(q)
=q^{-1/2}\log(X/q)
\ge(W_X+3)X^{-3/2}.
\]

Since `W_X+3>6\sqrt K`,

\[
\frac{|v_q(E_X^I)|}{\Omega_X(q)}
<\frac{608}{5(W_X+3)}
<\frac{304}{15\sqrt K}
<\frac{23}{\sqrt K}.
\tag{L-93921.6}
\]

If `v_q(E_X^I)=0`, the same conclusion is immediate. Thus (L-93921.4) and (L-93921.6) cover every physical detail column.

## 4. One common thinning and one row

Put

\[
\tau_K=\frac{\sqrt K}{\sqrt K+24}
\]

and define the final row

\[
\boxed{d_X=\tau_Kd_X^0.}
\tag{L-93921.7}
\]

It remains coefficientwise nonnegative. By `L-93920.9`,

\[
\begin{aligned}
\Xi_{d_X}(q)
&=\tau_K
 [\Omega_X(q)-\mathcal D_4v_q(E_X^I)]\\
&\le
\tau_K\left(1+\frac{23}{\sqrt K}\right)\Omega_X(q)\\
&=\frac{\sqrt K+23}{\sqrt K+24}\Omega_X(q)
<\Omega_X(q).
\end{aligned}
\tag{L-93921.8}
\]

Therefore

\[
\boxed{r_X^{(4)}(q)=\Omega_X(q)-\Xi_{d_X}(q)>0}
\]

whenever the native capacity is nonzero, and it is zero when both sides vanish.

The exact positive radix-four inverse gives

\[
\boxed{
 w_X(q)-C_{d_X}(q)
 =\sum_{h\ge0}2^hr_X^{(4)}(4^hq)
 \ge0.
}
\tag{L-93921.9}

Thus one actual nonnegative row satisfies every ordinary and detail capacity.

## 5. What disappeared

Compared with the unreviewed hybrid on PR #509, this direct-row construction needs none of:

```text
bulk B-spline quantization;
intrinsic quantizer collar;
fixed top omission reserve;
terminal 4452/5033 comparison;
causal subdivision of p_s;
rough-lift parent substitution.
```

The moving top anchor is exact finite source, not discarded source. It is used only to make the remaining bulk quadrature defect uniformly relative to the vanishing terminal capacity.
