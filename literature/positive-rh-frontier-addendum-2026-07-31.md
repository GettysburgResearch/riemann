# Positive RH frontier addendum — newest repository and literature results

Agent: `gpt56-04-f`  
Date: 2026-07-31  
Status: source/repository synthesis; no RH theorem promoted

## 1. Exact radical-target repair changes the positive route

The newest stacked positive branch, draft PR #157, identifies a genuine source-domain issue in the global arithmetic radical map: the even Schwartz source must satisfy both

```text
f(0)=0
integral f=0.
```

A finite target selected only by one of these conditions is not automatically the truncation of an exact global radical vector.

Its repair is constructive. Start from a self-dual Fourier--Hermite source, cut it off smoothly, and subtract a fixed compact bump to repair the residual integral exactly. The resulting compact source satisfies both codimension-two constraints and converges in Schwartz topology. Poisson summation then transports its exterior radical tail through an exact Fourier defect. The branch also constructs growing repaired Hermite blocks and reduces the remaining positive step to a principal-angle/subspace-comparison theorem between:

1. the dangerous low prolate/multiband packet; and
2. a same-rank exact repaired radical packet.

This repair is compatible with `T-15104`: it improves the target-convergence gate, but does not prove the cofinal Finsler completion.

## 2. Symbol and leverage floors are the strongest complement-control layer

Draft PR #155 gives two exact variational lower-floor mechanisms.

### Ambient Fourier-density floor

A normalized function supported on an interval of length `L` has Fourier-energy density bounded by

```text
p_w(xi) <= L/(2*pi).
```

For a real multiplier symbol `s`, a bathtub principle gives the ambient floor

```text
B_L(s)=sup_G [G-L/(2*pi) integral (G-s)_+].
```

### Radical/packet leverage floor

After removing a finite packet `K`, the sharper pointwise density cap is

```text
c_K(xi)=||P_(K-perp) exp(-i xi x)||^2/(2*pi).
```

The complement floor becomes

```text
B_K(s)=sup_G [G-integral c_K(xi)(G-s(xi))_+ dxi].
```

This can prove a positive complement floor even when the ambient scalar floor is negative. It is a natural partner to the block Temple--Schur floor of PR #152 and to the repaired exact radical packet of PR #157.

The missing theorem remains cofinal: no production arithmetic symbol/leverage envelope has yet been proved to have limiting floor at least zero.

## 3. Exact Bézoutian diagnostic for the target-pinned route

`L-15109` sharpens `L-15107` when the finite target interpolation polynomial `P` has simple real roots `r_k`.

Let `R_c` be the special source polynomial after the scalar completion. The target-pinned matrix is congruent, up to a fixed sign, to the Bézoutian of `P` and `R_c`. Evaluation at the target roots diagonalizes its nonzero inertia:

```text
T_p(c) passes
iff
P'(r_k) R_c(r_k) < 0 for every k.
```

Since

```text
R_c(r_k)=R_0(r_k)-c Omega(r_k),
```

each root contributes one exact lower or upper threshold for `c`. The full interval is their intersection.

This yields a proof-producing finite audit:

1. Sturm-certify all target roots real and simple;
2. isolate them rationally;
3. enclose one scalar threshold per root;
4. choose a rational interior `c`;
5. independently replay exact complement LDL.

It also separates failure modes:

- nonreal target roots: target sequence fails at that level;
- real roots but empty scalar interval: arbitrary special metric may exist, but the restricted Weil completion fails;
- nonempty interval: finite real-zero target with an arithmetic positive metric.

## 4. Total-positivity shortcut is blocked at order five

Michałowski's arXiv:2602.20313 gives a rigorously certified negative `5 x 5` Toeplitz minor for the de Bruijn--Newman kernel, while lower-order minors at the same configuration remain positive. The result is explicitly about PF order and its configuration-dependent Gaussian repair threshold; it is not a value of the de Bruijn--Newman constant and does not imply or refute RH.

Consequently a blanket proof through `PF_infinity` of the undeformed kernel is unavailable. Log-concavity or `TP_2` cannot be promoted to all-order total positivity without additional structure.

This makes the localized Weil lower-floor, exact radical-subspace, and finite special-matrix completion programs more central.

## 5. Latest time-frequency localization input

Recent one-dimensional plunge-region estimates give explicit logarithmic bounds on the number of intermediate eigenvalues of time--frequency localization operators. They improve the scheduling and rank control of the finite prolate packet in PRs #152, #155, and #157.

They do not prove that the arithmetic Weil form is positive on the resulting complement. The arithmetic symbol/leverage estimate and the repaired-radical subspace angle remain separate obligations.

## 6. Updated positive-path decision tree

There are now two complementary cofinal routes.

### Route A — real-rooted target completion

Prove cofinally:

```text
1. exact repaired target transforms converge locally uniformly to Xi;
2. their finite interpolation polynomials are simple and real-rooted;
3. the L-15109 root-threshold interval is nonempty.
```

The finite special-matrix theorem and Hurwitz then prove RH.

### Route B — vanishing lower spectral floor

Prove cofinally:

```text
1. the exact repaired radical packet captures the dangerous low prolate packet;
2. the symbol/leverage complement floor is nonnegative up to epsilon_j;
3. the block Schur residual penalty is at most epsilon_j;
4. epsilon_j -> 0.
```

The monotone localized Weil ground floor then tends to zero from below, which is enough for RH.

## 7. Nonclaim

Neither cofinal theorem is currently proved. The new repo work substantially reduces and cross-checks the problem, but finite exact certificates, numerical spectra, target matching, or isolated passing levels cannot be extrapolated into RH.
