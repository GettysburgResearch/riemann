# X-2803 — D-0801 normalization fingerprint

Experiment ID: `X-2803`  
Agent: `gpt56-04-c`  
Issue: #28  
Status: exact integrity checker; theorem pending review  
Date: 2026-07-23

## Question

Can every producer and checker be bound to one explicit version of the D-0801
Guinand–Weil identity, so that a sign, frequency, Fourier, or zero-coordinate
mutation fails closed rather than silently producing a different theorem?

## Exact fingerprint

The canonical object fixes:

```text
Fourier forward:      integral g(t) exp(-2*pi*i*t*xi) dt
Fourier inverse:      integral hat_g(xi) exp(+2*pi*i*z*xi) dxi
zero coordinate:      (rho-1/2)/i
prime frequency:      log(q)/(2*pi)
prime coefficient:    -Lambda(q)/(pi*sqrt(q))
pole term:            +2*g(i/2)
archimedean term:     +(Re digamma(1/4+i*t/2)-log(pi))*g(t)/(2*pi)
normalized assembly:  A+R-h*S_K
```

The canonical SHA-256 is

```text
65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be
```

## Mathematical audit

T-2801 proves that the D-0801 piecewise autocorrelation family belongs to the
standard admissible Guinand–Weil class:

- `hat(g)` is continuous, compactly supported, and piecewise linear;
- its zero-extended derivative has bounded variation;
- two integrations by parts give uniform `O(|z|^-2)` decay on horizontal
  strips;
- the nontrivial-zero sum is absolutely convergent;
- compact support makes the prime side exactly finite;
- direct substitution fixes the source assembly as `A+R-h*S_K`.

The checker does not prove those analytic facts. It prevents later artifacts
from drifting away from the reviewed theorem.

## Reproduction

```bash
python verify_normalization.py \
  certificates/d0801-normalization.json \
  --output results/normalization-output.json

PYTHONPATH=. python -m unittest discover -s tests -v \
  > results/tests.txt 2>&1
```

Nine mutation tests reject changes to every load-bearing convention.

## Proof boundary

- T-2801 still imports the classical Guinand–Weil explicit formula rather than
  reproving it by contour integration.
- SHA-256 is an integrity binding, not mathematical evidence.
- A quantitatively negative fixed-vector interval still needs valid phase and
  prime-shard producers.
- Independent review must compare the displayed identity with a second primary
  normalization before promotion.

## Required downstream use

Every vector, alpha, prime-shard, correction, and final certificate artifact
should include this canonical digest. A mismatch invalidates composition even
when all numerical intervals are disjoint from zero.
