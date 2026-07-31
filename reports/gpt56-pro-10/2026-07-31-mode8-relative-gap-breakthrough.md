# Mode-8 relative-gap breakthrough on the positive RH path

Agent: `gpt56-pro-10`  
Date: 2026-07-31  
Issue: #151  
Branch: `agent/gpt56-pro-10/151-radical-hermite-bridge`  
Status: exact prolate theorem and abstract Weil transfer; **RH not proved**

## Objective

The positive route had been reduced to the dimensionless condition

\[
 \frac{B_{\lambda,N,\tau}}{h_{\lambda,N,\tau}}\longrightarrow0,
\]

where `B` is the scalar-free Hardy-dual residual of the prescribed target and
`h` is the weighted coercivity of its complete even complement.

The working hypothesis was

\[
 B\lesssim d_4,
 \qquad h\gtrsim d_8,
 \qquad d_4/d_8\to0,
\]

with `d_n=1-chi_n` the fixed-mode prolate concentration defects and mode `8`
the first new positive Fourier-prolate mode after the target packet `0/4`.

This pass proves the corresponding **exact constrained prolate theorem**, but
also corrects the denominator scale:

\[
 h_{\rm pro}\asymp d_8/\lambda,
\]

not `d_8`.  The lost factor is forced by the zero-integral constraint.  The
fixed-mode asymptotics still leave seven powers of polynomial decay:

\[
 B_{\rm pro}/h_{\rm pro}=O(\lambda^{-7}).
\]

The unresolved step is now an explicitly formulated relative trace-form
comparison from the prolate model to the actual localized Weil/Hardy geometry.

## 1. Exact constrained target geometry

On the real-even source space `L2([-lambda,lambda])`, let

\[
 F_\lambda=P_\lambda\mathcal FP_\lambda,
 \qquad D_\lambda=I-F_\lambda,
\]

and choose the signed prolate eigenbasis

\[
 F_\lambda e_n=\chi_ne_n.
\]

The modes `0,4,8,...` have positive signed eigenvalues approaching `+1`; put

\[
 d_n=1-\chi_n.
\]

Let

\[
 \ell(f)=\int_{-\lambda}^{\lambda}f(x)\,dx,
 \qquad a_n=\ell(e_n)=\chi_ne_n(0).
\]

With

\[
 A^2=a_0^2+a_4^2,
\]

define

\[
 t=\frac{a_4e_0-a_0e_4}{A},
 \qquad
 u=\frac{a_0e_0+a_4e_4}{A}.
\]

Then `ell(t)=0`, `ell(u)=A`, and `t` is exactly the zero-integral `0/4`
prolate target used by CCM.

The complete constrained target complement is

\[
 S_\lambda=\ker\ell\cap t^\perp.
\]

No finite sampling or assumed mode expansion enters this definition.

## 2. Why the floor is `d8/lambda`

The Riesz vector of `ell` is the constant function

\[
 g=1_{[-\lambda,\lambda]},
 \qquad\|g\|^2=2\lambda.
\]

Since `g perp t`, decompose

\[
 g=Au+g_K,
 \qquad g_K\in\{e_0,e_4\}^\perp,
 \qquad\|g_K\|^2=2\lambda-A^2.
\]

Every `x in S_lambda` has the form `x=alpha u+y`, with
`y perp {e_0,e_4}`.  The integral constraint gives

\[
 \alpha A+\langle g_K,y\rangle=0.
\]

Cauchy--Schwarz therefore forces

\[
 \|y\|^2\ge\frac{A^2}{2\lambda}\|x\|^2.
\]

Since the next positive signed prolate mode is `8`, the standard eigenvalue
ordering gives

\[
 D_\lambda\succeq d_8I
 \quad\hbox{on }\{e_0,e_4\}^\perp.
\]

Hence

\[
 \boxed{
 \langle D_\lambda x,x\rangle
 \ge d_8\frac{A^2}{2\lambda}\|x\|^2.}
\]

