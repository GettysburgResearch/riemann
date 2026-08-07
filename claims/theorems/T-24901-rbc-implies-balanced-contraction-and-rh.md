# T-24901 — `RBC(K)` implies balanced contraction and RH

Claim ID: `T-24901`  
Title: Uniform reflected boundary-charge certificates with bounded paid defect force the common rightmost-zero exponent to vanish  
Status: **PROPOSED COMPLETE CONDITIONAL THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #249  
Dependencies: `D-24901`, `L-24901`--`L-24904`; PR #158 scale contraction; `L-23008/T-23003` fixed-ratio shell transfer  
Scope: full Riemann Hypothesis conditional on an unbounded `RBC(K)` family

## 1. Assumptions

Assume there is an unbounded sequence of integers `K` for which `RBC(K)` holds
with constants

\[
\delta>0,\qquad \kappa_0>0,\qquad C_{\rm ref}<\infty
\]

independent of `K`, and with all fixed-order combinatorial constants having zero
exponential rate in `J`.

Let

\[
M_K(J)=1+\max_\tau\max_{u\le J}E_{K,\tau}(u)
\]

include the complete safe signal and every declared reflected auxiliary energy.

## 2. Non-top rows

By `L-24901`, every reflected row except the top-top residual corner has energy

\[
e^{-c_KJ}
\]

or is already an explicitly declared strict lower-scale source. These rows do
not affect the upper exponential rate.

## 3. Charged rows

By `L-24903` and `q_K<=C_ref`,

\[
\sum_\gamma\|b_\gamma(J)\|^2
\le
\exp\left[
\left({C_{\rm ref}\over K}+o_K(1)\right)J
\right]
\left[1+M_K((1-\delta)J+C_K)\right].
\tag{T-24901.1}
\]

The oriented incidence lemma ensures that no partition-created internal face is
counted in this ledger.

## 4. Reserve and recurrence

Insert (T-24901.1) into the strict reserve `D-24901.6`. Since `kappa_0` and all
fixed-order constants are independent of `J`, they contribute only
`e^{o_K(J)}`. Therefore every top packet satisfies

\[
\boxed{
E_{K,\tau}(J)
\le
\exp\left[
\left({C_{\rm ref}\over K}+o_K(1)\right)J
\right]
\left[1+M_K((1-\delta)J+C_K)\right].}
\tag{T-24901.2}
\]

Together with the non-top rows, this is a source-specific linear `BTP(K)`
recurrence with

\[
\varepsilon_K={C_{\rm ref}\over K}.
\tag{T-24901.3}
\]

No invocation of `L-23203` is used to create (T-24901.2); the recurrence is the
output of the reserve and charge certificates.

## 5. Scale contraction

The inherited finite-vector scale theorem gives

\[
\limsup_{J\to\infty}{\log M_K(J)\over J}
\le {C_{\rm ref}\over K\delta}.
\tag{T-24901.4}
\]

Every fixed superorder window remains nonzero in the open counterexample strip,
so it detects the same invariant `Theta_zeta`. Hence

\[
\boxed{
2\Theta_\zeta
\le {C_{\rm ref}\over K\delta}.}
\tag{T-24901.5}
\]

Letting `K` tend to infinity along the certified sequence gives

\[
\Theta_\zeta=0.
\]

Functional-equation symmetry yields

\[
\boxed{\mathrm{RH}.}
\tag{T-24901.6}
\]

## 6. Scalar firewall

The certificate controls one fixed-ratio shell source. By `L-23008`, all fixed
ratios have two-sided causal `ell^1` transfers and therefore the same Hardy
abscissa. In particular the dyadic shell estimate implies the square-root bound
for the exact `2/3` first Farey-cell increment, and conversely.

Thus the proof does not claim that the order-`K` packet automatically equals
`Delta_(2/3)^K M`. It exports one actual Möbius shell and uses an exact scalar
transfer.

## 7. Proof boundary

The deduction from a uniform `RBC(K)` family to RH is complete. The theorem does
not construct the source-bound reserve, incidence binding, or bounded charge
map. Those are the explicit proof obligations of Issue #249.
