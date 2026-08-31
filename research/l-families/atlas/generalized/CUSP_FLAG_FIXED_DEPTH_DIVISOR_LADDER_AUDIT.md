# Independent review: fixed-depth cusp divisor ladder

Verdict: PASS for the written source-specific theorem at exact scientific
commit 070751bf7e96c1dbd6d4b3cfbb05dc70f5a2aa22.
The finite arithmetic checks pass separately; they do not machine-certify
the analytic integral estimates or any sufficient-weight threshold.

Review date: 2026-08-31.
Scientific parent: 7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e.
Reviewer: designated non-author agent signed_count_independent_audit.
No author contact, source modification, push, main-branch change, or amendment
was used. This audit is an additional file on a separate review branch.
The exact source has five additions and no parent-file changes.

## 1. Accepted result and quantifiers

For each fixed depth J and each fixed 0<delta<12, all sufficiently large
even k have the following actual completed-period divisor cluster near
c=k(1-s)=12J. The threshold may depend on J and delta and is not computed.

For every 1<=i<=J, the native determinant D_i=det(I|W_i) has exactly one
zero counting multiplicity in |c-12J|<delta. These zeros are real and
simple; D_(J+1) is nonzero there. Their locations satisfy

    c_(J,J) < c_(J-1,J) < ... < c_(1,J),   c_(i,J) -> 12J.

Consequently the adjacent quotient Q_J has one simple zero and no pole in
that disk. Each Q_i for i<J has one simple zero and one distinct simple
pole there. In particular this is a new genuine cluster for the ORIGINAL
first-coefficient quotient Q_1, not merely an unrelated adjacent quotient.
The zero in the right s-disk lies to the left of the pole.

Writing A_n=Gamma(k-1)/(4pi n)^(k-1) and
S_h=sum_(d|h)1/d, the accepted residue and gap are

    Res_right Q_i = 288 J^2 S_(J-i)^2 A_J/k^2 * (1+o(1)) > 0,

    c_(i,J)-c_(i+1,J)
      = [288 J^2 S_(J-i)^2/F_i(12J)]
          A_J/(k^2 A_i) * (1+o(1)),

    F_i(12J)=(J-i)/(24iJ).

Reflection produces the other cluster and reverses residue signs.
The positive s-gap is the c-gap divided by k.

For Q_1 at J=2,3,4, the residue constants are 1152,5832,8192;
the c-gap constants are 55296,209952,262144. For Q_(J-1), by contrast,
S_1=1 and the residue constant is 288J^2. These are not interchangeable.

For any fixed finite L, simultaneous application gives at least L simple
reflected zero pairs and L-1 additional reflected pole pairs for Q_1 at
sufficiently large weight. No fixed-weight infinite divisor count follows.

## 2. Independent analytic reconstruction

The complete new proof was read before the finite verdict. The native
normalization and load-bearing source passages were checked against CF,
NP, LS, AW and EP, with the separate accepted NP audit also inspected.
All fourteen literal source identities were independently authenticated.
The classical references below are mathematical imports, not offline
byte-authenticated artifacts.

1. **The partial chart preserves the source.** Descending elimination in
   DL6 makes the first J Fourier coefficients of h_l equal to the l-th
   unit vector. Each trailing basis preserves the exact W_i flag.
   The change from the Miller basis has determinant one, so determinant
   ratios and residue normalizations acquire no hidden factor.
   The residual class 2 uses r=14 and d=(k-14)/12.

2. **The tails are complete, not sampled.** The product majorant on the
   whole complex q-disc R=1/(1000k) is valid uniformly in the six classes.
   Since 24l<=2k and p_l<=k/4, its exponent is below 1/4 for k>=48.
   Cauchy followed by descending elimination gives H_l=2*3^(J-l) and
   the complete tail |h_l-q^l|<=B_J k^J rho^(J+1).
   The low-domain supremum and factorial bound are normalized against
   A_(J+1), with an exponential base at most 12/625<1/10.
   Powers of k and constants may depend on fixed J only.
   The eventual requirements Y>=1 and exp(-2piY)<=R/2 are not claimed
   at the ledger's illustrative weight 65536.