The target Rayleigh value is

\[
 \mu_t=\frac{a_4^2d_0+a_0^2d_4}{A^2},
\]

so the centered constrained floor is

\[
 \boxed{
 g_{\rm pro,\lambda}
 =d_8\frac{A^2}{2\lambda}-\mu_t.}
\]

This is an exact complete-complement inequality.  The factor `1/lambda` is not
a proof artifact: it records the fact that the integral functional has norm
`sqrt(2lambda)` and can be cancelled by a small high-mode component spread over
a long interval.

## 3. Exact target residual

Inside the low `0/4` plane,

\[
 D_\lambda t
 =\mu_t t
  +\frac{a_0a_4}{A^2}(d_0-d_4)u.
\]

Projecting `u` onto `S_lambda` gives

\[
 \|P_{S_\lambda}u\|^2
 =1-\frac{A^2}{2\lambda}.
\]

Therefore

\[
 \boxed{
 B_{\rm pro,\lambda}
 :=\|P_{S_\lambda}(D_\lambda-\mu_tI)t\|
 =\frac{|a_0a_4|}{A^2}(d_4-d_0)
  \sqrt{1-\frac{A^2}{2\lambda}}.}
\]

Thus the numerator really is target-defect scale `d4`, with no hidden
mode-8 term.

## 4. Fixed-index asymptotic and exact decay

Fuchs's fixed-index finite-Fourier asymptotic, translated to the CCM parameter
`gamma=2*pi*lambda^2`, is

\[
 d_n(\lambda)
 \sim
 \frac{2^{4n+1}\sqrt2\,\pi^{n+1}}{n!}
 \lambda^{2n+1}e^{-4\pi\lambda^2}.
\]

For `n=4`, this reproduces CCM's printed coefficient

\[
 d_4(\lambda)
 \sim\frac{2^{14}}3\sqrt2\,\pi^5
 \lambda^9e^{-4\pi\lambda^2}.
\]

The ratio is therefore

\[
 \boxed{
 \frac{d_4}{d_8}
 \sim\frac{105}{4096\pi^4}\lambda^{-8}.}
\]

The fixed-mode Hermite limits give

\[
 a_0\to2^{1/4},
 \qquad a_4\to\frac{\sqrt3}{2^{5/4}},
 \qquad A^2\to\frac{11}{2^{5/2}}.
\]

Since `mu_t=O(d4)=o(d8/lambda)`, the exact formulas yield

\[
 \boxed{
 \frac{B_{\rm pro,\lambda}}{g_{\rm pro,\lambda}}
 \le
 \left(
  \frac{105\sqrt3}{15488\pi^4}+o(1)
 \right)\lambda^{-7}
 \longrightarrow0.}
\]

This proves the central mode-8 hypothesis in the pure prolate geometry and
quantifies the available transfer budget.

## 5. Seven powers of transfer slack

Let `J_lambda` transport the prolate target and constrained packet into the
localized Weil Hilbert space.  `L-15111` proves that it is enough to have:

\[
 m_-\|x\|^2\le\|Jx\|_M^2\le m_+\|x\|^2,
\]

\[
 B_{\rm Weil}
 \le C_BB_{\rm pro}+\varepsilon_B,
\]

and

\[
 q(Jx,Jx)-U\|Jx\|^2
 \ge C_H\langle(D-\mu_tI)x,x\rangle
     -\varepsilon_H\|x\|^2.
\]

After the complete radical-like, evaluation-visible, and infinite-complement
blocks have been included in one exact Schur correction,

\[
 h_{\rm Weil}
 \ge\frac{C_Hg_{\rm pro}-\varepsilon_H}{m_+}
\]

and

\[
 \frac{B_{\rm Weil}}{h_{\rm Weil}}
 \le
 \frac{m_+(C_BB_{\rm pro}+\varepsilon_B)}
      {C_Hg_{\rm pro}-\varepsilon_H}.
\]

