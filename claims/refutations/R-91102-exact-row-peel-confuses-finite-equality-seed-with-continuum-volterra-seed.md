# R-91102 — The claimed exact equality-row peel confuses the finite equality seed with its continuum Volterra model

Claim ID: `R-91102` (provisional research range)  
Status: **EXACT REFUTATION / LOAD-BEARING SCOPE CORRECTION**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-12  
Refutes: `L-91112.11`–`L-91112.24` and every downstream claim of exact finite outer saturation based on those displays  
RH status: **unproved**

## 1. The two seeds are different

The exact finite equality seed is

\[
 d_X^\star(m)=\sum_{k\le X/m}\frac{\mu(k)}{\sqrt{km}}
 \log\frac{X}{km},
 \qquad
 b_X^\star(n)=\sum_{m=n}^{X}d_X^\star(m).
\tag{R-91102.1}
\]

The Volterra inversion of `L-91107` instead generates the continuum seed

\[
 \overline b_X^\star(n)
 =\int_n^X d_X^\star(t)\,dt
 =\sqrt X\,\mathscr B^\star(n/X),
\tag{R-91102.2}
\]

where the summand in `d_X^star(t)` is interpreted with the causal cutoff
`k t<=X`.

In general

\[
 b_X^\star(n)\ne\overline b_X^\star(n).
\]

The former is a left Riemann sum and the latter is its integral. This is exactly
the finite/continuum mismatch treated asymptotically in `L-91303`; it cannot be
deleted by invoking the continuum endpoint inverse.

## 2. Exact counterexample at `X=3,m=2`

For `X=3,m=2`, only `k=1` occurs, so

\[
 \boxed{
 b_3^\star(2)=\frac1{\sqrt2}\log\frac32.
 }
\tag{R-91102.3}

On the other hand, throughout `2<=s<=3` one has `1<=3/s<2`, and therefore the
continuum equality density is

\[
 L(3/s)=2\sqrt{3/s}-1.
\]

Also

\[
 \partial_s b_s(2)=\frac{2\sqrt2}{s}-\frac4{s^{3/2}}.
\]

Hence the integral asserted equal to (R-91102.3) in `L-91112.11` is

\[
\begin{aligned}
 I
 &=\int_2^3(2\sqrt{3/s}-1)
 \left(\frac{2\sqrt2}{s}-\frac4{s^{3/2}}\right)ds\\
 &=8(\sqrt6+1)\left(\frac1{\sqrt2}-\frac1{\sqrt3}\right)
   -\frac{4\sqrt3}{3}
   -2\sqrt2\log\frac32.
\end{aligned}
\tag{R-91102.4}

The exact difference simplifies to

\[
\boxed{
 b_3^\star(2)-I
 =4\sqrt2-4\sqrt3+
   \frac{5\sqrt2}{2}\log\frac32>0.
}
\tag{R-91102.5}

The strict sign is elementary. Dividing by `sqrt(2)`, it is enough to note

\[
 \frac52\log\frac32>1
 \qquad\text{and}\qquad
 4\left(\sqrt{\frac32}-1\right)<1.
\]

The first inequality follows from
`log(1+x)>2x/(2+x)` at `x=1/2`; the second follows from
`sqrt(3/2)<5/4`.

Numerically the discrepancy is about

\[
 0.1621866566.
\]

No floating estimate is needed for the refutation.

## 3. Consequences

The invalid step is precisely

\[
 b_X^\star(m)
 \stackrel{\rm false}{=}
 \int_m^X L(X/s)\partial_s b_s(m)ds.
\]

What is true is

\[
 \overline b_X^\star(m)
 =
 \int_m^X L(X/s)\partial_s b_s(m)ds.
\tag{R-91102.6}
\]

Therefore the following conclusions of `L-91112` do not follow:

```text
exact finite equality-row representation;
exact nonnegative outer finite rows;
exact ordinary saturation by truncating those rows;
exact terminal-annulus saturation;
zero outer score debt from that truncation.
```

The infinitesimal row positivity proved in `L-91112` remains valid as a theorem
about the continuum endpoint frame. The positive component-row formula
`L-91112.25` is also an independent finite identity. They do not repair the
false equality (R-91102.6).

## 4. Correct surviving route

The valid finite route is:

1. use the positive continuum equality density on the certified factor-54
   window;
2. quantize it by the positive martingale B-spline of `L-91110`;
3. retain the finite Euler correction and quotient-knot packets of `L-91303`;
4. pay the positive width-three collar using `L-91111`;
5. treat the tapering terminal annulus by the bounded quotient-collar mechanism
   of `L-91306` or by a fixed top omission;
6. transfer the remaining source through the parity-resolved delayed renewal.

This route has bounded analytic/discretization debt but still requires the
capacity-faithful rough-prime allocation.

## 5. Exact boundary

```text
continuum Volterra identity                       VALID
finite equality seed = continuum Volterra seed    FALSE
L-91112 exact outer finite peel                    FALSE
L-91303 Euler correction                          RETAINED
L-91110/L-91111 positive quantization/collar      RETAINED
L-91306 terminal localization                     RETAINED
rough-prime capacity allocation                    OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVEN
```
