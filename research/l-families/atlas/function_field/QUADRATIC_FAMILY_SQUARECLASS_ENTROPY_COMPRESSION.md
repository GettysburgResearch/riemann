# Odd-notch squareclass entropy compression

Status: **exact detector-specific Fourier compression and unconditional
growing-depth theorem; raw detector zeros, not zeros of an individual
`L`-function**.

Exact bounded replay:
[`quadratic_family_squareclass_entropy_compression.py`](quadratic_family_squareclass_entropy_compression.py).

## 0. Outcome

Fix an odd prime power `q`.  Put

\[
 n=2h+1,\qquad M=4h+1,
\]

and, for `j>=1`, set

\[
 d=h-j,\qquad r=2j+1,\qquad
 \ell_r=\sum_{e\le r}eI_q(e),\qquad
 K_r=\sum_{e\le r}I_q(e).
\tag{0.1}
\]

Assume `d>r`.  Let `Z_(q,h,j)`, `T_j`, and

\[
 \beta_r=2^{-I_q(r)}
 {I_q(r)\choose\lfloor I_q(r)/2\rfloor}
\tag{0.2}
\]

have the source-locked meanings in the profile chi-square packet.  The full
unit group modulo the small-prime primorial has about `q^ell_r` elements,
but the notch detector sees only the quadratic sign at each of the `K_r`
small primes.  Define the squareclass discrepancy `mathfrak Q_j` in
Section 2.  Then

\[
\boxed{
 Z_{q,h,j}\le T_j
 \left(\beta_r+\sqrt{\beta_r}\,\mathfrak Q_j\right)}
\tag{0.3}
\]

and the detector-specific Fourier support gives

\[
\boxed{
 \mathfrak Q_j^2
 \le C_*M^{11}(\ell_r+1)^{10}2^{K_r}q^{-M},
 \qquad C_*=614400.}
\tag{0.4}
\]

Thus the exact sufficient gate is

\[
 C_*M^{11}(\ell_r+1)^{10}2^{K_r}q^{-M}\le\beta_r.
\tag{0.5}
\]

Using `beta_r>=1/(2q^r)`, the explicit condition

\[
\boxed{
 q^{M-r}\ge
 2C_*M^{11}(\ell_r+1)^{10}2^{K_r}}
\tag{0.6}
\]

implies

\[
\boxed{
 {Z_{q,h,j}\over q^M}\le {2\beta_r\over d^2}.}
\tag{0.7}
\]

In logarithmic form, (0.6) is

\[
 M-(\log_q2)K_r
 \ge r+\log_q(2C_*)+11\log_qM+10\log_q(\ell_r+1).
\tag{0.8}
\]

This crosses the generic residue-entropy wall.  Indeed the simpler condition

\[
 \boxed{2^{2K_r}\le q^M}
\tag{0.9}
\]

implies (0.6) for all sufficiently large `M`.  It permits
`ell_r` to have order `M log M`, rather than order `M`.  Since

\[
 K_r={q^{r+1}\over(q-1)r}
 \left(1+O_q(r^{-1})\right),
\tag{0.10}
\]

the squareclass entropy boundary is

\[
 r=\log_qM+\log_q\log M+O_q(1),
\tag{0.11}
\]

an unbounded additive `log log M` extension.  For a terminal depth `J`
satisfying (0.6), all earlier depths are safe and

\[
\boxed{
 {1\over q^M}\sum_{j=1}^{J}Z_{q,h,j}=O_q(M^{-2}).}
\tag{0.12}
\]

Section 7 gives a second, more ambitious exact reduction.  Permutation
symmetry within each prime degree compresses the relevant Fourier space to
Krawtchouk orbit sums.  Merely triangle-bounding their constituent
characters recovers `2^K_r` exactly, so symmetry alone gives no further
theorem.  The normalized orbit estimate isolated there, `KRAWLS`, would
replace `2^K_r` by

\[
 R_r=\prod_{e\le r}(I_q(e)+1),\qquad
 \log_qR_r=O_q(r^2),
\tag{0.13}
\]

and would open a genuinely mesoscopic `r=Theta(sqrt M)` window.  `KRAWLS`
is a precise open bilinear-cancellation gate, not a result claimed here.

## 1. Frozen source and claim boundary

This packet locks the corrected profile bridge at commit
`c6d68eaaf3d55e9a9deffcb6e08f3cb5fcdfb7e9`.

