# M-20204 — Transcendental-pinned endpoint-filter attack

Claim ID: `M-20204`  
Title: Combine optimal `O(N^-2)` prime conditioning with exact off-line pole exposure  
Status: **PROPOSED RESEARCH PROGRAM**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20206`; `L-20211`; `L-20213`; PR #219 prime polygon; PR #216 terminal-prime energy  
Scope: one fixed large degree followed by a cofinal scale proof

## 1. Fix degree before the cofinal argument

Choose one large integer `N`. Do not vary `N` inside the Landau limit. Define

\[
 \widetilde P_N=P_N+e^{-N}(1-\cos x),
\]

where `P_N` is the sharp algebraic endpoint Fejer filter.

For this one fixed filter:

- `T-20206` gives an uncancellable pole at every hypothetical off-line zero;
- the half-knot debt is `pi^2/(4N^2)+O(N^-3)`;
- the pin affects only prime powers `q<=n^(2/N)` at the critical sample `t_n=2log(n)/N`;
- the complete algebraic filter reaches `q<=n^2`.

Thus `N` may be chosen after a proof-level arithmetic estimate specifies how
small the fixed old-prefix debt must be. Once chosen, the full argument is
cofinal only in `n`.

## 2. Separate ledgers

Maintain two exact source ledgers:

### Algebraic bulk

\[
 \mathcal E_N^{(0)}(t)
 =\sum_{k=1}^{N}\lambda_{N,k}^{(0)}\Psi(kt).
\]

Its prime ramp is the explicit interpolation of the algebraic
autocorrelations `d_m^(N)`.

### Transcendental exposure pin

\[
 e^{-N}\Psi(t).
\]

Its prime, pole, gamma, and Lerch contributions are scalar and are supported on
the smallest dilation only. The final analytic proof retains the coefficient
symbolically; numerical production uses a directed interval additionally bound
to the symbolic `exp(-N)` declaration.

## 3. Center the bulk

Before any absolute value or operator norm, combine:

1. the terminal prime band;
2. the polar main term;
3. the exact gamma/Lerch correction.

Use either:

- `L-20705` centered prime convolution;
- PR #216's prime-pair `H^2` energy;
- PR #219's convex polygon margin.

The algebraic filter and the scalar polygon replay must consume the same
complete prime-power manifest.

## 4. Proof targets

Any one of the following closes RH for the chosen fixed `N`:

### Eventual sign

\[
 \mathcal E_N(2\log n/N)\ge0
 \quad(n\ge n_0).
\]

### Subpower negative part

\[
 \left(-\mathcal E_N(2\log n/N)\right)_+=n^{o(1)}.
\]

### Real-axis measure

Prove the associated pinned logarithmic-derivative ratio is completely monotone
by an explicit positive measure or Stieltjes continued fraction.

### Centered energy

Prove that the positive prime-pair/terminal energy dominates the exact
`O(N^-2)` endpoint debt and the exponentially smaller pin ledger.

## 5. Why the pin is proof-efficient

The pin is not a numerical regularizer. Its two roles are deliberately
separated:

- one transcendental coefficient proves that a pole residue cannot cancel
  against any finite algebraic combination of integer zero multiplicities;
- its arithmetic effect is exponentially small in `N` and confined to the old
  prefix `q<=n^(2/N)`.

A decimal approximation to `e^-N` may be used to enclose a finite value, but the
pole proof must bind the exact symbolic constant and Lindemann--Weierstrass.

## 6. Adversarial obligations

1. independently reconstruct the scaled-logarithmic-derivative residue factor
   `k^2`;
2. verify algebraicity of every endpoint-filter coefficient;
3. check that no other occurrence of `e^-N` enters a descendant coefficient;
4. audit Landau continuation for one fixed `N`;
5. retain the complete small-prime prefix rather than treating the pin as zero;
6. prove a genuine cofinal bound rather than extrapolating finite positivity.

No sign estimate is supplied by this methodology. Its contribution is to remove
the former incompatibility between optimal conditioning and rigorous false-RH
exposure.
