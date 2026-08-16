# L-96302 — The single-row producer is a positive smoothing of one universal reciprocal-zeta Riesz potential

Claim ID: `L-96302`  
Status: **PROVED EXACT FINITE CONVOLUTION AND MELLIN IDENTITY**  
Created: 2026-08-17  
RH status: **not assumed**

Define

\[
\boxed{
\mathcal V(x)
=
\sum_{d\le x}\frac{\mu(d)}{\sqrt d}
\log\frac xd,
\qquad x\ge1.
}
\tag{L-96302.1}
\]

For `Re(s)>1/2`, finite Fubini gives

\[
\boxed{
\int_1^\infty \mathcal V(x)x^{-s-1}\,dx
=
\frac1{s^2\zeta(s+1/2)}.
}
\tag{L-96302.2}
\]

Thus eventual nonnegativity of `mathcal V` is itself a direct Landau criterion for RH.

Using the positive base dictionary `q_*` of `L-96301`, reindexing the finite double sum gives

\[
\boxed{
\mathcal R_X
=
\sum_{m\le X}\frac{q_*(m)}{\sqrt m}
\mathcal V(X/m).
}
\tag{L-96302.3}
\]

Every coefficient in (L-96302.3) is positive. Hence

\[
\mathcal V(x)\ge0\ \text{eventually}
\quad\Longrightarrow\quad
\mathcal R_X\ge0\ \text{eventually}
\quad\Longrightarrow\quad\mathrm{RH}.
\]

The first implication is only sufficient: the positive smoothing may remain nonnegative despite localized negative values of `mathcal V`.

## Prime-power feedback equation

Put `v(t)=mathcal V(e^t)` and extend `v(t)=0` for `t<0`. Logarithmic differentiation of (L-96302.2) gives the exact distributional delay identity

\[
\boxed{
 t v(t)
 =2\int_0^t v(u)\,du
 -\sum_{q=p^a\le e^t}
 \frac{\Lambda(q)}{\sqrt q}
 v(t-\log q).
}
\tag{L-96302.4}
\]

This is the common prime-power feedback equation behind the reciprocal-row and complete-gap fronts. It contains no zero data and is a concrete target for a Lyapunov or variation-diminishing proof.