3. **The new projected dual estimate really gains the deep scale.**
   For N=J+1 and l<N, literal x-orthogonality picks out only Fourier
   frequency -(m-l). The bound |r_(m-l)|<=(m-l)rho^(m-l) changes the
   summand from a_m rho^(m+l) r_(m-l) to a bound
   |a_m|(m-l)rho^(2m). Cauchy--Schwarz therefore separates

       [sum_(m>=N)(m-l)^2 rho^(2m)]^(1/2)
       [sum_(m>=N)|a_m|^2 rho^(2m)]^(1/2).

   With L=N-l and x=rho^2, L+t<=N(t+1) gives directly

       sum_(t>=0)(L+t)^2 x^t
         <=N^2(1+x)/(1-x)^3<4N^2.

   Integrating in the original y^(k-2) weight yields DL14,
   2N sqrt(A_N G(f)), for EVERY f in W_N.
   This is not a claimed global Petersson-projection commutation.
   Reverse complex cross directions obey their own same norm bounds.

4. **No nonmodular moment estimate is smuggled into the argument.**
   The all-vector EP moment estimate is applied only to the actual
   modular f in W_N. The nonmodular tail h_l-q^l is bounded directly
   by its entire high-cusp envelope. The constant-term cross with q^l
   vanishes exactly; low-domain terms use the independently paid low
   mass. Thus DL15 holds in the full dual Petersson norm with no factor d.

5. **Deep inversion uses Hermitian part, not eigenvalues.**
   For a fixed closed buffered disk around 12J, DL16 gives
   Re(1/(2c))-1/(24N)>0. The LS complex-power estimate includes the
   O(log k) correction from the singular D(s) term.
   Hence the whitened deep block has uniformly negative Hermitian part
   of size k and inverse norm O(1/k). This holds on one fixed complex
   neighborhood, not a family of shrinking unverified domains.
   Combining both complete dual bounds gives the correction
   O(k^(2J+3) A_N), as in DL17.

6. **The native cross coefficient and its sign survive.**
   The mode h=m-l carries exponential-series coefficient 2sqrt(y).
   Substituting the exact half-order Bessel value contributes
   1/(2sqrt(hy)); the remaining factor is
   h^(s-1) sigma_(1-2s)(h), tending to S_h.
   The total exponential is exp(-4pi m y), giving exactly A_m.
   The Gamma-integral tangent bound for K_nu/K_(1/2) has error at most
   1/(8x), uniformly for the required real orders. All other high-tail,
   low-domain and deep-inverse terms are polynomial(k) A_N, hence
   exponentially smaller than A_m for fixed m<=J.
   DL22 is thus a source-specific positive coefficient, not an abstract
   two-by-two Schur example.

7. **Column scaling has the correct order.**
   For the earlier finite block, C_M=H_MM diag(A_m)^(-1), so

       H_MM^(-1)=diag(A_m)^(-1) C_M^(-1).

   Off-diagonal entries of C_M are O(1); after division by k they vanish.
   The limiting diagonal F_m(c), m<J, has no zero in the selected disk.
   Its inverse is O(1/k). In particular H_iM diag(A_m)^(-1)=O(1)
   and H_MJ=O(A_J), so the effective cross correction is O(A_J/k).
   The order of multiplication cannot be reversed. This pays the
   exponential-scale issue that a generic whitened norm would not pay.

8. **Zero counting has its fixed-domain hypotheses.**
   The scalar delta_i after all other blocks are eliminated is
   holomorphic on a fixed buffered disk and delta_i/(kA_J) tends locally
   uniformly to F_J. Real convergence and a dimension-free complex
   local bound justify the normal-family/identity argument.
   Cauchy's formula supplies derivative convergence.
   Rouche counts exactly one zero with multiplicity; conjugation makes
   it real, and count one makes it simple. All determinant prefactors
   are nonzero on that disk. No effective rate is inferred from Montel.

