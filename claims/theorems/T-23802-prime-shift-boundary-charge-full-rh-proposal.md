# T-23802 — Prime-shift boundary-charge proposal: corrected disposition

Claim ID: `T-23802`  
Status: **REFUTED AS A DIRECT NO-DOUBLE-SPEND MECHANISM; GLOBAL PRIME-SHIFT POSITIVITY REMAINS OPEN**  
Depends on: `L-23804`, `L-23805`, `L-23807`, `L-23808`, `R-23802`, `R-23803`, `L-23809`  
RH status: **UNPROVED**

## 1. Corrected disposition

The exact prime-shift state remains

\[
G(t)=\sum_{n\le e^t}\mu(n)h_0(t-\log n),
\qquad
h_0(t)=\left(e^t-\frac78e^{t/2}-\frac3{16}te^{t/2}\right)\mathbf1_{t\ge0}.
\]

On every open quotient layer it satisfies

\[
(\partial-1)(\partial-1/2)^2G=0,
\]

and its knot jump at `log n` is exactly `mu(n)/8`.

The local identity

\[
1=\sum_{p\mid n}\frac{\log p}{\log n}
\]

for `mu(n)=-1` gives a correct convex decomposition of each negative *birth* onto positive half-scale parents.

However, the proposed global no-double-spend Boundary Charge Transport theorem is false.

## 2. Exact refutation of BCT

For a prime child `n=p`, the unique declared parent is the root `1` and the routing weight is one. Hence at horizon `X` the root would have to pay

\[
D_1(X)=\sum_{p\le X}h_0\!\left(\log\frac Xp\right).
\]

Using the exact reserve `h_0(log y)>=y/8`,

\[
D_1(X)\ge\frac X8\sum_{p\le\sqrt X}\frac1p.
\]

The reciprocal-prime sum diverges, while the available root trajectory satisfies

\[
h_0(\log X)<X.
\]

Thus `D_1(X)>h_0(log X)` for all sufficiently large `X`. This is `R-23803`.

Therefore negative prime trajectories cannot be paid independently from the root before the positive semiprime and higher even-parity generations are recombined.

## 3. What survives

The following statements are retained:

```text
prime-shift / Mobius identity                       exact
three-state quotient-layer ODE                      exact
knot jump mu(n)/8                                   exact
local half-scale parent decomposition               exact
generic arbitrary-shift B-spline positivity         refuted by R-23802
direct no-double-spend BCT                          refuted by R-23803
pointwise G(t)>=0 / GCF                             open
RH                                                   unproved
```

Any future boundary proof must be **generation-netted**: odd and even Möbius generations must be recombined before a positive capacity estimate is imposed.

## 4. FGCM is not a boundary-escape workaround

`L-23809` proves that the stated sharp `FGCM` theorem cannot evade global factor positivity by moving mass to the finite horizon.

The local positivity of the carry kernel forces uniform exponential tightness of every FGCM family. If the positive mass tends to one, a weak limit exists with total mass one. Critical Mellin-mass conservation then forces the limiting convolution inequality to be equality, and the limit has exactly the Gamma/carry quotient transform `A(s)`.

Thus, at the stated sharp mass level,

```text
cofinal FGCM  ->  global positive Gamma/carry factor.
```

This does not refute FGCM, but it removes the claim that the moving endpoint by itself supplies a genuinely weaker positivity mechanism.

## 5. Correct elementary frontier

After the two refutations, the prime-shift branch has one honest frontier:

> Find a source-specific **signed generation-netted identity** for the actual Möbius Boolean lattice which proves `G(t)>=0`, or abandon global Gamma-factor positivity and use a different elementary certificate whose sharp mass does not compactify back to GCF.

A valid generation-netted proof must preserve the alternating prime/semiprime/higher-generation cancellation. It may use:

1. complete prime blocks before taking signs;
2. exact Selberg or square identities tied to the physical carry source;
3. a signed parabolic defect-to-slack flow in which positive and negative residuals are transported simultaneously;
4. a finite certificate with a genuinely weaker mass target than `L-23807`, together with a separately proved sharp entropy recovery.

Merely rephrasing `G>=0` as a new scalar criterion is not a completion.

## 6. Review instructions

Reviewers should now treat `T-23802` as a **refuted mechanism with retained exact lemmas**, not as a live full proof proposal.

The fastest checks are:

- replay `R-23803` on the prime-child root channel;
- replay the tightness argument in `L-23809`;
- reject any repair that spends root capacity before semiprime reimbursement;
- reject any claim that finite-horizon mass can escape to infinity under the current FGCM convolution constraint.

## Exact proof boundary

```text
prime-shift state / quotient ODE             exact
local parent identity                        exact
generic B-spline mechanism                   refuted
direct BCT capacity mechanism                refuted
FGCM boundary-escape distinction             removed by compactness
signed generation-netted GCF proof           OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```
