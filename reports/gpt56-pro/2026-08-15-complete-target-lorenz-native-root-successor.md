# Complete Target-Lorenz tail and native two-ledger successor

Date: 2026-08-15  
Repository: `gfreund123/riemann`  
Origin PR: `#468`  
Frozen origin head: `9e2ae6d26a7920055e1f11327dc0ddeb7b855c61`  
Normative content commit: `9421eb45bcd10f0b7cdf4881a7adddbc295c8b64`  
RH status: **unproved; candidate-complete proposal awaiting hostile reconstruction**

## Executive result

This successor keeps the Target-Lorenz programme independent from the
root-Hall proposals on PRs #488/#489/#493/#494 and closes the two obligations
left open at the latest PR #468 head:

1. the complete real-parameter proportional determinant beyond `py=166000`;
2. one concrete positive common-parent endpoint row with a separate signed
   observation ledger and direct native `Y_4` pricing.

The proposed final object is a nonnegative finite row `d_X`, for every integer
`X>=10^12`, satisfying

\[
C_{d_X}(q)\le w_X(q),
\qquad
\Xi_{d_X}(q)\le\Omega_X(q)
\quad(q\ge2),
\]

and

\[
0\le J_\Lambda(X)-\mathcal H(d_X)<61000.
\]

This is the producer strength consumed by the frozen one-sided endpoint
criterion. It is deposited as a complete proposal, not represented as an
accepted proof of RH.

## I. Arithmetic Vector-Lorenz closure

### Compact half

Frozen `L-91781` certifies the complete real activation-cell domain

\[
py<166000,
\qquad p\ge67,
\qquad1\le y<67,
\qquad2\le j\le66.
\]

Its proof object covers `702,511,095` cells and is not a sampling grid.

### Analytic tail

New `L-93600` proves

\[
\sum_{n\le Y}n^{-1/2}\log(Y/n)
=4\sqrt Y+\zeta(1/2)\log Y+\zeta'(1/2)+R(Y),
\]

with the deliberately loose but uniform estimate

\[
|R(Y)|<5Y^{-3/2}.
\]

After insertion into the component-row Green form, all parent determinant
prefixes change only at

```text
x=d, x=jd, x=(j+1)d, d|P61.
```

`X-93600` enumerates all `2^18` divisors and `51,118,080` row-event records.
It obtains

```text
parent determinant lower bound:        >79
parent derivative lower bound:         >0.23
complete causal determinant lower:     >26
computed complete minimum:             26.786236008153155...
minimum location:                      x=166000, j=66
```

The child correction is proved nonincreasing between events. The final
unbounded interval is handled by an explicit positive polynomial and derivative
check after every divisor prefix is complete.

The arithmetic evaluation uses exact unsigned-128 event order and extended
`long double` transcendental arithmetic with a one-unit theorem reserve. This
is intentionally classified as a proposed complete analytic/finite-event
certificate requiring hostile replay, not silently promoted to an accepted
directed proof.

### Complete AVLT

`L-91780` gives

\[
\mathfrak L_j(p,y)
\ge\frac{O_TE_R^{(j)}-E_TO_R^{(j)}}{E_T}.
\]

The compact and tail domains meet exactly at `py=166000`, so new `L-93602`
closes every row `2,...,66` for every real admissible `(p,y)`. The exact
ordered-cone theorem `L-91720` then makes the leftmost Target-Lorenz removal the
one simultaneous target/score/all-row optimizer.

## II. Concrete common-parent producer

The central repair relative to the abstract `L-91783` interface is formula
`L-93603.5`:

\[
\Lambda_X^{\rm TL}
=
\int_{I_X}
\sum_{\ell\in\mathscr L_{X,s}}
\omega_{s,\ell}g_{s,\ell}\,d\mu_X(s).
\]

Here:

- `dmu_X(s)=2L(X/s)ds/s` is the frozen positive endpoint measure;
- `mathscr L_(X,s)` is the finite exact stopped-leaf tree;
- `omega_(s,l)` is the product of its exact nonnegative path coefficients;
- `g_(s,l)=R(E)-R(O)=R(nu)+B>=0` is the proved leaf row.

Thus the common parent is an explicit positive direct integral of actual leaf
rows. It is not a coordinatewise complement and not an assumed packet equality.
All actual rough-child responses remain internal colours in this one row.

## III. The two-ledger correction

Reviews #490--#492 correctly reject proofs that treat mismatch, collar or taper
vectors as positive source stages. `R-93600` makes that warning normative.

### Positive source ledger

```text
Target-Lorenz leaf rows;
bottom/top positive omissions;
one common scalar thinning;
positive pushforward;
one positive martingale quantizer.
```

### Signed observation ledger

```text
retained-cell finite/continuum mismatch;
intrinsic collar comparison;
terminal comparison.
```

The signed vectors are used only through absolute response estimates. Native
slack is defined only after all-column feasibility:

\[
r_X=\Omega_X-\Xi(d_X)\ge0.
\]

This also blocks full-child-capacity promotion and the circular benchmark
bridge `J_Lambda(X)-4sqrt(X)=O(log X)`.

## IV. Native feasibility and direct cost

The all-column estimate gives

\[
\frac{|e_X(q)|}{\Omega_X(q)}<\frac{129}{\sqrt K}
\quad(q\ge2),
\]

including `2<=q<K`. One common thinning

\[
\tau_K=\frac{\sqrt K}{\sqrt K+130}
\]

therefore leaves exact relative reserve

\[
1-\tau_K(1+129/\sqrt K)=\frac1{\sqrt K+130}>0.
\]

The terminal omission leaves reserve `581X^(-3/2)` and triangular support gives
zero response above the retained range. Positive radix-four inversion gives
ordinary feasibility.

The direct native cost is named before estimation:

```text
square-root thinning       <12012
nonterminal comparison     <4
terminal comparison        <48972
positive omissions         <1
root port / large-X base    0
--------------------------------
total                       <60989 <61000
```

No recursive family is exported. The root-global port is zero. Consequently

\[
J_\Lambda(X)-\mathcal H(d_X)<61000=o(\log^2X).
\]

## V. Endpoint composition

The frozen one-sided dual has the orientation

\[
F_\Lambda(X)
\le J_\Lambda(X)-\mathcal H(d_X).
\]

The new bound therefore supplies the exact producer input of `T-91313`. On the
frozen prime-square moat and Mellin--Landau inputs, the resulting endpoint
estimate gives the proposed RH conclusion.

This final implication remains conditional on hostile reconstruction of every
frozen consumer dependency. The repository must not treat RH as established
merely because this proposal is now reachable.

## Replays

```bash
cd experiments/X-93600-target-lorenz-tail
python3 verify.py --output results/verification.json
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS

cd ../X-93601-target-lorenz-native-endpoint
python3 verify.py --output results/verification.json
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_COMPLETE_TARGET_LORENZ_TAIL_AVLT
PASS_TARGET_LORENZ_TWO_LEDGER_NATIVE_ENDPOINT_PACKET
```

Proof-object digests:

```text
e30b0e4e08802002b160ddfaaefebb4b6ab8aa5a3562785fc854cc93f4101aa0
7207cbe3b241173e02d3c9a346056df861801522e4633675ecc2740711f96f02
```

## Exact boundary

```text
common-source vector optimizer                  exact
compact AVLT py<166000                          frozen directed exact
tail AVLT py>=166000                            proposed complete / replayed
complete all-parameter AVLT                     proposed complete
concrete positive common parent                 explicit / proposed complete
positive-vs-signed ledger separation            exact type firewall
all native columns                              proposed complete on frozen bounds
native Y4 deficit <61000                        proposed complete
endpoint-to-RH composition                      frozen conditional
Riemann Hypothesis                              unproved pending hostile review
```