9. **The exponential gap is resolved by an exact identity.**
   On a real neighborhood of 12J, a_i>0, b_i>0 and
   d_i'=delta_(i+1)'>0. The exact Schur identities give

       delta_i=d_i-b_i^2/a_i,   Q_i=a_i-b_i^2/d_i.

   At the zero of delta_i, d_i=b_i^2/a_i>0, whereas at its own zero
   d_i=0. The mean-value theorem gives the exact positive gap
   b_i(c_i)^2/[a_i(c_i)d_i'(xi_k)].
   Substitution of separately proved relative limits gives DL4, even
   though the scale is exponential. No subtraction of two inaccurate
   coarse root locations is involved. The c-residue is -b_i^2/d_i';
   dc/ds=-k yields the positive residue in DL3.

The primary formulas were checked at
[DLMF 10.32.8](https://dlmf.nist.gov/10.32.E8),
[DLMF 10.32.9](https://dlmf.nist.gov/10.32.E9), and
[DLMF 10.39.2](https://dlmf.nist.gov/10.39.E2).
Positive real Bessel arguments and the stated order ranges satisfy their
domains. No PDF or source modification was needed for these checks.

## 3. Finite verification, separate from the analytic verdict

The new producer, tests, manifest and fixture data were inspected.
The frozen parent-to-source diff is exactly five added files.
The replay and independent controls gave:

- 136 tests passed normally in 23.788 seconds and under -O in 25.472 seconds:
  40 new DL tests plus 32 NP, 32 LS and 32 AW tests.
- Both DL producer checks and all four LF-exact report/manifest emissions
  passed. Ruff check, Ruff format check and the full-base whitespace check
  passed. No source assertions disappear under -O.
- A third independent primitive construction used
  Delta=(E4^3-E6^2)/1728, finite binomial expansion of unit-series powers,
  and exact Gauss--Jordan inversion of the Fourier pivot matrix.
  It rebuilt all 24 fixture charts and 48 held-out charts, at dimensions
  7 and 13, all six classes and depths 2,3,4,6, through q^10.
  This is different from both the producer's Euler-product construction
  and the test file's logarithmic-derivative recurrence.
- The closed projection generating function was independently rebuilt
  for all 36 fixture rows. All 28 residue/gap constants were rebuilt
  using sigma_1(h)/h and the derivative F_J'(12J).
- Twenty-eight fresh resealed category, arithmetic, type, source and scope
  attacks were rejected through ACTUAL primitive reconstruction, with
  no build_report mock or cache. These additional transient attacks ran
  in normal Python; the repository's hostile unit tests ran in both modes.
- All fourteen Git blob/LF-SHA source pairs were independently hashed;
  the four local artifact seals, fixture seal and payload seal matched.

These controls certify the stated finite algebra and provenance only.
They do not sample a period, locate an actual finite-weight zero, certify
a transcendental integral, or determine k_0(J,delta).

## 4. Frozen identities and remaining boundary

Scientific Git blobs:

| file | blob |
|---|---|
| proof | fc5a71b861d4f4eb6bac212ec89d272659e56e93 |
| producer | 126d033f3c06c65c97f829d9e0a873871d0b574a |
| fixture | 87fe400b04d190b4bdb20536f66c6e795c59f53e |
| sources | 1b7d9673eb16e33060406c6f9d4835ff045810ed |
| tests | 817d6510b956f28d8df3f3563397400e371b1daa |

Fixture LF SHA256:
378ed6aeb5af4c6adc74d66884dc1ab24f6b1a532cfda40e1de14f27692195cc

Payload SHA256:
a27d96afe2214ed29f64a337f81975400e88f5e50a74f575e1f75de184d6acc1

No mathematical repair was required at the reviewed identity.
The theorem is fixed depth followed by eventual all even weights.
It does not establish a uniform growing-depth ladder, an effective onset,
global interlacing, an unsigned divisor asymptotic, infinitely many poles
at one fixed weight, an Euler product, a critical-line theorem, or RH.
The terminal J=d,k=12d countercontrol correctly lands at the inherited
nonzero endpoint pole and lies outside the fixed-depth eventual hypotheses.
The classical source imports and non-effective convergence remain explicit
analytic dependencies, not debts discharged by a finite fixture.
