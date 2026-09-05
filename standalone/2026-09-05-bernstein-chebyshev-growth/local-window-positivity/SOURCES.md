# Source and scope ledger

The mathematical parent is PR #792's `cross-route-hardy-laguerre/BRIDGE.md`
at commit `39c13367f4b3956631ea1e00fac6c3005fc32057`, Git blob
`81d7d5db7a25f5875a08c10235fdb514d67cc744`. The source formula, operator
normalization, and the individual-atom trace-norm bound are imported from
that proposed proof. The checker authenticates the literal parent bytes.
The current publication base is `dc4bb9dbb49876732eb656339e79ee4ec43b157f`;
its raw-cutoff negative-index theorem is not rewritten.

PR #793 was checked at live head `6ebbe5efe6430584736649b87495af2be073f693`.
Its pass4 `PRIME_TAIL_TRANSITION.md` was read. That note proves a
uniform-in-moment-order PNT approximation and a continuum-balanced Hankel
error. This packet instead gives an EXACT finite-rank operator completion
on a fixed time interval. Neither result proves the other's positivity.
The extra deposited signed-energy attempt in #793 was identified from the
commit metadata, not independently reviewed. No claim about it is imported.

Classical references (not external novelty claims):

- NIST DLMF 25.2, zeta function and classical analytic continuation:
  https://dlmf.nist.gov/25.2
- NIST DLMF 5.9 and 5.11, gamma/digamma integral and remainder framework:
  https://dlmf.nist.gov/5.9 ; https://dlmf.nist.gov/5.11
- NIST DLMF 27.12.5, unconditional quantitative PNT:
  https://dlmf.nist.gov/27.12#E5
  Only Psi(x)~x is used for LW-2; no PNT is needed for LW-1 or LW-3.
- E. Bombieri, "Remarks on Weil's quadratic functional in the theory of
  prime numbers. I," Rend. Lincei Mat. Appl. 11 (2000), 183--233.
  The indexed abstract credits Yoshida's small-support positivity theorem:
  https://eudml.org/doc/252338
  This is a prior-art boundary, NOT an imported proof or a checked numerical
  comparison of support lengths. Direct landing/PDF retrieval was blocked
  during this pass; the paper's proof was not inspected here.

The triangle-mixture positivity argument is a classical Pólya-type
construction and is proved in full in Section 4. No general local-positivity
or extension theorem is needed as an unproved input.

A small exploratory floating-point linear program was tried during
formulation, for positive cosine corrections on bounded intervals. It is
not used in any theorem, interval bound, or acceptance result in this packet.
There is no numerical zero input or actual-prime sweep.
