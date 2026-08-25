# Rank-stable inverse design for the genus-two split locus

## Read this first

This packet repeats the bounded genus-two split-locus inverse-design
experiment after imposing one additional exact compact-group requirement:
the detector must have zero Haar mean both in `USp(4)` and in the imported
high-genus stable range.  In the source-locked coordinate order

\[
(I_{1,7},I_{1,9},I_{2,4},I_{2,8}),
\]

the four `USp(4)` means are already zero and the stable means are
`(1,1,2,2)`.  The new coefficient lattice is therefore

\[
c_1+c_2+2c_3+2c_4=0.
\]

The result is a clean negative control.  Under the same primitive,
sign-quotiented ambient-coordinate `L1<=8` contract, there are exactly **67**
rank-stable candidates.  The unique q=3,5 maximin winner is

\[
F_{\rm rs}=2I_{1,9}-2I_{2,4}+I_{2,8}.
\]

Its split-minus-complement conditional mean is positive at both training
fields and negative at held-out q=7:

| role | q | exact contrast | exact squared point-biserial correlation |
|---|---:|---:|---:|
| training | 3 | `8144/2187` | `10363240/209169793` |
| training | 5 | `22200752/6327375` | `38505733544180/804703506645951` |
| held out | 7 | `-80029416/61429585` | `266862809387544/44725418124652915` |

Thus removing high-genus universal mean drift does **not** repair transport
in this finite experiment.  This says nothing about all q, larger lattices,
or other objectives.

Start with `GENUS2_RANK_STABLE_INVERSE_DESIGN.md` (this note), then inspect
`genus2_rank_stable_inverse_design.json` for every exact score and survivor,
then read `genus2_rank_stable_inverse_design.py` for the
source locks and holdout firewall.  Independent checks are in
`test_genus2_rank_stable_inverse_design.py`.

## 1. Exact null lattice

A primitive integral basis is

\[
(-1,1,0,0),\qquad(-2,0,1,0),\qquad(-2,0,0,1).
\]

It is visibly saturated: every null vector is uniquely

\[
(c_1,c_2,c_3,c_4)=(-u-2v-2w,u,v,w),
\]

with `(u,v,w)=(c2,c3,c4)`.  “Null” here means only zero mean under the two
declared Haar functionals.  It does not mean pointwise or `L2` vanishing.

The search exhausts primitive integer vectors in this lattice, modulo overall
sign by requiring the first nonzero coordinate to be positive, under the
same ambient-coordinate `L1<=8` bound used by the preceding packet.  Of the
67 candidates, 28 have agreeing nonzero q=3 and q=5 contrast directions.
The training objective is unchanged: maximize first the smaller of the two
exact squared point-biserial correlations and then their sum, followed by
the inherited complexity tie-break.  The optimum has one witness.

## 2. Genuine q=7 holdout

The design function accepts exactly q=3 and q=5 summaries.  Only after it
returns the frozen winner does the holdout audit receive q=7.  Among the 28
training-eligible rank-stable directions:

- 2 retain their oriented training direction at q=7;
- 26 reverse or vanish; and
- the winner reverses.

The exact survival fraction is `1/14`.  Both survivors are retained in the
JSON.  The one with the best original training objective after filtering on
q=7 is

\[
2I_{1,7}+2I_{1,9}-I_{2,4}-I_{2,8}.
\]

Its held-out contrast is `141115481/368577510` and its held-out squared
correlation is
`19913578977861361/22948278614757432960`.  It is explicitly post hoc and is
not promoted as a replacement detector.

## 3. Exact comparison with the preceding winner

The previous unconstrained winner

\[
F_*=2I_{1,7}+4I_{1,9}-I_{2,4}+I_{2,8}
\]

has stable mean `6`, whereas `F_rs` has stable mean zero.  The added condition
therefore does exactly remove that universal mean channel.  It does not
improve the observed transport diagnostics:

| diagnostic | unconstrained packet | rank-stable packet |
|---|---:|---:|
| minimum q=3,5 `rho^2` | `1050205482451876/18533359280570751` | `38505733544180/804703506645951` |
| winner q=7 direction | reverses | reverses |
| eligible-lattice q=7 survival fraction | `80/849` | `1/14` |

The new minimum training effect is exactly
`1174856269609258840416435/1391282644902486179551367` times the old one.
The survival-fraction change is exactly `-271/11886`.  The absolute q=7
contrast is smaller by the exact ratio `160058832/255883667`, but its sign is
still wrong.  On the declared finite tests, rank-stability buys cleaner
compact calibration, not arithmetic generalization.

## 4. Provenance and resource boundary

The packet source-locks both the previous inverse-design packet and the
high-genus stability packet by LF-normalized file hashes and canonical JSON
payload hashes.  The former in turn authenticates the complete q=3,5,7
joint `(a_D,b_D)` histograms, their producer, the root-free interferometer
engine, and the integral `+q` elliptic-form split predicate.  The latter
imports the stable trace-moment theorem and its exact mean vector.

Only 251 signed histogram atoms are replayed.  The producer enumerates 67
coefficient candidates and performs 165 exact candidate/field score
evaluations.  Every count is below an inclusive fail-closed cap of 4,096.
There is no field, polynomial, curve, root, or member enumeration; no random
sampling; and no floating-point arithmetic.

## 5. Interpretation firewall

Established exactly are the declared lattice classification, its unique
two-field training winner, all three exact field scores, and the complete
q=7 survival ledger.  Not established are:

- an all-q or asymptotic transport law;
- optimality beyond this four-coordinate `L1<=8` lattice and objective;
- a geometric split-Jacobian classification;
- subgroup, endomorphism, motive, or monodromy diagnosis;
- a zero-statistics theorem; or
- any RH or GRH consequence.

The useful mechanism lesson is narrower: cancelling an independently known
universal compact-group mean is good detector hygiene, but that cancellation
alone does not force a finite arithmetic split contrast to transport.

## 6. Replay

The deterministic payload hash is

`99f2e9425a5b957f780ee85abf107d3b2ef3054398899f72a8eb19a59c67ae05`.

From the repository root:

```text
python research/l-families/atlas/function_field/genus2_rank_stable_inverse_design.py --check
python -O research/l-families/atlas/function_field/genus2_rank_stable_inverse_design.py --check
python -m unittest tests.test_genus2_rank_stable_inverse_design
python -O -m unittest tests.test_genus2_rank_stable_inverse_design
```
