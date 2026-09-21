# PET26 — coupled prime-extension transport

**Proposed component mathematics, pending independent review. RH/GRH and the
native all-scale Newton gain remain open.** Additive continuation of #903;
parent reading snapshot `519252721d8b4e4c70c0fd1f21d8c9465242b338`.

BCP26 and SBC26 established that separately bounding positive prime/pivot
blocks discards essential native cancellation. This pass proves an actual
uniform SIGNED estimate instead of proposing another positive partition.

For b=Y+1, a=log b, set

    E = integral_1^b M(x)^2 dx/x^2,
    I = integral_b^(b^2) M(x)^2 dx/x^2,
    P_Y = sum_(p prime) log(p) integral_b^(b^2) M(x)M(x/p) dx/x^2.

Every prime is kept with all its composite multiples. Explicit finite
prime-power window masses give d_b,h_b with

    P_Y <= -d_b*I + h_b*sqrt(E*I),
    (P_Y)_+ <= h_b^2/(4d_b)*E                 when d_b>0.

The proof gives d_b~(3/4)log b and h_b~(1/2)log b using only the classical
PNT. In particular

    (P_Y)_+ <= (1/12+o(1))*log(b)*E.

**This is not PCR26's full covariance.** It is an explicitly defined native
prime-dilation observable. The theorem bounds its POSITIVE part; controlling
a large negative magnitude is still necessary to obtain a new energy upper
bound. The sign/direction limitation is proved and discussed next to the
conditional consumer in PROOF.md, Section 7.

## What is new in this continuation

- Exact cancellation of the prime-power tail to single repeated-prime
  insertions, plus an early/late Schur estimate that pays all those terms.
- A finite, computable signed upper bound and its all-scale asymptotic.
- The logarithmic Newton-defect identity L_A(N(c))=2e*L_A(c), including the
  excluded square endpoint and arbitrary modifications after the prefix.
- A separate #738 adapter: finite local logarithmic-tail numerators for
  GL(2), the opposite inert-prime sign, and exact good-prime point counts
  for E_17 and E_53. Existing rank-deflation and CM fixtures are not replaced.

The logarithmic derivative identity, Euler algebra, PNT and Schur test are
classical. No broad priority claim is made for these ingredients.

## Complete finite example, Y=255

| Quantity | Descriptive decimal |
|---|---:|
| Known prefix E | 1.407569576725774 |
| Whole annular energy I | 0.179852003503374 |
| Signed prime-extension P_Y | -1.661488670264158 |
| Higher-prime-power correction | 0.260191372879282 |
| Log-weighted annular energy | 1.480561725271574 |
| Primitive cross term | 0.079264427886698 |
| Finite damping d_b | 2.541184385294153 |
| Finite early/late coupling h_b | 4.961459884257196 |
| Actual completed A_B | 1.587579815075734 |

The three signed quantities obey

    P_Y + C_powers + log_energy = primitive_cross.

Both signed means and the completed state are recorded. The finite bound
on P_Y is about 2.03929 at this cutoff: the theorem does not itself force
this observed negative value. The asymptotic 1/12 is NOT substituted into
finite certificates.

All seven complete stages Y=3,7,15,31,63,127,255 are replayed. This includes
87,369 coefficient indices counting overlapping ranges, and every cell
through 65,535 in the largest case. Finite prime covariances are negative
in these examples; no all-scale sign assertion is inferred.

## Replay

Python standard library only, no external service, site package, or network:

```sh
python -S -B check.py --check result.json
python -S -B verify.py result.json
python -S -B algebra.py
python -S -B test_check.py
```

All four commands also run with `-O`. `verify.py` imports neither the
producer nor repository code; it shares exact.py's interval primitives and
rechecks the core observables by trial factorization and reverse summation.
Its narrower scope is explicit in VALIDATION.md. The two implementations
have one author; they are not independent mathematical review.

## Reading order and scope

Read [PROOF.md](PROOF.md), especially Sections 3-5 and 7, then
[LFAMILY.md](LFAMILY.md) and [VALIDATION.md](VALIDATION.md).
[SOURCES.json](SOURCES.json) freezes the external and repository inputs.
No previous file, canonical claim status, CI workflow or repository setting
is changed by this packet. Next work belongs on the magnitude of signed
prime/composite compensation, not another isolated positive prime block.
