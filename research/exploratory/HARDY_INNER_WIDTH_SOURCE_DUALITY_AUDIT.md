# Independent audit: all-inner width and the source dual-jet interface

Status: exact-source review passed. The all-inner finite-denominator width
theorem and convention-consistent source interface are accepted. Native
cofinal accounting, total charge, free energy and descent remain open.

Reviewed source: ef7bbb8dca978269f24e7ff9d97b6dceeed5b460.
Programme copy: c59a92e74a86aa86c0925754e41640ff00aff701.
Review date: 2026-08-31.

The root read the proof, producer, complete fixture, tests and manifest,
independently reconstructed the analytic and matrix arguments, and replayed
the frozen checks. A separate reviewer independently checked that exact
scientific identity, including additional genuine Fourier-weight controls.
No repair of the five frozen files was required.

## Frozen identities

The reviewed Git blobs are:

- HARDY_INNER_WIDTH_SOURCE_DUALITY.md:
  955b92fe277bcdb3d6e260b5cc9dc02dd3f49144.
- hardy_inner_width_source_duality.py:
  bec60c15252f67eeeddffb50121ce0180eab10ee.
- hardy_inner_width_source_duality.json:
  02debe76fd3f1b41a1f40314948935ec05701867.
- hardy_inner_width_source_duality.sources.json:
  7aebd109b49d211b635ecc848a4063aaf7ceedb3.
- tests/test_hardy_inner_width_source_duality.py:
  d60a67be7157a111ddfb2d1e6fd77e1c148490f9.

The fixture LF-normalized SHA256 is
fc29c7e460cf5c1be2f813376a4619d65879acfd497c39db42c12fdfe3fb6fef.
The eight primitive Git/blob/LF source bindings authenticate. The resident
executable helper is hash-checked before import and checked again during
report construction. All five programme-copy blobs equal the source blobs.

## Analytic theorem

For denominator zeros b_j=a_j+i y_j, listed with multiplicity, the
Takenaka--Malmquist orthonormal basis has squared boundary modulus

    y_j / [pi ((x-a_j)^2+y_j^2)].

Multiplication by any genuine inner numerator preserves this modulus.
The unitary Fourier normalization gives the nonsharp Hausdorff--Young
constant (2 pi)^(-1/4) from L^(4/3) to L^4. Holder on a frequency set of
measure Delta and the elementary integral bound
integral (1+u^2)^(-2/3) du <=8 give the individual bound
C sqrt(Delta y_j), C=16/pi^(3/2)<4. Plancherel gives the individual unit cap.

Summation proves

    tr(G^-1 H_I) <= sum_j min(1,C sqrt(Delta y_j))
                 <= min(n,C sqrt(Delta) sum_j sqrt(y_j)).

Positivity gives the stated Loewner bound, while Cauchy--Schwarz gives
beta<=C sqrt(Delta n S), S=sum y_j. The proof uses no separation, numerator
degree, numerator phase moment or finite-inner approximation. It therefore
includes complex confluence, infinite Blaschke products and singular inner
numerators at finite denominator rank.

The physical band projection is never commuted with an inner or outer
multiplier. Absolute width, not relative width, drives this theorem.
The earlier finite-degree translated-band theorem and its fixed-width
delay counterexample are compatible with it.

## Source convention and the historical mismatch

With column Fourier kernels

    E_j(x)=i/[sqrt(2 pi)(x-conjugate(b_j))],
    G_ij=i/(b_i-conjugate(b_j)),

the coefficient matrix of the multiplier adjoint is A=J_B-star, not
the raw lower value-jet matrix J_B. The root checked the reproducing
normalization, Leibniz rule, derivative Gram and HT4 conversion separately:

    E_HT=E S0,  G_HT=S0-star G S0,
    A_HT=S0^-1 J_B-star S0,  S0=diag(i^r).

For simple nodes V=diag(B(b_j)), the physical adverse Gram is
V G V-star. The raw-value expression V-star G V from the historical
source interface is incompatible with this explicit column Gram.
An alternative inner-product convention is not ruled out; it must change
all associated synthesis and coefficient conventions consistently.

