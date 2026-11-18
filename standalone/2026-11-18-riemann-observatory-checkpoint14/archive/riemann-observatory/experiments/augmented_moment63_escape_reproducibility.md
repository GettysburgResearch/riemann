# Augmented lattice moment escape figure

## Caption

**An unattainable limit for a lattice moment cost.** Each synthetic probability measure is supported on \(2,6,x\) with \(x=m(m-1)\) and has exact moments \((M_0,M_1,M_2)=(1,6,37)\). **A.** The positive cost gap \(c-1/4\) tends to zero. The leading term is \(3/(16x)\). **B.** Although the mass of the remote atom tends to zero, its contribution \(x^2w_x\) to the second moment approaches 1. The weak limit is the unit mass at 6, whose second moment is 36. Strict Jensen inequality for \(g(x)=4/(\sqrt{1+4x}-1)^2\) makes \(c=1/4\) unattainable at the prescribed positive variance \(37-6^2=1\). The figure uses synthetic measures. [Augmented moment audit](../audits/adversarial_reviews/augmented_moment63_review.md)

## Exact construction

The three weights are

\[
w_2=\frac1{4(x-2)},\qquad w_x=\frac1{(x-6)(x-2)},\qquad w_6=1-w_2-w_x.
\]

The cost is \(c=w_2+w_6/4+w_x/(m-1)^2\). Its exact expansion is

\[
c-\tfrac14
=\frac3{16x}+\frac{x-10+8/(m-1)}{8x(x-2)(x-6)}.
\]

For every \(m\ge4\), the remainder is positive and at most \(1/(8x^2)\). For the upper bound, the difference between its cross-multiplied numerator \(x(x-10+8/(m-1))\) and \((x-2)(x-6)\) is \(x(-2+8/(m-1))-12\), which is negative at \(m=4\) and remains negative for \(m\ge5\).

## Reproduction

From the repository root, run the following with Python and Matplotlib. The original render used Matplotlib 3.10.8 with the `Agg` backend. The script checks all 197 profiles for \(4\le m\le200\) using `Fraction`. All weights, the three prescribed moments, the gap identity and remainder bound, and the remote contribution are checked before conversion to floats for plotting. The JSON records every profile's exact weights and plotted quantities. [Source code](code/augmented_moment63_escape_figure.py) · [Exact checks](results/augmented_moment63_escape_checks.json)

```bash
python experiments/code/augmented_moment63_escape_figure.py
```

The figure is available as [PDF](results/augmented_moment63_escape.pdf), [SVG](results/augmented_moment63_escape.svg), and [PNG](results/augmented_moment63_escape.png). The PNG is rendered at 300 dpi. A second run in a temporary directory reproduced all three formats and the exact-check JSON byte for byte in the same environment.
