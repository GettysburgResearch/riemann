# M-105300 — Hostile review contract for the moderate Xi saddle and residue spectrum

Claim ID: `M-105300`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-23  
RH status: **unproved**

Review in this order:

1. `L-105300` quotient algebra and resultant;
2. exact replay `X-105300`;
3. `L-105301` cubic contour-shifted saddle;
4. `L-105302` Rouché and residue transfer;
5. `R-105300` firewalls;
6. `T-105300` implication graph.

## Finite-algebra checks

Reject `L-105300` unless:

- `gcd(p',p'')=1` is retained;
- `u=p(p'')^(-1) mod p'` is formed in the quotient algebra, not pointwise;
- the resultant normalization contains the factor
  `n^2 Res(p',p'')`;
- the electrostatic formula is asserted only when `p` itself is real-rooted;
- spectral flatness is not promoted to an automatic variance bound.

## Moderate-saddle checks

Reject `L-105301` unless:

- the asymptotics of `S_m'''` and `S_m''''` are uniform for every `m>=M`;
- first-summand dominance proves a zero-free complex saddle neighbourhood;
- the contour displacement is `O((log m/m)^(1/3))` and both endpoint
  connectors are bounded;
- the result is **relative**, not additive;
- the order-one cubic term is retained;
- every nonconstant cubic cross term after the shift is shown to be `o(1)`;
- local, intermediate and global tails are bounded on the displaced contour;
- derivative control is obtained from a strictly larger buffered box.

The key separator is the boundary scale

\[
|s_mz|\asymp(w_m/m)^{-1/6},
\]

where the cubic action is order one. A Gaussian-only proof must be rejected.

## Rouché/residue checks

Reject `L-105302` unless:

- the analytic phase `Theta_m` has `Im Theta_m(z)` of the same sign as
  `Im z` in the full strip;
- the complement of all Rouché disks has a uniform model lower bound;
- the box used for residues is strictly buffered inside the approximation box;
- the exact cubic-model logarithmic curvature formula is used;
- the `O(1)` phase-count correction is justified;
- no high-tail quantifier is exchanged with a fixed derivative order.

## Conclusion firewall

The exact quotient spectrum and the improved high-derivative entry do not
prove `CRDB105200`. Every endpoint and winding charge remains load bearing.
The replay does not authenticate the contour deformation or RH.