The three-node control b=(i,1+i,2+i), B(z)=(z-2i)/(z+2i) distinguishes the
two conventions:

    physical charge = 235/117 <3, physical deficit rank =1;
    raw-value charge = 1943/585 >3;
    det(G-V-star G V) = -64/14625.

In an additional independent SymPy calculation, using explicit matrices
rather than the packet helper, the root obtained

    Zphysical(tau) = (1-tau)^2 (1-tau/117),
    Zraw(tau) = -(5 tau^3-339 tau^2+1943 tau-585)/585.

Already at tau=1/2, these are 233/936 and -2419/4680 respectively.
Regularization does not repair a mismatched convention.

Historical scientific files are unchanged. Their algebraic commuting-matrix
congruences and relative Loewner inequalities remain algebraically valid
for the forms they define. Their physical interpretation, absolute
contraction estimates and determinant positivity require the corrected
source coefficients. This audit does not silently certify all downstream
historical free-energy consumers.

## Outer covariance and scope of suppression

For the actual local source R=O(Bplus-Bminus), the retained denominator
multiplicities imply J_R=J_O J_Bplus. Taking Riesz adjoints gives commuting
coefficient matrices Rc=CA=AC, with C=J_O-star and G_O=C-star G C.
The determinant and weighted-trace covariance retain that exact outer
metric. Dropping it or treating a freely chosen matrix as source jets is
not permitted.

From A-star G A<=G, finite-dimensional contraction duality gives
P=A G^-1 A-star<=G^-1. For total physical charge Q=tr(PG) and band charge
S_I=tr(PH_I),

    S_I <= min(Q,beta,min(1,beta)Q).

The zero-charge case is explicit. Dividing a source-relative factor by
denominator rank is not justified. Rank-normalized and independently
globally normalized bounds have their separate stated hypotheses.

The actual-Xi scalar envelope has absolute width
(KM/pi+o(1)) exp(-X)/X at fixed K,M. Applying the global bound requires
the corresponding denominator count and height ledgers, and a justified
order of all native limits. Neither X proportional to log(T) nor a
cofinal count estimate is supplied by this packet. Small band charge is
not small total charge and does not remove forced unit eigenvalues.

## Reproduction and independent controls

The root ran all 30 tests in normal Python (6.333 seconds) and with -O
(6.380 seconds), both producer modes, Ruff lint/format and whitespace
checks. All passed. The producer passed again after import.

The independent reviewer reported 30 tests in both modes, all source
and artifact checks, both producers and Ruff. It also independently
verified, normally and with -O:

- nine actual source/dual-jet cases, including three held-outs with
  complex confluence, a fourfold collision and a 1/100 near-collision;
- 27 genuine positive Fourier-frequency-weight controls with
  weights exp(-2 sigma t), sigma=1/3,2,7/5, using independent partial
  fractions rather than fitted abstract weights;
- nine Takenaka--Malmquist cases, 28 rational columns, with every
  partial-fraction identity and cross-Gram checked.

Those smooth positive weights are not sharp-band integrals or numerical
Xi computations. The packet's own positive matrix weight is explicitly
an abstract covariance control, not a claimed physical band Gram.
The exact machine checks do not formally prove the analytic theorem.

## Classical boundary and acceptance

The root checked the model decomposition (2.12), finite-space statements
(2.18)--(2.19), upper-half-plane normalization and multiplier-adjoint
identity in
[Fricain--Hartmann--Ross](https://arxiv.org/pdf/1605.07418v2).
The nonsharp Fourier inequality was independently derived by interpolation.
The [Beckner publisher record](https://annals.math.princeton.edu/1975/102-1/p11)
and [Takenaka publisher record](https://www.jstage.jst.go.jp/article/jjm1924/2/0/2_0_129/_article)
support the classical attribution; the independent reviewer also checked
Takenaka's original paper. No assertion of external priority follows.

Accept IW1--IW9 with their explicit hypotheses and the separate
convention-relative correction. Keep the frozen fixture's historical
subject-to-review status unchanged; this audit records acceptance.
Do not infer native exhaustion, a bound for total Pick charge,
free-energy closure, reverse-Rolle descent, a critical-line percentage,
RH or GRH.

