# Report — Uniform Hardy defect: stable remainder closed, unstable pole packet isolated

Date: 2026-07-31  
Agent: `gpt56-05-l`  
Issue: #180  
Branch: `agent/gpt56-05-l/154-nonlocal-barta-floor`  
Status: no RH proof; exact structural advance and scope correction

## Objective

The requested positive target was

```text
sup_sigma sigma/(2*pi) integral
 |Ghat(sigma+it) zeta'/zeta(1/2+sigma+it)|^2 dt < infinity,
```

or equivalently bounded Cesaro mean square for the pole-free prime statistic.

The pass attacked:

1. eta/parity contraction;
2. reflected Selberg linearization;
3. symmetric completed-xi reflection;
4. Suzuki meromorphic-inner/model-space structure;
5. exact half-plane Hardy principal parts.

## Result 1 — symmetric compact filter

`L-15416` introduces

```text
B_h(z)=2 sinh(hz/2)/(hz),
P_h(z)=cosh(hz)-cosh(h/2),
Omega_h(z)=B_h(z)^2 P_h(z).
```

Its inverse bilateral Laplace profile is a finite signed combination of three
translated symmetric triangles on `[-2h,2h]`. Its zeros lie only on

```text
Re z=0,
Re z=+1/2,
Re z=-1/2.
```

It therefore preserves every possible off-critical centered zero.

For

```text
F_h(z)=Omega_h(z) Xi'(z)/Xi(z),
```

the exact symmetry is

```text
|F_h(sigma+it)|^2
 =-F_h(sigma+it)F_h(-sigma+it).
```

No conjugation or vertical-frequency reversal is hidden.

## Result 2 — phase-gradient identity

For Suzuki's boundary-unimodular ratio

```text
Theta_omega(t)
 =xi(1/2-omega-it)/xi(1/2+omega-it),
```

direct differentiation gives

```text
partial_t log Theta     =  2 i Re[xi'/xi],
partial_omega log Theta = -2 i Im[xi'/xi].
```

Hence

```text
|xi'/xi|^2
 =1/4 (|partial_t log Theta|^2
      +|partial_omega log Theta|^2).
```

The Hardy target is exactly a weighted Dirichlet energy of Suzuki's scattering
phase. An off-line zero is an interior phase vortex.

## Result 3 — exact finite pole Gram

For

```text
p(z)=sum_j r_j/(z-a_j),
Re a_j<sigma,
```

Laplace Plancherel gives

```text
(1/(2*pi)) integral |p(sigma+it)|^2 dt
 =r^* C_sigma r,
C_sigma(j,k)
 =(2 sigma-conjugate(a_j)-a_k)^-1.
```

This is a positive Cauchy Gram. It yields the exact trichotomy:

```text
Re a<0:  normalized Abel mass -> 0;
Re a=0:  finite boundary mass |r|^2/2;
Re a>0:  divergence on the pole line.
```

Distinct maximal-real-part poles cannot cancel the divergence because their
diagonal terms scale as `1/(2 epsilon)` and their cross terms remain bounded.

## Result 4 — unconditional renormalized Hardy bound

Let `P_+` be the complete principal-part packet of centered xi zeros with
positive real part. `T-15407` proves, subject to an independent reconstruction
of the standard grouped Mittag--Leffler estimate,

```text
sup_(0<sigma<=1/2)
 sigma/(2*pi) integral
 |Omega_h Xi'/Xi-P_+|^2 dt < infinity.
```

The critical-line residues are absolutely summable after filtering because
`Omega_h(it)=O(t^-2)` and the unit zero count is `O(log t)`. Their normalized
Abel energy is uniformly bounded. The fully pole-subtracted analytic remainder
has uniform ordinary `L2` boundary control.

Thus there is no additional diffuse Hardy defect. The complete unstable object
is `P_+`.

## Result 5 — original target remains exactly RH

The unrenormalized bound holds exactly when

```text
P_+=0.
```

If an off-line zero exists, the filtered logarithmic derivative has a genuine
nonzero residue because the filter is zero-free in the open strip. The vertical
integral is infinite on its real-part line.

Therefore the requested bounded mean square was not proved. It is now isolated
as the statement that one explicit positive Cauchy/model-space packet is empty.

## Refuted proof shortcut

`R-15402` gives the exact model

```text
f_a(z)=1/(z-a)+1/(z+a).
```

It has all the required odd/reality symmetries and satisfies the exact reflected
modulus identity, but its Hardy energy diverges at `sigma=a`.

Any contour proof which linearizes the reflected bulk and omits the crossed
residue ledger therefore produces a false conclusion even in this rational
model.

## Literature alignment

Suzuki's canonical-system work studies

```text
Theta_omega(z)
 =xi(1/2-omega-iz)/xi(1/2+omega-iz).
```

Its boundary modulus is one unconditionally. Innerness in the upper half-plane
is equivalent to the relevant zero-free half-plane. The present pole packet is
the Hardy/Cauchy-coordinate form of the same non-inner defect.

The new reduction also matches the localized-Weil cardinal results elsewhere
in the repository: an off-line conjugate pair gives an exact indefinite finite
block. The pole Gram, anti-causal Hankel range, phase vortex, and cardinal block
are the same obstruction in four coordinate systems.

## Exact regression

`X-15408` is a standard-library Gaussian-rational checker. It retains:

```text
unstable two-pole energy     1562625/5002
unstable sigma energy        812565/10004
boundary sigma energy        21/26
boundary rational Abel bound 2
stable sigma energy          9/28
```

Nine adversarial tests pass.

## Correct positive continuation

The remaining proof must establish one of the following equivalent statements:

1. `P_+=0`;
2. every `Theta_omega` is meromorphic inner;
3. every anti-causal Hankel component vanishes;
4. the corresponding model-space defect has zero rank;
5. the off-line Xi-cardinal block is absent;
6. the localized Weil form has the required cofinal nonnegative floor.

The most concrete next attack is a causal-support theorem for Suzuki's kernel
or a collectively compact anti-Hardy family with a common tail modulus.

## Truth boundary

```text
symmetric reflection algebra          exact
finite pole Cauchy Gram                exact
renormalized Hardy defect bound        proposed/proved at theorem interface
residue-free reflection closure        refuted
right-half-plane pole packet empty     not proved
bounded mean square                    not proved
RH                                     not proved
```
