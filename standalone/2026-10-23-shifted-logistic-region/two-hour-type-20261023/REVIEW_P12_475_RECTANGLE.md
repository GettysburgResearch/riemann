# Independent review of the R=4.75 low rectangle

Reviewed 23 October 2026. Verdict: the parameter change and exact scalar replay pass. This is the low-height component only; the high-height Ford/Revers adapter and the full global-minimum assembly are separate inputs.

Reviewed and rerun:

- `../two-hour-root-20261023/verify_p12_475_fraction.py`, SHA256 `02dfaf5ae18becb4688d80ba79bef8ca76752ec7d95749c1ff465ec0c520837d`.
- Output `P12_475_FRACTION_CERTIFICATE.json`, SHA256 `da296619225f33ed0c1f7a7327b3b6e3ce75c23b467f21fed6bf5da17f7b6065`.

The unchanged exact interval engine is pinned to `68f31c13bbc906e99dfdb283648415cf52473861b825ffa15ee608c301fafb3a`. I previously independently derived and reviewed that engine and the P12 quadratic-sigma scalar reduction. This review checks the new domain rather than treating the old domain as automatic authorization.

The new box is 0<=A<=4/19 and 287/10<=log(t)<=60, with c=153/400 and d=2/25. Although 4/19 exceeds .21, the two relevant small parameters are A/log(t) and A/log(t)^2. The exact checks correctly show eta<.0075 and A/log(t)^2<.21/28^2 throughout. Thus the inherited frequency-cutoff correction is still an upper bound. The explicit twelve cutoff inequalities are also replayed. The lower sigma bound is above .99, and c+144d<28 keeps every sigma below one; the old alpha, gamma, tail, curvature and real-axis bounds remain within their domains.

The exact check exp(28.7)<3*10^12 makes the low endpoint overlap the imported finite verification; it creates no uncovered height interval. The upper endpoint is exactly 60 and must be matched by a separately proved high-height exclusion. The old kernel, exact P12 coefficients, prime gain, negative real-axis term and varying-sigma loss are unchanged. The latter is independently checked using the same coefficient second moment and four-prime upper sum.

The isolated Python replay accepted 31 boxes in 61 evaluations. Their interiors are pairwise disjoint, they lie in the stated box, and their exact total area is 626/95. Every lower interval margin is positive; the minimum is greater than 0.0001906387685. The unsupported-A negative control is also retained. The checker has no floating-point acceptance condition.

This receipt verifies the scalar rectangle and its elementary domain interfaces. It does not alone prove a zero-free region, certify the external finite-height computation or Revers input, or establish any fixed half-plane or RH statement.
