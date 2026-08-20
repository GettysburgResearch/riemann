# Review report: assault on HHFE102010

The half-divisor symmetrization in PR #696 is a genuine advance, but its final energy was not yet decomposed at physical scale. The present packet performs that decomposition exactly.

The key finding is that the full coefficient diagonal is harmless. The entire RH-bearing content is the signed off-diagonal autocorrelation of one half-completed coefficient sequence at multiplicative distance at most four. A positive finite scale factorization can shrink this window to `1+o(1)` at subpower cost.

This is stronger than another Hardy-square criterion because the source has already been reduced to one Möbius cofactor sign and positive renewal weights. It is weaker than a proof: no source-faithful estimate for the final near-collision is supplied.
