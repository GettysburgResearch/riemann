# Odd-notch logarithmic-depth zero firewall

Status: **rigorous growing-depth upper bound, using the standard uniform
prime-polynomial theorem in residue classes; raw detector zeros, not zeros of
an individual `L`-function**.

Exact bounded replay:
[`quadratic_family_logarithmic_depth_zero_firewall.py`](quadratic_family_logarithmic_depth_zero_firewall.py).

## 0. Outcome

Fix an odd prime power `q`.  Put

\[
 n=2h+1,\qquad M=4h+1,
\]

and, for a depth `j>=1`, set

\[
 d=h-j,\qquad r=2j+1.
\tag{0.1}
\]

Let `Z_(q,h,j)` count monic squarefree degree-`M` conductors whose least
irreducible-factor degree is exactly `d` and whose raw closed-place notch
detector vanishes.  Define

\[
 \mathcal A_r=\prod_{\deg P\le r}P,\qquad
 \ell_r=\deg\mathcal A_r=\sum_{e\le r}eI_q(e),
\tag{0.2}
\]

and

\[
 \beta_r=2^{-I_q(r)}{I_q(r)\choose\lfloor I_q(r)/2\rfloor}.
\tag{0.3}
\]

If `d>r`, then the complete layer, without a degree-profile expansion,
obeys

\[
\boxed{
 {Z_{q,h,j}\over q^M}
 \le {\beta_r\over d^2}
 \left(1+(\ell_r+1)q^{\ell_r-d/2}\right).}
\tag{0.4}
\]

The anti-concentration packet gives

\[
 \beta_r\le I_q(r)^{-1/2}
 \le \sqrt{{3r\over2}}q^{-r/2}
 =O_q(\sqrt j\,q^{-j}).
\tag{0.5}
\]

Now let `J=J(h)>=1` satisfy

\[
 \boxed{\ell_{2J+1}\le{h-J\over4}.}
\tag{0.6}
\]

Condition (0.6) itself implies `h-J>2J+1`: by (0.8), it forces
`h-J>=4ell_(2J+1)>=8q^(2J+1)/3>2J+1`.  Then

\[
\boxed{
 {1\over q^M}\sum_{j=1}^{J}Z_{q,h,j}=O_q(h^{-2})=O_q(M^{-2}).}
\tag{0.7}
\]

After division by the exact squarefree count `q^M-q^(M-1)`, the same result
holds with the constant multiplied by `(1-q^-1)^(-1)`.  Thus this genuinely
growing window contributes no additional term of order `1/M`.

Since

\[
 {2q^r\over3}\le\ell_r
 <{q^{r+1}\over q-1}\qquad(r\ge3\text{ odd}),
\tag{0.8}
\]

the safe window has logarithmic size.  In particular, for every fixed
`epsilon>0`,

\[
 J(h)\le\left({1\over2}-\epsilon\right)\log_q h
\tag{0.9}
\]

satisfies (0.6) once `h` is sufficiently large.  This is a conductor-layer
theorem, not merely summability of formal fixed-depth coefficients.

## 1. Frozen inputs and claim boundary

The replay checks the historical source blobs exactly.

| input | commit | blob |
|---|---|---|
| closed-place notch | `9716d2261e9e7843a6c1ffffd67ee8d6756060aa` | `a1b8476ddd3cad6f63ff205392426ae9c2d0829c` |
| depth phase/rough bound | `4fc8930e14eaa3863d3f3edc151c056d7d5aedce` | `01cefa8a55c9b1ae1a0b5bed9c11fe323fb6764e` |
| fixed-depth theorem | `d61323f8c269bdf114d958d6596d0d32bf793efb` | `1803cdf033710d2bbb53b83144cbf4b2ae324554` |
| fixed-depth replay | `d61323f8c269bdf114d958d6596d0d32bf793efb` | `935c3ddbef1550675384441daa679802d75636a6` |
| fixed-depth JSON | `d61323f8c269bdf114d958d6596d0d32bf793efb` | `68e17b580208e12756cc3ed9f102407e07765dfd` |
| local anti-concentration theorem | `cf7b10ef5e50693b9150996e3891da8debb6b180` | `c6c9c27417ccf9521a2b777946e09b09d9184068` |
| local anti-concentration replay | `cf7b10ef5e50693b9150996e3891da8debb6b180` | `3938f64a81e33349e7e7c9b795a018597ec36f72` |
| local anti-concentration JSON | `cf7b10ef5e50693b9150996e3891da8debb6b180` | `91086ee46dea9961cde6d740e424dcfd355761f0` |

