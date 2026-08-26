# Odd-notch second boundary: exterior-cubic zero reduction

Status: **exact all-odd-prime-power structural theorem for odd family degree
`n>=11`; no trace-zero density theorem**.

The zeros below are zeros of the raw quadratic-family correlation sum
`S_(n,Q)`, not zeros of an individual `L`-function.

Exact replay:
[`quadratic_family_second_boundary_trace_zero_reduction.py`](quadratic_family_second_boundary_trace_zero_reduction.py)

## 0. Outcome

Let `q` be an odd prime power, let

\[
 n=2h+1,\qquad h\ge5,\qquad M=2n-1=4h+1,
\]

and let `Q` be monic squarefree of degree `M`.  On the second factor-degree
boundary

\[
 \min_{P\mid Q}\deg P=h-1,
 \tag{0.1}
\]

write `m_e` for the number of irreducible factors of degree `e`.  The exact
notch residual is

\[
 \boxed{S_{n,Q}=m_{h-1}D_3+m_hD_1.}
 \tag{0.2}
\]

Here `D_1` is odd and `D_3` is even.  Hence every raw zero has even `m_h`.
The total degree then gives a complete dichotomy:

\[
\boxed{
S_{n,Q}=0
\Longleftrightarrow
\begin{cases}
m_h=0\ \text{and}\ D_3=0, &\text{or}\\
\{\deg P:P\mid Q\}=\{h-1,h,h,h+2\}
\ \text{and}\ D_3+2D_1=0.
\end{cases}}
\tag{0.3}
\]

The multiset in the second line retains multiplicity: there are two distinct
degree-`h` prime factors.  Thus, outside one explicit four-factor profile,
the first possible accidental-zero layer is exactly the primitive
exterior-cubic character-zero condition

\[
 \boxed{D_3=0.}
 \tag{0.4}
\]

The exceptional profile itself has exact conductor count

\[
 \boxed{
 E_q(h)=I_q(h-1)\binom{I_q(h)}2I_q(h+2),}
 \tag{0.5}
\]

and therefore

\[
 E_q(h)\le
 {q^M\over2(h-1)h^2(h+2)}.
 \tag{0.6}
\]

Even if every exceptional conductor satisfied `D_3+2D_1=0`, its density
would be `O_q(M^-4)`.  The whole second boundary is
`O_q(M^-2)` by the exact layer bound.  Consequently it cannot contribute a
new `c/M` term; only the `D_3=0`, `m_h=0` branch can affect the `M^-2`
coefficient.

## 1. Frozen inputs

| source | commit | git blob | role |
|---|---|---|---|
| `QUADRATIC_FAMILY_FIRST_BOUNDARY_TRACE_ZERO_DENSITY.md` | `1205d4bed` | `f2a6be22e720be40aa19abb3405c5c8bf6b2ec63` | first boundary and fixed-layer density firewall |
| `QUADRATIC_FAMILY_NOTCH_PARITY_SIEVE.md` | `0b9f407f1` | `38f1b6e95f9a7eb6756450673ff067308886a0ff` | all-profile parity and shallow collapse |
| `QUADRATIC_FAMILY_NOTCH_DEPTH_PHASE_DIAGRAM.md` | `4fc8930e1` | `01cefa8a55c9b1ae1a0b5bed9c11fe323fb6764e` | exact depth residual and uniform layer bound |

The source identity for odd conductor degree is

\[
 S_{n,Q}=\sum_{k=1}^{h}a_kD_{n-2k},\qquad
 \sum_{k\ge0}a_kx^k=\prod_{P\mid Q}(1-x^{\deg P})^{-1}.
 \tag{1.1}
\]

No polynomial, finite-field element, curve, Frobenius class, or zero is
enumerated in this packet.

## 2. Exact residual and parity obstruction

Condition (0.1) gives `a_k=0` for `1<=k<h-1` and
`a_(h-1)=m_(h-1)`.  Since

\[
 2(h-1)>h,
\]

no sum of two positive factor degrees can contribute to `a_h`; hence
`a_h=m_h`.  The only surviving indices in (1.1) are `h-1` and `h`, proving
(0.2).

Because `h-1>=4`, every monic polynomial of degree one or three is coprime
to `Q`.  Thus

\[
 p_1=\sum_{\deg F=1}\psi_Q(F)
\]

is a sum of `q` signs and is odd, while

\[
 p_3=\sum_{\deg F=3}\psi_Q(F)
\]

is a sum of `q^3` signs and is odd.  Since `D_1=p_1` and
`D_3=p_3-qp_1`, oddness of `q` gives

\[
 \boxed{D_1\equiv1\pmod2,\qquad D_3\equiv0\pmod2.}
 \tag{2.1}
\]

Reducing (0.2) modulo two therefore yields

\[
 \boxed{S_{n,Q}\equiv m_h\pmod2.}
 \tag{2.2}
\]

This is the `j=1`, odd-`n` specialization of the general shallow parity
sieve, now paired with the exact integer residual.

## 3. Degree-budget classification

Assume `S_(n,Q)=0`.  Equation (2.2) makes `m_h` even.

If `m_h>=4`, the mandatory degree-`h-1` factor gives total degree at least

