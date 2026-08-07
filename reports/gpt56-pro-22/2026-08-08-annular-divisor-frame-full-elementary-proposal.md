# Annular divisor-gradient projection: a full elementary carry proposal

Date: 2026-08-08  
Agent: `gpt56-pro-22`  
Issue: #261  
Parent: draft PR #254 at `be8405e543957ae64ddd10965e9d709e38beb5ff`

## Executive result

The parabolic carry route has acquired a concrete recursive mechanism.

The failed monotone cover taught us that the seed has two macroscopic ledgers:
positive prime-power defect and negative prime-power slack. A sharp proof must
move one into the other rather than delete the positive part.

The new exact coordinate is the prime-power divisor gradient

```text
g_q(m)=1_(q|m)-1_(q|m-1).
```

A cumulative divisor flow is a Gram correction in these rows. The upper-support
concentration at highly composite integers is therefore structural: one such
integer superposes many active divisor gradients, while its two neighbors are
the discharge channels.

On one fixed interior annulus, the active minimum-norm correction has an exact
finite formula. The initial positive residual now has the proved bound

```text
||(r_X)_+||_2 << log^(3/2)(2X).
```

If the source-generated active Gram retains a subpower frame moat and its
leakage contracts the positive residual, the cumulative flow has subpower norm.
Interior slack then preserves every `b_m>=0`, and the exact objective loss is
only

```text
X^(-3/2+o(1)).
```

This gives the sharp `4 sqrt(X)-X^o(1)` prime-ramp lower bound and the inherited
square-screw/Landau implication to RH.

## New exact results

### Divisor-gradient Gram

For amplitudes `a_d`,

```text
F(j)=sum_(d|j)a_d,
b_a(m)-b0(m)=F(m-1)-F(m)=-sum_d a_d g_d(m).
```

Therefore every prime-power constraint changes by the exact rectangular Gram

```text
v_q(b_a)-v_q(b0)=-sum_d <g_q,g_d>a_d.
```

The von-Mangoldt identity

```text
log(m/(m-1))=sum_(q=p^a) Lambda(q)g_q(m)
```

makes the objective charge the same Gram in its dual coordinate.

### Annular transfer

For any fixed `0<alpha<beta<1`, the parabolic seed has a positive
`c_(alpha,beta) sqrt(X)` moat on the annulus and its two boundary sites. A flow
with `||F||_2=X^o(1)` therefore preserves every primal coordinate.

The exact objective weight has annular `l2` norm `O(X^-3/2)`, so the total loss
is `X^(-3/2+o(1))`.

### Closed initial source budget

Write the first-unit selector in every `q`-block as

```text
chi_q=1/q+(chi_q-1/q).
```

The mean-zero term has a periodic primitive bounded by one. Integrating the
continuous parabolic derivative by parts gives

```text
(r_X(q))_+ << [1+log(X/q)]/sqrt(q).
```

Summing over prime powers and enlarging to all integers yields

```text
||(r_X)_+||_2^2 << log^3(2X).
```

This closes the former `SAF1` gate by elementary calculus.

### Active minimum-norm projection

For active residual rows `S`,

```text
u=A_S^* (A_S A_S^*)^-1 r_S
```

is the exact minimum-norm repair. A half step reduces every active residual by
exactly one half, and

```text
||u||_2^2=<r_S,(A_S A_S^*)^-1 r_S>.
```

The only remaining issue is leakage into inactive rows.

### Complete-period model

Different prime bases are exactly orthogonal over complete common periods.
Same-base prime-power chains have normalized correlation

```text
p^(-|a-b|/2)
```

and a uniform Toeplitz frame floor. Thus the source of difficulty is not a
hidden degeneration inside one prime-power chain; it is finite-annulus boundary
coupling and leakage across prime bases.

## Load-bearing theorem

The remaining Slack-Anchored Annular Frame theorem asks for two source-specific
bounds along the deterministic iteration:

```text
A_S A_S^* >= X^-o(1) I for every generated active set,
||(r_next)_+||_2 <= rho ||(r)_+||_2, rho<1.
```

Together with the closed initial source budget, these imply a convergent flow
with `||F||_2=X^o(1)`.

The theorem is deliberately not stated for arbitrary row subsets. Full annular
prime-power matrices contain badly conditioned artificial subsets. The
quantifier is over active sets generated from the exact parabolic residual after
identical-row compression.

## Why the theorem is plausible but not proved

The source contains four favorable mechanisms:

1. complete-period orthogonality across different prime bases;
2. uniformly conditioned normalized chains for one prime base;
3. bounded same-scale consecutive-prime-power clusters, including the exact
   `{2,3,4,5}` inverse from PR #254;
4. a macroscopic negative-slack reservoir which absorbs boundary leakage.

What remains is a deterministic finite-annulus theorem showing these mechanisms
combine with a uniform leakage ratio. An entrywise bound is too crude and would
again destroy the dipole cancellation.

## Reconnaissance

For `I_X=[0.45X,0.80X]`, ordinary floating active projections gave generated
frame floors between roughly `0.65` and `1.05` through `X=5000`, while flow
`l2` norms stayed near `0.06--0.08`. The exact objective costs fell to about
`3e-10` at `X=5000`.

These values motivate the frame/leakage theorem but prove nothing asymptotic.

## Exact replay

`X-26101` verifies the finite algebra using integers and `Fraction`:

```text
divisor-gradient/cumulative-flow replay     PASS
rectangular Gram replay                      PASS
formal von-Mangoldt objective identity       PASS
minimum-norm active projection               PASS
active residual halving                      PASS
complete-period covariance controls          PASS
annular slack/cost synthetic control          PASS
mutation tests                               7/7
proof-object SHA-256
8f9bae3c146f304704a9350977aecd8300b050766c32d2d6a7808d60a118dd44
```

## Full proposal

```text
carry/binomial factorization
-> divisor-gradient LP
-> parabolic 4 sqrt(X) seed
-> exact signed constraint dipole
-> polylog initial residual budget
-> annular divisor-gradient frame
-> active minimum-norm projection
-> generated frame moat and leakage contraction
-> subpower annular flow
-> sharp prime-ramp lower bound
-> square-screw upper envelope
-> Landau pole exclusion
-> RH.
```

## Honest boundary

```text
exact finite algebra                    retained/proposed complete
annular slack and objective transfer    proposed complete
initial residual L2 budget              proposed complete
active projection recursion             proposed exact
generated frame moat                    open / RH-bearing
positive leakage contraction            open / RH-bearing
remaining theorem -> prime ramp -> RH   proposed complete composition
Riemann Hypothesis                      unproved
```

This pass supplies a serious full elementary proposal and a concrete recursive
potential. It does not promote the reconnaissance into a proof.