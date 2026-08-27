# Anchor-renormalized shifted-zero flow and the scalar outer-phase frontier

Date: 2026-08-24  
Programme: PR #729  
Scientific status: **RH unproved**

## Remote audit

Before this continuation, PR #729 was read back at exact head

```text
c47b7d5d8917b96e97687cfc8a516e58f523b0ca
```

and was open, draft and mergeable. The corrected `T-105410` physical-width
firewall, the moving-saddle files `L-105413--L-105415`, their addendum/report,
and the exact `X-105410` result were fetched from that exact head.

## The new identity

For

```text
E_alpha=F'-alpha F,
M_alpha=E_alpha/E_(-alpha),
```

remove the moving central zero in the even case. The resulting tangent is

```text
d_alpha log M_alpha^sharp|_0=-2 mhat_F.
```

For every polynomial `q` and `a=0,1`, choose the inverse-power primitive with

```text
Psi_(q,a)'(z)=z^(-2a-2) q(z^-2)^2.
```

Then

```text
(1/2) d_alpha [ contour Psi d log M_alpha^sharp ]|_0
   = q^T S_(k,Omega)^(a) q.
```

The oriented motion of the noncentral shifted zeros contributes `-q^T Cq`.
The residue of the test at the source anchor contributes `q^T Aq`. Their sum
is the boundary reserve `q^T(A-C)q`.

Thus:

```text
source-critical capacity
boundary Stieltjes hierarchy
all-packet boundary Loewner positivity
anchor-renormalized oriented shifted-zero flow
```

are one exact object.

The first scalar test `q=1,a=0` is precisely `ZCAP105412`.

## The scalar harmonic reduction

Assume every critical pole is real and has nonpositive residue. Then `F/F'` is
holomorphic in the upper half-plane and has nonnegative imaginary singularity
at every real pole.

If on one cofinal outer boundary

```text
inf Im(F/F') >= -epsilon_R,
epsilon_R -> 0,
```

the harmonic minimum principle gives

```text
Im(F/F') >= 0
```

throughout the upper half-plane. Hence `F/F'` is Pick. Its Herglotz
representation has one nonnegative affine coefficient and exactly the positive
critical atoms. All boundary Stieltjes matrices follow automatically, and a
nonreal zero of `F` is impossible.

Equivalently,

```text
d_alpha arg M_alpha^sharp|_0=-2 Im(mhat_F),
```

so the all-packet boundary gate becomes one scalar oriented phase velocity on
the outer boundary.

## Cross-program leverage

The independent oriented-ratio programme already proves that:

- this alpha tangent is the reciprocal `F/F'` source;
- the functional equation folds the left safe line onto the right;
- common factors cancel confluently;
- the omitted reciprocal Dirichlet tail is power-saving;
- frozen real tangent coefficients have one global sign; and
- one-sided Hardy support produces an explicit strict phase gap.

The remaining source statement is therefore a physical smooth-frame estimate
for one folded outer phase velocity, with archimedean, horizontal, pole,
freezing and taper errors kept below the explicit gap.

## Exact frontier

```text
anchor-renormalized flow identity             PROVED EXACT
central even branch correction                PROVED EXACT
all matrix tests = all flow tests             PROVED EXACT
signed poles + scalar outer phase -> Pick      PROVED EXACT
Pick -> ZCAP, BRP and real zeros               PROVED EXACT
terminal high-derivative phase                 PROPOSED / REVIEW REQUIRED
complete low-order critical sign               OPEN
source-owned outer phase velocity              OPEN
Riemann Hypothesis                             UNPROVEN
```

## Replay

```text
PASS_X_105416_ANCHOR_ORIENTED_FLOW
91 exact rational checks
b6798c3b111efb1b8f6b90ae5eafb0291e2704bf7712710fb3e604cb175dfdeb
```
