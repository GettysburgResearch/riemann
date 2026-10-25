# Internal mathematical review: mark variance and native affine reduction

Date: 2026-10-25. Scope: prepublication algebra, normalization, quantifiers,
and finite-control review. This is an internal agent review, not an external
referee report, a proof-assistant certificate, or certification of the cited
52-page external paper or the repository's complete analytic framework.

## Independence disclosure

Before reviewing `MARK_VARIANCE.md`, I had supplied suggestions for its finite
CRT generating-function formula, support lower bound, and packing caveat.
This review of the variance note therefore has limited author independence.
The native affine reduction and its projected version were new to me when
this review began. I checked them against the pinned repository sources and
constructed a separate finite Eisenstein arithmetic control.

## Exact reviewed bytes

The mathematical files are frozen in `GettysburgResearch/riemann` at commit
`14aba2d9af60f2c2849dfe31bab10f5c6996c8aa`, on branch
`research/hlc-zero-free-transfer-20261025`. All final paths are under
`standalone/2026-10-25-hlc-zero-free-transfer/`.

After publication I fetched `MARK_VARIANCE.md`, `NATIVE_AFFINE_REDUCTION.md`,
and `check_exact_identities.py` directly through the GitHub connector at that
exact commit. Their returned Git blob IDs matched the IDs independently
computed from the reviewed local bytes, and the SHA256 values below were
unchanged. This binds the prior mathematical review to the published commit;
no new mathematical claim or expanded review scope is introduced.

| Published file | Verified Git blob |
| --- | --- |
| `MARK_VARIANCE.md` | `ac7095cb2a8870a241bb8d5093c51023048a3f3e` |
| `NATIVE_AFFINE_REDUCTION.md` | `5a3e1f87b47701982bc4a22e8cc066f8335f7909` |
| `check_exact_identities.py` | `1e0d1fbd9360f96e8e525952a69819ea628569ff` |

| Reviewed artifact | Source originally reviewed | SHA256 |
| --- | --- | --- |
| `MARK_VARIANCE.md` | Same file in `standalone/2026-10-25-hlc-zero-free-transfer/` | `37895c3c69945d8e898d91d54a2cb60b9e77576168e3d64d88dc4dd8203940f0` |
| `NATIVE_AFFINE_REDUCTION.md` | Scratch `repo_connections.md` | `abccb83b1a37d491b4d485cf21297d25f65febe06ea5c3fae91bf415198d33ca` |
| `check_exact_identities.py` | Same file in the packet | `89c45bc8128ba5d6f956ee1724843d0154e548bab97510ec780ed25a687f6bfa` |
| Reviewer arithmetic control | Scratch `review_affine_checks.py` | `2c6445c6635c878d74bdacb1021c0092f89556c468f82a2f57e7590216ae3598` |

I additionally read the following pinned GitHub source files directly:

- PR1014 `standalone/2026-10-22-inverse-length-consumer/PROOF.md` at commit
  `845225c2e7713b69766b95c5e6964d44bb62f6bb`, Git blob
  `50f611b563446d32838721d05d4c693e7b9b310b`.
- PR1020 `fifth-pass/PR1019_COEFFICIENT_TRANSFER_AUDIT.md` under
  `standalone/2026-10-23-structured-moment-gains/` at commit
  `de3403df774ae0eaddfaeb9bae045ea7c9250b69`, Git blob
  `945847ee7d1bc1ba0836f916dfabb01b9ae56a9b`.
- PR1020 `fifth-pass/SEXTIC_ROW_PHASE_CANCELLATION.md` at that same commit,
  Git blob `3a5d7adcc24ec8907be5c8fd6879d81736d44788`, specifically its
  field, primary-generator, zero-mask and normalization conventions.

## Disposition

The reviewed finite identities and fixed-parameter variance deduction are
correct at the stated scope after the four clarifications listed below.
The affine reduction retains the actual coefficient orientation, diagonal,
physical row measure, and common projection. Its lower-bound condition is
sufficient for the pinned conditional inverse-moment consumer. No missing
analytic estimate is proved by these identities or by the finite checks.

### Clarifications raised and now present in the reviewed bytes

1. **Nonempty finite prime bands.** The variance identity divides by `V_i`
   and the mark mean. Each finite band must be nonempty. The hypothesis now
   says this explicitly.
2. **Growing-parameter quantifiers.** A fixed-parameter theorem does not
   justify a prescribed quantitative `b=b(x)`. It does not prohibit a
   sufficiently slow diagonal choice. The note's earlier categorical wording
   was corrected, and the reviewed version makes this distinction.
3. **PR1019 coefficient conjugation.** Its actual vector is
   `x=A_U overline(b)`, not `A_U b`. The affine note now explicitly maps
   `b_n=mu_E(n)nu_0(n)W(Nn/D)/sqrt(Nn)` to positive character orientation,
   `nu=overline(nu_0)`, `V(y)=y^(-1/2)overline(W(y))`, with the same puncture
   and conjugated height phase. The frame/projection remains unchanged.
4. **Invertible Gram range.** The formula
   `P_K=V_frame G^(-1)V_frame^*` now explicitly retains the source's licensed
   label range where `G` is invertible. An arbitrary dependent frame would
   not permit that ordinary inverse.

## Variance calculation

