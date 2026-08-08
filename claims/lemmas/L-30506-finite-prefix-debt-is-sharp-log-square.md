# L-30506 — The coupled finite-prefix boundary debt is sharply logarithmic-square

Claim ID: `L-30506`  
Title: Every aggregate central-edge coefficient from row eight onward is negative, and the finite-prefix capacity debt has exact order `log^2 X`  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-30503`  
Scope: finite rows `n<X`; no statement about the analytic tail

Retain

\[
\beta(n)
=
\frac{\log(1+1/n)}{\sqrt{n+1}}
-\log n\left(\frac1{\sqrt n}-\frac1{\sqrt{n+1}}\right).
\tag{L-30506.1}

Multiplication by `sqrt(n+1)` gives

\[
\boxed{
\sqrt{n+1}\,\beta(n)
=
\log(1+1/n)
-\log n\,[\sqrt{1+1/n}-1].
}
\tag{L-30506.2}

## 1. Exact sign from row eight onward

For `n>=8`,

\[
\log(1+1/n)<1/n.
\tag{L-30506.3}

Also

\[
\sqrt{1+1/n}-1
=\frac1{n(\sqrt{1+1/n}+1)}.
\]

Since

\[
\sqrt{1+1/n}\le\sqrt{9/8}<17/16,
\]

one has

\[
\sqrt{1+1/n}-1>\frac{16}{33n}.
\tag{L-30506.4}

The atanh expansion gives

\[
\log2
=2\sum_{r\ge0}\frac{1}{(2r+1)3^{2r+1}}
>2\left(\frac13+\frac1{81}\right)
=\frac{56}{81}
>\frac{11}{16}.
\]

Therefore

\[
\log n\ge3\log2>\frac{33}{16}.
\tag{L-30506.5}

Combining (L-30506.3)--(L-30506.5),

\[
\log n\,[\sqrt{1+1/n}-1]>rac1n>\log(1+1/n),
\]

and hence

\[
\boxed{\beta(n)<0\qquad(n\ge8).}
\tag{L-30506.6}

Thus the coupled boundary does not become coefficientwise positive; its gain is quantitative capacity cancellation, not pointwise positivity.

## 2. Upper bound

`L-30503` already proves

\[
\sum_{n=2}^{X-1}\omega_n(-\beta(n))_+
\le\sum_{n=2}^{X-1}\frac{\log n}{n}
\le\frac12\log^2X+\log X.
\tag{L-30506.7}

## 3. Matching lower bound

For every `n>=64`,

\[
\sqrt{1+1/n}+1<3,
\]

so

\[
\sqrt{1+1/n}-1>\frac1{3n}.
\]

Using again `log(1+1/n)<1/n`,

\[
-\sqrt{n+1}\,\beta(n)
>\frac{\log n-3}{3n}
\ge\frac{\log n}{6n}.
\]

Since `sqrt(n+1)<=sqrt(2n)`,

\[
\boxed{
-\beta(n)
>\frac{\log n}{9n^{3/2}}
\qquad(n\ge64).
}
\tag{L-30506.8}

For the central edge, every integer

\[
\lfloor n/2\rfloor<q\le n
\]

is a carry. Hence

\[
\omega_n
=\sum_{q=2}^n\frac{\chi_n(q)}{\sqrt q}
\ge\sum_{\lfloor n/2\rfloor<q\le n}\frac1{\sqrt q}
\ge\frac13\sqrt n
\tag{L-30506.9}

for `n>=2`.

Equations (L-30506.8)--(L-30506.9) yield

\[
\sum_{n=64}^{X-1}\omega_n[-\beta(n)]
\ge\frac1{27}\sum_{n=64}^{X-1}\frac{\log n}{n}
\ge c\log^2X-O(1)
\tag{L-30506.10}

for one absolute `c>0`.

Therefore

\[
\boxed{
\sum_{n=2}^{X-1}\omega_n(-\beta(n))_+
=\Theta(\log^2X).
}
\tag{L-30506.11}

## 4. Meaning

The first aggregate boundary has three sharply different sizes in three gauges:

```text
divisor-source atomic norm       Omega(X);
coupled finite-prefix debt        Theta(log^2 X);
raw infinite-tail edge debt       divergent.
```

The proof strategy must therefore retain both the coupled flow and the all-scale tail commutator. Neither source total variation nor pointwise flow positivity reflects the correct cost.

## 5. Proof boundary

Closed exactly or elementarily:

1. negativity of every finite-prefix coefficient from row eight onward;
2. upper and lower logarithmic-square capacity bounds;
3. sharp separation of the three gauges above.

Open:

1. the all-scale paired-tail compression;
2. RH.
