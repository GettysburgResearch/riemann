# Centered gamma continuation: exact tail removal, faster whole-xi approximation, and a tested obstruction

**Status: proposed component proofs and two computer-assisted finite zero certificates; independent mathematical/code review required. RH and cofinal zero confinement remain OPEN.** This is an add-only continuation of [PR #849](https://github.com/GettysburgResearch/riemann/pull/849), frozen at `11a12b8ceb7db98c7961a5cebf3870b2f31dfa79`. No canonical acceptance or integration change is made.

## What changes the next attack

The raw reciprocal gamma flow does not preserve the critical strip: at the exact interpolation time u=7/10 in the second-to-third step, its transform has a certified nonreal zero near `26.813585536814 + 0.420994940463 i`. The old integer-N4 scout near `28.055585538409 + 2.621997933269 i` is also certified. Each certificate counts one simple zero in a disk of radius 10^-12 using the defining integral, all quadrature errors, and the entire time tail. **Neither is a zero asserted for xi. No collision time or complete root trajectory is certified.**

There is a positive replacement tool. For the prescribed gamma sum X_N, add the EXACT mean of the omitted tail, tau_N=2 sum_(n>N)n^-2, before reciprocal projection. The resulting positive even density has compact support of radius (log(pi/tau_N))/2. Its normalized entire transform Fhat_N approaches the complete unchanged Xi/Xi(0), uniformly on each whole horizontal strip, at rate **O(N^-3)**. This is not a relative error near zeros; the constants are unevaluated.

More precisely, if v_N=2 sum_(n>N)n^-4, the full leading correction is

    Fhat_N = Phi + v_N [D Phi - Phi D Phi(0)] + O(N^-5),
    D P = [(z^2+3/4-iz)P(z-4i)+(z^2+3/4+iz)P(z+4i)]/(16pi^2).

For real z, these shifted xi values lie on Re(s)=9/2 and its reflected line. The signed correction is explicit; its sign or its control of zero collisions is not established. The proof retains every tail coordinate through a convergent infinite differential expansion and positive collision-counting bounds. It also proves the raw family's translation approximation and improves its absolute error to O(N^-1).

## Read and reproduce

Read [PROOF.md](PROOF.md) for the analytic construction, domains, full tails and exact remaining RH implication. [CERTIFICATE.md](CERTIFICATE.md) gives the complete circle, branch, quadrature and Rouché argument. [SOURCE_LOCK.json](SOURCE_LOCK.json) and [VALIDATION.md](VALIDATION.md) distinguish inherited inputs, new derivations, actual executions and omissions.

From this directory, run:

```sh
python -I -S -B verify.py --check results.json
python -I -S -B -O verify.py --check results.json
python -I -S -B test_verify.py
python -I -S -B -O test_verify.py
```

The accepting command reconstructs both complete integrals; it does not merely hash a supplied result. `certificate.py --write /tmp/receipt.json` is producer mode, not acceptance. Integer/Fraction arithmetic and standard-library code only. Output files belong outside the source packet.

## Exact boundary

Faster convergence does not force spectral reality. At a fixed simple zero z0 of Phi, the construction tracks it with displacement `-v_N D Phi(z0)/Phi'(z0)+O(N^-5)` whether that zero is real or nonreal. A cofinal expanding-window confinement theorem for the exact centered family is still needed. The centered first member is not the parent's real-zero Bessel seed; no such property is inherited by fiat.

The next substantive problem is to control the signed reciprocal variance correction at increasing height, including multiple-zero splitting and boundary entry. A positive density, a successful finite disk count, or simple-real-root kinematics does not supply that theorem. Original parent files and status remain unchanged; classical gamma/xi, Cauchy, Fourier, Bonferroni and Rouché mechanisms are credited without a novelty claim.
