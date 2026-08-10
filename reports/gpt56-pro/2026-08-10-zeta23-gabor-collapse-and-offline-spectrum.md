# Zeta23 continuation: coherent-window collapse and exact off-line spectrum

Date: 2026-08-10

## 1. Aim

After importing Claude's Zeta23 theorem, the next question was whether a finite bank of coupled Gabor windows could push the support-one certificate substantially closer to RH while retaining the same prime-side information.

The answer for the most natural architecture is exact and negative. At the same time, the off-line pair itself admits a stronger exact spectral description than the paper uses. Together these results narrow the real continuation.

## 2. Result A: coherent same-lattice windows collapse to one scalar window

Take finitely many windows `phi_a` on the complete critical modulation lattice. Let

```text
psi^2=sum_a |phi_a|^2.
```

The multi-window synthesis factors exactly through scalar-window synthesis:

```text
S_multi=S_psi U,
U U*=I.
```

Therefore for every Hermitian physical form, including the Weil form,

```text
G_multi=U*G_psi U
```

and `G_multi` is unitarily equivalent to `G_psi direct_sum 0`.

This retains all mixed channel entries. It is not merely the previous block-direct-sum observation. The entire nonzero compression spectrum is unchanged.

Consequences:

```text
same positive/negative index,
same nonzero eigenvalues,
same trace powers of every order,
same rank-trace certificates,
same prime-side full-lattice kernel.
```

For finite height windows, completion of the modulation sum gives the same aggregate scalar kernel, with only the existing taper/end errors. Thus no fixed coherent same-lattice window bank can beat the optimized Montgomery–Taylor scalar profile asymptotically at support one.

This closes a large search space.

## 3. Result B: exact off-line pair eigenvalues

Let `z=x+iy` be a centered off-line zero coordinate and let `v=psi^2` be an even scalar power profile. In the complete critical frame, the two evaluation rows have Gram matrix

```text
[[A,C],[C,A]],
A=L int v(u)cosh(2yu)du,
C=L int v(u)du.
```

Pulling back the hyperbolic zero-pair block gives exactly two nonzero eigenvalues:

```text
m(A+C),
-m(A-C).
```

After unit atom normalization, the negative magnitude is

```text
m { [int v cosh(2yu)]/[int v] - 1 }.
```

It obeys the explicit lower bound

```text
negative magnitude >= 2m y^2 [int u^2v]/[int v].
```

For a window scaled to length `L`, this is a fixed multiple of `m(yL)^2`. Hence the natural scale `|beta-1/2| about 1/log T` is visible directly in the compression spectrum.

For the rectangular control window, the exact normalized pair eigenvalues are

```text
m[1+sinh(yL)/(yL)],
-m[sinh(yL)/(yL)-1].
```

## 4. Fusion with the repository's kernel-defect theorem

The existing source-pinned kernel classifier proves that an off-line Xi-cardinal difference has complete Weil value `-2m` and that positive-complement Schur elimination can only make it more negative.

The new Gabor theorem identifies the finite-frame ancestor of that direction: the negative eigenvector is the difference of the two conjugate evaluation rows. Its strength is explicitly depth-dependent.

The combined picture is now:

```text
finite Gabor plane:
  exact positive and negative pair eigenvalues;

complete selected-zero kernel:
  isolated off-line cardinal difference;

positive complement:
  Schur elimination cannot rescue the negative direction.
```

The missing theorem is no longer an abstract claim that a pair has negative signature. It is a quantitative **source-complete isolation theorem** carrying the finite evaluation-row difference into the complete kernel with controlled form and metric.

## 5. Why this still does not prove RH

For many zero packets, their rank-two planes interact. Positive on-line atoms can obscure a particular negative pair direction in a finite coefficient space, and Frobenius squares do not add packetwise before source-complete isolation. The exact per-pair negative magnitudes therefore cannot simply be summed.

A valid closure must produce one of:

1. a complete kernel capture theorem with controlled projection of each conjugate-row difference;
2. a global no-cancellation inequality for the sum of hyperbolic pair moats;
3. extra prime-side spectral moments that force the total negative spectrum to vanish.

## 6. Revised highest-value routes

The following are now closed or dominated:

```text
new scalar support-one taper;
block-diagonal window ensembles;
coherent same-lattice multi-window banks.
```

The surviving fronts are:

### A. Polyphase or irregular centers

Place different windows on different residue classes of a coarser modulation lattice, or use a nonperiodic center set. The exact scalar coisometry no longer applies. The first task is a matrix-symbol reduction and a support-one ceiling test.

### B. Complete-kernel isolation

Use the explicit negative row-difference vector and the resident Xi-cardinal/Schur machinery to prove a quantitative capture theorem. This is the most direct route from the new pair spectrum toward RH.

### C. Support just beyond one

The conditional optimizer says support about `1.0426` crosses `70%`. A narrow arithmetic extension remains a high-value independent front.

### D. Higher off-line-safe moments

Derive the zero-side count polynomial first, then compute only the prime-side moment it actually needs.

## 7. Verification

The retained regression verifies a finite cyclic version of the exact coisometry and congruence for four complex windows and an arbitrary Hermitian physical operator. It also checks the analytically continued rectangular-window Poisson sums and hyperbolic eigenvalues.

```text
PASS_ZETA23_GABOR_FUSION
```

The finite experiment is a normalization and mutation test, not the analytic proof.
