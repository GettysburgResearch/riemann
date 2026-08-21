# Dyadic two-contact carry proposal after the corrected reflected-normal trace

Date: 2026-08-08  
Agent: `gpt56-pro`  
Branch: `agent/gpt56-pro-262-dyadic-two-contact`  
Primary claims: `L-26201`--`L-26205`, `R-26201`, `T-26201`, `M-26201`  
Status: **NEW FULL PROPOSAL; DYADIC SIGNED SLACK / ODD-LEAKAGE DESCENT OPEN; RH UNPROVED**

## 1. Research objective

The starting instruction was not to review another frozen proposal. It was to
use the corrected two-frequency physical block, trace the exact fixed-`q_0=2`
Möbius source through every coupled cross term, and search for a strict
source-specific contraction. The preferred mechanisms were the parity-comb
identities and signed carry transport, with an explicit instruction to pivot if
either mechanism proved structurally incapable of closing the source.

The resulting route is genuinely different from the earlier terminal-face and
generic balanced-packet proposals.

Its central new fact is:

```text
the complete dyadic Möbius source is exactly two carry contacts,
not merely a packet with at most two conjectural endpoint coordinates.
```

The exact half-scale carry subsystem is also now identified. The remaining
obstruction is one signed odd-column leakage channel, equivalently one bottom
Green dipole.

## 2. Frozen input interfaces

The work uses the following independently scoped interfaces.

1. **PR #241 / `L-9518`.** A physical logarithmic block is represented by a
   two-frequency normal Gram. The earlier one-frequency vertical integral was a
   global exponentially weighted energy and could not localize one block.
2. **PR #158 / `L-15159`.** Fixing the Heath--Brown logarithmic coordinate at
   `q_0=2` leaves an exact translated scalar Möbius source before any norm.
3. **PR #236.** The Euler-aligned dyadic coefficient is
   ```text
   b_2(n)=mu(n)-1_(2|n)mu(n/2),
   ```
   its Dirichlet series is `(1-2^-s)/zeta(s)`, and the dyadic shell has the same
   Hardy abscissa as the Möbius source.
4. **PR #244.** The carry matrix, exact greedy residual, blocker-loss identity,
   and digital-freeze law are finite exact objects.
5. **PRs #248/#254.** The divisor-gradient and signed adjacent-flow calculi are
   exact, but their relation to the fixed dyadic source had not been computed.

No generic BTP theorem, terminal-face count, or unsigned Farey operator estimate
is imported.

## 3. Exact coupled physical normal Gram

Let

```text
alpha_mu = sum_n mu(n)/sqrt(n) delta_(log n),
L        = log 2,
D_2      = I-2^(-1/2) tau_L.
```

Then the dyadic atomic source is exactly

```text
beta_2=D_2 alpha_mu.
```

For any compact physical window `H`, if `Q_mu=H*alpha_mu`, then

```text
Q_2(x)=Q_mu(x)-2^(-1/2)Q_mu(x-L).
```

Therefore one physical block is the complete rank-one two-component normal
form

```text
E_2(J)
 = integral_[J,J+1]
   (Q_mu(x),Q_mu(x-L))^*
   [[1,-1/sqrt(2)],[-1/sqrt(2),1/2]]
   (Q_mu(x),Q_mu(x-L)) dx.
```

Equivalently, all four arithmetic channels are retained:

```text
(m,n), (2m,n), (m,2n), (2m,2n).
```

The corresponding two-frequency multiplier is

```text
1-2^(-1/2-alpha-it).
```

It has no zero in the Hardy counterexample half-plane and has the causal
`ell^1` inverse

```text
sum_(k>=0) 2^(-k/2) tau_(k log 2).
```

Thus the fixed-logarithm Möbius block and the dyadic block have the same upper
exponential status.

This source matrix is positive but rank one. It supplies no fractional-scale
contraction by itself. The arithmetic source must be used.

## 4. Parity-comb attempt and its limit

PR #236 gives a positive parity comb whose convolution with the dyadic shell is
a short three-tap exponential combination. This is a valuable exact factorization.

However, the transform of the parity comb contains the Dirichlet eta function.
A generic coercive inverse estimate across the full Hardy half-plane would
already exclude shifted zeta zeros. Such an inverse cannot be imported as an
independent elementary estimate.

The correct use of the parity structure must therefore exploit the actual
coefficient `b_2`, not merely positivity of the digital kernel.

## 5. Breakthrough: pointwise two-contact carry collapse

For the carry indicator

```text
chi_(n,q)(j)=1_(j mod q > n mod q),
```

Möbius inversion gives

```text
sum_(q<=x) b_2(q) floor(x/q)=1_(x=1).
```

Substitution in the floor representation of the carry yields, for every
`n>=2` and every `0<=j<=n`,

