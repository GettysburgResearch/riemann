# Agent report — certified-zero cardinal residues and the final cofinal inequality

Agent: `gpt56-04-f`  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Date: 2026-07-31  
Status: **new exact finite and cofinal theorem interfaces; RH not proved**

## Objective

Continue the smooth-target / canonical-Loewner / arithmetic-line program past the
matrix-norm comparison and identify the complete phase-aware arithmetic object
that must be positive cofinally.

## Main breakthrough

For the CCM basis on an interval of length `L`, a proof-grade critical-line zero
`1/2+i gamma` contributes the positive Cauchy ray

```text
A_(gamma,L) / [(r_gamma-n)(r_gamma-m)],
r_gamma=L gamma/(2 pi),
A_(gamma,L)=m_gamma L/pi^2 sin^2(pi r_gamma).
```

Its special source is explicit. A finite certified zero set can therefore be
subtracted exactly from the complete prime-side arithmetic source without any
assumption about the unselected zeros.

For a finite target polynomial `P`, every simple real target root `u_k` has the
cardinal kernel

```text
K_k(r)
 = Omega(u_k)/P'(u_k)
   * P(r)/[Omega(r)(r-u_k)].
```

The complete target-pinned arithmetic residue is exactly

```text
w_k(c)
 = c Omega(u_k)/P'(u_k)
   + sum_(gamma in Z) A_(gamma,L) K_k(r_gamma)
   + e_k^rem,
```

where `e_k^rem` is evaluated from the complete prime-side source after the
selected source is removed.

This is the exact last arithmetic arrow. The scalar line passes if and only if
all exact weights are positive.

## Conservative root-capture floor

Pair each target root with one certified zero. Define

```text
epsilon_k = |K_k(r_pair)-1|,
C_k^Z     = sum_(other selected gamma) A_gamma |K_k(r_gamma)|,
|e_k^rem| <= E_k.
```

Then

```text
w_k(c) >= A_k(1-epsilon_k)-C_k^Z-E_k+c v_k,
v_k=Omega(u_k)/P'(u_k).
```

The resulting lower and upper scalar thresholds give a finite exact sufficient
interval. In particular, `c=0` works whenever

```text
max_k [epsilon_k+(C_k^Z+E_k)/A_k] < 1.
```

A sufficient cofinal theorem is

```text
max_k epsilon_(j,k)
+ max_k (C_(j,k)^Z+E_(j,k))/A_(j,k)
-> 0.
```

The finite phase-avoidance lemma proves that, for every frozen finite zero set,
arbitrarily large supports exist on which no selected sine weight is small. It
does not give a uniform moat for a growing set.

## Exact checker

`X-15107` uses only Python integers and `fractions.Fraction`. The retained
synthetic control has

```text
nodes                         (-1,0,1)
target                        (3/8,1/4,3/8)
target roots                  (-1/2,1/2)
selected masses               (2,3)
residual masses               (1/10 at -2, 1/10 at 2)
selected residue sums         (2,3)
residual residue weights      (-1/40,-1/40)
complete residue weights      (79/40,119/40)
complement LDL pivots         (11803/405,1654576/48285)
proof-object digest           77befc9465424c51e03bbf44fc2c01248c5f22ff2f6d3eef615b50ba20dc2cc3
```

Eight fail-closed mutation tests are retained.

## Composition theorem

`T-15106` proves that the following cofinal package implies RH:

1. directed actual smooth-window coefficients;
2. exact simple real target roots;
3. proof-grade selected critical-line zeros;
4. complete prime-side source and selected-source subtraction;
5. strict positivity of every exact arithmetic residue weight for one scalar;
6. local-uniform convergence of the finite transforms to `Xi`.

The finite CvS theorem gives real zeros at every level and Hurwitz gives RH.

## What remains open

The new theorem does not establish for the Riemann data:

- cofinal simple real-rootedness of the actual smooth finite targets;
- a growing target-root / certified-zero pairing;
- small selected-zero cardinal cross leakage;
- small complete prime-side residual residues;
- the final strict scalar interval.

These are not missing finite algebra. They are the RH-bearing cofinal estimates.

## Strategic meaning

The final arithmetic problem is no longer expressed as an opaque matrix fit to
`-P'/P`. It is a phase-aware quadrature problem:

```text
positive selected zero mass
+ signed cardinal leakage
+ complete prime-side residual
+ one common scalar boundary direction.
```

The formula permits known line zeros to contribute positively without assuming
RH and keeps all unknown-zero information inside one directed arithmetic
residual. It is therefore suitable both for finite certification and for a
future asymptotic theorem.
