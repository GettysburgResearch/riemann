# Internal review of the moving-twist estimate

Reviewed object: `MOVING_TWIST_MOMENT.md`, 15,256 bytes,
SHA256 `e741c1dd5109111eb3489d361251dbff2d18f318dbf0a5b1e3e03370c04f74d4`.
This report is bound to those local bytes. Remote-commit authentication
is a separate publication step.

Reviewer: the `native_gain` research agent. I did not author the
reviewed note, but independently suggested the moving-twist extension
and participated in discussion of the powerful-frequency refinement.
This is an internal cross-check with disclosed intellectual overlap,
not external peer review, formal verification, or a wholly independent
invention of its proof.

## Inputs read

I fetched the pinned PR1020 sextic proof, its resonant-angle companion,
and its coefficient-transfer audit. Their Git blob identifiers are
those listed in the reviewed note. I also fetched the complete pinned
`openai/math` source at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, blob
`268c4e3206d460c617d3d2129742a72b831b3def`, and checked the stated sieve
normalizations. This does not amount to independent reconstruction of
the full quasi-Riemann argument or every imported analytic lemma.

## Specific mathematical checks

1. **Growing twist and zeros.** The fourth power of the sextic symbol
   is cubic. Its original zero set is rad(c), including phase-cancelled
   primes. The primitive conductor times the redundant radical has
   norm O(Q). The proof uses this union bound and does not remove zeros
   on the grounds that a local phase is trivial.
2. **Fixed-powerful-row conductor.** For k=u v, u squarefree and v
   powerful, the remaining variable u has norm R=K/T. At each good
   prime, the natural presentation has exponent one in its conductor
   union. Hence R rad(v) FQ is the correct upper budget. The inequality
   rad(v)<=T^(1/2) is valid for every such v.
3. **Reflection and coefficient scope.** After fixing v, the reflected
   polynomial has a common column coefficient and variable character
   chi_n(u), with original zeros retained. Natural divisors and root
   numbers are outside bounded row scalars. The source's scale-supremum
   device, not rowwise arbitrary-coefficient substitution, is needed
   and explicitly retained. Principal inducing rows are removed first.
4. **Dyadic exponents.** I recomputed each term after counting powerful
   v. They are K T^(-1/2), K^(1/2)T^(1/4)(FQ)^(1/2), and
   K T^(-1/3)(FQ)^(1/3). Their dyadic sums are exactly of the stated
   sizes K, K^(3/4)(FQ)^(1/2), and K(FQ)^(1/3).
5. **Squarefree columns and additional masks.** Inserting d^2|n and
   e|n produces the factors 1/Nd and 1/sqrt(Ne), respectively. The
   quotient retains the same natural character. The external row
   scalars do not add d or e to the conductor budget. A nonexistent
   quotient coprimality would invalidate this step; none is imposed.
6. **Complete f,m,l ledger.** The first nonprincipal cost has f weight
   F^(-5/3); the second has F^(-1) and divisor weight M^(-1/4).
   The former converges and the latter has a subpower loss on the
   finite support. Both include all Fourier dyads through their actual
   Schwartz tail; subunit nominal widths do not create a constant
   frequency count.
7. **Resonance.** A principal ordinary row has one prescribed valuation
   class modulo six at every good prime. Its good part is k_*q^6.
   Replacing Nk_* by its lower bound one gives a valid uniform upper
   bound H^(1/6), including subunit H. The resulting f exponent is
   -4/3, and the m,l weights are M^(-5/6), L^(-2); their sums converge.
   Thus no growing-Q loss was omitted from this principal-frequency
   upper bound.
8. **Claim boundary.** The proven coefficient is mu gamma_2, and the
   native first-Poisson coefficient still lacks that mu. The final
   note expressly retains this discrepancy and the signed frequency
   consumer. It does not assert hypothesis (H), RH, or a new zero-free
   region.

## Assessment

I found no gap in the displayed deduction at its stated imported-source
scope. It is a genuine conductor-uniform component improvement over
the direct B sqrt(Q) extension. Its applicability to the complete
native inverse remains unproved for the specific reasons the note
states. The stronger intermediate bound in `NATIVE_GAIN.md` is a
separate proposed object and was not used to certify these reviewed
bytes.

## Exact remote authentication (2026-10-25)

I independently fetched `MOVING_TWIST_MOMENT.md` and `MANIFEST.json` from
`GettysburgResearch/riemann` at the exact final mathematical commit
`5c7f4aa542ea2112b7f95fce984a35dfe454cfd6`, under
`standalone/2026-10-25-hlc-zero-free-transfer/second-pass/`.
For the fetched note, I recomputed both SHA256 and Git blob SHA-1
(including the `blob <byte-length>\0` header), compared the reported
GitHub blob, checked the manifest entry, and compared the local bytes.
All four checks agree:

- Byte length: `15257`.
- SHA256: `51490a1139f6a466de69d10faa15570b3b26e67976360fc75f7bcb4374bb629a`.
- Git blob: `0efad91ee54db8f7f264614f18d8d2815f028016`.

The manifest itself is 2963 bytes, SHA256
`68f69ad289a722a358b113cdec20db41cf54755bffb2c1bce73cecdf045e3536`,
Git blob `ca948bb86211998ad92e2c147bfb6e9b4b945f8f`; its fetched bytes also match the
local manifest, and its Git blob was independently recomputed.

The publication bytes contain one reviewed editorial repair to the
initial local object named at the top of this report. Equation (21)
had a literal carriage-return byte where the TeX command `\rm` was
intended. Commit `3b47783a7c775bc8133f6601cb9bb97b1b38678a` normalized
that byte to a line feed during text transport, giving SHA256
`c3441a845d5c5f5791a82b2f896045a62ff87101a5647ba66046dae23ee91718`;
it was therefore not byte-identical to the initial reviewed object.
The final commit replaces it with the literal backslash followed by
`r`, restoring `\sum_{k\ {\rm principal}}` without changing the
mathematical formula. I checked the exact difference: reversing this
single repair reproduces the initial reviewed 15,256-byte object and
its SHA256 `e741c1dd5109111eb3489d361251dbff2d18f318dbf0a5b1e3e03370c04f74d4`.
The assessment above also applies to the repaired publication bytes.

This appendix authenticates this note and its manifest entry. It does
not extend the analytic assessment, authorship independence, imported
source certification, or claim scope stated above.
