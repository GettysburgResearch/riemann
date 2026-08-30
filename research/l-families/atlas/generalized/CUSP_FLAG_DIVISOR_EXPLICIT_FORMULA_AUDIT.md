# Independent audit: actual cusp-flag divisor and explicit formula

Status: PASS at the exact frozen source. This separate audit preserves the
original proposed packet's bytes and its classical-input boundaries.

Scientific source: a27781310ded92125ef16d97d78db4d97cec4c1b.
Authoring base: 282ce03941444d0e02daba5fde260ccb54a3f909.
Programme import: c68fc82fb7f48cc0958d7712d58f9126155d9c33.
Review date: 2026-08-31.

Root and a separate non-author reviewer read the
[complete proof](CUSP_FLAG_DIVISOR_EXPLICIT_FORMULA.md), producer, fixture,
manifest and tests. Independent analytic and arithmetic reviews passed.
No source repair or author coordination was required.

## Accepted statement

At each fixed level-one weight with dim S_k>=2, retain the full Miller
basis, ell=[q], W=ker ell and the exact completed period quotient

    Q_k(s)=det I(s)/det I_W(s)=A_k(s) L_k(s+k-1),
    A_k(s)=pi^-s (4pi)^(-s-k+1) Gamma(s) Gamma(s+k-1).

The pole-cleared matrix J=s(s-1)I is entire entrywise, with logarithmic
maximum growth O_k(R log(R+2)). Its full and W determinants are not
identically zero. Q_k and L_k are meromorphic of order at most one;
their unsigned NET zero/pole counts obey O_k(R log(R+2)) in their
respective coordinates.

The divisor of Q_k lies in a finite vertical strip. The uncompleted L_k
only receives a left-location conclusion, not that same strip.

If -log L_k(w)=sum b_lambda exp(-lambda w) on a sufficiently right
half-plane, then for phi in C_c^infinity((0,infinity)),

    sum_(rho in div Q) nu_rho integral exp(rho t) phi(t) dt
      = sum_lambda lambda b_lambda exp(-(k-1)lambda) phi(lambda)
        - integral [(1+exp(-(k-1)t))/(1-exp(-t))] phi(t) dt.

The first sum is absolutely convergent AFTER test pairing; no pointwise
exponential zero series is asserted. The atom sum is finite on the compact
test support. At weight 24, the actual fractional atom has mass

    88203653222400 (9/2)^(-23) log(9/2).

The atomic distribution has both signs. Neither it nor the signed divisor
is a positive spectral measure or a Weil positivity criterion.

## Load-bearing analytic checks

1. The lattice theta normalization is the half-Epstein normalization of
   the frozen period. Splitting the Mellin integral at one gives exactly
   1/[2s(s-1)], with residues -1/2 and +1/2. The fixed sesquilinear
   form coefficients are not conjugated as functions of s.

2. A uniform exp(-c u) theta tail over the whole fundamental domain
   would be unjustified. EF6 instead keeps the small shortest vector
   at large y. Cusp decay, the Gaussian shift bound, and the displayed
   AM-GM reserve yield |H_ij(u)|<=C_ij exp(-pi sqrt(3) sqrt(u)/4).
   The powers y^(k-3/2), y^(k-5/2), y^(k-2) in its finite constant
   agree with the measure and both Gaussian terms.

3. That square-root exponential tail justifies Fubini in the initial
   half-plane and local uniform convergence of the continued integral.
   The substitution v=sqrt(u) gives the gamma factor in EF9. This
   proves finite order directly, without importing an unproved global
   growth axiom for the determinant quotient.

4. I(2), I_W(2) are positive definite. Their pole-cleared determinants
   therefore give legitimate nonzero Jensen anchors at TWO, not at
   a possible zero. Inner/outer radii R+2, 2R+4 fit within the global
   radius 2R+6. The separate s(s-1) denominator costs two zeros/poles.
   Common determinant zeros only lower the unsigned bound.

5. The exact relation Q=det J/[s(s-1)det J_W] gives meromorphic finite
   order. Multiplication by the entire reciprocal completion gives
   the corresponding L result. No maximum-modulus bound is assigned
   to meromorphic circles through poles.

6. The normally absolute parent expansion tends uniformly to one
   sufficiently far right. This proves that L and Q are zero/pole-free
   there. Reflection Q(s)=Q(1-s) provides the left half-plane for Q.
   The gamma ladders prevent transferring that same strip to L.

7. Absolute smallness of the nonconstant series makes the minus-log
   expansion legitimate. Its positive frequency minimum and locally
   finite generator set give locally finite product coverage. The
   factor lambda is retained on differentiation, with the sign fixed
   by minus log. The exact first fractional atom cannot be a product
   of smaller frequencies: those are all integers.

8. O_k(R log R) unsigned count implies summability of
   |nu_rho|/|rho|^2 outside a bounded set. Two integrations by parts,
   with compact support away from zero and a left-located divisor,
   give absolute convergence of the test pairing.

9. The distributional passage does not require an unproved bound on
   a contour logarithmic derivative. Choose a real sigma right of
   the divisor of L and form the uniformly convergent regularized sum

       K_2(t)=sum nu_omega exp((omega-sigma)t)/(omega-sigma)^2.

   The distribution exp(sigma t) D^2[(K_2-K_2(0))1_(t>=0)] agrees
   with the divisor pairing for t>0. Its Laplace transform is the
   genus-one regularized pole series. Hadamard factorization of the
   actual order-one entire factors makes its difference from L'/L
   a constant. The inverse transform of that constant is supported
   at zero, precisely outside the allowed test support.

