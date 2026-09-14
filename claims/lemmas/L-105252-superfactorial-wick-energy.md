# L-105252 — Superfactorial residual energy and the all-degree effective-rank reserve

Claim ID: `L-105252`  
Status: **PROVED FROM L-105250 AND THE PINNED PRIME-SIMPLEX ENERGY LAW**  
Created: 2026-08-24  
Depends on: L-105250; PR #726 L-105321/L-105511 at `45e416d932818399045ec7d3ba36e9d6efc50f00`  
RH status: not assumed

At the frozen one-sided prime-simplex model, a source coefficient in degree `m` contributes normalized diagonal energy
\[
t_m=\frac{m!}{(2m)!}.
\tag{1}
\]
For the degree-`K` square-root polynomial, define
\[
\boxed{
\mathcal D_K=
\sum_{m\ge K+1}q_{K,m}^2\,\frac{m!}{(2m)!}.
}
\tag{2}
\]

By L-105250, `0<=q_(K,m)<=c_K^2`. Moreover
\[
\frac{t_{m+1}}{t_m}=\frac1{2(2m+1)}
\le\frac1{4K+6}\qquad(m\ge K+1).
\]
Therefore
\[
\boxed{
\mathcal D_K
\le
c_K^4
\frac{(K+1)!}{(2K+2)!}
\frac{4K+6}{4K+5}.
}
\tag{3}
\]
In particular
\[
\boxed{\mathcal D_K\longrightarrow0}
\tag{4}
\]
superfactorially.

The first two levels admit sharper explicit bounds
\[
\mathcal D_1
=\frac1{16}\sum_{m\ge2}\frac{m!}{(2m)!}
<\frac3{520},
\tag{5}
\]
and
\[
\boxed{
\mathcal D_2
\le\frac{1669}{11698176}
<\frac1{7000}.
}
\tag{6}
\]

The frozen Hermitian two-sided symbol has normalized first moment one and second moment `1+2 D_K`. Hence its normalized effective rank obeys
\[
\boxed{
\eta_K\ge\frac1{1+2\mathcal D_K}.
}
\tag{7}
\]
Combining this with the exact confluent full-signature theorem from PR #726 gives the perfect-transfer model proportion
\[
\boxed{
p_K^{\rm model}
\ge
\frac{2}{1+2\mathcal D_K}-1
\longrightarrow1.
}
\tag{8}
\]

This is a model/source theorem. It does not identify the frozen source form with the actual Xi contour matrix.
