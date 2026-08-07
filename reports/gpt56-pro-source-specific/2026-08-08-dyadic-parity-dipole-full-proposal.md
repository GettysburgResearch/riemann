# Source-specific full attack: dyadic parity dipole, reflected Hall, and positive carry transport

Agent: `gpt56-pro-source-specific`  
Date: 2026-08-08  
Status: **FULL PROPOSAL PENDING ADVERSARIAL REVIEW; RH IS NOT CLAIMED PROVED**

## Executive conclusion

The coefficient-first and Brion programmes supplied one durable lesson:

```text
recombine the complete signed arithmetic source before estimating it.
```

Their universal closures did not survive exact review.  Same-sign Möbius
hypercubes remain; a polyhedral line is not automatically an arithmetic
difference; absolute resonance rank can grow; and the diagonal reflected
Selberg integral is not a physical logarithmic block.

The strongest replacement I found is genuinely source specific.  Apply the
minimal dyadic polynomial

\[
 (1-X)(1-X/2)=1-\frac32X+\frac12X^2
\]

to the Möbius-adjoint carry row.  This produces one four-layer opposite-parity
source

\[
 \omega_2
 =
 \mu-\frac32\tau_2\mu+\frac12\tau_4\mu
\]

with three simultaneous exact faces:

1. its carry image is a compact positive/negative dipole on the factor-four
   interval `[m,4m)`;
2. its binary-digit dual collapses to the three atoms `1,2,4`;
3. its Dirichlet inverse and generalized Selberg prime weights are strictly
   positive.

This is the cancellation the generic geometry lacked: not every line cancels,
but this exact opposite-parity family cancels both affine carry modes.

The new full proposal couples that source to the corrected two-frequency
reflected block and to a positive multiplicative carry transport.  The sole new
hinge is one symbolic identity, **Reflected Dyadic Hall (RDH)**.  It is narrower
than BTP for every packet but still RH-bearing: at the universal logarithmic
Hall witness it is exactly the prime-ramp inequality.

## 1. Frozen live inputs

The proposal was written after inspecting these exact heads:

```text
PR #257  2f508a77a21593c7a8bc852a61e8b19c63367f8b
PR #254  be8405e06bc6c845267727b7347ea91f3593e16b
PR #248  45d327082422021955be81f1a49fde7b646ce1cb
PR #244  c81883549aa15ab16a77b19168647d0d39787f21
PR #241  3a227e7595e1fe9e38956048297aa97531c80e4e
PR #236  f1d51ae13da93a325349229a3701ae9f5f2f348d
```

The relevant live corrections are:

- generic Brion line cancellation is not established;
- absolute bounded resonance rank is false;
- terminal endpoint counting does not control the balanced source;
- the correct local reflected consumer uses independent frequencies `t,s`;
- monotone carry repair costs order `sqrt(X)`;
- the exact Green correction solves equality constraints but need not preserve
  nonnegative carry coefficients;
- Greedy Slack, DCRS, and the continuum carry state are different coordinates
  of the same arithmetic obstruction.

## 2. The exact source

Define

\[
 \omega_2(n)
 =
 \mu(n)
 -\frac32{\bf1}_{2\mid n}\mu(n/2)
 +\frac12{\bf1}_{4\mid n}\mu(n/4).
\]

Its Dirichlet series is

\[
 \Omega_2(s)
 =
 \frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}.
\]

The added Euler factor has no zero in the counterexample half-plane.  The new
source is therefore stably equivalent to the dyadic Mertens shell.

Writing `n=2^nu m`, `m` odd, its exact layers are

```text
nu=0       +1 mu(m)
nu=1       -5/2 mu(m)
nu=2       +2 mu(m)
nu=3       -1/2 mu(m)
nu>=4       0.
```

Unlike an abstract line-cone cancellation, these are actual arithmetic sibling
families present in the source.

## 3. Compact carry dipole

