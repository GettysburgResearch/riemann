# L-23712 — Digital Abel descent and eventual positivity

Claim ID: `L-23712`  
Title: Subquadratic logarithmic boundary energy forces eventual positivity of the fifth-aligned cumulative shell by an exact dyadic descent  
Status: **PROPOSED EXACT/ASYMPTOTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23709`, `L-23711`  
Scope: repairs the global implication in `T-23704`; no energy upper bound is proved

## 1. Exact one-step lower bound

Retain

\[
C(y)=\mathfrak S_5(y),
\qquad
Y_m(y)=m^{-1/2}C(y/m),
\qquad
M=\lfloor y\rfloor,
\]

and the digital forcing

\[
R_5(y)=p(y)-\sqrt5\,p(y/5).
\]

The exact Abel identity of `L-23711` is

\[
\begin{aligned}
C(y)={}&R_5(y)+Y_2(y)-s_5(M)Y_M(y)\\
&-\sum_{m=2}^{M-1}s_5(m)
 [Y_m(y)-Y_{m+1}(y)].
\end{aligned}
\tag{L-23712.1}
\]

Define

\[
\mathcal E_5(y)
=\sum_{m=2}^{M-1}m^2|Y_m(y)-Y_{m+1}(y)|^2
\]

and

\[
\kappa_5^2=\sum_{m=2}^{\infty}\frac{s_5(m)^2}{m^2}<\infty.
\]

Since

\[
Y_2(y)=2^{-1/2}C(y/2)
\]

and

\[
0\le s_5(M)Y_M(y)\le s_5(M)M^{-3/2},
\]

Cauchy--Schwarz gives the global, sign-free recurrence

\[
\boxed{
C(y)
\ge
R_5(y)
+2^{-1/2}C(y/2)
-\kappa_5\sqrt{\mathcal E_5(y)}
-\frac{s_5(\lfloor y\rfloor)}{\lfloor y\rfloor^{3/2}}.
}
\tag{L-23712.2}
\]

No first-zero assumption occurs in this inequality.

## 2. Asymptotic forcing

For `y>=5`,

\[
\boxed{
R_5(y)
=(\sqrt5-1)\log y
+4(\sqrt5-1)-\sqrt5\log5.
}
\tag{L-23712.3}
\]

Put

\[
a=\sqrt5-1>0,
\qquad q=2^{-1/2}<1.
\]

Also

\[
\frac{s_5(\lfloor y\rfloor)}{\lfloor y\rfloor^{3/2}}=o(1).
\tag{L-23712.4}
\]

Assume

\[
\boxed{
\mathcal E_5(y)=o((\log y)^2).
}
\tag{L-23712.5}
\]

Then, for every fixed `0<eta<a`, there is `Y_eta` such that

\[
\kappa_5\sqrt{\mathcal E_5(y)}
+\frac{s_5(\lfloor y\rfloor)}{\lfloor y\rfloor^{3/2}}
\le\eta\log y
\qquad(y\ge Y_\eta).
\tag{L-23712.6}
\]

Therefore (L-23712.2) gives

\[
\boxed{
C(y)
\ge
(a-\eta)\log y+b_5+qC(y/2)
\qquad(y\ge Y_\eta),
}
\tag{L-23712.7}
\]

where

\[
b_5=4(\sqrt5-1)-\sqrt5\log5
\]

is an absolute constant.

## 3. Iteration

For `y>=2Y_eta`, let `J` be the unique integer such that

\[
Y_\eta\le y/2^J<2Y_\eta.
\]

Iterating (L-23712.7) gives

\[
\begin{aligned}
C(y)
\ge{}&
\sum_{j=0}^{J-1}q^j
\left[(a-\eta)\log(y/2^j)+b_5\right]
+q^J C(y/2^J).
\end{aligned}
\tag{L-23712.8}
\]

The compact terminal interval has a finite lower bound

\[
B_\eta
=\inf_{Y_\eta\le u\le2Y_\eta}C(u)>-\infty,
\]

because `C` is continuous. Moreover

\[
\sum_{j=0}^{J-1}q^j\log(y/2^j)
=
\frac{\log y}{1-q}
-\frac{q\log2}{(1-q)^2}
+O(q^J\log y),
\tag{L-23712.9}
\]

and

\[
q^J B_\eta=o(1).
\]

Consequently

\[
\boxed{
C(y)
\ge
\frac{a-\eta}{1-q}\log y-O_\eta(1)
\qquad(y\to\infty).
}
\tag{L-23712.10}
\]

In particular,

\[
\boxed{
C(y)>0
\quad\text{for every sufficiently large }y.
}
\tag{L-23712.11}
\]

This is the one-sign conclusion required by Landau. Positivity on every finite initial annulus is not needed for the RH implication.

## 4. Correction to the first-zero-only argument

The earlier first-crossing barrier remains a valid local theorem, but the inference

```text
E_5(y)=o((log y)^2)
+ one finite positive annulus
=> no first zero
```

is not logically sufficient unless the asymptotic threshold is made effective and the entire preceding compact interval is checked. A first zero could lie before that threshold.

Equation (L-23712.2) removes this defect. It proves eventual positivity directly from the asymptotic energy estimate and therefore supplies exactly the hypothesis needed for the Mellin/Landau argument.

## 5. Proof boundary

Closed here:

- the global one-step digital descent;
- iteration of the lower-scale recurrence;
- `CRE(5) => eventual positivity`;
- the correction of the first-zero-only inference.

Open:

- `CRE(5)` itself;
- the source-specific reflected-energy estimate;
- Greedy Slack/DCRS;
- RH.
