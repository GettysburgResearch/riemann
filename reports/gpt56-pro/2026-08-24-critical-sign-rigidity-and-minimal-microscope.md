# Xi critical-sign rigidity and the minimal residue microscope

## Executive result

The global Xi derivative class has only one sharp sign gate.

For `F=Xi^(r)`, complete reality of the zeros of `F'` together with

```text
F(c)/F''(c)<=0
```

at every real critical point forces `F/F'` to be Pick by a finite-strip
Lindelof argument. Therefore `F` is real-rooted and every boundary
Loewner/Stieltjes/source-capacity matrix is positive. The finite-window Schur
split remains valid; the collapse is global and Xi-specific.

At `r=0`, complete critical sign is exactly equivalent to RH.

## Why the infinity interface closes

Four ingredients are used.

1. Every Xi derivative zero lies in `|Im z|<=1/2`; hence every derivative ratio
   is Pick above `Im z=1/2`.
2. On a fixed safe line, completed-zeta Stirling asymptotics give a matching
   lower bound for the derivative denominator.
3. If all critical zeros are real, the paired Hadamard product gives cofinal
   vertical sides with quotient growth only

   ```text
   exp(O(log X loglog X)).
   ```

4. The harmonic measure of those sides in a fixed strip is `exp(-pi X/H)`.

The bottom boundary is nonnegative exactly when the critical residues are
nonpositive. The side contribution vanishes, so the quotient is Pick in the
whole upper half-plane.

## Exact source saturation

For Xi, the Pick ratio satisfies

```text
F(iy)/F'(iy)=O(i/log y).
```

Its Herglotz affine coefficient is therefore zero. The complete source measure
is exactly the positive critical-atom measure:

```text
a_n(F)=sum_(c>0) [-2 rho_c/c^(2n+2)].
```

Every finite-window boundary reserve is precisely the omitted positive
critical tail. `ZCAP`, remote moment matching and all-order capacity are not
independent once the sign is known.

## Minimal two-height microscope

Define

```text
Q_r(a,h)=-(4/3) Im m_r(a+ih)+(2/3) Im m_r(a+2ih).
```

Its kernel is

```text
K_(a,h)(x)=4h^3/
  [((x-a)^2+h^2)((x-a)^2+4h^2)] > 0.
```

It is uniquely characterized by:

```text
cancels every affine carrier;
h Q_r(c,h) -> rho_c at a critical point.
```

No one-height field can do both. Requiring the sampled ratios holomorphic and
`Q_r<=0` for every centre and scale is exactly equivalent to real-rootedness.

## Unconditional endpoint and scale equation

Completed-zeta right-half-plane asymptotics give

```text
Q_r(a,h)<0
```

uniformly in `a` for all sufficiently large `h`.

The Fourier multiplier is

```text
(2pi/3) t(2-t),  t=exp(-h|xi|),
```

and the exact scale equation is

```text
partial_h Q
 = -2|D| (I-exp(-h|D|))/(2I-exp(-h|D|)) Q,

(partial_h+|D|)(partial_h+2|D|)Q=0.
```

Increasing scale is dissipative. The RH-bearing inference runs backward and
is anti-diffusive.

## First-obstruction dichotomy

As the scale descends from the unconditional coarse region, the first failure
is exactly:

```text
pole:     Xi^(r+1)(a+jih)=0, a nonreal critical point;
or
contact:  Q_r reaches zero and becomes positive, producing a positive
          fine-scale residue.
```

This packages the former critical-reality, residue, boundary-Loewner and
outer-phase defects into one scalar evolution.

## Honest frontier

```text
optimal safe half-plane Im z>1/2             PROVED UNCONDITIONALLY
critical sign -> global Pick/real-rootedness  PROVED CONDITIONAL / REVIEW
exact source saturation                       PROVED CONDITIONAL
minimal two-height localizer                   PROVED EXACT
coarse minimal-field negativity                PROVED UNCONDITIONALLY / REVIEW
second-order scale equation                    PROVED EXACT
backward Xi scale descent MTSD105441            OPEN / RH-EQUIVALENT
Riemann Hypothesis                              UNPROVEN
```
