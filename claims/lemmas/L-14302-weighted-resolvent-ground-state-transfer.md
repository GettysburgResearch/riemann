# L-14302 — Audited weighted Schur–Ritz ground-state transfer

Claim ID: L-14302  
Title: Parity-adapted weighted coercivity certifies a simple-even ground state and its prolate distance  
Status: PROPOSED  
Authoring agent: `gpt56-09`  
Auditing and repairing agent: `gpt56-pro-09-a`  
Reviewing agents: none independent yet  
Created: 2026-07-29  
Last updated: 2026-07-29  
Dependencies: finite-dimensional spectral theorem, Cauchy interlacing, Schur complement  
Scope: exact finite-dimensional improvement of the T-14301 target-distance and simple-even gates  
Related counterexample candidates: none

## Audit disposition

The first committed version contained a sound resolvent inequality but was not
proof-grade as written:

1. it defined `M` only on the finite complement and then applied `||.||_M` to
   ambient target tails, so two displayed projective distances were ill-typed;
2. if that notation were interpreted as a seminorm ignoring the target
   direction, the displayed infimum over nonzero scalars would be vacuous;
3. it assumed a simple ground eigenpair even though the proposed coercivity gate
   itself can certify globality, simplicity, and parity;
4. it said every finite predicate was rational-LDL checkable without introducing
   rational Loewner enclosures for the generally transcendental Hardy Gram;
5. it described the new bound as stronger without qualification. It can be
   arbitrarily sharper on residual-orthogonal high-weight modes, but its scalar
   coercivity constant can also absorb worst-case geometry.

The theorem below repairs all five points and strengthens the useful kernel. Git
history preserves the initial formulation.

## Statement

Let `K` be a real Hilbert space with ordinary inner product `⟨.,.⟩`. Let `H` be
a finite-dimensional subspace and `P:K -> H` its ordinary orthogonal
projection. Let

\[
 A:H\to H
\]

be self-adjoint. Suppose `Gamma` is a self-adjoint involution on `H`,
`A Gamma=Gamma A`, and

\[
 H=H_+\oplus H_-,
 \qquad H_\pm=\ker(\Gamma\mp I).
\]

Let `p in H_+` be nonzero and put

\[
 q=\|p\|,
 \qquad v=p/q,
 \qquad W_+=H_+\cap v^\perp.
 \tag{L-14302.1}
\]

Relative to

\[
 H=\operatorname{span}\{v\}\oplus W_+\oplus H_-,
\]

write

\[
 \mu=\langle Av,v\rangle,
 \qquad b=P_{W_+}Av,
 \qquad C_+=P_{W_+}A|_{W_+},
 \qquad C_-=P_{H_-}A|_{H_-}.
 \tag{L-14302.2}
\]

Let `||.||_mathfrakM` be a second Hilbert norm on a linear space containing `H`
and the target vectors used below. Assume it is invariant under `Gamma` on
`H`. On the finite space `W_+`, let `M_+` be the unique positive-definite
operator satisfying

\[
 \langle M_+w,w\rangle=\|w\|_{\mathfrak M}^2
 \qquad(w\in W_+).
 \tag{L-14302.3}
\]

An assertion on a zero-dimensional subspace is interpreted vacuously.

Suppose there are real numbers

\[
 U\geq\mu,
 \qquad h>0,
 \qquad g_->0
 \tag{L-14302.4}
\]

such that

\[
 C_+-UI\succeq hM_+,
 \qquad
 C_--UI\succeq g_-I.
 \tag{L-14302.5}
\]

Then the following conclusions hold.

### A. The gate itself certifies the global simple-even ground state

The lowest eigenvalue `lambda_0` of `A` is simple, satisfies

\[
 \lambda_0\leq\mu\leq U,
 \tag{L-14302.6}
\]

and has a normalized eigenvector

\[
 \xi_0=\alpha v+w,
 \qquad \alpha>0,
 \qquad w\in W_+.
 \tag{L-14302.7}
\]

In particular, `xi_0` is even. If additionally

\[
 M_+\succeq m_+I
 \qquad(m_+>0),
\]

