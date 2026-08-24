# L-105561 — Analytic three-point pressure gives a strict unconditional gain

Claim ID: `L-105561`  
Status: **PROVED ANALYTICALLY; NO FINITE CERTIFICATE USED**

Let `k(x)` be the normalized optimized Montgomery--Taylor overlap kernel. Its
positive zeros satisfy

\[
x\tan(\pi x)=c,
\qquad
c=\frac{\tan(1/\sqrt2)}{\sqrt2\pi}>0.
\tag{1}
\]

If positive numbers `x`, `y`, and `x+y` were all zeros, the tangent addition
formula would give

\[
\frac{c}{x+y}
=
\frac{c/x+c/y}{1-c^2/(xy)}.
\]

After clearing denominators,

\[
\boxed{x^2+xy+y^2+c^2=0,}
\tag{2}
\]

which is impossible. Hence the positive zero set of `k` is sum-free.

Define

\[
\epsilon_4
=
\min_{\substack{u,v\ge0\\u+v\le4}}
\left(k(u)^2+k(v)^2+k(u+v)^2\right).
\tag{3}
\]

The compact triangle in (3) cannot contain a simultaneous zero by (2), and at
`u=0` or `v=0` one summand equals one. Therefore

\[
\boxed{\epsilon_4>0.}
\tag{4}
\]

Partition the normalized zero interval into cells of length four and split the
simple on-line zeros in each cell into disjoint triples. The zero-counting
asymptotic gives at least

\[
\frac13\left(S-\frac N2\right)-o(N)
\tag{5}
\]

triples. Join each triple by its three edges. The graph has maximum degree two,
and the dual form of `Psi` gives

\[
\Delta(M)
\ge
\frac32\sum_{\{i,j\}\in E}|\langle v_i,v_j\rangle|^2
\ge
\frac{\epsilon_4}{2}\left(S-\frac N2\right)-o(N).
\tag{6}
\]

Combining (6) with `L-105560` yields

\[
\boxed{
\liminf\frac SN
\ge
\frac{H_0-\epsilon_4/4}{1-\epsilon_4/2}
>H_0.
}
\tag{7}
\]

Thus a strict unconditional improvement over the formal baseline is already a
machine-free theorem. The finite seven-gap certificate is needed only for the
stronger explicit value in `T-105560`.
