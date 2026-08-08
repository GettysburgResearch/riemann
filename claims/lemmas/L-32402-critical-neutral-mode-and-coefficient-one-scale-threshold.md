# L-32402 — Critical neutral mode and the coefficient-one dyadic threshold

Claim ID: `L-32402`  
Title: Zeta-zero modes are exactly neutral for the critical eta transfer, and coefficient-one dyadic scale descent is the sharp RH threshold  
Status: **PROPOSED COMPLETE EXACT SPECTRAL/SCALE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-08  
Dependencies: PR #323 `R-32201`; PR #297 `L-29001`; PR #316 `T-30901`  
Scope: spectral normalization and recurrence threshold; no proof of the source-specific recurrence and no RH claim by itself

## 1. Critical eta transfer

Retain the square-root normalized paired eta comb

\[
\beta
=\sum_{k\ge1}
\left[
(2k)^{-1/2}\delta_{\log(2k)}
-(2k+1)^{-1/2}\delta_{\log(2k+1)}
\right].
\tag{L-32402.1}
\]

For a Mellin exponential

\[
F_\lambda(t)=e^{\lambda t},
\]

paired convolution gives exactly

\[
\boxed{
(\beta*F_\lambda)(t)
=\left[1-\eta\left(\frac12+\lambda\right)\right]F_\lambda(t).
}
\tag{L-32402.2}
\]

Indeed the multiplier is the paired series

\[
\sum_{k\ge1}(2k)^{-1/2-\lambda}
-
\sum_{k\ge1}(2k+1)^{-1/2-\lambda}
=1-\eta(1/2+\lambda).
\]

## 2. Exact neutrality at a zeta zero

Let

\[
\rho=\beta_0+i\gamma
\]

be a nontrivial zeta zero, and put

\[
\lambda_\rho=\rho-\frac12.
\]

Since

\[
\eta(\rho)=(1-2^{1-\rho})\zeta(\rho)=0,
\]

one has

\[
\boxed{
\beta*F_{\lambda_\rho}=F_{\lambda_\rho}.
}
\tag{L-32402.3}
\]

Thus the principal RH-bearing mode is **neutral**, not contractive, under the unshifted eta propagation.

This is the correct interpretation of PR #323's zero-mode firewall. Any strict source-blind contraction containing this mode is impossible, but strict contraction is also unnecessary for a dyadic proof.

## 3. Rebased dyadic scale factor

The same Mellin mode has endpoint dependence

\[
X^{\lambda_\rho}.
\]

Under the dyadic endpoint dilation `X -> 2X`,

\[
\boxed{
(2X)^{\lambda_\rho}
=2^{\lambda_\rho}X^{\lambda_\rho},
\qquad
\left|2^{\lambda_\rho}\right|
=2^{\beta_0-1/2}.
}
\tag{L-32402.4]

(The closing bracket in the tag is typographical only.)

Consequently

```text
critical-line zero beta_0=1/2     dyadic amplitude factor 1;
off-line zero beta_0>1/2          dyadic amplitude factor >1.
```

The critical exponent is therefore detected by **nonexpansion across endpoint scale**, not by strict decay of the eta transfer itself.

## 4. Coefficient-one recurrence is sufficient

Let `E(J)>=0` be any local energy controlling the complete pole field of `L-29001`. Suppose that for one fixed `delta>0`,

\[
\boxed{
E(J)
\le C(1+J)^A+E(J-\delta)
}
\tag{L-32402.5}
\]

for all sufficiently large `J`.

Iteration through `O(J/delta)` levels gives

\[
\boxed{
E(J)=O((1+J)^{A+1}).
}
\tag{L-32402.6}
\]

In particular

\[
E(J)=e^{o(J)}.
\]

For the atomized Nyman/carry energy of `L-29001`, that subexponential bound implies RH by its vector-valued pole criterion.

Thus a coefficient-one fixed-scale recurrence is already sufficient:

\[
\boxed{
\text{fixed scale descent + total coefficient }1
\Longrightarrow\text{ polynomial energy }
\Longrightarrow\mathrm{RH}.
}
\tag{L-32402.7}
\]

No strict coefficient below one is required.

## 5. Sharpness

Equation (L-32402.4) explains why coefficient one is the natural threshold.
A source-complete recurrence with asymptotic scale coefficient strictly larger than one may accommodate an off-line mode. A coefficient-one recurrence permits critical-line neutral modes but forbids persistent exponential growth in the scale variable.

Therefore the correct research target is not

```text
contract the complete eta/Möbius state by theta<1;
```

but

```text
carry the principal dyadic mode losslessly;
dissipate or route every transverse/capped component;
obtain a coefficient-one lower-scale recurrence.
```

This aligns the finite carry program with the exact spectral threshold rather than asking for an unnecessarily strong inequality which PR #323 proves impossible on the full source.

## 6. Proof boundary

Established here, subject to review:

1. exact eta multiplier on Mellin exponentials;
2. exact unit multiplier at every nontrivial zeta zero;
3. exact dyadic rebasing factor `2^(rho-1/2)`;
4. critical/off-line modulus dichotomy;
5. coefficient-one fixed-delay recurrence implies polynomial local energy and hence RH through the already-stated pole criterion.

Not established:

1. a source-specific coefficient-one recurrence;
2. the cap/transverse transport needed to construct it;
3. RH.
