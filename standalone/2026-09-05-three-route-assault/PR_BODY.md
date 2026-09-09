# Three-route RH assault: horizontal surplus, theta determinant, and fixed-frequency transport

**Status: proposed mathematics, complete proofs supplied, independent review required. RH remains unproved.**

Base: `main@6dda8b5125457ed936330229f8c9eb6491728e76`.
The exact publication head belongs in the external publication receipt or PR text; a tracked file cannot contain its own commit hash.

This is one additive research packet under `standalone/2026-09-05-three-route-assault/`. No predecessor, canonical, integrated, production, or formal-library file changes.

## Route 3: constructive horizontal-energy extraction

For every finite conjugation-invariant multiset, the exact identity is

`E-(2M-S)=2d+2ell+4h_E+8h_N+R`,

with all terms nonnegative. An intrinsic horizontal Schur matrix

`H=C* C-C* B(B* B)^(-1)B* C`

gives `E>=2M-S+8 Tr(H)+4 Tr(H^2)`. It is positive definite when nonreal pairs are present; real multiplicities do not create horizontal directions. For simple packets with q nonreal pairs, `E>=2M-S+8h+8h^2/q`, sharp for one pair.

A companion theorem gives a tail-error threshold below which a negative direction survives. The obligatory adversarial control proves that two nearby real nodes can screen the raw quadratic signal to `y^6/1575`; arbitrarily many real nodes can screen a fixed displaced pair arbitrarily strongly at fixed bandwidth.

**Open:** an unaveraged arithmetic bound and a complete tail estimate beating the actual conditioned gap. No improved zero proportion is claimed.

## Route 1: exact scalar determinant, but marked positive collapse fails

An explicit rational weighted shift plus a source-Taylor-coefficient rank-one row is trace class and has Fredholm determinant exactly `F(u)/F(0)`. Its finite determinants are the Taylor sections. It has a coefficient-independent negative Rayleigh direction and no positive diagonal symmetrizer.

For the actual theta mixture, distinct half-integer modes have strictly positive covariance. That contradicts the two-mode principal-minor inequality required by a Hermitian marked determinant. The parent's vacuum/forced-bit model gives an independent covariance obstruction. The natural nonatomic direct integral is not compact and has no ordinary Fredholm determinant. Explicit second/third scalar cumulant debts are retained.

**Open:** a different positive scalar realization. The marked obstruction does not refute the scalar TQF target or RH.

## Route 2: one fixed frequency interval suffices

For any probability frequency measure of finite second moment, its maximal-prefix energy is comparable to the untwisted maximal prefix with logarithmic loss. The stationary ratio-67 Möbius energy is therefore equivalent, at subpower scale, to the fixed `[1,2]` frequency integral. The same outer-horizon measure is required for every prefix.

The exact damped causal twist-transport norm is `(sqrt(t^2+4sigma^2)+abs(t))/(2sigma)`, with sharp ambient equality frequencies. It diverges at the critical boundary. The attempted long-frequency mean-value bootstrap does not improve the exponent; a positive-source countercontrol explains why signs must enter.

**Open:** any new signed Möbius power saving or exponent contraction.

## Sources and validation

Sources are pinned to PRs #785, #779 and #788; source receipts and literature boundaries are in the packet. Standard Fredholm, Abel/Plancherel, Hilbert projection and Schur-complement tools are credited. No external novelty or priority claim.

447 freshly recomputed exact rational controls pass normally and under `-O`. All 17 unit/rejection tests pass in both modes. Controls include independent matrix and ordered-kernel pair energies, exact Schur complements, finite companion polynomials and Legendre screening coefficients. They do not machine-prove the analytic theorems.

No Lean build, directed integration, broad zero/prime scan, independent referee review, or parent repository-wide suite was run.

## Reading and next pass

Start with the packet README, then Route 3's surplus proof and screening countercontrols, Route 1, and Route 2. Read the self-audit before extending any conclusion. Provisional next-pass priority: Route 3, Route 1, then Route 2 as the arithmetic audit. All three remain open research routes.
