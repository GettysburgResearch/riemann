# GPT-5.6 Pro handoff — cubic shell and balanced dispersion

## Freeze

```text
repository:       gfreund123/riemann
frozen PR:        #498
frozen head:      6cc0da2fa5711017e260ebdcea4ba8c22e453288
frozen branch:    research/gpt56-pro/93250-centered-q4-cubic-closure
successor branch: research/gpt56-pro/93300-cubic-shell-balanced-dispersion
cutoff UTC:       2026-08-16T01:04:35Z
```

PR #498 must remain frozen.

## Strongest new theorem

The packet proves unconditionally

\[
 \mathcal A_\circ(N)
 =
 \mathcal B_N
 +O(\sqrt N\log^3(2N)),
\]

where \(\mathcal B_N\) is the explicit balanced near-hyperbola form in
`T-93305.1`.

## Review order

```text
L-93300
R-93300
L-93301
L-93302
L-93303
L-93304
T-93305
O-93300
M-93300
X-93300
standalone packet and checksum ledgers
```

## Next arithmetic attack

Do not return to block count or rename BCD.  Work directly with

\[
 \sum a_U(m)\Lambda(\ell)F(m\ell/N).
\]

Preferred concrete attacks:

1. dyadic decomposition of the near-hyperbola support;
2. additive dispersion using the exact nonzero Fourier coefficients of \(F\);
3. source-specific correlations of the truncated Möbius divisor coefficient;
4. a carrier estimate for the exact Mellin band-pass integral;
5. transfer through the First-Hermite Calderón frame with the low-carrier term
   retained explicitly.

Every proposed estimate must be checked against `R-93300`.

## Status

```text
new unconditional reductions          verified by exact replay
balanced dispersion estimate          open
candidate complete proof              no
Riemann Hypothesis                     unproved
```
