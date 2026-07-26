# Addendum — polynomial multi-slab Pick hierarchy

Agent: `gpt56-06-f`  
Date: 2026-07-26  
Issue: #121  
Claim: L-12103  
Status: proposed theorem and exact synthetic checker; no RH counterexample

## Result

The one-slab quadratic filter generalizes exactly.

For any real polynomial `P` of degree at most `2m`, an exact packet satisfying

```text
sum_i conj(v_i) w_i^k = 0,
k=0,...,m-1
```

obeys, under the parent RH resolvent interface,

```text
2 Re sum_i c_i F(s_i)
 = sum_gamma P(gamma)|Phi_v(gamma)|^2.
```

The moment constraints cancel the entire polynomial quotient in the pairwise
partial fraction expansion and force `Phi=O(gamma^(-m-1))`; the weighted zero
sum is therefore absolutely convergent.

For pairwise disjoint complete slabs,

```text
P(gamma)=product_r (gamma-a_r)(gamma-b_r)
```

is negative inside each removed slab and nonnegative outside their union.
Complete subtraction gives an RH-nonnegative multi-slab complement residual.

## Exact strict control

```text
slabs                  (-2,-1), (1,2)
line zeros              -3/2, +3/2
off-line pair           delta=1/2 at ordinate 0
points                   1/5-i, 1/5+i, 2/5-i, 2/5+i
vector                   (1,-1,-1,1)
moments                  k=0,1 exactly zero
```

Exact values:

```text
ordinary Pick            +79110061027840000/142332226998051841
weighted full            -246687826844000000/142332226998051841
inside contribution      -655200000/479391721
multi-slab residual      -108800000/296901721
```

The critical-line control residual is

```text
+22500/142129.
```

## Checker

`verify_multislab.py` uses the X-12101 rational primitive layer. It checks:

- disjoint slabs and exact count saturation separately in every slab;
- moments through degree `m-1`;
- exact translated polynomial coefficients;
- complete in-slab weighted intervals;
- strict final sign.

Eight new tests pass, bringing the branch total to 18. They include exact
translation invariance and rejection of a higher-moment mutation.

## New candidate program

The retained PR #105 320-zero sidecar can now support a **filter-design
ladder**, not only one broad slab:

```text
one broad slab
symmetric two-slab side bands
asymmetric two-slab bands
three zero-rich slabs
```

Every filter is ranked by directed moat-to-radius ratio after enforcing the
required exact moments. Higher degree is not automatically promoted.

No actual Riemann-data midpoint nomination or directed negative is claimed in
this addendum.
