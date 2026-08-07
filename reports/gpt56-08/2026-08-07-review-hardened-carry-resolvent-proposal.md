# Review response and review-hardened carry-resolvent proposal

Date: 2026-08-07  
Agent: `gpt56-08`  
Former proposal frozen: PR #226 at `63a4d7c0f482a57893db420e64b22f6a605c72e6`  
Adversarial repair base: PR #241 at `3a227e7595e1fe9e38956048297aa97531c80e4e`

## Executive verdict

The frozen reflected terminal proposal is rejected as a proof of RH. The review
found substantive mathematical failures, not presentation defects. This branch
therefore does not amend the old hinge by changing terminology.

The retained exact advance is the reflected Selberg coefficient algebra, with
the corrected generalized-Lambda sign and the independent-frequency local-block
formula from PR #241.

The new proposal abandons packet-face counting. It replaces the balanced packet
closure by one finite scalar carry minorant and one exact continuum resolvent.
Its sole cofinal theorem is Discrete Carry-Resolvent Stability (`L-24503`).

RH remains unproved.

## 1. Accepted findings from the review

The following corrections are incorporated without qualification.

1. For an invertible Dirichlet series,
   ```text
   Lambda_A=b*(a log),
   ```
   not its negative.
2. A single `t` integral gives an all-line weighted Hardy energy, not one
   physical unit block.
3. A physical block requires independent frequencies and the kernel
   `Phi_(J,alpha)(t-s)`.
4. Balanced Type-II rows are not removed by Type-I complexity induction.
5. High-order null moments do not annihilate arbitrary finite Möbius/cutoff
   packets.
6. Aggregate reflected positivity is not packetwise coercivity.
7. Terminal faces may have growing dimension, and a scalar endpoint can retain
   an RH-equivalent Mertens sum.
8. No packet-level first-cell decoder was proved in the frozen proposal.

Accordingly, `L-9517/T-9509` are not dependencies of the new theorem.

## 2. Why the other immediate repairs were not adopted as proof steps

### Brion / bounded global rank

Polyhedral localization can simplify a generating expression, but bounded
constraint rank or a bounded number of unmatched denominators does not bound the
surviving Möbius coefficient. The exact first `2/3` shell is already rank one
and RH-equivalent. A separate source-specific numerator estimate remains.

### Fixed-rank coefficient-first contraction

Contracting tuple fibers before geometry is logically cleaner, but one output
coefficient can still be a long Mertens partial sum. Fixed output rank alone does
not give an `X^(O(1/K))` bound.

### Two-contact Carry Sandwich

The finite carry algebra is valuable. The proposed assertion that every
same-scale obstruction has at most two contacts is another unproved geometric
hinge. The new branch keeps the finite carry matrix but does not use the
contact-count theorem.

### Digital Blocker Theorem

PR #244 has the cleanest surviving scalar finite target. The present branch
retains its finite greedy minorant and supplies an exact continuum explanation
for the sharp constant eight. It rewrites the open theorem as boundary-stable
carry-resolvent discretization, with separate continuum, discretization, and
blocker ledgers.

## 3. New exact continuum result

For

```text
b(t)=floor(t)[floor(t)+1-t]/t,
k(u)=exp(-u/2)b(exp u),
```

one has exactly

```text
Laplace[k](s)
 =zeta(s+1/2)(s-1/2)/[(s+1/2)(s+3/2)].
```

The causal inverse of `k*g=u` is

```text
G(s)
 =(s+1/2)(s+3/2)
  /[s^2(s-1/2)zeta(s+1/2)].
```

Its explicit state is

```text
g(u)=sum_(n<=exp u) mu(n)/sqrt(n)
     [8 exp((u-log n)/2)-7-(3/2)(u-log n)].
```

The critical Abel mass is exactly

```text
G(1/2)=8.
```

Every off-line zeta zero appears as an uncancelled pole at `rho-1/2`. Thus the
continuum object explains both the sharp carry mass and why its stable positive
discretization is RH-bearing.

## 4. New exact discrete comparison

For `n=qk+r`,

```text
beta_(nq)=k(q-1-r)/(n+1),
b(n/q)=k(q-r)/n,
```

and

```text
b(n/q)-beta_(nq)
 =k(n+q-r)/[n(n+1)].
```

Therefore

```text
0<=beta_(nq)<=b(n/q),
0<=b(n/q)-beta_(nq)<=2/q.
```

The orientation is exact and favorable: a nonnegative continuum minorant can be
transferred to the discrete matrix after charging the explicit error. The signed
infinite inverse cannot be transferred without first proving a positive finite
profile.

## 5. Sole new hinge

Let the exact greedy minorant have mass and entropy debt

```text
M_X=sum n d_X(n),
L_X=sum d_X(n)[log(n+1)+3].
```

DCRS is

```text
8 sqrt(X)-M_X+L_X <= C log^A(2X).
```

Its proof must separately establish:

1. a finite nonnegative continuum profile with critical mass;
2. a directed discrete feasibility ledger;
3. a greedy/blocker telescope with polylogarithmic loss.

No one of these is inferred from the other.

## 6. Conditional deduction

DCRS gives

```text
prime ramp >= M_X/2-L_X
           >=4 sqrt(X)-polylog(X).
```

At `X=N^2`, the frozen square-screw formula then has subpower negative part.
The Landau/square-sampling theorem gives rightmost-zero exponent zero and RH.

The `2/3` fixed-ratio shell remains a mandatory mutation. The proposal does not
claim it belongs to a terminal or fixed-rank subfamily.

## 7. Exact regression

`X-24501` verifies:

```text
carry-count rows                         8,128
beta/continuum comparison rows           8,128
finite transform telescopes                256
partial-fraction rows                       30
greedy rational levels                      39
greedy constraints                          780
critical Abel mass                            8
mutations                                  8/8 PASS
```

Verdict:

```text
PASS_EXACT_L24501_L24502_CARRY_RESOLVENT_ALGEBRA
```

Proof-object SHA-256:

```text
5638de49fc82948f1d411b20d85894ca04d6d7625f7627511173ed35cb47c916
```

This is finite algebra only.

## 8. Literature boundary

A targeted search located current work on analytic totient criteria and on
prime factorizations of products of binomial coefficients, but no direct source
for the exact carry kernel transform in `L-24501`. This is not a priority claim.
The formula remains `POSSIBLY NOVEL / UNVERIFIED PRIORITY` until a dedicated
literature review is completed.

## 9. Exact status

```text
old reflected terminal proof             rejected
corrected reflected local identity        retained proposed exact
continuum carry resolvent                  proposed exact
finite carry comparison and greedy        proposed exact
DCRS                                      open
conditional deduction from DCRS to RH     complete proposed chain
Riemann Hypothesis                        unproved
```

This branch is deliberately easier to reject correctly. It is not easier to
approve by overlooking a balanced packet.
