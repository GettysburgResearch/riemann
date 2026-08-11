# L-91108 — The full theta source supplies an exact supersymmetric passive bulk

Claim ID: `L-91108`  
Status: **EXACT THETA FACTORIZATION; BOUNDARY IDENTIFICATION OPEN**  
Created: 2026-08-11  
Depends on: PR #202 `L-19814`--`L-19817`; `L-91105`--`L-91107`  
RH status: **unproved**

## 1. Theta Gibbs ensemble

For `v>=0` put

\[
 b_n(v)=e^{v/4-\pi n^2e^v},
 \qquad
 B(v)=\sum_{n\ge1}b_n(v),
 \qquad
 p_n(v)=\frac{b_n(v)}{B(v)},
 \qquad
 Y_n(v)=\pi n^2e^v.
\]

Define

\[
 a(v)=-\frac{B'(v)}{B(v)}=\mathbb E_vY-\frac14
\]

and

\[
 \Psi(v)=\Phi(v/2),
 \qquad
 \mu(v)=\frac{\Psi(v)}{B(v)}.
\]

Differentiation of the Gibbs weights gives

\[
 a'(v)=a(v)+\frac14-\operatorname{Var}_v(Y).
\tag{L-91108.1a}
\]

The exact theta variance identity from PR #202 is

\[
\boxed{
 \mu(v)=4a(v)^2-4a'(v)-\frac14
 =4\left(a-\frac54\right)\left(a+\frac14\right)
  +4\operatorname{Var}_v(Y).
}
\tag{L-91108.1}
\]

The variance term is itself the pairwise square

\[
 4\operatorname{Var}_v(Y)
 =2\sum_{m,n}p_m(v)p_n(v)(Y_m(v)-Y_n(v))^2.
\tag{L-91108.2}
\]

## 2. Supersymmetric Hamiltonian

On the compact smooth core of `L^2(0,infinity)` define

\[
 Q_\theta=2(\partial_v+a(v)).
\]

Then

\[
\boxed{
 \mathcal H_\theta
 :=Q_\theta^*Q_\theta
 =-4\partial_v^2+\mu(v)+\frac14
 \succeq0.
}
\tag{L-91108.3}
\]

Moreover

\[
 Q_\theta B=0.
\tag{L-91108.4}
\]

Thus the full theta family already supplies a canonical positive bulk operator with a ground state. The cross-mode variance coordinates in (L-91108.2) are load-bearing: every one-mode reduction deletes them.

## 3. Exact Xi impedance in theta coordinates

From

\[
 \Xi(z)=\int_{\mathbb R}\Phi(t)e^{izt}dt
\]

and evenness of `Phi`, the impedance of `L-91105` is

\[
\boxed{
 \ell_a(r)
 =\frac{\displaystyle\int_0^\infty
       \Phi(t)\sinh(rt)\sinh(at)\,dt}
       {\displaystyle\int_0^\infty
       \Phi(t)\cosh(rt)\cosh(at)\,dt}.
}
\tag{L-91108.5}
\]

It is therefore the odd/even port ratio of one positive theta source.

## 4. The new constructive target

The old open statement was the matrix inequality

\[
 \left(\frac{\ell_a(r_i)+\ell_a(r_j)}{r_i+r_j}\right)\succeq0.
\]

The radical replacement is an identity problem:

> Construct an `a`-dependent boundary triple or passive two-port for the positive bulk `H_theta` whose Weyl/Dirichlet-to-Neumann function is exactly `ell_a`.

If `Gamma_0,Gamma_1` are the two ports and `f_r` is the decaying solution at spectral parameter `r`, the desired normalization is

\[
 \Gamma_0 f_r
 =\int_0^\infty\Phi(t)\cosh(rt)\cosh(at)dt,
\]

\[
 \Gamma_1 f_r
 =\int_0^\infty\Phi(t)\sinh(rt)\sinh(at)dt.
\]

Then `ell_a(r)=Gamma_1 f_r/Gamma_0 f_r`, and Green's identity factors the complete kernel automatically.

The exact theta dilation law from PR #202,

\[
 (X\partial_X-R\partial_R)a_X(R)=\frac12a_X(R),
\]

is the natural transmutation equation for this boundary system. The Gamma--Beta Dirichlet form of `L-91107` supplies a probabilistic candidate for the same bulk after the BPY change of variables.

No such exact boundary identification is asserted here.
