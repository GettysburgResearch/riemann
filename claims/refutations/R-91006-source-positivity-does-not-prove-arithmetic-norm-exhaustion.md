# R-91006 — Safe source positivity does not prove arithmetic norm exhaustion

Claim ID: `R-91006`  
Status: **EXACT NORM-EXHAUSTION FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91034`, `L-91038`, `R-91005`, PR #398 controls  
RH status: **unproved**

## 1. The tempting implication

The live programme has explicit positive objects on the safe side:

```text
positive generalized-Jordan coefficients;
a divisor-splitting Stinespring isometry;
a compound-Poisson/Fock product system;
all finite Green divisions of the centered source;
a completed positive Hankel measure in the proved scale ranges;
Suzuki's completed amplitude-level Hankel isometry at safe scales.
```

It is tempting to infer

```text
safe positive source
 + exact source/critical/stable/zero-port identity
 -> critical and stable outputs exhaust the source norm
 -> zero port vanishes.
```

This implication is false without an additional tangent/source-ordering
identity.

## 2. Exact one-pole control

For `p in H`, let

\[
 b_p(z)=\frac{z-p}{z+\overline p},
 \qquad
 \Theta(z)=b_p(z)^{-1}.
\]

Then `B=b_p` removes the pole and

\[
 B\Theta\equiv1.
\]

The pole-removed source kernel is zero, while

\[
 \boxed{
 0=K_\Theta+rac{K_{b_p}}{b_p\overline{b_p}}.
 }
 \tag{R-91006.1}
\]

The second term is the nonzero positive rank-one port

\[
 \boxed{
 \frac{K_{b_p}(z,w)}{b_p(z)\overline{b_p(w)}}
 =\frac{2\Re p}{(z-p)(\overline w-\overline p)}.
 }
 \tag{R-91006.2}
\]

Thus a positive source—indeed the zero source—can coexist with a nonzero
hyperbolic port that exactly cancels an adverse critical kernel.

## 3. Exact logical content of exhaustion

By `L-91038`, the statement

\[
 \mathcal K_a^{\rm src}
 =\mathcal K_a^{\rm crit}+\mathcal K_a^{\rm st}
 \tag{R-91006.3}
\]

is not a generic consequence of positivity.  It is equivalent to

\[
 K_{B_a}\equiv0,
 \]

hence to the absence of every crossed zero pole at depth greater than `a`.
Requiring it on all positive scales is exactly RH.

Therefore a purported proof has not constructed norm exhaustion if it merely:

1. produces a positive source Gram;
2. proves the stable port positive;
3. invokes conservation of a larger source/critical/stable/hyperbolic
   colligation;
4. omits the hyperbolic output from the target diagram.

The omitted output is precisely the conclusion-producing defect.

## 4. Arithmetic-Hankel versus model-space source

The safe arithmetic feature of `L-91031` has Hankel form

\[
 H_a(z+\overline w).
\]

The pole-removed scattering feature of `L-91034` has model-space form

\[
 m_a(z)\overline{m_a(w)}
 \frac{1-I_a(z)\overline{I_a(w)}}{z+\overline w}.
\]

Both kernels may be positive without being equal or even comparable.  A
coisometry between their feature spaces exists only after the appropriate
Douglas kernel inequality is proved.  Identifying them by notation, by matching
one diagonal, or by matching one scalar transfer function is a polarization
error.

The actual source-ordering theorem must retain:

```text
all vertical carrier phases;
the normalized Jordan first chaos;
the gamma and pole tangent channels;
the delayed causal and anti-causal Hardy fibres;
the bridge direction;
every cross term.
```

Suzuki's unitary Hankel operator identifies the completed **amplitude**.  As
recorded on PR #400, differentiating an amplitude isometry does not sign its
radial Wigner--Smith curvature.

## 5. Correct final target

The only noncircular formulation is:

> Construct an explicit tangent-level coisometry from the completed arithmetic
> first-chaos space onto the critical and deterministic Hardy output spaces,
> and prove the exact feature-kernel identity on a uniqueness set.

By `L-91038`, success automatically deletes the Blaschke zero port and proves
the corresponding zero-free strip.  Conversely, under that zero-free strip the
canonical model-space coisometry is given explicitly by `(L-91038.10)`.

Thus the target is mathematically sharp, but it is not a lemma already implied
by the existing safe positivity stack.

## 6. Boundary

```text
safe source positivity -> norm exhaustion             FALSE
amplitude isometry -> tangent norm exhaustion          FALSE
model-space exhaustion under zero-port absence         EXACT
model-space exhaustion -> zero-port absence             EXACT
all-scale arithmetic exhaustion                        RH-EQUIVALENT
unconditional arithmetic tangent coisometry            OPEN
Riemann Hypothesis                                      UNPROVED
```
