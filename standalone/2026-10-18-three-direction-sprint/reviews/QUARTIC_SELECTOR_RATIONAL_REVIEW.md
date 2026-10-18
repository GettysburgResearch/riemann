# Internal review of the squareclass projection obstruction

Reviewed source: intended publication file
`quartic/SQUARECLASS_PROJECTION_OBSTRUCTION.md`, read from workspace
`QUARTIC_SQUARE_SELECTOR_LATE_DRAFT.md`.
Actual raw-file SHA256:
`7769a60d2f513c49ae4219199e664eaa7d91ef37d2585d1c317315972d857853`.

Outcome: no blocking error found in the exact classical multiplier-intersection
proof and its stated norm obstruction. This is independent internal team
reconstruction, not external review or a zero-free theorem.

I reconstructed the finite algebra as follows.

- The CRT choice of `a` with `a=1 mod lambda^4`, `(a,D)=1` and
  `(a/D)_2=-1` is possible for every good nonunit squarefree `D`.
  The separate congruences defining `u` are compatible. Only `(u,a)=1`
  is required: allowing shared primes between `u` and `D` is essential
  and is explicitly retained.
- With `c=D lambda^4 u`, choosing `d` inverse to `a` modulo
  `c lambda^4` makes `B=(ad-1)/c` divisible by `lambda^4` and puts
  `gamma` in the required congruence group. The congruence
  `lambda^8 b u=a-a^(-1) mod D` makes the conjugated upper-right
  entry integral. All four entries of `gamma'` have the required
  level. Its top-left entry `a'` is inverse to `a` modulo `D`, equals
  `a` modulo `u`, and is coprime to `c`.
- In the multiplier ratio, the `lambda^4` factor contributes 1.
  Quartic reciprocity has no residual sign because `a,a'` are 1
  modulo 4. The `u` factors cancel even when `u` and `D` share primes.
  The remaining ratio is exactly `(a/D)_4^2=(a/D)_2=-1`.
- The same unitary pullback by `gamma'` acts on the original vector
  and its translated vector with these opposite eigenvalues.
  Orthogonality follows without an adelic spherical-vector import,
  a pure-tensor hypothesis, or a conflation of the classical
  common-cover space with a genuine local cover.
- Cancelling the gcd of a nonzero numerator with squarefree `D`
  reduces every nontrivial additive correlation to that exact case.
  The finite additive pairing is nondegenerate at good primes, so
  the residue projectors are self-adjoint orthogonal projections.
  Expanding their quadratic forms gives uniform mass `1/ND` for
  EVERY residue class, and CRT gives the joint mass product.
- The necessary squareclass test includes zero and retains
  `(Np+1)/(2Np)` at each prime outside the fixed base. These commuting
  projections decrease. Infinitely many factors bounded by `3/5`
  force their cofinal norm on the original same-character vector
  to zero. Local-global sufficiency of the residue conditions is
  neither used nor claimed.

The conclusion is correctly limited to these explicit bounded local
quadratic-residue projections applied to the original same-character
quartic vector. A nonzero local Fourier trace can survive a zero Hilbert
limit because that trace is unbounded. The text does not rule out a
different descent, a higher-rank kernel, a controlled renormalization,
or a separately estimated unbounded arithmetic period, and it proves
no new zero-free region.
