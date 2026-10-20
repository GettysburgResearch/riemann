# Exact-head packaging, scalar, and uniform-consequence review

20 October 2026. Reviewer: the global-route research agent.

**Reviewed commit:** `9bf9e21f95669abdcaa74e3b2ba54fb93e779503`.
This review binds that commit, not a subsequent working tree or commit.
The packet's `MANIFEST.json` has SHA256
`45db98ab4dbc9689f58314c110e9ea6aad28d83cfb3312314caf1ae3b2665e08`.
The committed `REPLAY_RESULTS.json` has SHA256
`818f56dc7ec583eecd198a0f06ee89bd9e413933a793d6fa2c848eb035bef37d`.

**Verdict:** no outstanding defect found within the review scope below.
The proposed analytic results retain their explicitly named upstream
inputs. This is not a certification of the entire upstream analytic
argument, an improved numerical zero-free boundary, or a proof of RH.

## 1. Authorship and independence

I authored or co-developed the files under `global/`, including the
spherical residue, inverse interface, auxiliary guard, unitary assembly,
and guarded spherical mean. My consistency check of those objects is a
**coauthor check**, not independent validation. The separate type-I and
boundary agents' auxiliary-guard reviews remain the independent component
reviews recorded by the packet. I did not reclassify those reviews as an
independent certification of the complete all-field theorem.

The packaging review, master replay, scalar-certificate review, and the
uniform analytic consequences below are independent of their authors.
I did not reprove every imported large-sieve, theta, or canonical
induction theorem during this exact-head review.

## 2. Isolated archive and reproducibility

I created a fresh `git archive` of the named commit's packet and extracted
it outside the working checkout. The ZIP commit comment is exactly the
reviewed 40-character commit ID. The archive contains **74 files**.

Running `python -I -S -B replay.py` in that isolated archive passed:

- all **64** frozen source-file hashes;
- all **eight** exact checkers in ordinary and optimized Python mode;
- every ordinary/optimized canonical-JSON equality;
- the aggregate result and its stated finite-check scope.

I then compared every extracted file with its original ZIP member. All
**74 files remained byte-for-byte identical**, including every regenerated
receipt and the aggregate report. Thus this replay reproduces the
committed output without silently updating it. The working packet was
not used as a destination for generated receipts.

The ten files excluded from source hashing are the manifest itself and
nine generated JSON artifacts; they remain bound by the reviewed Git
commit. The numerical centered-canonical artifact is clearly exploratory
and excluded from acceptance. No source acceptance file is silently
omitted. I also resolved all **71 local Markdown links** against the
reviewed commit's complete Git tree; none was missing.

The master replay rejects Python `assert` nodes in acceptance scripts.
It validates paths within the packet and compares explicit pass receipts.
This authenticates finite algebra and recorded coverage, not analytic
continuation or an infinite family theorem.

## 3. Claim-scope consistency

I read the exact-head `README.md`, `CLAIMS.md`, `VALIDATION.md`, manifest,
assembly review, and the main global theorem statements. They consistently
state the following distinctions:

- the cubic bilinear improvement has a free smooth variable and a fixed
  angular profile; it is not an arbitrary selected-prime polynomial;
- the all-unitary claim extends the covered family at the inherited
  `B_flat`, without decreasing its numerical value;
- the new all-field interfaces are proposed source-dependent arguments;
- the initial `11/12` base, the subsequent `7/8` step, and the refined
  closing scalar comparison have separate dependencies;
- fixed-prime exploratory guards are not inputs to the reviewed cubic
  guard or to the full-family assembly;
- full RH and the missing moving-conductor/centered estimates are not
  claimed.

The angular-profile and moving-quadratic restrictions in the claim table
are material and correctly retained. The exact descent dichotomy is
finite order times a common norm character versus its complement; it
does not erroneously treat a removable real sign parity as a persistent
nonzero angular type.

## 4. Independent scalar-certificate review

Reviewed files:

| File | SHA256 |
|---|---|
| `scalar/TANGENT_CERTIFICATE.md` | `70ce8146419c289f5643566001ab46c16aa1fc3e7c8aede2393f7c455108de64` |
| `scalar/verify_tangent.py` | `74d4fe6d3d0fd6727a4f352d3fd1cfc629ca97f8c842c724a3caa1d0b81cad89` |

I checked the primitive formulas directly against Liu 2610.26835v1
equations (14.3), (14.8), and (14.10). The local HTML's SHA256 is
`5b128f3cedb4d6ecfe3a3d57b1290cb576cac03092cf0b807c6f8092abf864c6`,
matching the certificate's source pin.

I independently checked the scaling from `D,P,J,R` to the polynomial
numerators, including the coefficients of `b` and `ell`; the critical
root condition makes the `b` numerator vanish. The formula for `b*`
then imposes the delta derivative condition, while `ell*` imposes the
value condition. These exact relations supply the double root; an
interval merely containing zero would not do so.

The completed-square argument is valid over the continuous rectangle.
The constant discriminant coefficient is zero by that exact double root;
strict positivity of every remaining coefficient gives positivity for
every positive `y=1/2-x`. At `y=0`, the unique zero is the critical
delta. The denominator `J` is positive on the source rectangle. The
64 adjacent rational kappa intervals are a cover, not a sample.

I checked the strictification derivative
`E_ell >= 5/4 - 9 delta/8 >= 5/16`: lowering `ell` creates a uniform
strict margin. The self-consistency gap stays positive above the unique
endpoint root if that decrease is small enough. The resultant and its
nonvanishing prefactors identify the correct quartic branch; the
separate sign bracket and monotonicity checks prevent selection of an
irrelevant resultant root. The three small-row inequalities correspond
to the actual source (14.10).

The certificate's stated limitation is correct: it verifies this narrow
closing scalar family, not the earlier analytic improvement to `7/8` or
the analytic estimates entering the scalar formulas.

## 5. Independent uniform-consequence review

Reviewed files:

| File | SHA256 |
|---|---|
| `uniform/UNIFORM_INVERSE_AND_STRIPPING.md` | `fcee7547018c62c5a54c273501b7f2032a93b3633b5b04b3cdce90fdc1015c12` |
| `uniform/FULL_FAMILY_CONSEQUENCES.md` | `4d2c4476e3235cb9e1bfa3557134b8ec2eed71dc18004eed0ed67e2f6369a159` |

The common zero-free family premise is explicitly separated from the
uniformity argument. Uniform Euler-product bounds, the Hecke functional
equation, and conductor-comparable fixed disks give the needed polynomial
growth. Pole removal for a norm twist uses the stated rational factor;
its artificial pole lies outside the positive strips used. The logarithm
argument, Borel--Caratheodory, and three circles yield a sublinear power
of `log C`, and hence any prescribed positive conductor power for the
reciprocal. Cauchy then gives its derivatives.

The sharp Perron use is compatible with the ideal-coefficient divisor
bound and the half-integer cutoff. In the prime-ideal consequence the
height grows with the conductor and includes a translated principal pole.
The logarithmic derivative's pole sign and extra rational term are
correct. Removing higher prime powers is uniform in angular degree.

The signed dilation proof retains the derivative of the profile and its
small-argument hypothesis. Its exact threshold is `(3+beta)/6`; it is
correctly described as a threshold for this operator, not as a smaller
zero-free boundary for the original target.

For Eisenstein sectors, every integer harmonic is an actual Hecke
character with bounded finite conductor and quadratic archimedean
conductor growth. The trigonometric approximation uses nonnegative prime
weights and includes all first harmonics. Choosing the internal epsilon
before the Fourier cutoff gives the claimed uniform arc error and the
stated shrinking-arc asymptotic. These remain conditional consequences
of the proposed full-family premise.

No edit to any frozen proof, checker, manifest, or receipt was needed
for this review.
