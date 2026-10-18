# The exact positive modular representation and its missing transfer

Status: an analytic route assessment. The identities in Sections 1--2 are
exact and unconditional; their basic probabilistic content is classical.
They do not establish the all-order Stieltjes positivity required for RH,
or a smaller zeta zero strip. The obstruction in Section 3 explains why an
automatic transfer from the positive representation would be invalid.

## 1. An actual all-order positive representation

Let \(G_{h,n}\), \(n\ge1\), be independent gamma variables with shape
\(h>0\) and rate one. Define

\[
 \Sigma_h=\frac{2}{\pi^2}\sum_{n\ge1}\frac{G_{h,n}}{n^2}.
\]

This is a finite positive random variable almost surely, since the sum of
the expectations converges. Its Laplace transform is

\[
 L_h(\lambda)=\mathbb E e^{-\lambda\Sigma_h}
    =\prod_{n\ge1}\left(1+\frac{2\lambda}{\pi^2n^2}\right)^{-h}
    =\left(\frac{\sqrt{2\lambda}}{\sinh\sqrt{2\lambda}}\right)^h,
 \qquad \lambda\ge0.                                           \tag{1}
\]

In particular

\[
 -\frac{d}{d\lambda}\log L_h(\lambda)
     =h\sum_{n\ge1}\frac1{\lambda+\pi^2n^2/2}.                  \tag{2}
\]

The right side is a Stieltjes transform of an explicitly positive discrete
measure. This is a full positive gamma-convolution construction, not a
finite moment fit.

The Jacobi identity gives the Mellin transforms, with the following
normalizations (Biane--Pitman--Yor, Section 3, Table 1):

\[
 \begin{split}
 \mathbb E\Sigma_2^{s/2}
    &=(2/\pi)^{s/2}\,2\xi(s),\\
 \mathbb E\Sigma_1^{s/2}
    &=\frac{2^{1-s}-1}{1-s}\,(2/\pi)^{s/2}\,2\xi(s).
 \end{split}                                                     \tag{3}
\]

Both sides are entire in \(s\), with the value at \(s=1\) interpreted by
continuity. All real powers of \(\Sigma_h\) have finite expectation:
positive moments follow from exponential tails; for any required negative
power one can retain a sufficiently long finite gamma sum as a lower
bound for \(\Sigma_h\).

Formula (3) is the exact arithmetic content of this construction. The
positive measure in (2) has atoms at the elementary spectrum
\(\pi^2n^2/2\). It is **not** the putative positive measure for the
logarithmic derivative of \(\xi(1/2+\sqrt x)\).

## 2. A positive scaling identity, checked directly

Let \(U\) be uniform on \([1,2]\), independent of \(\Sigma_2\). Then

\[
 \Sigma_1\ \stackrel d=\ \frac{\Sigma_2}{U^2}.                   \tag{4}
\]

Indeed, for \(x=\sqrt{2\lambda}>0\),

\[
 \begin{split}
 \int_1^2 L_2(\lambda/u^2)\,du
  &=\int_1^2\frac{x^2}{u^2}\operatorname{csch}^2(x/u)\,du\\
  &=x\int_{x/2}^x\operatorname{csch}^2v\,dv\\
  &=x\{\coth(x/2)-\coth x\}
   =\frac{x}{\sinh x}=L_1(\lambda).
 \end{split}
\]

Uniqueness of Laplace transforms proves (4), and the case \(\lambda=0\)
follows by continuity. Taking Mellin transforms yields exactly the
additional factor in (3), because

\[
 \mathbb E U^{-s}=\int_1^2u^{-s}\,du
             =\frac{2^{1-s}-1}{1-s}.                            \tag{5}
\]

Since \(\Sigma_2\) is also a sum of two independent copies of
\(\Sigma_1\), this gives a positive distributional fixed-point equation.
It does not express the logarithm of the Mellin transform as a Laplace
transform of a positive measure. The addition in the random-variable
equation is transformed multiplicatively by Laplace transforms, whereas
the independent scaling is transformed multiplicatively by Mellin
transforms; these are different operations.

## 3. Why positivity has not crossed to the required logarithm

The shape-one variable in (1) already supplies a decisive test of an
overbroad proposed transfer theorem. It has the same positive \(n^2\)
spectrum and an explicitly Stieltjes logarithmic Laplace derivative.
Nevertheless its Mellin transform has zeros at

\[
 s=1+\frac{2\pi i k}{\log2},\qquad k\in\mathbb Z\setminus\{0\},
                                                                    \tag{6}
\]

by (3). The factor \(\xi(s)\) is entire, so it cannot cancel these zeros.
Thus the positive gamma-convolution representation, by itself, does not
confine the Mellin zeros to \(\operatorname{Re}s=1/2\), or even to any
strictly smaller right-hand boundary than one. This is a statement about
the proposed general inference, not about zeros of the target \(\xi\).

For the shape-two law, the wanted function is

\[
 f(x)=\frac{\xi(1/2+\sqrt x)}{\xi(1/2)}.
\]

Its log derivative being Stieltjes would mean a representation

\[
 \frac{f'(x)}{f(x)}=\int_{[0,\infty)}\frac{d\nu(t)}{x+t},
 \qquad \nu\ge0,                                                \tag{7}
\]

with the appropriate convergence. Under RH the atoms are the squares of
the critical zero ordinates, counted with multiplicity; conversely the
analytic continuation of a Stieltjes transform rules out poles of the
logarithmic derivative off the negative axis. Thus (7) contains the
unresolved zero-location content. It is not obtained by substituting (2)
into a Mellin integral, taking a logarithm through that integral, or
dividing by the factor in (5).

The exact modular identities therefore identify a useful positive
starting object, but this pass has not supplied the missing all-order
positive measure for the target logarithm. Any future construction from
(1) must exploit the specific shape-two Mellin structure in a way that
survives the counterexample (6).

## Primary source

P. Biane, J. Pitman, and M. Yor, *Probability laws related to the Jacobi
theta and Riemann zeta functions, and Brownian excursions*, Section 2,
Section 3 and Table 1: <https://arxiv.org/pdf/math/9912170>.

The preceding statements do not rely on recent manuscripts claiming a
Thorin or GGC factorization for the reciprocal xi function. In particular,
infinite divisibility of some reciprocal transform, if available, must not
be confused with the stronger Stieltjes property in (7).
