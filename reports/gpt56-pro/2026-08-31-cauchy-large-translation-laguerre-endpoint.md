# Cauchy translation: the large-height Laguerre endpoint

## Summary

The corrected T-105660 programme already proved constant-one CTI at first
contact and the sharp universal `32/27` bound at every height. This pass
proves the opposite endpoint.

For a rank-`n` exponential packet `K`, let

```text
T_H = multiplication by exp(-H x);
Q_H = projection onto T_H^2 K.
```

If `kappa_K` is the squared norm of evaluation at zero, then

\[
\operatorname{tr}(PT_HP)
 =\kappa_K/H+O_K(H^{-2}),
\]

\[
\operatorname{tr}(PQ_H)
 =n\kappa_K/H+O_K(H^{-2}).
\]

The factor `n` is universal. After dilation, the deep packet converges to

\[
e^{-2y}\operatorname{span}\{1,y,\ldots,y^{n-1}\},
\]

whose orthonormal Laguerre modes each have integral of modulus one.

Therefore CTI is strict for every sufficiently large translation at every
rank. Combined with the first-contact theorem, any counterexample must be a
rank-at-least-three finite intermediate-height stationary contact. The exact
value and derivative equations for such a contact are now written without
any matrix-order premise.

## New files

- `L-105670` large-translation Laguerre theorem;
- `L-105671` stationary-contact ledger and symmetry reductions;
- `T-105670` revised two-ended frontier;
- `X-105670` exact Laguerre/Cauchy replay;
- `M-105670` hostile review contract.

## Replay

```text
PASS_T105670_CAUCHY_LAGUERRE_ENDPOINT
checks=97
28e5db953aaccd25a328f7380b9d8162407c54ada77dc640c895531aff54eaaa
```

## Boundary

```text
CTI near zero                         proved all ranks
CTI at large translation              proved all ranks
rank one and rank two                 proved all heights
sharp 32/27 theorem                   proved all ranks/heights
intermediate stationary contact       open
arbitrary-rank CTI all heights        open
cofinal/pointwise Xi interfaces       open
RH                                    unproved
```