# Canonical detector ports on a function-field norm lattice

**Status:** exact sampling/commensurability theorem and normalization
firewall.  It evaluates no L-function family and proves no sign, moment, RH,
or GRH statement.

**Question.**  The canonical number-field programmes use the literal dyadic
shift `S_2`, the ratio-four HCNC geometry, and dyadic physical-occupancy
shells.  What survives if their scale variable is sampled only at polynomial
norms

\[
        X=q^n,\qquad n\in\mathbf Z,
\]

for a fixed prime power `q`?

The answer has two parts.  A dilation is a genuine translation of the native
degree lattice only when it is an integral power of `q`.  A noncommensurate
dilation can still be evaluated after choosing a step extension in the
continuous scale variable, but then it aliases to adjacent degree shifts.
For the canonical minimal wavelet this aliasing lowers its double
constant-annihilation zero to a simple zero for every integer `q>2`.

This is not a claim that a function-field experiment is impossible.  It says
exactly which experiments are the literal detector, which require an extra
log-phase coordinate, and which are new `q`-adic analogues.

## 1. Native translations

Let `Lambda_q={q^n:n in Z}`.  Multiplication by a positive rational `lambda`
maps `Lambda_q` to itself if and only if

\[
             \lambda=q^k\quad\text{for some }k\in\mathbf Z.
\tag{1}
\]

Indeed, applying the putative map to `1` proves necessity, and sufficiency is
immediate.  In prime valuations, (1) says that the valuation vector of
`lambda` is an integral multiple of that of `q`.

Consequently, for an odd prime power `q`, none of `2`, `4`, or `8` is a
native degree translation.  More generally, if `q=p^f` and the dilation is
`2^j`, commensurability holds exactly when `p=2` and `f` divides `j`; the
degree shift is then `j/f`.

Two norm lattices have a common nontrivial rational translation precisely
when their bases are powers of the same prime.  Thus the `q=3,5,7` panels do
not share any nontrivial native dilation.  This is an exact obstruction to a
single translation-invariant degree kernel across those characteristics, not
an obstruction to comparing separately normalized statistics.

## 2. What a step extension actually does

Given a degree sequence `(a_n)`, its standard right-continuous norm-step
extension is

\[
 F(q^{n+t})=a_n,\qquad 0\le t<1.
\]

Write `lambda=q^(k+beta)` with integer `k` and `0<=beta<1`.  Directly taking
the floor gives

\[
 (S_\lambda F)(q^{n+t})=
 \begin{cases}
 a_{n-k-1},&0\le t<\beta,\\
 a_{n-k},&\beta\le t<1.
 \end{cases}
\tag{2}
\]

When `beta=0`, this is one native degree shift.  Otherwise the continuous
shell is cut at the extra log-phase `beta={log_q lambda}`.  At the sampled
right endpoints `t=0`, the induced shift is

\[
             n\longmapsto n-\lceil\log_q\lambda\rceil.
\tag{3}
\]

Equations (2)--(3) expose two distinct choices:

* retain the continuous log-phase and the literal physical dilation; or
* discard the phase and accept endpoint aliasing to a degree kernel.

Neither choice may silently be described as a native lattice translation
when (1) fails.

## 3. Exact collapse of the minimal XD wavelet

The reviewed canonical kernel is

\[
 K_1=(I-\sqrt2S_2)(I-S_2)^2
 =I-(2+\sqrt2)S_2+(1+2\sqrt2)S_4-\sqrt2S_8.
\tag{4}
\]

On the full dyadic scale its symbol has a double zero at `z=1`.  If only the
endpoint samples `X=q^n` are retained, (3) groups the four terms by

\[
        d_j(q)=\lceil\log_q(2^j)\rceil,qquad j=0,1,2,3.
\]

There are only three cases for integer `q>=3`:

| `q` | `(d_0,d_1,d_2,d_3)` | collapsed endpoint symbol |
|---:|---|---|
| `3` | `(0,1,2,2)` | `1-(2+sqrt(2))z+(1+sqrt(2))z^2` |
| `4<=q<=7` | `(0,1,1,2)` | `1+(sqrt(2)-1)z-sqrt(2)z^2` |
| `q>=8` | `(0,1,1,1)` | `1-z` |

Every row still annihilates constants, but its derivative at `z=1` is,
respectively,

\[
       \sqrt2,\qquad -(1+\sqrt2),\qquad -1.
\]

Hence:

\[
\boxed{\text{endpoint sampling lowers the double zero of }K_1
       \text{ to a simple zero for every integer }q>2.}
\tag{5}
\]

This is stronger than saying that the ratio-eight support becomes awkward.
One of the exact cancellation moments is lost.  For `q=3`, the `S_4` and
`S_8` terms collide; for `4<=q<=7`, the `S_2` and `S_4` terms collide; for
`q>=8`, all three nonidentity terms collide.

At `q=2` the shifts are `(0,1,2,3)` and no collapse occurs.  Characteristic
two, however, is outside the odd-characteristic quadratic-character model
used by the current hyperelliptic atlas; it would require a separate
Artin--Schreier source and is not supplied by this packet.

## 4. HCNC and BPOE

The same theorem applies before any arithmetic estimate is attempted.

* A literal ratio-four translation is native only if `4=q^k`.  Among prime
  powers this means `q=2` with `k=2` or `q=4` with `k=1`.  For odd `q`, the
  endpoint ratio-four comparison aliases to a norm ratio `q^ceil(log_q 4)`.
  It is therefore not the same physical near-collision geometry.
* A dyadic BPOE shell carries the phase split (2) unless its dilation is a
  power of `q`.  Erasing that phase changes its physical occupancy ledger.

No HCNC or BPOE bound is refuted: their native scopes are number-field
dyadic shells.  The conclusion is only that an odd-characteristic,
degree-only packet cannot be called a literal port without a theorem that
handles the additional phase/aliasing.

## 5. The admissible research choices

There are now three clean paths.

1. **Continuous-scale port.**  Keep `X` continuous, retain every threshold
   `{log_q(2^j)}`, and carry the resulting phase-dependent source ledger.
   This is closest to the literal dyadic detector but is not a finite
   translation-invariant degree convolution.
2. **Native `q`-adic analogue.**  Replace `S_2` by `S_q` and, if the
   normalization is scaled with the shell ratio, replace `sqrt(2)` by
   `sqrt(q)`.  This restores a native degree kernel but defines a new
   detector whose relation to XD/HCNC/BPOE must be proved rather than named.
3. **Characteristic-two programme.**  Work at the commensurate bases and
   rebuild the arithmetic family in its correct characteristic-two model.

The physical-squareclass FFPS packet follows a fourth, already native route:
it keeps the Boolean/Kummer source of corrected `FFPS106121` and does not
rename a degree wavelet as XD.

## 6. Provenance and replay

The producer locks the integrated XD, HCNC, and BPOE summaries and the
physical-squareclass adapter by LF-normalized SHA-256.  It performs only
integer factorization and the nine displayed tiny controls; its claim
payload contains no floating-point approximation to any logarithm or
square root.

Replay from the repository root:

```text
python -B research/l-families/atlas/function_field/canonical_detector_norm_lattice_obstruction.py --check
python -B -O research/l-families/atlas/function_field/canonical_detector_norm_lattice_obstruction.py --check
python -B -m unittest tests.test_canonical_detector_norm_lattice_obstruction
python -B -O -m unittest tests.test_canonical_detector_norm_lattice_obstruction
```

