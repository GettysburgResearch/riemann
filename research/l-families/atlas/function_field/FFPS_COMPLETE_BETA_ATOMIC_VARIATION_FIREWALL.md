# The complete beta current has unavoidable square-root atomic variation

Status: **exact complete-source signed-measure firewall; the raw Jordan
negative-mass premise is false, while the fixed-mollified analytic consumer
remains viable; RH and GRH unproved**

Bounded exact replay:
[`ffps_complete_beta_atomic_variation_firewall.py`](ffps_complete_beta_atomic_variation_firewall.py).

Read first:

1. `FFPS_SIGNED_DIFFERENTIAL_ATOMIC_SHELL_FIREWALL.md`;
2. `FFPS_EXTRA_NOTCHED_MELLIN_LANDAU_CONSUMER.md`;
3. `FFPS_MOLLIFIED_COMPLETE_SOURCE_ADAPTER.md`.

The replay pins the two analytic source blobs at the full commit
`3f10a6be2009f8e499b1bd421fd97b2095a82b06`.  The third item is contextual,
not used in the lower-bound proof, and is pinned separately at
`a970a55a11adc3d30bd98be90be12055984056ef`.

## 0. Outcome

Let

\[
 \nu_{\rm ext}
 =\sum_{n\ge1}{\beta(n)\over\sqrt n}\,\tau_nK_{\rm ext},
 \qquad
 \beta(n)=\mu(n)-1_{67\mid n}\mu(n/67),
\tag{0.1}
\]

be the **complete** duplicate-\(67\) extra-notched current.  The atomic part
of `K_ext` has coefficients

\[
 C=(5,\,-10-10\sqrt2,\,15+20\sqrt2,\,
       -20-10\sqrt2,\,10)
\tag{0.2}
\]

at ratios `1,2,4,8,16`.

For every odd `m`,

\[
 \beta(2m)=-\beta(m),\qquad \beta(4m)=0.
\tag{0.3}
\]

Grouping the atoms at one point `X=2^j m` therefore gives the six-layer
coefficient vector

\[
 B_j=C_j-{C_{j-1}\over\sqrt2}
\quad(C_{-1}=C_5=0),
\tag{0.4}
\]

namely

\[
\boxed{
B=\left(
5,\,
-10-\frac{25}{2}\sqrt2,\,
25+25\sqrt2,\,
-40-\frac{35}{2}\sqrt2,\,
20+10\sqrt2,\,
-5\sqrt2
\right).}
\tag{0.5}
\]

The positive and negative coefficient masses agree exactly:

\[
\boxed{
\sum_{B_j>0}B_j
=\sum_{B_j<0}|B_j|
=50+35\sqrt2,
\qquad
\sum_{j=0}^5|B_j|=100+70\sqrt2.}
\tag{0.6}
\]

Unique `2`-adic factorization makes all pairs `(m,j)` distinct.  Thus,
once all six layers lie below the horizon,

\[
\boxed{
\nu_{\rm ext}^-([1,Y])
\ge
(50+35\sqrt2)
\sum_{\substack{m\le Y/32\\m\ {\rm odd}}}
{|\beta(m)|\over\sqrt m}.}
\tag{0.7}
\]

The same complete groups contribute the exact atomic total variation

\[
 (100+70\sqrt2)
 \sum_{\substack{m\le Y/32\\m\ {\rm odd}}}
 {|\beta(m)|\over\sqrt m}.
\tag{0.7a}
\]

Restricting the sum to odd squarefree `m` gives

\[
\boxed{\nu_{\rm ext}^-([1,Y])\gg\sqrt Y.}
\tag{0.8}
\]

Consequently the raw premise

\[
 \nu_{\rm ext}^-([1,Y])=Y^{o(1)}
\tag{0.9}
\]

in the first form of the direct consumer is unconditionally false.  The
implication “(0.9) implies RH” remains logically correct but is vacuous as an
arithmetic target.

This does **not** invalidate the fixed positive mollifier.  After convolution,
nearby atoms and the continuous density can cancel before a negative part is
taken.  The viable analytic gate is therefore

\[
 \int_1^Y(\eta_\varepsilon*\nu_{\rm ext})_-(X){dX\over X}
 =Y^{o(1)}
\tag{0.10}
\]

for one fixed `epsilon>0`.  Its multiplier is still zero-free in the open
right half-plane, so the audited Mellin--Landau proof applies directly to
(0.10).