then, whenever a next eigenvalue exists and with terms belonging to absent
subspaces omitted,

\[
 \lambda_1-\lambda_0
 \geq \min\{hm_+,g_-\}.
 \tag{L-14302.8}
\]

### B. Dual-weighted correction bound

The normalized ground line obeys

\[
 \boxed{
 \left\|\frac{w}{\alpha}\right\|_{\mathfrak M}
 \leq
 \frac{\|b\|_{M_+^{-1}}}{h}.}
 \tag{L-14302.9}
\]

Equivalently, with the normalization along `v` fixed rather than minimized away,

\[
 \boxed{
 \left\|\frac{\xi_0}{\langle\xi_0,v\rangle}-v\right\|_{\mathfrak M}
 \leq
 \frac{\|b\|_{M_+^{-1}}}{h}.}
 \tag{L-14302.10}
\]

This is the nonvacuous projective distance intended by the first formulation.

### C. Unnormalized target form

Let `k` belong to the domain of `||.||_mathfrakM` and assume

\[
 Pk=p.
 \tag{L-14302.11}
\]

Put

\[
 t=\|k-p\|_{\mathfrak M},
 \qquad
 r=P_{W_+}Ap=P_{W_+}(A-\mu I)p.
 \tag{L-14302.12}
\]

Then the explicit scalar `c=q/alpha` satisfies

\[
 \boxed{
 \|c\xi_0-k\|_{\mathfrak M}
 \leq
 t+\frac{\|r\|_{M_+^{-1}}}{h}.}
 \tag{L-14302.13}
\]

Hence

\[
 \inf_{c\ne0}\|c\xi_0-k\|_{\mathfrak M}
 \leq
 t+\frac{\|r\|_{M_+^{-1}}}{h}.
 \tag{L-14302.14}
\]

The projection norm `q` has disappeared because `r=qb`. This unnormalized form
is the natural exact certificate: a rational frozen projection vector need not
be divided by an irrational square root.

## Proof

### 1. Globality, simplicity, and parity

The compression of `A` to `v^perp` is block diagonal on `W_+ \oplus H_-`.
By (L-14302.5), every eigenvalue of that compression is strictly larger than
`U`. On the other hand, the Rayleigh principle gives

\[
 \lambda_0(A)\leq\langle Av,v\rangle=\mu\leq U.
\]

Cauchy interlacing for the codimension-one compression therefore gives

\[
 \lambda_1(A)\geq
 \lambda_{\min}(A|_{v^\perp})>U\geq\lambda_0(A).
\]

Thus the global ground eigenvalue is simple. Its eigenvector cannot be
orthogonal to `v`, because an eigenvector in `v^perp` with eigenvalue at most
`U` would contradict the compression bound. Since the simple ground line is
invariant under `Gamma`, its eigenvector has definite parity. An odd vector is
orthogonal to the even vector `v`, so the nonzero overlap forces even parity.
This proves (L-14302.6)--(L-14302.7).

If `M_+>=m_+I`, the even complement lies above `U+hm_+` and the odd sector lies
above `U+g_-`. Interlacing and `lambda_0<=U` give (L-14302.8).

### 2. Weighted resolvent estimate

The `W_+` component of `A xi_0=lambda_0 xi_0` is

\[
 (C_+-\lambda_0I)w=-\alpha b.
 \tag{L-14302.15}
\]

Because `lambda_0<=U`,

\[
 C_+-\lambda_0I\succeq C_+-UI\succeq hM_+.
\]

Set

\[
 T=M_+^{-1/2}(C_+-\lambda_0I)M_+^{-1/2}.
\]

Then `T>=hI`, so `||T^{-1}||<=1/h`, and (L-14302.15) yields

\[
 M_+^{1/2}\frac{w}{\alpha}
 =-T^{-1}M_+^{-1/2}b.
\]

Taking ordinary norms proves (L-14302.9), and (L-14302.10) is the same identity
with the `v` component normalized to one.

### 3. Ambient target

Choose `c=q/alpha`. Since `Pk=qv`,

\[
 c\xi_0-k=q\frac{w}{\alpha}-(k-p).
\]

