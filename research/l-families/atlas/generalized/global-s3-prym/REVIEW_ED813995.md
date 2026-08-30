# Independent review of the Kummer tower checkpoint

Reviewed scientific commit: `ed8139953de75d5ef0d1c9fab5402360b7b7e9b7`.
Review date: 2026-08-31. Reviewer: independent `recent_landscape` agent.

Result: no blocker found in the stated theorem or bounded exact replay.
This report distinguishes an independent proof/source/code reading from
the root's execution results. I did not run a producer, test suite or
finite-field computation on the shared machine.

## Frozen object and dependencies

The six scientific files reviewed are the theorem
`KUMMER_TOWER_AND_PAIRED_DUALITY.md`, `kummer_replay.py`,
`test_kummer_replay.py`, `kummer_source.json`, `kummer_artifact.json`
and `kummer_provenance.json`, under
`research/l-families/atlas/generalized/global-s3-prym/`.
The proof's LF SHA-256 is
`18d70ac6eea94ab2a6af24ed91f7f38f2d1dbea733ffbc8209edfc7ddf79a175`;
the artifact's is
`2c3bd8850b3bc615037102737b6db293f6e13019f9317c0fc63fea042ae672d1`.
The two pre-existing review copies added by the same commit are not new
mathematical assertions of this packet.

The imported helper is pinned to
`4ba9cf883ecf49fe0034d6b05a878caf2768d263`, with the earlier cubic and
quadratic-twist source packet at
`23ad35cc8010f72cf1df54f09eccb4dcba108879`. These earlier geometry and
finite-field definitions remain load-bearing dependencies; the new
producer compares the working helper with its frozen source before import.

## Proof-critical checks

1. The assumptions `p` not dividing `6m`, `q=1 mod m`, `A!=0` and
   nonzero cubic discriminant are substantive. Eisenstein at a simple
   zero of `y` proves `W^m-y` irreducible even for composite `m`. The
   Riemann--Hurwitz computation includes the three finite totally
   ramified points and the `d=gcd(m,3)` points over infinity, giving
   `g(C_m)=2m-(1+d)/2`.
2. The character convention is coherent. The pullback action of
   `w->eta*w` has character `zeta_m^j`; geometric-Frobenius stalk traces
   are the displayed multiplicative character. Extension-field traces
   must use the norm to the declared base field. Replacing geometric
   Frobenius with arithmetic action on points without inversion would
   relabel the nonreal factors, so this distinction is not optional.
3. Finite pushforward and the normalization provide the inertia-invariant
   middle-extension stalks, not an arbitrary extension across the branch
   locus. The pure Kummer summands have no nontrivial global cohomology
   because their complete cyclic source is `P1`. The constant splitting
   handles `j=0`, leaving all the stated `V_j` with vanishing `H0,H2`.
4. The nonidentity deck fixed-point count is `3+d*1_(d|a)`. Its tame
   Lefschetz trace and the explicit finite Fourier transform give
   dimension two for the trivial character and
   `4-1_((m/d)|j)` for nontrivial characters. Thus degree three occurs
   precisely for order-three twists. This is a geometric proof, not
   inference from the bounded trace samples.
5. The ramification ledger has the correct drops: two at zero, one at
   each old finite branch, and two at infinity except for the order-three
   resonance, where it is one. Monicity and `mu_3` in the base field
   make the three normalized infinity points rational. The resonant
   invariant line therefore has Frobenius eigenvalue `+1`, not just
   unspecified rank one. Omitting it multiplies the global polynomial
   by `1-T`; the packet correctly treats that as an error.
6. Cup product pairs `j` with `-j`. If `c_j` is the actual leading
   coefficient, the normalization
   `P_j(T)=c_j T^r P_-j(1/(qT))` and `c_j c_-j=q^r` is correct,
   including the odd-degree sign. The quadratic factor is self-dual;
   a nonreal odd-degree factor does not acquire an alternating pairing
   on itself. The explicit cubic factors over F7 give a useful concrete
   failure of imposed individual self-reciprocity.
7. The proof now justifies `Z[zeta_m]` coefficients via the complete
   finite-order Euler factors together with polynomiality. A projector
   by itself would not establish that global coefficient-field claim.
   The square-root Frobenius weights are explicitly imported from the
   curve weight theorem, not deduced from the finite Gram projector.

During pre-freeze review I requested the explicit Eisenstein argument and
the Euler-factor route to integral cyclotomic coefficients. Both clarity
repairs are present in the frozen proof; they did not change the bounded
mathematical output.

## Producer and tests

The quadratic cyclotomic arithmetic uses the correct integral equations
for orders 3, 4 and 6, including conjugation and exact division in Newton
identities. The primitive root chosen in the base field fixes the character
orientation consistently across extension degrees. Norm restriction and
multiplicativity have separate controls. The direct tower count uses
the actual `w^(2m)` fibres and all normalized infinity points, independently
of the character decomposition sum.

The point-minus-`q+1` sums are negative Frobenius power traces, so the
positive sign in the producer's Newton recurrence is correct. Each
factor is reconstructed at its proved degree; the degree-three factors
predict the fourth extension independently. The high-degree total
product is checked against four primitive counts, but is not independently
reconstructed to its full degree. The artifact explicitly preserves that
coverage boundary.

I read all 12 tests. They cover the exact ring arithmetic, Newton signs,
norm characters, direct prime-field equations, the missing infinity
factor, paired versus individual reciprocity, dimensions, wrong strata
and counterfeit numeric/source inputs. Complete canonical JSON comparison
prevents booleans or floats from masquerading as the frozen integer data.
Exponent and source caps avoid an unbounded hidden computation. There is
no proof-critical Python `assert` that disappears in optimized mode.

## Execution evidence and remaining limits

The root reported Ruff, full producer write/check and optimized check,
and 12 ordinary plus 12 optimized tests passing for six towers over four
extensions each, with field sizes bounded by 2401. Those are reported
execution results, separate from this independent reading.

The new theorem concerns the full tame Kummer family under its hypotheses;
the finite replay covers only the declared orders 3, 4 and 6 and named
curves. No all-order statement is established by sampling. The fixed-point,
finite-pushforward, duality and weight theorems are classical imports.
External novelty is not certified by this review. The result is an honest
function-field geometric source, not a transfer to the integer-source
programme or a number-field RH/GRH argument.

The `q=1 mod m` hypothesis is explicitly retained. Frobenius-orbit descent
when it fails, including the changed infinity factor, is separate work
and is not covered by this exact-SHA report.
