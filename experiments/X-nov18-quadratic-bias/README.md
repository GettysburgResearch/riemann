# Reflected prime-tail witnesses through conductor 10,000

The integer-interval calculation certifies sign-changing integrated prime races for 5,941 of the 6,086 nonprincipal fundamental discriminants with absolute value at most 10,000. There are 2,939 witnesses among 3,043 negative discriminants and 3,002 among 3,043 positive ones. Each row gives the tested integer phase \(X\) and a rounded-down bound for \(-1000K_\chi(-\log X)\) under individual GRH. The strict comparison with \(2/3\) uses the unrounded integer. Combined with Chua's and Watkins's real-zero theorems, the resulting sign changes for the integrated prime sums hold unconditionally, as proved in the [sign dichotomy](../../research/explorations/zhao-bias-unconditional-nov18.md).

Run the following with Python 3 and NumPy.

```sh
OPENBLAS_NUM_THREADS=1 python census.py --output witnesses.tsv.xz
```

The uncompressed TSV has SHA-256 `e9cf7436a7a4912df1aa64865785231244d1b2c13a72e0613dfac0860f99de4a`. The count includes 4,977 discriminants outside the span of the reported 381 candidates in Zhao's §8(2). Inside that span it includes witnesses from the explicitly printed Tables 2 and 3, prompting a correction to the asserted inclusion in that concluding remark. See the [discussion and independent one-point verification](../../research/explorations/zhao-bias-unconditional-nov18.md).

Let \(b_j=-(L'/L)(j,\chi)\), \(j=1,2\). For integer \(X\ge1\), dividing the [reflected identity](../../research/explorations/zhao-bias-kernel-nov18.md) by \(-\sqrt X\) gives the expression
\[
 b_1-Xb_2+\sum_{n\le X}(X-n)\Lambda(n)\chi(n)/n^2
 +X^{-1-a}\sum_{h\ge0}\frac{X^{-2h}}{(1+a+2h)(2+a+2h)} .
\]
Here \(a\) is zero for positive discriminants and one for negative discriminants. Each positive archimedean term follows by expanding \((1-e^{-2y})^{-1}\) in the integral. The implementation keeps up to 128 terms, rounding them down individually. At \(j=1\) the ordinary twisted von Mangoldt series converges by the fixed-character prime number theorem, and at \(j=2\) convergence is absolute.

For the arithmetic ratios, truncate the character series for \(L,L'\) at \(N=16|D|\). For any decreasing positive weight \(f\) beyond this whole-period endpoint the omitted signed sum has magnitude at most \(M f(N)\), where \(M\) is the largest absolute character prefix sum in one period. This applies to the four weights used. Logs use Python's correctly rounded Decimal.ln at 37 significant digits. Each scaled floor is within two integer units of its exact value at scale \(2^{40}\), since the scaled quantities are smaller than \(2^{42}\). Interval endpoints for each ratio are rounded outward by exact integer division. The total absolute normalized finite-prime weight rounding cost is below \(2 X^2\) scaled units. All vector sums and products before the selection have magnitude below \(2^{63}\), e.g. \(\sum_{n\le4096}\log n/n^2<2\) by integral comparison. For each character a floating maximum only selects a phase to check. The positivity and the final squared strict inequality at that phase use integer arithmetic. Positive and negative signs correspond respectively to arbitrarily late positive excursions and at least the negative almost-periodic mean, as in the linked sign dichotomy. A missing row asserts no sign conclusion.

## Refinement stages

Run `python refine.py`, `python spectral.py` and `python classify_li.py` in this directory with NumPy and python-flint installed. The first two start with the exceptions from the previous stages. The final one independently covers every nonprincipal conductor below 130 and checks the uniform cutoff. The stages use 128, 80 and 96 bits of Arb precision, respectively.

In `refine.py`, the four initial weights use a \(2^{56}\) scale, with the same two-unit bound per weight and no possible signed 64-bit overflow since \(\sum_{n\le160000}(1+\log n)/n<100\). For \(j=1,2\) the exact remaining Dirichlet series past \(16q\) and its derivative are obtained by summing
\[
 q^{-s}\sum_{k\ge1}(-1)^k(s)_k\zeta(s+k,16)M_k/k!,
 \qquad M_k=\sum_{r=1}^q\chi(r)(r/q)^k
\]
at \(s=j\). The constant term vanishes and the expansion follows by Taylor expansion of \((m+r/q)^{-s}\) for \(m\ge16\). At \(k\ge25\), the binomial coefficient is at most \(k+1\), its derivative at most \((k+1)^2\), and \(|M_k|\le q\). Integral comparison gives \(\sum_{m\ge16}(1+\log m)m^{-j-k}\le 10\cdot16^{-k}\). Together with \(q^{1-j}\le1\) and \(\log q<10\), the entire omitted value or derivative is smaller than \(\sum_{k\ge25} 10(k+12)^2 16^{-k}<10^{-23}\). The candidate phase search uses floating arithmetic followed by an Arb evaluation of the selected finite formula. The Cauchy majorant and low-zero checks are proved in the [classification note](../../research/explorations/zhao-bias-classification-nov18.md).

Starting from the first-stage 5,941, periodic summation certifies 98 further cases and real Hardy sign changes below 19/26 certify 14 more. In combination this gives **6,053 unconditional sign-changing cases through 10,000**. Of the 33 others, 19 have negative eventual sign on their individual GRH. The remaining 14 here have conductor at most 73.
