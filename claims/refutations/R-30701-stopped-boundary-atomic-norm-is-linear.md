# R-30701 — The stopped central boundary has linear square-root atomic norm

Claim ID: `R-30701`  
Title: The complete first stopped-power boundary contains a macroscopic triangular divisor band, so its square-root divisor-source atomic norm is linear rather than polylogarithmic  
Status: **EXACT REFUTATION OF THE TERMINAL ATOMIC-NORM STEP IN PR #304**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #307  
Frozen parent: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Scope: the complete first-generation critical stopped-power boundary; no verdict on cycle-optimized flow

## 1. Critical central boundary

Put

\[
p(x)=x^{-1/2},
\qquad
w_X(x)=x^{-1/2}\log(X/x)\mathbf1_{x\le X}.
\]

For an integer column `q`, define

\[
(\mathcal C_Xw_X)(q)
=\sum_{k\ge1}
 [w_X(2kq-1)-w_X((2k+1)q)]
\tag{R-30701.1}
\]

and

\[
(\mathcal Cp)(q)
=\sum_{k\ge1}
 [p(2kq-1)-p((2k+1)q)].
\tag{R-30701.2}
\]

The second series converges by adjacent-pair cancellation. The complete first
stopped boundary in the sign convention used here is

\[
\boxed{
P_X(q)
=(\mathcal C_Xw_X)(q)
-\log\frac{X}{2q-1}(\mathcal Cp)(q),
}
\tag{R-30701.3}
\]

for `2q-1<=X`, and zero otherwise. Reversing the global sign does not affect the
atomic-norm conclusion.

## 2. Exact formula on one macroscopic band

Assume

\[
\frac{3X}{8}\le q\le\frac{2X}{5}.
\tag{R-30701.4}
\]

Then `3q>X`, so only the first positive finite term survives in (R-30701.1):

\[
(\mathcal C_Xw_X)(q)=w_X(2q-1).
\]

Consequently

\[
\boxed{
P_X(q)
=\log\frac{X}{2q-1}
\left[(2q-1)^{-1/2}-(\mathcal Cp)(q)\right].
}
\tag{R-30701.5}
\]

Expanding the alternating series gives

\[
\begin{aligned}
(2q-1)^{-1/2}-(\mathcal Cp)(q)
={}&(3q)^{-1/2}-(4q-1)^{-1/2}\\
&+(5q)^{-1/2}-(6q-1)^{-1/2}+\cdots.
\end{aligned}
\tag{R-30701.6}
\]

Every displayed pair is positive. Hence

\[
(2q-1)^{-1/2}-(\mathcal Cp)(q)
\ge
\left(\frac1{\sqrt3}-\sqrt{\frac27}\right)q^{-1/2},
\tag{R-30701.7}
\]

because `4q-1>=7q/2` for `q>=2`.

Also `2q-1<=4X/5`, so

\[
\log\frac{X}{2q-1}\ge\log\frac54.
\]

Therefore

\[
\boxed{
P_X(q)\ge c_0q^{-1/2},
\qquad
c_0=\log\frac54
\left(\frac1{\sqrt3}-\sqrt{\frac27}\right)>0.
}
\tag{R-30701.8}
\]

## 3. Completely rational moat

The lower bound can be made rational without decimal arithmetic:

\[
\log\frac54>\frac15,
\]

by `log(1+x)>x/(1+x)`, while

\[
\frac1{\sqrt3}>\frac7{13},
\qquad
\sqrt{\frac27}<\frac{15}{28}.
\]

Since

\[
\frac7{13}-\frac{15}{28}=\frac1{364},
\]

we have the explicit bound

\[
\boxed{c_0>\frac1{1820}.}
\tag{R-30701.9}
\]

## 4. Triangular divisor inversion

Let

\[
M=\left\lfloor\frac{X+1}{2}\right\rfloor
\]

and suppose the boundary is represented in the divisor-source coordinate
used by the terminal adjacent-commutator map:

\[
P_X(q)=\sum_{\substack{m\le M\\q\mid m}}\sigma_X(m).
\tag{R-30701.10}
\]

For every `q` in (R-30701.4), one has `2q>M`. Thus `q` has no second multiple
inside the state and (R-30701.10) is triangular:

\[
\boxed{\sigma_X(q)=P_X(q).}
\tag{R-30701.11}
\]

For every `X>=160`, the integer interval in (R-30701.4) contains at least
`X/80` elements. Combining (R-30701.9)--(R-30701.11) gives

\[
\begin{aligned}
\sum_{m\le M}\sqrt m\,|\sigma_X(m)|
&\ge
\sum_{3X/8\le q\le2X/5}\sqrt q\,P_X(q)\\
&>\frac1{1820}\cdot\frac{X}{80}.
\end{aligned}
\]

Hence

\[
\boxed{
\sum_{m\le M}\sqrt m\,|\sigma_X(m)|
>\frac{X}{145600}.
}
\tag{R-30701.12}
\]

## 5. Consequence

PR #304 terminates every emitted boundary source through

\[
\Phi(\sigma)=\sum_m\sigma_mE_{m-1}
\]

and bounds its negative capacity by a constant multiple of

\[
\sum_m\sqrt m|\sigma_m|.
\]

Equation (R-30701.12) proves that the complete first critical boundary already
has linear norm in that coordinate. No decomposition into finitely many Euler,
Peano, or Taylor channels can lower the atomic norm of the recombined total on
the triangular band.

Therefore:

```text
PR #304 polylog complete boundary atomic norm   FALSE
PR #304 terminal atom-by-atom closure           REJECTED
adjacent-tree source identity                   RETAINED
cycle-optimized coherent boundary flow          NOT REFUTED
RH                                                UNPROVED
```

## 6. Proof boundary

Proved exactly:

1. the macroscopic boundary formula;
2. a rational positive moat;
3. triangular uniqueness of the source coordinates;
4. the linear atomic lower bound.

Not proved:

1. a cycle-optimized boundary transference theorem;
2. Cycle Debt;
3. RH.