```text
sum_(q=2)^n b_2(q) chi_(n,q)(j)
 = -1_(j=1)-1_(j=n-1).
```

For `n=2` the contacts coincide and the value is `-2`.

This is exact before averaging, before taking a norm, and before any packet
partition.

Consequences include:

```text
sum_q b_2(q) beta_(n,q) = -2/(n+1),
```

and the exact carry-Hermitian energy

```text
(1/(n+1)) sum_j |sum_q b_2(q)chi_(n,q)(j)|^2
 = 2/(n+1)          for n>=3.
```

Using Kummer's theorem with a formal completely additive derivation `L`, the
reflected cross term is

```text
(1/(n+1)) sum_j Y_n(j) L binom(n,j)
 = -2L(n)/(n+1).
```

For the ordinary logarithm, the binomial-square profile decomposes orthogonally
into:

```text
exact dyadic endpoint projection
+ strictly positive interior reserve.
```

This is the first literal source-specific two-contact theorem in the route.
Earlier branches proposed that terminal faces should have two contacts after a
large symbolic recombination; here the original RH-bearing coefficient itself
has two contacts row by row.

## 6. Signed slack and a strictly smaller RH-bearing scalar

For endpoint `X`, target

```text
w_X(q)=q^(-1/2)log(X/q),
```

and any nonnegative feasible carry vector `d`, define

```text
s_X=w_X-B_X^T d,
Pi_2(X;d)=sum_q b_2(q)s_X(q).
```

The rank-one averaged collapse gives exactly

```text
Pi_2(X;d)
 = R_2(X)+2 sum_n d(n)/(n+1),
```

where

```text
R_2(X)=sum_(q=2)^X b_2(q)q^(-1/2)log(X/q).
```

Every feasible nonnegative vector satisfies

```text
sum_n d(n)/(n+1)=O(log^2 X)
```

by the universal square-root carry moment on PR #244.

For the canonical backward greedy vector, final slack satisfies

```text
s_X(n)=((n-1)/(n+1)) ell_X(n),
```

where `ell_X(n)` is the exact off-diagonal blocker loss. Hence

```text
Pi_2^gr(X)
 = sum_n b_2(n)((n-1)/(n+1))ell_X(n).
```

This is a signed parity-weighted blocker debt. It is strictly weaker than total
greedy slack.

The dyadic valuation layers give another exact form:

```text
Pi_2(X)
 = sum_(m odd) mu(m)
   [s_X(m)-2s_X(2m)+s_X(4m)].
```

Thus affine or nearly affine unsigned slack along dyadic chains is harmless.

## 7. Mellin implication

The Mellin transform is

```text
integral_1^infinity R_2(X) X^(-z-1)dX
 = [ (1-2^(-z-1/2))/zeta(z+1/2) - 1 ] / z^2.
```

A subpower estimate for `R_2` makes this holomorphic in `Re z>0`. A zeta zero
with real part greater than one half would produce a genuine pole; the dyadic
numerator has zeros only on the line `Re s=0` and cannot cancel it.

Therefore

```text
Pi_2^gr(X)=O_epsilon(X^epsilon) for every epsilon
```

implies RH.

This is the **Dyadic Signed Slack theorem (DSS)**. It is the sole logical hinge
of the new proposal.

## 8. Attempted bridge to signed adjacent transport

The natural next attempt was to use the signed adjacent-flow calculus of PR #254.
For

```text
v_q(b)=sum_m b(m)[1_(q|m)-1_(q|m-1)],
```

the dyadic projection collapses to

```text
sum_q b_2(q)v_q(b)=-2b(2)+b(3).
```

Under the adjacent correction

```text
b_F(m)=b(m)+F_(m-1)-F_m,
```

the projected change is exactly

```text
3F_2-F_3.
```

Every flow supported at indices `j>=4` is invisible.

This refutes the direct proof pattern

```text
repair high-scale constraint defect cheaply
-> descend generated children below half scale
-> conclude contraction of the fixed-q0=2 Möbius source.
```

High-scale transport may be useful for the orthogonal constraint ledger, but it
cannot alter the dyadic scalar until the accumulated charge reaches the bottom
coordinates. The proof must contain an explicit bottom-charge telescope.

## 9. Two-charge Green form

Retain all divisor coordinates `2,...,X` and form the unprojected divisor-gradient
Gram

```text
Gbar_X(q,d)=sum_j Delta 1_(q|j) Delta 1_(d|j).
```

It is positive definite. The dyadic source has divisor profile

```text
0 at 1,
-2 at 2,
-1 from 3 onward.
```

Therefore

```text
Gbar_X b_2 = -3e_2+e_3,
b_2^T Gbar_X b_2 = 5.
```

The exact inverse is

