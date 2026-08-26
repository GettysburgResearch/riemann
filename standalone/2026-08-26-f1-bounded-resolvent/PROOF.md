# Standalone proof — corrected F1 bounded detector and critical resolvent

## Theorem

Let

\[
K_L(y)=
\begin{cases}
8-4\sqrt y,&1\le y<2,\\
-8(1+\sqrt2)+4\sqrt2\sqrt y,&2\le y<4,\\
8\sqrt2-2\sqrt y,&4\le y<8,\\
0,&\text{otherwise},
\end{cases}
\]

and

\[
\widehat A(s)=
\frac{(1-2^{-s})(1-\sqrt2\,2^{-s})}
{s(s-\tfrac12)},
\qquad
P(s)=\frac12s(s-1)(5s+\tfrac32)(2s-1).
\]

Then:

1. the direct Mellin symbol is
   \[
   \widehat K_L(s)=
   \frac{4(s-1)(1-2^{-s})^2(1-\sqrt2\,2^{-s})}
   {s(s-\tfrac12)};
   \]
2. the exact bridge is
   \[
   (5s+\tfrac32)(1-\sqrt2\,2^{-s})\widehat K_L(s)
   =4P(s)\widehat A(s)^2;
   \]
3. after critical conjugation, the bounded spectral weight is
   \[
   \Omega_K(t)=
   \frac{
   16|P(\tfrac14+it)|^2r_A(t)^4
   }{
   ((\tfrac{11}{4})^2+25t^2)
   (1+\sqrt2-2\,2^{1/4}\cos(t\log2))
   }
   \asymp(1+t^2)^{-1};
   \]
4. the historical weight
   \(|P(\tfrac14+it)|^2r_A(t)^4\) is nondecaying and gives an infinite
   unregularized integral for every nonzero finite Dirichlet polynomial;
5. the corrected normal-ordered Beta fourth moment implies the bounded F1
   Gram, but its estimate remains open.

## Direct Mellin calculation

For constants \(c,d\),

\[
\int_a^b(c+d\sqrt y)y^{-s}\frac{dy}{y}
=
c\frac{a^{-s}-b^{-s}}s
+
d\frac{b^{1/2-s}-a^{1/2-s}}{1/2-s}.
\]

Apply this to the three intervals \([1,2]\), \([2,4]\), \([4,8]\).
Writing \(z=2^{-s}\), the numerator simplifies polynomially to

\[
4(s-1)(1-z)^2(1-\sqrt2 z),
\]

which proves the first formula.

Substitution of \(\widehat A\) and \(P\) then gives the bridge by direct
cancellation.

## Operator form and resolvent

Let \((\mathsf Sf)(X)=f(X/2)\). Its Mellin multiplier is \(2^{-s}\), hence

\[
(5D+\tfrac32)(I-\sqrt2\,\mathsf S)K_L
=
4P(D)(A*_MA).
\]

On the logarithmic line, \(\mathsf S=\tau_{\log2}\). Since \(\sqrt2>1\),

\[
(I-\sqrt2\,\tau_{\log2})^{-1}
=
-\sum_{j\ge1}2^{-j/2}\tau_{\log2}^{-j}.
\]

The series is bounded on every translation-invariant \(L^p\), with norm at
most \(1/(\sqrt2-1)\). Also

\[
[(5\partial+\tfrac32)^{-1}g](x)
=
\frac15\int_{-\infty}^xe^{-3(x-y)/10}g(y)\,dy,
\]

whose \(L^p\) norm is at most \(2/3\).

Thus total variation of the differential reflection current controls the
\(L^1\) norm of the bounded current. Differentiation prevents the converse.

## Critical conjugation

For \(C_{1/4}f(x)=e^{-x/4}f(e^x)\),

\[
C_{1/4}(5D+\tfrac32)C_{1/4}^{-1}
=
5\partial+\frac{11}{4},
\]

and

\[
C_{1/4}(I-\sqrt2\,\mathsf S)C_{1/4}^{-1}
=
I-2^{1/4}\tau_{\log2}.
\]

The latter multiplier has modulus

\[
|1-2^{1/4}e^{-it\log2}|^2
=
1+\sqrt2-2\,2^{1/4}\cos(t\log2),
\]

strictly bounded away from zero.

Since

\[
\widehat A(\tfrac14+it)=e^{-it\log2}r_A(t),
\]

the bridge gives the displayed formula for \(\Omega_K\).

The numerator \(r_A\) is comparable to \((1+t^2)^{-1}\),
\(|P(1/4+it)|\) is comparable to \((1+t^2)^2\), the differential denominator
is comparable to \(1+t^2\), and the dyadic denominator is bounded above and
below. Therefore

\[
\Omega_K(t)\asymp(1+t^2)^{-1}.
\]

## Why the old integral diverges

Without the denominator, the old weight is comparable to one. A nonzero finite
Dirichlet polynomial

\[
Q(t)=\sum_jq_je^{-it\lambda_j}
\]

has long mean square

\[
\frac1{2T}\int_{-T}^T|Q(t)|^2dt
\to\sum_j|q_j|^2>0.
\]

Therefore its integral against the old weight diverges.

## Correct Plancherel and Beta reduction

For the exact Boolean-normal-ordered amplitude

\[
\mathscr Q_U^\diamond(t)
=
\int_0^1(1-\theta)
:\!S_{U,\theta}(t)^2\!:_B\,d\theta,
\]

ordinary Plancherel gives

\[
\int e^{-x/2}|H_K^\diamond(e^x)|^2dx
=
\frac1{2\pi}\int
\Omega_K(t)|\mathscr Q_U^\diamond(t)|^2dt.
\]

Cauchy in \(\theta\) yields

\[
|\mathscr Q_U^\diamond(t)|^2
\le
\frac12\int_0^1(1-\theta)
|:\!S_{U,\theta}(t)^2\!:_B|^2d\theta.
\]

This proves the corrected fourth-moment implication. It supplies no estimate
for the right side.

## Conclusion

The corrected implication chain is

```text
F1KFOURTH105493
  -> F1KASQ105492
  <=> F1GRAM105480
  <=> F1HCNC105481
  -> F1HARDY105470
  -> RH.
```

Every premise remains open. RH is unproved.
