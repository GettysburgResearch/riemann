# Independent review of the R=4.72 low-height rectangle

23 October 2026. Reviewed `../two-hour-root-20261023/verify_p12_472_fraction.py`, SHA256 `50d75fee1e1a01feebab763fe8086dcd6d464ef4b306c3e68afcc02be0e57ab6`, and its output `P12_472_FRACTION_CERTIFICATE.json`, SHA256 `f83ed356819fb6d3e93a107ff64c32ee47a464bbc2fbbd4253379b692afb2217`.

The change from the previously reviewed R=4.75 certificate is the exact rectangle A in [0,25/118] and log t in [287/10,52]. The scalar formula, P12 polynomial, c=153/400 and d=2/25 quadratic profile, kernel, prime gain, real-axis gain, and prime-variation cost are unchanged. The imported exact engine is pinned to SHA256 `68f31c13bbc906e99dfdb283648415cf52473861b825ffa15ee608c301fafb3a`.

The larger A endpoint is legitimate: A/log t remains below .0075 and A/(log t)^2 remains below the original .21/28^2 cutoff envelope. The per-frequency cutoff inequalities are rechecked exactly, sigma stays in (.99,1), and the coefficient second moment and four-prime variation bound are unchanged. The exact inequality exp(28.7)<3*10^12 supplies overlap with the imported finite verification. The high endpoint is exactly 52 and must be matched by the separately reviewed shifted-center exclusion.

Normal and python -O replays both passed with identical reported rational results: 28 boxes, 55 evaluations, exact covered area 1165/236, minimum lower bound

    597954910911225340546815071985262352157698808551526845 /
    6277101735386680763835789423207666416102355444464034512896

which is approximately 0.00009525971317945992. The unsupported-A negative control was rejected. Exact nonoverlap and area checks cover the entire rectangle. Floating point is used only for the displayed decimal, not for any acceptance decision.

No additional defect was found. This receipt certifies the changed scalar domain and elementary interfaces, not the external analytic lemmas or the complete global theorem in isolation.
