# Exact-commit nonauthor review: Bessel channels and damping calibration

**Verdict: PASS within the scope below. No substantive release blocker found.**

This is an independent automated-agent review of specified files at GettysburgResearch/riemann commit **`c07b9f653b8d0eb82d9f056d935a4ecef6770f56`**, packet `standalone/2026-10-12-parity-and-cubic-fibers/`. It is not human peer review, integration into main, or certification of the generalized moment hypothesis.

## 1. Exact source and review scope

The five files below were fetched from GitHub at the displayed immutable commit. I recomputed both SHA-256 and the Git blob identity `SHA1("blob " + decimal_byte_length + NUL + bytes)`. Every recomputed blob matched the value returned by the GitHub connector. The three supplied proof/document SHA-256 identities also matched exactly.

| Published relative path | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `BESSEL_CHANNELS_AND_LEAKAGE.md` | 38165 | `c97e7c1befc3c1099de6a0b30a03c81ecb08b1acfe3ff42467c0b58901498579` | `a8aaee5cb912d74da6f96bdae10a3f96488fe88f` |
| `CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md` | 25697 | `026d1a3d6f458b872128fa77fbe683a35cc38a799e822d29760dbc566c2bd91e` | `f8824c18f1ba54f0ab863f2a4b0fc92a55bc01e9` |
| `README.md` | 13477 | `54fc1389b5fb2b4bc625dc2c4a364af67fc02211bb22a7e07786d4164ee5718b` | `b0521476c95d4cfa30561489530dff2fa02bc03a` |
| `checks/verify_bessel_channels.py` | 21881 | `416f54154aa9b02261a0c07fbfba5fc9d84e414ab195d87c2944f22ce1c88da6` | `049e24f19146bd5d2b2f381f117f09644d1619af` |
| `results/bessel_channels.json` | 4639 | `db88a9ab641e11c13686f4aac00339906ce23e2965a36ee4e99e7a6abd9cd943` | `3c7f09eadc76f5dca162ea0855831072f40c1ba1` |

