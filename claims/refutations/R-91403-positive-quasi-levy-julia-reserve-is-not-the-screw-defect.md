# R-91403 — The positive quasi-Lévy Julia reserve is not automatically the zeta screw defect

Claim ID: `R-91403`  
Status: **EXACT JORDAN-SUBTRACTION FIREWALL; CORRECTED RH GATE**  
Created: 2026-08-12  
Depends on: `L-91402`, `L-91403`, `T-91401`, Nakamura's signed quasi-Lévy formula  
Corrects: the final-defect wording of the first version of `T-91401`  
RH status: **unproved**

## 1. Three source channels

Let

\[
 \mathscr Q_a:
 H_+^2\longrightarrow
 H_-^2\otimes
 \left(
  \mathbb C
  \oplus L^2(\nu_\sigma^+)
  \oplus L^2(\nu_\sigma^-)
 \right)
\]

be the prime-inclusive completed source Hankel operator of `L-91403`.  Let

\[
 \mathscr Q_{a,0},
 \qquad
 \mathscr Q_{a,+},
 \qquad
 \mathscr Q_{a,-}
\]

be its orthogonal drift, positive-jump, and negative-jump components.

The positive Hilbert dilation uses the total-variation source form

\[
 \boxed{
 \mathcal C_a^{\rm abs}
 =2\left(
  \mathscr Q_{a,0}^*\mathscr Q_{a,0}
  +\mathscr Q_{a,+}^*\mathscr Q_{a,+}
  +\mathscr Q_{a,-}^*\mathscr Q_{a,-}
 \right).
 }
\tag{R-91403.1}
\]

This is positive and satisfies

\[
 \mathcal C_a^{\rm abs}
 =\mathcal J_a^*\mathcal J_a
  +\mathcal D_a^{\rm abs},
 \qquad
 \mathcal D_a^{\rm abs}\succeq0,
\tag{R-91403.2}
\]

by the score-projection Pythagorean identity.

## 2. The signed source form is different

Nakamura's completed logarithm is linear in the **signed** quasi-Lévy measure

\[
 \nu_\sigma=\nu_\sigma^+-\nu_\sigma^-.
\]

Therefore every source form intended to replay that signed explicit formula
linearly must retain the fundamental sign of the long-jump channel.  With the
same drift convention, define

\[
 \boxed{
 \mathcal C_a^{\rm sgn}
 =2\left(
  \mathscr Q_{a,0}^*\mathscr Q_{a,0}
  +\mathscr Q_{a,+}^*\mathscr Q_{a,+}
  -\mathscr Q_{a,-}^*\mathscr Q_{a,-}
 \right).
 }
\tag{R-91403.3}
\]

Then exactly

\[
 \boxed{
 \mathcal C_a^{\rm abs}
 -\mathcal C_a^{\rm sgn}
 =4\mathscr Q_{a,-}^*\mathscr Q_{a,-}.
 }
\tag{R-91403.4}
\]

The negative channel is nonzero: its measure has strictly positive density on

\[
 x>\log\varpi,
\]

and the carrier feature `G_t(x)` is nonzero for generic `t`.

## 3. Exact subtraction at the defect level

Put

\[
 \mathcal D_a^{\rm sgn}
 =\mathcal C_a^{\rm sgn}
  -\mathcal J_a^*\mathcal J_a.
\tag{R-91403.5}
\]

Subtracting (R-91403.2)--(R-91403.4) gives

\[
 \boxed{
 \mathcal D_a^{\rm sgn}
 =\mathcal D_a^{\rm abs}
  -4\mathscr Q_{a,-}^*\mathscr Q_{a,-}.
 }
\tag{R-91403.6}
\]

Thus the positive Jordan-dilation reserve is a **majorant** of the signed
source-minus-shape form.  It is not the signed form itself.

Consequently the shortcut

\[
 \boxed{
 \mathcal D_a^{\rm abs}
 =\mathbb K_a^{\rm del}
 }
\]

is not licensed by the quasi-Lévy construction.  It silently replaces
`nu_plus-nu_minus` by `nu_plus+nu_minus`.

## 4. Deterministic drift is a connection, not stochastic sign budget

The scalar factor

\[
 \exp(-2it\lambda_\sigma)
\]

in the completed boundary phase is a deterministic unimodular multiplier.  Its
radial derivative is naturally a skew moving-unitary connection, in the same
sense as `L-91306`, rather than a Poisson first-chaos variance.

Placing it in a one-dimensional positive Hilbert coordinate is a valid Julia
dilation, but the norm assigned to that coordinate is not by itself a
canonical screw normalization.  Any final source identity must either:

```text
handle the drift covariantly; or
derive its one-dimensional metric from the same Guinand--Weil normalization.
```

This issue is independent of the unavoidable negative-channel correction in
(R-91403.4).

## 5. Finite hostile control

`X-91402` evaluates the boundary source features at

```text
sigma=9/2,
carriers=(0.31,0.83,1.37),
prime powers n<=50000.
```

The positive-dilation auxiliary has eigenvalues

```text
7.780766610822354e-06
0.003109834069897429
0.47278065706571115.
```

The positive long-jump channel has eigenvalues

```text
4.000179435278566e-06
0.0015882628086723192
0.23225685868866947.
```

The exact signed subtraction has eigenvalues

```text
-6.736415360827961e-05
-8.388778457951098e-11
 0.008267392786161332.
```

The numerical identity

\[
 D^{\rm sgn}=D^{\rm abs}-2G_-
\]

holds with zero retained floating error in the unscaled carrier convention.
The factor is `4` after the model-space normalization of (R-91403.1).

This finite packet is not a counterexample to RH: it is before the complete
model-space/delay/bridge source identification.  It is a counterexample to the
claim that signed positivity follows automatically from the positive Jordan
dilation.

## 6. Corrected remaining theorem

The final programme now has two logically separate obligations.

### Obligation A — signed source lock

Prove on the corrected delayed two-sided-plus-bridge core that the resident
Guinand--Weil/Suzuki source form is the signed quasi-Lévy source-minus-shape
form:

\[
 \boxed{
 \mathbb K_a^{\rm del}
 =\mathcal D_a^{\rm sgn,del,bridge}.
 }
\tag{R-91403.7}
\]

This requires the exact rational mother, both orientations, every delay cross
term, the bridge, and the deterministic connection normalization.

### Obligation B — negative-channel domination

Using (R-91403.6), positivity would then be equivalent to the explicit
operator domination

\[
 \boxed{
 \mathcal D_a^{\rm abs,del,bridge}
 \succeq
 4\mathscr Q_{a,-}^{*}\mathscr Q_{a,-}
 }
\tag{R-91403.8}
\]

with the delayed/oriented/bridge version of the negative-channel feature map.

This is now the concrete RH-bearing inequality: the positive Julia reserve
must absorb the long-jump archimedean channel after the exact structured
compression.

## 7. Exact boundary

```text
prime Poisson-Fock embedding                         EXACT
positive two-channel completed Hardy dilation        EXACT
positive total-variation auxiliary                   EXACT
signed quasi-Levy source form                        EXPLICIT INDEFINITE
absolute-minus-signed correction                     EXACT
positive auxiliary = screw defect                    REFUTED AS A SHORTCUT
signed source lock to delayed screw Gram              OPEN
positive reserve >= long-jump channel                 OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
