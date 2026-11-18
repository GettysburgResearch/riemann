# PAPER-D303: The roots of trigonometric integrals

N. G. de Bruijn. Duke Mathematical Journal17(3),197–226(1950). DOI10.1215/S0012-7094-50-01720-0. [Primary scan](https://repository.tudelft.nl/file/File_524a4d3c-0858-4c55-b425-8c8ce1fb89da).

**Audit scope:** L0; completed substantive reading=False. Targeted actual-source reading: introduction/Theorem1 and proof architecture,pp197–200; §3 Theorem10–14 and heat-contraction limit proof,pp204–205; selected §7 historical limitations and product-closure theorem. Whole30-page paper/saddle-point estimates not read or audited completely.

**Versions/corrections:** No exhaustive correction search. Repository1948 field corresponds to received-era metadata; original journal and Crossref identify1950. Pages197–226 verified against original and Newmanreference;297–314 is not this paper. SourceSHA256 `793a96ad64681bfc43740602cea0980ca5f86528ef2e96a4e14ed01ece83b8f5`.

## Exact source results

- Theorem10,p204; Theorem13,p205: If f is integrable onR, f(u)=conjugate(f(−u)), f(u)=O(exp(−|u|^β)),β>2, and all Fourier zeros lie in|Imz|≤Δ, then multiplying f byexp(λ²u²/2),λ>0, moves all zeros into|Imz|≤sqrt(max(Δ²−λ²,0)). No positivity orC∞ hypothesis is present.
- Theorem1,p198: For nonconstant even nonnegative real-axis entire potentialf whose derivative is a locally uniform limit of polynomials with only imaginary-axis roots, the Fourier integral ofexp(−f(u)) has only real zeros. In particular this applies to the quartic mollifierexp(−(u/ε)^4).

## Limitations

- Theorem13 requires all zeros in the initial strip, not merely all but finitely many.
- Atoms are not integrable functions and cannot silently be used as inputs to Theorem13.
- Gaussian heat factors were not shown in this source to have every asymptotic strong-universal-factor property.
- No direct classicalRH theorem is proved.

## Concrete research questions

- Independently audit the positive smooth sharpness construction and its exact source-class membership.
- Preserve heat normalizationλ²/2 versusdirectτ in computational transfers.

## Research reuse

`audits/heatflow_round2.md` preserves the exact source conventions and independently reconstructed positive-kernel controls. It separates atomic measures from admissible kernel functions and finite Li-type prefixes from all-zero/all-parameter theorems. The finite numerical enclosure is reproducible with `experiments/code/heatflow_round2.py`; independent adversarial review remains explicitly pending.
