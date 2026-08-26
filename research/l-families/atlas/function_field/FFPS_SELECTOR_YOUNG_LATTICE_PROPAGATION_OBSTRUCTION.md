# Contractive selector repairs must propagate almost to the Young-lattice equator

Status: **exact all-degree necessary condition for an optimal derangement
selector lift; asymptotic propagation-depth theorem; bounded integer/rational
replay; no construction of the lift, all-degree optimum, native FFPS adapter,
RH, or GRH**

Bounded replay:
[`ffps_selector_young_lattice_propagation_obstruction.py`](ffps_selector_young_lattice_propagation_obstruction.py).
Canonical summary:
[`ffps_selector_young_lattice_propagation_obstruction.json`](ffps_selector_young_lattice_propagation_obstruction.json).

Frozen source boundary:

1. the finite exact optimization packet at
   `6d9e66033c1a00066935cceed9ca66b76b67fd99`;
2. the all-degree hyperbolic-tangent calibration, algebraic lift, sharp
   nonhook gap, and descent-set rigidity packet at
   `0909baac5`.

The result below is a necessary condition on any solution of the contractive
primitive-lift problem.  It neither constructs such a solution nor proves
that one exists.

## 0. Outcome

Fix `d>=5` and put

\[
 z_d={2^{d-1}\over d}.
\tag{0.1}
\]

Suppose `R_d` solves the three conditions of the contractive primitive-lift
problem: it is zero on every hook Schur coordinate, it removes the
`p_1`-free `tanh` tail while retaining `z_d p_d`, and
`F_d+R_d` remains in every dimension box.  Then there is a unique homogeneous
symmetric function `X_(d-1)` such that

\[
 F_d+R_d=z_dp_d+p_1X_{d-1}.
\tag{0.2}
\]

Write `x_nu=[s_nu]X_(d-1)`, and on the two-row chain put

\[
 X_j=x_{(d-1-j,j)}
 \qquad
 \left(1\le j\le\left\lfloor{d-1\over2}\right\rfloor\right).
\tag{0.3}
\]

The exact half-plane propagation theorem is

\[
 \boxed{
 \operatorname{Re}\!\left((-1)^{j-1}X_j\right)
 \ge {2^d\over d}-{d\choose j}.}
\tag{0.4}
\]

In particular, the alternating open half-plane and hence nonvanishing are
forced whenever the right side is positive. For a real lift this is exactly
the asserted alternating sign. If

\[
 m_d=max\left\{
 j\le\left\lfloor{d-1\over2}\right\rfloor:
 {d\choose j}<{2^d\over d}
 \right\},
\tag{0.5}
\]

then every contractive lift must engage all two-row predecessor potentials

\[
 (d-2,1),(d-3,2),\ldots,(d-1-m_d,m_d).
\tag{0.6}
\]

Moreover,

\[
 \boxed{
 m_d={d\over2}-\left({1\over2}+o(1)\right)
 \sqrt{d\log d}.}
\tag{0.7}
\]

Thus a bounded-depth, fixed-width, or merely near-hook repair cannot solve
the all-degree problem.  Any successful lift must propagate through a number
of two-row layers that is asymptotic to half the rank.  This is a global
Young-lattice obstruction, not another finite LP observation.

## 1. From the primitive lift to predecessor potentials

The hyperbolic-tangent packet proves

\[
 \pi_0(F_d+R_d)=z_dp_d,
\tag{1.1}
\]

where `pi_0` sets `p_1=0`.  Since the symmetric-function algebra in
characteristic zero is the polynomial algebra in the power sums, the kernel
of `pi_0` is the principal ideal `(p_1)`.  Equation (1.1) therefore gives
(0.2), uniquely because multiplication by `p_1` is injective.

By Pieri's rule, the Schur coefficient of `p_1X_(d-1)` at `lambda|-d` is

\[
 \sum_{\nu\lessdot\lambda}x_\nu.
\tag{1.2}
\]

The correction `R_d` has zero hook coordinates, while the natural `tanh`
certificate saturates every hook:

\[
 [s_{H_k}](F_d+R_d)
 =(-1)^k{d-1\choose k},
 \qquad H_k=(d-k,1^k).
\tag{1.3}
\]

Let `x_k=x_(d-1-k,1^k)` for `0<=k<=d-2`, and set the two absent endpoint
potentials to zero.  Since `[s_(H_k)]p_d=(-1)^k`, (1.2)--(1.3) give the exact
hook recurrence

\[
 x_{k-1}+x_k
 =(-1)^k\left({d-1\choose k}-z_d\right).
\tag{1.4}
\]

Solving from the top hook yields

\[
 x_k=(-1)^k\left[
 \sum_{r=0}^k{d-1\choose r}-(k+1)z_d
 \right].
\tag{1.5}
\]

In particular the first two-row potential is forced exactly:

\[
 \boxed{X_1=x_1={2^d\over d}-d.}
\tag{1.6}
\]

It is positive for every `d>=5`.

## 2. The exact two-row telescope

