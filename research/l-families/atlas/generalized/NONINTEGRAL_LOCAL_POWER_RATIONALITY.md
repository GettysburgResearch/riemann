# Nonintegral local powers of a determinant-one rank-two recurrence

Status: **proposed exact local theorem; external novelty unreviewed**
Issue: [#764](https://github.com/gfreund123/riemann/issues/764)
Claim labels: GLO764.LOCAL_POWER_RATIONALITY,
GLO764.INTEGER_MINIMAL_DENOMINATOR,
GLO764.POLYNOMIAL_RECURRENCE_BOUND, and
GLO764.POLYNOMIAL_MULTIPLICATIVITY_RIGIDITY

## Scientific firewall

The theorem below lives only in the real chamber \(x>2\). In the
determinant-one rank-two normalization this is the **hyperbolic,
non-tempered** chamber: its roots are real reciprocals
\(\alpha,\alpha^{-1}\) with \(\alpha>1\). The normalized tempered
\(\mathrm{GL}_2\) trace chamber is \([-2,2]\), where the recurrence is
oscillatory and its coefficients can vanish or change sign.

Consequently, this packet proves a universal local-recurrence obstruction in
one branch-safe chamber. It does **not** prove an automorphic
nonintegral-\(\operatorname{Sym}^{\lambda}\) no-go theorem. The tempered,
oscillatory, zero, and branch-choice cases remain open here.

It also constructs no global Euler product, ramified local factors,
completion, functional equation, automorphic or motivic realization,
infinite-dimensional interpolation, explicit formula, or zero theorem.
There is no RH or GRH consequence.

## 1. Normalization and meaning of rationality

Fix a real number \(x>2\), and put

\[
\alpha=\frac{x+\sqrt{x^2-4}}{2}>1,
\qquad
\rho=\alpha^{-2}\in(0,1).
\]

Let

\[
u_0=1,\qquad u_1=x,\qquad
u_{r+2}=x u_{r+1}-u_r\quad(r\geq 0).
\]

The Binet formula is

\[
u_r
=\frac{\alpha^{r+1}-\alpha^{-(r+1)}}{\alpha-\alpha^{-1}}
=\alpha^r\frac{1-\rho^{r+1}}{1-\rho}.
\]

Thus every \(u_r\) is positive. For \(\lambda\in\mathbb C\), this packet fixes
the positive-real logarithm and defines

\[
u_r^\lambda=\exp\!\bigl(\lambda\log u_r\bigr).
\]

The series

\[
G_{\lambda,x}(T)=\sum_{r\geq0}u_r^\lambda T^r
\]

has radius of convergence \(\alpha^{-\operatorname{Re}\lambda}\). Saying
that it is rational means precisely that this analytic germ at \(T=0\)
belongs to \(\mathbb C(T)\).

## 2. Exact rationality classification

**Theorem (GLO764.LOCAL_POWER_RATIONALITY).** For each fixed real \(x>2\)
and each \(\lambda\in\mathbb C\), with the positive-real logarithm fixed as
above,

\[
G_{\lambda,x}(T)\in\mathbb C(T)
\quad\Longleftrightarrow\quad
\lambda\in\mathbb Z_{\geq0}.
\]

More precisely, for \(|T|<\alpha^{-\operatorname{Re}\lambda}\),

\[
G_{\lambda,x}(T)
=(1-\rho)^{-\lambda}
\sum_{j=0}^{\infty}
\frac{(-1)^j\binom{\lambda}{j}\rho^j}
     {1-\alpha^\lambda\rho^jT}.
\tag{2.1}
\]

If \(\lambda\notin\mathbb Z_{\geq0}\), the right side is a meromorphic
continuation with distinct actual poles

\[
T_j=\alpha^{-\lambda}\rho^{-j}
=\alpha^{2j-\lambda},
\qquad j=0,1,2,\ldots.
\tag{2.2}
\]

Here \(\alpha^\lambda=\exp(\lambda\log\alpha)\), so no additional branch is
implicit.

### Proof

From the Binet formula,

\[
u_r^\lambda
=(1-\rho)^{-\lambda}\alpha^{\lambda r}
  (1-\rho^{r+1})^\lambda .
\]

The generalized binomial theorem gives

\[
(1-\rho^{r+1})^\lambda
=\sum_{j\geq0}(-1)^j\binom{\lambda}{j}\rho^{j(r+1)}.
\tag{2.3}
\]

We first justify summing (2.3) over \(r\). Choose
\(|T|<\alpha^{-\operatorname{Re}\lambda}\), and set
\(s=\alpha^{\operatorname{Re}\lambda}|T|<1\). Then

\[
\sum_{j,r\geq0}
\left|
(1-\rho)^{-\lambda}
(-1)^j\binom{\lambda}{j}\rho^{j(r+1)}
\alpha^{\lambda r}T^r
\right|
\leq
|(1-\rho)^{-\lambda}|
\frac{1}{1-s}
\sum_{j\geq0}\left|\binom{\lambda}{j}\right|\rho^j .
\tag{2.4}
\]

The last series converges: its successive absolute ratio tends to
\(\rho<1\). Absolute convergence permits the interchange of the \(j\)- and
\(r\)-sums, and the geometric \(r\)-sum gives (2.1).

Next let

\[
\mathcal P=\{\alpha^{-\lambda}\rho^{-j}:j\geq0\}.
\]

On every compact set \(K\subset\mathbb C\setminus\mathcal P\), choose
\(J\) so large that

\[
\sup_{T\in K}|\alpha^\lambda\rho^jT|\leq\frac12
\quad(j\geq J).
\]

The corresponding tail in (2.1) is bounded uniformly on \(K\) by

\[
2|(1-\rho)^{-\lambda}|
\sum_{j\geq J}\left|\binom{\lambda}{j}\right|\rho^j .
\tag{2.5}
\]

The tail therefore converges locally uniformly on
\(\mathbb C\setminus\mathcal P\). The finitely many earlier terms are
meromorphic, so (2.1) defines a meromorphic continuation of the germ.

At \(T=T_j\), the \(j\)-th summand has residue

\[
-\frac{(1-\rho)^{-\lambda}
        (-1)^j\binom{\lambda}{j}\rho^j}
       {\alpha^\lambda\rho^j}
=-\frac{(1-\rho)^{-\lambda}
         (-1)^j\binom{\lambda}{j}}
        {\alpha^\lambda},
\tag{2.6}
\]

which is nonzero whenever \(\binom{\lambda}{j}\neq0\). For \(m\neq j\), the
\(m\)-th denominator at \(T_j\) equals

\[
1-\alpha^\lambda\rho^mT_j=1-\rho^{m-j}\neq0.
\tag{2.7}
\]

Thus all other terms are analytic there; local uniform convergence makes
their tail sum analytic there as well: choose \(M>j\) and a closed disk
\(\overline U\) around \(T_j\) so small that it contains none of the
finitely many points \(T_m\) with \(m<M\), \(m\neq j\), and so large in
index that

\[
\sup_{T\in\overline U}|\alpha^\lambda\rho^mT|\leq\frac12
\quad(m\geq M).
\tag{2.8}
\]

The same bound as (2.5) applies directly to the \(m\geq M\) tail; its
denominators have modulus at least \(1/2\) on \(\overline U\). The tail is
therefore analytic on \(U\) by uniform convergence. The remaining terms
with \(m<M\), \(m\neq j\), are finite in number and analytic at \(T_j\) by
(2.7). There is no pole cancellation.

The sequence \(\binom{\lambda}{j}\) terminates exactly when
\(\lambda\in\mathbb Z_{\geq0}\). In that case (2.1) is a finite sum of
rational functions. Otherwise every coefficient
\(\binom{\lambda}{j}\) is nonzero, the points \(T_j\) are pairwise distinct,
and the meromorphic continuation has infinitely many actual poles.

If the analytic germ at \(0\) were rational, its rational continuation and
(2.1) would agree first near \(0\), hence throughout the connected common
domain by the identity theorem. A rational function has only finitely many
poles, contradicting (2.2) and (2.6). This proves the theorem.
\(\square\)

## 3. Integer powers and the minimal denominator

Let \(k\in\mathbb Z_{\geq0}\). Formula (2.1) terminates:

\[
G_{k,x}(T)
=(1-\rho)^{-k}
\sum_{j=0}^{k}
\frac{(-1)^j\binom{k}{j}\rho^j}
     {1-\alpha^{k-2j}T}.
\tag{3.1}
\]

The characteristic roots \(\alpha^{k-2j}\), \(0\leq j\leq k\), are distinct
because \(\alpha>1\). Every partial-fraction coefficient is nonzero.
Therefore no factor cancels, and the reduced denominator is exactly

\[
D_{k,x}(T)
=\prod_{j=0}^{k}\left(1-\alpha^{k-2j}T\right).
\tag{3.2}
\]

This proves GLO764.INTEGER_MINIMAL_DENOMINATOR. Its degree is \(k+1\),
including the boundary case \(k=0\), where \(G_{0,x}(T)=(1-T)^{-1}\).

The denominator in (3.2) is the determinant-one
\(\operatorname{Sym}^k\) weight denominator. The scalar coefficient power
\(u_r^k\), however, generally has a nontrivial numerator. Exact reduction
gives the calibration defects

\[
N_{2,x}(T)=1+T,
\tag{3.3}
\]

\[
N_{3,x}(T)=1+2xT+T^2,
\tag{3.4}
\]

and

\[
N_{4,x}(T)
=(1+T)\bigl(1+(3x^2-2)T+T^2\bigr).
\tag{3.5}
\]

Expanded in ascending powers of \(T\), (3.5) has coefficient vectors in
ascending powers of \(x\)

\[
[[1],[-1,0,3],[-1,0,3],[1]].
\tag{3.6}
\]

These defects prevent the scalar Hadamard power from being silently
identified with the full symmetric-power Euler factor.

## 4. Polynomial coefficient transforms

Let

\[
\Phi(z)=\sum_{k\in S}c_kz^k\in\mathbb C[z],
\qquad c_k\neq0,
\qquad d=\deg\Phi.
\]

Using (3.1) degree by degree, the sequence \(\Phi(u_r)\) is a finite linear
combination of exponentials whose possible characteristic roots are

\[
\mathcal R_\Phi
\subseteq
\bigcup_{k\in S}
\{\alpha^{k-2j}:0\leq j\leq k\}.
\tag{4.1}
\]

Hence its generating function is rational and it satisfies a constant
coefficient recurrence of order at most

\[
|\mathcal R_\Phi|\leq2d+1.
\tag{4.2}
\]

This is GLO764.POLYNOMIAL_RECURRENCE_BOUND. Cancellation can lower the
order, so (4.2) is an upper bound, not a generic minimal-order claim.

Mixed even and odd degrees matter. If all degrees \(0,\ldots,d\) occur, the
union of possible exponent labels is

\[
\{-d,-d+1,\ldots,d-1,d\},
\tag{4.3}
\]

not merely the \(d+1\) weights of one symmetric power. In particular, the
constant term \(k=0\) supplies exponent \(0\), hence characteristic root
\(1\). Restricting to one parity gives only
\(\{-d,-d+2,\ldots,d\}\).

### Universal multiplicativity rigidity

**Lemma (GLO764.POLYNOMIAL_MULTIPLICATIVITY_RIGIDITY).** Let
\(\Phi\in\mathbb C[z]\) and \(\Phi(1)=1\). The formal identity

\[
\Phi(XY)=\Phi(X)\Phi(Y)
\quad\text{in }\mathbb C[X,Y]
\tag{4.4}
\]

holds if and only if

\[
\Phi(z)=z^m
\quad\text{for a unique }m\in\mathbb Z_{\geq0}.
\tag{4.5}
\]

**Proof.** Write \(\Phi(z)=\sum_k c_kz^k\). The left side of (4.4) is
\(\sum_k c_kX^kY^k\); the right side is
\(\sum_{i,j}c_ic_jX^iY^j\). Comparing off-diagonal monomials shows that at
most one coefficient is nonzero. If it is \(c_m\), comparing the diagonal
coefficient gives \(c_m=c_m^2\), and \(\Phi(1)=1\) forces \(c_m=1\).
Conversely every \(z^m\) satisfies (4.4). \(\square\)

This lemma is universal in two independent formal variables. It does not
classify transforms that happen to preserve multiplicativity on the values
of one fixed \(L\)-function.

## 5. Hostile controls and exact replay

The dependency-free producer declares the repository arithmetic class
EXACT_RATIONAL and performs only exact integer and rational
Laurent-polynomial, recurrence, Hankel, and formal coefficient algebra. It:

1. reconstructs \(u_r(\alpha+\alpha^{-1})\) as the Laurent polynomial
   \(\sum_{j=0}^{r}\alpha^{r-2j}\);
2. replays (3.2) and exact numerator annihilation for \(0\leq k\leq8\);
3. checks (3.3)--(3.6);
4. checks nontermination prefixes for
   \(\lambda=-1,\frac12,\frac32,-\frac32\);
5. records exact Hankel determinants through size \(5\) for \(x=3\) and
   \(\lambda=-1\), explicitly as a finite hostile control rather than an
   infinite-rank proof;
6. checks mixed-parity root unions and exhaustive small formal
   multiplicativity controls; and
7. refuses oversized or floating-point runs.

Replay from the repository root:

    python research/l-families/atlas/generalized/nonintegral_local_power_rationality.py --check
    python -O research/l-families/atlas/generalized/nonintegral_local_power_rationality.py --check
    python -m unittest tests.test_nonintegral_local_power_rationality
    python -O -m unittest tests.test_nonintegral_local_power_rationality

The finite hostile controls do not prove analytic nonrationality. The proof
is the locally uniform meromorphic continuation and actual-pole argument in
Section 2.

## 6. L0--L9 survival ledger

| Object | L0 | L1 | L2 | L3 | First stop |
|---|---|---|---|---|---|
| \(z^k\), \(k\geq0\) | defined | multiplicative on multiplicative coefficients | formal Euler product | local degree \(k+1\) | L4: numerator defect is not a full global \(\operatorname{Sym}^k\) construction |
| noninteger complex power, \(x>2\) | defined only after the positive log is fixed | no global branch coherence shown | not established | fails: infinitely many actual poles | L3 |
| polynomial \(\Phi\) | defined | universal multiplicativity iff a normalized monomial | conditional on L1 | recurrence order at most \(2\deg\Phi+1\) | L4 in general |

Levels L4--L9 respectively ask for local weight/determinant/duality and
ramified coherence; completion data; analytic continuation and functional
equation; functorial compatibilities; a realization; and a principled
explicit formula or zero theory. None is established here. The ladder is
diagnostic: survival at L3 does not imply L1.

## 7. Literature and novelty firewall

Integer powers of second-order recurrences and Hadamard closure are
classical. The source manifest records the inherited repository
normalization. The following external references mark nearby prior art:

- Pantelimon Stănică, *Generating Functions, Weighted and Non-Weighted Sums
  for Powers of Second-Order Recurrence Sequences*,
  [arXiv:math/0010149](https://arxiv.org/abs/math/0010149).
- Umberto Zannier, *A proof of Pisot's d-th root conjecture*,
  [arXiv:math/0010024](https://arxiv.org/abs/math/0010024).
- Andrea Ferretti and Umberto Zannier, *Equations in the Hadamard ring of
  rational functions*,
  [arXiv:math/0701772](https://arxiv.org/abs/math/0701772).
- Gessica Alecci, Stefano Barbero, and Nadir Murru, *Some notes on the
  algebraic structure of linear recurrent sequences*,
  [arXiv:2302.13867](https://arxiv.org/abs/2302.13867).

The first covers classical integer-power generating functions. The remaining
papers show that roots and algebraic equations in Hadamard rings have deep
existing theory. This limited search is not a priority proof. The precise
fixed-positive-branch theorem above is **external novelty unreviewed** and
requires specialist comparison before citation as new. This packet makes no novelty claim.

## 8. Excluded cases

No conclusion here is asserted for \(x=2\) (coalesced root), \(x<-2\)
(sign changes), \(|x|<2\) (oscillation and possible zeros), a differently
chosen logarithm, a recurrence with determinant parameter other than \(1\),
ramified primes, or any global automorphic family. These exclusions are
mathematical scope, not evidence that the corresponding programmes fail.
