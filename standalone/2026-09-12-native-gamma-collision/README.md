# Native gamma collision: an actual local defect loss

**PROPOSED component proofs and a source-complete finite certificate. Independent
mathematical/code review is required. RH and global defect decay remain OPEN.**

This continuation of #865 changes the question from approximation accuracy to
actual zero motion. It studies the uncompressed mean-centered family retained
in #855/#862, not a different Radau r>0 model.

The exact update admits a martingale coupling with explicit Bernoulli/exponential
increments and a complete forward density generator. Reciprocal projection then
gives a signed zero-defect flux, rather than an automatic positivity theorem.

The defining-integral certificate proves a local annihilation during the native
fifth-to-sixth update. A unique real double zero lies within 10^-35 in both
coordinates of

    x=31.1001854446439890503617267697554065740922204460843963878401,
    u=0.323788258419987986775868946870425118445263688003329898058626.

These are exact rational box centers, not the exact solution. The squared
splitting coefficient lies in (0.33402067,0.33403612). A whole tube of spectral
radius 10^-15 and parameter halfwidth 10^-32 retains exactly two zeros throughout:
they are nonreal conjugates at the lower endpoint and real simple roots at the
upper endpoint. The reflected tube completes the quartet. This is not a zero of
xi or a certificate for all zeros of one gamma stage.

Read [PROOF.md](PROOF.md), especially Sections 1, 3, 4 and 5. [result.json](result.json)
retains all three complete integral outputs and the two-variable contraction;
[tube.json](tube.json) prices the whole local continuation interval. The remaining
problem is a uniform balance of deaths, births, and drift of ALL exceptions.
The local event is not certified to be the same pair as #858's N=5 disk.

## Replay

All code is standard-library Python. Use a clean packet checkout and isolated
mode. The default bounded check is explicitly NOT a native integral replay:

```sh
python -I -S -B check.py
python -I -S -B -O check.py
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The complete fresh accepting command reconstructs all three integrals and then
the contraction and tube arithmetic:

```sh
python -I -S -B check.py --full
python -I -S -B -O check.py --full
```

In the author session the three complete integral cases were run separately in
each mode with `certificate.py --case 0`, `--case 1`, and `--case 2`, and the exact
contraction suffix was then evaluated on those completed outputs. Every case
and the final arithmetic agree byte-for-byte across modes. This is a completed
split reconstruction, not a claim that the two monolithic commands above ran.
See [VALIDATION.md](VALIDATION.md) for exact executed and unexecuted scope.

The 512-bit interval primitive is reused verbatim from #855. Two Python modes
are not two arithmetic backends or independent referee votes. No main or
integration activation, whole-repository build, Lean proof, large-order Radau
solve, parent zero replay, or global defect estimate is supplied.
