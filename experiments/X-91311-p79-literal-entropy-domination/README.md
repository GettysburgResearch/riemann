# X-91311 — Uniform literal-entropy domination for the direct `P_79` splice

This standard-library replay certifies `L-91353`.

It performs four proof layers.

## 1. Complete finite Euler corridors

It streams all

```text
2^22 = 4,194,304
```

squarefree divisor activations of `P_79` and proves

```text
A_P79(x) < 1/5 for x >= 83;
|A_P79(x)| <= 1;
|B_P79(x)| < 3/2.
```

The reciprocal-square-root prefix uses fixed-denominator outward integer enclosures.

## 2. Complete compact entropy cells

For every real cell through `10,000`, the literal entropy gap

```text
F_a(x) = E_P79(x) - W_(a,P79)(x),  a in {4,5},
```

is concave as a function of `sqrt(x)`.  The checker evaluates both left and right activation endpoints with exact atanh logarithm intervals and proves

```text
F_4(x) > 18;
F_5(x) > 18;
```

for every `83 <= x <= 10,000`.

## 3. Elementary analytic tail

A finite prime scan and a central-binomial/prime-power estimate prove

```text
theta(t) - theta(79) > t/2 for every t >= 179.
```

The positive prime subsource of the component entropy then gives the analytic tail bound required beyond `10,000`, without importing the prime number theorem.

## 4. One-prime residual

The compact child corridor gives `F_a(y)<76` for `1<=y<83`.  Since `p^-1/2<1/9`, the exact residual gap is

```text
F_a(py) - p^-1/2 F_a(y) > 86/9
```

for both target (`a=4`) and declared score (`a=5`).

Run:

```bash
python3 verify.py
```

Expected output:

```text
PASS_P79_LITERAL_ENTROPY_DOMINATION
```

The certificate proves a raw-row entropy theorem.  It does not certify that the later finite-frontier conversion, collar, and one-use quantization retain this full literal entropy; that is the next proof interface.  RH is not claimed.
