# Geometry round-two research log / checkpoint

Task007, 2026-11-17. Director requested actual primary-source geometry reading, exact finite-field RH hypotheses, a precise missing number-field counterpart, and a small independently checked lemma/curve example.

## Completed source work

- **PAPER-G001, Weil1949:** all printed pp.497–508 read. The Gauss-norm proof was independently reconstructed; extension-lifting and diagonal-counting architecture traced, but not every antecedent independently audited. Completed L1; partial technical check only.
- **PAPER-G002, DeligneI1974:** targeted §§1–3, statements/context(5.10),(6.1)–(6.3), and §7. The coefficient positivity and elementary tensor-amplification steps were checked. Main proof, SGA foundations, Lefschetz theory and rationality proof were not fully audited. Whole-paper L0, completed L1=false.
- **PAPER-G003, WeilII1980:** targeted introduction, conventions, weights, §2 selected passages, curve iteration statements/proof endpoint, §3.3, and hard-Lefschetz statement/linear-algebra reduction. Whole-paper L0, completed L1=false. Neither the 116-page paper nor its local-monodromy calculations were read completely.

Three original journal scans are available privately; `sources/geometry_round2/geometry_sources.jsonl` lists exact URLs, SHA-256 hashes, byte counts and nondistribution status. Downloads through new Numdam DOI URLs were slow; original item-ID URLs eventually succeeded. A university-hosted copy supplied Weil1949 after AMS returned403. The web reader could not load the 13.5MB WeilII PDF; local download/text extraction succeeded. A second MPIM scan was obtained but the Numdam scan is the citation authority. Failed guessed/forbidden download routes are not evidence sources. No source PDF/text/image should be included in the distributable archive by default.

Critical OCR checks used the actual rendered pages: Weil1949 p502 (inequality and M definition), DeligneI p301 (the 2n−i duality and power exponents), WeilII p204 (theorem3.3.1 inequalities), and p196 (strict curve bound on Hc¹). Image checks corrected the risk of mistaking an OCR `n−i` for the original `2n−i` and `≤` for `<`.

## Mathematical outputs

1. Proper/projective/open distinctions: I(1.6) is smooth projective; II(3.3.9) is smooth proper; II(3.3.6) is purity of the image Hc→H. Gm and A1 are exact negative controls for unrestricted modern paraphrases.
2. A formal genus-one rational zeta with integer positive Euler exponents in all degrees and a reciprocal equation but off-circle roots. The all-degree proof is a primitive-orbit injection, not finite numerical evidence.
3. An actual lisse-sheaf deletion test: geometric Frobenius A=[[2,1],[1,3]], pairing to Qℓ(−1), rational local determinants, trivial geometric monodromy. It fails exactly the open-Sp assumption in DeligneI(3.2); tensor global poles explain the failure. Parent independently checked this construction and the Frobenius convention.
4. Quantified tensor-amplification requirement: sublinear tensor-degree excess is sufficient; linear excess cannot force purity. The elementary limit lemma is checked.
5. A derived sufficient-condition lemma replacing open-Sp with asymptotically Tate geometric coinvariants is supplied as **pending independent review**, not assigned novelty. Full statement/proof in frontiers/geometry_round2.md §9, THM-G013.
6. Documented, rather than newly invented, transfer: WeilII §2 uses Mertens/Hadamard–de la Vallée-Poussin positivity for the strict initial weight bound; product geometry then contracts the error.
7. Exact elliptic-curve enumeration: E:y²=x³−x over F5 has 8,32,104 points over degrees1,2,3. α=−1±2i has exact magnitude sqrt5. Exact extension arithmetic checked all inverses.

## Artifacts and counts

- `papers/geometry_round2_records.jsonl`, `.md`, plus `PAPER-G001.md`–`PAPER-G003.md`: 3 source records, 1 completed substantive reading, 2 targeted readings.
- `theorems/geometry_round2.jsonl`: 13 theorem/lemma/countermodel nodes, including one explicitly pending derived lemma. Node count is not audit count.
- `theorems/geometry_round2_dependencies.jsonl`: 11 selected architecture edges; source-passage endpoints are defined in `graphs/geometry_round2_nodes.jsonl`. Not a complete proof DAG.
- `connections/geometry_round2_connections.jsonl`: 3 detailed connections, explicitly separating documented transfer, proved negative control and candidate strengthening.
- `frontiers/geometry_round2.md`: complete campaign synthesis and exact auxiliary proofs.
- `experiments/code/geometry_round2_exact.py`, `experiments/results/geometry_round2_exact.json`: standard-library reproduction. Finite Euler checks n≤80 and cyclic-code checks n≤8 supplement the all-n proof.
- `scripts/geometry_round2_build_records.py`, `scripts/geometry_round2_build_theorems.py`: reproducible source-record builders; require the privately downloaded scans for hashes.

## Outstanding / continuation

- Complete independent review of THM-G013, especially coefficient-field descent and the all-conjugate/local-degree quantifiers. Change its status only after review evidence is recorded.
- Search for prior literature versions of both auxiliary countermodels; no novelty claim should be made before that search.
- Reconstruct DeligneI rationality/monodromy and WeilII curve error contraction completely for one concrete sheaf family, keeping hypotheses precise.
- Search correction/version history systematically. Existence and identity are verified from originals; absence of later corrections is not certified.
- Formalize the Gauss-sum norm and elementary tensor-amplification lemma; no Lean proof was constructed in this round.
- No number-field spectral/cohomological construction or sublinear tensor localization bound was obtained. No progress toward a proof of classical RH is asserted from the finite-field results alone.

No alleged mathematical error in Weil or Deligne was found or asserted. The historical wording note on Weil1949 p507 concerns modern unrestricted paraphrases of a conjectural paragraph, not a confirmed author error.
