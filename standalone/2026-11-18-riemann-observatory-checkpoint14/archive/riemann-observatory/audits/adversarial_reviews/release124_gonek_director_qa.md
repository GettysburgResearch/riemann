# Independent QA of the Gonek source adjudication

18 November 2026. I checked the director's statement and local repairs against the exact journal scan, SHA-256 `dfdd2444a2f62f1947c897e87101080225714dbf1f21db8ca19096d2a6e80fc3`. The earlier version check shows the current Rochester faculty copy matches byte-for-byte. No separate Springer PDF manifestation or separately indexed correction was recovered. This review checks the director synthesis and its cited passages, with the independent complete reviews supplying whole-work coverage.

## The theorem and local repairs

The rendered p. 123 states (4) with a real inclusive shift (|\alpha|\le L_T/2), the sign ((-1)^{\mu+\nu}), the ordered arguments (H(\mu,\nu,2\pi\alpha)) and (H(\nu,\mu,-2\pi\alpha)), and a fixed-order error. The p. 124 kernel has the factorial and denominator given by the beta integral. The page makes the error constant uniform in the stated shift and explicitly introduces RH only for Corollaries 1 and 2. The diagonal coefficient at (\mu=\nu=1,\alpha=0) is (1/12), giving (T\log^4T/(24\pi)). Stieltjes partial summation with the left boundary term gives the stated strict positive tail. Multiplicity, physical shift and exact-cutoff handling agree with the proof scope.

All three proposed finding groups are bounded to the journal scan.

- On p. 123, the contextual equation (2) omits the sign at odd total order. At ((\mu,\nu)=(1,0)), the differentiated functional equation gives negative real leading term (-T\log^2T/2), while the display has the positive term. The discrete source theorem (4) has the correct sign.
- On p. 129, the printed phase has value −1 at zero after the constant phase has already been taken outside. Adding one gives a double zero and restores the exact phase decomposition for real saddle parameter (r). This repairs the auxiliary identity.
- On p. 140, the printed gap multiplier is the reciprocal of the p. 125 definition. Bounded gaps make the printed reciprocal normalization's limsup zero, whereas the defined normalization has limsup at least one. The p. 125 corollary itself uses the correct quantity and gives the weak bound.

The shrinking arcs do not justify literal coverage of the initial fixed-height interval. On a fixed bulk interval, the normalized eventual gap condition gives overlapping arcs with a strict margin. With the sine-kernel integral from Corollary 2 and the continuous second moment, the comparison yields (F(\beta)\ge1) for every (\beta>\lambda). Passing from the strict numerical (F(1.9)<1) through continuity gives the stated gap consequence. The bulk coverage is a proof repair and warrants no separate verified-error group. The gap implication retains RH, unlike the finite integral enclosure.

[Director adjudication](director_gonek_whole_round15.md) · [Local independent review](weighted89_gonek_local_adjudication_input.md) · [Version history](release123_gonek_version_history.md)

## Exact certificate and draft integration

I replayed the code with SHA-256 `67dd5cd4d7664bf419aa4443b7a92ba72581dff726aab05913670f4c994c2ace` in a separate directory. It reproduced the retained JSON byte-for-byte. I independently matched the cosine expansion after rescaling the interval, which gives coefficient (2(\pi\beta)^{2j}/((2j+2)!(2j+1))) for the mean squared sinc, with alternating signs. The first omitted term has (j=41) and negative sign, and subsequent absolute terms decrease because (\pi\beta<6). The rational enclosure preserves the strict inequality below one.

The draft source integrator has one Gonek whole-work promotion and three separate witnessed displays. The two additional events are Level 1 exact-edition readings. The Morse reading uses all 33 pages of arXiv v6, SHA-256 `307d253d70abc7d8ef3d24355e9ab7708010bda18c7b9060a4913033c6e224be`. The Bombieri–Lagarias reading uses the 12-page author manuscript, SHA-256 `cd13c8560f961c68e21256e5ba107bdd08fa7f34ce1e2cffbd4b63a16e8d48e0`. Their separately paginated journal versions are distinguished. No live promotion, finding merge or master rebuild was performed.

[Exact gap receipt](../../experiments/results/director_gonek_gap_round15.json) · [Draft source integrator](../../scripts/integrate_round15_sources.py)
