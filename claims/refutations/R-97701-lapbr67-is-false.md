# R-97701 — The `LAPBR67` large-prime residual is eventually negative

Claim ID: `R-97701`  
Status: **PROVED REFUTATION OF THE UNIVERSAL SIGN CLAIM**  
Created: 2026-08-18  
Depends on: PR #578 `L-97501/T-97500`; `R-97700`  
RH status: **unproved**

PR #578 chooses

\[
Z_X=(\log X)^{1/4}
\]

and the smallest even `L_X` satisfying

\[
L_X\ge8\left(1+\sum_{67\le p\le Z_X}{1\over p}\right).
\]

Mertens' theorem gives

\[
L_X=O(\log\log\log X),
\]

so

\[
L_X\log L_X=o(\log\log X).
\]

Its exact natural current is split as

\[
C_{L_X}(X)=\mathcal S_X+\mathcal L_X,
\]

where `S_X` is the small-prime cube and `L_X` contains every history meeting a
prime larger than `Z_X`. PR #578 proves `S_X>0` for all sufficiently large
`X`. By `R-97700`, however,

\[
C_{L_X}(X)<0
\]

for all sufficiently large `X`. Consequently

\[
\boxed{\mathcal L_X=C_{L_X}(X)-\mathcal S_X<0.}
\]

Thus `LAPBR67`, which asserts `mathcal L_X>=0` uniformly, is false. This does
not refute the native scalar or RH. It refutes the subcritical-depth threshold
architecture and forces the stopping line into the rough harmonic saddle.
