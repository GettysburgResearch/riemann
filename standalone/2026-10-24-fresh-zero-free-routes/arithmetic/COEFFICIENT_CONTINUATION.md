# Continue the coefficient, not the moment order

Status: proved elementary coefficient-transfer lemmas; proposed arithmetic application.
Scope: finite Hilbert-space polynomials on squarefree ideals of one fixed number field. No new zero-free region is claimed.
Exact dependencies: the elementary extremal inequality for Chebyshev polynomials and the Baire category theorem. Arithmetic comparison uses PR #1020 at `c690f96fe6876f945398b3e2779810c563a64743`, especially `fifth-pass/PR1019_COEFFICIENT_TRANSFER_AUDIT.md` and `fifth-pass/SEXTIC_ROW_PHASE_CANCELLATION.md`.
What was actually run: exact interpolation and counterexample checks in `check_continuation.py`; these checks are not the proof of the infinite assertions.
Smallest remaining gap: a power-saving estimate for a positive-measure continuum of softened coefficients, on the same rows, masks, profiles, and rectangle as the desired inverse consumer.

## 1. Why this changes the question

The most recent sextic theorem controls a column with coefficient
`mu(n) gamma_2(n) theta(n)`. The actual first Poisson transform of the raw
inverse instead contains `gamma_2(n) alpha(n)^(-1) conjugate(G(n))` after
conjugation. The extra Mobius factor is not a harmless unitary change of
the input vector: the arithmetic theorem is not an arbitrary-coefficient
operator estimate.

Introduce a real or complex coefficient parameter

\[
 F_{A,B}(z)=\sum_{\substack{n\ {\rm squarefree}}}
       \mu(n)z^{\omega(n)}v_{A,B,n},                 \tag{1}
\]

where the vectors `v` contain the Gauss factor, character rows, common
profiles, all natural zeros, and every fixed arithmetic multiplier.
The row norm is part of the Hilbert space, not changed with `z`.
At `z=1` this is the known coefficient. At `z=-1` the Mobius factor
disappears exactly, because `mu(n)(-1)^omega(n)=1` on squarefree support.

The key fact is that (1) has **sublogarithmic degree in the column
length**. Therefore extrapolation over any fixed distance in `z` costs
only a subpower of that length. A whole real interval of softened
coefficients would transfer the same exponent to the missing coefficient.
Uniform constants in the interval are not required in the final theorem.

## 2. The degree bound

Fix a number field of degree `d` and a fixed `c>=1`. Suppose all ideals in
(1) have norm at most `cB`, `B>=2`. Put

\[
 r_B=\max\{\omega(n):Nn\le cB\}.
\]

Then

\[
 r_B=O_{d,c}\!\left(\frac{\log(2B)}{\log\log(3B)}\right).
                                                               \tag{2}
\]

Indeed, at most `d` prime ideals lie above a rational prime. The number
of prime ideals of norm at most `y` is consequently at most `d floor(y)`.
If `q_1<=...<=q_r` are the norms of distinct prime ideals, then
`q_j>=j/d`, and

\[
 Nn\ge\prod_{j=1}^r q_j\ge r!/d^r.
\]

The elementary bound `log(r!)>=r log r-r` implies (2). In particular,
for every fixed `C>1` and every `epsilon>0`,

\[
 C^{r_B}\ll_{C,d,c,\epsilon}B^\epsilon.             \tag{3}
\]

Squarefree support matters. The unrestricted degree `Omega(n)` can be
as large as a constant times `log B`, which would give a power cost.

## 3. Hilbert-valued Chebyshev transfer

**Lemma 1.** Let `P` be a polynomial of degree at most `r`, with values in
a complex Hilbert space. Let `I=[a,b]`, `a<b`, and let `z_0` be real and
outside `I`. Put

\[
 x_0=\frac{2z_0-a-b}{b-a}.
\]

Then

\[
 \|P(z_0)\|\le |T_r(x_0)|\sup_{z\in I}\|P(z)\|.    \tag{4}
\]

