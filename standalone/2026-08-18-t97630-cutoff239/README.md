# T-97630 cutoff-239 standalone front door

Read:

1. `R-97630-pr565-bias-cutoff-67-is-false.md`
2. `L-97630-all-real-p61-bias-from-cutoff-239.md`
3. `R-97631-pr566-reserve-injection-does-not-imply-current-domination.md`
4. `L-97631-low-child-preobservation-recombination.md`
5. `L-97632-high-child-contraction-with-margin-one-over-960.md`
6. `L-97633-annular-scalar-mellin-landau-consumer.md`
7. `T-97630-corrected-p61-bias-annular-closure.md`

Replay:

```bash
cd experiments/X-97630-cutoff239
./build_and_replay.sh
```

RH remains unproved pending source-tree reconstruction.

This is a reconstruction from the quoted digest. The included C++ does not
perform the reported full 2.5-million-point sweep or analytic tail.
