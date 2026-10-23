# Independent review of the physical quartic orientation correction

23 October 2026. Reviewed `two-hour-type-20261023/QUARTIC_PHYSICAL_ORIENTATION.md`.
The O1--O6 algebra and coprime-pair CRT interface check: the cross phase is
chi_c^e(d)chi_d^-e(c), hence fixed finite reciprocity data, while the
transformed c coefficient retains both tau(chi_c^e) and chi_c^-e(k).
The codec gamma^2=mu*alpha then gives the two orientations stated there.

In particular the negative-sign physical coefficient is proportional to
alpha^-1 gamma(c)chi_c(k), whereas the native series contains
gamma(c)bar chi_c(k). Their difference is a moving quadratic twist.
Changing the additive Fourier sign only replaces k by -k; conjugating
both factors does not fix their mismatch. The exact native expression
uses numerator k^3, including literal zeros. The coprime pair already
exhibits the obstruction, so shared-divisor branches cannot repair it.

This review checks the symbolic interface and the one-prime distinction,
not another execution of the exact finite-field checker. The native
all-row tail remains a valid separate statement; its transfer to the
physical inverse requires the newly identified numerator/twist interface.
