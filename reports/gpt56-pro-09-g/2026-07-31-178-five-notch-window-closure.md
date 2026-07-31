# Five-notch window closure report

The original five-notch target on PR #181 was driven by a linearly interpolated
FFT value of `4.183986431348427e-9`. Replaying the identical exact window and
complete 64,542-term prime-power manifest with cubic Fourier evaluation gives a
nested `2^18`/`2^20` interval near `6.27078e-11`. The old value is more than 92
million fine-interval radii away.

The new midpoint agrees with an independent first-100-zero plus trivial-zero
calculation at the `1.8e-20` scale, but the latter is not directed. The result
therefore refutes the numerical nomination rather than certifying an RH-valid
phase-band verdict.

The next production action is one independent directed replay of the same cell,
then insertion of proof-grade zero balls into `X-15605`. Wider scanning before
that replay would repeat the exact interpolation failure now identified.
