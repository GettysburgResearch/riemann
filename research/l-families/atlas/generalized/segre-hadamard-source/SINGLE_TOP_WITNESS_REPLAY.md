# Single-witness replay contract

The new `single_top_witness.py` authenticates the frozen central source
contract and accepted prefix, constructs the original central matrix and
complete old list, and searches for one gauged integer witness. It never
calls the earlier full-kernel or full-build entrypoints. A successful
candidate is certified by every original row and the actual invertible
old-coordinate minor before global exactness is promoted.

The companion preregistration records all primes, dimensions, lift and
bit bounds. Modular LU, Dixon lifting and rational reconstruction are
search aids; the artifact does not promote their modular ranks to an
unmeasured rational nullity. All failed attempts remain in the record.
UNKNOWN exhaustion is distinct from source/authentication failure and
from a successful top-class certificate.

Root-owned commands, under the unchanged 128 MiB / 2 GiB guards:

```
python tests/test_segre_hadamard_single_top_witness.py SingleWitnessAuthentication SingleWitnessAlgebra SingleWitnessSource
python research/l-families/atlas/generalized/segre-hadamard-source/single_top_witness.py --scout
python research/l-families/atlas/generalized/segre-hadamard-source/single_top_witness.py --write
python research/l-families/atlas/generalized/segre-hadamard-source/single_top_witness.py --check
python -O research/l-families/atlas/generalized/segre-hadamard-source/single_top_witness.py --check
python -m unittest discover -s tests -p test_segre_hadamard_single_top_witness.py
```

The eighteen pre-acquisition controls and eight fixture-dependent controls
have separate test classes. The final class requires the new successful artifact; it
does not silently skip or reinterpret an UNKNOWN result. No author jobs
have run. Root validation and any exact freeze are pending. This packet
does not claim execution of the preserved central20, streamed52,
row-restricted42, continuation26 or full-composed contracts.
