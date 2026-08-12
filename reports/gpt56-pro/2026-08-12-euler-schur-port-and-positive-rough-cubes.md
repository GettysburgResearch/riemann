# Euler Schur port and positive rough-prime support routing

Date: 2026-08-12  
Branch: `research/gpt56-pro/91101-moment-neutral-shadow-transport`  
Parent: PR #399  
Status: **new exact structural continuation; RH remains unproved**

## 1. Starting frontier

The preceding factor-54 work had already paid:

```text
finite target/continuum mismatch;
positive width-three quantization collar;
complete tapering terminal annulus;
all sixteen small-prime Boolean states.
```

The surviving problem was the delayed rough-prime renewal of the two critical
states `(L,R)`. `L-91311/L-91315` had found the unique centered balanced ray
whose square-root and constant ledgers both vanish, but its finite boundary port
and coefficient-one child routing were still open in capacity coordinates.

## 2. The Euler remainder is strictly subordinate to the native endpoint atom

For `N=floor(x)`, define

\[
 \rho(x)=\sum_{k\le N}k^{-1/2}-2\sqrt x-\zeta(1/2),
\]

\[
 \varrho(x)=\frac{2N}{\sqrt x}-\sum_{k\le N}k^{-1/2}.
\]

The second function is the positive endpoint-renewal atom of the factor-four
programme. `L-91316` proves globally

\[
 |\rho(x)|<\frac89\varrho(x).
\]

The close case is the left limit at `x=2`; a 16-term Euler-transformed eta
certificate proves the exact needed bound

\[
 -\zeta(1/2)>\frac{10\sqrt2-1}{9}.
\]

Thus the two functions

\[
 P_\pm=(\varrho\pm\rho)/2
\]

are strictly positive, and

\[
 \begin{pmatrix}\varrho&\rho\\\rho&\varrho\end{pmatrix}
 \succeq\frac19\varrho I_2.
\]

After all primes through 53 are included, the same pointwise matrix inequality
holds for the finite Boolean boundary port. Its native endpoint mass is exactly

\[
 \prod_{p\le53}(1+1/p)
 =\frac{3328677500682240}{742518990138757}<\frac92,
\]

and the absolute off-diagonal mass is below four.

For the normalized balanced ray `e_*`, the rough renewal becomes the exact
positive-port identity

\[
 \mathcal V_{53}
 =\sum_{m\in\mathcal M_{59}}m^{-1/2}e_*(x/m)
  +(\mathcal V_{53}+\mathcal B_{53}),
\]

where both external ports are positive and the output retains at least one
ninth of the diagonal reserve. The former signed additive boundary defect is
therefore embedded in a strict positive two-port colligation of bounded critical
mass.

This does not yet scalarize every individual rough child into finite detail
columns. It removes the need for an alternating or unbounded additive boundary
correction.

## 3. Rough Euler factors route support positively

For the positive parity atom

\[
 w_a(x,n)=a\sqrt x/n-1/\sqrt n,
\]

one active prime factor satisfies exactly

\[
 w_a(x,n)-w_a(x,pn)
 =(1-p^{-1/2})
 w_a(x(1+p^{-1/2})^2,n)>0.
\]

A fully active finite Boolean cube is therefore one positive dilation:

\[
 \sum_{d\mid P_Q}\mu(d)w_a(x,nd)
 =\beta_Qw_a(x\Gamma_Q^2,n)>0.
\]

At a finite cutoff, one prime splits exactly into a positive paired interior and
one positive activation frontier. For every `p>=59`:

```text
paired interior       n <= x/p < c0 x;
inner frontier        x/p < n <= c0 x;
outer frontier        c0 x < n <= x.
```

The first two pieces are supported below the contracted reset scale; the third
lies in the already feasible outer block. Unique least-prime labels prevent
branch duplication. Hence coefficient-one support routing of the complete rough
Euler tree is exact and positive.

## 4. What remains

In the diagonal modes

\[
 X=\sqrt xB,
 \qquad
 Y=A,
\]

a rough Euler factor is positive diagonal scaling. In the original `(L,R)`
coordinates the same map has one negative off-diagonal coefficient. Thus the
remaining issue is not support, additive boundary size, or infinite Euler
branching. It is one two-dimensional projective cone conversion:

> Convert the contracted square-root/constant packet back into the admissible
> positive `(L,R)` capacity wedge, using the strict endpoint Schur reserve and
> the positive reserve coefficient left by the balanced ray.

The exact frontier is now:

```text
additive balanced boundary port                 CLOSED IN POSITIVE TWO-PORT FORM
rough-prime coefficient-one support routing     CLOSED EXACTLY
outer and terminal finite columns               CLOSED AT BOUNDED COST
projective (L,R) state-type conversion           OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```

## 5. Replay

```bash
python3 experiments/X-91108-euler-remainder-schur-port/verify.py
sha256sum -c experiments/X-91108-euler-remainder-schur-port/SHA256SUMS
```

Retained verdict:

```text
PASS_EULER_REMAINDER_SCHUR_PORT_AND_POSITIVE_CUBES
```
