# R-99800 — Native-source and publication firewalls

## Native source

For one rough prime, with \(r=p^{-1/2}\),

\[
P=(1-r)P+r(P-rUP)+r^2UP
\]

has net shifted coefficient zero, while the native Euler update

\[
(I-rU)P
\]

has shifted coefficient \(-r\). Therefore the contracted positive
\(\alpha\)-child tree is not the Möbius Euler source. Calibration, Hall
placement, and Radon–Nikodym thinning cannot repair this coefficient mismatch.

The coefficient-exact sequential first-owner identity of PR #652 survives, but
its future-completed sign theorem remains open.

## PR #656 publication boundary

At head `db404ec00cf022f003ee2bbee66e0cf62ac45003`, PR #656 commits five changed
paths. Its proof packet and retained replay establish owner-martingale
degeneracy, the prime-continuum Selberg identity, the three-band squarefree-core
Gram expansion, and RH-equivalence of the block-\(L^2\) estimate.

Its PR description also advertises a Cauchy–Poisson gap, compact filter, and
growing moment tower. Those claims are not present in the committed proof
packet or retained verification object, so they are reconstructed independently
here rather than imported from metadata.

No current repository branch survives these firewalls as a complete proof.