The only analytic input is the standard function-field RH estimate for
Dirichlet characters, written in the exact normalization used in Section 4.
The theorem concerns raw family-detector zeros.  It makes no claim about an
individual `L`-function zero, RH, GRH, external priority, or depths beyond
the displayed modulus range.

## 2. Mark one least-degree prime

Every conductor in the depth-`j` layer has at least one degree-`d`
irreducible factor.  Mark one such factor and write

\[
 Q=RC,\qquad \deg R=d,
\tag{2.1}
\]

where `C` is squarefree, has degree `M-d`, and all its irreducible factors
have degree at least `d`.  A conductor with `m_d` least-degree factors is
represented by exactly `m_d` marked pairs.  Consequently counting marked
pairs is an upper bound, with no division by `m_d` required.

Fix `C`.  As `R` varies among degree-`d` primes not dividing `C`, the
factor-degree multiset of `RC` is fixed: it is the multiset of `C` with one
additional labelled degree-`d` factor.  Hence every reciprocal coefficient

\[
 a_k=[x^k]\prod_{P\mid RC}(1-x^{\deg P})^{-1}
\]

is fixed, and

\[
 a_d=m_d(C)+1\ge1.
\tag{2.2}
\]

The locked odd-notch identity is

\[
 S_{n,RC}=\sum_{k=d}^{h}a_kD_{n-2k}.
\tag{2.3}
\]

Because `r=n-2d`, the first channel is `D_r`; every channel with `k>d`
has degree strictly below `r`.  No assumption on the number of factors, and
no two-/three-/four-factor remainder, enters (2.3).

## 3. The exact zero set in residue space

Assume `d>r`.  Then no prime dividing `RC` occurs in `A_r`, so all local
character values through degree `r` are signs.  Polynomial quadratic
reciprocity in the frozen curve orientation gives, for `deg P<=r`,

\[
 \psi_{RC}(P)=\left({-RC\over P}\right).
\tag{3.1}
\]

For fixed `C`, this is a fixed sign times the quadratic sign of `R mod P`.
CRT and the equal square/nonsquare fibers in every
`(F_q[T]/P)^*` show that uniform units modulo `A_r` produce independent
uniform signs at every prime of degree at most `r`.

The coefficient-one isolation from the anti-concentration packet says

\[
 D_r=S_r+A_r^{\rm low},\qquad
 S_r=\sum_{\deg P=r}\epsilon_P,
\tag{3.2}
\]

where `A_r^low` and every lower channel depend only on signs of degrees
strictly below `r`.  Equations (2.2)--(3.2) therefore give

\[
 S_{n,RC}=a_dS_r+H_C(\epsilon_P:\deg P<r).
\tag{3.3}
\]

Conditioning on the lower signs, the zero equation asks the sum of
`I_q(r)` independent signs to take at most one prescribed value.  The
positive integer `a_d` changes divisibility of the target but not the
maximum atom.  Hence the set `E_C` of unit residue classes `a mod A_r` for
which the formal detector (3.3) vanishes satisfies

\[
\boxed{{|E_C|\over\varphi(\mathcal A_r)}\le\beta_r.}
\tag{3.4}
\]

Only primes `R` not dividing `C` correspond to squarefree conductors.  They
form a subset of the primes counted through `E_C`.  Dropping the exclusion
`R not dividing C` can only enlarge the upper bound.  Classes contributed
by an excluded `R|C` are not being asserted to represent a conductor zero;
they are merely harmless members of the residue-class majorant.

## 4. Growing-modulus prime-polynomial normalization

Let `A` be monic of degree `ell`, let `a` be a unit class modulo `A`, and
suppose no degree-`d` prime divides `A`.  Character orthogonality and the
function-field RH bound for every nonprincipal Dirichlet character give

\[
\boxed{
 \pi_q(d;A,a)
 ={I_q(d)\over\varphi(A)}+E_{d,A,a},\qquad
 |E_{d,A,a}|\le{(\ell+1)q^{d/2}\over d}.}
\tag{4.1}
\]

Here `I_q(d)`, rather than `q^d/d`, is the exact principal-character term.
One direct proof of the error uses

\[
 \left|\sum_{\deg F=d}\Lambda(F)\chi(F)\right|
 \le(\ell-1)q^{d/2}
\]

and bounds all proper prime-power terms by
`sum_(m<=d/2)q^m<3q^(d/2)/2`; the rounded constant `ell+1` in (4.1) is
valid for odd `q>=3`.

Summing (4.1) over an arbitrary set `E` of unit classes with
`|E|<=beta*phi(A)`, and using