For

\[
 \lambda_j=(d-j,j),
 \qquad
 2\le j\le\left\lfloor{d-1\over2}\right\rfloor,
\tag{2.1}
\]

the only two predecessors are

\[
 (d-j,j-1)
 \quad\text{and}\quad
 (d-j-1,j),
\tag{2.2}
\]

whose potentials are `X_(j-1)` and `X_j`.  The shape `lambda_j` is not a
hook, so the `p_d` term has zero coefficient there.  Contractivity therefore
implies

\[
 |X_{j-1}+X_j|
 \le f^{(d-j,j)}
 ={d\choose j}-{d\choose j-1}.
\tag{2.3}
\]

Set `Y_j=(-1)^(j-1)X_j`. Equation (2.3) is exactly

\[
 |Y_j-Y_{j-1}|
 \le {d\choose j}-{d\choose j-1}.
\tag{2.4}
\]

Starting from the real value (1.6), taking real parts in (2.4), and
telescoping gives the **half-plane**, not merely absolute, lower bound

\[
 \begin{aligned}
 \operatorname{Re}(Y_j)
 &\ge Y_1-
 \sum_{r=2}^j\left({d\choose r}-{d\choose r-1}\right)\\
 &={2^d\over d}-d-\left({d\choose j}-d\right)\\
 &={2^d\over d}-{d\choose j}.
 \end{aligned}
\tag{2.5}
\]

This proves (0.4) for real or complex coefficients. Notice how little was
assumed: hook saturation, the
correct `p_1`-free target, and the ordinary dimension box.  No guessed
interior formula or finite-degree certificate enters the argument.

The first interior case also explains the role of the sharp `4/d` nonhook
slack.  At `lambda_2=(d-2,2)`, the natural `tanh` coefficient is

\[
 b_{d,(d-2,2)}={d-4\over d}f^{(d-2,2)},
\tag{2.6}
\]

so it has only `4f/d=2(d-3)` of outward room.  Meanwhile (2.5) forces

\[
 \operatorname{Re}(-X_2)\ge {2^d\over d}-{d\choose2}
\tag{2.7}
\]

whenever this quantity is positive.  The correction must therefore turn
inward and begin a long alternating propagation; the sharp slack cannot be
spent on a local outward patch.

## 3. Asymptotic depth

The binomial coefficients increase strictly for
`j<d/2`, so (0.5) is a single threshold.  Write

\[
 j={d\over2}-s.
\tag{3.1}
\]

Uniform Stirling expansion in the range `s=O(sqrt(d log d))` gives

\[
 \log\left(2^{-d}{d\choose d/2-s}\right)
 =-{1\over2}\log d+{1\over2}\log{2\over\pi}
  -{2s^2\over d}
  +O\left({s^4\over d^3}+{1\over d}\right).
\tag{3.2}
\]

At the threshold in (0.5), the left side is `-log d+o(1)`.  Hence

\[
 {2s^2\over d}={1\over2}\log d+O(1),
 \qquad
 s=\left({1\over2}+o(1)\right)\sqrt{d\log d}.
\tag{3.3}
\]

Moving one integer step does not change the leading term, which proves
(0.7).  Equivalently, the forced chain penetrates to within
`(1/2+o(1))sqrt(d log d)` of the two-row equator.

## 4. What this rules out, and what it does not

The theorem allows complex Schur coefficients. For a complex lift, (0.4)
places the alternating potential in an open right half-plane; for a real
lift, it forces its sign. Taking real parts of a feasible complex lift also
gives a feasible real lift because all targets and dimension boxes are real,
but the displayed statement applies directly to every complex lift.

The theorem rules out, in every sufficiently large degree:

- the hook-only predecessor-potential ansatz;
- every repair supported in a fixed number of two-row layers;
- every proposed all-degree formula whose two-row potentials vanish before
  the threshold `m_d`;
- interpreting the unrestricted algebraic zero-hook lift as evidence that a
  local contractive lift should exist.

It does **not** rule out a global correction extending through the forced
chain.  It also does not prove that the bound (0.4) is sharp, determine the
potentials off the two-row chain, or prove the all-degree selector optimum.
The next constructive problem is to find a dimension-box extension whose
two-row potentials follow the forced alternating transport and whose
three-row and deeper cover sums remain contractive.

## 5. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_selector_young_lattice_propagation_obstruction.py --check
python -B -O research/l-families/atlas/function_field/ffps_selector_young_lattice_propagation_obstruction.py --check
python -B -m unittest tests.test_ffps_selector_young_lattice_propagation_obstruction
python -B -O -m unittest tests.test_ffps_selector_young_lattice_propagation_obstruction
```

The replay authenticates both frozen source packets and checks the hook
recurrence, the two-row dimension identity, the exact real-part telescoping lower
bound, and the threshold through degree 256 using only integer and rational
arithmetic.  It performs no LP solve, character-table enumeration,
finite-field enumeration, `L`-function computation, zero search, or
floating-point asymptotic fit.