Here `T_r` is the usual Chebyshev polynomial. For `I=[1,2]` and
`z_0=-1`,

\[
 \|P(-1)\|\le T_r(5)\sup_{1\le z\le2}\|P(z)\|,
 \qquad T_r(5)\le(5+\sqrt{24})^r<10^r.              \tag{5}
\]

**Proof.** If `P(z_0)=0`, there is nothing to prove. Otherwise take the
unit vector in its direction and choose the phase of the associated
linear functional so that its value at `z_0` is positive real. The real
part of that functional applied to `P(z)` is a real scalar polynomial
on the real axis. Its absolute value on `I` is at most the displayed
supremum, and its value at `z_0` is `||P(z_0)||`. Apply the scalar
Chebyshev extremal inequality after the affine change from `I` to
`[-1,1]`. The elementary formula
`T_r(x)=((x+sqrt(x*x-1))^r+(x-sqrt(x*x-1))^r)/2` proves (5).
For completeness, the scalar extremal inequality follows by comparing
with a multiple of `T_r` and using the alternating extrema at
`cos(j pi/r)`: a strictly larger value outside the interval would force
at least `r+1` distinct real roots of a nonzero polynomial of degree at
most `r`. QED.

The statement applies to finite or infinite row spaces as long as each
coefficient vector has finite norm. Only the column sum is finite.

**Lemma 1b (positive-measure coefficient sets).** Let `E` be a measurable
subset of a bounded real interval `I`, of Lebesgue measure `m>0`. If
`P` has degree at most `r>=1`, then for any fixed **complex** `z_0`,

\[
 \|P(z_0)\|\le
       \left(\frac{8eM}{m}\right)^r
                    \sup_{z\in E}\|P(z)\|,
 \qquad M=\max_{x\in I}|z_0-x|.                    \tag{5b}
\]

**Proof.** Choose `r+1` points of `E` separated by at least
`delta=m/[2(r+1)]`. A greedy choice works: after `r` choices the open
intervals of radius `delta` around them remove measure at most
`2r delta<m`, so another point remains. Order the points
`x_0<...<x_r`. In the Lagrange formula the `j`th denominator has
absolute value at least `delta^r j!(r-j)!`, and its numerator at `z_0`
has absolute value at most `M^r`. The triangle inequality therefore
gives the coefficient mass bound

\[
 (M/\delta)^r\sum_{j=0}^r\frac1{j!(r-j)!}
       =(M/\delta)^r\frac{2^r}{r!}
       \le(8eM/m)^r,
\]

using `r!>=(r/e)^r` and `(r+1)/r<=2`. This proves (5b). Degree zero
is immediate. QED.

**Quantitative shrinking-window version.** Suppose instead the available
uniform interval is `[1-eta_B,1]`, with `0<eta_B<=1`, and the desired
target is `-1`. Then the transformed target has absolute coordinate
`4/eta_B-1`, and (4) gives

\[
 \|P(-1)\|^2\le(8/\eta_B)^{2r_B}
           \sup_{1-\eta_B\le z\le1}\|P(z)\|^2.     \tag{5a}
\]

Thus a fixed interval is unnecessary if one can prove a **uniform**
bound on these varying intervals and

\[
 \log(1/\eta_B)=o(\log\log B).
\]

For example `eta_B=1/log log B` (with harmless bounded-length
modifications) still costs only `B^o(1)`. For `eta_B=(log B)^(-c)`, the
cost is at most `B^(2c+o(1))`; here one uses the sharper consequence of
the factorial argument, `r_B<=(1+o(1)) log B/log log B` for each fixed
field. A shrinking interval does not follow from the fixed-point
estimate at `z=1`, and Baire alone does not supply this uniform
varying-interval hypothesis.

## 4. Pointwise constants suffice

Here is the version that makes an actual research target less demanding.

