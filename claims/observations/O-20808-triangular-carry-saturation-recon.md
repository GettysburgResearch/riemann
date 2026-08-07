# O-20808 — Triangular carry-saturation reconnaissance

Observation ID: `O-20808`  
Title: The canonical carry coefficients remain nonnegative through one million and reproduce the complete prime ramp  
Status: `ORDINARY NUMERICAL RECONNAISSANCE — NOT DIRECTED, NOT COFINAL`  
Authoring agent: `gpt56-03-x`  
Created: 2026-08-07  
Dependencies: `L-20815`; `L-20816`; `T-20805`; `X-20809`

## 1. Fast exact-algebra reconstruction

The direct backward solve is quadratic if implemented literally. `R-20805`
gives an equivalent `O(X log X)` adjoint reconstruction:

\[
 u_m=\sum_{k\le X/m}\mu(k)w_X(mk),
 \qquad
 z_m=u_m-u_{m+1},
\]

\[
 C_j={j u_j+\sum_{m=j+1}^Xu_m\over j(j-1)},
 \qquad
 c_X(j)=(j+1)(C_j-C_{j+1}).
\]

The two implementations agree at small and medium cutoffs to ordinary
roundoff.

## 2. Retained scale table

All logarithms and square roots in this table use ordinary binary floating
arithmetic. `num_negative` counts coefficients below `-1e-12`; the endpoint
`c_X(X)=0` is omitted from `min_positive`.

| `X` | `num_negative` | `min_positive` | `L_X-4 sqrt(X)` | `sum c log(n+1)` | binomial objective | direct prime ramp | identity error |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 100 | 0 | `1.030710978e-3` | `-4.023723529` | `18.17977682` | `23.871583097448326` | `23.871583097448330` | `-3.6e-15` |
| 1,000 | 0 | `3.171786544e-5` | `-1.670013804` | `31.45810364` | `104.17964562563871` | `104.17964562563837` | `3.4e-13` |
| 10,000 | 0 | `1.000300070e-6` | `0.907762463` | `45.15283744` | `371.51241548110335` | `371.51241548110056` | `2.8e-12` |
| 100,000 | 0 | `3.162372531e-8` | `3.540141622` | `58.96231318` | `1230.2452192635135` | `1230.2452192635267` | `-1.3e-11` |
| 1,000,000 | 0 | `1.000003000e-9` | `6.176043972` | `72.79217008` | `3959.152608993545` | `3959.1526089937815` | `-2.4e-10` |

Here

\[
 L_X={1\over2}\sum_{n=2}^Xn c_X(n).
\]

The coefficient budget grows slowly, while the leading objective has crossed
above `4 sqrt(X)` by `X=10,000`. The proof of `T-20805` does not require this
sign; it uses the weaker rigorous target

\[
 L_X\ge4\sqrt X-O(\log^2X).
\]

## 3. Million-level normalization check

At `X=10^6`, the complete von Mangoldt ramp is

```text
3959.1526089937815
```

and the independent factorial/binomial contraction is

```text
3959.1526089935450.
```

The difference is about `2.36e-10` in ordinary arithmetic.

Using the exact archimedean formula from `L-20809`,

```text
A(log 10^6) = 3959.18960391481037903963363909992488...
```

so the corresponding ordinary screw value is

```text
Psi(log 10^6) = 0.03699492102884...
```

This is a normalization check only.

## 4. Additional structural observations

1. The intermediate Möbius sequence `u_m` has many negative entries.
2. Its first difference also has both signs.
3. Positivity appears only after the final averaging-adjoint inversion.
4. The scaled profile `n^(3/2)c_X(n)` appears stable at fixed `n/X`.
5. The formal limiting profile has the reciprocal-zeta transform recorded in
   `R-20805`, so finite positivity cannot be extrapolated without proof.

## 5. Exact synthetic regression

`X-20809` separately verifies with `Fraction` arithmetic:

- the closed formula for `beta_(nq)` against exhaustive carry counting;
- exact reconstruction of a rational positive coefficient vector from its
  generated target;
- the adjoint Möbius reconstruction;
- equality of the direct and factorial coefficient contractions.

The Riemann-data table above is intentionally kept separate from that exact
synthetic result.

## 6. Proof boundary

The computation supports the Carry Saturation Lemma over a substantially larger
range than the earlier square-screw scans. It does not establish

\[
 \forall X\ \forall n\le X:\ c_X(n)\ge0.
\]

No finite cutoff can replace that quantifier. `R-20805` explains why the missing
step is analytically load bearing.