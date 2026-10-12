# Independent review of the directed Hardy-Z endpoint certificate

Status: PASS for the stated finite existence inference, reviewed October 10, 2026.
Scope: the current nine disjoint intervals in `../certificates/certify_hardy_z.py`; no simplicity, uniqueness or completeness claim.
What ran: independent read and replay at 128-bit precision with Python 3.12.14 and python-flint 0.9.0. The code had been expanded from four to nine anchors during this review; the replay used the nine-anchor version.
Smallest remaining gap: finite anchors do not discharge any all-height hypotheses in the downstream compact-domain argument.

The script uses exact integer and rational inputs and Arb/FLINT enclosing operations for pi, log-Gamma, exponential and zeta. The real balls exclude zero with each prescribed sign, including the endpoints near zeros (21,25,33,41,48). Every imaginary ball contains zero. Explicit exceptions preserve the checks under Python optimization.

The mathematical inference is valid. Log-Gamma has its analytic branch on the right half-plane, real on the positive real axis. For real t the zeta functional equation proves that exp(i theta(t)) zeta(1/2+it) is exactly real and continuous, where theta(t)=Im logGamma(1/4+it/2)-(t/2)log pi. The imaginary-ball test is a numerical consistency check; exact reality comes from that functional equation. Thus opposite certified signs imply a zero in each **open** endpoint interval by the intermediate value theorem. The nine intervals are disjoint and positive, so they supply nine distinct critical pairs; squaring their positive ordinates preserves the interval order.

No correction to the sign/branch/IVT logic was identified. The replay used the declared python-flint 0.9.0. The script records the runtime version but does not enforce that exact version; reproducibility relies on the environment's pin and the receipt. This is a minor provenance observation, not a mathematical failure of the replay.
