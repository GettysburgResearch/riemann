# Checks: how to rerun the Oct 5 (11/12) review scripts, and what they do and do not authenticate

```text
Status: PROPOSED (part of an integration packet draft). These are review instruments: finite,
  small-scale checks written by the bounded agent reviewers. They are not proof-producing
  computations and not certificates.
Scope: the four scripts behind R1, R2, R3 and the residual note, plus their shared module a2/eis.py
Exact sources or dependencies: scripts at commit c2050a5dd8c251f25e5fc285c0845b9f4a42487b
  (byte-identical at d47a04076f34152bd9d0276a9eaa3f43804120f9), hashes below; manuscript paper2.tex
  SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d (the scripts do not read it)
What was actually run: all four scripts, on 2026-10-10, in the environment below; results in §2
Smallest remaining gap: none of these checks replays an analytic estimate. The load-bearing
  verification is the hand reading recorded in the reviews.
```

RH remains unsolved. Passing these checks says nothing about RH. It also does not establish the
11/12 theorem. The scripts test conventions, exact identities and exponent bookkeeping at tiny
scales.

## 0. Environment and conventions

**Environment used for the rerun.** Python 3.13.16, numpy 2.5.3, scipy 1.18.1, sympy 1.14.0 and
mpmath 1.3.0, on Linux with 4 cores. The machine was shared and heavily loaded (load average about
10), and the four scripts ran in parallel, so wall times were 2-5 times those the reviews record.
The reviews used the same library versions.

**How to run.**

* Use `python3 -I -B`.
  * `-I` (isolated mode) keeps the current directory and `PYTHON*` variables off the import path.
  * `-B` stops `.pyc` files from being written into the repository; `__pycache__/` is gitignored,
    but this avoids touching the tree at all.
* R1 and R3 add `../a2` to `sys.path` themselves, to import `eis.py`.
* Write every JSON output **outside the repository**, for example in a scratch directory.

