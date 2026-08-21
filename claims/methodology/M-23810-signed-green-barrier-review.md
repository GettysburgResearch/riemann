# M-23810 — Review protocol for the signed Green quotient barrier

Methodology ID: `M-23810`  
Title: Fail-closed review of Green neutralization, signed cell balayage, and the source-bound quotient-layer barrier  
Status: **PROPOSED REVIEW AND PRODUCTION PROTOCOL**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238

## 1. Purpose

The prior two-contact proposal is no longer the review target. A scalar affine
interval having two endpoints does not bound the number of arithmetic source
coordinates feeding it.

The replacement proposal separates:

```text
exact finite Green orthogonalization;
exact zero-cost signed cell transport;
one source-specific lower-scale scalar barrier;
a complete conditional deduction to RH.
```

A reviewer should attack `SGQB(K)` directly rather than enumerate terminal
contacts.

## 2. Frozen exact interfaces

A production packet must bind immutable versions of:

```text
carry/divisor-gradient identities          PR #248
signed divisor-gradient consumer           PR #248 L-24508
endpoint-projected Dirichlet Gram           PR #248 L-24509
proper-prime-power reduction               PR #248 L-24517
green orthogonal neutralization             L-23820
zero-cost signed cell balayage               L-23821
high-order complete-lattice Euler           PR #158
fixed-ratio shell and all-ratio filters      PRs #229/#234/#236
square-screw/rightmost-zero transfer         PR #202
```

No status of an imported full proposal is inherited.

## 3. Exact finite Green certificate

For each finite endpoint, export:

```text
complete constraint index set
exact rational or outward interval Gram G
logarithmic vector lambda
complete signed residual r
E=lambda^T G lambda
delta=lambda^T r
r_perp=r-(delta/E)G lambda
T_perp=G^-1 r_perp
checks G T_perp=r_perp and lambda^T r_perp=0
new residual (delta/E)G lambda
exact zero objective change
```

The checker must reject any omitted residual coordinate or a correction whose
objective is merely small rather than exactly zero.

## 4. Exact signed balayage certificate

For every quotient cell, export:

```text
ordered ordinary-prime endpoints
complete signed residual at every point
cell total mass
cell logarithmic moment
left and right endpoint charges
the two incidence blocks for every interior point
exact final endpoint vector
exact zero objective cost
```

The transport amounts may be negative. A consumer must reject a proof that
inserts a positive part before computing the two moments.

## 5. `SGQB(K)` production object

One proof object for `L-23822` contains:

```text
fixed K and reserve eta
complete source-bound quotient-cell dictionary
all Mobius/resolvent words and coefficients
frozen-complement cell assignment
all cutoffs and transition surfaces
full signed destination recombination
green-orthogonal correction ledger
two-moment balayage ledger
lower-scale source maps and destinations
nonnegative scalar recurrence coefficients
polylogarithmic unmatched boundary budget
fixed-ratio Mertens shell channel
canonical input/output hashes
```

The consumer reconstructs the vector identity before accepting the scalar
recurrence.

## 6. Mandatory mutations

### 6.1 Rank-`K` same-sign cube

Inject the complete PR #239 cube. The source rank and number of products must
remain unchanged until Green projection and signed cell balayage. Reject any
certificate which claims the cube has bounded arithmetic rank.

### 6.2 Zero reserve

Set every proposed reflected Schur reserve to zero. The Green-orthogonal
correction must continue to work because it is an equality. Reject any proof
which needs a hidden positive reserve.

### 6.3 Constraint dipole

Use the PR #254 parabolic residual with macroscopic positive defect and negative
slack. Reject any packet which keeps only the positive defect before transport.

### 6.4 Fixed-ratio shell

Project to the first `2/3` Mertens/Farey cell. The corresponding scalar channel
must appear in the lower-scale or unmatched-boundary ledger with its exact sign.

### 6.5 Source grammar

Mutate one cell assignment so it depends on a live Euler variable. The checker
must reject it. Mutate one lower-scale destination above the declared reserve;
the checker must reject it.

## 7. Automatic rejection conditions

Reject a claimed proof if it:

```text
reintroduces the two-contact source-count theorem;
uses arbitrary packet rank or face dimension as an exponent;
uses total variation before signed recombination;
uses ordinary L2/Green energy to bound the logarithmic scalar;
uses a nonnegative monotone cover;
omits the orthogonal zero-cost correction;
forgets proper-prime-power reduction costs;
proves only finitely many endpoints or packet orders;
obtains an X^c boundary loss with fixed c>0;
uses PNT or a zero-free estimate strong enough to imply the target scalar;
drops the first fixed-ratio Mertens mutation.
```

## 8. Preferred production sequence

1. Review `L-23820` and `L-23821` independently.
2. Emit the exact finite synthetic checker `X-23820`.
3. Export one complete quotient-cell residual for moderate `X`.
4. Apply the rank-`K` same-sign cube mutation.
5. Verify zero-cost Green neutralization and balayage on that object.
6. Construct one full lower-scale source map, not merely a scalar estimate.
7. Close every quotient transition and endpoint term.
8. Prove the polylogarithmic boundary ledger.
9. Replay the scale contraction and square-screw normalization.

## 9. Status discipline

```text
L-23820/L-23821 finite equalities       proposed exact
synthetic rational replay               exact finite control
one finite SGQB packet                  finite evidence only
symbolic/source-bound SGQB(K)            RH-bearing theorem
T-23810 after SGQB(K)                    full proof
```

No finite trend, numerical LP optimum, or low-rank visualization proves
`SGQB(K)`.
