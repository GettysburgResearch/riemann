# Family binding: permutation counterfeits and the sharp mean-only tax

Status: **exact elementary structural firewall; not an RH estimate, not an
amplifier, and not a novelty claim**.

Scope: finite labeled scalar trace systems over the reals (the recovery
obstruction also holds over any set). Theorems hold for every integer
`N>=1`; computation is a bounded exact regression corpus, not their proof.

Exact sources: programme base
`6675c19f20760301d8c91dedc4a7836170003512`, with the two documentary sources
locked in `family_binding_permutation_firewall.sources.json`. No analytic or
RH-facing theorem is imported into the proofs below.

Smallest remaining gap: exhibit source-faithful, label-sensitive binding or
prove a useful uniform bound for the actual arithmetic family. Neither is
supplied here. RH and GRH remain open.

## 1. The interface and its exact loss

Let `I={0,...,N-1}`, fix an external principal label `p in I`, and let
`a=(a_i)_{i in I}` be a labeled tuple. The principal label stays fixed when
the tuple is relabeled. A datum `D(a)` is permutation invariant if

\[
 D((a_{\pi(i)})_{i\in I})=D(a)\qquad(\pi\in S_N).
\]

Thus `D` factors through the orbit map to the complete unlabeled multiset
`[a]`. Even providing `[a]` and the name `p` does not provide their binding.

**Theorem 1 (orbit-wise principal recovery).** On the full permutation orbit
of `a`, the possible values at the fixed label `p` are exactly
`{a_i : i in I}`. Consequently the principal coordinate is recoverable from
the complete unlabeled multiset on that orbit if and only if all entries
are equal. For `N>=2` there is no universal recovery function from any
permutation-invariant datum on all labeled real tuples.

Proof. Every permutation leaves the value at `p` among the original entries.
Conversely, transposing `p` with any `q` puts `a_q` at `p`. If two values
differ, these labelings have the same `D` but require different outputs of a
putative recovery function. If all entries equal `c`, the multiset recovers
`c`. This includes `N=1`. Repeated entries do not alter the obstruction when
at least two distinct values remain. A *coarser* invariant datum need not
recover even an all-equal tuple's common value. This last sufficiency is for
the complete multiset, not every invariant datum. QED.

This theorem concerns unrestricted relabeling with a fixed external mark.
If the principal member is independently characterized as, say, the maximum,
or if additional structure forbids the transposition, that is a binding
axiom outside this interface, not a counterexample to the theorem.

## 2. An upstream scalar trace counterfeit, at every order

Define the member operator first: `A_i=[a_i]` on a one-dimensional real
space. For each integer `r>=0`, its averaged trace moment is

\[
 m_r(a)=\frac1N\sum_i\operatorname{tr}(A_i^r)
       =\frac1N\sum_i a_i^r,
 \qquad m_0=1.
\]

Here `A_i^0` is the identity, including when `a_i=0`. No zero set or desired
spectral conclusion is inserted. Relabeling merely reindexes each sum, so
**every order** agrees, not only a finite trained list of moments.

For `N>=2` and `M>0`, fix `p=0` and take

\[
 a^+=(M,-M,0,\ldots,0),\qquad
 a^-=(-M,M,0,\ldots,0).
\tag{2.1}
\]

The complete unlabeled operator multisets agree, whereas the principal
traces are `+M` and `-M`. Their common moments are

\[
 m_0=1,\qquad m_{2j+1}=0\ (j\ge0),\qquad
 m_{2j}=2M^{2j}/N\ (j\ge1).
\]

Even nonnegativity does not restore recovery: the two labelings
`(M,0,...,0)` and `(0,M,0,...,0)` have identical every-order moments and
principal values `M` and `0`. Thus the failure is information loss under
label forgetting, not a moment-truncation error. These are synthetic scalar
trace systems; they are not asserted to be arithmetic `L`-function families.

## 3. What a nonnegative first average really gives

**Theorem 2 (sharp mean-only domination).** If all `a_i>=0` and
`bar a=(1/N) sum_i a_i`, then

\[
 \boxed{a_p\le N\bar a.}
\tag{3.1}
\]

For each fixed `N>=1`, the least constant valid for every such family and
every `p` is exactly `N`.

