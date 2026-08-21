# X-19803 — Theta variance and mixed Schur exact regression

This standard-library-only verifier checks two independent exact identities:

1. the full-theta score variance decomposition
   `mu = scalar_channel + pair_channel`;
2. the augmented mixed factorization
   `S - R*D*R = 4 J_mix* J_mix`.

The retained control uses two genuinely distinct theta coordinates, so the pairwise mode channel is nonzero. All arithmetic is performed with `fractions.Fraction`.
