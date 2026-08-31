# Independent implementation review of central contract547d91b6

Reviewed freeze:547d91b6c8f8432f0f594c634e8a58349c929288.

| Frozen file | Git blob |
| --- | --- |
| central_top_resolution.py | 30ec95de4345a4998775bb9a8f85b8207ab84dff |
| CENTRAL_TOP_CLASS_PREREGISTRATION.md | 463ea123f326e053d6029f2c8985308f7aebbb60 |
| CENTRAL_TOP_CLASS_REPLAY.md | 665b3b7b75e1a749da6101c0e023fb67bcb5fb2e |
| tests/test_segre_hadamard_central_top.py | cac53e90c84a2b4dcf81e2c3ec77a79062ba4923 |

I read the complete producer, declaration, replay note and all20 tests,
then inspected the final binding delta. All four working files have no
diff from this freeze. This is an independent review of the implementation
and its contract; I authored CENTRAL_TOP_CLASS_GLOBAL_EXACTNESS.md and
do not present this report as an independent review of that theorem.

Every helper, accepted prefix, promotion proof and source/Tor dependency
is authenticated before executable use. The accepted prefix body and
exact proof2301613316c82b81debf817ecf4580a1476e1b78e663dd23a57317a03eda8bb3
are checked, and its polynomial checks and inherited inputs are compared
with the fresh prefix result. The central path calls prefix.source(),
not the unexecuted full composed build or the older elimination and
coordinate-acquisition entrypoints.

The matrix retains all592 central domain descriptors and every original
target-row address. The complete central old list is independently
enumerated from all eleven degree-five and seventeen degree-six accepted
relations and all matching complementary monomials. Its coefficients
are retained in both central and original F2 coordinates, with full-row
composition checks. The unchanged640 kernel machinery certifies actual
relations in all original rows. Exact rational span increase, rather
than an unsupported modular-rank comparison, proves nonmembership in
the entire old central span. The actual marked polynomial top column
and all final polynomial compositions are checked again.

The tests include a separate lazy-module enumeration of the old list,
the modular-old-rank-drop counterfeit, source and shape refusals, and
final artifact/top-column controls. The declared storage, coefficient
and matrix bounds remain explicit. No blocker was found in this scope.

At review time the coordinator reported format/lint success and an
initial precheck worker stopped by the memory reserve after four tests;
the retry and central acquisition were pending. I ran no scientific job.
This report does not claim a successful top-class acquisition or a
completed20-test run. Global775/776 dimensions are conditional algebraic
deductions after success, not measurements under this contract. The
older full-census contracts remain separate.
