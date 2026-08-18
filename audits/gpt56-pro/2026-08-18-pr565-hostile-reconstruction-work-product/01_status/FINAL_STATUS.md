# Final status of the hostile reconstruction

## 1. First failed arrow: frozen L-97100

The candidate source uses

\[
q_\star(2)=15,\qquad q_\star(3)=6,\qquad q_\star(4)=3,
\qquad q_\star(m)=6\quad(m\ge5),
\]

\[
H_x(n)=\min\!\left(\log 4,\log\frac{x}{n}\right)_+,
\qquad
A_\star(x)=\sum_{m\ge2}\frac{q_\star(m)}{\sqrt m}H_x(m),
\]

and, for the product of primes through 61,

\[
F(x)=\sum_{d\mid P_{61}}\frac{\mu(d)}{\sqrt d}A_\star(x/d),
\qquad
M(x)=\sum_{d\mid P_{61}}\frac{1}{\sqrt d}A_\star(x/d).
\]

The frozen claim

\[
\frac1{40}\le \frac{F(x)}{M(x)}\le\frac18
\qquad(x\ge67)
\]

is false. At the exact finite point `x=184`, the independent high-precision computation gives

\[
F(184)=10.69357964877382995080531550498546\ldots,
\]

\[
M(184)=445.85760354260283631557807730110764\ldots,
\]

and hence

\[
\frac{F(184)}{M(184)}
=0.02398429355876630467327315865313\ldots
<0.025=\frac1{40}.
\]

Equivalently,

\[
F(184)-\frac{M(184)}{40}
=-0.4528604397912409570841364275\ldots<0.
\]

This is not a near-boundary numerical ambiguity.

## 2. Strongest scalar repair reached

The repaired window investigated in the pass was

\[
\boxed{\frac1{42}<\frac{F(x)}{M(x)}<\frac1{20}\qquad(x\ge67).}
\]

A corrected overflow-safe scan through `x=12,300,000` retained the margins

```text
minimum 42F-M      3.272741705896351...   at x=184
minimum M-20F     24.949644970914505...   at x=67
```

Because each margin is continuous and affine in `log(x)` between consecutive integer activation knots, endpoint checking is the correct continuum reduction on the covered finite range. The retained C++ scan is still classified as floating-point diagnostic, not an outward-rounded universal proof.

The analytic-tail work used the exact products

\[
\prod_{p\le61}\left(1-\frac1p\right)
=\frac{770527199232000}{5855632691117327},
\]

\[
\prod_{p\le61}\left(1+\frac1p\right)
=\frac{399441300081868800}{86204059532560853},
\]

alongside the annular comparison

\[
12\sqrt x-39\log2\le A_\star(x)\le12\sqrt x.
\]

The pass did not finish a publication-grade directed proof of the entire universal repaired window, so it remains labeled a strong repair candidate rather than a completed theorem.

## 3. Exact repaired contraction arithmetic

Taking the repaired upper bias `1/20` and recursive mass ratio `q=1/8`, the current upper constant is

\[
c=\frac{(1/20)+(1/8)(1/20)}{1-1/8}=\frac9{140}.
\]

The formal lower hereditary margin becomes

\[
\frac1{42}\left(1-\frac18\right)-\frac9{140}\frac18
=\boxed{\frac{43}{3360}}>0.
\]

This arithmetic is exact. It does **not** by itself prove that the recursion acts on the same literal source whose signed scalar is `F` and unsigned mass is `M`.

## 4. Composition frontier

The first unsupported compositional arrow is:

> the factor-67 recursion must act on a literal two-index positive source with unsigned mass exactly `M(x)` and signed observation exactly `F(x)`, and each recursively charged child must be an actual one-use source subpacket of that source.

The inspected materials did not complete this source-level theorem. In particular, scalar identities and comparison measures do not establish:

- first-owner uniqueness and disjoint ownership for the actual activated source;
- no double spending of reserve, target, or child mass;
- preservation of source normalization under every recombination;
- that the rough-child bound is measured on the activated source rather than a larger comparison object;
- a valid global common-source lift when parity histories are combined.

## 5. RH status

```text
Riemann Hypothesis: UNPROVED.
```
