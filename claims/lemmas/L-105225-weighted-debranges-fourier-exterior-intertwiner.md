# L-105225 — Weighted de Branges and Fourier exterior squares are linked by one explicit contraction

Claim ID: `L-105225`  
Status: **PROPOSED EXACT COMPOUND-SPACE THEOREM; independent review pending**  
Created: 2026-08-23  
Depends on: `L-105224`; PR #724 `L-105207` and `L-105212`  
RH status: **not assumed**

## 1. One derivative step and one physical weight

Fix an integer \(k\ge 1\), put

\[
F=\Xi^{(k-1)},\qquad G=F'=\Xi^{(k)},
\]

and let \(c_1,\ldots,c_R\) be distinct simple real zeros of \(G\). Write

\[
h_i=F''(c_i)=\Xi^{(k+1)}(c_i)\ne0,
\qquad
\rho_i=\frac{F(c_i)}{h_i}.
\tag{L-105225.1}
\]

Fix a real centre \(a\). With the safe multiplier from `L-105224`,

\[
g_a(z)=\frac{6}{(z-a+i)(z-a+2i)(z-a+3i)},
\]

put

\[
w_i=|g_a(c_i)|^2=\Omega_a(c_i)>0,
\qquad
N=\sum_iw_i,
\]

\[
A=-\sum_iw_i\rho_i,
\qquad
B=\sum_iw_i\rho_i^2.
\tag{L-105225.2}
\]

Assume the finite de Branges hypotheses of `L-105224`. In the normalized
Clark basis at the zeros \(c_i\), its two moment vectors have coordinates

\[
u_i=\sqrt\pi\,\theta_i\sqrt{w_i},
\qquad
v_i=\sqrt\pi\,\theta_i\sqrt{w_i}\rho_i,
\tag{L-105225.3}
\]

where every \(\theta_i\) has modulus one. Consequently

\[
\boxed{
\|u\wedge v\|^2
=
\pi^2\sum_{i<j}w_iw_j(\rho_i-\rho_j)^2
=
\pi^2(NB-A^2).
}
\tag{L-105225.4}
\]

This is the correction-free de Branges exterior square of `L-105224`.

## 2. The exterior-square Fourier samples

Choose any split

\[
r+s=k-1,\qquad r,s\ge0.
\]

Use the unconditional exterior-square Fourier vectors of PR #724:

\[
x=\omega_{r,0},
\qquad
y_i=\frac{\omega_{s,c_i}}{h_i^2}.
\tag{L-105225.5}
\]

Then `L-105212` gives

\[
\boxed{
\langle x,y_i\rangle=-\rho_i,
\qquad
\|x\|^2=\Lambda_{2r}(0),
}
\tag{L-105225.6}
\]

and

\[
K_{ij}:=\langle y_i,y_j\rangle
=
\frac{\Lambda_{2s}(c_j-c_i)}{h_i^2h_j^2}.
\tag{L-105225.7}
\]

In particular \(K\succeq0\).

Define the physical pair bundle

\[
Z_a=
\bigoplus_{i<j}\sqrt{w_iw_j}\,(y_j-y_i).
\tag{L-105225.8}
\]

Let

\[
\mathcal J_x:
\bigoplus_{i<j}\mathcal H_{\rm ext}\longrightarrow
\ell^2\{(i,j):i<j\}
\]

be the coordinate map

\[
\mathcal J_x((z_{ij}))=(\langle x,z_{ij}\rangle)_{i<j}.
\tag{L-105225.9}
\]

It has operator norm at most \(\|x\|\). Equations (L-105225.3) and
(L-105225.6) show that there is a diagonal unitary \(U_a\) on the
pair-coordinate space such that

\[
\boxed{
u\wedge v=\pi U_a\mathcal J_x Z_a.}
\tag{L-105225.10}
\]

This is the explicit source-faithful intertwiner requested in `T-105230`.
It is not chosen after observing the residue signs: \(x\), \(y_i\), \(w_i\),
and the harmless phases in \(U_a\) are fixed by the Xi Fourier source, the
derivative level, and the safe multiplier.

Taking norms gives

\[
\boxed{
NB-A^2
\le
\Lambda_{2r}(0)
\sum_{i<j}w_iw_j\|y_i-y_j\|^2.
}
\tag{L-105225.11}
\]

## 3. Weighted Hilbert variance and the exact Gram form

Let

\[
W=\operatorname{diag}(w_1,\ldots,w_R),
\qquad
\mathbf w=(w_1,\ldots,w_R)^T,
\]

and define the weighted centering matrix

\[
\boxed{L_w=W-\frac{\mathbf w\mathbf w^T}{N}\succeq0.}
\tag{L-105225.12}
\]

If \(Y:\mathbb C^R\to\mathcal H_{\rm ext}\) sends the \(i\)-th coordinate
vector to \(y_i\), then \(K=Y^*Y\). The weighted Hilbert variance identity is

\[
\boxed{
\sum_{i<j}w_iw_j\|y_i-y_j\|^2
=
N\sum_iw_i\|y_i\|^2
-\left\|\sum_iw_iy_i\right\|^2
=
N\operatorname{tr}(L_wK).
}
\tag{L-105225.13}
\]

Since the residue vector is \(\rho=-Y^*x\),

\[
\boxed{NB-A^2=N\langle x,YL_wY^*x\rangle.}
\tag{L-105225.14}
\]

Therefore the sharper spectral estimate is

\[
\boxed{
NB-A^2
\le
N\Lambda_{2r}(0)
\left\|L_w^{1/2}KL_w^{1/2}\right\|_{\rm op}.
}
\tag{L-105225.15}
\]

The trace relaxation is

\[
\boxed{
NB-A^2
\le
\Lambda_{2r}(0)
\left[N\operatorname{tr}(WK)-\mathbf w^TK\mathbf w\right].
}
\tag{L-105225.16}
\]

The negative cross term is load bearing. It records coherent translation
overlap of the same physical exterior-square source.

## 4. Meaning and scope

The theorem supplies the previously missing map between

```text
de Branges residue-moment wedge
        and
Xi exterior-square Fourier near-collision energy.
```

It closes that compositional interface exactly. It does not prove that the
centered Gram operator in (L-105225.15) is small at fixed low derivative
order. That remaining estimate is arithmetic/analytic and is isolated in
`T-105231`.
