# Field catalog used in the degree five through eight classification

The source is the LMFDB Collaboration's production export of 17 November 2026, released under CC BY-SA 4.0. Its versioned Zenodo record contains the 1,755,561,276-byte compressed table \(\mathtt{nf\_fields.txt.zst}\). The [extractor](../../scripts/extract_zhao_lmfdb_fields_nov18.py) checked the published compressed SHA-256 `eb006d5a10c4153a0a8ce98ee0004b8d826f40d2d6e5c1fbe1fc8974a3b04016`, read all 22,444,816 rows, and checked the degree, signature, discriminant, index in the label and length and monicity of every retained coefficient vector. Each extracted record has keys `label` and `coeffs`, with coefficients in ascending order. Run the extractor with the compressed file path and a destination directory. [Versioned dataset and manifest](https://doi.org/10.5281/zenodo.24323763)

The broad absolute discriminant ceilings are 1,100,000 in degree five, 2,300,000 in degree six, 4,300,000 in degree seven and 5,100,000 in degree eight. In degrees five through seven every signature is included. In degree eight the catalog includes the signatures \((2,3)\) and \((0,4)\). The published LMFDB completeness bounds for all these signatures exceed the respective ceilings. Signature exclusions and the [smaller discriminant cutoffs](../../scripts/check_zhao_field_cuts_nov18.py) precede the prime-ideal tests. They leave 21,440 quintics, 13,499 sextics, 2,248 septics and 116 octics. Completeness of the arithmetic catalog is imported from the published computations. [LMFDB completeness table and sources](https://www.lmfdb.org/NumberField/Completeness)

| Degree | Complex places | Rows before the smaller cutoff | Extracted JSON SHA-256 |
|---:|---:|---:|---|
| 5 | 0 | 476 | `eaa26b96eaad76eddb43d9eca2fcfee452522c91384f6a37e8cacaec11d833b1` |
| 5 | 1 | 12215 | `597c05a6fe1b5a2d87cb49d64b5c5638e609951e1b7d196d85e96b2f47bf56d1` |
| 5 | 2 | 32331 | `ea2e52d51a66e3d26ad8cbf034cae8522943942e84af228e4edd992241259a15` |
| 6 | 0 | 38 | `c66e8beb6bc025bc166085fbbe47aaf21bd34354f06fd23221bbdbbf88649202` |
| 6 | 1 | 1535 | `10eefe722f06d6d45fd35da3f582b0b28e0e6110951e7dab6bcf80ddd298a5d5` |
| 6 | 2 | 13698 | `c000a7104abe8d19420f579a165edbeae50bc980500456bf9ffd97190d2e2daa` |
| 6 | 3 | 10239 | `d74e97a2cae86cefea60bb530c99b5d6647f3391e3aad4400818e191cc0727ed` |
| 7 | 0 | 0 | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` |
| 7 | 1 | 24 | `9e90a8c458904fdcdd3b9f160f762dd048cdfdeb1bfc7c22eecdaa107d67074e` |
| 7 | 2 | 998 | `0b06c75ec9492fc8c81edafae5a486d63f136220150af130c2c164f9c8121fd6` |
| 7 | 3 | 3797 | `02dfceb006df90f492e0161228539b4b4760a3e18a4d286e359fa0a4f9b5e544` |
| 8 | 3 | 33 | `41561476484d825f4c3cd35260e693231d1fb4916e24b9b8073a78e2a278ecfb` |
| 8 | 4 | 183 | `d6c88584587859dac64342ba8b4a2da5df4bdb073b52c2f710686429bc56a645` |

### Independent comparison with the corrected Bordeaux tables

On the intersection of the above ranges with the published 2008 PARI `nftables` ranges, all 2,064 sextic entries and all 307 septic entries in the latter have an isomorphic LMFDB entry. For 2,369 entries the supplied defining polynomials agreed after reversing the PARI coefficient order. For the other two fields PARI's exact `nfisisom` determined the correspondence within each shared discriminant. Within the old stated signature \((3,2)\) range the LMFDB includes two more fields than PARI's \(T73\) file. The polynomials \(x^7-x^4-x^3-x^2+1\) and \(x^7-x^5-3x^4+2x^2+x+1\) have positive maximal-order discriminants 1,328,121 and 1,771,597 respectively and both have three real places, as checked by \(\mathtt{nfinit}\). The prime-ideal classification uses the newer catalog, including these fields. The [overlap checker](../../scripts/check_zhao_field_catalog_overlap_nov18.py) takes the LMFDB extraction directory and a directory with the eight compressed PARI tables \(T60,T62,T64,T66,T71,T73,T75,T77\) (each named `Tnr.gp.gz`); its optional `--gp` argument selects the PARI executable. [PARI tables and README](https://pari.math.u-bordeaux.fr/pub/pari/packages/nftables/)