Proof. The selected term is at most the sum of all nonnegative terms. For
the spike with value `M>0` at `p` and zero elsewhere, `bar a=M/N`, so a
constant `C` in place of `N` requires `M<=CM/N`, hence `C>=N`. If the mean
is zero, all entries are zero; there is no ratio to divide by. The `N=1`
case has constant one. QED.

The optimality concerns the **first average alone**, not all symmetric data.
With the complete multiset the sharp uniform envelope is `max_i a_i`, even
though the principal coordinate itself is unknown. For nonnegative entries
and any integer `r>=1`,

\[
 a_p\le (N m_r)^{1/r},\qquad
 \max_i a_i\le (N m_r)^{1/r}
       \le N^{1/r}\max_i a_i.
\tag{3.2}
\]

Hence all moments can recover the maximum by taking `r` to infinity. The
firewall does not rule out a bound on **every** member from symmetric data,
and it does not assert an unavoidable `N`-loss when stronger moments or
additional structure are available. Obtaining useful arithmetic moment
bounds with affordable constants is a separate analytic burden.

## 4. Signed quantities and exact escape routes

For `N>=2`, (2.1) has signed mean zero and positive selected value `M` in
one labeling. No finite multiplicative constant can bound that value by the
ordinary signed mean on all real families. Nonnegativity in Theorem 2 is
essential. For `N=1`, the signed mean is the selected value, so this
zero-mean counterexample is unavailable.

An absolute envelope is different and always valid:

\[
 |a_p|\le N\,\frac1N\sum_i |a_i|,
\]

with the same sharp constant `N` for a spike. A centered or signed trace
must not silently be treated as a nonnegative family moment.

The datum `sum_i 1_{i=p} a_i=a_p` would recover the principal member, but it
explicitly uses the missing label binding. It is not an amplifier or inverse
constructed from the invariant datum. A genuine escape may instead use
independently supplied labeled transform coefficients, source identities,
rigidity, or uniform estimates. This packet constructs none of them.

In particular the frozen
[`FFPS_PRINCIPAL_ANOMALY_TRANSFER_DICHOTOMY.md`](../l-families/atlas/function_field/FFPS_PRINCIPAL_ANOMALY_TRANSFER_DICHOTOMY.md)
already records the labeled signed identities `P=A-K=C-S`. They are **not**
unlabeled family averages. Once either required pair of signed global bounds
is supplied, that identity already performs principal extraction; this
firewall imposes no third amplifier. The open arithmetic estimates in that
packet remain open. Its RH-facing source implications are neither replayed
nor used to prove Theorems 1 and 2 here.

## 5. Bounded replay and source boundary

The producer uses integers and `fractions.Fraction` only. It checks signed
opposite pairs for `2<=N<=8`, positive spikes for `1<=N<=8`, repeated and
all-equal controls, and moments `0<=r<=12`. It independently enumerates
every tuple over `{-1,0,1}` of lengths one through four, every principal
label, and all distinct permutation labelings. The fixture retains census
counts and a digest of the complete deterministic census transcript rather
than a large table. The mathematical all-order statement is the reindexing
proof above, not an inference from these twelve positive orders.

Runtime helpers reject empty families, `N>8`, inexact or Boolean values,
oversized rational inputs, invalid permutations/labels, and moment orders
outside `0..12`. Numerator/denominator bit length is capped at 32. These are
computation caps, not theorem hypotheses.

The source manifest authenticates the programme target and the labeled
signed-extraction boundary at the exact base commit: both Git blob IDs and
LF-normalized SHA-256 contents are checked through the Git object database.
It does not authenticate any live arithmetic family or analytic estimate.
The fixture binds the current note, producer, tests, and manifest by
LF-normalized SHA-256 hashes; check mode independently rebuilds every field.
No result-bearing check is a Python `assert`, so optimization cannot remove
it. This is an exploratory packet awaiting independent exact-SHA review,
not an integrated theorem or an externally established novelty claim.

```powershell
python -B research/riemann-structures/family_binding_permutation_firewall.py --check
python -B -O research/riemann-structures/family_binding_permutation_firewall.py --check
python -B -m unittest tests.test_family_binding_permutation_firewall
python -B -O -m unittest tests.test_family_binding_permutation_firewall
```

The reusable output is an exact structural firewall: any claim using only
label-erasing averages must either pay the applicable information/mean cost
or identify the additional binding/stronger estimate it uses. It is not an
RH estimate, not an actual amplifier or inversion, and not a novelty claim.
