# L-15123 — Phase-avoiding root capture gives a positive arithmetic residue floor

Claim ID: `L-15123`  
Status: **PROVED ABSTRACT/FINITE LEMMA; COFINAL ZETA CAPTURE ESTIMATES OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15114`, `L-15122`; elementary compact-group recurrence  
Scope: a proof-producing sufficient condition for all arithmetic residue weights to be positive  
Related counterexample candidates: none

## 1. Purpose

`L-15122` expresses every arithmetic target-pinned residue as

\[
 w_k(c)
 =c v_k+
  \sum_{\gamma\in Z}
  A_{\gamma,L}\mathcal K_k(r_{\gamma,L})
  +e_k^{\rm rem}.
 \tag{L-15123.1}
\]

This lemma turns that exact identity into a robust finite lower bound and then
into a cofinal criterion.  It also removes a superficial phase obstruction:
for any fixed finite set of nonzero real ordinates, arbitrarily large supports
can be chosen so that none of their sine weights is small.

The remaining hard statement is no longer an undefined source comparison.  It
is a concrete weighted cardinal-leakage estimate against the complete
prime-side residual.

## 2. Phase-avoidance lemma

Let

\[
 \gamma_1,\ldots,\gamma_M\in\mathbb R\setminus\{0\}.
\]

Then there are a number `delta>0` and an unbounded set of real support lengths
`L` such that

\[
 \boxed{
 \min_{1\le j\le M}
 \left|\sin\left(\frac{L\gamma_j}{2}\right)\right|
 \ge\delta.}
 \tag{L-15123.2}
\]

### Proof

Consider the one-parameter orbit

\[
 L\longmapsto
 \left(rac{L\gamma_1}{2},\ldots,
       rac{L\gamma_M}{2}\right)
 \pmod{\pi}
\]

in the compact torus `(R/pi Z)^M`, and let `G` be its compact closure.  For each
coordinate `j`, the restriction to `G` of

\[
 z\longmapsto\sin z_j
\]

is not identically zero because `gamma_j!=0`.  Hence its zero set is a proper
closed subgroup coset union with empty interior in `G`.  A finite union of such
sets cannot cover the compact group `G`.  Choose a point of `G` outside their
union.  By continuity, one neighborhood of that point has all coordinate sine
values bounded below by one `delta>0`.

The original one-parameter orbit is dense in `G`; after any fixed time its tail
has the same closure.  It therefore returns to that neighborhood at arbitrarily
large values of `L`. QED.

No rational independence of the ordinates is required.  The lemma is existential;
a proof-producing implementation may locate one support by directed phase
balls and retain the resulting explicit lower bound.

## 3. Root capture data

Use the notation of `L-15122`.  Let the simple real roots of the finite target
polynomial be

\[
 u_1<\cdots<u_{n-1}.
\]

Choose distinct certified real zeros

\[
 \gamma(k)\in Z,
 \qquad 1\le k<n,
\]

and put

\[
 A_k=A_{\gamma(k),L},
 \qquad
 r_k^{Z}=r_{\gamma(k),L}.
\]

Define the paired cardinal error

\[
 \boxed{
 \varepsilon_k
 =\left|\mathcal K_k(r_k^Z)-1\right|,}
 \tag{L-15123.3}
\]

the selected-zero cross leakage

\[
 \boxed{
 C_k^Z
 =\sum_{\substack{\gamma\in Z\\
                    \gamma\ne\gamma(k)}}
   A_{\gamma,L}
   \left|\mathcal K_k(r_{\gamma,L})\right|,}
 \tag{L-15123.4}
\]

and let `E_k` be a directed absolute upper bound for the complete arithmetic
residual weight:

\[
 \boxed{|e_k^{\rm rem}|\le E_k.}
 \tag{L-15123.5}
\]

All three objects are finite proof data.  In particular `E_k` is obtained from
the complete prime-side source after subtracting the selected-zero source; it
is not an assumed unlisted-zero tail sign.

## 4. One-root lower bound

For every real scalar `c`,

\[
 \boxed{
 w_k(c)
 \ge
 A_k(1-\varepsilon_k)
 -C_k^Z-E_k+c v_k.}
 \tag{L-15123.6}
\]

### Proof

Separate the paired selected-zero term in (L-15123.1).  Its value is at least
`A_k(1-epsilon_k)`.  Bound every other selected term and the complete residual
by absolute value. QED.

Thus the paired zero supplies a positive diagonal mass, while all remaining
arithmetic information is charged in exactly two explicit error budgets.

## 5. Exact scalar interval from the conservative bounds

Put

\[
 b_k=A_k(1-\varepsilon_k)-C_k^Z-E_k.
 \tag{L-15123.7}
\]

The conservative residue inequalities are

\[
 b_k+c v_k>0
 \qquad(1\le k<n).
\]

Define

\[
 c_-^{\rm cap}
 =\max_{v_k>0}\frac{-b_k}{v_k},
 \qquad
 c_+^{\rm cap}
 =\min_{v_k<0}\frac{-b_k}{v_k},
 \tag{L-15123.8}
\]

with empty sides interpreted as infinite.  For every `k` with `v_k=0`, require
`b_k>0`.

If

\[
 \boxed{
 c_-^{\rm cap}<c_+^{\rm cap},}
 \tag{L-15123.9}
\]

then every rational

\[
 c\in(c_-^{\rm cap},c_+^{\rm cap})
\]

satisfies

\[
 w_k(c)>0
 \quad\text{for all }k.
\]

Consequently

\[
 \boxed{
 T_p(c)\succeq0,
 \qquad
 \ker T_p(c)=\mathbb Rp.}
 \tag{L-15123.10}
\]

The conclusion follows from the exact Cauchy-ray inertia formula of `L-15114`.

This interval is only a conservative selected-zero certificate.  If it is
empty, the exact directed values from (L-15122.15) or the exact
Bézoutian thresholds must still be tested.

## 6. The zero-boundary-scalar criterion

A particularly clean sufficient condition is

\[
 \boxed{
 \max_k
 \left(
  \varepsilon_k+rac{C_k^Z+E_k}{A_k}
 \right)<1.}
 \tag{L-15123.11}
\]

Then all `b_k>0`, so the arithmetic line passes already at

\[
 \boxed{c=0.}
\]

This is the exact root-capture diagonal-dominance target.  It compares:

- the displacement of one finite target root from one certified zero;
- the complete interaction with every other selected zero;
- the full remaining prime-side arithmetic residual;

against the positive phase weight of the paired zero.

## 7. Cofinal diagonal theorem

Let the level `j` have target roots `u_(j,k)`, a selected-zero set `Z_j`, and an
injective pairing `k -> gamma(j,k)`.  Suppose directed proof objects establish
for every sufficiently large `j`:

1. all target roots are real and simple;
2. every selected zero and its multiplicity is proof grade;
3. every paired phase weight `A_(j,k)` is strictly positive;
4. the complete residual source is produced from the full polar,
   archimedean, and prime-power formula;
5. either the scalar interval (L-15123.9) is nonempty or the stronger bound
   (L-15123.11) holds.

Then the fixed arithmetic target-pinned line passes cofinally.

A useful asymptotic sufficient form is

\[
 \boxed{
 \max_k\varepsilon_{j,k}
 +
 \max_k\frac{C_{j,k}^{Z_j}+E_{j,k}}{A_{j,k}}
 \longrightarrow0.}
 \tag{L-15123.12}
\]

The finite phase-avoidance lemma shows that, after freezing any one finite
selected-zero set, a support can be chosen with a positive phase moat.  It does
not supply a uniform moat for a growing zero set; the ratio in
(L-15123.12) is the correct cofinal object.

## 8. Relation to canonical-ray and moat tests

The canonical-ray LP of `L-15120` controls the complete matrix by one operator
norm.  The present theorem instead works in the exact Cauchy-residue basis and
can succeed when the matrix norm comparison is pessimistic.

The two tests have different strengths:

- canonical-ray LP: root free after canonical inertia, but sufficient only;
- selected-zero residue floor: root explicit, phase aware, and adapted to the
  actual zero-side arithmetic;
- exact `L-15114` thresholds: necessary and sufficient in the simple-real-root
  regime.

A production pipeline should run them in that order of cost and retain all
verdicts separately.

## 9. Gap audit

1. Phase avoidance is finite-set existential, not a uniform growing-set theorem.
2. Root capture cannot be inferred from coefficient signs or gap parity.
3. A small transform error on compact sets does not by itself control all
   cardinal kernels or the growing residual source.
4. The residual `E_k` must come from the complete prime-side source; replacing it
   by an RH-positive zero tail would be circular.
5. Bound (L-15123.11) is sufficient, not necessary.
6. No production Riemann level and no cofinal sequence satisfying
   (L-15123.12) is claimed here.