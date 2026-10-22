# M-26201 — Review and production protocol for the critical Euler-fiber proposal

Claim ID: `M-26201`  
Status: `METHODOLOGY / FAIL-CLOSED REVIEW CONTRACT`  
Date: 2026-08-08  
Applies to: `L-26201`, `L-26202`, `T-26201`

## 1. Freeze the proposal

Record one exact head SHA before review.  No later repair inherits the verdict on the frozen source.

Review in this order:

1. `L-26201` transform and source identities;
2. `X-26201` exact finite regression;
3. `L-26202` positive inverse, generalized primes, and annular reserve;
4. the imported two-frequency identity on PR #241;
5. `T-26201` conditional composition;
6. only then any production `EFRC` artifact.

## 2. Independent algebraic reconstruction

Do not begin from the displayed factorization.  Starting from

\[
H(t)=
\left(8e^t-7e^{t/2}-\frac32te^{t/2}\right)\mathbf1_{t\ge0},
\]

reconstruct independently:

\[
\widehat H(s)
=\frac{s(s+1)}{(s-1)(s-1/2)^2},
\]

\[
P(s)=(1-2^{1-s})(1-2^{1/2-s})^2,
\]

and

\[
P(s)\widehat H(s)
=s(s+1)\widehat W(s).
\]

Check the causal distributional endpoints; do not differentiate a truncated classical function while dropping its atoms.

## 3. Exact source checks

Verify the four-scale source

\[
b_{\mathcal E}(n)
=\mu(n)
 -(2+2\sqrt2)\mathbf1_{2\mid n}\mu(n/2)
 +(2+4\sqrt2)\mathbf1_{4\mid n}\mu(n/4)
 -4\mathbf1_{8\mid n}\mu(n/8).
\]

Required mutations:

1. remove `1-2^(1-s)` and confirm the pole mode survives;
2. replace the double half-pole factor by one copy and confirm the derivative moment survives;
3. remove the local Möbius factor and confirm the five-tap mass identity fails;
4. verify `b_E(n)=mu(n)` on odd integers;
5. inject the same-sign Möbius hypercube of PR #239 and retain every odd vertex;
6. compare the summatory source directly with the four scaled Mertens sums.

## 4. Positive inverse and Selberg sign

Reconstruct the local inverse

\[
\frac1{(1-z)(1-2z)(1-\sqrt2z)^2}
\]

and prove coefficient positivity for all orders, not only on a finite ladder.

Recompute

\[
-\frac{A_{\mathcal E}'}{A_{\mathcal E}}
\]

with the corrected sign convention from PR #241.  A sign error here invalidates the reflected forcing.

## 5. Annular reserve

For a declared `eta`, verify

\[
|P(\sigma+it)|
\ge
(2^\eta-1)(1-2^{-\eta})^2
\]

uniformly on

\[
1/2+\eta\le\sigma\le1-\eta.
\]

The reserve is a lower multiplier bound only.  Reject any argument that treats it as an upper estimate for the filtered source.

## 6. Production `EFRC` object

A production object must export:

```text
exact block index and support;
complete b_E source manifest;
complete five-tap two-adic fibers;
two independent reflected frequencies;
window packet {W,uW};
all product collisions;
all quotient and cutoff faces;
actual G,C,D matrices or an exact equivalent ledger;
strict LDL/SOS certificate for G-C*D^-1 C >= kappa_0 G;
every lower-block destination and coefficient;
polynomial endpoint budget;
2/3-shell causal-transfer mutation;
same-sign odd-Möbius-cube mutation.
```

The object fails if an unmatched same-scale row survives.

## 7. Quantifier table

Keep the following quantifiers separate:

| Object | Quantifier |
|---|---|
| Euler-fiber algebra | one fixed source, exact |
| finite block matrix | one declared block |
| `EFRC` | every sufficiently large dyadic block |
| annular reserve | uniform in vertical frequency on one compact substrip |
| RH deduction | global/cofinal |

A finite positive matrix or a finite block ladder is not `EFRC`.

## 8. Nearest false versions

The proposal must remain distinct from:

```text
PR #243: false conditional-Hankel positivity of the undifferenced spline;
PR #239: false absolute rank ceiling;
PR #226: false one-frequency physical-block identification;
PR #254: false nonnegative monotone carry cover;
PR #248 L-24518: stale flow-plateau telescoping identity.
```

For the last item, the direct constant-`b` incidence transport of current `L-24520` is the correct finite endpoint identity.  It is an equivalence/firewall, not the reflected reserve proved here.

## 9. Status rule

Use the following classifications literally:

- `VERIFIED`: the exact displayed claim has been independently reconstructed;
- `VERIFIED WITH FIXES`: the claim survives one named repair;
- `UNPROVEN`: a production matrix, uniform rate, or arithmetic inequality is absent;
- `FALSE`: an exact hypothesis-matching contradiction is present.

A failure of `EFRC` does not refute the fixed-source RH criterion.  A later modified fiber is a new proposal.
