# T-105640 — Strong Xi log-concavity and the critical-depth collar frontier

Claim ID: `T-105640`  
Status: **MAJOR UNCONDITIONAL SOURCE/LOCALIZATION ADVANCE; HEIGHT-OWNER TRANSFER OPEN**  
Created: 2026-08-25  
Depends on: `T-105620--T-105630`; `L-105640--L-105644`; `R-105640`  
RH status: **unproved**

## 1. Uniform strong log-concavity

The standard positive Xi Fourier kernel satisfies the explicit global bound

\[
\boxed{
-(\log\Phi)''(u)
>{20476\over2345}>8
\qquad(u\in\mathbb R).
}
\tag{T-105640.1}

The proof is a self-contained theta-mixture argument. The first theta orbit has
probability greater than `200/201`; its negative curvature absorbs the complete
score variance with the retained rational margin `5119/7000`.

This is a uniform second-order source theorem. It is not `TP_infinity` and does
not imply RH by itself.

## 2. The current–Turán ratio has an exponential envelope

At total analytic height `H`, define

\[
R_H(\xi)
={H e^{-H\xi}\Lambda_2(\xi)\over\widehat J_H(\xi)},
\qquad \xi\ge0.
\]

The exterior-square conditional law gives exactly

\[
R_H(\xi)
={e^{-H\xi}\over
 \displaystyle\mathbb E
 {\sinh(2HX_\xi)\over2HX_\xi}}.
\]

Consequently

\[
\boxed{0<R_H(\xi)\le e^{-H\xi}.}
\tag{T-105640.2}

For a base `b` and microscope scale `h`, with `H=b+h`,

\[
\boxed{
0<r_{b,h}(\xi)
\le {h\over H}e^{-H\xi}.
}
\tag{T-105640.3}

Together with T105630, the canonical profile is both monotone and
exponentially enveloped.

## 3. Exact model-space price of one adverse zero

For a finite inner function `B`,

\[
\boxed{
\operatorname{tr}_{K_B}M_{e^{-H\xi}}
={1\over2\pi H}
\int_{\mathbb R}
(1-|B(x+iH/2)|^2)\,dx.
}
\tag{T-105640.4}

For one Blaschke factor at shifted depth `y`,

\[
\boxed{
\operatorname{tr}_{K_{B_y}}M_{e^{-H\xi}}
={2y\over H+2y}.
}
\tag{T-105640.5}

Thus the exponential current metric prices the all-pass model space by a
literal midline inner defect.

## 4. The first anti-inner Xi-prime packet is a soft depth sum

Let `B_(H,T)` be the finite Blaschke product formed by zeros

\[
\rho=\alpha+i\gamma
\]

of `Xi'` with `|alpha|<=T` and `gamma>H`, shifted to depth `gamma-H`. Then

\[
\boxed{
\begin{aligned}
\operatorname{tr}_{K_{B_{H,T}}}M_{r_{H,h}}
&\le {h\over H}
\sum_{\gamma>H}{2(\gamma-H)\over H+2(\gamma-H)}\\
&\le {2h\over H^2}
\int_H^{\beta_1}N_1(T;t)\,dt.
\end{aligned}
}
\tag{T-105640.6}

If `beta_1>0`, `H=beta_1-delta`, `delta<=beta_1/2`, and `h<=H`, then

\[
\boxed{
\operatorname{tr}_{K_{B_{H,T}}}M_{r_{H,h}}
\le {4\delta\over\beta_1}N_1(T;H).
}
\tag{T-105640.7}

Hence every anti-inner packet at fixed vertical depth has a fixed positive
current price. Only a collar whose depths collapse to zero can become
source-cheap.

This sharpens `SAFEDESC105628`: the uncontrolled region is not the entire
strip below `beta_1`; it is the microscopic top collar of the first anti-inner
Xi-prime factors, together with its pointwise/index conversion.

## 5. Binding topological firewall

A simple Blaschke factor always has degree one, but

\[
{2y\over H+2y}\longrightarrow0
\qquad(y\downarrow0).
\]

Therefore small current charge cannot itself remove a boundary zero. The soft
depth theorem localizes the obstruction but does not close it.

The remaining fixed-height collar statement is

```text
BCOLLAR105643 — boundary-collar index conversion

Use the complete current hierarchy, signed all-pass index and confluent
endpoint ledger to convert the source-cheap anti-inner collar into a
nonpositive signed charge or a pointwise two-trace inequality.
```

## 6. Every zero nevertheless owns one positive unit across height

For one Xi-prime zero

\[
\rho=\alpha+i\gamma,
\]

define

\[
Q_\rho(H)
=2(\gamma-H)
\int_0^\infty
R_H(\xi)e^{-2(\gamma-H)\xi}\,d\xi
\qquad(0\le H<\gamma),
\]

and `Q_rho(H)=0` for `H>=gamma`.

The current profile decreases both in total height and in frequency. The
normalized exponential model vector moves stochastically to higher frequencies
as `H` approaches `gamma`. Consequently

\[
\boxed{
Q_\rho(0)=1,
\qquad
Q_\rho(H)\downarrow0
\text{ as }H\uparrow\gamma.
}
\tag{T-105640.8}

Therefore

\[
\boxed{d\nu_\rho(H)=-dQ_\rho(H)}
\tag{T-105640.9}

is a positive probability measure on `[0,gamma]`. For every finite packet,

\[
\boxed{
\left(\sum_\rho m_\rho\nu_\rho\right)([0,\infty))
=\sum_\rho m_\rho.
}
\tag{T-105640.10}

Thus the apparently lost integer degree of a shallow zero is not absent from
the current metric: it is distributed as one positive unit across descent
heights. A zero can be cheap at one height only by concentrating its owner mass
in a shrinking interval.

This supplies the common positive object sought by the pointwise and shell
routes:

```text
HOWNXFER105644 — height-owner transfer

Identify the positive current-height owner measure with the signed height flow
of the physical all-pass, retaining point evaluation, common-zero confluence
and the endpoint ledger.
```

## 7. Updated implication matrix

```text
standard Xi kernel uniformly strongly log-concave     PROVED / REVIEW
current/Turan profile monotone in frequency            PROVED / REVIEW
current/Turan profile decreasing in height             PROVED EXACT
current/Turan profile exponentially enveloped          PROVED EXACT
safe Xi-prime allpass innerness above beta_1           PROVED / REVIEW
source-owned phase descent to beta_1                   PROVED / REVIEW
one-zero exponential model-space charge                PROVED EXACT
finite anti-inner packet soft-depth bound               PROVED EXACT
fixed-depth adverse packet                              PAID
small weighted charge -> zero exclusion                 REFUTED
one-zero current-height owner probability               PROVED EXACT
HOWNXFER105644 height-owner/allpass transfer             OPEN / RH-BEARING
BCOLLAR105643 fixed-height collar conversion             OPEN / RH-BEARING
POINTID105630 physical point evaluation                 OPEN / RH-BEARING
ENDIDX105630 cofinal endpoint/index ledger              OPEN
Riemann Hypothesis                                      UNPROVEN
```

## 8. Scope

The theorem gives a quantitative localization and a positive scale-resolution
of the first anti-inner event. It does not identify the sum of one-zero owner
measures with a nonorthogonal packet Gram at each height, does not prove the
height-owner transfer, and does not prove RH. The strong-log-concavity and
innerness proofs remain marked for independent hostile review.