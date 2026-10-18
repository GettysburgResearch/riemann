# Growing orders for the full native Mobius moment

**PROPOSED source-qualified proof; independent mathematical review required.**
The common 31/32 Hecke theorem and de Faveri's fixed-field zero density are
explicit inputs. This is not a new zero-free region or a proof of RH.

The native sum is the original ideal-Mobius Gaussian A_u(D), with every row,
nonunit zero, repeated sixth-power core and infinite Gaussian tail retained.

For L=log D, ell=log L, m=log ell, one D0 works simultaneously for

    D>=D0, 1<=p<=ell/m, 2<=H<=D^(p/4):

    sum_(Nu<=H) |A_u(D)|^p
       <= H^(1/6) D^(31p/32 + 100 p m/ell + L^(-1/4)).

Thus any p(D)>=1 with p(D) log log log D=o(log log D) satisfies the
H^(1/6) D^(31p(D)/32+o(1)) bound. In particular even orders genuinely tend
to infinity. There is no hidden C_p; D0 remains field/source dependent and
unevaluated, and can be far beyond computational scales.

This is stronger UNIFORMITY than the preceding fixed-order theorem, not a
better fixed-order exponent. Updated #983 already has fixed-core growing
mask transfers and a fixed-order two-class density-native bound. The old
53-threshold partition and Euler algebra are credited, not rediscovered.

The essential new proof estimates the logarithm of the reciprocal near the
INPUT boundary with explicit delta dependence, uses a subpower small-core
cutoff exp(sqrt(log D)), and fixes density losses before raising any moving
power. One cannot infer this by substituting p(D) in an unspecified O_p bound.

For each fixed kappa>0 the same proof, uniformly for p<=ell/m^2, saves a
fixed power on the complete sector whose sixth-free core has norm >=D^kappa.
The unresolved small cores include the original principal Mobius source.
The critical exponent 1/2 has not been reached.

Read PROOF.md, then SOURCES.md and VALIDATION.md. Run:

    python replay.py

The checker uses exact rational algebra and checks the finite certificate,
disc margins, uniform exponent budgets, literal mask identities and negative
controls. It is not a proof assistant and computes no Hecke L-values or zeros.
Publication status is in the enclosing bundle's PUBLICATION.md. This packet
contains no claim of a successful remote push.