The triangle inequality and `qb=P_{W_+}Ap=r` prove (L-14302.13), hence
(L-14302.14). QED.

## Rational Loewner certificate

The exact Hardy Gram generally contains transcendental quantities. Rational LDL
therefore applies only after directed rational Loewner enclosures are supplied.
The following interface is sufficient.

Let `A=A_0+E`, where `A_0` is rational symmetric,

\[
 \|E\|_{op}\leq\delta,
 \tag{L-14302.16}
\]

and the exact `A` is known independently to commute with `Gamma`. Let `B_+` and
`B_-` be rational full-column-rank bases of `W_+` and `H_-`, with ordinary Gram
matrices

\[
 S_+=B_+^TB_+,
 \qquad S_-=B_-^TB_-.
\]

Let `G_+` be the exact Hardy Gram on `B_+`, with entries

\[
 (G_+)_{ij}=\langle (B_+)_i,(B_+)_j\rangle_{\mathfrak M},
\]

and suppose rational matrices satisfy

\[
 0\prec\underline G_+\preceq G_+\preceq\overline G_+,
 \qquad
 \underline G_+\succeq mS_+
 \quad(m>0).
 \tag{L-14302.17}
\]

Put

\[
 s=p^Tp,
 \qquad
 \mu_0=\frac{p^TA_0p}{s},
 \qquad
 U=\mu_0+\delta.
 \tag{L-14302.18}
\]

It is sufficient to certify by exact rational LDL

\[
 B_+^T(A_0-UI)B_+-\delta S_+-h\overline G_+\succeq0,
 \tag{L-14302.19}
\]

and

\[
 B_-^T(A_0-UI)B_--\delta S_--g_-S_-\succeq0.
 \tag{L-14302.20}
\]

Indeed, the exact compression errors are bounded below by `-delta S_+` and
`-delta S_-`, while `lambda_0<=mu(A)<=U`.

For the dual residual put

\[
 d_0=B_+^TA_0p.
 \tag{L-14302.21}
\]

The coordinate identity behind the certificate is worth making explicit. If
`r in W_+`, `d=B_+^Tr`, and `G_+` is the weighted Gram above, then

\[
 \|r\|_{M_+^{-1}}^2=d^TG_+^{-1}d.
 \tag{L-14302.21a}
\]

Indeed, writing `r=B_+y` and `S_+=B_+^TB_+`, one has `d=S_+y`; the operator
representing the weighted form in these coordinates is `S_+^{-1}G_+`, and a
direct substitution gives (L-14302.21a).

A rational number `B_0>=0` satisfying

\[
 \begin{pmatrix}
 B_0^2&d_0^T\\
 d_0&\underline G_+
 \end{pmatrix}\succeq0
 \tag{L-14302.22}
\]

certifies `d_0^T \underline G_+^{-1}d_0\leq B_0^2`. If a rational `epsilon>=0`
satisfies

\[
 \epsilon^2m\geq\delta^2s,
 \tag{L-14302.23}
\]

then

\[
 \|B_+^TEp\|_{\underline G_+^{-1}}\leq\epsilon.
\]

To see this, `\underline G_+\succeq mS_+` implies

\[
 \|\underline G_+^{-1/2}B_+^T\|_{op}^2\leq m^{-1};
\]

combine this with `\|Ep\|\leq\delta\sqrt{s}`. Since
`G_+\succeq\underline G_+`, inversion reverses Loewner order, and the triangle
inequality in the `\underline G_+^{-1}` norm gives the exact unnormalized
residual bound below.

Since `G_+>=underline G_+`, the exact unnormalized residual in
(L-14302.12) obeys

\[
 \|r\|_{M_+^{-1}}\leq B_0+\epsilon.
 \tag{L-14302.24}
\]

Consequently the fully rational finite output is

\[
 \boxed{
 \inf_{c\ne0}\|c\xi_0-k\|_{\mathfrak M}
 \leq t+\frac{B_0+\epsilon}{h}.}
 \tag{L-14302.25}
\]

Every algebraic matrix decision in (L-14302.17), (L-14302.19),
(L-14302.20), and (L-14302.22) is now genuinely rational. Producing the directed
Loewner enclosures and the target-tail bound remains an analytic/provenance gate.

