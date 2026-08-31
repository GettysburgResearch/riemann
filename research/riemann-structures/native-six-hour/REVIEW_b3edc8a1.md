# Independent review of the frozen row-envelope refinement

Reviewed commit: `b3edc8a1b2c37d4827c72ca86a398c14196a7598`.
File: `FULL_SUPPORT_ROW_ENVELOPE_REFINEMENT.md`.
Exact Git blob: `eae82cf7bfa50531faa12da5cc01b3f7522f2410`.
The working file has no diff from this freeze. I read the complete note
and independently checked its algebra and scope; no blocker was found.

The even and odd coefficient subsequences give exactly
e_1=e_2=5/8 and e_3=e_4=21/128. The positive-exponent requirement is
essential and is satisfied by every fixed full-support row. Summing all
column absolute values before the alias bound yields

    row_tail_b <= 64 H^(-1/2) product_i p_i^(beta_i/2) e_(beta_i).

No finite-cutoff factorization is assumed. At each prime, beta 2 dominates
1 and beta 4 dominates 3; the remaining ratio is 21p/80. Therefore
beta=(2,2,4) maximizes this bound over the existing 64 rows, giving
L_3=39375/64.

With the already accepted B=483723248, I checked
B*39375=19046602890000 and 2BL_3=595206340312.5. Exact squaring and
rounding give

    floor((2BL_3)^2)+1=354270587548199562597657.

For every integer H at least this value, the inverse comparison is
strictly below 1/2. Thus the same declared tensor matrix is invertible;
the nonzero physical row scaling and the fixed source-coordinate
congruence preserve the conclusion for the original observation and its
20-dimensional current-variation subspace.

This is a proof-only refinement of the predecessor at
`ae60a59d103a6696a667be4dbd0721387adc6a77`, using the unchanged numerical
certificate at `0103b95130de0f8151c529a0911a52842732227d`. It neither
changes the registered H0 record nor claims a new execution/test result.
The earlier H1/H2 remain valid. The gap 2^48<H<H3, optimal first horizon,
old singular limiting minor, all-prime and retained-gamma claims are
explicitly excluded.

I authored the effective-theorem predecessor; this independent review is
of the root-authored new row-envelope refinement and its exact arithmetic,
not a self-review of that predecessor. No scientific jobs or Git mutations
were performed for this review.
