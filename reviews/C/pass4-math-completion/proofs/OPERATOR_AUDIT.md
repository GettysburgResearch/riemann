# C4-O: independent finite-window and energy-Schur reconstruction

Source: PR #792 at `465cb28ed8cbfa1bb071d9a85eeda9890decfe6b`.
Files: `finite-window-coercivity/PROOF.md` and `energy-schur-reduction/PROOF.md`
under `standalone/2026-09-05-bernstein-chebyshev-growth/` (SRC-O0, SRC-O1).
Status: the components reconstructed below are supported at their stated scope.
No actual effective-matrix sign, continuum numerical certificate, or all-length
positivity is proved. The original 581-control suite was not run.

The present successor to C is the former A, not the author of #792 in the
preceding C conversation. This is a fresh derivation of the named components,
not a reassignment-based acceptance of the entire branch. Earlier A reports
and our own #793 research receive no independent acceptance from this role change.

<a id="O1"></a>
## O1. Literal source and the two-sided tail

Set a=3/4, b=3/2, c=1/2, lambda_j=2j+1/2 and

\[
 C_b=(1-\gamma_E-\log(2\pi))/3,\qquad q_n=\Lambda(n)/\sqrt n.
\]

The source being reviewed is the **explicit arithmetic kernel**

\[
 W(x)=\tfrac12e^{c|x|}+C_be^{-b|x|}
 +\sum_{j\ge1}\frac{e^{-\lambda_j|x|}}{\lambda_j^2-b^2}
 -\frac1{2b}\sum_{n\ge2}q_n
       \left(e^{-b|x-\log n|}+e^{-b|x+\log n|}\right).
\tag{O1.1}
\]

For fixed L>0 the prime tail converges uniformly on [-L,L], since for
n>e^L its terms are bounded by constants depending on L times Lambda(n)/n^2.
The elementary bound Lambda(n)<=log n proves convergence. The gamma series
converges uniformly since its coefficients are O(j^-2). Thus W is continuous
and real even on the window; its integral operator is compact self-adjoint
by the Hilbert--Schmidt criterion, without needing the stronger parent global
trace-class theorem.

On H=L2(0,L), with inner products antilinear in the first argument, use

\[
 q(h,k)=b\int_0^L\overline{h(t)}\int_0^L W(t-u)k(u)du\,dt.
\]

This equals the original damped form when f=e^(at)h. That multiplication
is boundedly invertible on each fixed interval, preserving positivity and
negative index, but not eigenvalues.

For an integer X>=e^L let W_X retain all prime powers n<=X, all gamma terms,
and the other exact terms. Write tau_X=sum_(n>X) Lambda(n)/n^2. For |x|<=L,

\[
 W(x)-W_X(x)=-\frac{\tau_X}{b}\cosh(bx).
\]

Consequently

\[
 q(h,h)-q_X(h,h)=
 -\tau_X\left|\int\cosh(bt)h(t)dt\right|^2
 +\tau_X\left|\int\sinh(bt)h(t)dt\right|^2.
\tag{O1.2}
\]

This is an exact complete-tail formula. Suppressing the negative cosh term
without its constraint would be wrong. Only that constraint is needed for a
lower bound; suppressing the remaining positive sinh contribution is allowed.
The finite prime cutoff counts powers n, not merely prime bases p.

<a id="O2"></a>
## O2. Reconstruct the all-frequency coercivity bound

Impose the two moments against e^(ct) and e^(-ct). Define

\[
 \phi(t)=c^{-1}\int_0^t\sinh(c(t-u))h(u)du.
\]

Then phi is in H^2, h=phi''-c^2 phi, and both phi and phi' vanish at 0 and L.
The endpoint L equations follow explicitly by expanding sinh/cosh and using
the two imposed moments. The zero extension is in H^2(R), so
hhat(w)=-(w^2+c^2)phihat(w).

The growing exponential in W_X cannot be Fourier transformed as an ordinary
L1 kernel. Its convolution with this constrained h vanishes outside [0,L]
and satisfies (D^2-c^2)(e^(c|.|)*h)=2c h. The convolution is therefore 2c phi,
giving multiplier -2c/(w^2+c^2) on these tests. This is the necessary domain
argument for the otherwise invalid unrestricted transform of e^(c|x|).

The integrable exponential and gamma terms have their ordinary transforms.
Partial fractions give

\[
 q_X(h,h)=\frac b{2\pi}\int_{\mathbb R}
 \frac{V_X(w)}{b^2+w^2}|\widehat h(w)|^2dw,
\]

\[
 V_X(w)=\Omega(w)-2\sum_{n\le X}q_n\cos(w\log n),
 \qquad \Omega(w)=\Re\psi(1/4+iw/2)-\log\pi.
\tag{O2.1}
\]

