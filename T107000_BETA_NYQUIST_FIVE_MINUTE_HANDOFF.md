# T-107000 beta Nyquist compression — five-minute handoff

Status: **new unconditional analytic compression; RH remains unproved**

Parent: PR #758 at `070be728e8d434bfb72645e23f9894acf920d3c0`.

## Read in order

1. `claims/lemmas/L-107000-logarithmic-box-cascade-has-near-exponential-fourier-decay.md`
2. `claims/lemmas/L-107001-exact-paley-wiener-sampling-of-native-beta-energy.md`
3. `claims/theorems/T-107000-near-quadratic-nyquist-native-beta-rh-criterion.md`
4. `claims/refutations/R-107000-polylogarithmic-rank-does-not-supply-arithmetic-cancellation.md`

## Result

One fixed compact source-faithful beta detector has exterior Fourier energy
smaller than every power beyond

```text
T_A(X) = O_A(log X (loglog X)^2).
```

Its complete energy is sampled **exactly** on the lattice

```text
t_k = 2*pi*k/(log X + O(1)).
```

After the every-power tail is removed, only

```text
O_A(log^2 X (loglog X)^2)
```

samples remain. Therefore RH is equivalent to the norm of one native beta
vector in an almost-quadratic-dimensional deterministic feature space.

## Live target

```text
NBV107000:
  the native beta feature vector has squared norm X^o(1).
```

This is RH-equivalent and unproved.

## Do not do

- Do not complete or square the beta source.
- Do not replace the fixed detector by an X-dependent one.
- Do not infer cancellation from the low rank.
- Do not take owner/core norms before native sign recombination.
