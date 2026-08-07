# R-15402 — A residue-free Hardy reflection closure is false

Claim ID: `R-15402`  
Title: Reflection/Selberg bulk algebra cannot bound the Hardy norm unless every crossed pole is retained  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15415`, `L-15416`, `T-15407`; elementary contour deformation  
Scope: the proposed uniform Hardy--reflection defect bound in Issue #180  
Related counterexample candidates: none

## Refuted shortcut

A tempting continuation of `L-15415` is:

```text
1. replace the positive Hardy modulus by the reflected two-line product;
2. linearize that product into the von Mangoldt derivative, the positive
   Selberg stream, and the archimedean term;
3. move the reflected line back to the original line;
4. bound only the linear bulk and conclude the Hardy norm is bounded.
```

Step 3 is invalid unless the contour ledger includes every zero crossed between
the two lines. The missing residues are not a lower-order error. They are the
entire unstable Hardy component isolated by `T-15407`.

## Exact rational model

Fix `a>0` and consider the real odd meromorphic function

\[
 f_a(z)=\frac1{z-a}+\frac1{z+a}
       =\frac{2z}{z^2-a^2}.
 \tag{R-15402.1}
\]

It satisfies the same formal symmetries as the centered completed logarithmic
derivative:

\[
 f_a(-z)=-f_a(z),
 \qquad
 f_a(\bar z)=\overline{f_a(z)}.
 \tag{R-15402.2}
\]

Therefore, for `z=sigma+it`,

\[
 \boxed{|f_a(z)|^2=-f_a(z)f_a(-\bar z).}
 \tag{R-15402.3}
\]

The reflection identity is exact. Nevertheless, the Hardy integral is infinite
on `sigma=a`, and as `sigma downarrow a` from the right its principal part is

\[
 \boxed{
 \frac{\sigma}{2\pi}
 \int_{\mathbb R}|f_a(\sigma+it)|^2dt
 =\frac{\sigma}{2(\sigma-a)}+O(1).}
 \tag{R-15402.4}
\]

Moving the reflected line from `-sigma` to `+sigma` crosses the poles at
`-a` and `+a`. Omitting their residues would falsely turn a divergent positive
energy into a finite bulk expression.

The same model works with conjugate pole pairs and with any compact entire
filter nonzero at the pole.

## Exact zeta interpretation

For the filtered centered completed logarithmic derivative

\[
 f_h(z)=\Omega_h(z)\frac{\Xi'(z)}{\Xi(z)},
 \tag{R-15402.5}
\]

a zero

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad\delta>0,
 \]

produces residue

\[
 m_\rho\Omega_h(\delta+i\gamma)\ne0.
 \tag{R-15402.6}
\]

The exact Cauchy Gram of `T-15407` is the contour-residue contribution. It is
positive semidefinite and diverges at the pole line. Thus:

\[
 \boxed{
 \text{bounded linear Selberg bulk}
 \not\Longrightarrow
 \text{bounded Hardy energy}
 }
 \tag{R-15402.7}
\]

unless a separate theorem proves that the right-half-plane pole packet is empty.

## What remains valid

The following contributions survive unchanged:

1. `L-15415` exactly linearizes the **reflected bulk**;
2. the positive Selberg coefficients remain useful for a proof-producing replay;
3. `L-15416` exactly identifies the Hardy modulus with a same-height reflected
   product;
4. `T-15407` proves a uniform bound after subtracting the complete unstable
   principal-part packet;
5. a proof that the packet is empty would prove RH and the bounded mean square.

Only the residue-free final inference is refuted.

## Consequence for proof architecture

Every valid positive proof must do at least one of the following:

- prove Suzuki's `Theta_omega` is inner for every `omega>0`;
- prove the anti-causal Hankel/model-space component vanishes;
- prove the right-zero Cauchy Gram is absent;
- prove a contour identity whose residue term is nonnegative and simultaneously
  forced to zero by an independent arithmetic inequality;
- establish an equivalent cofinal localized-Weil lower floor.

Merely estimating the derivative, Selberg, and gamma streams on one safe
vertical line does not address the pole packet.

## Status boundary

This refutation does not say that the desired Hardy bound is false. It says that
a proposed proof which omits the pole ledger is logically incomplete. For the
Riemann zeta function, emptiness of that ledger is exactly the Riemann
hypothesis.