## 1. Exact local calculation at 2

The atomic polynomial of `K_ext` is

\[
 C(z)=5(1-z)^2(1-\sqrt2z)^2.
\tag{1.1}
\]

For odd `m`, the complete source has only the `2`-adic exponents zero and
one.  Their coefficients are

\[
 {\beta(m)\over\sqrt m},
 \qquad
 {\beta(2m)\over\sqrt{2m}}
 =-{\beta(m)\over\sqrt2\sqrt m}.
\tag{1.2}
\]

Hence the grouped atomic polynomial is

\[
\boxed{
B(z)=C(z)\left(1-{z\over\sqrt2}\right).}
\tag{1.3}
\]

Expanding (1.3) proves (0.5).  Since `C(1)=0` and the coefficient
vector alternates strictly in sign, its positive and negative masses are
equal.  Direct summation gives both the one-sided masses and the total
variation in (0.6).

The relation (0.3) follows from the definition of `beta` and
`\mu(2r)=-\mu(r)` for odd `r`; it remains true when either side vanishes.
The second equality follows because every term contains a square factor
`2^2`.

## 2. No collision can remove these atoms

Every positive integer has a unique representation

\[
 X=2^j m,\qquad m\ {\rm odd}.
\tag{2.1}
\]

Thus atoms indexed by different `(m,j)` never collide.  The non-atomic part
of `K_ext` is absolutely continuous and cannot cancel a point mass in the
Jordan decomposition.  The six positions for one odd part are
`m,2m,4m,8m,16m,32m`; hence all six occur in the endpoint-inclusive interval
`[1,Y]` exactly when `32m<=Y`.

If `beta(m)>0`, the negative layers contribute the negative mass in (0.6).
If `beta(m)<0`, the positive layers become negative and contribute the
positive mass in (0.6).  This proves the exact lower bound (0.7), independently
of the sign of every arithmetic coefficient.

## 3. Square-root growth

For odd squarefree `m`, one has `|beta(m)|>=1`.  The classical count

\[
 \sum_{\substack{m\le x\\m\ {\rm odd}}}\mu^2(m)
 ={4\over\pi^2}x+O(\sqrt x)
\tag{3.1}
\]

and partial summation give

\[
 \sum_{\substack{m\le x\\m\ {\rm odd}}}
 {\mu^2(m)\over\sqrt m}
 ={8\over\pi^2}\sqrt x+O(\log x).
\tag{3.2}
\]

Equations (0.7) and (3.2), with `x=Y/32`, prove (0.8).  More precisely, the
odd-squarefree lower comparator is

\[
 {70+50\sqrt2\over\pi^2}\sqrt Y+O(\log Y),
\tag{3.3}
\]

because `8/sqrt(32)=sqrt(2)`.  Thus the left side of (0.8) is at least the
displayed leading term minus `O(log Y)`.  The terms carrying one or two
labelled copies of `67` only increase the absolute sum and are not needed.

## 4. Consequences for the programme

The exact disposition is:

```text
raw complete Radon-measure negative mass       REFUTED: Omega(sqrt(Y))
raw deleted-shell diagonal route               REFUTED independently
fixed-mollified complete density criterion      ANALYTICALLY SUFFICIENT
mollified complete-source adapter               SEPARATE SOURCE THEOREM
mollified live one-sided estimate                OPEN / RH-BEARING
RH and GRH                                       UNPROVED
```

Any future theorem must state which convention it uses:

- **raw Jordan measure:** includes endpoint atoms and cannot satisfy a
  subpower complete-current estimate;
- **fixed positive mollification:** permits cancellation before the negative
  part and retains the off-line-zero pole;
- **endpoint-colour removal:** must move the six coefficients (0.5) into an
  explicit separate ledger and prove that ledger harmless.

No statement about zeros of an individual `L`-function is inferred from the
atomic lower bound.

## 5. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_complete_beta_atomic_variation_firewall.py --check
python -B -O research/l-families/atlas/function_field/ffps_complete_beta_atomic_variation_firewall.py --check
python -B -m unittest tests.test_ffps_complete_beta_atomic_variation_firewall
python -B -O -m unittest tests.test_ffps_complete_beta_atomic_variation_firewall
```

The replay uses exact arithmetic in `Q(sqrt(2))`.  It enumerates no prime,
source family, conductor, curve, or point.
