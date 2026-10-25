# Independent review of the fourth-moment gcd-ratio component

Reviewer: `two_sign_hlc`, independently of the note's author.

**Verdict: PASS within the stated source-dependent scope.**
The final note and checker bytes below were independently authenticated,
and the checker was replayed successfully under `python -O`.
I checked the complete argument, including its coprimality inversion,
modified Euler factors, buffered pointwise estimate, common profiles,
normalizers, physical-row moments, and endpoint arithmetic. I found no
unresolved mathematical issue in that deduction. The complementary
ratio component remains open; this is not a complete inverse estimate
or a new zero-free theorem.

## Exact reviewed bytes

| File | Bytes | SHA-256 | Git blob |
|---|---:|---|---|
| `GCD_FOURTH_COMPONENT.md` | 20,400 | `375aa810def5b44673ab551528c6c10449418fdc8adc7430240c0697fc98ca6a` | `656613a66ce65b814ce19fc29b1c3f995ed43a4a` |
| `check_gcd_fourth_component.py` | 11,271 | `e9d7015d4ec514bb3f92abae255d623a650fc3ad330b3bbbbc3b97757c0cb5c6` | `61c2d006dff4d044cfc5e5eb4376a85338667d06` |

These are the current local bytes, including the author's final status-line
update. The local Git blob identifiers use the standard blob header and
content hash. No remote commit authentication is claimed by this review.

## 1. Exact coefficient and coprimality inversion

The starting point is the exact full smooth gcd return proved in
`GCD_NATIVE_COEFFICIENT.md`. The two cutoff scales may be unequal:
their product is $2D$, and their linear Heath--Brown terms vanish
on the original annulus under the conditions displayed in the new
note. The complete outer support through $8D$ is retained before
gcd grouping. In particular, reflected terms whose complete primal
sums are zero are not deleted individually.

The coefficient

\[
 C_a(P;y_1,y_2)=\sum_{(d,P)=1}\frac{A_{y_1,y_2}(ad)}{Nd}
\]

contains every original outer-product scale. The mask is the full

\[
 P_u=\operatorname{rad}(\mathfrak f_u Q_s),
\]

including the extra common puncture as well as primitive and redundant
natural zeros. This explicit definition was clarified during review.
It is required for the exact identity
\(\psi_u(k)\overline{\psi_u^*(k)}=1_{(k,P_u)=1}\).
No extra puncture mask is put on the primitive dual variable.

For an annular reduced-numerator block, the insertion

\[
 1_{(a,b)=1}=\sum_{k\mid a,b}\mu_E(k),\qquad a=kA,
 \quad b=kB'
\]

