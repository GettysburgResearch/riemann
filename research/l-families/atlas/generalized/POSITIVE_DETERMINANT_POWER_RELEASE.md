# Positive-determinant release for local coefficient powers

Status: **exact transport corollary; no new mechanism or novelty claim**

Issue: [#764](https://github.com/gfreund123/riemann/issues/764)

Claim labels:
`GLO764.POSITIVE_DETERMINANT_POWER_RATIONALITY`,
`GLO764.POSITIVE_DETERMINANT_INTEGER_MINIMAL_DENOMINATOR`, and
`GLO764.POSITIVE_DETERMINANT_BRANCH_GATE`.

## Audit verdict

The positive real semisimple varying-determinant chamber is worth recording,
but it is **not** an independent nonrationality theorem.  It is exactly the
determinant-one theorem transported by a positive scalar and a nonzero change
of the generating variable.  The durable content of this packet is the exact
coordinate release:

\[
 u_r=s^r v_r,
 \qquad
 G_{\lambda;t,\delta}(T)
 =G_{\lambda;x,1}(s^\lambda T),
 \qquad
 s=\sqrt\delta>0.
\tag{0.1}
\]

It closes the positive-real portion of the scalar determinant-parameter
queue, makes every logarithm and square-root choice explicit, and transports
the sharp integer denominator.  The rationality classification itself is a
corollary of the authenticated determinant-one source theorem.

## 1. Positive semisimple chamber

Fix real numbers

\[
 \alpha>\beta>0,
 \qquad
 t=\alpha+\beta,
 \qquad
 \delta=\alpha\beta>0.
\tag{1.1}
\]

Equivalently, one may start from

\[
 \delta>0,
 \qquad
 t>2\sqrt\delta,
\tag{1.2}
\]

and take the two distinct positive roots of

\[
 X^2-tX+\delta=0.
\tag{1.3}
\]

Define

\[
 u_0=1,
 \qquad
 u_1=t,
 \qquad
 u_{r+2}=t u_{r+1}-\delta u_r.
\tag{1.4}
\]

The exact Binet formula is

\[
 \boxed{
 u_r=\frac{\alpha^{r+1}-\beta^{r+1}}{\alpha-\beta}.
 }
\tag{1.5}
\]

Indeed, the right side has initial values `1,t`, and both geometric
components satisfy (1.4).  It is positive for every `r>=0` because
`alpha>beta>0`.

For any `lambda in C`, use only the ordinary logarithm of a positive real
number:

\[
 u_r^\lambda=\exp(\lambda\log u_r),
 \qquad
 G_{\lambda;t,\delta}(T)
 =\sum_{r\geq0}u_r^\lambda T^r.
\tag{1.6}
\]

Rationality means that the analytic germ at `T=0` belongs to `C(T)`.

## 2. Determinant normalization

Let

\[
 s=\sqrt\delta>0,
 \qquad
 a=\sqrt{\alpha/\beta}>1.
\tag{2.1}
\]

These are the unique positive square roots.  Then

\[
 \alpha=sa,
 \qquad
 \beta=sa^{-1},
 \qquad
 x=\frac{t}{s}=a+a^{-1}>2.
\tag{2.2}
\]

Let

\[
 v_0=1,
 \qquad
 v_1=x,
 \qquad
 v_{r+2}=xv_{r+1}-v_r.
\tag{2.3}
\]

Substitution in (1.5) gives

\[
 \boxed{u_r=s^r v_r.}
\tag{2.4}
\]

Every factor in (2.4) is positive.  Therefore the positive logarithm is
additive here:

\[
 \log u_r=r\log s+\log v_r.
\tag{2.5}
\]

For complex `lambda`, define the unambiguous positive-base scalar

\[
 s^\lambda=\exp(\lambda\log s)\ne0.
\tag{2.6}
\]

Equations (2.4)--(2.6) yield the formal and analytic-germ identity

\[
 \boxed{
 G_{\lambda;t,\delta}(T)
 =G_{\lambda;x,1}(s^\lambda T).
 }
\tag{2.7}
\]

The substitution `T -> s^lambda T` is invertible because `s^lambda` is
nonzero.  Hence it preserves rationality in both directions.

## 3. Exact rationality classification

### Theorem GLO764.POSITIVE_DETERMINANT_POWER_RATIONALITY

For every fixed `alpha>beta>0`, or equivalently every
`delta>0, t>2*sqrt(delta)`, and every `lambda in C` under the positive-real
logarithm convention,

\[
 \boxed{
 G_{\lambda;t,\delta}(T)\in\mathbb C(T)
 \quad\Longleftrightarrow\quad
 \lambda\in\mathbb Z_{\geq0}.
 }
\tag{3.1}
\]

### Proof

The normalized trace `x=t/s` satisfies `x>2`, so the authenticated theorem
`GLO764.LOCAL_POWER_RATIONALITY` applies to `v_r`: its generating series is
rational exactly when `lambda` is a nonnegative integer.  Equation (2.7) and
the invertibility of the variable scaling transport that verdict in both
directions.  \(\square\)

This proof imports exactly one nonrationality input.  It does not repackage a
finite experiment as a new theorem.

## 4. Sharp integer denominator

### Theorem GLO764.POSITIVE_DETERMINANT_INTEGER_MINIMAL_DENOMINATOR

For `k in Z_{>=0}`, the reduced denominator of

\[
 \sum_{r\geq0}u_r^kT^r
\]

is exactly

\[
 \boxed{
 D_{k;\alpha,\beta}(T)
 =\prod_{j=0}^{k}
  \left(1-\alpha^{k-j}\beta^jT\right).
 }
\tag{4.1}
\]

The minimal eventual constant-coefficient recurrence order is `k+1`.

### Proof

Raising (1.5) to the integer power `k` gives

\[
 u_r^k
 =\sum_{j=0}^{k}
   \frac{(-1)^j\binom{k}{j}
         \alpha^{k-j}\beta^j}
        {(\alpha-\beta)^k}
   \left(\alpha^{k-j}\beta^j\right)^r.
\tag{4.2}
\]

Every coefficient is nonzero.  Consecutive characteristic roots have ratio
`beta/alpha`, which lies strictly between zero and one, so all `k+1` roots
are distinct and nonzero.  Each simple partial fraction therefore has a
nonzero residue and no denominator factor cancels.  This proves (4.1) and
minimality.  The case `k=0` reads `D=1-T`.  \(\square\)

The determinant scaling in (2.2) is visible factor by factor:

\[
 s^k a^{k-2j}=\alpha^{k-j}\beta^j.
\tag{4.3}
\]

Thus freeing the positive determinant rescales the fixed-degree symmetric
weights but does not change their count.  The quadratic filtered growth from
the separate parent packet concerns combining several degrees while the
determinant varies; it is not contradicted by the `k+1` result here.

## 5. Branch gate

### Proposition GLO764.POSITIVE_DETERMINANT_BRANCH_GATE

The transport identity (2.7) is branch-free precisely because this packet
uses the unique positive `s=sqrt(delta)`, the positive `a`, and ordinary real
logarithms of `s`, `u_r`, and `v_r`.

Choosing `-sqrt(delta)` makes the normalized sequence alternate in sign and
leaves the positive-log chamber.  For nonpositive or complex `delta`, a
square root and logarithm branch must be supplied, positivity can fail, and
the step

\[
 (s^rv_r)^\lambda=(s^\lambda)^r v_r^\lambda
\]

is not a branch-independent identity.  No classification in those chambers
is asserted here.

The coalesced boundary `t=2*sqrt(delta)` is also excluded.  There
`alpha=beta=s` and `u_r=(r+1)s^r`; it is not covered by the distinct-root
transport theorem.

## 6. Exact controls and source lock

The adjacent dependency-free producer uses exact integers and fractions.  It:

1. checks (1.5) against (1.4) for several positive rational root pairs;
2. checks the normalization `u_r=s^r v_r` when the positive square root is
   rational;
3. expands every integer power through `k=8` into the exact terms (4.2);
4. proves the stored weights are nonzero and distinct and checks recurrence
   annihilation by (4.1);
5. retains rejected equal-root, reversed-root, zero-root, and negative-root
   controls; and
6. authenticates every imported theorem packet as an exact Git object at
   commit `522493abae0f8e5526ceff4192d73b2cc617c069`.

Replay from the repository root:

    python -B research/l-families/atlas/generalized/positive_determinant_power_release.py --check
    python -B -O research/l-families/atlas/generalized/positive_determinant_power_release.py --check
    python -B -m unittest tests.test_positive_determinant_power_release
    python -B -O -m unittest tests.test_positive_determinant_power_release

The finite controls check the transport and integer algebra.  The all-complex
`lambda` nonrationality classification is inherited through (2.7) from the
authenticated source theorem, not inferred from those rows.

## 7. Structural survival ledger

| object | L0 | L1--L2 | L3 | first unresolved level |
|---|---|---|---|---|
| integer power `u_r^k` | positive-log branch independent | multiplicative when supplied primewise | exact rational local series of degree `k+1` | L4: determinant, duality, ramified and global coherence |
| noninteger positive-log power | well defined in this chamber | no primewise coherence proved | nonrational at every fixed positive semisimple parameter | L1 and L3 |
| complex or nonpositive determinant | branch data absent | not reached | not reached | L0 |

Nothing here constructs a global Euler product, ramified factors, completion,
functional equation, automorphic or motivic lift, infinite-dimensional
parent, explicit formula, or zero theory.  There is no RH or GRH consequence.

## 8. Novelty and continuation boundary

The integer-power formulas are classical recurrence algebra, and the
noninteger verdict is a literal corollary of the determinant-one packet.  No
priority or external novelty is claimed.

What remains genuinely new work is outside this packet: complex or negative
determinants with complete branch data, the coalesced/Jordan boundary,
tempered sign-changing chambers, ramified local factors, and compatibility
of determinant variation with duality and twists.