\[
 I_q(d)\le {q^d\over d},\qquad
 \varphi(A)\le q^\ell,
\]

gives

\[
\boxed{
 \#\{R:\deg R=d,\ R\bmod A\in E\}
 \le {\beta q^d\over d}
 \left(1+(\ell+1)q^{\ell-d/2}\right).}
\tag{4.2}
\]

Apply (4.2) to `A=A_r`, `E=E_C`, and `beta=beta_r`.

## 5. Sum the complements, not the profiles

Let `R_q(N,d)` count monic squarefree degree-`N` polynomials all of whose
factor degrees are at least `d`.  The exact rough-polynomial lemma gives

\[
 R_q(M-d,d)\le {q^{M-d}\over d}.
\tag{5.1}
\]

There are at most this many possible complements `C`.  Multiplying (4.2)
by (5.1) proves (0.4).  This proof absorbs every factor-degree profile at
once and has no profile-count or asymptotic remainder depending on `j`.

If `j<=J`, then `ell_(2j+1)<=ell_(2J+1)` and `h-j>=h-J`.  Under (0.6),

\[
 \ell_{2j+1}-{h-j\over2}\le-{h-j\over4},
\tag{5.2}
\]

so the parenthesis in (0.4) is uniformly bounded and tends to one
exponentially fast.  Using (0.5),

\[
\begin{aligned}
 {1\over q^M}\sum_{j=1}^{J}Z_{q,h,j}
 &\ll {1\over(h-J)^2}
       \sum_{j=1}^{J}\sqrt j\,q^{-j}\\
 &\ll_q h^{-2}.
\end{aligned}
\tag{5.3}

This proves (0.7).

For (0.9), use

\[
 \ell_{2J+1}< {q^{2J+2}\over q-1}
 \le {q^2\over q-1}h^{1-2\epsilon}.
\tag{5.4}
\]

The right side is `o(h)`, while `J=O(log h)` and therefore `h-J~h`.
Equation (0.6) follows for sufficiently large `h`.

## 6. The genuine logarithmic barrier

The full local conditioning uses all signs of degrees below `r`.  Their
CRT modulus already has degree

\[
 \ell_{r-1}=\Theta_q(q^r),
\]

and adjoining the top-degree signs leaves `ell_r=Theta_q(q^r)`.  The
progression error in (4.2) is useful only while this exponential-in-`r`
modulus degree is smaller than the varying prime degree `d` by a fixed
margin.  Thus this method naturally stops at

\[
 q^{2j}\ll h,
\]

or `j` logarithmic in `h`.

Moment orthogonality of products of `k` degree-`r` signs when `kr<=d` does
not by itself remove this obstruction.  The right side of (3.3) is a target
depending on all lower-degree signs from the same prime `R`.  A
`k`-wise Littlewood--Offord bound for a fixed target does not apply to an
adaptively correlated target.  Abstract `k`-wise marginal information
allows such a target to equal `-a_dS_r` identically.  Conditioning it away
returns to the modulus `A_(r-1)` and the same logarithmic barrier.

This is a no-go for the present CRT/progression argument, not a theorem that
larger windows contain zeros.  A conditional small-ball theorem, a suitable
large sieve, or growing-rank monodromy could in principle go further.

## 7. Proof ledger and bounded replay

Proved:

- the marked-least-prime overcount, including the `R|C` exclusion fence;
- the exact residue-space anti-concentration (3.4) for every fixed
  complement;
- the uniform PNT-AP normalization (4.1) and subset bound (4.2);
- the whole-layer bound (0.4), with no factor-profile remainder;
- the logarithmic-window summation (0.7) and corollary (0.9);
- the precise obstruction to a marginal `k`-wise extension.

Not proved:

- a bound for depths with `ell_(2j+1)` comparable to or larger than `h-j`;
- any cancellation density in a macroscopic-depth window;
- uniform growing-rank monodromy or conditional small-ball estimates;
- a zero of an individual `L`-function, RH, or GRH.

Run:

```text
python -B research/l-families/atlas/function_field/quadratic_family_logarithmic_depth_zero_firewall.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_logarithmic_depth_zero_firewall.py --check
python -B -m unittest tests.test_quadratic_family_logarithmic_depth_zero_firewall
python -B -O -m unittest tests.test_quadratic_family_logarithmic_depth_zero_firewall
```

The replay uses exact irreducible-count arithmetic only through depth eight
and a few integer window panels.  It enumerates no polynomial, irreducible,
residue class, finite-field element, curve, point, conductor, or zero.