**Theorem 2 (continuum transfer).** Consider any collection of pairs
`(A,B)`, with `A>=1`, `B>=2`, and Hilbert-valued polynomials (1) of degree
at most `r_B`. Let `Q(A,B)>0`. Suppose that on a nondegenerate compact
real interval `I`, for each real `z in I` and each `epsilon>0`,

\[
 \|F_{A,B}(z)\|^2
       \le C_{z,\epsilon}(AB)^\epsilon Q(A,B)        \tag{6}
\]

for **all** admissible pairs `(A,B)`. The constants may depend
arbitrarily on `z`. Then for every fixed real `z_0`,

\[
 \|F_{A,B}(z_0)\|^2
       \ll_{z_0,\epsilon}(AB)^\epsilon Q(A,B).       \tag{7}
\]

**Proof.** Fix a requested final loss `epsilon>0`, and use (6) at loss
`epsilon/2`. For positive integers `m`, define

\[
 E_m=\{z\in I:\ \|F_{A,B}(z)\|^2
        \le m(AB)^{\epsilon/2}Q(A,B)
        \text{ for every admissible }(A,B)\}.
\]

Each `E_m` is closed: it is an intersection of closed subsets of `I`,
since each polynomial is continuous in `z`. Their union is `I` by the
pointwise hypothesis. The Baire category theorem implies that some
`E_m` contains a nondegenerate subinterval `J`. If `z_0 in J`, the
result follows immediately. Otherwise Lemma 1 applies on `J`. Its
constant is at most `C_J^(2r_B)` after squaring, hence at most a constant
times `B^(epsilon/2)` by (3). Since `A>=1`, (7) follows. QED.

No convergence of `F` as `B` grows, no bound for derivatives in `z`, and
no arithmetic independence of the rows is assumed. In particular the
argument cannot lose a row mask, a common twist, or a small-conductor
sector: they remain in the same vectors on both sides.

**Positive-measure strengthening.** In Theorem 2 it is enough that (6)
hold for each `z` in a measurable positive-measure subset `E` of `I`;
the target `z_0` may then be any fixed complex number. Intersect the
closed sets `E_m` with `E`. They cover `E`, so at least one has positive
measure, by countable subadditivity. On that subset the normalized
bound is uniform. Apply Lemma 1b, whose fixed constant raised to
`2r_B` is again subpower. This is a direct measure-theoretic proof and
does not require that the uniform subset contain an interval. In
particular an almost-everywhere-in-`z` arithmetic estimate is enough.

**Corollary 3 (variable positive saving).** Restrict to a fixed-power
range `1<=A<=B^C`, with fixed `C`. Suppose for each `z in I`
there is some `eta_z>0` such that, for every `epsilon>0`,

\[
 \|F_{A,B}(z)\|^2
       \ll_{z,\epsilon}(AB)^\epsilon
             B^{-\eta_z}Q(A,B).
\]

Then there is some `eta>0` for which the same bound, with `eta` in place
of `eta_z`, holds at any prescribed fixed real `z_0`.

To prove this, for each `z` first choose the input loss smaller than
`eta_z/[2(C+1)]`. Since `(AB)^epsilon<=B^((C+1)epsilon)`, this gives a
bound `C_z B^(-eta_z/2)Q` with no remaining small-loss factor. Use the
countable closed cover indexed by a constant bound `m` and an integer
`k` with saving `1/k`; Baire supplies a common subinterval and one fixed
positive saving. Spend half that saving on Chebyshev's subpower factor.
The fixed-power range, or an equivalent normalization of the saving by
total complexity, is necessary for this argument.

**Corollary 4 (arbitrarily small coefficient perturbations).** It is
enough that for every sufficiently small fixed `delta>0`, each `z` in
some nondegenerate interval inside `(1,1+delta)` has a bound with
`Q(A,B) B^(C delta+epsilon)`, where `C` is fixed. Choose `delta` after
the requested final exponent loss and apply Theorem 2. Thus an
exponent loss tending to zero with the size of the perturbation would
transfer the unperturbed exponent.

## 5. Centered moments can be continued too

