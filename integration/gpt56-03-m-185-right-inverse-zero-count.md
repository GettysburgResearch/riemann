# Integration handoff — Issue #185

## New claims

```text
L-18501  exact right-inverse selected-zero spectral gap
T-18501  cofinal cardinal–radical count diagonal
X-18501  Fraction-only finite verifier
```

## Dependency placement

```text
L-14321 / T-14306
        |
        v
L-18501 / T-18501
        |
        +--> selected-zero count and visible Schur floor on constructed packet
        |
        v
L-15306 / PR #169 three-block composition
```

## Correct remaining gate

Do not continue treating

```text
N_(G^-1/2 K_T G^-1/2)(B_T+beta) <= dim R
```

as an unexplained spectral asymptotic. On a packet with an exact selected-zero
right inverse it follows from one finite Gram bound.

The unresolved theorem is instead:

```text
constructed cardinal–radical packet captures the complete dangerous low index.
```

Valid interfaces include the weighted-deficit trace/Schatten margins of PR #163,
the finite saturation block of `L-15604`, or a direct source-frame capture
theorem. Bare dimension comparison remains invalid.
