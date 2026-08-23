# L-104541 — Critical-value amplitude regularity converts weighted reverse Rolle into a count

Claim ID: `L-104541`  
Status: **PROVED EXACT CONDITIONAL COUNT TRANSFER**  
Created: 2026-08-23  
Depends on: `L-104540`  
RH status: **not assumed**

Let `f` satisfy the hypotheses of `L-104540` on a regular interval `[a,b]`.
Write its simple critical points as `c_1,...,c_R`, and put

\[
a_j=|f(c_j)|,
\qquad
\varepsilon_j=
\begin{cases}
+1,&c_j\text{ is Rolle-generating},\\
-1,&c_j\text{ is wrong}.
\end{cases}
\]

Define

\[
S=\sum_{j=1}^{R}a_j,
\qquad
D=\sum_{j=1}^{R}\varepsilon_j a_j,
\tag{L-104541.1}
\]

and, when `R>0` and `S>0`,

\[
\bar a={S\over R},
\qquad
\sigma_a^2={1\over R}\sum_{j=1}^{R}(a_j-\bar a)^2,
\qquad
v_a={\sigma_a\over\bar a},
\qquad
\rho_a={D\over S}.
\tag{L-104541.2}
\]

By `L-104540`,

\[
D={1\over2}
\left[
 \int_a^b|f'(t)|dt
 +\operatorname{sgn}f'(a)f(a)
 -\operatorname{sgn}f'(b)f(b)
\right].
\tag{L-104541.3}
\]

## 1. Exact conversion from amplitude bias to count bias

Let

\[
G=\#\{j:\varepsilon_j=+1\},
\qquad
W=\#\{j:\varepsilon_j=-1\},
\qquad
R=G+W.
\]

Since

\[
D
=\bar a(G-W)
 +\sum_{j=1}^{R}\varepsilon_j(a_j-\bar a),
\]

Cauchy--Schwarz gives

\[
\left|
\sum_{j=1}^{R}\varepsilon_j(a_j-\bar a)
\right|
\le R\sigma_a.
\]

Therefore

\[
\boxed{
{G-W\over R}
\ge \rho_a-v_a.
}
\tag{L-104541.4}
\]

Equivalently,

\[
\boxed{
{G\over R}
\ge {1\over2}+{\rho_a-v_a\over2}.
}
\tag{L-104541.5}
\]

Thus the proved amplitude-weighted majority of `L-104540` becomes a strict
unweighted majority as soon as its normalized amplitude bias exceeds the
coefficient of variation of the critical values.

This is sharp at the level of the two supplied moments: equality can occur
when the centered amplitude vector is proportional to the orientation vector.

## 2. Xi fixed-order consequence

Take

\[
f(t)=\Xi''(t)
\]

on regular symmetric intervals `[-T,T]`. Let `rho_T` and `v_T` be the
quantities in (L-104541.2), formed from all real simple zeros of `Xi'''` in the
interval. Stirling decay makes the endpoint term in (L-104541.3) negligible
under the fixed-order zero-count normalization.

Suppose

\[
\boxed{
\liminf_{T\to\infty}(\rho_T-v_T)\ge\eta>0.
}
\tag{L-104541.6}
\]

Then a proportion at least `(1+eta)/2` of the real `Xi'''` zeros is
Rolle-generating for `Xi''`. Combining with `L-104538` gives

\[
\boxed{
\alpha_2\ge \eta\,\alpha_3.
}
\tag{L-104541.7}
\]

With Conrey's unconditional `alpha_3>0.9873`,

\[
\boxed{
\alpha_2>0.9873\,\eta.
}
\tag{L-104541.8}
\]

The third-derivative proportion is load bearing and the independent known
`alpha_2>0.9584` theorem is not used.

## 3. New two-moment target

The conclusion-facing amplitude theorem is

```text
AMPREG104580 — critical-value amplitude regularity

For Xi'' at the real zeros of Xi''', prove

  liminf (rho_T-v_T) > 0,

where rho_T is the exact total-variation amplitude bias of L-104540 and v_T
is the coefficient of variation of |Xi''(c)|.
```

This target involves only the first two moments of the **critical values** of
`Xi''`; it does not count parent zeros and it is distinct from the inverse-
curvature residue moments in `RCMV104530`.

## 4. Scope

`L-104540` alone gives a weighted majority, not a count majority.  The
regularity condition (L-104541.6) is not proved here.  The theorem isolates the
precise amplitude statistic needed to turn the unconditional total-variation
identity into a genuine fixed-order proportion descent.