| predecessor file | blob |
|---|---|
| `QUADRATIC_FAMILY_PROFILE_CHI_SQUARE_BRIDGE.md` | `8bf123cdc595152eda3030f13705db4df2d7f695` |
| `quadratic_family_profile_chi_square_bridge.py` | `43fdb4000656dd958d8636efd3c122ca15174cf5` |
| `quadratic_family_profile_chi_square_bridge.json` | `c8a0a340cd57332322cb36ae4f268b8aef6ab86d` |
| `test_quadratic_family_profile_chi_square_bridge.py` | `c2a0fa71c87096199bfce367793457570a451dc0` |

The only analytic input remains function-field RH for Dirichlet
characters.  This is a theorem over finite fields, not an assumption about
integer RH.  The result concerns a raw family detector and makes no claim
about an individual `L`-function zero, RH, GRH, a number-field transfer, or
external novelty.

## 2. The quadratic sign quotient

Let

\[
 \mathcal P_r=\{P:P\text{ monic irreducible},\ \deg P\le r\},
 \qquad |\mathcal P_r|=K_r,
\]

and put

\[
 \Omega_r=\{\pm1\}^{\mathcal P_r}.
\tag{2.1}
\]

Every conductor in the depth layer is coprime to
`A_r=prod_(P in P_r)P`.  Its detector coordinates are

\[
 \epsilon_P(Q)=\left({-Q\over P}\right).
\tag{2.2}
\]

CRT and the equal square/nonsquare fibers show that the map from units
modulo `A_r` onto `Omega_r` is surjective with equal fibers.  More
importantly, the locked Euler-product formula for every `D_s`, `s<=r`,
depends on the residue class only through (2.2).  The full unit residue is
therefore nuisance information.

For a nonempty factor-degree profile `lambda`, put

\[
 N_\lambda(\epsilon)
 =\#\{Q\text{ in profile }\lambda:
           (\epsilon_P(Q))_P=\epsilon\}.
\tag{2.3}
\]

The zero set `E_lambda` is a subset of `Omega_r`.  The coefficient-one
isolation of the degree-`r` signs is unchanged, so

\[
 |E_\lambda|\le\beta_r2^{K_r}.
\tag{2.4}
\]

Define

\[
\boxed{
 \mathfrak Q_j^2
 ={2^{K_r}\over T_j}
 \sum_{\lambda}{1\over T_\lambda}
 \sum_{\epsilon\in\Omega_r}
 \left|N_\lambda(\epsilon)
       -{T_\lambda\over2^{K_r}}\right|^2.}
\tag{2.5}
\]

Exactly the two Cauchy steps in the predecessor, now on `Omega_r`, give
(0.3).  No information is lost: (2.2) is the complete coordinate list used
by the detector.

## 3. Exact squareclass Fourier support

For `S subseteq P_r`, write

\[
 \chi_S(\epsilon)=\prod_{P\in S}\epsilon_P,
 \qquad
 \widehat N_\lambda(S)
 =\sum_{Q\in\lambda}\chi_S(\epsilon(Q)).
\tag{3.1}
\]

Parseval on the sign cube gives

\[
\boxed{
 \mathfrak Q_j^2
 ={1\over T_j}
 \sum_\lambda{1\over T_\lambda}
 \sum_{\varnothing\ne S\subseteq\mathcal P_r}
 |\widehat N_\lambda(S)|^2.}
\tag{3.2}
\]

Let `B_S=prod_(P in S)P`.  Up to the harmless fixed signs coming from the
minus orientation in (2.2), `chi_S(epsilon(Q))` is the quadratic Dirichlet
character `(Q/B_S)`.  It is nonprincipal for every nonempty `S` and has
conductor degree at most `ell_r`.  Thus (3.2) contains exactly `2^K_r-1`
quadratic characters, rather than every one of the roughly `q^ell_r`
characters modulo `A_r`.

This is both a quotient compression and a Fourier-support theorem: any
character of the full unit group which is not a product of the local
quadratic characters has Fourier coefficient zero against the detector
coordinates.

## 4. The profile transform bound

Fix nonempty `S`.  If the profile has multiplicities `m_e`, multiplicativity
gives

\[
 \widehat N_\lambda(S)
 =\prod_e E_{e,m_e}(\chi_{B_S}),
\tag{4.1}
\]

where `E_(e,m)` is the elementary symmetric sum over the degree-`e`
primes.  In Newton's permutation formula, an odd power of the quadratic
character is nonprincipal and an even power is principal.  The former is
bounded by function-field RH and the latter is a diagonal Newton term.
Exactly as in the predecessor,

