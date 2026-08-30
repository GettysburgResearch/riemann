# Independent audit: actual-Xi uniform companion count and width

Status: PASS FOR ACTUAL GEOGRAPHIC PACKETS; NATIVE COFINAL CAPTURE OPEN.
Review date: 2026-08-31.
Programme: #763, carrying the earlier actual-Xi research.

## Frozen identity

Reviewed source: 76454e3db0ccce8f500297ea27668d6088b5091a.
Authoring base: 08187bdfae119f66c8c82baca2d1c1068e48ff40.
Imported scientific commit: f32b4d9fed173f32a4d95909cd728194e3cb73ce.

| Artifact | Git blob in reviewed state |
|---|---|
| XI_UNIFORM_COMPANION_COUNT_WIDTH.md | a97d25f556a2bd085a4749d1e96d883a0646e666 |
| xi_uniform_companion_count_width.py | 6a4a97b14bbe2774de75ff619fb915c7a862294e |
| xi_uniform_companion_count_width.json | 295b2f637d8a59e5e1df61d8cd34835f26dc5025 |
| xi_uniform_companion_count_width.sources.json | b63b5f7431c4580ceea956765c0b61a5e3e75aa7 |
| tests/test_xi_uniform_companion_count_width.py | 04d15c9ed5449f8d1951caf3b9ba70c1cf496592 |

The first four paths are in research/exploratory/.
Fixture LF-normalized SHA-256:
093bb4ab1a60057531796a170884c8fbef6af6c12a2ef71d80abe4adb43b8cf9.

All ten primitive Git/blob/LF-hash bindings and four current-artifact
hashes were independently authenticated. In particular L-106610 here is
the Riemann--Siegel gauge-factorization file, not the different historical
residue-sign file with the same claim number.

## Mathematical review

The [proof](XI_UNIFORM_COMPANION_COUNT_WIDTH.md) has two distinct results:
a uniform actual-entire-function zero count, and a normalized band bound
for finite geographic factors. Neither is a native cofinal-capture theorem.

### Uniform count

The literal standard Xi normalization is retained: Phi = 2 phi_0 in the
full-line Fourier convention, with no frequency rescaling.
The primitive theta bound is Phi(u) <= 6 pi^2 exp(9u/2-pi exp(2u)) for u>=0.

Using u^r <= r! exp(u), pairing both halves of the integral, and substituting
v=pi exp(2u) gives

    abs(Xi^(r)(z)) <= 6 pi^2 r! pi^(-a) Gamma(a),
    a = R/2 + 11/4,  abs(z)<=R,  0<=r<=6.