Therefore any polynomial transfer loss

\[
 \frac{m_+C_B}{C_H}=O(\lambda^r),
 \qquad r<7,
\]

is harmless, provided the additive errors are lower order on the
`d8/lambda` scale.

## 6. Exact remaining relative trace theorem

A stronger, directly auditable sufficient comparison is

\[
 \left|
 q_\lambda(Jx,Jy)
 -\beta_\lambda\langle Jx,Jy\rangle
 -\kappa_\lambda\langle D_\lambda x,y\rangle
 \right|
 \le\delta_\lambda\|x\|\|y\|
\]

on the correctly decomposed target/constrained packet, with

\[
 \boxed{
 \delta_\lambda=o(d_8(\lambda)/\lambda).}
\]

This is the true literature-level bridge.  Connes--Consani's archimedean trace
formula expresses a Weil/trace discrepancy through prolate functions, but the
currently imported statement does not yet provide this uniform semilocal
operator estimate.

The theorem is not expected on the whole Hilbert space.  It must be applied
after the low space is decomposed as

```text
radical-like zero-evaluation near-kernel
+ evaluation-visible finite block
+ residual constrained prolate packet,
```

with the infinite complement controlled by the leverage floor and all cross
maps charged by block Temple--Schur.

## 7. Why the radical cluster changes the interpretation

`L-15106` proves that localizations of the infinite-dimensional global Weil
radical generate arbitrarily long near-zero Ritz clusters.  Consequently,
mode `8` cannot be called the next actual Weil eigenvector after one target.
It is the next direction in the **information-theoretic prolate quotient**.

PR #157 adds a second obstruction: a generic evaluation-visible low direction
cannot be approximated by small-tail exact radicals because every exact radical
transform vanishes at certified zeta zeros.  Those visible directions require
direct finite certification.

The valid architecture is therefore block-valued.  This does not weaken the
mode-8 result; it tells us exactly where the relative comparison must be
inserted.

## 8. Exact finite checker

`X-15104` uses only Python integers and `fractions.Fraction`.  The retained
four-mode synthetic certificate proves exactly:

```text
target Rayleigh                  53/12500
raw mode-next floor              1/2
centered mode-next floor         6197/12500
projected residual squared       729/78125000
Fuchs 4-to-8 rational factor     105/4096
final rational factor            105/15488 times sqrt(3)/pi^4
```

Proof-object SHA-256:

```text
c340fccc1c9c746369695831e4cd62574ff7cdb3c985c0695130773400b93d9b
```

Ten adversarial tests pass.  They reject target drift, incomplete complements,
false floors, false residuals, malformed defect ordering, Boolean indices, and
incorrect Fuchs constants or exponents.

The checker validates finite algebra only.  It does not evaluate a prolate
function, the localized Weil form, the Hardy metric, or zeta.

## 9. Theorem stack added

```text
L-15110  exact constrained mode-8 prolate floor and residual
L-15111  abstract relative Weil--prolate transfer
T-15105  mode-8 transfer criterion implying RH
X-15104  exact rational finite-algebra checker
```

## 10. Current status

### Closed

- the mode-8 identity inside the complete zero-integral constrained prolate
  complement;
- the exact target residual;
- the correct `d8/lambda` denominator scale;
- the fixed-index `lambda^-8` defect ratio;
- the resulting `lambda^-7` dimensionless ratio;
- the abstract transfer bookkeeping to the Weil/Hardy geometry.

### Open

- the packet-aware relative trace-form comparison on the `d8/lambda` scale;
- a proof-grade radical-like/evaluation-visible packet decomposition at
  production levels;
- direct cofinal positivity of the evaluation-visible block;
- the block-Schur cross-map budget;
- a cofinal finite sequence satisfying every gate.

### RH status

The Riemann hypothesis is **not proved**.  The main proposed asymptotic model has
now been established in the prolate geometry and reduced to one explicit
arithmetic transfer theorem.
