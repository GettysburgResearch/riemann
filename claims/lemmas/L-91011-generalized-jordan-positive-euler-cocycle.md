# L-91011 — The zeta shift ratio has positive generalized-Jordan coefficients and a positive cocycle

Claim ID: `L-91011`  
Status: **EXACT EULER/ARITHMETIC LEMMA**  
Created: 2026-08-11  
Depends on: Euler products only  
RH status: **unproved**

## 1. Positive coefficient formula

For \(a>0\), define the arithmetic shift ratio

\[
 \mathcal J_a(s)
 =
 \frac{\zeta(s-a)}{\zeta(s+a)}.
 \tag{L-91011.1}
\]

In the half-plane of absolute convergence \(\Re s>1+a\),

\[
 \boxed{
 \mathcal J_a(s)
 =
 \sum_{n\ge1}\frac{c_a(n)}{n^s},
 \qquad
 c_a(n)
 =
 n^a\prod_{p\mid n}(1-p^{-2a})
 =
 \frac{J_{2a}(n)}{n^a}.
 }
 \tag{L-91011.2}
\]

Here \(J_\alpha(n)=n^\alpha\prod_{p\mid n}(1-p^{-\alpha})\) is the generalized
Jordan totient. Every coefficient is strictly positive.

Indeed the local factor is

\[
 \frac{1-p^{-s-a}}{1-p^{-s+a}}
 =
 1+\sum_{r\ge1}
 (p^a-p^{-a})p^{(r-1)a}p^{-rs},
 \tag{L-91011.3}
\]

whose coefficients are positive.

## 2. Positive shifted cocycle

The ratios obey the exact cocycle

\[
 \boxed{
 \mathcal J_{a+b}(s)
 =
 \mathcal J_a(s-b)\,
 \mathcal J_b(s+a).
 }
 \tag{L-91011.4}
\]

Equating coefficients gives

\[
 \boxed{
 c_{a+b}(n)
 =
 \sum_{de=n}
 c_a(d)c_b(e)d^b e^{-a}.
 }
 \tag{L-91011.5}
\]

Every summand is nonnegative. Thus the horizontal shift parameter has a
source-complete positive convolution law, although it is a shifted rather than
stationary semigroup.

## 3. Exact bridge to the elementary totient/Jordan route

At the critical half shift,

\[
 \boxed{
 c_{1/2}(n)
 =
 \frac{\varphi(n)}{\sqrt n}.
 }
 \tag{L-91011.6}
\]

At unit shift,

\[
 \boxed{
 c_1(n)=\frac{J_2(n)}n.
 }
 \tag{L-91011.7}
\]

Thus the completed shift/Clark family is not external to the repository's
analytic-totient and Jordan-energy programme. It continuously interpolates
its Euler-totient and \(J_2\) sources.

## 4. Completed factor

The completed ratio of `L-91010` factors as

\[
 \boxed{
 \Theta_a(s)
 =
 \pi^a
 \frac{(s-a)(s-a-1)}
      {(s+a)(s+a-1)}
 \frac{\Gamma((s-a)/2)}
      {\Gamma((s+a)/2)}
 \mathcal J_a(s).
 }
 \tag{L-91011.8}
\]

The finite pole/gamma factor supplies the archimedean part, while the entire
arithmetic deformation is the positive generalized-Jordan source.

## 5. Scope firewall

Coefficient positivity in (L-91011.2) is proved only in the natural absolute
half-plane \(\Re s>1+a\). The RH-sensitive Clark boundary is
\(\Re s=1/2\). Analytic continuation and preservation of the Schur/Pick or
soft-count monotonicity structure across that gap is precisely the hard
theorem.

Therefore

```text
positive generalized-Jordan coefficients
    do not by themselves prove RH;
```

but they give an exact positive source and cocycle for attacking the remaining
radial-curvature sign.
