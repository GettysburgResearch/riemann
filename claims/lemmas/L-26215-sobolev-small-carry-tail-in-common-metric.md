# L-26215 — Sobolev-small digital tails after a declared smoothing intertwiner

Claim ID: `L-26215`  
Title: The binary-digit tail has explicit `H^1 -> L^2` decay, but application to the raw annular step signal requires a separate smoothing/source-map theorem  
Status: **SCOPE-CORRECTED CONDITIONAL ADAPTER — RAW CARRY APPLICATION OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Depends on: `L-26213`, `L-26214`; PR #236 `L-23016`; `L-26204`  
Scope: exact physical tail identity and Sobolev estimate on an `H^1` carrier; no direct estimate for the unsmoothed carry signal

## 1. The digital tail operator

For

\[
c_2(n)=1-v_2(n),
\]

define

\[
\mathcal T_Y
=\sum_{n\ge Y}\frac{c_2(n)}{\sqrt n}\tau_{\log n}.
\]

PR #236 `L-23016` proves, for every causal source in its declared absolutely-continuous Sobolev domain,

\[
\boxed{
\|\mathcal T_Yf\|_2
\le
\varepsilon_Y
\left(\|f\|_2+\|f'\|_2\right),
}
\tag{L-26215.1}

where

\[
\boxed{
\varepsilon_Y
=O\!\left({\log Y\over\sqrt Y}\right).
}
\tag{L-26215.2}

This theorem is retained exactly at that scope.

## 2. Exact source identity

For every finite coefficient sequence `x`, the source intertwiner of `L-26213` gives, as a causal distribution and in `L^2`,

\[
\boxed{
Q_{c_{\ge Y}*x}
=\mathcal T_YQ_x.
}
\tag{L-26215.3}

Thus whenever the chosen physical carrier `Q_x` belongs to the Sobolev domain of (L-26215.1),

\[
\boxed{
\|Q_{c_{\ge Y}*x}\|_2
\le
\varepsilon_Y
\left(\|Q_x\|_2+\|Q_x'\|_2\right).
}
\tag{L-26215.4}

The same statement holds after convolution with a fixed compact `C_c^1` smoother, because smoothing commutes with every translation and with arithmetic source convolution.

## 3. Scope correction for the raw annular window

The compact window `h_omega` used in `L-26213` is piecewise exponential with jump discontinuities. For a generic finite annular coefficient sequence, the raw signal

\[
Q_x=h_\omega*\alpha_x
\]

is not in `H^1`: its distributional derivative contains the source jump atoms.

Therefore (L-26215.1) may **not** be applied directly to the raw `Q_x`, and the equality of its `L^2` norm with the weighted carry norm does not by itself supply an `H^1` estimate.

The earlier version of this lemma silently combined these incompatible domains. That inference is withdrawn.

## 4. Two legitimate completion interfaces

A proof may recover the intended tail decay through either of the following explicit routes.

### 4.1 Smoothed annular intertwiner

Choose a fixed zero-safe compact smoother `g` and prove an exact source map from

\[
g*Q_x
\]

to a positive integral or finite direct sum of the carry rows used in the factor-five reserve. Then (L-26215.4) applies to `g*Q_x`.

The smoothing-to-carry source map is not supplied by `L-26213` and remains a production obligation.

### 4.2 Six-factor positive potential

`L-26204` represents the complete Euler-fiber source as

\[
Z=\partial_t^2(\partial_t-1/2)Y_K,
\]

where `K` is a six-factor compact convolution. The potential has sufficient spline regularity to furnish a Sobolev carrier after the declared boundary operator is incorporated.

A production proof must still connect that smoother carrier to the exact annular/factor-five carry feature without dropping endpoint atoms.

## 5. Surviving exact conclusion

The physical tail identity (L-26215.3) and the Sobolev estimate (L-26215.4) are valid under their explicit regularity hypothesis. They show that no new arithmetic estimate is needed once a Sobolev-compatible physical-to-carry intertwiner is constructed.

They do **not** currently prove that the raw strict-prefix carry tail is `O((log Y)/sqrt Y)` in the weighted carry norm.

## 6. Proof boundary

Closed exactly:

- identification of the coefficient tail with the physical digital-tail operator;
- the `O((log Y)/sqrt Y)` estimate on an `H^1` carrier;
- commutation with a declared fixed smoothing.

Open:

- a Sobolev-compatible smoothing/potential-to-carry intertwiner;
- a quantitative raw carry-tail estimate;
- the annular recurrence;
- RH.
