# L-91353 — A causal shifted-eight target transport produces a positive all-row packet with uniformly bounded score debt

Claim ID: `L-91353`  
Status: **PROVED POSITIVE-PACKET / BOUNDED-DEBT THEOREM — GLOBAL SOURCE REGROUPING SEPARATE**  
Created: 2026-08-13  
Depends on: `L-91343`, `L-91352`; positive component-row identity from `L-91112.25--26`  
RH status: **unproved**

## 1. One-prime source atoms

For `p>=67`, `1<=y<67`, and a source `d`, define

\[
T_d=K_4(d;p,y),
\qquad
S_d=K_5(d;p,y).
\]

Whenever `T_d>0`, put

\[
\sigma_d=\frac{S_d}{T_d}.
\]

The formulas of `L-91345` give

\[
\frac54<\sigma_d\le2
\tag{L-91353.1}
\]

and show that `sigma_d` is nondecreasing in `d` inside each activation regime and across the child-activation interface.

## 2. Every positive source atom has a nonnegative complete row

Let

\[
h_X(m)=m^{-1/2}\log(X/m)\mathbf1_{m\le X}
\]

and put

\[
g_{p,y}(m)=h_{py}(m)-p^{-1/2}h_y(m).
\]

For `m<=y`,

\[
g_{p,y}(m)=m^{-1/2}
\left[(1-p^{-1/2})\log(y/m)+\log p\right],
\]

while for `y<m<=py`,

\[
g_{p,y}(m)=m^{-1/2}\log(py/m).
\]

Thus `g_(p,y)>=0`, it is continuous at `m=y`, and direct differentiation on both pieces gives

\[
\boxed{g_{p,y}'(m)<0.}
\tag{L-91353.2}
\]

For any nonnegative decreasing sequence `g`, the component-row functional has the positive form

\[
\begin{aligned}
\mathcal Q_j[g]={}&
\frac{j+1}{j-1}[g(j)-g(j+1)]\\
&+\frac{2(j+1)}{j(j-1)}g(j+1)
+\frac2{j(j-1)}\sum_{m\ge j+2}g(m)
\ge0.
\end{aligned}
\tag{L-91353.3}
\]

By linearity,

\[
\boxed{
Q_{py}(j)-p^{-1/2}Q_y(j)=\mathcal Q_j[g_{p,y}]\ge0
\qquad(j\ge2).
}
\tag{L-91353.4
}

After the source dilation `d`, every individual one-prime residual atom therefore produces a coefficientwise nonnegative row in **all** row indices, not only the inherited range.

## 3. Positive target-Hall residual

Choose any target-mass Hall flow `t_(o,e)` supplied by `L-91352`, so

\[
\sum_e t_{o,e}=T_o,
\qquad
\sum_o t_{o,e}\le T_e,
\qquad
 e\le o+8.
\]

Define residual target masses

\[
r_e=T_e-\sum_ot_{o,e}\ge0
\]

and the positive coefficient measure

\[
\boxed{\nu(e)=r_e/T_e.}
\tag{L-91353.5
}

Then

\[
\boxed{
\sum_e\nu(e)T_e
=
\sum_{\mu(e)=1}T_e-
\sum_{\mu(o)=-1}T_o.
}
\tag{L-91353.6
}

Thus the signed one-prime target is represented exactly by a positive source measure. By (L-91353.4), the corresponding complete row is coefficientwise nonnegative.

This gives a constructive positive row packet. It is not asserted to equal the signed arithmetic residual row, nor is it yet identified with the standard single-endpoint source cone of `L-91343`. `R-91309` remains a mandatory firewall against either stronger inference.

## 4. Exact score difference

The score of the positive residual minus the signed arithmetic score is

\[
\boxed{
\mathfrak S(\nu)-\mathfrak S_{\rm signed}
=
\sum_{o,e}t_{o,e}(\sigma_o-\sigma_e).
}
\tag{L-91353.7
}

No-upward edges are favorable. Only edges with `o<e<=o+8` can create positive score loss.

## 5. Uniform bound away from the activation interface

Within either activation regime,

\[
\sigma(d)=\frac{5u_d-3}{4u_d-3},
\qquad
u_d=C/\sqrt d,
\]

up to a common positive scalar. Hence

\[
\sigma'(d)=\frac{3u_d}{2d(4u_d-3)^2}.
\]

For `d in [o,e]` with `e<=o+8`, put `q=sqrt(d/o)<=3`. Since `u_o=q u_d` and `u_d>=1`,

\[
\frac{T_o}{T_d}
=q\frac{4qu_d-3}{4u_d-3}
\le4q^2
\le36.
\]

Moreover

\[
T_d\sigma'(d)
=\frac{3u_d}{2d^{3/2}(4u_d-3)}
\le\frac3{2d^{3/2}}.
\]

Therefore one same-regime upward edge has adverse score at most

\[
\boxed{
T_o(\sigma_e-\sigma_o)
\le432\,o^{-3/2}.
}
\tag{L-91353.8
}

Using `sum_(n>=1)n^(-3/2)<3`, the total same-regime adverse score is below `1296`.

## 6. Interface edges

An edge can cross `d=y` only if `y-8<o<=y`, so there are at most eight crossing odd demands. Write

\[
u=\sqrt{py/e},
\qquad
R=(1+p^{-1/2})\sqrt{e/o}.
\]

Then `R<=27/8`, and the two score-per-target ratios are `sigma(u)` and `sigma(Ru)`, where

\[
\left|\frac d{du}\frac{5u-3}{4u-3}\right|
=\frac3{(4u-3)^2}
\le\frac3{u^2}.
\]

Thus

\[
\sigma(u)-\sigma(Ru)
\le\frac{3(R-1)}{Ru}.
\]

The child-active target demand satisfies

\[
T_o\le\frac{4(1-p^{-1/2})Ru}{\sqrt o}.
\]

Consequently

\[
T_o(\sigma_e-\sigma_o)_+
\le\frac{12(R-1)}{\sqrt o}
\le\frac{57}{2}<29.
\]

All interface edges together cost less than `232`. Combining Sections 5--6,

\[
\boxed{
\mathfrak S(\nu)
\ge
\mathfrak S_{\rm signed}-1600.
}
\tag{L-91353.9
}

The constant is intentionally crude and independent of `p`, `y`, the threshold, and the selected Hall flow.

## 7. Consequence

The true causal one-prime splice admits a positive source/row packet which:

```text
represents the SHARP target exactly;
has every component row nonnegative;
has a uniformly bounded endpoint-score deficit;
requires a separate source-cone/capacity typing theorem before recursive use.
```

The theorem does not prove that the exact paired least-prime source tree can be regrouped into these complete one-prime packets without source or target duplication. That global packet-regrouping statement remains the load-bearing producer theorem.

```text
positive individual one-prime rows           EXACT
causal target Hall residual                   EXACT POSITIVE
standard positive-kernel entry                NOT YET IDENTIFIED
uniform score debt                            EXACT / CONSERVATIVE
arithmetic-row equality of Hall residual      NOT CLAIMED
all-generation source regrouping              OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
