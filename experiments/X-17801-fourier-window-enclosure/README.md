# X-17801 — Five-notch Fourier-window enclosure

This experiment replaces the old linearly interpolated FFT window by the exact
periodic Fourier representation in `L-17801`, a closed coefficient tail, and a
four-node cubic interpolation moat.

Build the producer on a system with MPFR, GMP, and libquadmath:

```bash
cc -O3 -std=gnu11 replay_interval.c -lmpfr -lgmp -lquadmath -lm -o replay_interval
./replay_interval 18 4096
./replay_interval 20 4096
```

Replay the retained finite logic:

```bash
python verify.py certificates/five-notch-x0.json
python -m unittest discover -s tests -v
```

The C producer uses 256-bit MPFR intervals for transcendental inputs and a
conservative binary128 complex-disc FFT. It is classified as a directed
engineering prototype pending a second directed backend and an audit of the
floating-disc constants. The analytic coefficient and interpolation tails are
independent of that implementation.