**Arithmetic classes.** These use the vocabulary of [CONTRIBUTING.md](../../../../../CONTRIBUTING.md#computational-artifacts).

* `EXACT_RATIONAL`: Fractions, sympy rationals, or integer arithmetic in `Z[ω]`.
* `FLOATING_RECONNAISSANCE`: ordinary double precision. It is neither directed nor certified.
* `NON_DIRECTED_HIGH_PRECISION`: mpmath at 30 digits.
* No check here is `DIRECTED_INTERVAL` or `CERTIFIED_INTEGER_COVERAGE`.

**Verify the scripts before running.** From `research/exploratory/qrh-2026-10/`:

```sh
sha256sum -c <<'EOF'
4fc6c5d72aa5533a88c205b7ba8b39783212fed14e83a51e3c1b3c34afc9cd54  reviews/oct5_r1_checks.py
e4017ed5c78c5d067c379e90122105b465e7015764099e19d877e50bb9da4bdd  reviews/oct5_r2_iteration_check.py
504d84f340b31fd5866c548530d713c25227183c73df21d7f3d0e78669c3b16e  reviews/oct5_r3_theta_checks.py
d175c9736a75c581b0ee314ce013d932ed7c85e9723302b16959cff5acbec9b5  reviews/oct5_residual_checks.py
87ca11d98bf3ee130a6dab613b5f7efe444058320b7c22b005327686f2798e65  a2/eis.py
EOF
```

All five lines printed `OK` for this draft. Each script hash equals the hash recorded inside its
review file.

**Re-extract and hash the manuscript** (the scripts do not read it; this binds the line numbers):

```sh
git show pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex | sha256sum
# expect d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d, 3988 lines
```

## 1. The scripts

### 1.1 `reviews/oct5_r1_checks.py` (R1: reduction, arithmetic identities, Poisson)

| Field | Value |
|---|---|
| SHA-256 / git blob / size | `4fc6c5d72aa5533a88c205b7ba8b39783212fed14e83a51e3c1b3c34afc9cd54` / `2e92cbcc` / 370 lines |
| Dependencies | `a2/eis.py` (exact sextic symbols and Gauss sums), numpy |
| Command | `python3 -I -B reviews/oct5_r1_checks.py --out /scratch/r1.json`. `--quick` uses smaller ranges and two C6 cases |
| Wall time | review: 114 s; this rerun: 287 s (loaded machine) |
| Arithmetic class | MIXED. C1 is `EXACT_RATIONAL`. C5 is exact integer. C2, C3, C4 and C6 are `FLOATING_RECONNAISSANCE`, with residue symbols computed exactly |
| Pass rule | prints `ALL CHECKS PASSED` and exits 0 |

**Expected output.** Each value below was reproduced exactly in this rerun.

```text
fast symbol tables vs eis.sym_prime: 0 mismatches in 4000 random trials
C1 exponent arithmetic: OK {'1/10': {'A1_exponent': '23/24', ...}, '1/20': {...'15/16'...}, '1/1000': {...'2201/2400'...}}
C2 eq:convert2 on 337 composite squarefree n (N<= 2500, {2: 312, 3: 25}): max err 6.55e-15
C3 eq:initial-paired-gauss on 1242 ordered coprime pairs (414 with a composite member): nu_trivial 6.9e-15, nu_order3 6.9e-15
C4 lem:poisson: 8 cases, errors between 6.3e-16 and 2.94e-14
C5 change of variables (Z model): 278519 distinct images, inverse legal on 15900 targets
C6 replay D=30 H=6  nu=None   M_D=0.7574802363 Z=0.5009765555 err=5.55e-16
C6 replay D=30 H=6  nu=order3 M_D=0.7521794556 Z=0.5009765555 err=1.11e-15
C6 replay D=30 H=40 nu=order3 M_D=4.3228220185 Z=3.3398437033 err=1.78e-14
C6 replay D=45 H=4  nu=None   M_D=0.5956489153 Z=0.4326239083 err=5.56e-16
C6 replay D=60 H=9  nu=order3 M_D=0.8157936237 Z=0.9216711908 err=3.13e-15
ALL CHECKS PASSED
```

**JSON record.** SHA-256 `59160e442b881d68ad1785fddfb4b04bffe671de9e70ac98c4e9ebdf0c52f44d`. This
equals the hash recorded by R1 (`59160e44…f44d`), so the run is byte-reproducible. Standard output
contains the output path, so its hash is not stable.

**What it authenticates.**

* The exponent arithmetic of eq:prime-extract, in exact rationals.
* eq:convert2 for every composite squarefree `n` with `N(n) ≤ 2500`, by direct summation without CRT.
* The paired identity eq:initial-paired-gauss on 1242 coprime pairs, for `ν` trivial and `ν` of
  order 3.
* Lemma lem:poisson in eight cases, including composite moduli and exclusions that meet the modulus.
* The bijection `(g,e,v,h) ↔ (b,f,k)`, in a `Z`-model.
* **C6, the strongest check:** the exact identity `M_D = Z + Σ_ξ c_ξ S_ξ` from the `u`-sum to the
  final (eq:initial-column-output) form, at five tiny `(D, H)` pairs.

**What it does not authenticate.**

* No analytic estimate: not eq:ms, not eq:auxiliary-target, and nothing at large `D`.
* C6 uses a Gaussian `Φ`, whose `Φ̂` is not compactly supported. The identity is exact for any
  Schwartz `Φ`, but the support step (paper2 1168-1202) was checked by hand only.
* C3 evaluates `G` through the mod-4 closed form of App. A. So it tests consistency with Hecke's
  quadratic Gauss-sum reciprocity (I8); it does not prove that reciprocity.
* The symbols come from `a2/eis.py`, which R3 also uses. R1 and R3 therefore share one
  symbol implementation, although R1's fast tables are cross-checked against `eis.sym_prime`.

### 1.2 `reviews/oct5_r2_iteration_check.py` (R2: descent and transfer)

| Field | Value |
|---|---|
| SHA-256 / git blob / size | `e4017ed5c78c5d067c379e90122105b465e7015764099e19d877e50bb9da4bdd` / `1b7c60f8` / 548 lines |
| Dependencies | sympy (1.14); its own sextic-symbol implementation over `Z[ω]` for part E (it does **not** import `eis.py`) |
| Command | `python3 -I -B reviews/oct5_r2_iteration_check.py`. It writes no files |
| Wall time | review: about 10 s; this rerun: 114 s (loaded machine) |
| Arithmetic class | MIXED. Parts A-D and F are `EXACT_RATIONAL` (Fractions, sympy). Part E is `FLOATING_RECONNAISSANCE`, tolerance `1e-9` |
| Pass rule | 53 lines starting `PASS`, none starting `FAIL`, and a final line `53/53 checks pass`; exit 0 |

**Expected output.** Standard output is deterministic: 55 lines, SHA-256
`620f4224d42698f0c95ab70a4970ae6bc285572ca73abcbf6ea2e9fa1913df17`, identical across two runs for this
draft. The key lines are:

```text
PASS [A] A_1(D) << D^(11/12+5th/12+eps)  -- 5*vartheta/12 + 11/12
PASS [C] Farkas: h - 2kappa - h' == s1 + s2 + 2 s3 (so H' < D^(-2kappa) H; line 1566-1572)
PASS [C] grid exploration (kappa=1/20, C0=2, step 1/20, 22960 start states, all f' splits): ... max recursion depth 13 <= ... 20
PASS [D] sum over (C,d,e,w) of mu(e)mu(w) == 1_{f'|k'} for all squarefree f' with <=6 primes ...  -- 127 patterns
PASS [E] first paired identity (CRT + convert1/2 + recip) on 161 coprime pairs  -- max err 2.11e-14
PASS [E] second paired identity (CRT + convert1/2 + recip) on 161 coprime pairs  -- max err 2.09e-14
PASS [F] at theta = 1/10, j_max = 40: derivative order >= 5*4^40 - 4  -- 6.045e+24
53/53 checks pass
```

**What it authenticates.**

* The 11/12 bookkeeping, in exact rationals (A).
* The 17 weight, argument and scale identities of the two Poisson steps, as exact monomial
  identities (B).
* An exact Farkas identity that proves the descent contraction and the preservation of the gap for
  **all** real states (C).
* The preimage sign sum `Σμ(e)μ(w) = 1_{f'|k'}` and the factor `τ(r)`, exhaustively over all
  divisibility patterns with up to 6 primes (D).
* The derivative-order, `ε` and interval recursions (F).

**What it does not authenticate.**

* Prop. prop:R, which was a black box for R2.
* Lemma lem:arithmetic as a theorem. Part E is EMPIRICAL: it tests conventions and the CRT step
  on 161 pairs with norms at most 43 per factor.
* The grid exploration in C is an illustration. The Farkas identity is the proof.
* The analytic content of lem:smooth-mean-square, which was checked by hand.

### 1.3 `reviews/oct5_r3_theta_checks.py` (R3: cubic theta reflection)

| Field | Value |
|---|---|
| SHA-256 / git blob / size | `504d84f340b31fd5866c548530d713c25227183c73df21d7f3d0e78669c3b16e` / `2d610471` / 824 lines |
| Dependencies | `a2/eis.py`, numpy, scipy (`kv`), mpmath |
| Command | `python3 -I -B reviews/oct5_r3_theta_checks.py /scratch/r3.json 22000`. Both arguments are positional; the second is the series truncation `Nmax`, default 22000 |
| Wall time | review: 31 s; this rerun: 163 s (loaded machine) |
| Arithmetic class | MIXED. D is `EXACT_RATIONAL` (symbols as integer exponents). H is `NON_DIRECTED_HIGH_PRECISION` (mpmath, 30 digits). All others are `FLOATING_RECONNAISSANCE` |
| Pass rule | there is no single PASS line; compare each group with the table below (from R3 "Reproduction"). The script exits 0 and prints `done <seconds>` |

**Expected output.** Every row was reproduced in this rerun, to the printed precision.

| Group | What | Expected | This rerun |
|---|---|---|---|
| gauss | prime Gauss sums vs direct; composite by twisted multiplicativity; `g̃(p)³ = −p/\|p\|` | `≤ 1.6e-14`; `8.1e-14` (65 composites); `1.2e-14` | `1.64e-14`; `8.11e-14` (65); `1.20e-14` |
| G | eq:intro-theta-coefficients | 434 cases, `2.7e-15` | 434, `2.73e-15` |
| H | Bessel–Mellin; assembled scalar `−i/81` and scale | `4e-31`; `1e-16` | `4.1e-31`; `1.05e-16` |
| C | eq:ray-fourier; eq:ray-local-transform for `j = 0..5`; `γ₂³ = −α`; `γ₄ = γ̄₂` (14 primes) | `5e-16`; `2.0e-14`; `4e-15`; `1.2e-15` | `5.0e-16`; `1.96e-14`; `4.0e-15`; `1.2e-15` |
| D | eq:ray-multiplier vs `(c₁/a₁)_3` | 700/700 EXACT (cases 85/261/354) | 700/700 (85/261/354); 255 also agree with the conjugate formula, so 445 discriminate |
| A | `E`-, `T`- and `3ω`-invariance; `Tω` not invariant (control); `Γ₁(3)` multiplier on 12 elements | `1e-17`, `0`, `4e-16`; `1.7e-13`, conjugate fails by `1.73` | `1.1e-17`, `0`, `3.6e-16`; control `0.449`; `1.68e-13`, conjugate `1.732` |
| B | cusp expansions at `γ₁₀`, `γ₁₉` | `≤ 5.3e-15`; swapped labels `≥ 0.049` | `≤ 5.28e-15`; swapped `≥ 0.0488` |
| F | `H → γ_σ` reduction | 22 cases, `9e-15` | 22, `9.06e-15` |
| E | translate identity, all three denominator cases | 44 cases, `1.1e-8`; conjugate `κ` fails by `1.73` | 44, `1.10e-8`; conjugate `1.732` (31 nontrivial `κ`) |

**JSON record.** The file stores wall-clock fields (`seconds`, `series.build_seconds`), so its raw
hash changes between runs.

* R3 recorded `2760e3dd…4ec98f`; this rerun gave `c2a0166ce7d01c0b7738e0542cb8d3c0626c3041463c5d814a4dc8e690daa7a6`.
* For future comparison, a timing-stripped canonical hash was also computed: remove those two keys,
  then apply `json.dumps(d, sort_keys=True)` and SHA-256. It is
  `772eca48d15226a7433582d21ca87deaeb74abf7b6770f9a7915b1c817db3f0c`. No earlier run recorded this
  canonical hash, so it cannot yet be compared.

**What it authenticates.**

* Dunn–Radziwiłł's transcription of the cubic theta function, truncated at `Nmax = 22000`, is
  automorphic under the finitely many tested elements.
* The multiplier convention `θ(gw) = (c/a)_3 θ(w)` is the one under which it is automorphic. The
  conjugate convention fails by `√3`, and this is the sign that makes `B_{p,1}` quadratic.
* The cusp expansions at `γ₁₀` and `γ₁₉`.
* The local transforms `B_{p,j}` for `j = 0..5` on 14 primes.
* The three-case multiplier formula, exactly, on 700 instances.
* The assembled translate identity, on 44 translates.
* The Mellin scalar and scale, and the theta-coefficient formula.

**What it does not authenticate.**

* Patterson's theorem, or automorphy as a theorem. The checks use finitely many group elements, a
  truncated series and floating point.
* eq:reflection end to end. R3 sized such a test at about `10⁶` dual terms; it was not run.
* The contour shift (see §1.4), the bookkeeping of lem:squarefree-completed, and GL.
* The `1.1e-8` error in group E reflects series truncation near the cusps. Its role is to
  discriminate conventions (`√3` versus `1e-8`), not to give a precise value.

### 1.4 `reviews/oct5_residual_checks.py` (residual items: GL hypotheses, contour shift)

| Field | Value |
|---|---|
| SHA-256 / git blob / size | `d175c9736a75c581b0ee314ce013d932ed7c85e9723302b16959cff5acbec9b5` / `136ad58e` / 473 lines |
| Dependencies | numpy, scipy (`loggamma`). Its own integer arithmetic in `Z[ω]`; it does **not** import `eis.py` |
| Command | `python3 -I -B reviews/oct5_residual_checks.py --out /scratch/res.json`. The defaults are `--norm-bound 2000 --pair-bound 700` |
| Wall time | review: about 105 s; this rerun: 239 s (loaded machine) |
| Arithmetic class | MIXED. G1-G5 are `EXACT_RATIONAL` (integer arithmetic in `Z[ω]`). G6, C1 and C2 are `FLOATING_RECONNAISSANCE` |
| Pass rule | prints `ALL CHECKS PASSED in <s> s` and exits 0 |

**Expected output.** Every value below was reproduced in this rerun.

```text
G: norm_bound 2000, 302 primary primes, 568 squarefree rows;
   G1_unit_failures 0 (control: 288 rows with (-1/k)_2 = -1);
   G2 109 rows, primitivity failures 0, periodicity failures 0;
   G3 17741 coprime pairs, R values {-1,1}, 144 classes mod 4, 0 with two values (control: 9 classes mod 2 with two values);
   G4 e mismatch within class mod 4: 0;  G5 48 classes mod 8, 0 with two values
G6 (illustration): lambda_max(AA*)/(H+U) = 0.397, 0.370, 0.390 at H=U=250, 500, 1000
C1: all asymptotic ratios 1 + O(1/|T|); within 1e-7 of 1 at |T| = 1e4
C2: 6 cases (log-Gaussian and compact bump, x = 1e2, 1e4, 1e6), all 'pass': True;
    the control on Re t = -1 differs by exactly the residue at t = -5/6
ALL CHECKS PASSED in <s> s
```

**JSON record.** SHA-256 `e2892bb20bb2baf7a43ed1b5d8ae2f1898a679da5f79d6e9354a004fd006adba`. This
equals the hash recorded by the residual note (`e2892bb2…6adba`), so the run is byte-reproducible.

**What it authenticates.**

* For the family `ψ_k(x) = (x/k)₂ κ_λ(x)^{e_k}`, the hypotheses of GL Definition 1 on finite
  ranges:
  * triviality on units (568 rows);
  * primitivity of conductor `kλ^{e_k}` (109 rows with `N(k) ≤ 400`);
  * the reciprocity factor is a class function mod 4 (17,741 pairs), with a failing control mod 2;
  * `e_k` is constant on classes mod 4.
* The Stirling growth rates used in the Phragmén–Lindelöf argument.
* Contour-shift invariance of `V_*^♯` on several vertical lines. A residue control shows the test
  would detect a crossed pole.

**What it does not authenticate.**

* GL Theorem 1.1 itself, which is imported.
* The hypotheses for all `k`. The finite range is supported by the algebraic argument in the
  residual note §1.3.
* G6 is an illustration and not evidence for the large sieve.
* The Phragmén–Lindelöf argument itself, which was checked by reading.

## 2. Summary of this rerun

| Script | Exit | Result | Output hash vs review |
|---|---|---|---|
| `oct5_r1_checks.py` | 0 | ALL CHECKS PASSED | JSON identical (`59160e44…f44d`) |
| `oct5_r2_iteration_check.py` | 0 | 53/53 | stdout `620f4224…df17`, identical across two runs (the review recorded no hash) |
| `oct5_r3_theta_checks.py` | 0 | all groups as tabulated | JSON differs only in timing fields; values identical to R3's table |
| `oct5_residual_checks.py` | 0 | ALL CHECKS PASSED | JSON identical (`e2892bb2…6adba`) |

**What was not rerun.**

* The earlier numerics on `origin/claude/openai-math-riemann-analysis-w5copg`.
* PR 908's `checks/` scripts, which concern the import and the 7/8 manuscript.
* Any Lean build. The upstream Lean release targets 7/8, not this argument.

## 3. Independence and limits

* **Authorship.** The same agent reviewers wrote and ran all four scripts. This rerun repeats their
  computations; it is not an independent implementation.
* **Code paths.** R2 part E and the residual script each implement the symbols independently of
  `a2/eis.py`. R1 and R3 share `eis.py`.
* **No primitive data.** No script reads external data. Each one recomputes from definitions, so
  there is no primitive-replay or coverage contract to authenticate.
* **Small, finite scales.** Every script works at tiny norms and scales: `D ≤ 60`, norms up to a few
  thousand, and theta series truncated at `22000`.
* **Reviewing the scripts themselves.** An independent reviewer should treat these as evidence that
  conventions and identities were checked. They are not evidence for any estimate. Reviewing the
  scripts would be a separate task under [docs/REVIEWING.md](../../../../../docs/REVIEWING.md).