For independent Bernoulli variables with probabilities `1/(p-1)`,
`F_i(z)=E z^(N_i)` is the exact finite probability generating polynomial.
The first mark moment is `F_i'(rho)/V_i`. Since

    F_i'(t)+t F_i''(t) = E[N_i^2 t^(N_i-1)],

the normalized second-moment ratio in (2) is correct. Independence across
disjoint groups gives the variance sum in (3), with the factor `b^(-2)`.
The support Cauchy--Schwarz argument in (4) is valid even if the mark is
supported on a strict subset of the event `N_i>=1` for all i.

The limiting expression

    r(rho)=(rho^2+1/log(2))*exp(log(2)*(rho-1)^2)

is correct. In particular the support event has limiting probability
`2^(-K)`, so its variance cost cannot be replaced by a K-independent
constant. This is a statement about the Cauchy--Schwarz bound, not a lower
bound on the actual signed Möbius correlation.

The transfer from CRT residues to shifted primes uses fixed-dimensional
mixed factorial moments with all selected moduli `x^(o(1))`. At each fixed
moment order, disjoint bands give unique selected-divisor data and bounded
coefficients, so Bombieri--Vinogradov controls the total discrepancy. The
prime measure has total mass tending to one by the prime number theorem.
The independent Poisson limit is moment-determinate. Fixed-rho marks and
squares are bounded; passing their expectations through weak convergence
therefore causes no missing uniform-integrability problem. No uniformity
for growing b or K follows from this argument.

The geometric packing estimate correctly distinguishes disjoint real
intervals from merely disjoint prime sets. The latter case is handled by
harmonic prime mass, where the claim is the asymptotic order `O(log log x)`.

## Native affine and projected identities

Every ideal prime to 3 in the Eisenstein integer ring has one generator
congruent to 1 modulo 3, and products of these chosen generators stay in that
coset. Thus the substitution `n=ap`, `m=ap+h` has the exact restriction
`h in 3O`; no extra unit multiplicity occurs. The coprime prime-only identity
is valid on squarefree support and has zero right side on nonsquarefree
ideals. Removing `(a,p)=1` would invalidate it already at a prime square.

The profile identity is

    mu_E(n)V(Nn/D)
    = -(1/log D) sum_(ap=n,(a,p)=1) mu_E(a)log Np V_D(Na Np/D).

Using it only in the first member of each unequal pair in the expanded norm
gives exactly `I=Delta-T/(D log D)`. The second profile and character must
remain conjugated. The note has that orientation. It follows that the
complete T is real, even though individual affine terms need not be.
A **lower bound** on T is sufficient for an upper bound on I; an absolute
bound is stronger than needed. This sign is correctly stated in (10).

The true diagonal retains `|psi_u(n)|^2`, including the original natural
zeros and fixed punctures. It is `O_V(U)` under the stated physical
row-volume hypothesis. The projected kernel is

    K_Pi(n,m)=sum_u (Pi A(n))_u conjugate((Pi A(m))_u).

This is linear in the first column and gives exactly the displayed norm
expansion. Since the same orthogonal Pi acts on every column,
`0<=K_Pi(n,n)<=||A(n)||^2`; hence the projected diagonal has the same upper
bound. The kernel is generally not multiplicative after projection, and
the note correctly makes no such substitution.

Finally, (10) plus the diagonal estimate reproduces the pinned native
hypothesis (H), including the exponent `D^(4/5)`. The remaining height,
seminorm, conductor, mask and endpoint uniformities are correctly listed as
requirements, rather than supplied by the finite identity. The proposed
`437/500` conclusion remains conditional on (H) and all other pinned
analytic interfaces.

## Checks and their limits

I read the root's exact standard-library checker. Its formal prime-log
representation, rational complex arithmetic, independent affine triple
loop, coprime negative control, and projected kernel convention match the
stated identities. Its character example is explicitly a synthetic
rational-field control; it should not be described as an Eisenstein field
computation.

For additional independent coverage I ran `review_affine_checks.py`:

- Actual primary generators in `Z[omega]`, excluding primes above 6, were
  enumerated through norm 140 and factored by exact ideal divisibility.
- Sextic residue symbols were computed prime-by-prime as the unique unit
  congruent to `u^((Np-1)/6)` modulo the prime ideal, with zero at nonunits.
- The example used seven physical test rows, eighteen norm-annular columns,
  a common complex angular and height twist, a complex smooth profile, and
  a noncoordinate complex two-column Gram projection.
- The full affine identity agreed with the directly computed norm within
  `2e-17`; the projected identity agreed within `3e-16`. Their complete
  affine sums were real within `7e-15` floating-point error.
- Reversing the kernel orientation changed the projected norm by about
  `0.00548`, so the control is sensitive to conjugation errors.

The ideal and residue-symbol computations use exact integers. Norms,
angular/height phases, smooth profiles, and projection calculations use
floating-point complex arithmetic; this reviewer control is therefore not
an exact certificate. It confirms the finite normalization and orientation
in an arithmetic example. It neither tests a large-scale moment estimate
nor supplies the missing affine correlation bound.

## Remaining mathematical burden

The complete signed affine estimate (10), or the corresponding exact
complement-kernel estimate, is still open. The supplied fixed-shift HLC
paper does not provide its variable affine coefficients, lattice shift
family, polynomial conductors, or fixed power saving. The present packet
makes those requirements precise and quantifies the original unmarking
cost. It must not be presented as a new zero-free region or an RH proof.