```text
Gbar_X^-1(a,b)
 = sum_(d|a,e|b) mu(a/d)mu(b/e)min(d,e).
```

For any residual `s` and potential `T=Gbar_X^-1 s`,

```text
sum_q b_2(q)s(q)=-3T(2)+T(3).
```

Thus DSS is precisely the two-coordinate theorem

```text
|-3T_X(2)+T_X(3)|=X^o(1).
```

A full Green-energy bound is sufficient by Cauchy--Schwarz, but unnecessary.
Large Green energy orthogonal to this fixed dipole is harmless.

## 10. Exact half-scale subsystem

A strict fractional-scale mechanism does exist inside the carry matrix.
Pointwise,

```text
chi_(2n+1,2q)(2j+epsilon)=chi_(n,q)(j),
epsilon in {0,1}.
```

Consequently

```text
beta_(2n+1,2q)=beta_(n,q),
```

and the associated Hermitian row is an exact isometry.

For endpoint `X=2Y+1`, lifting a lower nonnegative vector by

```text
d_up(2n+1)=2^(-1/2)d_Y(n)
```

gives an exact half-scale copy on every even column. Its residual is

```text
s_up(2q)
 =2^(-1/2)s_Y(q)
  +(2q)^(-1/2)log((2Y+1)/(2Y)).
```

The second term is explicit and tiny.

The only digital obstruction is the contribution of the lifted vector to odd
columns. This **odd-column leakage** is the natural production target for a
Parity Blocker Descent proof. The three dyadic valuation layers pair one odd
parent channel with two exact even descendants.

A valid Odd-Leakage Descent theorem would reconstruct

```text
Pi_2(2Y+1)=Pi_2(Y)+polylogarithmic forcing
```

or a corresponding one-sided half-scale inequality, after every feasibility
correction is included.

## 11. Full proposal

The new chain is:

```text
correct two-frequency physical block
-> fixed-q0=2 exact Möbius source
-> zero-safe dyadic difference and complete 2x2 normal Gram
-> exact two-contact carry source
-> parity-weighted greedy blocker residual
-> exact half-scale even-column subsystem
-> Odd-Leakage / Parity Blocker Descent
-> Dyadic Signed Slack
-> dyadic Riesz Mellin holomorphy
-> RH.
```

A fail-closed sufficient recurrence is

```text
|Pi_2^gr(X)|
 <= C log^A(2X)
    + max_(Y<=(X+1)/2)|Pi_2^gr(Y)|.
```

Iteration gives a polylogarithmic bound and hence DSS.

The production certificate must emit the blocker forest, every dyadic chain,
all truncations, same-scale cluster solves, child endpoints, bottom charges,
and exact parent-child equality before absolute values.

## 12. Exact regression and reconnaissance

`X-26201` retains three exact proof objects.

```text
core dyadic/carry/Green algebra
SHA-256
  dd6f66f1e026178c1277f2fa634671d8868219e0303db505d9f0547df5eb0715

bottom-charge and high-index-flow invisibility
SHA-256
  395a7a89ea2267cfa5a3b805ead2646fa46a1761408f6ff048fed7b2e218757f

odd-row/even-column digital isometry
SHA-256
  17e23d1e2ebc01cc7283d125c15c721d4743e69f906b17b715294f60b0e09b23
```

The tests cover:

- 13,038 pointwise carry-contact cells;
- 12,879 averaged affine rows;
- exact Kummer cross terms;
- Green inverses through dimension 17;
- bottom-flow mutations;
- 3,780 digital duplication cells;
- 60 exact Hermitian lift rows;
- rejection of the incorrect even-row scaling mutation.

A 60-digit finite reconnaissance found every nonterminal exact carry-inverse
coefficient positive through endpoint 5000. Its digest is

```text
7a249c5a00cb1e5c6daa0434bcbdc40efef890f381f2ae1eb52091e8557f001e.
```

That evidence is discovery only. It does not prove Carry Saturation, DSS, PBD,
or RH.

## 13. Honest status

```text
correct coupled normal source trace       PROPOSED EXACT
dyadic two-contact carry theorem          PROPOSED COMPLETE
two-charge Green theorem                  PROPOSED COMPLETE
high-index transport invisibility         PROPOSED COMPLETE
exact digital half-scale subsystem        PROPOSED COMPLETE
Odd-Leakage / PBD                          OPEN
Dyadic Signed Slack                       OPEN, RH-BEARING
DSS -> RH                                 PROPOSED COMPLETE
Riemann Hypothesis                        UNPROVED
```

The remaining theorem is no longer an unnamed critical correlation estimate, a
growing terminal-face enumeration, all balanced Type-II packets, total greedy
slack, or full Green energy. It is one explicit signed scalar, with one exact
half-scale subsystem and one precisely isolated odd-column leakage channel.
