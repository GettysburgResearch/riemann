# O-26701 — Affine Green boundary-charge reconnaissance

Claim ID: `O-26701`  
Title: The canonical maximum positive Green edge decreases rapidly on the first growing endpoints  
Status: **FLOATING RECONNAISSANCE / NOT A CERTIFICATE**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-26702`; PR #248 `L-24509`

The endpoint-projected Dirichlet Gram was assembled in ordinary floating
arithmetic. For the parabolic residual, the canonical exact-equality Green
potential was solved and
\[
C_X^G
=
\max_m(F_X(m)-F_X(m-1))_+
\]
was measured.

| \(X\) | prime-power columns | \(C_X^G\) | \(\sqrt X\,C_X^G\) | Green energy | minimum signed \(b_X^G\) |
|---:|---:|---:|---:|---:|---:|
| 100 | 35 | 0.1629410767 | 1.6294107669 | 9.0663922938 | -0.1266399072 |
| 200 | 60 | 0.1042884631 | 1.4748615890 | 11.3718845102 | -0.0865829427 |
| 500 | 114 | 0.0578002112 | 1.2924520140 | 14.4192217154 | -0.0522389627 |
| 1,000 | 193 | 0.0349355523 | 1.1047591665 | 16.6467425773 | -0.0333491199 |
| 2,000 | 333 | 0.0205629649 | 0.9196037459 | 19.1898592004 | -0.0171501774 |
| 5,000 | 711 | 0.0104517987 | 0.7390537755 | 22.4627676155 | -0.0098197482 |
| 7,500 | 998 | 0.0077859948 | 0.6742869323 | 24.0082223996 | -0.0062615500 |
| 10,000 | 1,280 | 0.0061593874 | 0.6159387439 | 24.9914482647 | -0.0056041285 |

The striking feature is the separation
\[
C_X^G\ll\sqrt{\mathcal G_X}
\]
in the observed range. The full Green energy grows slowly, while the one-sided
maximum edge decreases roughly at a square-root scale.

This is precisely why the affine boundary lift is a different proof target
from GET.

No directed intervals were used. The table does not prove ABLC, an asymptotic
law, or RH. A hypothetical off-line zero could force polynomial growth only at
much larger scales.
