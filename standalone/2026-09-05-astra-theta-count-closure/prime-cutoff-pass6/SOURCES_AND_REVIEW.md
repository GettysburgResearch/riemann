# Source ledger and independent-review priorities

## Repository sources

1. PR #790 at bce97be9727dea9968db7517738edc966d2cc86b,
   heat-hankel-pass5/PROOF.md, Git blob
   caf9753e5c3e3bb918289da0f4e92ae7c6441f6c.
   Read in full, including the source budget, explicit formula, inherited
   metric, and distinction between positive heat and positive matrices.
   The local attached snapshot has this exact Git blob identity.
2. PR #792 at 39c13367f4b3956631ea1e00fac6c3005fc32057,
   cross-route-hardy-laguerre/BRIDGE.md: read the arithmetic construction,
   finite matrices and conserved-form/trace mechanism. Its explicit
   arithmetic relative-form obstruction motivated the cutoff test here.
   No independent acceptance of every theorem or replay of its code is claimed.
3. PR #793's latest pass3 description at bfb66e07f7e38306dbcb916911332a591efce917
   was read at PR-summary scope, not independently proof-audited this pass.
4. Original #790 checkpoint bc3c35d8f434949748a2185783bf831d3afd9126:
   verify_low_zero.py, blob dc65c7a2273c9657bb2e68ec3fa99ad115f42c3e;
   low_zero_result.json, blob d8617fb2c96b14531e4288d02119be0d917ebc17.
   Both locally supplied files match these identities. The script was run
   again normally and under -O; both complete outputs match the retained
   JSON. This is only a sign change between ordinates 14 and 15, not V100.

## External mathematical inputs

[S1] A. Chirre and F. Goncalves, Bounding the log-derivative of the zeta-function,
Mathematische Zeitschrift 300 (2022), 1041--1053, Proposition 5.
https://doi.org/10.1007/s00209-021-02820-9
The full HTML statement of Proposition 5 was read. It explicitly sums over
rho=beta+i gamma and is unconditional. None of the paper's RH-conditional
main theorems is used. Its Fourier variable is ell/(2pi) in our convention.
The endpoint term gives R(0)^2 after dividing the full zero sum by two.

[S2] NIST Digital Library of Mathematical Functions, Sections 5.4, 5.9,
5.11, 5.12: digamma special values/integral representations and Euler beta integral.
https://dlmf.nist.gov/5.4
https://dlmf.nist.gov/5.9
https://dlmf.nist.gov/5.11
https://dlmf.nist.gov/5.12
These HTML pages were consulted. Beta integration, duplication/reflection,
and the positive digamma difference series supply the elementary formulas.
Their consequences needed here are also derived in the proof.

[S3] D. R. Yafaev, Quasi-diagonalization of Hankel operators,
arXiv:1403.3941, abstract consulted for general prior-art context only.
https://arxiv.org/abs/1403.3941
General Hankel sign/inertia theory is classical. PC-2 includes its own
finite-dimensional negative-subspace construction rather than assuming
that abstract theorem as an unexamined positivity input.

[S4] D. Platt and T. Trudgian, The Riemann hypothesis is true up to 3*10^12,
Bull. London Math. Soc. (2021), DOI 10.1112/blms.12460,
arXiv:2004.09765. Abstract/theorem scope checked online.
https://arxiv.org/abs/2004.09765
Only its restriction to 0<gamma<=100 is used, and only for PC-3. The
published zero verification was not rerun. No simplicity is assumed.
No PDF was analyzed or new PDF hash asserted in this pass.

## Scope and novelty

PC-1/PC-2 concern deletion of the prime tail in the ACTUAL explicit formula.
They are not counterexamples to the full form or to RH. The positive
family in PC-3 is already implicit in the earlier b=2 inequality; a short
independent budget proof is included, so no high-order heat theorem is used.
No priority claim is made for the cutoff observation, beta calculation,
density argument, or general Hankel mechanism.

## Review priorities

1. Verify the 4pi normalization, the exact gamma integral, the vanished
   endpoint, and all prime-power/Fourier orientations in (1)--(2).
2. Check beta moments, the all-real-parameter variance inequality, and
   the rational certificates used in the gamma constant.
3. Check that PC-1 applies uniformly to EVERY n<=X, not just typical primes.
4. Check PC-2's trace-class integral, the zero-endpoint subspaces, and the
   dominated-convergence exponent in the finite Gaussian Gram limit.
5. Check that PC-3 bounds the ENTIRE unverified zero tail, with multiplicity;
   then check the sign of the prime-tail inference.
6. Check the dense-span proof, and the exact high-index negative witness
   which prohibits promoting generatorwise positivity to all-matrix PSD.
7. Keep source cutoff and finite-dimensional compression distinct.
8. Do not label the unresolved arbitrary-signed-vector estimate proved.
