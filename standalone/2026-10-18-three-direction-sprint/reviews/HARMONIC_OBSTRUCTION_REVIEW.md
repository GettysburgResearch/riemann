# Independent review and fresh replay of the observed-hub obstruction

Status: **component review within the research team.** No cofinal theta
construction or zero-free improvement is certified by this receipt.

Reviewed `theta/HARMONIC_OBSERVED_OBSTRUCTION.md`, raw SHA256
`213e47cb677f7196cc0b0d8ea4e30492640f2138e6235d31155cff92fe570147`.
The coordinating track independently reconstructed the Mellin evaluation
of the tanh integral, the resulting linear-coefficient identity for B,
the variance monotonicity, both elementary digamma inequalities, and
the endpoint choices of the rational covering. The proof explicitly
uses psi'>0 for all a>0 when excluding the initial range.

The lower bound is valid for the specified unmodified harmonic weights
and ALL couplings above (7/2)w with that asymptotic tail. It is not an
obstruction for arbitrary changed finite weights or couplings below
that profile. The natural positive quadratic correction is included.

Fresh optimized replay by the coordinator:

    python -O theta/certify_harmonic_observed_obstruction.py --emit <scratch>

PASS, 3.406 seconds. All six directed theta source indices were freshly
reconstructed with the complete stated source tails. The resulting
canonical sorted JSON plus LF digest is
`be55ed53de47f742a192951ce81fe7dfe30030384c05ead5eb4f5a898326d3a3`,
equal to the author's independent run. This is a CANONICAL JSON digest,
not a claim about the platform's newline-translated file bytes.

The 44 whole-interval variance enclosures have minimum lower bound
greater than0.0481816, while the fresh theta upper bound is below0.047.
The initial and infinite parameter tails are covered analytically; no
optimizer or finite sample decides acceptance. No blocking gap was
found at the displayed scope. This is not external referee acceptance.
