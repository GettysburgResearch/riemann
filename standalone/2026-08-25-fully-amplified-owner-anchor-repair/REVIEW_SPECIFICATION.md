# Review specification — fully amplified owner/anchor repair

Review `R-106095`, `L-106095--L-106096`, and `T-106100` before relying on
the superseded Q-indexed moment in `T-106090`.

## Reconstruction order

1. verify the least-discrepancy incidence and fixed-Q local family
   `L-106090--L-106092`;
2. reconstruct `R-106095.1--.2` and confirm that the Q-weight cancels the
   reciprocal Q source energy;
3. test the general `Q^theta` dual/diagonal incompatibility;
4. verify that all opposite owner products Q are summed inside
   `B_(alpha;g,ell,sigma,h)` before squaring;
5. for each Q in one quadratic class, construct `r_Q` with
   `Q*g^2=u_sigma*r_Q^2 mod ell`;
6. derive the exact even-character transform in the combined variable
   `r_Q*d`;
7. reconstruct the fully amplified member `Z_tilde_(g,ell,sigma,h)`;
8. verify the corrected source-dual weight `g^2*ell` and the dual sum
   `sum 1/(g^2*ell)`;
9. expand the literal atomic diagonal and verify the factor
   `ell^2/(g^2*c^2*d^2*P*Q)`;
10. write `c=ell*m` and reconstruct the harmonic bound in `L-106096`;
11. list every off-atomic-diagonal cross-incidence term without declaring
    it orthogonal;
12. inspect `FAPCX106100` and `FANEX106100` separately;
13. do not invoke `BCI102990` or the Mellin consumer before both corrected
    off-diagonal moments are genuinely closed.

## Firewalls

A proposed repair fails if it:

```text
uses the Q-indexed moment of the first T-106090 as controlling;
claims the Q factor is paid after it cancels 1/Q;
fixes Q, proves a local theorem and sums Q absolutely;
puts different Q fibres in an orthogonal coordinate after physical collapse;
omits the owner quadratic-class split when Q varies;
claims the whole same-anchor block is diagonal;
uses X-106100 as proof of the analytic off-diagonal moment;
claims BCI102990 or RH is proved.
```

## Current classification

```text
R-106095 Q-dimension correction          binding;
L-106095 fully amplified normal form     accepted internally;
L-106096 atomic diagonal                 accepted internally;
FAPCX106100                              open;
FANEX106100                              open;
BCI102990                                open;
RH                                       unproved.
```
