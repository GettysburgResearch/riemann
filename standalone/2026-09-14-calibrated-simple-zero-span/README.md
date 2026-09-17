# A small actual improvement, not another RH reformulation

**Proposed mathematical contribution; independent review required. Not a world
record, not RH, and not a claim that a fixed fraction of RH is solved.**

The focused response to the supplied critique is to improve an existing
unconditional quantitative argument rather than introduce another unproved
RH-equivalent target.

Using the repository's already certified seven-point pressure, a sharper
spectral-to-span conversion gives the proposed global bound

    liminf S(T)/N(T) >= 0.673012903898232480616262...
                      > 0.6730129.

`S(T)` counts simple zeros on the critical line, and `N(T)` counts all
nontrivial zeros with positive ordinate at most T, with multiplicity.
The prior repository 280-block extraction gives 0.673009652279136912... .
The new argument improves that constant by 0.00000325161909556860... as a
fraction, or 0.000325161909556860... percentage points. It is a **small** gain.
The earlier bound was dyadic and implies its global version; the new direct
BGST proof here is global. A new dyadic-window result is not claimed.

The decisive finite inequality is, for a trace-m PSD matrix,

    E+z>=q  =>  Delta+(phi_m(q)/q)z >= phi_m(q),

instead of the older Delta+z>=phi_m(q). The span coefficient is strictly
smaller. Section 2 of PROOF.md proves it at all energies and shows it is the
sharp slope for the given intercept in the scalar relaxation. Section 3
retains that coefficient under full block-offset averaging. Sections 4--7
close the implication to the proposed number with a direct finite Hermitian
realization and the PUBLISHED unconditional BGST theorem. This removes the
need to leave a new analytic source-to-count estimate unproved.

## Honest benchmark

Michael Devine's publicly posted Zenodo preprint 22066689, version 1.0.3,
claims the stronger unconditional number 0.673399. We retrieved its primary
metadata/abstract but could not inspect the full paper/certificate in this
pass. Thus this package is neither an acceptance of that result nor a claim
to improve it. Even ignoring that claim, no exhaustive priority audit of the
new extraction is asserted. The package improves the **pinned repo argument**.

## Reading / replay

Read PROOF.md, RESPONSE_TO_CRITIQUE.md and VALIDATION.md. The finite pressure
implementation is preserved byte-for-byte from Reviewer A's supplement; it
is not a new independent backend in this pass.

    python -I -S -B check_constants.py --check constants.json
    python -I -S -B -O check_constants.py --check constants.json
    python -B pressure/seven_independent_cached.py /tmp/seven.normal.json
    python -B -O pressure/seven_independent_cached.py /tmp/seven.optimized.json

The seven-point computation takes a few minutes on the authoring machine.
Its elapsed-time field varies, but all mathematical fields and table/traversal
hashes should reproduce pressure/verification.json. It is a producer that
rebuilds the entire search, not a JSON-only acceptance command. A failure to
close a final cell raises an exception. The included constants checker neither
runs that search nor proves the external analytic theorem.

The new code's exact fractions certify the displayed constants. The inherited
pressure code combines directed dyadic primitives and outward binary64 bounds;
it must not be described as integer-only arithmetic. Both commands use the
same backend, not independent numerical implementations.

No files in existing research packets, main, formal sources or acceptance
registries are to be changed. The local add-only patch is intended for a new
research branch from main f99d9e3908dde4865377c75d9ca051c1f545bf4f. There is no
new remote commit or PR unless a later uploader records one separately.
