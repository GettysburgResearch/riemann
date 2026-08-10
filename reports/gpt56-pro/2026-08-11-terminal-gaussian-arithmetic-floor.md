# Session report: direct attack on the arithmetic corrected-kernel floor

## Verdict

The full matrix floor was not honestly closed. The attack did, however, remove its remaining matrix and main-term bookkeeping and reduce it to one explicit scalar oscillatory integral of the ordinary Chebyshev discrepancy.

The exact identity is

\[
W(f,f)=\Gamma(f)+R_{\rm low}(f)
+\int_0^\infty [\psi(e^t)-e^t+1]
 {d\over dt}\left(e^{-t/2}[k_f(t)+k_f(-t)]\right)dt.
\]

For the terminal Gaussian pair cardinal, the first two terms tend to zero, and the surviving scalar is written in closed form using a three-Gaussian shell. A hypothetical terminal off-line pair forces that scalar to tend to `-2m`.

Thus the requested corrected-kernel floor is equivalent to the terminal Gaussian Chebyshev gate in the proof note. This is now a one-frequency prime-cancellation theorem, rather than a Schur, Gram, tail, pole, gamma, or interpolation theorem.

## Main discovery

The pole contribution is not an independent large obstruction. Its growing half cancels *exactly* against the continuous `d(e^t)` main term of the prime measure. After writing

\[
\Theta(t)=\psi(e^t)-e^t+1,
\]

Stieltjes integration by parts leaves only the oscillatory discrepancy transform.

## Gaussian formula

For `z=x+iy`, `0<y<1/2`,

\[
F_{\sigma,z}(w)
=\frac{e^{-\sigma^2(w-\bar z)^2/2}
       -e^{-\sigma^2(w-z)^2/2}}
      {e^{2\sigma^2y^2}-1},
\]

and its autocorrelation is

\[
k_{\sigma,z}(t)=A_{\sigma,y}e^{-ixt}H_{\sigma,y}(t)
\]

with the explicit three-Gaussian `H` in the proof note. The real-axis mass is

\[
\int |F_{\sigma,z}|^2
=\frac{2\sqrt\pi(e^{\sigma^2y^2}-1)}
       {\sigma(e^{2\sigma^2y^2}-1)^2},
\]

so the gamma and lower-pole pieces vanish exponentially.

## Firewalls found

1. A phase-blind PNT envelope loses an exponential factor. Its saddle exponent is
   \[
   \sigma^2(1/4+y-3y^2)>0
   \]
   throughout the open critical strip.
2. Increasing trace-moment order while shrinking support stays below the resource line `r lambda < 2`; a single depth-`y` pair contributes at most `T^(2y+o(1))=o(T)` and remains invisible to normalized global moments.
3. Therefore the next proof must exploit oscillatory arithmetic cancellation at the precise ordinate `x`, or replace the observable by a genuinely stronger source-specific positive identity.

## Verification

The retained script reports

```text
PASS_TERMINAL_GAUSSIAN_ARITHMETIC_FLOOR_NORMAL_FORM
```

and checks the transform, autocorrelation, Stieltjes normal form, decay law, and moment-support barrier.

## Exact boundary

```text
completed-Chebyshev normal form       PROPOSED COMPLETE
Gaussian terminal scalar formula      PROPOSED COMPLETE
pole/main cancellation                PROPOSED COMPLETE EXACT
archimedean/lower-pole decay           PROPOSED COMPLETE
matrix floor -> scalar gate            PROPOSED COMPLETE, using PRs #364/#365/#199
terminal Gaussian Chebyshev gate       OPEN / RH-EQUIVALENT
corrected-kernel arithmetic floor      OPEN / RH-EQUIVALENT
Riemann Hypothesis                     UNPROVED
```
