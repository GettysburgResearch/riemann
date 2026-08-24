## T105600 addendum — phase variance, anti-Poisson descent and height-shell energy

The remaining zero-height/spatial-escape defect now has three exact,
source-compatible coordinates.

### Unit-phase barycenter

For the extremal-base Pick ratio, the normalized hyperbolic derivative is a
barycenter of unit Herglotz phases:

```text
y f'(z)/Im f(z) = E omega_z.
```

The differential microscope is the exact directional phase variance

```text
C = -(Im f/4) E|omega_z-1|^2.
```

A shallow nonnegative contact forces local Herglotz-mass evacuation and a
Schwarz--Pick automorphism blow-up.

### Exact backward Poisson

After descending the base by `delta`, Xi's vanishing affine Herglotz
coefficient gives

```text
C_h^[delta] = exp(delta |D|) C_h^[0].
```

The physical kernel is negative in a central core and positive in a remote
tail. Every contact satisfies one exact local-hole inequality. Compactly
supported finite Pick measures necessarily develop the wrong positive
`delta M/(2a^2)` tail, so finite polynomial models cannot certify the global
Xi descent.

### Reciprocal-source dictionary

In reflected safe-line coordinates,

```text
-2 C_(r,b)(a,h) = Re(q_r-h q_r'),
q_r=xi^(r)/xi^(r+1).
```

The frozen rung-zero source is

```text
sum_n b_L(n)(1+h log n)n^(-s),
b_L(n)>=0.
```

Lowering the base multiplies frequency `log n` by `n^delta`, exactly matching
the backward-Poisson amplifier. The existing one-sided-Hardy phase gap is
therefore a producer for the literal microscope.

### Height-shell all-pass

For real polynomials, `F(x+ih)/F(x-ih)` has winding minus the number of roots in
`|Im rho|<h`. Height-shell quotients telescope down the derivative ladder.
Negative shell winding is paid by negative `H^(1/2)` energy. In finite Xi
rectangles, all intermediate endpoint terms cancel and only one low/high
vertical correction remains.

The strict shell closure condition is

```text
sum adjacent negative H^(1/2) energies
+ positive part of the telescoped endpoint correction
< 2.
```

Because off-line shell roots come in conjugate pairs, this empties the shell.

### Common phase family

With the normalized companion `F'-(alpha/h)F`,

```text
C_F(x,h)
 = -(h^2/4) partial_h partial_alpha arg Theta_(alpha,h)(x)|_(alpha=0).
```

The pointwise microscope and shell all-pass winding are two derivatives of the
same circle-valued deformation.

### Replay and status

```text
PASS_X_105600_PHASE_BARYCENTER_ANTIPOISSON_SHELL
checks=2187
proof object:
6127ff8f37d767ca34b32a271ae44c10a469d5783a0c31a5f078453ade71b9df
```

Exact remaining gates:

```text
DMPXFER105603   physical one-sided-Hardy pointwise transfer       OPEN
HSHE105602      physical shell H^(1/2) plus endpoint transfer     OPEN
spatial escape exclusion                                         OPEN
Riemann Hypothesis                                                UNPROVEN
```
