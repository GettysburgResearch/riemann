# T-98010 — Zero-marginal Lorenz collapse and the one-switch root frontier

Claim ID: `T-98010`  
Status: **UNCONDITIONAL STRUCTURAL ADVANCE; ARITHMETIC ROOT AND TARGET PRODUCERS OPEN**  
Created: 2026-08-18  
Frozen base: PR #596 at `40bfd7e70521f4205e95d3960812a6cef6073c05`  
Compared exact inputs: PRs #589, #591, #594, #595, #597  
RH status: **unproved**

## 1. What is closed

The canonical unsieved scalar-to-target marginal

\[
\vartheta(Y)={Q_*(Y)\over4\sqrt Y-3}
\]

is zero through `Y=2`, then strictly increases to `6`. Therefore every positive Lorenz hinge has one source-index switch. For a finite prime state,

\[
\prod_{p\mid P}(I-p^{-1/2}U_p)(Q_*-\lambda T)_+
\]

is an integral of the explicit target prefixes

\[
4\sqrt X\sum_{d<K}{\mu(d)\over d}
-3\sum_{d<K}{\mu(d)\over\sqrt d}.
\]

No arbitrary source subset remains after ordering by the true marginal ratio.

Independently, for any finite paired source, the complete Lorenz dual has its global minimum at the zero hinge exactly when

\[
T_E^+\le T_O\le T_E,
\]

where `T_E^+` is the target carried by even atoms with positive scalar. Under this target sandwich,

\[
D^+(\lambda)\ge0\ \forall\lambda
\iff
D^+(0)=R_E-R_O\ge0.
\]

## 2. Canonical arithmetic names

Define the following two source-faithful statements.

### Zero-Marginal Target Sandwich 67 (`ZMTS67`)

At every sufficiently large completed factor-67 root state,

\[
\boxed{
T_E^+(X)\le T_O(X)\le T_E(X).
}
\tag{T-98010.1}
\]

For the canonical dictionary, the positive-scalar even atoms are exactly those with source index `k<X/2`. Equivalently,

\[
0\le\mathcal T_X\le\mathcal Z_X,
\]

where `mathcal T_X` is the signed complete target and `mathcal Z_X` is the even target in the zero-scalar band `X/2<=k<=X`.

### One-Switch Target Prefix 67 (`OSTP67`)

For every active finite future-prime state and every threshold `Y>=2`,

\[
\boxed{
\mathcal T_P(X;Y)
=4\sqrt X\sum_{d<X/Y}{\mu(d)\over d}
-3\sum_{d<X/Y}{\mu(d)\over\sqrt d}
\ge0,
}
\tag{T-98010.2}
\]

with the exact divisor restrictions and source ownership of the state retained.

`OSTP67` is a strong sufficient theorem for all nonnegative Euler-minus hinges. It is not asserted to be necessary.

## 3. Exact implication graph

Let `GPC67` / `RBLPTE67` denote eventual nonnegativity of the native root zero-hinge scalar. Then

\[
\boxed{
\mathrm{ZMTS67}+\mathrm{GPC67}
\Longrightarrow
\mathrm{CPSL67}.
}
\tag{T-98010.3}
\]

Also

\[
\boxed{
\mathrm{OSTP67}
\Longrightarrow
\mathrm{GPC67}.
}
\tag{T-98010.4}
\]

The retained Mellin-Landau theorem gives

\[
\boxed{
\mathrm{GPC67}\Longrightarrow\mathrm{RH}.
}
\tag{T-98010.5}
\]

Thus either of the following would close the route:

```text
OSTP67;

or

ZMTS67 + the native root zero-hinge estimate GPC67.
```

However, `GPC67` alone already implies RH. Therefore the genuinely minimal conclusion-producing theorem remains the root scalar; the nonzero Lorenz hinges are now classified as a target-only strengthening rather than an independent analytic bottleneck.

## 4. Relation to the live Type-II routes

The one-switch representation exposes only two prefix moments. Any proposed bridge to PR #590's `BLPTE67`, PR #595's fifteen Q4 moments, or PR #597's reciprocal-zeta-square resonance must provide an exact identity from its kernel to

\[
\sum_{d<K}{\mu(d)\over d}
\quad\text{and}\quad
\sum_{d<K}{\mu(d)\over\sqrt d},
\]

including the strict cutoff, real activation side, installed-prime set, and boundary terms. Similarity of Type-II geometry is not enough.

At the zero hinge, the positive Lorenz cushion vanishes. PR #596's fixed-angle no-go remains binding: no fixed positive multiple of unsigned mass can replace the signed root profile.

## 5. Exact finite falsifiers

A finite failure of `ZMTS67` is one of two target witnesses:

```text
T_O > T_E                       target-capacity ray;
T_E^+ > T_O                     positive-marginal oversupply.
```

A finite failure of a nonnegative hinge has a one-switch separator:

```text
endpoint X;
future-prime state P;
source cutoff d<X/Y_lambda;
the two prefix moments;
negative directed target-prefix or hinge value.
```

No general LP coefficient vector is needed.

## 6. Honest boundary

```text
ordered scalar/target marginal                    PROVED
all Lorenz active sets are one-switch             PROVED
layer-cake target-prefix representation            PROVED
zero-marginal target-sandwich criterion             PROVED EXACT
ZMTS67 arithmetic validity                          OPEN
OSTP67 arithmetic validity                          OPEN / STRONG
native root scalar GPC67 / RBLPTE67                 OPEN / RH-BEARING
fixed positive mass aperture                        REFUTED BY PR #596
SACF classical subexponential gain                  RETAINED / INSUFFICIENT
Riemann Hypothesis                                  UNPROVEN
```

This packet removes the continuous Lorenz geometry from the list of mysteries. It does not relabel either target-prefix cancellation or the root Möbius cancellation as proved.