For real `z`, the full moment

\[
 J_{A,B}(z)=\|F_{A,B}(z)\|^2
\]

is a real polynomial of degree at most `2r_B`. Its genuine diagonal is
also such a polynomial:

\[
 D_{A,B}(z)=\sum_n z^{2\omega(n)}\|v_{A,B,n}\|^2.
\]

Consequently the **signed centered quantity** `J(z)-D(z)` satisfies the
same continuum-transfer theorem using the scalar Chebyshev inequality
and degree `2r_B`. A common bound on `|J(z)-D(z)|` transfers without
first replacing the difference by an upper bound on `J(z)`.

More generally any fixed bilinear pair of these coefficient vectors,
or any fixed bounded row operator applied to them, gives a polynomial
of degree at most `2r_B` on the real axis. This includes an explicitly
fixed subtraction of a principal-frequency projection. The projection
must be the same for every `z`; a `z`-dependent unproved projection
identity is not licensed by this observation.

This distinction is important for the inverse application. A positive
`A+B` estimate alone can leave the dual diagonal too large. Continuing
a complete centered estimate could retain cancellation that an
uncentered norm bound discards. The resonant angular type `-1` and the
complete divisor/row reassembly still need their actual arithmetic
proofs.

## 6. Why all fixed integer divisor orders do not suffice

Let `r(B)=floor(sqrt(log B))` and

\[
 P_B(z)=B^E\prod_{j=1}^{r(B)}(1-z/j).                \tag{8}
\]

For each fixed positive integer `K`, `P_B(K)=0` for all sufficiently
large `B`. But

\[
 P_B(-1)=B^E(r(B)+1).
\]

Its degree is `o(log B)`, and on every fixed compact set in the complex
plane it has the bound `B^(E+o(1))`: use
`prod(1+|z|/j)<=exp(|z| sum 1/j)`.
Thus even arbitrarily strong eventual estimates at **every fixed
positive integer** do not transfer to `-1`. The counterexample concerns
the interpolation logic; it is not an arithmetic counterexample for
Gauss sums. Multiplying (8) by `z` also enforces a zero at `z=0`, as
occurs for an annular source with no unit-ideal column, without changing
the conclusion at `z=-1` or the sublogarithmic degree.

There is also an exact finite interpolation formula at the integer
nodes `1,...,r+1`:

\[
 P(-1)=\sum_{j=1}^{r+1}(-1)^{j-1}
       j\binom{r+2}{j+1}P(j),                       \tag{9}
\]

and the absolute coefficient mass is

\[
 \sum_{j=1}^{r+1}j\binom{r+2}{j+1}
       =r2^{r+1}+1.                                \tag{10}
\]

This formula is exact and has subpower interpolation cost at `r=r_B`.
However it demands estimates **uniform in a growing divisor order**
`K<=r_B+1`, including the growth of their coefficient energies,
constants, and analytic losses. The existing fixed-order theorems do
not give that. At such growing `K`, even the diagonal can be far larger
than a subpower, so (9) is a separate research option, not a completed
adapter.

## 7. Concrete next arithmetic target

For the actual sextic row vectors, prove an estimate on a nondegenerate
interval, or just a measurable positive-measure set, of real `z` for

\[
 \mu(n)z^{\omega(n)}\gamma_2(n)\theta(n),
\]

with the exact same moving masks and angular order as the raw inverse
after Poisson. Prefer a centered estimate, and isolate its principal
frequency part before continuing. Theorem 2 will then do the
coefficient transfer, with no additional fixed power loss.

The proposed fractional extension is not a formal consequence of the
integer case. `FRACTIONAL_ZERO_DETECTOR.md` identifies its exact
branch-point content and distinguishes a fixed-row obstruction from
what may still be possible in a family mean.

The cleaner direct application is in `DIRECT_NATIVE_APPLICATION.md`:
start from `mu^2 z^omega` without any Gauss factor, and evaluate at
`z=-1` to recover the original native Mobius inverse itself.
