# Global S3 elliptic / ramified Prym adapter

Status: proposed reviewable mathematics, with bounded primitive replay.
Scope: function fields of smooth curves in characteristic greater than three.
RH and number-field GRH remain open. This does not bind the native integer
source in the companion programme.

[The proof](GLOBAL_S3_PRYM_SOURCE.md) starts from
`E:y^2=x^3+A*x+B`, the cubic map `t=y`, and the ramified double cover
`C:w^4=x^3+A*x+B`. It proves:

- For `A != 0` and nonsingular E, the S3 permutation augmentation is the
  earlier commutator Gram operator multiplied by `2/3`, including at ramification.
- The global standard factor is the degree-two elliptic numerator. Its
  Kummer twist by `t=w^2` is the degree-four anti-invariant/Prym numerator.
- Every ramified factor, the Frobenius convention, cup-product reciprocity,
  and the separately imported curve weight theorem are identified.
- On the smooth cyclic stratum `A=0`, the geometric commutator vanishes
  while the augmentation and cohomological factors survive.

The source equations precede all counts. [source.json](source.json) fixes
six curves over F5 and F7 and all four extensions of each base field.
[producer.py](producer.py) reconstructs polynomial finite fields, counts
every point, computes local traces including ramification, and checks the
exact low-degree determinants. Its maximum field has 2401 elements; no
external library or floating calculation is used.

Run from this directory:

```powershell
python -B -m unittest -v test_producer.py
python -B producer.py
python -O -B -m unittest -v test_producer.py
python -O -B producer.py
```

The checker rebuilds from primitive source and compares the artifact and
LF-normalized content bindings in `provenance.json`. The source has a fixed
canonical SHA256 in the producer. `--write` explicitly regenerates both
artifacts after a reviewed source change; it does not perform a check.
The external trust anchor is the reviewed Git commit containing all files,
not the mere existence of an internally consistent manifest.

The tests independently count the original equations over prime fields,
use multiplicative-group root counts over extensions, test irreducibility
against exhaustive small divisors, change the polynomial field model, and
exercise incorrect ramification, arithmetic parameters, and weight controls.
The four-extension Newton reconstruction of the Prym polynomial is independent
of reciprocity; a separate reconstruction using only the first two extensions
and the proved reciprocity predicts extensions three and four. Neither is
presented as a finite proof of the all-field result.

The initial replay passed all 24 extension-field panels and 16 substantive
tests in both ordinary and optimized Python. An extra independently prescribed
F7 branch (`A=B=4`, `t=3`, double root `x=1`) checks a negative Kummer sign.
Exact-SHA review is recorded separately after freezing.
No external priority for the classical elliptic/Kummer/Prym ingredients is
claimed. The new object is their explicit adapter to the prior holonomy
construction and its demonstrated deformation boundary.
