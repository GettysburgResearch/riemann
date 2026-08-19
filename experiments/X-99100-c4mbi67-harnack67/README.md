# X-99100 — Exact segmented scan of the factor-67 Harnack defect

This experiment certifies the prefix

\[
 H_{67}(t)=\sum_{n\le t}\frac{b_{67}(n)}{\sqrt n},
 \qquad
 b_{67}(n)=a(n)-\mathbf1_{67\mid n}a(n/67),
\]

through `2,000,000,000`.

## Sparse coefficient

For `n=2^e 67^f m`, `(m,134)=1`,

```text
b_67(n) = 6*[n=1] - 6*[n=67]
          - 3*c2[e]*c67[f]*mu(m),

c2  = (2,-5,4,-1),
c67 = (1,-2,1),
```

with either local coefficient zero outside its displayed range.

## Segmented Möbius method

Each block stores two arrays:

- `rad[n]`: the product of distinct primes `q<=sqrt(R)`, `q!=2,67`, dividing
  `n`;
- `mu[n]`: the parity sign, set to zero on multiples of `q^2`.

After removing powers of `2` and `67`, any quotient not accounted for by
`rad[n]` is either `1` or one prime larger than `sqrt(R)`.  This supplies the
last Möbius sign without a full `O(N)` least-prime table.

For `S=2^40`, every term uses the exact integer `q_n` satisfying

```text
q_n^2*n <= S^2 < (q_n+1)^2*n.
```

Positive and negative terms are rounded in opposite directions to obtain a
rigorous interval.

## Fast verification

```bash
./replay.sh
```

## Full replay

```bash
FULL=1 ./replay.sh
```

The retained result is

```text
minimum lower numerator: 57,262,723,035
minimum upper numerator: 57,692,032,737
minimum endpoint:        61,848,971
scale:                   1,099,511,627,776
proof object:             e4534298fd460fdaef22065645a6abd25022f58a093580ca00321de29b8e17c4
```

The status flags intentionally retain `global_harnack67=false` and
`rh_established=false`.
