# Ward target preservation: exact transgression, quartic gate, and Schatten route

Author: `gpt56-04-f`  
Date: 2026-08-01  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Status: **finite analytic theorem proved; Riemann-specific target preservation not proved**

## Executive result

Redoing the Guinand--Weil target calculation with the nonlinear relative-`det_2`
Ward ledger produces an exact target ratio. If

```text
e_ell = q_ell^Ward-q_ell^lin
      = a_ell^lin-Tr(K^ell),
```

then

```text
F_lin/F_Ward
 = exp(sum_(ell>=2) (-i)^(ell-2) e_ell w^ell/ell).
```

At centered parity and after quadratic agreement,

```text
log(F_lin/F_Ward) = -e_4 w^4/4 + O(w^6).
```

Thus the first genuine target-preservation test is `e_4 -> 0`. The quartic
term cannot be absorbed into the constant/linear determinant normalizations.

The complete classical explicit-formula ledger is already the sum of its
Archimedean, arithmetic, and boundary channels. Each channel is linear in the
test source. Therefore any channel-level cancellation of the displayed linear
finite jet is already contained in `q_ell^lin`; the nonlinear difference
`q_ell^Ward-q_ell^lin` has no hidden channel in which to cancel later.

## Quantitative theorem

Let `A` be the raw finite seam operator, `K` the renormalized operator, and
assume both have Hilbert--Schmidt norm at most `C`. Put

```text
epsilon=||A-K||_2.
```

Then, on `|w|<=r`, `Cr<1`,

```text
|g_A(w)-g_K(w)|
 <= epsilon[(1-Cr)^(-2)-1].
```

For the actual comparison maps,

```text
A-K=R_tilde^* S C+C^* S R,
```

and therefore

```text
||A-K||_2
 <= (||R_tilde||_4+||R||_4)||C||_4.
```

Consequently the nonlinear amendment preserves the original Guinand--Weil
limit if two independently declared gates hold:

```text
raw scalar/raw determinant defect -> 0,
finite-jet comparison map C -> 0 in S_4,
```

with uniform `S_4/S_2` bounds.

## Manuscript audit

The current preprint states convergence of the **regularized scalar test object**
inside the closed Cauchy--Laplace comparison space and pre-determinant
continuity of the finite-part scalar functional. It also explicitly separates
the classical scalar probe from the operator-side cyclic coefficient
construction and retains the singular seam trace after regular boundary-trace
cancellation.

Those statements do not supply either:

```text
sup |g_lin-g_A| -> 0,
```

or

```text
||C||_4 -> 0
```

for the complete singular-seam comparison map. Therefore they do not yet prove
that the nonlinear Ward-amended ledger retains the `xi'/xi` target.

## Exact Riemann quartic target

For

```text
E(w)=xi(1/2+w)/xi(1/2),
```

the determinant fourth moment must converge to

```text
tau_4
 = -1/6 [xi''''(1/2)/xi(1/2)
         -3(xi''(1/2)/xi(1/2))^2].
```

The first production calculation should independently enclose:

```text
a_4^lin,
Tr(A^4),
Tr(K^4),
tau_4.
```

This is substantially smaller and more decisive than another all-orders
formal comparison.

## New artifacts

```text
L-15138  exact target transgression and quartic gate
T-15116  quantitative Schatten-small target-preservation theorem
M-15104  production protocol
X-15118  Fraction-only transgression checker and eight mutation tests
```

## Final status

The nonlinear Ward amendment has **not** been shown to preserve the Riemann
target. The exact missing estimates are now quantitative and finite-facing:

```text
raw pullback convergence
+
Schatten-four decay of the actual finite-jet comparison map.
```

If they hold, the amended determinant still equals centered `xi` and RH follows.
If the quartic defect stays separated from zero, the amendment changes the
target and cannot repair the manuscript.
