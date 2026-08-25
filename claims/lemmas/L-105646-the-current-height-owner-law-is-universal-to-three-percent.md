# L-105646 — The Xi-prime current-height owner law is universal to three percent

Claim ID: `L-105646`  
Status: **PROVED EXACT CONSEQUENCE OF THE MAXWELL SANDWICH**  
Created: 2026-08-25  
Depends on: `L-105644--L-105645`  
RH status: **not assumed**

## 1. Explicit reference law

Let

\[
\rho=\alpha+i\gamma,
\qquad
0<\gamma\le{1\over2},
\]

be one zero of `Xi'`. Define on `0<=H<=gamma` the explicit survival function

\[
\boxed{
S_\gamma(H)
={2(\gamma-H)\over2\gamma-H}.
}
\tag{L-105646.1}

It decreases from one to zero. Its Stieltjes probability measure is absolutely
continuous with density

\[
\boxed{
{d\mu_\gamma\over dH}
={2\gamma\over(2\gamma-H)^2},
\qquad0<H<\gamma.
}
\tag{L-105646.2}

Indeed,

\[
- S_\gamma'(H)
={2\gamma\over(2\gamma-H)^2}
\]

and the density integrates to one.

This is exactly the height-owner law obtained by replacing the actual current
profile `R_H` by the elementary exponential profile `exp(-H xi)`.

## 2. Actual survival function

`L-105644` defines the actual current-height survival function

\[
Q_\rho(H)
=
2(\gamma-H)
\int_0^\infty
R_H(\xi)e^{-2(\gamma-H)\xi}\,d\xi.
\tag{L-105646.3}

`L-105645` gives, throughout `0<=H<=gamma<=1/2`,

\[
{97\over100}e^{-H\xi}
< R_H(\xi)
\le e^{-H\xi}.
\]

Integrating against the normalized exponential model vector yields

\[
\boxed{
{97\over100}S_\gamma(H)
< Q_\rho(H)
\le S_\gamma(H).
}
\tag{L-105646.4}

Thus the actual owner survival function differs from the explicit reference
law by at most three percent:

\[
\boxed{
0\le S_\gamma(H)-Q_\rho(H)<{3\over100}
\qquad(0\le H\le\gamma).
}
\tag{L-105646.5}

## 3. Kolmogorov control of the owner measure

Let

\[
d\nu_\rho=-dQ_\rho
\]

be the actual probability measure of `L-105644`. Since `Q_rho` and `S_gamma`
are survival functions,

\[
\boxed{
\sup_{0\le H\le\gamma}
\left|
\nu_\rho([H,\gamma])
-
\mu_\gamma([H,\gamma])
\right|
<{3\over100}.
}
\tag{L-105646.6}

Equivalently, the Kolmogorov distance between the actual source-owned height
law and the explicit rational law is below `0.03`, uniformly in the zero
height and horizontal location.

## 4. Mean owner height

For any probability law on `[0,gamma]`, the mean is the integral of its
survival function. Direct integration gives

\[
\boxed{
\int_0^\gamma S_\gamma(H)dH
=2\gamma(1-\log2).
}
\tag{L-105646.7}

Equation (L-105646.5) therefore implies

\[
\boxed{
\left|
\int H\,d\nu_\rho(H)
-2\gamma(1-\log2)
\right|
<{3\gamma\over100}.
}
\tag{L-105646.8}

Thus a zero at height `gamma` assigns its current owner mass around the
universal scale `2(1-log 2) gamma`, with an absolute mean error below
`0.03 gamma`.

## 5. Packet consequence

For a finite multiset of Xi-prime zeros, sum the individual owner measures.
The total mass remains the multiplicity count, and every normalized component
obeys the same universal three-percent law. No zero-specific saddle, local gap
or horizontal spacing enters.

This gives a source-owned, positive replacement for the formerly arbitrary
choice of a descent scale: each zero comes with an almost universal canonical
height distribution.

## 6. Relevance to the final transfer

`HOWNXFER105644` may now be attacked against the explicit reference density

\[
{2\gamma\over(2\gamma-H)^2}
\]

rather than against an unknown positive measure. The actual source changes the
survival law by less than three percent throughout the critical strip.

The remaining difficulty is topological/physical: proving that this positive
owner law is the same signed height flow seen by the Xi-prime all-pass and its
two-trace point evaluation.

## 7. Scope

Kolmogorov closeness of owner measures does not identify individual all-pass
phase jumps, does not remove common-zero or endpoint charges, and does not
prove RH. The theorem supplies an explicit source law for the remaining
transfer; it does not prove the transfer itself.