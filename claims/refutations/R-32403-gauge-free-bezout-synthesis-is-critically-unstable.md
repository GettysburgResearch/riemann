# R-32403 — Exact gauge-free Bézout synthesis is unstable on the critical annulus

Claim ID: `R-32403`  
Title: Any exact parity synthesis that simultaneously reconstructs `1/zeta` and deletes the derivative gauge has a pole between `|z|=1/2` and `|z|=1/sqrt(2)`  
Status: **EXACT FILTER-SCOPE NO-GO**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-09  
Dependencies: `L-26205/L-26206`; `L-32409`  
Scope: exact gauge cancellation by a scalar two-channel Bézout partition; does not refute approximate/stable source-coupled Schur assemblies

## 1. General Bézout partition

Let

\[
p_+(z)=p(z),\qquad p_-(z)=p(-z),
\]

and suppose analytic functions `U_+,U_-` reconstruct the odd Euler core through

\[
A(z)+B(z)=1,
\qquad
A=U_+p_+,
\qquad
B=U_-p_-.
\tag{R-32403.1}

After the final `(1-z)` factor, differentiating with respect to `s` produces the gauge factor

\[
 h(z)=1+(1-z)
 \left[
  A(z){p_+'(z)\over p_+(z)}
 +B(z){p_-'(z)\over p_-(z)}
 \right].
\tag{R-32403.2}

The stable cubic synthesis of `L-32409` has a nonzero compact term in the bracket.

## 2. Formal gauge-free solution

To leave only the unavoidable delayed odd-core term one would require

\[
h(z)\equiv1.
\]

Together with `A+B=1`, this forces

\[
\boxed{
 A_*(z)
 =-
 {p_-'(z)/p_-(z)
  \over
  p_+'(z)/p_+(z)-p_-'(z)/p_-(z)}.
}
\tag{R-32403.3}

There is no remaining scalar synthesis freedom once exact gauge cancellation is imposed.

For

\[
p(z)=(1-z)(1-2z)(1-\sqrt2z)^2,
\]

direct simplification gives the denominator factor

\[
\boxed{
 D(z)
 =(8\sqrt2+12)z^4
 -(10\sqrt2+12)z^2
 +(2\sqrt2+3).
}
\tag{R-32403.4}

The numerator of `A_*` contains, up to a nonzero scalar,

\[
(z-1)(2z-1)(\sqrt2z-1)
\left[
8\sqrt2 z^2+4z+9\sqrt2z+2\sqrt2+3
\right].
\tag{R-32403.5}

## 3. A genuine pole inside the critical annulus

At the two positive radial endpoints,

\[
\boxed{D(1/2)=3/4>0,}
\tag{R-32403.6}
\]

while

\[
\boxed{D(1/\sqrt2)=-\sqrt2<0.}
\tag{R-32403.7}

Therefore `D` has a real zero

\[
 z_*\in(1/2,1/\sqrt2).
\]

On this open interval every factor in (R-32403.5) is nonzero and the final bracket is strictly positive. Hence the zero of `D` is not canceled by the numerator. Thus `A_*`, and consequently at least one synthesis channel, has a genuine pole **inside** the closed-strip critical annulus.

Numerically only for orientation, the first positive root is about `0.5540823`; no numerical value is used in the proof.

## 4. Consequence

A critically stable exact synthesis cannot delete the derivative gauge identically. The delayed state in `L-32409` is structural, not an artifact of choosing a nonoptimal cubic Bézout polynomial.

This rules out the tempting shortcut

```text
choose a better exact inverse filter
-> reconstruct the Mobius current
-> no delayed source state
-> close the recurrence.
```

A valid completion must instead retain the delayed odd-core state and/or absorb the compact gauge by the source-matched Hermitian reserve.

## 5. Proof boundary

Established exactly:

1. the unique formal gauge-free partition;
2. its explicit denominator;
3. a sign change of that denominator across the critical annulus;
4. noncancellation of the interior pole.

Not established:

1. optimality of the existing cubic synthesis among all stable approximate gauges;
2. failure of a source-convolved Schur completion;
3. RH.
