# M-0602 — Moment-corrected nonuniform carrier transform

Claim ID: M-0602  
Title: A Taylor-corrected FFT screen with an explicit nonuniform-gridding remainder  
Status: PROPOSED  
Authoring agent: `gpt56-02-b`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-0605  
Scope: discovery evaluation of consecutive high carrier indices  
Related counterexample candidates: none

## Problem

For a center index `n_0`, the source arrays require values of

\[
 C_k=\sum_q a_q e^{i(n_0+k)\theta_q}
\]

for many consecutive offsets `|k|<=K`, where the phases `theta_q` are
nonuniform. Direct recurrence costs `O(PK)`. Nearest-bin FFT gridding is fast
but its uncontrolled phase bias was comparable to the smallest margins in the
first high-carrier screens.

## Proposed method

Choose a power-of-two grid `M`. For each phase, choose the nearest grid point

\[
 \phi_q=\frac{2\pi j_q}{M},\qquad
 \delta_q=\theta_q-\phi_q,
 \qquad |\delta_q|\le\frac\pi M.
\]

For `0<=r<=R`, accumulate the gridded moments

\[
 A_{j,r}=\sum_{q:j_q=j}a_qe^{in_0\theta_q}\delta_q^r.
\]

Then

\[
 C_k=\sum_{r=0}^{R}\frac{(ik)^r}{r!}
 \sum_{j=0}^{M-1}A_{j,r}e^{2\pi i k j/M}+E_k.
\]

Thus `R+1` FFTs replace a full direct carrier recurrence. If

\[
 W=\sum_q|a_q|,
 \qquad \eta=\frac{K\pi}{M},
\]

Taylor's theorem gives the uniform analytic gridding bound

\[
 |E_k|\le
 W e^\eta\frac{\eta^{R+1}}{(R+1)!}
 \qquad(|k|\le K).
\]

The same construction is run separately for the `P_S` and `P_D` weights of
L-0605.

## Proof

For each term,

\[
 e^{ik\theta_q}=e^{ik\phi_q}e^{ik\delta_q}
 =e^{ik\phi_q}\sum_{r=0}^{R}\frac{(ik\delta_q)^r}{r!}
 +e^{ik\phi_q}R_{q,k}.
\]

The complex exponential remainder satisfies

\[
 |R_{q,k}|\le e^{|k\delta_q|}
 \frac{|k\delta_q|^{R+1}}{(R+1)!}.
\]

Summation, `|k delta_q|<=eta`, and the triangle inequality prove the bound.

## Proof boundary

The displayed bound controls only Taylor truncation caused by nonuniform
gridding. It does **not** include:

- floating accumulation error in the moment bins;
- phase-reduction or transcendental-library error;
- FFT roundoff;
- conversion from source values to matrix entries;
- eigenvalue conditioning.

X-0602 therefore remains EMPIRICAL. A proof implementation would replace every
stage with complex balls or exact dyadic intervals and add a certified FFT or a
separate direct verifier for the final short list.

## Calibration

At `c=10^6`, `K=64`, `M=4096`, and `R=10`, the analytic Taylor bounds were
approximately

```text
P_S: 2.0951e-19
P_D: 6.0131e-20
```

while the observed maximum discrepancy from a direct `__float128` phase
recurrence after double serialization was `1.7764e-15` for both arrays. This
correctly shows that floating/FFT error, not gridding truncation, was the
calibration floor.

At `c=10^8`, `K=8192`, `M=65536`, and `R=10`, the analytic bounds were
approximately

```text
P_S: 2.541e-8
P_D: 5.511e-9.
```

These are small relative to the retained positive packet margin but are not a
certificate.

## Suggested next attack

Use ball-valued moments, a rigorously bounded radix-2 FFT, and a direct
ball-arithmetic reevaluation of every nominated packet. The wide transform
should remain a screening device; the final certificate should not depend on a
million-point FFT.
