# R-26201 — Fixed Euler filtering does not strengthen the real positive-adjoint Selberg identity

Claim ID: `R-26201`  
Status: `SCOPE REFUTATION — exact gauge cancellation`  
Scope: positive real-exponential adjoints for fixed translation-polynomial filters  
Date: 2026-08-08  
Depends on: `L-26203`

A tempting completion of the critical Euler-fiber programme is:

```text
filter the centered Selberg equation;
use the positive inverse and positive generalized prime sequence;
solve the filtered real-exponential adjoint;
deduce a stronger positive energy inequality.
```

The final step is false. The filtered adjoint exists, but it is exactly gauge-equivalent to the unfiltered adjoint.

## Exact calculation

For a fixed multiplier `P`, put

\[
M(s)=P(s)H(s).
\]

`L-26203` gives the filtered Riccati equation

\[
-PM'
+\left(P'+\frac{2P}{s-1/2}\right)M
+M^2
=P^2\mathcal R.
\tag{R-26201.1}
\]

The unique positive density cancelling the complete interior linear term and producing a unit boundary atom at `s_0>1` is

\[
 m_{P,s_0}(u)
 =\frac{P(s_0)(s_0-1/2)^2}
 {P(u)^2(u-1/2)^2}.
\tag{R-26201.2}
\]

Pairing gives

\[
 M(s_0)+\int m_{P,s_0}M^2
 =\int m_{P,s_0}P^2\mathcal R.
\tag{R-26201.3}
\]

Substituting `M=PH` cancels `P(u)^2` from both integrals. Dividing by `P(s_0)` gives exactly

\[
\boxed{
 H(s_0)
 +(s_0-1/2)^2
  \int_{s_0}^{\infty}\frac{H(u)^2}{(u-1/2)^2}du
 =(s_0-1/2)^2
  \int_{s_0}^{\infty}\frac{\mathcal R(u)}{(u-1/2)^2}du.
}
\tag{R-26201.4}
\]

This is the original unfiltered positive-exponential identity.

## Consequence

The critical Euler fiber is still valuable:

- it produces a positive compact Green factor;
- it has a positive inverse and positive generalized primes;
- it supplies a strict vertical multiplier reserve;
- its parity pair supplies the `45/4` closed-strip frame.

But none of those facts turns the real-axis positive-exponential adjoint into a new inequality. A proof must use structure that is absent from (R-26201.4), for example:

- the two-frequency physical block of PR #241;
- a source-bound signed boundary contraction;
- a paired parity-channel reserve;
- an independently proved carry/LP minorant.

## Automatic scope correction

Reject any proposed EFRC proof whose only substantive estimate is the filtered version of the real positive-adjoint identity. Such a proof has merely multiplied and divided by the same gauge.

This refutation does not contradict:

- `L-26201` or `L-26202`;
- the paired reserve of `L-26205`;
- a genuinely local two-frequency contraction;
- RH.
