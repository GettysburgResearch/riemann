# R-23706 — The uncentered cumulative-energy condition is false

Claim ID: `R-23706`  
Title: The known zero-frequency double pole forces superquadratic uncentered logarithmic energy, so the former `HCRE(5)` condition cannot hold  
Status: **EXACT REFUTATION OF THE FROZEN ENERGY CONDITION; SHELL POSITIVITY REMAINS OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23709`, `L-23713`  
Scope: the former condition in `T-23704.6`--`T-23704.7`

## 1. Zero-frequency principal part

Put

\[
Q(t)=C(e^t),
\qquad
s=z+\frac12,
\]

and define

\[
\boxed{
h(z)=
\frac{s(1-5^{-s})}{(s-1)\zeta(s)}.
}
\tag{R-23706.1}
\]

The exact transform of `L-23709` is

\[
\boxed{
\widehat Q(z)=\frac{h(z)}{z^2}.
}
\tag{R-23706.2}
\]

The value

\[
\boxed{
a_5=h(0)
=-\frac{1-5^{-1/2}}{\zeta(1/2)}>0
}
\tag{R-23706.3}
\]

is nonzero. The sign follows elementarily from

\[
\eta(1/2)=(1-\sqrt2)\zeta(1/2)>0,
\]

where the alternating eta series is positive.

Thus

\[
\widehat Q(z)=\frac{a_5}{z^2}+O(1/z)
\qquad(z\to0).
\tag{R-23706.4}
\]

The double pole is the explicit positive linear main mode `a_5 t` of the cumulative state. It is unrelated to any hypothetical off-line zero.

## 2. The former continuous energy has a forced divergence

`L-23713` defined

\[
D(t)=Q'(t)+\frac12Q(t).
\]

Since `Q(0)=0`,

\[
\widehat D(z)
=(z+1/2)\widehat Q(z)
=rac{a_5}{2z^2}+O(1/z).
\tag{R-23706.5}
\]

Hence there are absolute `epsilon,c>0` such that, for

\[
0<\sigma<\epsilon,
\qquad |\tau|\le\sigma,
\]

one has

\[
|\widehat D(\sigma+i\tau)|
\ge c\sigma^{-2}.
\]

Therefore

\[
\boxed{
\int_{-\infty}^{\infty}
|\widehat D(\sigma+i\tau)|^2d\tau
\ge c^2\sigma^{-3}.
}
\tag{R-23706.6}
\]

In particular,

\[
\boxed{
\sigma^2
\int_{-\infty}^{\infty}
|\widehat D(\sigma+i\tau)|^2d\tau
\longrightarrow+\infty.
}
\tag{R-23706.7}
\]

This contradicts the former condition `T-23704.7`.

By the exact Abel--Cesaro identity in `L-23713`, the physical assertion

\[
\int_0^T|D(t)|^2dt=o(T^2)
\]

is likewise impossible. The linear main mode produces energy of cubic logarithmic order.

## 3. Scope of the refutation

Refuted:

```text
former continuous HCRE(5) condition;
former claim that the uncentered D-energy is subquadratic;
former T-23704 deduction using that condition.
```

Not refuted:

```text
the exact cumulative profile and Mellin transform;
the two positive forcing identities;
the finite annulus certificate;
the digital Abel identity and first-zero lower bound;
pointwise or eventual positivity of C;
Greedy Slack/DCRS;
RH.
```

The correct energy must subtract the explicit linear mode before taking a Hardy norm. That centered theorem is stated in `L-23714` and the corrected `T-23704`.

## 4. Review lesson

A proposed energy estimate must inspect every real-axis principal part before invoking a reflected square. Here the zero-frequency pole is not an error or an off-line-zero contribution; it is the sharp positive carry mass. Removing it is a normalization, not an assumption of RH.