is exact. The original numerator support makes the $k$ sum finite;
the rapid dual transform permits the interchange with the dual sum.
Only squarefree $k$ survive, but neither $(A,B')=1$ nor a new
coprimality condition involving $k,A,B'$ may be retained afterward.
The kernel is a function of $NB'/NA$, so $k$ cancels from its
argument. The denominator $Na$ leaves exactly $(Nk)^{-1}$, and
the coefficient becomes $C_{kA}$.

This is the decisive algebraic improvement over freezing the dual
variable and treating $(a,b)=1$ as an arbitrary moving mask. The
modified outer polynomial is controlled as its actual arithmetic
coefficient sequence. It is not submitted to an arbitrary-coefficient
moment theorem.

## 2. Local factors and analytic continuation

On the scalar contours write

\[
 \operatorname{Re}s=\operatorname{Re}z=-\theta,
 \qquad \theta=1-\beta\in(0,1/8),
\]

and, for a prime of norm $q$, put

\[
 x=q^{-s},\quad y=q^{-z},\quad
 \Delta=(1-x/q)(1-y/q).
\]

I independently derived the three local coefficients from the exact
three-way prime allocation:

\[
 \mathfrak b_1=1,\qquad
 \mathfrak b_p=-\frac{x+y-xy/q}{\Delta},\qquad
 \mathfrak b_{p^2}=\frac{xy}{\Delta}.
\]

The $xy/q$ term has the sign imposed by the both-divisible allocation.
Coefficients with a local exponent at least three are zero. At a prime
dividing squarefree $k$, the coefficient sequence in $A$ consequently
has local factor

\[
 \mathfrak b_p+\mathfrak b_{p^2}\psi_u(p)q^{-w}.
\]

The second coefficient is not $(\mathfrak b_p)^2$, and no character
factor $\psi_u(k)$ remains outside: that factor was canceled by the
primitive conjugate value in the exact inversion.

At primes outside $kP_u$, the ordinary quadratic local polynomial
is divided only by

\[
 (1-x\psi_u(p)q^{-w})(1-y\psi_u(p)q^{-w}).
\]

These factors are nonzero in the region used. The primes dividing
$k$ are instead omitted from both reciprocal $L$-functions, with
their modified polynomials left explicit. I checked the exact
factorization (13)--(14) on the initial absolute-convergence line.
Its continuation uses no reciprocal of either
$1+\mathfrak b_pT+\mathfrak b_{p^2}T^2$ or
$\mathfrak b_p$.

This precaution is substantive. For example, at the genuine
Eisenstein prime norm $q=7$, take

\[
 x=(14+168i)/145,\qquad y=\overline{x}.
\]

Then $x+y=xy/q=28/145$, $\Delta=1$,
$\mathfrak b_p=0$, and $\mathfrak b_{p^2}=196/145\ne0$.
Moreover $1<|x|<7^{1/8}$, since
$196^4<7\cdot145^4$, so these phases are compatible with a
scalar contour having $7/8<\beta<1$.

For the correction product I checked the polynomial identity

\[
\begin{split}
 D_p(T)-(1-xT)(1-yT)
 ={}&\frac{-(x^2+xy+y^2)/q+xy(x+y)/q^2}{\Delta}T\\
 &+\frac{xy(1-\Delta)}{\Delta}T^2.
\end{split}
\]

Its two errors have magnitudes
$O(q^{2\theta-1-\sigma})$ and
$O(q^{3\theta-1-2\sigma})$, where
$\sigma=\operatorname{Re}w$. Thus absolute convergence holds for
$\sigma>2\theta$. At the buffered contour
$\sigma=a+\theta+8e$, the summability exponents are
$a+\beta+8e$ and $2a+\beta+16e$. The printed floor
$a\ge.51$ and $\beta>7/8$ leave a fixed positive margin
above one. These estimates are uniform in both scalar Mellin heights,
the row, and the deleted prime set. Omitting some factors cannot harm
the absolute upper bound.

The explicit $k$-prime polynomial costs $O_\beta(q^\theta)$
per prime. Its product is at most
$(Nk)^{\theta+\epsilon}$, uniformly on the needed strip.
Additional incomplete Euler factors are bounded by a subpower of their
radical. Since $Nk\ll B$, that radical remains a prescribed bounded
power of $U$. There is no new family of primitive zero sets and no
new density assertion hidden in these deletions.

## 3. The pointwise estimate and the common buffer

The scalar Mellin formula is exact on the original natural support.
Its row-dependent factors are
$F_{P_u}(1+s)F_{P_u}(1+z)$, whose absolute bound is a subpower
of $NP_u$ and a fixed polynomial of the two heights. The scalar
Mellin densities decay rapidly. The scalar pole at zero is canceled by
$F_{P_u}(1)=0$, as in the previously reviewed gcd note.

At a fixed $s,z$, shifting the common annular outer Mellin integral
to $\operatorname{Re}w=a+\theta+8e$ gives normalized scale

\[
 (Nk)^\theta R^{a+\theta-1/2}U^{O(e)+\epsilon}.
\]

Both reciprocal arguments have real part $a+8e$. Multiplication
by the absolute scalar cutoff weight
$(y_1y_2)^{-\theta}=(2D)^{-\theta}$ leaves, up to a fixed
constant,

\[
 D^{-\theta}(Nk)^\theta R^{\theta+\delta/2}
      =(B/D)^\theta R^{\delta/2},
 \qquad R=B/Nk,\quad\delta=2a-1.
\]

This computation is exact at the level of the scale powers. It is why
the modified $k$-prime cost does not create an extra $k$ power
outside the eventual harmonic sum. Unequal cutoffs cause no loss:
their two real Mellin powers depend only on $y_1y_2$.

I checked the height argument rather than assuming an infinite
zero-free rectangle. The two scalar frequencies, outer profile norm
height, separation frequencies, and shifted outer Mellin height all
share one previously chosen positive polynomial buffer. Their sums are
the actual $L$-arguments. The truncated horizontal integrals use
that same rectangle. External Mellin decay orders are selected after
the inherited source orders and buffer.

Outside that range the proof does not shift a reciprocal contour. The
uniform coefficient bound gives a trivial normalized estimate of scale
$(Nk)^\theta R^{\theta+1/2}$, whose excess over the buffered
bound is a fixed power of $U$. A frequency exceeding the fixed
polynomial buffer absorbs that excess into a fixed polynomial of the
frequency. Rapid external decay then supplies the integrable majorant.
All resulting orders are fixed before $U$ varies.

The later consumer may reduce its own norm-height exponent after these
new finite orders are known. That is distinct from enlarging, or
reselecting circularly, the existing source buffer. The note states
this order of choices explicitly.

Raising the pointwise bound to the fourth power and using the actual
physical-row bins gives

\[
 \sum_u w_U(u)1_{(k,P_u)=1}|Z_{u,k}(R;W)|^4
 \ll (B/D)^{4\theta}
       U^{\mathcal E_{.51}(2\log_U R)+\epsilon}
       (\text{fixed profile and height costs}).
\]

The bottom bins retain the printed floor $\delta=1/50$; no
adjustable-floor extension is used. The count includes nonsquarefree
physical rows. The $k$-dependent row restriction can be retained
and then discarded by positivity. Nonempty scales $R<1$ differ
from one only by a fixed support constant and cause no negative-scale
exponent problem.

## 4. Primitive dual, common profiles, and norm summation

After the exact coprimality inversion, restoring the fixed bad-place
zeros of the primitive dual produces no new moving coprimality mask.
The extra common puncture is already accounted for by the original
finite $e$ expansion; it is not falsely imposed on the primitive
dual. The $h$ restoration involves only the fixed bad-place set.

I independently checked the central normalization on a primitive
conductor sector $\mathcal C_u\asymp\mathcal C_*$:

\[
 \frac1{Nk}(Ne\,Nh)^{-1/2}\sqrt{N/L_0},\qquad
 L_0=\frac{\mathcal C_*R\,Ne}{D\,Nh}.
\]

There is neither a hidden $(Nk)^{1/2}$ loss nor a puncture factor
inside the primitive conductor. The row root number and primitive
values at $e,h$ are bounded row scalars.

The conductor ratio, outer ratio, and dual ratio lie in a fixed compact
profile box. Their logarithmic Fourier separation gives the actual
outer polynomial $Z_{u,k}$, an ordinary polynomial for the conjugate
original natural family, and a bounded conductor phase. Both column
profiles remain common to the row sum. The dependence of $C_{kA}$
on the row is handled by the newly proved fourth moment; only the
ordinary factor is submitted to the supplied ordinary fourth moment.

Hölder consequently gives the exponent
$[1+\mathcal E_{.51}(2\rho)]/4$ for the row norm, where
$\rho=\log_U(B/Nk)$. I checked all of the additional sums:

- The dyadic dual sum retains
  \(\sqrt{N/L_0}(1+N/L_0)^{-J}\), whose sum is uniformly
  bounded for every $L_0>0$, including $L_0<1$.
- The infinite $h$ expansion has summable $(Nh)^{-1/2}$
  mass because its prime support is fixed.
- The common puncture divisors have
  \(\sum_{e\mid Q_s}(Ne)^{-1/2}\ll U^\epsilon\).
- Conductor sectors and coherent smooth dyads cost at most logarithmic
  factors.
- Beyond a prescribed bounded-power dual length, the proof uses rapid
  transform decay and a trivial estimate. It does not extend the source
  moment to an unbounded log-length range.

Finally $\mathcal E_{.51}$ is nondecreasing, so its argument may
be enlarged from $2\rho$ to $2b$. The previously absorbed
$k$ subpowers are uniform for $Nk\ll B$. Minkowski over the
exact finite inversion therefore costs the genuine harmonic ideal sum

\[
 \sum_{Nk\ll B}(Nk)^{-1}\ll\log(2B).
\]

Squaring the row-norm bound yields precisely (25). Choosing a fixed
$\beta>7/8$ sufficiently close to $7/8$, depending on the
final epsilon and prescribed length range, gives (1). Constants may
depend on that choice; the proof makes no uniform assertion on the
boundary line $\beta=7/8$.

## 5. Exact endpoint and remaining scope

The smooth head uses the weight $\chi_0(Na/U^{7/9})$, with a
common transition from one to zero. A sharp terminal cutoff is not
inferred from the buffered proof. Coherent dyadic norms are recovered
by Minkowski, and the scalar exponent increases with the numerator
log-length.

At $b=7/9$, I checked exactly

\[
 2b-200/147=86/441>0,
 \qquad \mathcal E_{.51}(14/9)=61/42,
\]

and the gap from the printed-floor competitor is $1327/3150>0$.
The resulting exponent is

\[
 \frac{b-r}{4}+\frac{1+61/42}{2}
        =\frac{179}{126}-\frac r4.
\]

Its difference from $(1+5r)/6$ is increasing in $r$, with
derivative $13/12$. At the left endpoint $r=29/25$, its
saving is exactly

\[
 17/6300,\qquad 17/6300-1/1000=107/63000>0.
\]

Thus the uniform interval claim is established by exact arithmetic,
not a sample grid. The comparison at $b=.78$ is correctly kept
separate: its left-endpoint saving is only $1/2100$, although its
saving at the old critical length is larger.

The all-family finite-order cap, buffered density theorem, ordinary
fourth moment, and ordinary functional equation remain explicit
imported premises. I have reviewed this deduction and its use of the
previously reviewed source lemmas, not independently certified the
entire external cap proof. The new buffered argument does not extend
the older scalar-only gcd theorem to nonzero angular twists.

This is a theorem about the reduced numerator $a$, with its full
coefficient $C_a$. A further selector in the original product
changes that coefficient. The result cannot be spliced with the
original-product head or far-tail bounds without a new overlap
estimate. An appropriate saving for the complete complementary ratio
component would give the full inverse input by the triangle inequality;
that complementary estimate is not proved here.

## Checker replay

I read the checker and ran it independently under `python -O`. It passed:

- 2 generic polynomial identities after clearing the scalar denominator;
- 243 direct harmonic-gcd and modified Euler-coefficient cases;
- an exact admissible case with a vanishing first prime coefficient and
  nonzero second prime coefficient;
- 72 complete coprimality inversions with natural and extra puncture masks;
- 96 exact central-normalization identities;
- 216 fixed-divisor scale and convergence checks;
- exact endpoint, printed-floor, and uniform-margin predicates.

The deliberately incorrect inversion weight failed in 46 cases, and
removing the required divisor mask failed in 50. Other active controls
detect dropping the repeated-prime term, replacing the second prime
coefficient by the square of the first, charging only a square-root
harmonic weight, and asserting a uniform 1/1000 saving for the oversized
0.78 cutoff. Acceptance predicates use explicit exceptions and remain
active under optimization.

The local coefficients are checked in a free-prime model, and the full
phase-and-mask inversion uses an integer character model. Those tests
corroborate the exact multiplicative identities, which hold equally for
ideals; they are not numerical experiments asserting an Eisenstein
analytic theorem. The displayed critical-length decimals are labeled
as diagnostics and are not used in any acceptance predicate. The proof
of the uniform interval margin is the rational identity and monotonicity
argument above.

These finite checks do not certify the imported cap, buffered density,
ordinary fourth moment, analytic contour bounds, complementary ratio
tail, or a zero-free conclusion.
