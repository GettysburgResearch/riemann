# Complete ternary-cube Tor character replay

The [proof](TERNARY_CUBE_TOR_CHARACTERS.md) completes the low-grade actual
Koszul computation using canonical duality. This producer authenticates
the frozen first packet at `a895f47628b0bc7c7ee5e0392df2f79c24166f92` and
reads all three complete ternary-cube primitive panels. It does not import
or execute the old producer, and performs no new rational elimination.

Every torus weight and factor-permutation class is checked against an
independent Schur interlacing-pattern character. The dual upper table is
then checked weightwise, the prior normalization component is recovered,
and all three tensor-cycle character Euler identities are verified at
four declared diagonal matrices, including repeated eigenvalues. The
constant and all omitted low-degree zero homologies are retained.

The result determines all Tor representations, but does not construct
the minimal differential matrices. The frozen finite chain calculation
and the all-grade duality theorem are distinct inputs. No new arithmetic
monodromy identification or finite superdeterminant is asserted.

Execution is queued for root's serialized runtime. This note, the proof,
producer and substantive test file are bound into the resulting fixture.

```text
python -B research/l-families/atlas/generalized/segre-hadamard-source/tor_character_replay.py --write
python -B research/l-families/atlas/generalized/segre-hadamard-source/tor_character_replay.py --check
python -B -O research/l-families/atlas/generalized/segre-hadamard-source/tor_character_replay.py --check
python -B -m unittest discover -s tests -p test_segre_hadamard_tor_characters.py
python -B -O -m unittest discover -s tests -p test_segre_hadamard_tor_characters.py
```
