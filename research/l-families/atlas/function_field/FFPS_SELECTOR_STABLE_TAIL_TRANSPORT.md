# Stable-tail transport for every contractive selector lift

Status: **exact all-degree necessary edge law, complex-to-real and signed
transpose reductions, compatible three-row transport, and bounded exact
replay; no global bulk extension, all-degree selector optimum, native FFPS
adapter, RH, or GRH**

Bounded replay:
[`ffps_selector_stable_tail_transport.py`](ffps_selector_stable_tail_transport.py).
Canonical summary:
[`ffps_selector_stable_tail_transport.json`](ffps_selector_stable_tail_transport.json).

Frozen source boundary: the audited real-part Young-lattice propagation
packet at `9ced25befb6dd88146809866a34a15fec034b096`.  All four source blobs are
pinned by the replay.

## 0. Outcome

The two-row propagation theorem is the first slice of a more general stable
edge law.  Fix a partition `beta|-m`, independent of `d`, and define the
rank-`d-1` predecessor shape

\[
 \nu_\beta(d)=(d-1-m,\beta).
\tag{0.1}
\]

It is a partition once `d>=m+beta_1+1`; for the empty tail use `beta_1=0`.
Let `x_nu` be the predecessor potentials of any real or complex contractive
optimal lift, and put

\[
 Z_\beta(d)=(-1)^{m+1}\operatorname{Re}x_{\nu_\beta(d)}.
\tag{0.2}
\]

Define positive integers `a_beta` recursively.  On a column, including the
empty column,

\[
 a_{(1^m)}=m+1.
\tag{0.3}
\]

For every noncolumn partition,

\[
 a_\beta=\sum_{\gamma\lessdot\beta}a_\gamma,
\tag{0.4}
\]

where the sum is over the distinct Young-lattice predecessors of `beta`.
Define exact nonnegative errors by

\[
 E_{(1^m)}(d)=\sum_{r=0}^m{d-1\choose r}
\tag{0.5}
\]

and, off the columns,

\[
 E_\beta(d)
 =f^{(d-m,\beta)}+
  \sum_{\gamma\lessdot\beta}E_\gamma(d).
\tag{0.6}
\]

Then every contractive lift, including one with complex coefficients,
satisfies the exact stable-tail estimate

\[
 \boxed{
 \left|Z_\beta(d)-a_\beta{2^{d-1}\over d}\right|
 \le E_\beta(d).}
\tag{0.7}
\]

For each fixed `beta`,

\[
 E_\beta(d)=O_\beta(d^m),
\tag{0.8}
\]

and hence

\[
 \boxed{
 \operatorname{Re}x_{(d-1-m,\beta)}
 =(-1)^{m+1}a_\beta{2^{d-1}\over d}
  +O_\beta(d^m).}
\tag{0.9}
\]

Thus every fixed Young-lattice neighborhood of the hook edge is eventually
engaged with a forced sign and an explicitly recursive exponential leading
coefficient.  The repair is not merely deep along the two-row chain: it must
spread through every fixed tail shape.

The first genuine three-row family is already explicit:

\[
 a_{(j,1)}=2j+1\qquad(j\ge1).
\tag{0.10}
\]

Its leading terms cancel exactly around every stable three-row cover diamond.
So the three-row diamonds produce no local contradiction; instead they force
the next edge amplitude.  The unsolved problem is a **bulk matching gate**:
extend these forced top and transpose-edge profiles through tails whose size
grows with `d`, while keeping every cover sum inside its dimension box.

## 1. The predecessor-potential model

The audited source packet shows that any contractive primitive lift can be
written

\[
 F_d+R_d=z_dp_d+p_1X_{d-1},
 \qquad z_d={2^{d-1}\over d},
\tag{1.1}
\]

with

\[
 X_{d-1}=\sum_{\nu\vdash d-1}x_\nu s_\nu.
\tag{1.2}
\]

Pieri's rule turns the nonhook dimension boxes into

\[
 \left|\sum_{\nu\lessdot\lambda}x_\nu\right|
 \le f^\lambda
 \qquad(\lambda\vdash d\text{ nonhook}).
\tag{1.3}
\]

The hook potentials are real and forced.  If
`H_k=(d-1-k,1^k)`, then

\[
 x_{H_k}
 =(-1)^k\left[
   \sum_{r=0}^k{d-1\choose r}-(k+1)z_d
  \right].
\tag{1.4}
\]

Complex phases do not weaken the problem.  Taking real parts preserves
(1.4), and

\[
 \left|\sum\operatorname{Re}x_\nu\right|
 \le\left|\sum x_\nu\right|.
\tag{1.5}
\]

Consequently the real parts of every complex lift form a feasible real
potential system.  All estimates below apply directly to those real parts.

## 2. Exact stable-tail induction

Let `beta|-m` be noncolumn and consider the rank-`d` shape

\[
 \lambda_\beta(d)=(d-m,\beta).
\tag{2.1}
\]

Its first row is strictly longer than `beta_1`.  Removing its first-row
corner gives `nu_beta(d)`.  Removing a tail corner gives

\[
 (d-m,\gamma)=\nu_\gamma(d)
 \qquad(\gamma\lessdot\beta).
\tag{2.2}
\]

These are all its predecessors.  Since `beta` is not a column,
`lambda_beta(d)` is not a hook, so (1.3) says

\[
 \left|
  x_{\nu_\beta(d)}+
  \sum_{\gamma\lessdot\beta}x_{\nu_\gamma(d)}
 \right|
 \le f^{(d-m,\beta)}.
\tag{2.3}
\]

