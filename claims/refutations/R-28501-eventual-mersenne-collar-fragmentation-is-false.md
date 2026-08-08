# R-28501 — Eventual Mersenne-Collar Fragmentation is false

Claim ID: `R-28501`  
Title: The declared MCF edge menu has a dyadic Farkas ray whose eta-factor poles force infinitely many positive and negative endpoint values  
Status: **PROPOSED EXACT REFUTATION — complete proof submitted for independent review**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #285 at `61d0b66196f308981d36dbb8723d5e64d7a27533`, especially `T-28001`  
Dependencies: `L-28501`; the classical Landau theorem for Mellin transforms of eventually nonnegative functions  
Scope: refutes eventual feasibility of the exact MCF support menu; it does not refute unrestricted carry saturation, the eta/Mersenne source identity, PKRC, or RH

## 1. Frozen statement contradicted

`T-28001` asks that for every sufficiently large integer endpoint `X` there be a nonnegative exact carry-saturation flow supported on:

```text
binary central-window splits at non-Mersenne rows;
extreme splits at Mersenne rows.
```

The theorem also asks for a subpower Mersenne collar, but that extra estimate is irrelevant here. The support-feasible exact saturation itself is impossible cofinally.

## 2. The exact dual consequence

Let `Phi` and `mathfrak D` be the objects of `L-28501`:

\[
\Phi(1)=0,
\qquad
\Phi(n)=2^{\lfloor\log_2n\rfloor}-1\quad(n\ge2),
\tag{R-28501.1}
\]

and

\[
\mathfrak D(X)
=\sum_{q\le X}a(q)q^{-1/2}\log(X/q),
\qquad
\sum_{q\ge1}\frac{a(q)}{q^s}
=\frac{2^{-s}}{\eta(s)}.
\tag{R-28501.2}
\]

Every allowed MCF edge has

\[
\Phi(n)-\Phi(j)-\Phi(n-j)\ge0.
\tag{R-28501.3}
\]

Therefore every nonnegative exact MCF flow at endpoint `X` forces

\[
\boxed{\mathfrak D(X)\ge0.}
\tag{R-28501.4}
\]

No limiting argument is used in this implication.

## 3. Mellin singularities

`L-28501` proves initially for `Re(z)>1/2` that

\[
\boxed{
F(z):=
\int_1^\infty\mathfrak D(X)X^{-z-1}\,dX
=
\frac{2^{-(z+1/2)}}{z^2\eta(z+1/2)}.
}
\tag{R-28501.5}
\]

For every nonzero integer `k`,

\[
\eta\!\left(1+\frac{2\pi i k}{\log2}\right)=0,
\]

so `F` has a genuine pole at

\[
\boxed{
z_k=rac12+\frac{2\pi i k}{\log2}.}
\tag{R-28501.6}
\]

The numerator is nonzero and `z_k` is not zero. Zeta is finite at the displayed points; if it vanished there, the eta zero and hence the inverse pole would only have higher order.

On the positive real axis, `F` is regular. The alternating Dirichlet eta function is strictly positive for every real `s>0`, and `eta(1)=log2` is removable. Hence

\[
\boxed{F(x)\text{ is holomorphic at every real }x>0.}
\tag{R-28501.7}
\]

## 4. Passing from integer endpoints to a one-sign function

Suppose for contradiction that MCF holds for every integer `N>=N_0`. By (R-28501.4),

\[
\mathfrak D(N)\ge0\qquad(N\ge N_0).
\tag{R-28501.8}
\]

Let `mathfrak D_lin` be the piecewise-linear interpolation of these integer values. Then

\[
\mathfrak D_{\rm lin}(X)\ge0
\qquad(X\ge N_0).
\tag{R-28501.9}
\]

The interpolation estimate of `L-28501` is

\[
|\mathfrak D_{\rm lin}(X)-\mathfrak D(X)|
\ll X^{-3/2}(1+\log X).
\tag{R-28501.10}
\]

Therefore the Mellin transform of `mathfrak D_lin` differs from `F(z)` by a function holomorphic throughout `Re(z)>-3/2`, together with an entire compact-initial correction. It consequently retains every nonreal pole (R-28501.6) and has no positive-real singularity.

The coefficient bound in `L-28501` also gives polynomial growth, so the Mellin integral of `mathfrak D_lin` has a finite abscissa of convergence.

## 5. Landau contradiction

Landau's one-sign theorem says that the abscissa of convergence of the Mellin transform of an eventually nonnegative, nonzero function is a singular point on the real axis.

The pole (R-28501.6) forces the abscissa to be at least `1/2`: if it were smaller, the integral itself would be holomorphic at `z_k`.

Thus Landau forces a singularity at one positive real point. But Section 4 and (R-28501.7) show that the interpolated transform is holomorphic at every positive real point. This is a contradiction.

Therefore

\[
\boxed{
\text{MCF exact support-feasible saturation cannot hold for all sufficiently large integers.}
}
\tag{R-28501.11}

Applying the same argument to `-mathfrak D` shows that `mathfrak D(N)` cannot be eventually nonpositive either. Hence

\[
\boxed{
\mathfrak D(N)>0\text{ and }\mathfrak D(N)<0
\text{ each occur for arbitrarily large integers }N.
}
\tag{R-28501.12}

## 6. What failed structurally

The MCF support menu was designed to make the eta carry profile nonnegative away from Mersenne rows. The dyadic potential `Phi` is the exact dual shadow of that design. Its divisor coefficient contains

\[
\frac1{1-2^{1-s}},
\]

so it imports the nonreal dyadic boundary zeros on `Re(s)=1` before any zeta-zero question is reached.

The artificial eta poles are therefore not a removable numerical collar. They are a cofinal obstruction to the declared one-sided menu.

Any corrected positive-flow theorem must include additional exterior/parity edges whose dual action cancels the factor

\[
1-2^{1-s}
\]

before a one-sign Landau argument is attempted. This is precisely why a source-complete parity lift cannot be replaced by MCF support alone.

## 7. Exact disposition

```text
L-28001 eta/odd-Mobius resolvent identity       not contradicted
L-28002 eta carry sign classification            not contradicted
finite MCF LP feasibility at tested endpoints    not contradicted
T-28001 MCF for all sufficiently large endpoints FALSE
T-28001 as an RH proof                            REJECTED
PR #295 support-flow implication to MCF           cannot hold cofinally as stated
PKRC/parity-paired physical route                 remains open
unrestricted Carry Saturation                     remains open
Riemann Hypothesis                                unproved
```

## 8. Review checklist

A reviewer can decide the refutation without inventing a repair theorem. Verify only:

1. the MCF edge menu and (L-28501.4);
2. the finite divisor identity (L-28501.9);
3. the transform (R-28501.5);
4. the eta-factor poles (R-28501.6);
5. the interpolation error (R-28501.10);
6. the standard Landau one-sign theorem.

If all six pass, eventual MCF is false.