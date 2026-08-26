# Higher moments give a positive atom-free escape—at a delocalization price

Status: **exact finite-dimensional theorem and candidate amplifier boundary;
no FFPS moment estimate, RH, or GRH claim**

Exact replay:
[`ffps_higher_order_atom_free_escape.py`](ffps_higher_order_atom_free_escape.py).

## 0. Outcome

The quadratic no-go is absolute: a nonzero positive-semidefinite quadratic
form cannot have zero atomic diagonal.  It does not extend unchanged to
higher degree.

Put

\[
 a_i=|z_i|^2,\qquad A=\sum_i a_i,
 \qquad \max_i a_i\le\alpha A,
\tag{0.1}
\]

and define the ordered collision-free `k`-tuple energy

\[
 U_k(a)=
 \sum_{i_1,\ldots,i_k\ {m distinct}}
 a_{i_1}\cdots a_{i_k}.
\tag{0.2}
\]

It is positive and vanishes on every source supported on fewer than `k`
atoms.  In particular, it has no one-atom contribution.  If
`(k-1)alpha<1`, then

\[
 \boxed{
 U_k(a)\ge A^k
 \prod_{j=0}^{k-1}(1-j\alpha).}
\tag{0.3}
\]

For `N` source atoms, Cauchy gives `|P|^2<=NA`; hence

\[
 \boxed{
 |P|^{2k}
 \le {N^k\over\prod_{j=0}^{k-1}(1-j\alpha)}\,U_k(a).}
\tag{0.4}
\]

This is a genuine positive atom-free principal majorant, but only on a
delocalized class.  It makes the escape route exact:

\[
 \text{higher family moment}
 +\text{ source delocalization}
 \longrightarrow\text{ positive collision-free domination}.
\tag{0.5}
\]

Neither input is free.  The factor `N^k` may be too expensive, and high
moments are precisely where exceptional geometric strata can dominate.

## 1. Proof of the distinct-tuple bound

Expand (0.2) sequentially.  After choosing `j` distinct indices, the mass
available to the next index is

\[
 A-a_{i_1}-\cdots-a_{i_j}
 \ge A(1-j\alpha).
\]

Summing one index at a time therefore gives

\[
 \begin{aligned}
 U_k
 &=\sum_{i_1}a_{i_1}
   \sum_{i_2\ne i_1}a_{i_2}\cdots
   \sum_{i_k\notin\{i_1,\ldots,i_{k-1}\}}a_{i_k}\\
 &\ge A\cdot A(1-\alpha)\cdots A(1-(k-1)\alpha),
 \end{aligned}
\]

proving (0.3).

If `a_i=A/s` on exactly `s` atoms, then `alpha=1/s` and

\[
 {U_k\over A^k}={(s)_k\over s^k}
 =\prod_{j=0}^{k-1}\left(1-{j\over s}\right).
\tag{1.1}
\]

Thus (0.3) is sharp at every reciprocal delocalization level.  When the
`z_i` also have a common phase, Cauchy in (0.4) is sharp for `s=N`, so the
complete principal constant is sharp on the uniform source.

## 2. The first useful case

At `k=2`,

\[
 U_2=A^2-\sum_i a_i^2
 \ge(1-\alpha)A^2,
\tag{2.1}
\]

and

\[
 |P|^4\le{N^2\over1-\alpha}U_2.
\tag{2.2}
\]

This is a fourth-moment object.  It deletes the repeated source atom
positively rather than subtracting a Wick diagonal from a square.  The
quadratic PSD firewall does not apply because `U_2` is quartic in `z`.

However, (2.1) shows the exact new gate.  If one atom carries nearly all the
mass, `alpha` approaches one and the bound degenerates.  An arithmetic use
must prove a participation-ratio or maximum-atom estimate before invoking the
positive collision-free moment.

## 3. Candidate FFPS use and its risks

The corrected FFPS source already distinguishes literal atoms, equal
physical products, shared incidence, roots, and owner/core overlaps.  A
higher-order adapter could retain only tuples surviving the full collision
ledger and seek a bound for their positive `U_k` energy.

The required programme would be:

1. define `a_omega` from the native amplified atom before any conductorwise
   absolute value;
2. prove a uniform delocalization inequality
   `max a_omega <= alpha sum a_omega` with `(k-1)alpha<1`;
3. express the distinct-tuple energy as a source-faithful fourth or higher
   family moment;
4. remove geometric partial diagonals and constant constituents, not just
   literal equality;
5. compare the resulting `N^k` loss with the hard-mask leverage and the size
   of the character family.

This is a possible nonlinear route around atom-free quadratic indefiniteness.
It is not automatically favorable.  The atlas's high-symmetric-power tail
theorem warns that high moments may be governed by a thin exceptional
stratum; here that failure is measured directly by `alpha`.

## 4. What this changes about individualization

At quadratic order, positive family domination must pay the full principal
diagonal.  At order four and above, positivity can coexist with collision
deletion, but a single concentrated member defeats every such domination.
Therefore a higher-order individualization theorem must have two parts:

\[
 \boxed{
 \text{positive distinct-tuple moment}
 \quad+\quad
 \text{anti-concentration/rigidity}.}
\tag{4.1}
\]

The anti-concentration statement could come from a deterministic source cap,
an incidence theorem, or a rigidity result saying that a large principal
atom forces many comparable family atoms.  This gives a concrete role to the
rare-event tomography programme: classify exactly the strata on which
`alpha` is large.

## 5. Proof ledger

Proved exactly:

- positivity and collision-freeness of `U_k`;
- the delocalized lower bound (0.3);
- the principal corollary (0.4);
- sharpness on uniform finite supports.

Not proved:

- an FFPS delocalization estimate;
- a source-faithful higher moment with all partial diagonals removed;
- an affordable `N^k` loss;
- a family-to-principal theorem, RH, or GRH.

## 6. Bounded replay

Run:

```text
python -B research/l-families/atlas/function_field/ffps_higher_order_atom_free_escape.py --check
python -B -O research/l-families/atlas/function_field/ffps_higher_order_atom_free_escape.py --check
python -B -m unittest tests.test_ffps_higher_order_atom_free_escape
python -B -O -m unittest tests.test_ffps_higher_order_atom_free_escape
```

The replay uses rational masses on at most eight atoms and ordered tuples of
length at most four.  It performs no point count, conductor enumeration, or
floating-point operation.
