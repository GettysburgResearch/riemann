# L-104543 — Weighted critical moments force an unweighted Rolle count

Claim ID: `L-104543`  
Status: **PROVED EXACT**  
Created: 2026-08-23  
Depends on: `L-104540`  
RH status: **not assumed**

Let `f` satisfy the regularity hypotheses of `L-104542`, and let `w` be any
positive `C^1` weight on `[a,b]`.

At the simple critical points `c_j` put

\[
a_j=w(c_j)|f(c_j)|,
\qquad
\varepsilon_j=
-\operatorname{sgn}f(c_j)\operatorname{sgn}f''(c_j)
\in\{+1,-1\}.
\tag{L-104543.1}
\]

Thus `epsilon_j=+1` at a Rolle-generating extremum. Define

\[
D_w=\sum_j\varepsilon_ja_j,
\qquad
B_w=\sum_j a_j^2,
\qquad
R=G+W.
\tag{L-104543.2}
\]

## 1. Exact weighted bias

The weighted monotone-interval calculation gives

\[
\boxed{
\begin{aligned}
2D_w
={}&
\int_a^b w(t)|f'(t)|\,dt
+\int_a^b w'(t)f(t)\operatorname{sgn}f'(t)\,dt\\
&+\operatorname{sgn}f'(a)w(a)f(a)
-\operatorname{sgn}f'(b)w(b)f(b).
\end{aligned}
}
\tag{L-104543.3}
\]

This is a source-visible first moment. The weight can be chosen to remove the
gamma envelope or to localize a short height window.

## 2. Second moment to count

Let `G` be the number of good critical points. Since

\[
(D_w)_+
\le
\sum_{\varepsilon_j=+1}a_j,
\]

Cauchy-Schwarz gives

\[
(D_w)_+^2
\le
G\sum_{\varepsilon_j=+1}a_j^2
\le
GB_w.
\]

Therefore

\[
\boxed{
G\ge\frac{(D_w)_+^2}{B_w}.
}
\tag{L-104543.4}
\]

Equivalently,

\[
\boxed{
\frac{G-W}{R}
\ge
2\frac{(D_w)_+^2}{RB_w}-1.
}
\tag{L-104543.5}
\]

This bound is sharp for the supplied first and second moments.

## 3. Fixed-order Xi consequence

Take `f=Xi''` and let `R_3(T)` be the real simple zeros of `Xi'''` in a
regular height window. If one proves, for source-visible normalizers `w_T`,

\[
\boxed{
\liminf_{T\to\infty}
\frac{(D_{w_T})_+^2}
     {R_3(T)B_{w_T}}
\ge
\frac{1+\eta}{2}
}
\tag{L-104543.6}
\]

for some `eta>0`, then a proportion at least `(1+eta)/2` of those derivative
zeros is Rolle-generating. The exact factor-two count gives

\[
\boxed{
\alpha_2\ge\eta\alpha_3.
}
\tag{L-104543.7}
\]

Using Conrey's fixed-order input `alpha_3>0.9873`,

\[
\boxed{
\alpha_2>0.9873\,\eta.
}
\tag{L-104543.8}
\]

The `alpha_3` hypothesis is load bearing.

## 4. New terminal target

```text
CM2X104590 — critical marked two-moment theorem

Construct a fixed-order source-visible normalizer w_T and prove (L-104543.6)
for Xi'' at the real Xi''' zeros.
```

Unlike `AMPREG104580`, this target needs no first absolute critical-value
moment and no coefficient-of-variation subtraction. It asks only for:

1. the exact weighted signed first moment (L-104543.3);
2. one marked discrete second moment `B_w`.

The second object has the contour representation of `L-104544`.