\[
 |E_{e,m}(\chi_{B_S})|
 \le(\ell_r+1)^m q^{me/2}.
\tag{4.2}
\]

The assumption `d>r` implies every profile has at most five factors.
Consequently

\[
\boxed{
 |\widehat N_\lambda(S)|
 \le(\ell_r+1)^5q^{M/2}.}
\tag{4.3}
\]

The bound is uniform in the subset `S`; no enumeration of those subsets is
used in the replay.

## 5. Proof of the unconditional gate

The predecessor proves

\[
 |\Lambda_j|\le5M^4,\qquad
 T_\lambda\ge {q^M\over122880M^5},\qquad
 T_j\ge {q^M\over M^2}.
\tag{5.1}
\]

Insert (4.3) into (3.2), use the `2^K_r-1` nonempty subsets, and apply
(5.1).  This gives

\[
\begin{aligned}
 \mathfrak Q_j^2
 &\le {M^2\over q^M}(5M^4)
       (122880M^5q^{-M})
       2^{K_r}(\ell_r+1)^{10}q^M\\
 &=614400M^{11}(\ell_r+1)^{10}2^{K_r}q^{-M},
\end{aligned}
\]

which is (0.4).  Conditions (0.5)--(0.7) follow from (0.3),
`T_j<=q^M/d^2`, and the predecessor's lower bound
`beta_r>=1/(2q^r)`.

For fixed `M`, divide the left side of (0.6) by its right side.  Increasing
`r` decreases the numerator by a power of `q`, while both `K_r` and
`ell_r` are nondecreasing.  The ratio is therefore nonincreasing (also when
restricted to the odd values `r=2j+1`).  Thus a terminal safe depth makes
every earlier depth safe.  Moreover, (0.6) itself forces `K_r=O_q(M)`.
The lower bound `I_q(r)>=2q^r/(3r)` then gives `r=O_q(log M)`, so
`d>=h-J asymp M`.  Since `beta_r=O_q(sqrt(j)q^-j)`, summing (0.7) proves
(0.12).

## 6. Location of the new entropy wall

Condition (0.9) says `(log_q2)K_r<=M/2`.  By the lower bound
`I_q(r)>=2q^r/(3r)`, this gives `q^r<=C_qMr`.  The standing condition
`d>r` gives `r<M`; taking logarithms first yields
`r<=2log_qM+O_q(1)`, and substitution sharpens this to
`r=O_q(log M)`.  Since

\[
 \ell_r\le rK_r,
\tag{6.1}
\]

the factor `M^11(ell_r+1)^10q^r` in (0.6) is polynomial in `M` and
`log M`.  On the other hand, (0.9) gives `2^K_r<=q^(M/2)`, so after
cancelling this factor the available left side is `q^(M/2-r)`.  It
dominates that polynomial.  Hence (0.9) implies (0.6) for all sufficiently
large `M`, uniformly over every admissible `r` satisfying (0.9).

For fixed `q`, Möbius inversion gives

\[
 I_q(e)={q^e\over e}+O_q(q^{e/2}/e).
\]

Summing the geometrically dominated main terms yields (0.10).  Solving
`K_r asymp M` gives (0.11).  At this boundary
`ell_r asymp rK_r asymp M log M`, so the theorem genuinely lies beyond the
full-residue criterion `ell_r<M`.  It still has
`j/log M ->1/2`; the gain is the unbounded additive `log log M` term, not a
macroscopic-depth theorem.

The discrete sequence `K_(2j+1)` jumps geometrically.  As in the
predecessor, no claim is made that every `M` has a depth landing within the
logarithmic tolerance (0.8).

## 7. Krawtchouk orbit reduction and its exact obstruction

The detector is invariant under permutations of the primes within each
fixed degree.  Let

\[
 \mathbf k=(k_1,\ldots,k_r),\qquad
 0\le k_e\le I_q(e),
\]

and define

\[
 C_{\mathbf k}=\prod_{e\le r}{I_q(e)\choose k_e},\qquad
 \Psi_{\mathbf k}
 ={1\over\sqrt{C_{\mathbf k}}}
 \sum_{\substack{S\subseteq\mathcal P_r\\
                  |S\cap\mathcal P_e|=k_e\ \forall e}}
 \chi_S.
\tag{7.1}
\]

