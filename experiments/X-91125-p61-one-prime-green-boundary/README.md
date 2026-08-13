# X-91125 — P61 one-prime Green-boundary domination

Companion replay for `L-91346`.

```bash
python3 experiments/X-91125-p61-one-prime-green-boundary/verify.py
```

Expected verdict:

```text
PASS_P61_ONE_PRIME_GREEN_BOUNDARY_DOMINATION
```

The standard-library checker uses exact `Fraction` arithmetic, directed fixed-point square-root and logarithm enclosures, and a one-dimensional bounded-Lipschitz/Kantorovich--Rubinstein boundary calculation. It certifies:

- all `2^18=262144` activation cells of the `P_61` finite Green error;
- `beta_61<1/400`;
- `|E|<7/6` and `Lip_log(E)<27/20` on the required range;
- the bounded-Lipschitz norm of every inherited row boundary `j=2,...,66`;
- a positive coefficient of `log p` in every row;
- the uniform lower bound `R_(p,y)(j)>1/500` for every real `p>=67` and `2<=j<=y<=67`.

The checker does not audit the remaining activation/frontier source-typing composition and does not prove RH.
