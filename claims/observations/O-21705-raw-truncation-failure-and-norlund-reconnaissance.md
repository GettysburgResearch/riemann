# O-21705 — Raw truncation failure and logarithmic Nörlund reconnaissance

Claim ID: `O-21705`  
Status: **HIGH-PRECISION / FLOATING RECONNAISSANCE — NOT A PROOF OBJECT**  
Scope: discovery and adversarial mutation for `T-21704`

## 1. Raw truncations leave the line

The direct symmetrization

\[
X_N^{\rm raw}(s)=m_N(s)+m_N(1-s)
\]

looked real-rooted at small levels. Higher-precision root finding and argument-principle counts found reflected off-line pairs.

Representative approximate roots are

\[
\begin{aligned}
N=75:\quad
&s=0.71058467639965048
 +111.46024679129043i,\\
&1-s^*=0.28941532360034952
 +111.46024679129043i;\\[1mm]
N=100:\quad
&s=0.89805406781177834
 +111.48438840407651i,
\end{aligned}
\]

with the reflected partner. Direct high-precision residuals were below `10^-90` in the discovery run. A rectangular winding count for `N=75`, height `120`, gave 38 strip zeros against 36 critical-line crossings.

No interval/Rouché certificate is committed, so this file does not classify the raw theorem as an exact refutation. It is nevertheless a mandatory mutation: a proof mechanism covering raw and Nörlund truncations indiscriminately is almost certainly proving a false surrogate.

## 2. Logarithmic Nörlund scan

For

\[
\mathcal X_N(s)
=\frac1{H_N}\sum_{K=1}^N\frac{m_K(s)+m_K(1-s)}K,
\]

the gamma-stripped function used in the contour calculation is

\[
Q_N(s)
=\overline D_N(s)
+\frac{g(1-s)}{g(s)}\overline D_N(1-s),
\qquad
 g(s)=\pi^{-s/2}\Gamma(1+s/2).
\]

This has the same zeros in the critical strip and avoids gamma underflow.

The retained ordinary floating-point scans found:

```text
N=75 raw, T=120       winding 38, line crossings 36
N=500 Nörlund, T=300  winding 138, line crossings 138
N=1000 Nörlund,T=2000 winding 1517, line crossings 1517
N=2000 Nörlund,T=2000 winding 1517, line crossings 1517
```

Earlier scans covered every `N<=100`, then every fifth level through `300`, and `N=350,400,450,500` through height `300`, with matching counts. Additional scans at `N=500` and `1000` through height `1000` gave 649 line crossings and winding 649.

The first positive critical-line zero moves toward the first Riemann ordinate:

```text
N=10    14.390466...
N=50    14.182512...
N=100   14.159961...
N=200   14.149857...
N=500   14.144079...
```

These values are not directed intervals.

## 3. Genericity mutations

The phenomenon is not generic.

- Random increasing phase-type rates can produce off-line zeros.
- Raw nested gamma cutoffs produce off-line zeros.
- Several alternative positive averaging rules eventually failed in exploratory scans.
- The exact square spectrum `n^2` and logarithmic occupation weights `1/K` therefore remain load bearing.

## 4. Discovery implications

The strongest present proof targets are:

1. a finite Hermite–Biehler or canonical-system realization;
2. a Gasper-style integral of squares;
3. a total-positivity theorem for the positive mixture of repeated-knot Dirichlet splines;
4. a Pólya/Lagarias–Suzuki zero-block inequality for the one-sided Mellin factor;
5. a nested phase-type Sturm comparison.

The scan does not select among them and does not establish BLNRZ.