For clarity, the archimedean constant in this normalization can be checked
without an unspecified Fourier convention. Multiplying its transform by
b^2+w^2 gives

\[
 -\frac{c(b^2+w^2)}{c^2+w^2}+2bC_b+
 \sum_{j\ge1}\frac{2\lambda_j(b^2+w^2)}
 { (\lambda_j^2-b^2)(\lambda_j^2+w^2)}.
\]

Subtract its value at zero. The growing term gives the k=0 summand below;
the jth term gives the k=j summand. At zero, the convergent remaining sum is

\[
 \sum_{j\ge1}\left(\frac1{2j-1}+\frac1{2j+2}
                        -\frac2{2j+1/2}\right)
 =\psi(1/4)+7/2+\gamma_E+\log2.
\]

Combining with -b^2/c=-9/2 and 2bC_b=1-gamma_E-log(2pi) gives
Omega(0)=psi(1/4)-log pi, exactly as required. The digamma partial-fraction,
shift, reflection and duplication identities are classical inputs, identified
in REFERENCES.md. Hence, with c_k=2k+1/2,

\[
 \Omega(w)-\Omega(0)=\sum_{k\ge0}\frac2{c_k}
                      \frac{w^2}{c_k^2+w^2},\qquad
 \Omega(0)=-\gamma_E-\pi/2-3\log2-\log\pi>-6.
\]

If qbar>=Q_X=sum_(n<=X) q_n and
S_m=sum_(k=0)^m 4/(4k+1)>=7+2qbar, put C_m=(m+1)(2m+1). Positivity of
all the retained digamma increments, the cosine upper bound 1, and
sum_(k=0)^m 2c_k=C_m imply, for **all** real w,

\[
 V_X(w)\ge1-C_m/(w^2+1/4).
\tag{O2.2}
\]

Substituting hhat and using exact polynomial division,

\[
 \frac{(x+1/4)^2-C(x+1/4)}{x+9/4}
 =x-(C+7/4)+\frac{4+2C}{x+9/4},
\]

