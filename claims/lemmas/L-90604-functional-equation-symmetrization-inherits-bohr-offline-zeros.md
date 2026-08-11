# L-90604 — Functional-equation symmetrization inherits the one-sided Bohr zeros off the critical line

Claim ID: `L-90604`  
Status: **PROPOSED COMPLETE STIRLING / HURWITZ TRANSFER THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-90603`; uniform Stirling asymptotics  
Scope: finite Brownian functional-equation symmetrizations

## 1. Setup

For one of the positive cutoff mixtures of `L-90603`, write

\[
 m_N(s)=A(s)D_N(s),
 \qquad
 A(s)=\pi^{-s/2}\Gamma(1+s/2),
 \tag{L-90604.1}
\]

and symmetrise:

\[
 \mathcal X_N(s)=m_N(s)+m_N(1-s).
 \tag{L-90604.2}
\]

Then `X_N(s)=X_N(1-s)` and `X_N` has the required real symmetry.

### Theorem

Fix `1/2<beta<1`. Under the top-mass hypothesis of `L-90603`, every sufficiently large `N` has infinitely many zeros `rho_j` of `mathcal X_N` satisfying

\[
 |\operatorname{Im}\rho_j|\to\infty,
 \qquad
 \operatorname{Re}\rho_j\to\beta.
 \tag{L-90604.3}
\]

In particular, the finite functional-equation symmetrization has infinitely many zeros off `Re s=1/2`.

No simplicity of the limiting or finite one-sided zeros is required.

## 2. One-sided vertical limit

By `L-90603` there is a completely multiplicative unimodular twist `chi` such that

\[
 B_{N,\chi}(\beta)=0,
 \tag{L-90604.4}
\]

where `B_(N,chi)` is a nonzero finite Dirichlet polynomial. Kronecker supplies a sequence `t_j->infinity` for which

\[
 \boxed{
 \frac{D_N(w+it_j)}{it_j}
 \longrightarrow B_{N,\chi}(w)
 }
 \tag{L-90604.5}
\]

locally uniformly in `w`.

Choose a closed disk `K` centered at `beta`, small enough that

\[
 \operatorname{Re}w\ge\frac12+\delta
 \qquad(w\in K)
 \tag{L-90604.6}
\]

for some `delta>0`, and whose boundary contains no zero of `B_(N,chi)`.

## 3. The reflected term vanishes after normalization

Define on `K`

\[
 \mathcal Y_j(w)
 =\frac{\mathcal X_N(w+it_j)}{it_jA(w+it_j)}.
 \tag{L-90604.7}
\]

The gamma factor has no zeros, so this normalization is analytic. Expanding,

\[
 \mathcal Y_j(w)
 =\frac{D_N(w+it_j)}{it_j}
 +\frac{A(1-w-it_j)}{A(w+it_j)}
  \frac{D_N(1-w-it_j)}{it_j}.
 \tag{L-90604.8}
\]

Because `D_N(s)=sB_N(s)+A_N(s)` with finite Dirichlet polynomials `A_N,B_N`,

\[
 \sup_{w\in K}
 \left|\frac{D_N(1-w-it_j)}{it_j}\right|
 \le C_{N,K}.
 \tag{L-90604.9}
\]

Uniform Stirling asymptotics give

\[
 \boxed{
 \sup_{w\in K}
 \left|\frac{A(1-w-it_j)}{A(w+it_j)}\right|
 \ll_K t_j^{1/2-\inf_{w\in K}\operatorname{Re}w}
 \le t_j^{-\delta+o(1)}.
 }
 \tag{L-90604.10}
\]

Indeed the powers in Stirling are

\[
 |A(w+it)|\asymp_K
 t^{1/2+\operatorname{Re}w/2}e^{-\pi t/4},
 \qquad
 |A(1-w-it)|\asymp_K
 t^{1-\operatorname{Re}w/2}e^{-\pi t/4}.
\]

Combining (L-90604.5), (L-90604.9), and (L-90604.10),

\[
 \boxed{
 \mathcal Y_j(w)\longrightarrow B_{N,\chi}(w)
 }
 \tag{L-90604.11}
\]

locally uniformly on `K`.

## 4. Hurwitz transfer

The limit is not identically zero and has a zero at `beta`. Hurwitz's theorem, or Rouché on the boundary of a sufficiently small zero-isolating disk, gives zeros `w_j` of `Y_j` with

\[
 w_j\longrightarrow\beta.
 \tag{L-90604.12}
\]

Therefore

\[
 \rho_j=w_j+it_j
 \tag{L-90604.13}
\]

are zeros of `mathcal X_N`, with

\[
 |\operatorname{Im}\rho_j|\to\infty,
 \qquad
 \operatorname{Re}\rho_j\to\beta>1/2.
\]

Choosing the Kronecker return sequence with increasing gaps makes these zeros distinct. This proves the theorem.

## 5. Interpretation

Functional-equation symmetrization cannot repair a one-sided high-frequency torus zero away from the central line. On `Re s>1/2`, Stirling makes the reflected term polynomially smaller after the natural `it A(s)` normalization:

\[
 |t|^{1/2-\operatorname{Re}s}.
\]

The entire symmetrized vertical limit is therefore the same one-sided twisted Dirichlet polynomial.

This phenomenon is independent of bounded-height scans, local-uniform convergence to xi, and multiplicity of the limiting zero.

## 6. Proof boundary

Proved here:

- direct locally uniform vertical-limit convergence for the symmetrized producer;
- infinitely many off-line zeros of each sufficiently large symmetrized positive cutoff mixture;
- no simplicity hypothesis.

Not proved:

- any claim about the true xi function;
- RH.