The Möbius-adjoint carry row is

\[
 \sum_{k\le n/m}\mu(k)\beta_{n,mk}
 =\frac{2m-n-1}{n+1}.
\]

Applying the dyadic source gives

\[
 \sum_{k\le n/m}\omega_2(k)\beta_{n,mk}
 =
 \begin{cases}
  (2m-n-1)/(n+1),&m\le n<2m,\\
  (n+1-8m)/(2(n+1)),&2m\le n<4m,\\
  0,&\text{otherwise}.
 \end{cases}
\]

The inner band is nonnegative, the outer band is negative, and the entire
affine tail beyond `4m` vanishes exactly.  The two roots of
`(1-X)(1-X/2)` annihilate the two affine modes.

This identity survives the same-sign-hypercube objection: the odd family is
not erased; its concrete `2`-adic siblings supply the cancellation.

## 4. Positive inverse and digital boundary

The inverse is

\[
 A_2^\star(s)
 =
 \frac{\zeta(s)}{(1-2^{-s})(1-2^{-s-1})}.
\]

Its coefficient at `2^nu m`, `m` odd, is

\[
 a_2^\star(2^\nu m)=2\nu+2^{-\nu}>0.
\]

The generalized prime weights are positive:

\[
 \Lambda_2^\star(2^k)=(2+2^{-k})\log2,
 \qquad
 \Lambda_2^\star(p^k)=\log p
 \quad(p\text{ odd}).
\]

Thus the generalized Selberg forcing is coefficientwise nonnegative.

For the binary-digit dual `c_2(n)=1-v_2(n)`, whose partial sums are the
nonnegative binary digit sums,

\[
 c_2*\omega_2
 =
 \varepsilon-\frac52\delta_2+\delta_4.
\]

The complete infinite arithmetic source therefore becomes three boundary atoms
under one positive digital dual.

## 5. Positive multiplicative transport

The parabolic carry seed is nonnegative and already carries the sharp
`4sqrt(X)` objective.  Higher prime powers cost only `O(log^2 X)`, so only
ordinary-prime constraints need repair.

For `1<=A<B<=X` and `t>=0`, add

\[
 \delta b_m=t{\bf1}_{A<m\le B}.
\]

Then exactly

\[
 \Delta v_p=-t{\bf1}_{p\mid A}+t{\bf1}_{p\mid B},
\]

while the objective increases by

\[
 t\log(B/A)\ge0.
\]

Hence a positive block can transport violated constraint mass from all prime
divisors of `A` into available slack at the prime divisors of `B`, without ever
making a carry coefficient negative.

The exact bipartite certificate is:

```text
outflow from every positive-defect prime >= its defect;
inflow into every negative-slack prime <= its slack capacity;
all block amounts nonnegative;
all A<B.
```

Such certificates for all large `X` imply the prime-ramp lower bound and RH.

## 6. Exact Hall alternative

For any finite licensed block family, failure of transport is equivalent to
nonnegative weights `alpha` on positive-defect primes and `beta` on
negative-slack primes such that

\[
 \sum_{p\mid A}\alpha_p
 \le
 \sum_{p\mid B}\beta_p
\]

for every licensed block, but

\[
 \sum d_X^+(p)\alpha_p
 >
 \sum d_X^-(p)\beta_p.
\]

This is exact finite Farkas duality, not a heuristic Hall analogy.

The source-specific target is to rule out every such witness using the same
`omega_2` family.

## 7. The logarithmic firewall

Set

\[
 \alpha_p=\beta_p=\log p.
\]

Every block inequality holds because `A<B` implies `log A<log B`.  RDH at this
single witness is

\[
 \sum_{p\le X}(\log p)d_X(p)\le0,
\]

which is exactly

\[
 J_{\mathbb P,X}(b_X^{(0)})
 \le
 \sum_{p\le X}\frac{\log p}{\sqrt p}\log(X/p).
\]

