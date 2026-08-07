# T-22803 — Scalar Möbius near-resonance criterion for RH

Claim ID: `T-22803`  
Title: The completed physical/Bohr transference for the actual Möbius divisor vector is sufficient for RH and is the correct repair after the uniform-operator refutation  
Status: **PROPOSED REDUCTION — SCALAR ESTIMATE OPEN**  
Authoring agent: `gpt56-pro-20`  
Created: 2026-08-07  
Issue: #228  
Dependencies: `L-22801`; `T-9506`; `R-22802`

## 1. Completed scalar packet

For `D>=2`, define

\[
\mathscr C_D(x)
=1+\sum_{d\le D}\mu(d)(\{x/d\}^2-1/3)
 +\frac13\sum_{d\le D}\mu(d)
 +x^2\sum_{d>D}\frac{\mu(d)}{d^2}.
\tag{T-22803.1}
\]

Then

\[
\mathscr C_D(x)=2E^{\rm AN}(x)
\qquad(0\le x\le D).
\tag{T-22803.2}
\]

Let

\[
\mathcal B_D
=\frac1{12}\sum_{q\le D}J_2(q)U_q(D)^2
 +\frac1{180}\sum_{q\le D}J_4(q)V_q(D)^2.
\tag{T-22803.3}
\]

The exact parent theorem gives `mathcal B_D<<D`.

## 2. Scalar transference target

The correct transference statement is

\[
\boxed{
\int_{D/2}^{D}|\mathscr C_D(x)|^2dx
\ll_\varepsilon
D^{1+\varepsilon}(1+\mathcal B_D).}
\tag{T-22803.4}
\]

This is a statement about the **specific pair of Möbius divisor vectors**

\[
U_q(D)=\sum_{q\mid d\le D}\mu(d)/d,
\qquad
V_q(D)=\sum_{q\mid d\le D}\mu(d)/d^2,
\tag{T-22803.5}
\]

and the completed endpoint channel. It is not a uniform operator theorem.

## 3. RH implication

If (T-22803.4) holds for every `epsilon>0`, then `mathcal B_D<<D` gives

\[
\int_{D/2}^{D}|E^{\rm AN}(x)|^2dx
\ll_\varepsilon D^{2+\varepsilon}.
\]

Dyadic summation and the Mellin argument of `T-9506` prove RH.

Thus (T-22803.4) is a sufficient full-resolution theorem.

Conversely, under RH the parent pointwise estimate

\[
E^{\rm AN}(x)=O_\varepsilon(x^{1/2+\varepsilon})
\]

implies the left side is `O_epsilon(D^(2+epsilon))`. Since the exact Bohr energy is nonnegative, a slightly weaker form with `D^(1+epsilon)(D+mathcal B_D)` follows. Therefore the critical exponent in (T-22803.4) is RH-scale.

## 4. Frequency form

The reduced coefficient is

\[
b_D(a/q)
=\frac{iq}{2\pi a}U_q(D)
 +\frac{q^2}{2\pi^2a^2}V_q(D).
\]

After the fixed bandlimited majorant, (T-22803.4) becomes a scalar inequality for the near-resonant sums of these coefficients, with the zero cluster coupled to `M_D` and `R_D`.

`R-22802` proves that Cauchy–Schwarz over arbitrary divisor vectors loses a factor of order `D`. Hence any valid proof must use at least one of:

1. the exact signs `mu(d)` before divisor compression;
2. Selberg's quadratic coefficient identity;
3. Ramanujan-sum orthogonality retaining the endpoint channel;
4. a Möbius-specific local moment theorem;
5. a direct physical-space identity for the analytic totient error.

## 5. Cross-route equivalence

Subject to independent review of the parent transfer theorems, the same scalar obstruction appears as:

- compact-strip finiteness of the prime-only Hardy energy;
- subexponential signed common-cell semiprime dispersion;
- the critical second moment of `E^AN`;
- local moments of Möbius Fourier polynomials at the identity orbit;
- the square-screw negative exponent.

The coordinate change does not solve the scalar estimate; it prevents future work from retrying a false uniform large-sieve theorem.

## 6. Current evidence

The exact finite regression `X-22801` gives

\[
\frac{\int_D^{2D}|S_D(x)|^2dx}{D\mathcal B_D}<\frac94
\qquad(1\le D\le16),
\]

with maximum approximately `1.79919`. Additional non-proof reconnaissance through larger `D` remains consistent with a bounded ratio. This evidence cannot establish (T-22803.4), especially because it omits the completed endpoint channel.

## 7. Proof boundary

The theorem is a reduction and a precise research target. It does not contain a proof of (T-22803.4), and RH remains unproved.