## Comparison with L-14301

The earlier gate uses an ordinary residual/gap estimate followed by the global
embedding factor

\[
 \kappa=\sup_{w\in W_+}\frac{\|w\|_{\mathfrak M}}{\|w\|}.
\]

L-14302 instead asks for weighted coercivity and the dual norm of the actual
unnormalized residual. Neither finite bound dominates the other without
additional structure. L-14302 can, however, be arbitrarily sharper when the
modes responsible for a large `kappa` are weakly coupled to `p`. Both bounds
should therefore be computed and the smaller certified endpoint retained.

## Adapter to T-14301

At level `j`, take

\[
 p_j=P_jk_{\lambda_j},
 \qquad
 t_j=\|(I-P_j)k_{\lambda_j}\|_{\lambda_j,\tau_j}.
\]

A passing L-14302 certificate gives

\[
 \boxed{
 d_j^+
 =t_j+\frac{B_j}{h_j},}
 \tag{L-14302.26}
\]

where `B_j` bounds the dual Hardy norm of the **unnormalized** projected-prolate
residual. It simultaneously proves that the corresponding finite Weil matrix
has a global simple even ground state. Gate 9 is therefore reduced to

\[
 t_j\to0,
 \qquad
 B_j/h_j\to0.
 \tag{L-14302.27}
\]

This is a cleaner target than the first formulation's `q_jB_j/h_j`, but it is
still a genuine asymptotic theorem, not a finite-prefix inference.

## Gap audit

- The ordinary projection `P` and the Hardy norm need not be mutually
  orthogonal. Only the triangle inequality is used.
- `B_+` must span the entire even complement and `B_-` the entire odd sector.
- Exact parity commutation is an analytic/formula-level fact; an unstructured
  operator ball around a parity-commuting midpoint does not prove it.
- `underline G_+` and `overline G_+` must be Loewner bounds, not merely
  entrywise interval endpoints.
- The scalar coercivity `h` may be small. The new route is not automatically
  stronger than L-14301.
- The CCM normalization import still requires independent review; projective
  rescaling is used only because nonzero scalar multiplication preserves zeros.

## Adversarial tests

1. **Vacuous-infimum trap.** Interpreting `M` as a seminorm that ignores the
   `v` component makes `inf_{c!=0}||c xi-v||_M=0`; the repaired statement fixes
   the `v` normalization explicitly.
2. **Lower-endpoint trap.** Replacing the upper Rayleigh endpoint `U` by a
   lower eigenvalue endpoint reverses the needed monotonicity.
3. **High-weight uncoupled mode.** Let `M=diag(1,K^2)`,
   `C-U I=hM`, and `b=(epsilon,0)`. The old `kappa` penalty grows like `K`,
   while the dual residual bound is independent of `K`.
4. **No-universal-dominance case.** If only an ordinary complement gap is
   available, converting it to weighted coercivity can force `h` down by
   `kappa^{-2}`; L-14302 may then be worse.
5. **Parity omission.** Weighted coercivity only on the even complement does
   not exclude a lower odd state; the odd gate in (L-14302.5) is indispensable.
6. **Gram enclosure direction.** Coercivity uses `overline G`, while the dual
   residual uses `underline G`. Reversing either direction is unsafe.

## Remaining uncertainty

The finite theorem and rational adapter are complete-looking but remain
`PROPOSED` pending an independent reconstruction. No production CCM matrix,
Hardy Gram enclosure, or prolate tail has yet passed this certificate. The
large-parameter estimates in (L-14302.27) remain the central analytic blocker.

## Suggested next attack

Construct the production `G_+` Loewner enclosure analytically in the CCM Fourier
basis. Then expand the unnormalized residual covector

\[
 d_j=B_{+,j}^TQW_{\lambda_j}p_j
\]

before norms are taken, keeping prime, pole, and archimedean contributions in one
shared interval expression. Search for cancellation in the lower-Gram dual norm
and compare the resulting `B_j/h_j` endpoint against the older
`kappa_jR_j/g_j` endpoint at the same finite levels.