10. Shifting w=s+k-1 multiplies the atom by exp(-(k-1)lambda).
    Divisor addition contributes the two negative gamma ladders,
    counting their overlap twice. All cancellations with L are kept:
    the formula does not declare uncancelled gamma poles of Q.

## Primary-source check

Root read Muñoz--Pérez-Marco's relevant sections and Laplace proof,
including visually checking the displayed formulas on PDF pages
6 and 11--14 of
[Poisson-Newton formulas and Dirichlet series](https://arxiv.org/pdf/1301.6511v2).
Theorem 3.5 and Corollary 3.6 use the same minus-log sign, frequency
multiplier and restriction away from zero. The review uses their
Laplace argument, not the unrelated printed min-genus convention on
page 6 or the stronger degree equalities in Corollary 3.7. The direct
order-one factor argument in item 9 suffices for this packet.

[Zagier's Eisenstein-series paper](https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf),
printed page 277, equations (6)--(7), supplies the checked half/theta
normalization. Its relevant pages were visually read during source
review. [Cogdell--Piatetski-Shapiro, Theorem 2.3](https://people.math.osu.edu/cogdell.1/rorsc-www.pdf)
is compatible continuation/vertical-strip context, not a hidden growth
dependency. Remote PDF bytes are not authenticated by the offline hashes.
The PDF workflow clarified these normalization and theorem-scope checks.

## Independent finite reconstructions

Root independently reconstructed all twelve logarithmic prefixes
(128 nonzero coefficients), by solving an auxiliary-parameter reciprocal
and integrating its coefficients. An independent auxiliary differential
equation reconstructed each original F,L prefix. All 67 shifted L
coefficients, the exceptional weights 124/248 and prime-power zeta
corrections matched the fixture.

Four rational numerator/denominator controls gave sixteen exact atom-mass
checks. They distinguish a zero from a pole and verify that the factor
lambda cancels the logarithmic word denominator in the single-generator
case. They are controls, not replacements for the actual source.

Root also checked six gamma-ladder/endpoint panels, the AM-GM square,
the two-integration-by-parts boundary identity and four exact Mellin
integrals. Ten independently resealed semantic drifts were rejected in
normal and optimized Python.

The other reviewer rebuilt all twelve maps by multiset enumeration:
133 retained multisets reproduced the 128 entries without importing
producer/test algorithms. Cubic collision controls, all shifted masses,
six primitive bindings, four artifacts and both seals agreed. Forty-four
additional attacks (20 resealed payloads, six manifests, ten raw JSON
and eight type/cap inputs) failed in both modes.

These finite calculations do not compute any actual zero or period, or
machine-prove theta decay, analytic continuation, Jensen or Poisson-Newton.
The parent q/closed-word producer is intentionally not rerun by this
packet; its authenticated complete fixture and earlier proof/audit remain
load-bearing dependencies.

## Exact identity and release checks

Six primitive commit/path/blob/LF bindings were independently checked.
Five are the repaired family release at
b69c854d9e3dd1db7b82d95fe6f032fe47d5306b; the sixth is the unchanged
positive-spectrum proof at 1483ff25e9100276ac7064ba7d7d696b45afb9ea.
The family metadata repair did not change its mathematical coefficients.

| Frozen file | Git blob |
|---|---|
| CUSP_FLAG_DIVISOR_EXPLICIT_FORMULA.md | 1ec20ba529d34b833799d72515921fda7252da81 |
| cusp_flag_divisor_explicit_formula.py | 81f8f778488e83fe7ae7d0a2c9296031558449cb |
| cusp_flag_divisor_explicit_formula.json | 2eef1c6196789b852db99391b931d668da383b8e |
| cusp_flag_divisor_explicit_formula.sources.json | 0649c2b51271f92499903fc209e575422c482d61 |
| tests/test_cusp_flag_divisor_explicit_formula.py | cd121b856db740cf16bb78b7ff0cde1e4ad5a39a |

Fixture LF-SHA256:
bdf15afc43f5d246b494f0c9ebd3b0947a5ba6209c0ccfa0418513abc1db3922.

Payload SHA256:
fc904a2b5a7b3c8681b1061858742be2827bb28832ba13d7e17e4eed51af3c9a.

Root replay passed 36 tests normally (2.391s) and under -O (2.380s),
both complete producers, both independent reconstruction modes, Ruff
lint/format without cache and the full authoring-base-to-source whitespace
check. The non-author reviewer independently passed the same release gates.
No scientific source bytes were edited in the review or import.

Arithmetic is MIXED with exact rational and integer-coverage components.
The declared bounds are cutoff 28, support 512, word degree 16, 32-bit
primitive frequencies, 4096-bit internal coefficients, 500000 charged
work units, and 2000000 source/JSON bytes; the report used 1742 units.
The work budget covers declared expansions, not every Python instruction.
Logarithms remain symbolic multipliers, never claimed exact rationals.

Numerical growth constants, effective Jensen anchors, signed cancellation,
a useful zero-location theorem, positive Weil form, RH/GRH and external
novelty remain outside this acceptance.
