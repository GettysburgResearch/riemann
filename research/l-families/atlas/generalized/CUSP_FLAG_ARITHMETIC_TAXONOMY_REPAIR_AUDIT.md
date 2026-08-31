# Independent audit: cusp-flag arithmetic taxonomy repairs

Status: PASS; release metadata repair only, with new scientific identities.
Review date: 2026-08-31.
Programme: #764.

## Frozen and imported identities

| Object | Original scientific source | Separate repair source | Programme repair import |
|---|---|---|---|
| All-weight cusp family | 43ecb4ac3f2487ee944b6bb6bef72e1ad92f2678 | b69c854d9e3dd1db7b82d95fe6f032fe47d5306b | eef7f99b666aea3e5c541c76504bc9a6bb22b99a |
| Positive-spectrum boundary | 1483ff25e9100276ac7064ba7d7d696b45afb9ea | 282ce03941444d0e02daba5fde260ccb54a3f909 | 65e3f808714bbfeaeac30ca389695fa055082ea9 |

The family repair's immediate authoring parent is the original
positive-spectrum source 1483ff25; its patch touches only the three
family files. The second patch touches only the three positive-spectrum
files. No new theorem is created by these metadata changes.

The original [family mathematical audit](CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY_AUDIT.md)
remains an immutable record of its exact original source. This report
adds the release correction that was not covered there. Its mathematical
approval is not withdrawn or strengthened.

## Why the repair was required

Both original reports used the custom arithmetic label
EXACT_INTEGER_AND_RATIONAL. That is outside the repository's accepted
arithmetic taxonomy in atlas/schema/common.schema.json. The earlier
universal-Euler audit had already treated this same mismatch as a release
defect. Calling the files custom reports is not a reason to repeat it.

Both repaired reports now declare:

    arithmetic_class: MIXED
    arithmetic_components: [CERTIFIED_INTEGER_COVERAGE, EXACT_RATIONAL]
    rounding_contract: exact Python integers and Fraction; no rounding

Each producer changes only those metadata lines. Each test module adds
one taxonomy/rounding tamper test. The fixtures are regenerated with the
new metadata and current producer/test hashes; the positive-spectrum
payload seal changes accordingly. The original family report has no
separate payload-seal field; its full typed reconstruction remains the
acceptance rule.

The written scientific notes, source manifests, original source identities,
mathematical payloads, coverage, arithmetic limits and work budgets are
unchanged. None of the original frozen files or their old commits was
amended in place.

## Exact repaired artifact identities

| Artifact | Repaired Git blob |
|---|---|
| cusp_flag_quotient_global_family.py | 7e6ae5bb1fd9c53930cee1198eb185806a2ea118 |
| cusp_flag_quotient_global_family.json | 7ca422e505e6ccd817aadee3362f1ace2fa83fd4 |
| tests/test_cusp_flag_quotient_global_family.py | c2d9dc7ea92a75c7e3fd99c5463e664fb79e0d3a |
| cusp_flag_positive_spectrum_boundary.py | f229a4e3819759e778a41209576f2c1725cd0d59 |
| cusp_flag_positive_spectrum_boundary.json | e553f9404ab87e7b057fea1e81c81b539242c673 |
| tests/test_cusp_flag_positive_spectrum_boundary.py | 8f8879c5f483c73a8f8d7282e9df4fe1324b9916 |

Non-test paths are in research/l-families/atlas/generalized/.
Repaired family fixture LF SHA-256:
fb6ae6ad8535b8cc519d33ab0e901cf17b9cf53ddff9c0bde427daf61faa60db.
Repaired positive-spectrum fixture LF SHA-256:
5684f78e970ac3fc9c03f2bab498a0bfc54b4c409d6dd157d07830354a063e8b.
Repaired positive-spectrum canonical payload seal:
2d9a02f5eb3a23861c65f9a54dad5ddaceae82912559bf01b8f686ff56eb097d.

## Independent verification

The root compared the entire mathematical JSON payload before and after
each repair, excluding only the declared metadata and consequent hashes.
Arbitrary-size integers were compared without conversion to floating point.
The producer bytes match exactly the specified metadata substitution.
The test AST differs by exactly one added test in each module.
Both notes and manifests remain byte-identical.

The root independently checked all six primitive Git-blob/LF-SHA bindings
and four current artifact hashes for each report, and its complete fixture
identity. These semantic and hash checks also pass under Python -O.

Each repaired module has 36 tests. Root normal/-O times were 5.422s/5.556s
for the family and 3.123s/2.684s for positive spectrum. Both producers
passed in both modes. Ruff lint/format and the complete 1483ff25-to-repair
whitespace check passed.

An independent reviewer separately verified both three-file patch scopes,
the exact producer substitution, test AST delta, all source/artifact hashes,
unchanged mathematical payloads and positive-spectrum seal. Its 36-test
normal/-O and producer replays passed for both reports; twelve additional
resealed metadata/type controls failed closed in each mode.

The family still uses the original frozen parent source in its manifest.
The positive-spectrum packet still authenticates original family 43ecb4,
not a silently substituted repaired fixture. Durable source acquisition
must retain those original identities as well as the separate repairs.

No mathematical conclusion, analytic proof, native-source binding,
effective cusp derivative onset or RH/GRH claim is supplied by this repair.