This gives logarithmic maximum growth O(R log(R+2)).
The two companions use opposite noncancelling anchors:

    (Xi+i lambda Xi')(i) = h(1)+lambda h'(1),
    (Xi^(5)-i lambda Xi^(6))(-i)
        = i [h^(5)(1)+lambda h^(6)(1)].

Here h(v)=Xi(iv), and the displayed h-derivatives at 1 are strictly positive
by the positive even kernel. The second anchor is imaginary; only its
modulus is ordered. Both lower bounds are uniform for lambda in [0,1].

Jensen centered at the appropriate anchor uses inner radius R+1 and outer
radius 2(R+1), within the origin-centered disk of radius 2R+3.
Consequently the Gamma parameter there is R+17/4, and every counted inner
zero contributes at least log(2). Multiplicities and boundary-circle zeros
are handled. The two companion counts sum to O(R log(R+2)), uniformly in
lambda. Divisor reduction can only lower that count.

### Exact physical scale and geographic application

The same physical constant lambda_j=1/omega(t_j) gives
X_j=2/lambda_j=2 omega(t_j)=log(t_j/(2 pi))+O(T^-2).
It is not changed into a frequency-dependent multiplier.
The previously reviewed CB18--CB20 envelope therefore has absolute width

    Delta_j = (2 K M+o(1))/(t_j log(t_j/(2 pi)))

for fixed odd K and fixed M>0. Uniformity follows from the actual tail
envelope and the dyadic physical scale, not from a pointwise inversion.
No growing-order claim or coverage outside [X_j/2,2X_j] is imported.

Actual reduced-denominator zeros in abs(b)<=C_0 T and 0<Im(b)<=eta have
total selected multiplicity O(J_T T log T), including repetitions across
the J_T windows. Their height sum is at most eta times that count.
The all-inner theorem then gives

    sum_j tr(G_j^-1 H_Ij)/N(T,2T)
        = O(J_T/sqrt(T log T)) = o(1),

for J_T=ceil((log T)^B) with B fixed. This does not need the historical
cofinal height-transfer claim. That unproved claim is not silently imported
through the optional stronger height-budget variant (UC14).

### Physical adjoints and outer factors

The bound permits any genuine inner numerator, including infinite and
singular inner factors. Its denominator factors are still finite.
For compatible physical data the coefficient matrices are

    A=J_Bplus-star, C=J_O-star, Rc=J_R-star=CA=AC,
    G_O=C-star G C.

The exact identity is
tr(G_O^-1 Rc-star H_I Rc)=tr(A G^-1 A-star H_I), followed by the dual
contraction. No multiplier is commuted through the band projector.
Confluent HT4 coordinates retain their diagonal i^r phase conversion.
Historical raw-value determinants are not repaired or certified in place.

## Replay and primary-source checks

The root read all five packet files, reviewed the load-bearing derivations
against the bound actual-kernel, band and source-duality results, and
independently authenticated every declared primitive and artifact identity.
All 32 tests passed normally and under Python -O (1.304s and 1.288s in
this replay). Both complete producer modes, Ruff lint/format and the full
base-to-reviewed-state whitespace check passed. The author worktree was clean.

The root separately reconstructed 63 published growth, shifted-geometry,
Fourier-phase, scale, width, squared-bound and cosine-factor controls.
A separate reviewer read all ten bound source notes, authenticated the
same identities, replayed both test/producer modes, reconstructed
53 algebraic controls and rejected 22 additional tampered inputs.
Its separate nonreal/confluent three-node example verified literal residual
jets, outer covariance and all seven principal minors of the dual contraction.
It found no actionable mathematical or implementation gap within scope.

The classical growth input agrees with [DLMF 5.11.1](https://dlmf.nist.gov/5.11.E1);
the physical gauge expansion uses the corresponding
[digamma expansion](https://dlmf.nist.gov/5.11.E2).
The normalization agrees with [DLMF 25.4.4](https://dlmf.nist.gov/25.4.E4).
The normalizing zero-count scale agrees with
[Hasanalizade--Shen--Wong, Section 1, (1.1)](https://arxiv.org/pdf/2107.06506v1).
Only the classical O(log T) error scale is used, not a modern numerical
constant. These external formulas were manually consulted; their remote
page bytes are not authenticated by the fixture.

Reproduce the resident controls from the repository root:

~~~text
python -B tests/test_xi_uniform_companion_count_width.py
python -B -O tests/test_xi_uniform_companion_count_width.py
python -B research/exploratory/xi_uniform_companion_count_width.py --check
python -B -O research/exploratory/xi_uniform_companion_count_width.py --check
~~~

Strict bounded inputs and typed complete JSON comparison reject Boolean
integers in numeric controls, floats, duplicate/nonfinite JSON, changed
sources/artifacts and oversized inputs. Result checks survive -O.
These are bounded exact algebra and source checks, not machine verification
of Jensen, Stirling, arbitrary-inner limits or any unbounded analytic proof.

## Remaining boundary

The cosine control is correctly restricted to a positive even atomic
Fourier source, not Xi. It shows that finite geographic counts do not imply
a finite global shallow denominator: infinitely many upper poles remain
at height artanh(lambda), with no common numerator cancellation.

No proof here identifies a native cofinal family with the geographic
packets. Omitted directions, approximation zeros, collars, boundary terms,
outer/source compatibility and the order of limits still need a ledger.
Infinite inner numerator scope is not infinite denominator scope.

The conclusion is an absolute band trace divided by N(T,2T), not a
vanishing source-relative ratio, not a rank-divided Loewner factor,
and not a bound on total charge. No forced unit eigenvalue is deleted.
Free-energy, critical-line percentage, reverse-Rolle descent, RH and GRH
claims remain unproved. Stronger interfaces require new scientific packets.