The `Psi_k` are an orthonormal basis for the degree-permutation-invariant
subspace of `L^2(Omega_r)`.  They are products of normalized Krawtchouk
polynomials in the degree-wise sign counts.  Put

\[
 A_\lambda(\mathbf k)
 =\sum_{Q\in\lambda}\Psi_{\mathbf k}(\epsilon(Q)).
\tag{7.2}
\]

Projecting the discrepancy onto this invariant subspace gives the smaller
exact quantity

\[
\boxed{
 \mathfrak K_j^2
 ={1\over T_j}\sum_\lambda{1\over T_\lambda}
 \sum_{\mathbf k\ne\mathbf0}|A_\lambda(\mathbf k)|^2,}
\tag{7.3}
\]

and, because every `E_lambda` is invariant,

\[
\boxed{
 Z_{q,h,j}\le T_j
 \left(\beta_r+\sqrt{\beta_r}\,\mathfrak K_j\right).}
\tag{7.4}
\]

This is an exact detector-specific reduction, not a heuristic replacement
of the sign cube by its count vectors.

There are only

\[
 R_r=\prod_{e\le r}(I_q(e)+1)
\tag{7.5}
\]

orbit coordinates.  However, applying (4.3) separately to the constituent
characters in (7.1) gives

\[
 |A_\lambda(\mathbf k)|
 \le\sqrt{C_{\mathbf k}}
      (\ell_r+1)^5q^{M/2}.
\tag{7.6}
\]

The binomial theorem now returns the entire squareclass entropy exactly:

\[
 \sum_{\mathbf k}C_{\mathbf k}
 =\prod_{e\le r}\sum_{k=0}^{I_q(e)}{I_q(e)\choose k}
 =2^{K_r}.
\tag{7.7}
\]

Therefore permutation invariance plus constituent-wise triangle bounds
cannot replace `2^K_r` by `R_r`.  This is a rigorous method no-go, not a
claim that the orbit sums themselves never cancel.

The smallest new target is

\[
\boxed{
 \sum_\lambda{1\over T_\lambda}
 \sum_{\mathbf k\ne\mathbf0}|A_\lambda(\mathbf k)|^2
 \le T_j\beta_r.}
\tag{KRAWLS}
\]

It would make (7.4) independently useful.  For scale, a uniform normalized
orbit estimate

\[
 |A_\lambda(\mathbf k)|
 \le(\ell_r+1)^5q^{M/2}
\tag{7.8}
\]

would replace `2^K_r` by `R_r` in (0.4).  Since

\[
 R_r\le2^rq^{r(r+1)/2},
\tag{7.9}
\]

such a theorem would reach, for every fixed `epsilon>0`,
`r<\left(\sqrt2-\epsilon\right)\sqrt M`, subject to `d>r`, and hence a
`J<(1/sqrt2-epsilon/2)sqrt M` notch window.  Equation (7.8) is intentionally
displayed as a moonshot normalization, not asserted.  Proving cancellation
between the quadratic conductor characters inside a Krawtchouk orbit is the
new arithmetic content required beyond (0.11).

## 8. Proof ledger and bounded replay

Proved:

- the exact quadratic sign quotient and equal-fiber map;
- the squareclass chi-square gate (0.3) and Parseval identity (3.2);
- the `2^K_r`, rather than `q^ell_r`, discrepancy theorem (0.4);
- the explicit gate (0.6), summed theorem (0.12), and squareclass half-wall
  corollary;
- the `log M+log log M` entropy boundary;
- the exact invariant Krawtchouk projection (7.3)--(7.4);
- the triangle-bound obstruction (7.7).

Not proved or claimed:

- `KRAWLS` or the normalized orbit estimate (7.8);
- a depth window larger than logarithmic order unconditionally;
- raw-zero cancellation density beyond the squareclass entropy wall;
- an individual `L`-function zero, integer RH/GRH, external novelty, or a
  number-field transfer.

Run:

```text
python -B research/l-families/atlas/function_field/quadratic_family_squareclass_entropy_compression.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_squareclass_entropy_compression.py --check
python -B -m unittest tests.test_quadratic_family_squareclass_entropy_compression
python -B -O -m unittest tests.test_quadratic_family_squareclass_entropy_compression
```

The replay uses irreducible-count arithmetic only through degree seven,
small sign cubes through four variables, and binomial-orbit ledgers through
seven variables.  It enumerates no polynomial, irreducible, residue class,
Dirichlet character, conductor, curve, point, or zero.
