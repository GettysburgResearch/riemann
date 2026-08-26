# Genus-two detector conditioning on zero geometry

**Status:** exact finite, bounded, source-locked pushforward.

**Scope:** complete member-uniform monic squarefree quintic families over
exactly `q=3,5,7`, using only the existing `(a_D,b_D)` histograms and the
locked rational adapters for `P,D,S`. This packet enumerates no fields,
polynomials, curves, or members and finds no roots. It is not an asymptotic
zero theorem, a causal classifier, a monodromy diagnosis, or an RH result.

## 1. Spectral proxies and their exact meanings

Normalize the reciprocal quartic as

\[
 Q(Z)=Z^4-e_1Z^3+e_2Z^2-e_1Z+1,
 \qquad e_1=-a_D/\sqrt q,\quad e_2=b_D/q.
\]

If its unit-circle roots are written with cosine coordinates
`x=cos(theta_1)` and `y=cos(theta_2)`, then

\[
 Q(Z)=(Z^2-2xZ+1)(Z^2-2yZ+1),\quad
 e_1=2(x+y),\quad e_2=2+4xy.
\]

The two root-free, twist-invariant proxies are

\[
\begin{aligned}
 C&=Q(1)Q(-1)
   =(2+b_D/q)^2-4a_D^2/q\\
  &=16(1-x^2)(1-y^2)
   =16\sin^2\theta_1\sin^2\theta_2,\\
 G&=(a_D^2-4b_D+8q)/q
   =e_1^2-4e_2+8
   =4(x-y)^2.
\end{aligned}
\]

Thus `C=0` is an exact certificate that at least one normalized root is
`+1` or `-1`, while `G=0` is an exact repeated-cosine, equivalently
repeated-angle, certificate. A positive but small `C` or `G` is only a
finite-support proximity heuristic. This packet does not promote any
positive threshold to a zero event.

The producer verifies both polynomial identities over several exact rational
`(x,y)` probes and checks nonnegativity on all 251 locked source atoms.

## 2. Choice-free conditioning

There are no empirical quantiles, fitted cutoffs, or outer-tail definitions.
For each detector separately, the only partition is its predetermined exact
sign: negative, zero, or positive. The JSON retains the complete exact joint
`(C,G)` law in every nonempty sign stratum, its mean vector and covariance
matrix, and the exact `C=0`, `G=0`, and simultaneous-certificate counts.

The unconditional proxy census is:

| `q` | `mean(C)` | `mean(G)` | `C=0` members | `G=0` members |
|---:|---:|---:|---:|---:|
| 3 | `1244/243` | `464/81` | 0 | 0 |
| 5 | `17054/3125` | `3432/625` | 1 | 15 |
| 7 | `94184/16807` | `12896/2401` | 0 | 84 |

Absence at `q=3` and the field-specific counts at `q=5,7` are exact finite
facts only; no trend is inferred.

## 3. A stable `P/D` spectral contrast

The cleanest signal is a stable opposition between `P` and `D`. Listed below
are the positive- and negative-sign conditional means; zero strata remain in
the JSON rather than being silently merged.

| detector; `q` | `mean(C | +)` | `mean(C | -)` | `mean(G | +)` | `mean(G | -)` |
|---|---:|---:|---:|---:|
| `P`; 3 | `70/9` | `127/36` | `19/5` | `341/48` |
| `P`; 5 | `408/53` | `13208/3525` | `1034/265` | `1592/235` |
| `P`; 7 | `5359/686` | `19905/4949` | `759/196` | `9101/1414` |
| `D`; 3 | `128/45` | `988/153` | `41/5` | `218/51` |
| `D`; 5 | `5302/1295` | `5876/915` | `1864/259` | `784/183` |
| `D`; 7 | `23747/6517` | `23479/3430` | `996/133` | `2962/735` |

Across all three fields:

- positive `P` has larger mean `C` and smaller mean `G` than negative `P`;
- positive `D` has smaller mean `C` and larger mean `G` than negative `D`;
- correspondingly, `Cov(P,C)>0`, `Cov(P,G)<0`, `Cov(D,C)<0`, and
  `Cov(D,G)>0` in every field.

This is a repeatable three-field association, not a causal or asymptotic
classification. Both signs still carry broad `(C,G)` support.

The `S` behavior is less uniform. `Cov(S,C)<0` at all three fields, but
`Cov(S,G)` is negative at `q=3` and positive at `q=5,7`. Conditional sign
means and covariance need not tell the same story because detector magnitude
inside a sign stratum matters. This is precisely why the JSON keeps complete
joint conditional laws rather than reporting correlations alone.

## 4. Exact certificate incidence

The endpoint certificate occurs only once in the frozen families: at `q=5`
it lies in `P=0`, `D>0`, and `S<0`.

For the repeated-angle certificate:

| `q` | total `G=0` | `P: - / 0 / +` | `D: - / 0 / +` | `S: - / 0 / +` |
|---:|---:|---:|---:|---:|
| 3 | 0 | `0 / 0 / 0` | `0 / 0 / 0` | `0 / 0 / 0` |
| 5 | 15 | `0 / 5 / 10` | `0 / 0 / 15` | `10 / 0 / 5` |
| 7 | 84 | `0 / 42 / 42` | `0 / 0 / 84` | `42 / 0 / 42` |

So every `G=0` member at `q=5,7` has `D>0`. The converse is very false:
there are `1036` and `5586` positive-`D` members, respectively. This is an
exact finite enrichment and a strong warning against treating detector sign
as a certificate.

## 5. Same detector, different geometry

Exact equal-value collisions rule out memberwise recovery of zero geometry
from these detectors.

- At `q=5`, `P=0` occurs with `(C,G)=(0,16)`, `(5,1)`, and `(16,0)`.
  One detector value therefore spans an endpoint certificate, neither
  certificate, and a repeated-angle certificate.
- At `q=7`, `P=9792/2401` occurs both with `G=0` and with `G>0`.
- At every field, one `S` value has at least three distinct `(C,G)` pairs;
  at `q=7`, `S=0` has four.
- Exact same-value ambiguity for `D` occurs at `q=5`, where
  `D=16/25` has `(C,G)=(16/5,16/5)` and `(64/5,4/5)`. None occurs on the
  frozen `D` supports at `q=3,7`; this is a support fact, not an injectivity
  theorem.

The JSON gives deterministic coefficient-state witnesses and the number of
ambiguous values for every detector and field.

## 6. Provenance, boundary, and replay

The complete histogram fixture is pinned at LF-normalized SHA-256
`c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e`
and canonical payload hash
`50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c`.
The rational selector producer is pinned at
`48474ebcbb99efea23227126f66f566fdb525a3c9ae9e81a77bf83d4075f55e7`.
All primitive, note, and test hashes are verified before input parsing or
dynamic module execution. The three complete member-ledger hashes, schema,
coverage, atom counts, and member mass are also checked.

The transform visits exactly `32+81+138=251` source atoms and refuses above
the inclusive cap of `4096`. Its claim payload contains no floats.

Replay from the repository root:

```text
python research/l-families/atlas/function_field/genus2_detector_zero_geometry_conditioning.py --check
python -m unittest tests.test_genus2_detector_zero_geometry_conditioning -v
python -O -m unittest tests.test_genus2_detector_zero_geometry_conditioning -v
```