gives q_X>=b(||phi'||^2-(C_m+7/4)||phi||^2). Remove phi's first K Dirichlet
sine coefficients with pi^2(K+1)^2/L^2>=2C_m+7/2. Poincare's inequality
then gives

\[
 q(h,h)\ge(b/2)||\phi'||^2+
 \tau_X\left|\int\sinh(bt)h(t)dt\right|^2.
\tag{O2.3}
\]

The positive space is the ordinary L2 orthogonal complement of
{e^(-ct),e^(ct),cosh(bt),sin(j pi t/L):1<=j<=K}. Integration by parts
equates the sine constraints on h and phi. These K+3 functions are linearly
independent, as their distinct exponential frequencies show, so the stated
codimension is exact in this formulation. Nonzero h has phi' nonzero.
The bound is a primitive-norm bound, not a uniform L2 spectral gap.

### Independent rational constants at L=1

The new checker reconstructs log bounds with the positive atanh series and
its explicit geometric remainder, and sqrt(2)>707/500, sqrt(3)>433/250.
It proves Q_3<9/8, S_152>37/4, S_92>35/4, and the needed rational comparisons.
No saved upstream JSON or floating-point special-function value is used.
The strict pi>3 and pi<22/7 are classical bounds (the checker additionally
supplies a rational Machin arctangent enclosure).

For the improved constant, gamma_E<H_32-5 log2<3/5 and log pi<6/5 give
Omega(0)>-383/70>-11/2. Replacing m=152 by 92 in the bound, while keeping
the same removed 101 modes, yields

\[
 q(h,h)\ge\frac32\left(1-\frac{17205+7/4}{93636}\right)||\phi'||^2
 \ge\frac65||\phi'||^2.
\tag{O2.4}
\]

This reconstructs the stronger constant on the **same** positive subspace.
It does not certify the sign on its 104-dimensional complement.

<a id="O3"></a>
## O3. The source really has the regularity needed for the coupling

On [0,L], rewrite the prime part using the safe complete constant
P2=sum_(n>=2) Lambda(n)/n^2. Then

\[
 W(x)=e^{x/2}/2+C_be^{-bx}+S_\Gamma(x)-(P2/b)\cosh(bx)
       +b^{-1}\sum_{2\le n\le e^x}q_n\sinh(b(x-\log n)).
\]

There are finitely many prime-power knots, and each displayed knot term is
continuous and piecewise C1. The gamma series is decreasing and positive,
with

\[
 S_\Gamma(0)=1/6+(\log2)/3<2/5,
 \quad\int_0^L |S_\Gamma'(x)|dx=S_\Gamma(0)-S_\Gamma(L).
\]

The equality follows by Tonelli applied to the nonnegative negative derivatives
of the exponential terms; integrating their sum recovers the uniformly
convergent series. It establishes absolute continuity including the logarithmic
derivative singularity at zero. Even extension thus gives W in W^(1,1)(-L,L).
No bounded second derivative is required or asserted.

For K_z(t)=int_0^L W(t-u)z(u)du, Young's inequality and weak differentiation
on the window give K_z in H1, with ||K_z||_2<=||W||_1||z||_2 and
||K_z'||_2<=||W'||_1||z||_2. One may extend W absolutely continuously outside
the window before taking local derivatives. Differentiating a hard-truncated
kernel and then forgetting its artificial endpoint deltas would not be valid.

Define

\[
 F_z=-K_z'+c^2\int_0^t K_z(s)ds.
\]

For the clamped primitive of v in the positive space V, two integrations by
parts, each with its actual zero boundary term, give

\[
 q(v,z)=b\langle\phi_v',F_z\rangle
       =b\langle\phi_v',\Pi F_z\rangle.
\tag{O3.1}
\]

Here Pi projects off {1,cos(j pi t/L),sinh(bt)}. Orthogonality follows from
the endpoints, the sine constraints, and
int cosh(bt)v=(b^2-c^2)int cosh(bt)phi_v=0. Therefore, if q(v,v)>=kappa
||phi_v'||^2,

\[
 |q(v,z)|\le\frac b{\sqrt\kappa}||\Pi F_z||_2\sqrt{q(v,v)}.
\tag{O3.2}
\]

This is the actual source-dependent range/continuity condition, not a formal
inverse assumption. The constants squared are b^2/kappa=3 generally and 15/8
for the specified L=1 subspace.

<a id="O4"></a>
## O4. Complete the positive space before eliminating it

Let V_q be the completion of V in the q norm and E its finite ordinary L2
complement. By (O3.2), each functional q(.,e), e in E, has a unique Riesz
representative g_e in V_q. No claim that g_e lies in L2 is needed. Define
S_ij=q(e_i,e_j)-q(g_ei,g_ej) in a fixed basis of E. Then

\[
 q(v+e_u,v+e_u)=||v+g_u||_q^2+u^*Su.
\tag{O4.1}
\]

The infimum over v in V is u*Su because V is dense in V_q. Hence the full
window is nonnegative exactly when S is. Every negative subspace injects
into E and has S-negative image by (O4.1). Conversely approximate the finitely
many g_e on a negative eigenspace of S; approximation is uniform on its
finite-dimensional unit sphere and preserves its strict negative gap. This
proves equality of negative indices. It does **not** prove equality of nullities.

For nested finite V_m dense in V, the finite solutions v_i,m are q-orthogonal
projections of g_ei. Consequently

\[
 S_m-S=[q(g_{e_i}-v_{i,m},g_{e_j}-v_{j,m})]\succeq0,
 \quad S_{m+1}\preceq S_m,\quad S_m\longrightarrow S.
\]

These are upper bounds. A negative finite section detects a negative full
form; a positive finite section need not establish any lower bound.

For arbitrary exact trials v_i in V put z_i=e_i-v_i,
U_ij=q(z_i,z_j), and R_ij=<Pi F_zi,Pi F_zj>. The same Riesz calculation gives

\[
 \boxed{U-(b^2/\kappa)R\preceq S\preceq U.}
\tag{O4.2}
\]

For operator-norm numerical errors eta_U and eta_R the safe lower matrix is
U_tilde-(b^2/kappa)R_tilde-(eta_U+(b^2/kappa)eta_R)I. The error must bound
full continuum matrices and exact constraints, not just sampled arrays.
No such arithmetic matrix certificate is generated here.

### Exact countercontrols and limits of the result

With A=diag(4^-j), coupling b_j=4^-j, j>=1, the energy representative is the
constant sequence 1, not an L2 vector. The effective scalar is C-1/3 and
S_M-S=4^-M/3. At C=1/3 the original L2 form has zero kernel although the
effective scalar vanishes. At C=1/4, S_1=0 but S=-1/12<0. If instead
b_j=2^-j, the finite variational minima are C-M, so the effective infimum
is minus infinity despite positivity on a codimension-one subspace.
These models are reproduced exactly in the new checker. They concern scope,
not actual xi zeros or signs of the arithmetic source.

## Disposition

The exact full-source tail, finite-window frequency bound, primitive coercivity,
W^(1,1) coupling, energy completion, negative-index identity, upper Galerkin
direction and residual lower enclosure survive this reconstruction. The fixed
L=1 constants are freshly checked with rational arithmetic. The operator is
not proved nonnegative on a full interval, still less on every large interval.

The terminal identification of this explicit kernel with the earlier global
xi/Weil construction and the trace identity driving the coefficient criterion
remain separate predecessor inputs, not newly reviewed here. The original
sampled lower eigenvalues are not outward continuum certificates. Accepting
these component proofs does not clear that numerical or all-length sign gate.
