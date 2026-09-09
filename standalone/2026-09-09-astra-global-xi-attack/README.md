# Direct attack on the complete xi function

Date: 2026-09-09. Status: **UNSUCCESSFUL GLOBAL RH PROOF ATTEMPT**, with
self-contained analytic reductions and one proposed directed countercertificate.
**The Riemann Hypothesis is not proved.** This is not another divisor-gap extension.

Read `GLOBAL_ATTEMPT.md`. The target is the original entire xi function on its
whole critical band. A classical complex Laguerre inequality would settle it.
The note derives that exact source inequality, tries a finite-theta completion,
and identifies where it fails. The global Fourier-sign inequality is not supplied.
No novelty is claimed for the classical criterion or the theta representation.

A particularly important failed step is now testable: the three-term positive
half-line theta truncation has a simple NONREAL zero near

    67.8801896551476196444591034891
      + 0.4773438417708229856896978584 i.

A radius-10^-25 disk is certified below. It lies inside |Im z|<1/2. This is a
zero of F_3, a CHANGED entire function, not of Xi or zeta. Local uniform
approximation and positive half-line source values do not justify the proposed
zero-free-strip transfer. The all-N boundary calculation separately proves
that no finite raw theta truncation, even with any fixed Gaussian heat weight,
is in the real-zero class. It does not prove where all its nonreal zeros lie.

## Reproduce the single finite certificate

From this directory, standard-library CPython only:

    python -I -S -B certify_truncation.py --check root_certificate.json
    python -I -S -B -O certify_truncation.py --check root_certificate.json
    python -I -S -B test_certificate.py
    python -I -S -B -O test_certificate.py
    sha256sum -c SHA256SUMS

The certificate uses 384-bit outward integer intervals, a complete degree-80
analytic Taylor enclosure on 152 prescribed cells, explicit infinite tails,
and Rouche's theorem. No mpmath, zeta, incomplete-gamma or eigenvalue oracle is
called by acceptance. Ordinary mpmath scouts only selected the rational center.
The code and analytic enclosure proof need independent review.

`SOURCES_AND_VALIDATION.md` records the frozen repository orientation, classical
sources, actual execution, and omissions. Main, the pending integration, prior
research and canonical/formal statuses are not modified by this add-only record.

The outcome is not a full proof proposal awaiting a routine last check. The
missing global sign is stated as unproved, and the rejected truncation step is
not replaced with an assertion that the modular tail must fix it positively.
