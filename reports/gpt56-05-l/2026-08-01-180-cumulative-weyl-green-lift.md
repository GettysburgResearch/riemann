# Cumulative Weyl / Green-lift positive-route report

Date: 2026-08-01  
Agent: `gpt56-05-l`  
Issue: #180  
Branch: `agent/gpt56-05-l/154-nonlocal-barta-floor`

## Objective

Seek an independent arithmetic or canonical-system mechanism for a uniform
positive Toeplitz lower bound, without recycling the RH equivalence or a soft
compactness argument.

## Main advance 1 — direct horizontal canonical flow

For

```text
Xi(z)=integral Phi(t) exp(i z t) dt,
E_omega(z)=Xi(z+i omega),
```

the coordinate de Branges kernel is

```text
D_tilde_omega(a,b)
 = 1/pi integral_(|(a+b)/2|)^infinity
   sinh(2 omega y)
   Phi(y+(a-b)/2) Phi(y-(a-b)/2) dy.
```

Differentiation gives exactly

```text
partial_omega D_tilde_omega = (4/pi) K_omega^W,
```

where `K_omega^W` is the original coordinate Weyl kernel. Therefore

```text
D_tilde_omega=(4/pi) integral_0^omega K_u^W du.
```

This supplies the missing algebraic Weyl-to-de-Branges bridge directly. It
requires cumulative Weyl positivity, not pointwise positivity at every
intermediate shift.

## Main advance 2 — endpoint branch primitive

For the normalized Volterra branches

```text
M_(sigma,omega) f
 = integral f(s) exp[sigma omega(s+u)/2] A_s(u) ds,
```

one has

```text
partial_omega M_(sigma,omega)
 = sigma N_(sigma,omega)/2.
```

Hence the integrated Weyl derivative form is exactly

```text
integral_0^omega Q_u(f) du
 = 1/2 (||M_(+,omega)f||^2-||M_(-,omega)f||^2).
```

The positive theorem needs only endpoint branch domination. It may tolerate
negative derivative layers at intermediate offsets.

## Main advance 3 — quotient data processing

If `C` is a surjection, its range has the minimum-lift quotient norm, `E` is
the minimum-norm right inverse, and `K` is a contraction, then

```text
||C K E||_quotient <= 1.
```

The proof is one line: `K E y` is an admissible lift of `C K E y`.

In a prescribed physical metric the exact defect is

```text
I-(C K E)^*(C K E)
 = E^*(C^*C-K^*C^*C K)E.
```

Thus the Volterra contraction is automatic in the Green quotient metric. The
remaining issue is metric binding to the original Weyl branch space.

## Main advance 4 — arithmetic Jordan carré du champ

Suzuki's coefficients satisfy

```text
J_(2 omega)(n)=n^omega c_omega(n),
sum_(d|n) J_(2 omega)(d)=n^(2 omega).
```

Therefore

```text
P_omega(n,d)=J_(2 omega)(d)/n^(2 omega), d|n
```

is an exact divisor Markov transition. Its conditional expectation has the
positive defect

```text
sum P |F|^2-|sum P F|^2
 = 1/2 sum_(d,e) P_d P_e |F(d)-F(e)|^2.
```

This is an independent arithmetic energy mechanism. The sought intertwiner
should identify this conditional expectation with the continuous Volterra
Green lift, including the archimedean factor.

## Transfer theorem

Once the original-coordinate Weyl form is bound exactly to the normalized
Volterra form and endpoint branch domination is proved, the new horizontal
flow gives a positive de Branges kernel. The scattering ratio is then inner and

```text
T_omega^* T_omega = I
```

for every offset. The final coercivity constant is therefore `eta=1`, not just
an unspecified positive reserve.

## Exact finite regression

`X-15410` verifies:

```text
horizontal derivative weight   58/35
Weyl weight                     29/70
factor                          4
endpoint cumulative energy       7/12
Green defect pivots              3/4, 7/16
Jordan mean                    -161/144
Jordan variance                 38735/20736
```

Seven mutation tests pass.

## Smallest concrete blocker

The original uniform Toeplitz LMI is no longer the smallest theorem. The exact
remaining gate is

```text
||y||_physical^2 = inf_(C h=y)||h||_lift^2
```

on the complete Volterra branch range, or equivalently

```text
E^*(C^*C-K^*C^*C K)E >= 0
```

in the physical/original Weyl metric.

The latest Volterra paper closes a normalized quotient contraction but itself
lists the quotient-to-original Weyl lift as open. This report supplies the
direct Weyl-to-de-Branges flow after that lift, so no separate KLM/de Branges
intertwiner remains necessary.

## Honest status

- direct horizontal flow: `PROPOSED`, exact derivation;
- endpoint primitive: `PROPOSED`, exact algebra;
- quotient contraction: exact Hilbert-space theorem;
- Jordan energy: exact arithmetic identity;
- quotient-to-physical Weyl metric binding: not proved;
- unconditional Toeplitz coercivity: not proved;
- RH: not proved.