Every predecessor tail has size `m-1`.  After inserting the alternating
normalization (0.2), (2.3) becomes the stable transport inequality

\[
 \boxed{
 \left|Z_\beta(d)-
  \sum_{\gamma\lessdot\beta}Z_\gamma(d)
 \right|
 \le f^{(d-m,\beta)}.}
\tag{2.4}
\]

On a column, (1.4) gives an exact boundary value rather than an inequality:

\[
 Z_{(1^m)}(d)
 =(m+1)z_d-\sum_{r=0}^m{d-1\choose r}.
\tag{2.5}
\]

Equations (2.4)--(2.5), induction on `m`, and the definitions
(0.3)--(0.6) prove (0.7).

The coefficients `a_beta` are positive integers.  Equivalently, they are
weighted absorbing-path counts: follow all downward Young-lattice paths
until they first hit a column, and give a terminal column of height `r`
weight `r+1`.  This interpretation makes diamond compatibility automatic;
different downward routes are added, not identified.

For the error growth, a tableau of shape `(d-m,beta)` is determined in
particular by choosing the `m` entries outside its first row and then a
standard filling of `beta`.  Therefore

\[
 f^{(d-m,\beta)}
 \le {d\choose m}f^\beta=O_\beta(d^m).
\tag{2.6}
\]

The column error (0.5) is `O_m(d^m)`, and the predecessor errors in (0.6)
have degree at most `m-1`.  This proves (0.8), while exponential growth of
`z_d` proves (0.9).

## 3. Three-row diamonds are compatible but rigid

For a row tail, `a_(j)=2` for every `j>=1`.  The tail `(j,1)` has predecessors
`(j)` and `(j-1,1)`, with the column base `a_(1,1)=3`.  Thus

\[
 a_{(j,1)}=2+a_{(j-1,1)}=2j+1.
\tag{3.1}
\]

Write

\[
 A_j=x_{(d-1-j,j)},
 \qquad
 B_j=x_{(d-j-2,j,1)}.
\tag{3.2}
\]

For fixed `j>=2` and `d>=2j+2`, (0.9) gives

\[
 \begin{aligned}
 \operatorname{Re}A_j
  &=(-1)^{j+1}2z_d+O_j(d^j),\\
 \operatorname{Re}B_j
  &=(-1)^j(2j+1)z_d+O_j(d^{j+1}),\\
 \operatorname{Re}B_{j-1}
  &=(-1)^{j+1}(2j-1)z_d+O_j(d^j).
 \end{aligned}
\tag{3.3}
\]

The three predecessors of `(d-j-1,j,1)` are exactly the shapes carrying
`B_j`, `A_j`, and `B_(j-1)`.  Their exponential coefficients cancel:

\[
 (-1)^j\bigl((2j+1)-2-(2j-1)\bigr)=0.
\tag{3.4}
\]

This proves a useful negative result: no obstruction can come merely from
comparing the leading exponential transport around a fixed three-row
diamond.  Any obstruction must arise from the polynomial error budget or
from tails growing with `d`.

## 4. Signed transpose and the opposite edge

Put `n=d-1`.  For a real feasible potential system define

\[
 (\mathcal Tx)_\nu=(-1)^n x_{\nu'}.
\tag{4.1}
\]

Transposition preserves dimensions and Young-lattice covers.  The hook
boundary obeys

\[
 x_{H_{n-1-k}}=(-1)^n x_{H_k},
\tag{4.2}
\]

so `mathcal T` preserves both the boundary and every box constraint.
Averaging `x` with `mathcal T x` proves:

\[
 \boxed{
 \text{if any complex lift exists, a real lift with }
 x_{\nu'}=(-1)^{d-1}x_\nu\text{ exists}.}
\tag{4.3}
\]

Applying (0.7) to `mathcal T x` also forces the opposite-edge profile for
every lift:

\[
 \left|
 (-1)^{d+m}\operatorname{Re}x_{\nu_\beta(d)'}
 -a_\beta z_d
 \right|
 \le E_\beta(d).
\tag{4.4}
\]

Thus top-row and long-column edge transport are simultaneous necessities,
not alternative ansatzes.

## 5. The remaining bulk matching gate

The theorem removes three tempting shortcuts:

1. fixed-depth support is impossible;
2. restricting propagation to two-row shapes is impossible;
3. hoping that the first three-row diamonds create an immediate
   contradiction is also impossible, because their exponential parts obey
   the exact recursion (3.4).

The remaining gate is precise.  One must construct, or rule out, real
potentials on partitions of `d-1` which:

- have the forced hook values (1.4);
- may be chosen signed-transpose symmetric by (4.3);
- match (0.7) at every fixed tail and (4.4) at every transposed fixed tail;
- and satisfy all cover-sum boxes (1.3) when the tail size grows with `d`.

This is the **bulk Young-lattice matching gate**.  Fixed-tail asymptotics
cannot decide it: the relevant new regime is precisely the moving central
band where the Specht dimensions become exponential and can absorb the edge
flow.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_selector_stable_tail_transport.py --check
python -B -O research/l-families/atlas/function_field/ffps_selector_stable_tail_transport.py --check
python -B -m unittest tests.test_ffps_selector_stable_tail_transport
python -B -O -m unittest tests.test_ffps_selector_stable_tail_transport
```

The replay authenticates the audited source quartet and verifies the
absorbing-path recursion, exact column boundary, stable error recursion,
hook-transpose parity, and the three-row cancellation through tail size
eight and ambient degree 64.  It uses only integer and rational arithmetic:
no LP solve, character-table enumeration, finite-field enumeration,
`L`-function computation, zero search, or floating-point fit occurs.