Canonical sources: [Bessel proof](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/BESSEL_CHANNELS_AND_LEAKAGE.md), [cubic-fiber note](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md), [README](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/README.md), [Bessel checker](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/checks/verify_bessel_channels.py), and [committed result](https://github.com/GettysburgResearch/riemann/blob/c07b9f653b8d0eb82d9f056d935a4ecef6770f56/standalone/2026-10-12-parity-and-cubic-fibers/results/bessel_channels.json).

The mathematical review covers **the entire Bessel note and checker**, **Sections 6–7 of the cubic-fiber note**, and **README consistency and scope**. For the calibration review I also read the cubic-fiber definitions in Section 1 and the prime-count lemma in Section 4.1. Its remaining probability-comparison theorems and its own checker are outside this review's scope. This is not a nonauthor review of `PARITY_DAMPED_MOMENTS.md`, whose author is the present reviewer.

The fetched Bessel proof, cubic-fiber proof, checker, and committed result are byte-identical to the corresponding local files used during the preliminary reading. This final verdict is bound to the fetched committed identities above, rather than to a branch name or an unverified local draft. No mathematical source was edited during the review.

## 2. Full Bessel proof review

### Primitive normalization and exceptional channels

I reconstructed `T=F_+ R F_-` from the stated finite Bessel kernel. Additive orthogonality makes the Fourier maps unitary; inversion with the cubic weight makes `R` Hermitian, and `R^2` deletes exactly the zero coordinate. Its Fourier conjugate consequently satisfies

\[
T^*=T,\qquad T^2=I-P_0.
\]

The two inversion fixed points give trace two. Together with rank `q-1`, this gives the stated multiplicities `(q+1)/2`, `(q-3)/2`, and one zero eigenvalue.

The exceptional channels are essential and are correctly retained. The exponent-zero input is the unit indicator `u`, not the constant function one. The exponent-four image is the Ramanujan vector `r`, including its nonzero value at the zero residue. Direct calculation gives

\[
T\chi^4=\gamma_4 r,\quad
Tu=-q^{-1/2}\gamma_2\chi^4,\quad
Tr=\gamma_2\chi^4,\quad T1=0.
\]

I checked the declared local adapter against the exact imported `paper2.tex` formulas `eq:theta-local-factors`, `eq:ray-local-transform`, and `eq:theta-weight`. The materialized source has SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d` and Git blob `2000faddbbebac5de0ecfe0b962534ea61a852d5`, independently recomputed here. In particular, the source's `q^(-1/2)` in the active zero channel is already in `B_(p,0)`; the unit factor displayed in the note does not remove it. Inactive primes remain separate density/conductor branches. This review of the finite normalization does not endorse the imported source's zero-free claims.

### Native compression and exact leakage

The Gauss product formulas imply

\[
T\chi=a\chi^3,\qquad T\chi^3=\overline a\chi,
\qquad T\chi^5=\chi^5,
\quad a=\gamma_1/\gamma_3.
\]

Orthogonality therefore gives the rank-one native compression and its mixed-sign zero. The tensor identities hold at each fixed common squarefree conductor. The note correctly distinguishes fully singleton higher-order incidences from arbitrary higher-order odd incidences, where exponent three is possible. Its example with an even positive-side prime and two negative singleton primes also correctly prevents side balance alone from being used as a mixed-odd-sign hypothesis.

Inserting the complementary projection between the two reflections gives the exact return identity. On the mixed native subspace the return has coefficient one. Thus zero compression does not imply a small norm for the reflected vector. For the source map with an output dilation and a unit scalar, the stable statement correctly uses `U* (I-P) U`, rather than assuming `U^2=I` for an arbitrary dilation.

### Simultaneous S3 action and three-color ambient

The Gauss-gauged basis makes the two operators exactly the transpositions `(1 3)` and `(1 5)`. Their tensor products generate the **diagonal, simultaneous S3 action**. No prime-selective independent `S3` actions are inferred from it.

A mixed word has trivial stabilizer, hence a six-state orthogonal orbit with precisely two native words. I reconstructed the trivial and alternating projection matrices and their sum `I/3` on each native pair. The alternating component appears in the mixed orbit even though it is absent in the one-prime three-dimensional representation; the note explicitly makes that distinction.

The symmetric walk has eigenvalues `1,-1,1/2,-1/2` on the relevant representation types, so the exact norm formula

\[
\|W^n f\|^2=(1/3+(2/3)4^{-n})\|f\|^2
\]

follows from the one-third cyclic-invariant energy. The counterterm minimization is also valid: the ambient for `g` is the invariant three-color space `O_r`; projecting onto the three orthogonal color sectors leaves a constraint `h_1+h_2=-f`. It requires squared norm at least `||f||^2/2`, attained by the two displayed counterterms. Nothing in this proof supplies those counterterms from the arithmetic coefficients.

### Mellin norm and physical covariance boundary

The growing-conductor spectrum and the direct-sum noncompactness statement are valid for their stated normalized operator. The Mellin gamma ratio has modulus one on the imaginary axis and cancels with its reflected ratio; Mellin-Plancherel gives the claimed unitary involution in `L^2(dx/x)`. Neither operation supplies a physical contraction by itself.

The note keeps the physical variables separate. A tuple polynomial is sampled by a linear row functional; its Bessel self-pairing is quadratic in tuple coefficients. Ordinary row Fourier sends `j` to `-j`, whereas the column Bessel action sends it to `-j-2`. A physical sampling weight transforms as well. The note retains the conductor-dependent dilations, Gauss ratios, finite-ray scalars, active/inactive branches, cusp coefficients, and physical scale changes. It does not identify these separate structures through reciprocity alone.

The exact mismatch is valid. The four prime ideals are distinct, their two product ideals have equal norm `91` and are not associates, and their Hermitian tuple polynomial belongs to the mixed native class. Its sum is `12` on the six unit rows and `30` on the entire nonzero height-13 ball of `54` rows. The shell table retains the zeros at norms 7 and 13. With `D=H=13`, one fixed smooth test supported in `(1/2,2)` can take value one at both required norm ratios. This is a genuine native tuple-pair example; it is expressly not the whole fourth moment or an asymptotic counterexample.

Finally, the optimistic quadratic comparison is arithmetically consistent. Even if its unproved coefficient/scale adapter were granted, the Cauchy closure would return the bound `HD^k+sqrt(H)D^(k(1+b))`. Its second term has relative cost `D^(kb)/sqrt(H)`. At `k=2,b=7/8,H=D`, the stated exponent is `17/4`, compared with target `3`. The note correctly treats the adapter and the required improved signed covariance as unproved.

## 3. Calibration review of the cubic-fiber note, Sections 6–7

The positive and negative sign conventions in the companion notes define the same damped functional. For the calibration, the test is fixed in `C_c^infinity((1,2))`, which is stronger than arbitrary annular support and is used legitimately in the noise-floor proof.

For a prime `p` with `D<Np<2D`, every proper multiple lies outside that support. Its centered-chaos coefficient is therefore exactly the displayed prime term. Orthogonality of distinct centered prime sets then gives the variance lower bound. A row of norm at most `D^h` has at most `h` prime-ideal divisors of norm greater than `D`; this bounds the deleted prime mass uniformly over all rows. The prime singularity/Mellin argument in Section 4.1 supplies the needed subsequence, and Jensen plus the full lattice row count yields

\[
\lambda_{k,h}(t)\ge h+k\qquad(t>0).
\]

The qualification `t>0` is necessary and is preserved. The argument supplies no positive-noise floor at `t=0`.

The test shift in the Jensen adapter is also correct:

\[
F_{k,t}(D,H)\ge D^{-2kt}M_{2k}(D,H;W_t),
\quad W_t(y)=y^{-t}W(y),
\quad \widehat W_t(z)=\widehat W(z-t).
\]

I re-fetched the pinned sampling source at commit `086bf0560c0c2679a1fe41418f583d2c5ca743c3`: `SAMPLED_MOMENT_CRITERION.md`, SHA-256 `18bf2fdad438eb21ae3318eba7d42e9c03803b2dd1abc4d8f6448fb3b04499de`, Git blob `ccb083b8bfd2e3c015c9a8aad5b27ba2754243a4`. Its detector and exact sixth-replica/causal-inverse argument give the stated shifted strict boundary

\[
1/2+t+5h/(12k)+e/(2k).
\]

For the lower-growth formulation, an actual fixed zero with real part `beta>t` is detected by `W_hat(z-t)`. Assuming a smaller limsup exponent makes the replica mean integrable on a positive weighted scale line strictly to the left of that zero. The cited causal inverse applies on that line; the finite Euler correction and shifted detector are nonzero at the zero. This proves the asserted contradiction without simultaneous record scales across different orders.

The upper bound is kept logically separate. Its `PW_B` is uniform in the physical row, with explicit conductor and scale losses. The finite-exclusion adapter and the centered-sign upper proof use that premise. The note does not identify a supremum of zero real parts with this uniform pointwise input. Its cofinal lower and upper frontiers have the stated conditional scopes; recovering only the original boundary at `t=B-1/2` is the correct calibration. Section 7 continues to leave damping removal and the incomplete-row arithmetic comparison open.

## 4. Committed checker review and actual replay

The full checker source was read. It constructs primitive residue characters, rather than starting only from the claimed channel permutation. Its cyclotomic quotient-ring arithmetic implements the Bessel kernel directly; the inert norm-25 case uses the correct Eisenstein finite-field multiplication and trace. The matrix checks include every zero row/column, the active zero channel, the exponent-four Ramanujan channel, and the Gauss-gauged permutations.

The following commands were actually executed with Python **3.12.14**, from the fetched exact-commit packet directory. The outputs are separate review artifacts, so the committed result was not overwritten.

```sh
python checks/verify_bessel_channels.py --note BESSEL_CHANNELS_AND_LEAKAGE.md --output /workspace/scratch/5b23d9b20a3a/attack4_moment_bessel_normal.json
python -O checks/verify_bessel_channels.py --note BESSEL_CHANNELS_AND_LEAKAGE.md --output /workspace/scratch/5b23d9b20a3a/attack4_moment_bessel_optimized.json
```

Both runs returned **PASS, 11,562 explicit predicates**. A subsequent byte comparison established

```text
ordinary replay == optimized replay == committed results/bessel_channels.json
SHA256 = db88a9ab641e11c13686f4aac00339906ce23e2965a36ee4e99e7a6abd9cd943
```

AST inspection found **zero Python `assert` nodes**. The result's proof and checker hash fields match the authenticated bytes in Section 1. Thus optimization does not bypass the tested predicates, and the replay is attached to the intended committed source.

The finite coverage matches the note: five prime-ideal cases (the two above 7, the two above 13, and the inert norm-25 prime), `1061` ordered matrix positions, `510` native words at one through eight prime positions, `247` mixed complement pairs, walk powers zero through eight, the sharp counterterms, and both native row examples. The rational comparison check gives exponent `17/4` and loss `5/4` in the displayed example. No broader numerical sweep was performed.

The replay verifies these bounded finite diagnostics. It does not test the infinite Mellin theorem, an arithmetic covariance adapter, an imported pointwise or zero-free assertion, a new uniform large-sieve estimate, or the full generalized moment.

## 5. README consistency and final limits

The README accurately distinguishes the proved damped hierarchy from the open undamped hierarchy, retains the same-height/all-shorter-scale premise for the second-moment refinement, labels `b=7/8` conditional, and preserves the distinction between the Walsh baseline and the complete-residue principal projection. Its prime-face warning is restricted to the selected face. Its finite Bessel discussion does not turn zero compression into a physical contraction. Its proposed next estimate at `t=b-1/2-eta` has the correct conditional extraction to `b-eta`, with cofinal sublinear height and remaining excess and the source's detector/twist coverage still required.

Accordingly, the named claims pass this review at their declared scope. The missing signed arithmetic comparison remains a mathematical task. This receipt does not certify RH, prove an undamped generalized moment, independently certify the numerical pointwise exponent, or replace the separate reviews of other packet components.
