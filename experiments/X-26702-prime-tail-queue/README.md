# X-26702 — Prime-tail queue reconnaissance

This experiment evaluates the explicit ordinary-prime queue of `L-26704` for the parabolic seed.

```bash
python recon.py 100 1000 10000 100000 1000000
```

## Arithmetic class

```text
FLOATING_RECONNAISSANCE_ONLY
```

The script uses ordinary binary64 logarithms and square roots. It does not emit directed intervals or a proof certificate.

## Quantities

For

```text
r_X(p)=v_p(b_X^(0))-p^(-1/2) log(X/p),
```

it reports

```text
Q_X=max_P (sum_(P<=p<=X) r_X(p))_+,
```

the maximizing initial prime, and the last prime whose complete upper tail is positive.

The retained levels show a small, slowly growing queue and a last positive starting prime whose ratio to `X` rapidly decreases. This is consistent with the fixed-ratio theorem `L-26705`, but it is not evidence for the subpower theorem `PTQ`.

## Proof boundary

The exact queue and transport algebra are in `L-26704`. The fixed-ratio asymptotic theorem is `L-26705`. This experiment proves neither the shrinking-ratio estimate nor RH.