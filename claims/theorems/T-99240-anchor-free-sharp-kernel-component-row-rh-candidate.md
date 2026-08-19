# T-99240 — Anchor-free SHARP-kernel common-parent component-row RH candidate

Claim ID: `T-99240`  
Status: **PROPOSED COMPLETE UNCONDITIONAL PROOF CANDIDATE — HOSTILE INDEPENDENT RECONSTRUCTION REQUIRED**  
Created: 2026-08-19  
Frozen parent: PR #636 at `387f775f95d5e21e01c3fb39d91acc5b67f62b02`  
RH status: **not established by publication**

## 1. Corrections accepted

This successor accepts the binding live corrections:

1. PR #635: the constant-deficit score endgame is not used;
2. PR #638: a second-order smooth Volterra density does not fix boundary modes;
3. PR #552: the historical `FRONTIER-CHAIN` positivity proof is not used.

The theorem uses only a fixed physical component row and its direct
reciprocal-zeta Mellin transform.

## 2. New source-to-row theorem

For every fixed `j>=2`, `L-99240` proves the exact positive factorization

\[
 Q_Y(j)=\int_1^Y(4\sqrt{Y/t}-3)\kappa_j(t)\frac{dt}{t},
 \qquad \kappa_j(t)>0.
\tag{T-99240.1}
\]

Finite Möbius Fubini gives

\[
 c_X(j)=\int_1^X\Psi(X/t)\kappa_j(t)\frac{dt}{t},
\tag{T-99240.2}
\]

where `Psi` is exactly the SHARP target signed state used by the compact
factor-67 Hall theorem.

The compact Hall flow supplies a positive target-exact residual and a
nonnegative current row bonus. Only the residual recurses. The positive
kernel source is endpoint-restricted under every same-index child. The
random-key construction of PR #636 therefore gives one finite one-owner
physical source whose output marginal is exactly (T-99240.2).

Hence

\[
 \boxed{c_X(j)\ge0\qquad(X\ge1,\ j\ge2).}
\tag{T-99240.3}
\]

This closes the exact source-to-row arrow that PR #636 left to the frozen
endpoint-frame identity, without invoking the rank-two inverse of PR #638.

## 3. Fixed-row analytic consumer

For fixed `j`, define

\[
 \mathcal C_j(s)=\int_1^\infty c_X(j)X^{-s-1}\,dX.
\]

For `Re(s)>1/2`, finite/absolute Fubini gives

\[
 \boxed{
 \mathcal C_j(s)
 =\frac{C_j}{s^2}
 +\frac{P_j(s+\frac12)}
        {s^2\zeta(s+\frac12)}.
 }
\tag{T-99240.4}
\]

The right side is analytic at every positive real `s`.

For every open-strip complex number `rho`,

\[
 P_j(\rho)
 =-\frac{\rho(\rho+1)}{1-\rho}j^{-\rho-1}
  +O_\rho(j^{-\Re\rho-2}),
\tag{T-99240.5}
\]

so a sufficiently large fixed row satisfies `P_j(rho)!=0`.

If `zeta(rho)=0` with `Re(rho)>1/2`, (T-99240.4) has a genuine nonreal pole at

\[
 s=\rho-\frac12,\qquad\Re s>0.
\]

Since `c_X(j)>=0`, Landau's theorem forces the Mellin transform's finite
abscissa of convergence to be a real singularity. But the explicit
continuation has no positive-real singularity. This contradiction excludes
every zero to the right of the critical line. The functional equation excludes
zeros to the left.

Thus the candidate concludes

\[
 \boxed{\mathrm{RH}.}
\]

## 4. Conclusion-producing DAG

```text
explicit SHARP kernel kappa_j>0
 -> exact Q_Y(j)=T*kappa_j
 -> exact full-row marginal c_X(j)=Psi*kappa_j
 -> compact target Hall + current-only row bonus
 -> residual-only causal random-key tree
 -> one positive source with marginal c_X(j)
 -> c_X(j)>=0 for every fixed row
 -> reciprocal-zeta Mellin transform
 -> large-j noncancellation
 -> Landau + functional equation
 -> RH candidate.
```

## 5. Scientific boundary

The new algebra and kernel positivity are unconditional. The candidate still
requires hostile reconstruction of the compact Hall/profile theorem and the
exact causal random-key tree at their frozen scopes. The score, capacity,
thinning, terminal, prime-square, and second-order Volterra interfaces are no
longer conclusion-producing.

```text
positive SHARP row kernel                   PROVED EXACT
full Möbius row factorization               PROVED EXACT
rank-two Volterra gate                      BYPASSED EXACTLY
compact Hall/profile                        FROZEN / RECONSTRUCT
causal common-parent tree                   FROZEN / RECONSTRUCT
fixed-row Mellin and noncancellation        PROPOSED EXACT / RECONSTRUCT
accepted proof of RH                        NO
Riemann Hypothesis                          UNPROVED PENDING REVIEW
```
