# L-91547 — Both Hall residual sources contract by one fixed deterministic 67-split

Claim ID: `L-91547`  
Status: **PROVED EXACT SYMMETRIC POST-HALL CONTRACTION THEOREM**  
Created: 2026-08-13  
Depends on: `L-91540`, `L-91545`  
RH status: **unproved pending merged producer and loss audits**

## 1. Positive source measures after Hall

By `L-91545`, the target-bearing outputs of the one-prime survival and hazard
Hall networks are genuine positive source measures

\[
 c_s\ge0,
 \qquad
 c_h\ge0
 \tag{L-91547.1}
\]

in paired positive kernel types at the common parent endpoint `X`.  Their target
masses satisfy

\[
 \boxed{
 \mathfrak T_{s,X}(c_s)+
 \mathfrak T_{h,X}(c_h)
 =\mathfrak T_X^{\rm parent}.
 }
 \tag{L-91547.2}
\]

Every matched Hall edge has already been removed into a target-null positive
current row bonus.  No next-prime color is attached to `c_s` or `c_h`.

## 2. Apply the same split to both types

For `tau in {s,h}` define

\[
 \theta_\tau(n)=\mathbf1_{n\le X/67}.
 \tag{L-91547.3}
\]

Apply `L-91540` with the single geometric scale `67`.  The actual child measure
is

\[
 c_\tau^{\rm child}
 =c_\tau|_{\{n\le X/67\}},
 \tag{L-91547.4}
\]

retaining the same paired type `tau` and now evaluated at endpoint `X/67`.
For target, score, and every exact component row one has

\[
 \boxed{
 K_{\tau,X}(c_\tau)
 =K_{\tau,X/67}(c_\tau^{\rm child})
  +K_\tau^{\rm residual},
 \qquad
 K_\tau^{\rm residual}\ge0.
 }
 \tag{L-91547.5}
\]

The residual is current-generation data.

## 3. Subprobability target weights

Normalize the parent target in (L-91547.2) to one and put

\[
 \omega_\tau
 =\mathfrak T_{\tau,X/67}(c_\tau^{\rm child}).
 \tag{L-91547.6}
\]

Summing the positive target residuals in (L-91547.5) gives

\[
 \boxed{
 \omega_s\ge0,
 \qquad
 \omega_h\ge0,
 \qquad
 \omega_s+\omega_h\le1.
 }
 \tag{L-91547.7}
\]

Both child endpoints equal

\[
 \boxed{Y_s=Y_h=X/67<c_0X.}
 \tag{L-91547.8}
\]

After target normalization, the total positive local debt of the two geometric
residuals is at most their total residual target and hence at most one.

## 4. Why this is stronger than the ordered-prime placement

The original binary-return architecture sent the hazard output through a
variable-`p` affine child lift and sent survival to the next ordered rough prime.
Neither operation is needed after `L-91545`:

```text
Hall has already made both target-bearing outputs positive sources;
paired-type endpoint monotonicity supplies a geometric split for either type;
the factor-54 consumer needs contraction, not arithmetic provenance.
```

Only the fixed scale-`67` affine functor is needed when arbitrary child packings
are assembled in parent coordinates.  Its normalization is the resident exact
identity of `L-91318`; no Hall coefficient is transported through a variable
rough-prime lift.

Thus the following are removed from the load-bearing chain:

```text
ordered-prime survival recursion;
unique-next-prime color transport;
variable-p hazard affine normalization;
repeated one-prime Hall projection.
```

## 5. Row and quantization assembly

For both types, the child component row at endpoint `X/67` is lifted by the same
positive affine map.  All current residuals and Hall row bonuses remain at the
parent endpoint.  Push the two child measures to the parent continuum
coordinate, sum them with the current rows, and apply `L-91329` once.

Because (L-91547.7) is a target subprobability identity before quantization, the
fixed affine lift and collar cannot duplicate target mass.

## 6. Boundary

```text
positive survival/hazard residual sources           EXACT
same deterministic 67-split for both types           EXACT
both child endpoints equal X/67                      EXACT
child target weights sum <=1                         EXACT
variable-p affine hazard joint                       REMOVED
ordered-prime recursive color joint                  REMOVED
fixed-67 affine/collar integration                    RESIDENT / MERGED AUDIT
Riemann Hypothesis                                   UNPROVEN
```
