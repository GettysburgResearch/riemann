# PFR-T4 — Phase de-Poissonization is the critical explicit formula

Status: **PROVED STANDARD DISTRIBUTIONAL IDENTITY IN A NEW NORMAL FORM**
RH status: **unproved**
External novelty: **not claimed**

For `g in C_c^infinity((0,infinity))`,

\[
\begin{aligned}
\sum_\rho\int_0^\infty g(t)e^{(\rho-1/2)t}dt
={}&\int_0^\infty g(t)
\left[e^{t/2}+e^{-t/2}-{e^{-t/2}\over1-e^{-2t}}\right]dt\\
&-\sum_{n\ge2}{\Lambda(n)\over\sqrt n}g(\log n).
\end{aligned}
\]

The zeros are counted with multiplicity.  This is the positive-frequency
explicit formula obtained by Fourier transforming `PFR-T2` and undoing the
Poisson damping.

For a quartet `rho=1/2 +/- delta +/- i gamma`, its real contribution is

\[
4\cosh(\delta t)\cos(\gamma t).
\]

Thus the zero height is a real growth exponent and the zero ordinate is a real
frequency.  The formula does not itself prove that all growth exponents vanish.
