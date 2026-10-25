# Independent review of the moving cubic twist

Reviewer: the `fractional_native` agent. I did not author
`MOVING_TWIST_MOMENT.md` and reviewed its completed deduction independently.
My own contributions in this pass are the growing-prime/mark estimates and
the capped native inverse estimate; this report does not review those files.

Reviewed file: `MOVING_TWIST_MOMENT.md`, SHA256
`e741c1dd5109111eb3489d361251dbff2d18f318dbf0a5b1e3e03370c04f74d4`.
The report is bound to these local mathematical bytes. Remote commit/blob
authentication is a separate publication step; later mathematical edits
require renewed review.

Status: no defect found in the displayed deduction at its explicitly
imported-source scope. This is internal mathematical review, not external
peer review or formal verification.

## Source and independence boundaries

I read the complete proposed note and fetched its two parent notes at
`c690f96fe6876f945398b3e2779810c563a64743`:
`SEXTIC_ROW_PHASE_CANCELLATION.md`, blob
`3a5d7adcc24ec8907be5c8fd6879d81736d44788`, and
`SEXTIC_RESONANT_ANGLE_COMPLETION.md`, blob
`e2a88e75c09cbb01cd47a3cb8295f0acc8cb6a1a`.
I also read the corresponding character/sieve conventions and relevant
analytic interfaces in Xu--Sang arXiv:2610.17675v2. I later fetched the
pinned OpenAI source for the separate all-family-cap investigation, but I
have not independently reconstructed its complete natural reflection and
Gauss-phase derivations. Those remain the named premises of this review.

## Mathematical checks

- The character `chi_n(c)^4` is cubic on units and retains every zero at
  primes dividing `c`, including phase-cancelled primes. Its primitive
  conductor and redundant natural radical count a good prime once. Thus
  the union budget in (9), with `Q=Nrad(c)`, is the appropriate one.
- For a fixed powerful part `v` of a frequency, the squarefree row scale is
  `R=K/T` and `Nrad(v)<=T^(1/2)`. Retaining this bound before reflection
  gives the effective column length `(R Nrad(v) FQ)^(1/2)`.
- Extending the squarefree sieve to full columns through their powerful
  parts gives (7): the powerful count and normalized coefficient energy
  produce the asserted dyad expression. `R+X+(RX)^(2/3)` is a permissible
  weaker sieve form, not an assumed quadratic bound for arbitrary sextic
  coefficients.
- The fixed-`v` bound gives, after counting powerful `v`, exactly
  `K T^(-1/2)`, `K^(1/2)T^(1/4)(FQ)^(1/2)` and
  `K T^(-1/3)(FQ)^(1/3)`. Their dyadic sums yield the three terms in (6).
- In reflection, the conjugate natural polynomial retains its original
  zeros and has one common coefficient after `v` is fixed. The note uses
  weighted Cauchy followed by the source's common logarithmic scale
  supremum. It does not insert a different arbitrary coefficient vector
  for each row into the sieve. Principal inducing rows are removed before
  any pole could be crossed.
- In the extra-puncture and squarefree expansions, the quotient keeps the
  same natural character. The outside masses are respectively subpower
  and logarithmic. No false coprimality with the quotient is imposed, and
  those outside divisors do not enter the conductor union.
- In the complete Poisson ledger, the first new term has summable
  `F^(-5/3)` weight. The second has `F^(-1)` and an absorbable divisor
  loss. The `l` sum is harmonic. All frequency dyads use their real
  Schwartz tail, including subunit nominal widths.
- At the resonant angular type, principal frequencies have prescribed
  valuations modulo six, hence good part `k_*q^6`. Replacing `Nk_*` by
  its lower bound one safely gives the uniform `H^(1/6)` estimate. The
  resulting `f,m,l` weights are convergent and give the displayed
  `A^(5/6)B^(1/3)` term with no lost growing-`Q` cost.
- The comparison at balance is exact:
  `B^(3/4)Q^(1/2)<=BQ^(1/3)` precisely when `Q<=B^(3/2)`.
  At `Q=1` the extra middle term is absorbed by `A+B`.

## Assessment

The result is a genuine conductor-uniform component improvement for the
coefficient `mu gamma_2`. It includes all nonzero Fourier frequencies and
the principal-frequency exception at the resonant angle. It does not prove
the corresponding assertion for the raw native Möbius coefficient, and
the coherent signed frequency consumer is not supplied by its positive
norm bound. No numerical experiment is used to certify this deduction.

## Corrected frozen bytes and remote authentication

The initial publication check detected a typesetting control byte in (21):
the locally reviewed file contained a carriage return where the literal
LaTeX command `\rm` was intended. The first upload normalized that carriage
return to a newline. I reported the mismatch; I did not attest identical
bytes for that first upload.

The corrected mathematical freeze is
`GettysburgResearch/riemann@5c7f4aa542ea2112b7f95fce984a35dfe454cfd6`.
I fetched the corrected `MOVING_TWIST_MOMENT.md` directly at that commit
under `standalone/2026-10-25-hlc-zero-free-transfer/second-pass/` and verified:

- UTF-8 byte length: **15,257**;
- SHA256: `51490a1139f6a466de69d10faa15570b3b26e67976360fc75f7bcb4374bb629a`;
- Git blob: `0efad91ee54db8f7f264614f18d8d2815f028016`.

The fetched bytes equal the corrected local file. I independently recomputed
both hashes, including the Git blob identifier from its header and contents.
I also verified that the entire difference from the originally reviewed
SHA256 at the beginning of this report is the replacement of that single
carriage-return byte by the literal two-byte sequence backslash-r. This
restores the intended `\rm` command and changes no mathematical statement.
The review above therefore applies to these explicitly repaired, remotely
authenticated bytes. The earlier source identity remains recorded rather
than being silently overwritten.