\[
 (h-1)+4h=5h-1>4h+1=M,
\]

which is impossible.  Hence `m_h` is zero or two.

If `m_h=0`, equation (0.2) is `m_(h-1)D_3`.  Its positive multiplicity
shows that it vanishes exactly when `D_3=0`.

Suppose `m_h=2` and put `r=m_(h-1)>=1`.  If `r=1`, the already prescribed
factors have degree `3h-1`, leaving degree `h+2`.  Two further factors would
have total degree at least `2h-2>h+2`, so the complement is one irreducible
factor of degree `h+2`.

If `r=2`, the prescribed degree is `4h-2`, leaving only three; this cannot
be supplied by a factor of degree at least `h-1>=4`.  If `r>=3`, the
prescribed degree already exceeds `M`.  Therefore `r=1` and the profile is
exactly `(h-1,h,h,h+2)`.  Substitution in (0.2) gives `D_3+2D_1` and proves
(0.3).

The threshold `h>=5`, equivalently odd `n>=11`, simultaneously ensures the
parity truncation and every strict degree inequality above.  Smaller rows
are not inferred from this theorem.

## 4. Counting firewall

The phase-diagram layer bound gives

\[
 \#\{Q:\deg Q=M,\ \min\deg P=h-1\}
 \le {q^M\over(h-1)^2}.
 \tag{4.1}
\]

Since there are `q^M-q^(M-1)` monic squarefree degree-`M` conductors, the
entire second-boundary raw-zero density is at most

\[
 {1\over(1-q^{-1})(h-1)^2}=O_q(M^{-2}).
 \tag{4.2}
\]

For the exceptional profile, squarefreeness and distinct degrees give (0.5).
Using `I_q(d)<=q^d/d` and `binom(I,2)<=I^2/2` proves (0.6).  For fixed `q`,
the irreducible-count formula also gives the sharper expansion

\[
 {E_q(h)\over q^M-q^{M-1}}
 ={128\over(1-q^{-1})M^4}+O_q(M^{-5}).
 \tag{4.3}
\]

This is a count of the whole exceptional profile, not of the subset obeying
the mixed trace equation.  It therefore remains a valid upper bound without
any distributional assumption.

## 5. The remaining finite-residue gate

For fixed `q`, `D_3` is a finite local residue statistic even though the
conductor degree grows.  Let

\[
 \mathcal R_{\le3}=\prod_{\substack{R\ {m monic\ irreducible}\\
                                     \deg R\le3}}R.
\]

Every conductor on (0.1) is coprime to this modulus.  Polynomial quadratic
reciprocity, with `deg Q=4h+1` fixed, rewrites every value
`psi_Q(F)=(F/Q)` for `deg F<=3` as a fixed sign times `(Q/F)`.  Consequently

\[
 \boxed{D_1\ \text{and}\ D_3\ \text{depend only on}
 Q\bmod\mathcal R_{\le3}.}
 \tag{5.1}
\]

Thus the irreducible gate is precise: determine the distribution of
second-boundary, `m_h=0` squarefree rough conductors among the invertible
residue classes modulo `R_(<=3)`.  A residue-class asymptotic with main terms
at scale `q^M/M^2` and error `o(q^M/M^2)` would turn the finite set of classes
satisfying `D_3=0` into the exact second-boundary `M^-2` constant.  No
growing-rank monodromy or broad conductor census is needed for that next
step, but the required rough-factor residue-class theorem is not proved here.

## 6. Exact replay and claim boundary

The producer enumerates only nondecreasing **degree multisets** for
`5<=h<=80`.  It verifies the coefficient reduction, parity split, and that
the only even-positive `m_h` profile is `(h-1,h,h,h+2)`.  It also evaluates
(0.5) for a small exact `(q,h)` control grid using the Möbius formula for
`I_q(d)`.  No irreducible polynomial is constructed.

Proved:

- the exact residual (0.2) and parity obstruction (2.2);
- the complete zero reduction (0.3);
- the exact exceptional-profile count and `M^-4` bound;
- the impossibility of a new second-boundary `c/M` term;
- the finite-residue reduction (5.1).

Not proved:

- existence or density of conductors with `D_3=0`;
- equidistribution of rough factor profiles in residue classes;
- a connected-cumulant zero or an individual `L`-function zero;
- RH, GRH, or an external novelty or priority claim.

Reproduce with:

~~~powershell
python research/l-families/atlas/function_field/quadratic_family_second_boundary_trace_zero_reduction.py --check
python -O research/l-families/atlas/function_field/quadratic_family_second_boundary_trace_zero_reduction.py --check
python -m unittest tests.test_quadratic_family_second_boundary_trace_zero_reduction
python -O -m unittest tests.test_quadratic_family_second_boundary_trace_zero_reduction
python -m ruff check research/l-families/atlas/function_field/quadratic_family_second_boundary_trace_zero_reduction.py tests/test_quadratic_family_second_boundary_trace_zero_reduction.py
python -m ruff format --check research/l-families/atlas/function_field/quadratic_family_second_boundary_trace_zero_reduction.py tests/test_quadratic_family_second_boundary_trace_zero_reduction.py
~~~
