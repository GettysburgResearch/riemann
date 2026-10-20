# Positive Mellin domain in the alternative fixed odd-class guard

20 October 2026. Supplementary source-domain audit only. The frozen
cubic guard remains the input to the full-family theorem. This note
makes no estimate uniform in a growing auxiliary prime.

The alternative in `ODD_CLASS_GUARD_EXPLORATION.md` has local Mellin
multipliers with denominator `1-q^(-6z)`. They are holomorphic on
`Re z>0` but can have poles on its boundary. Consequently one must not
assume arbitrary power decay of its sheet profile at zero.

The actual high-side argument requires only this positive domain:

- In the pinned Ope26b `05-poisson.tex`, lines 60--74 establish local
  weighted integrability for every positive real part. Lines 309--328
  justify absolute orbit unfolding using a sheet majorant
  `O_sigma(T^(-sigma))`, with `sigma>1` for the frequency sum, and give
  Mellin inversion on every positive line. Initial inversion uses `z=2`.
- In `06-zero-free.tex`, the principal remainder uses `Re z=.16`;
  nonprincipal rows use `.4`; the far frequency tail moves right to the
  fixed line `350000`. The last step explicitly invokes only holomorphy
  on the positive half-plane. No negative small-argument shift appears.
- Liu2610.26835v1, (13.11), starts at `z=2`. The principal remainder
  uses `Re z=33/200` in (13.12); the modified nonprincipal contours in
  Sections 13--14 have `Re z>=17/50`. The shift to `z=-1/4` in
  Section 13.4 is a separate zero-detector Gamma integral, with no
  sheet Mellin multiplier in its integrand.

For each fixed auxiliary prime, restricting the local integral to one
of six valuation classes preserves all positive weighted integrability
estimates. The six multipliers and their derivatives are bounded on
each fixed compact positive strip; archimedean integration by parts
continues to supply arbitrary vertical decay. The finite class split
therefore meets the identified high-side domain and tail requirements.
It introduces no crossing of a new boundary pole.

This resolves the specific small-T contour concern for a fixed prime.
It neither supplies uniform constants as that prime grows nor removes
the leakage among nonprincipal valuation classes proved in the
exploratory note. The original reviewed cubic guard is unchanged.

Source pins: Ope26b commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`;
`05-poisson.tex` SHA256
`bd5e53c2d9436aa1c621dca2d1c423035b610b423f064f7d5b6e19f3d9f31992`;
`06-zero-free.tex` SHA256
`c565166640d5e8210a2af70f00f6b9072112033a182ec7dede17e1517e76be33`.
Liu2610.26835v1 HTML SHA256
`5b128f3cedb4d6ecfe3a3d57b1290cb576cac03092cf0b807c6f8092abf864c6`.