Thus RDH contains the prime-ramp theorem explicitly.  It cannot be proved by
abstract Hall expansion, total slack, or PNT mass alone.

This is a feature of the review interface: any proposed reflected reserve must
specialize to the exact prime-ramp scalar at logarithmic weights.

## 8. Correct reflected consumer

PR #241 proves that a physical block is represented by a two-frequency
identity with kernel

\[
 \Phi_{J,\alpha}(t-s),
\]

not by the diagonal vertical integral.  Insert the complete positive inverse,
source, and generalized prime weights before splitting the carry dipole.

For a Hall witness, the proposed source vector is

\[
 \mathcal V_{\rm in}-\mathcal V_{\rm out},
\]

and the reflected contribution is the normal Gram

\[
 \int_J^{J+1}
 |Q_{\mathcal V_{\rm in}}(x)-Q_{\mathcal V_{\rm out}}(x)|^2dx.
\]

All inner/outer cross terms are retained.  This is the exact algebraic benefit
of reflection that survives the rejection of the old terminal proof.

## 9. Reflected Dyadic Hall

The sole new hinge is the symbolic reserve identity

\[
 \sum_{p\in\mathcal P_X^-}d_X^-(p)\beta_p
 -
 \sum_{p\in\mathcal P_X^+}d_X^+(p)\alpha_p
 =
 \mathfrak R_X+\mathfrak D_X+\mathfrak O_X,
\]

where

- `mathfrak R_X` is the two-frequency reflected normal Gram;
- `mathfrak D_X` is the atom-by-atom binary-digit boundary ledger;
- `mathfrak O_X` is the explicitly signed outer parabolic reserve on ordinary
  primes.

Every term must be written from the complete source and proved nonnegative.
The higher-prime-power `O(log^2 X)` comparison is handled outside this identity.

If the identity holds, Hall witnesses are impossible, a positive transport
exists, the carry certificate is feasible, and RH follows.

No version of this identity is currently proved.  It is the precise
adversarial-review target.

## 10. Full chain

```text
parabolic carry seed
-> prime-only defect/slack bipartition
-> dyadic opposite-parity Möbius source
-> compact inner/outer carry dipole
-> two-frequency reflected normal Gram
-> binary-digit finite boundary ledger
-> Reflected Dyadic Hall
-> positive multiplicative transport
-> feasible nonnegative carry certificate
-> 4sqrt(X)-O(log^2 X) prime ramp
-> square-screw/Landau
-> RH.
```

## 11. Exact regression

`X-26201` is standard-library only.  Through `n=192` it verifies:

```text
affine Möbius carry rows        18,336
compact dipole rows             18,336
2-adic source coefficients         192
digital convolution rows           192
positive inverse rows               192
shell inversions                    192
transport incidence rows             20
mutations rejected                    6
```

Retained classification:

```text
EXACT_DYADIC_PARITY_DIPOLE_ALGEBRA_VERIFIED
```

This is finite algebra only.

## 12. Review verdicts

The proposal is accepted only if the complete symbolic RDH identity is emitted
and the logarithmic witness reproduces the exact prime-ramp scalar.

It is rejected by any missing parity sibling, omitted reflected cross term,
wrong digital endpoint sign, hidden prime-power term, wrong defect/slack
bipartition, or unsigned replacement of the Möbius source.

## 13. Honest status

```text
dyadic source and compact carry dipole       proposed exact
positive inverse and digital dual            proposed exact
bipartite transport and Hall dual             proposed exact
transport certificate -> RH                  proposed complete composition
two-frequency source map                     proposed interface
Reflected Dyadic Hall identity                open / RH-bearing
Riemann Hypothesis                            unproved
```

The proposal is narrower than generic BTP and more honest than universal Brion
localization.  It identifies one concrete opposite-parity source whose carry,
digital, and reflected Selberg forms can all be checked against the same
coefficients.
