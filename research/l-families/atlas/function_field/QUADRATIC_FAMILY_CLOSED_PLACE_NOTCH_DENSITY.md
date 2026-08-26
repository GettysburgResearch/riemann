# Density of support-forced closed-place odd-notch zeros

Status: **EXACT FINITE COUNT** for `q in {3,5,7}` and `2 <= n <= 80`,
plus a **RIGOROUS FIXED-q ASYMPTOTIC** derived separately from the exact
factor-degree decomposition.

This packet counts a certified subset of monic primitive squarefree
closed-place conductors. It enumerates no polynomial, irreducible, finite-field
element, curve, root, or zero.

## 1. Exact question and answer

Fix an odd prime power `q` and an integer `n >= 2`, and put

\[
 M=2n-1,\qquad h=\left\lfloor{n\over2}\right\rfloor,
 \qquad L=h+1.
\tag{1}
\]

Let

\[
 Q=\prod_iP_i\in\mathbf F_q[T]
\tag{2}
\]

be monic and squarefree of degree `M`, with the `P_i` distinct monic
irreducibles. The source-locked closed-place notch theorem says

\[
 \min_i\deg P_i>h
 \quad\Longrightarrow\quad
 S_{n,Q}=0
\tag{3}
\]

exactly for the raw squarefree-family sum. Thus the first allowed factor
degree is strictly `L=h+1`, not `h`.

Write

\[
 I_q(d)={1\over d}\sum_{e\mid d}\mu(e)q^{d/e}
\tag{4}
\]

for the number of monic degree-`d` irreducibles over `F_q`. Choosing any
subset of those irreducibles contributes the local degree enumerator

\[
 (1+x^d)^{I_q(d)}.
\tag{5}
\]

Consequently the exact number of conductors certified by (3) is

\[
\boxed{
 Z_{q,n}=[x^M]\prod_{d=L}^{M}(1+x^d)^{I_q(d)}.}
\tag{6}
\]

Equivalently, exposing the degree multiset rather than coefficient notation,

\[
 Z_{q,n}=
 \sum_{\substack{m_L,\ldots,m_M\ge0\\
                   \sum_{d=L}^Mdm_d=M}}
 \prod_{d=L}^M\binom{I_q(d)}{m_d}.
\tag{6a}
\]

The strict cutoff below implies `sum_d m_d<=3`, so (6a) is also the exact
one-/two-/three-factor decomposition used in the asymptotic proof.

There are exactly

\[
 |\mathcal H_M(q)|=q^M-q^{M-1}
\tag{7}
\]

monic squarefree degree-`M` polynomials. Every one is the conductor of the
corresponding primitive quadratic character. The certified density is

\[
\boxed{
 \delta_{q,n}={Z_{q,n}\over q^M-q^{M-1}}.}
\tag{8}
\]

The denominator does not quotient by affine changes of variable, curve
isomorphisms, or twists.

Equation (6) counts exactly the conductors for which the locked theorem
forces the zero by coefficient support. It is not a converse classification:
other profiles could have zero raw sums through cancellations not detected by
this support predicate.

## 2. Bounded coefficient dynamic program

The producer starts with the truncated coefficient vector

\[
 c^{(L-1)}_0=1,\qquad c^{(L-1)}_j=0\quad(1\le j\le M).
\tag{9}
\]

For each `d=L,...,M` it applies

\[
 c^{(d)}_j=
 \sum_{0\le r\le j/d}
 c^{(d-1)}_{j-rd}\binom{I_q(d)}r,
 \qquad 0\le j\le M.
\tag{10}
\]

All entries are integers and all states above degree `M` are discarded.
The returned value is `c^(M)_M`. Formula (4) supplies the cardinality of the
degree-`d` irreducible set; no member of that set is constructed or listed.

The strict cutoff makes the computation especially small. For both parities
of `n`,

\[
 4L>M.
\tag{11}
\]

Hence every conductor in (6) has at most three irreducible factors, and each
local binomial in (10) is needed only through multiplicity three. Replacing
`d>h` by `d>=h` would change the counted set and, for odd `n`, admit
four-factor profiles. That weak-inequality mutation is explicitly tested and
rejected.

The DP replays every pair

\[
 q\in\{3,5,7\},\qquad 2\le n\le80,
\tag{12}
\]

for 237 exact calculations. Every replayed tuple
`[q,n,M,L,Z_(q,n),q^M-q^(M-1)]` enters a canonical ordered SHA-256 digest in
the JSON, so a changed numerator outside the displayed table changes the
artifact. To keep the artifact readable, the JSON expands only the
deterministic 45-row grid

```text
n = 2,...,10, 20,21, 40,41, 79,80
```

for each `q`. Each expanded row records `Z_(q,n)`, (7), the reduced fraction
(8), and the reduced fraction `M*delta_(q,n)`. The tests independently rebuild
all 237 numerators from the one-/two-/three-factor multiset formula and check
the full digest. The JSON integers and fractions are canonical; the decimal
values below are only a reading aid.

Selected scaled densities `M*delta_(q,n)`, rounded to nine decimal places:

| `n` | `M` | `q=3` | `q=5` | `q=7` |
|---:|---:|---:|---:|---:|
| 2 | 3 | 1.333333333 | 1.200000000 | 1.142857143 |
| 3 | 5 | 2.222222222 | 2.048000000 | 1.982507289 |
| 5 | 9 | 2.765432099 | 2.440396800 | 2.309591606 |
| 10 | 19 | 2.872941735 | 2.413835871 | 2.255569099 |
| 20 | 39 | 3.124280158 | 2.604005553 | 2.430419419 |
| 21 | 41 | 3.286193067 | 2.738959369 | 2.556377150 |
| 40 | 79 | 3.244254243 | 2.703546240 | 2.523309827 |
| 41 | 81 | 3.327094102 | 2.772579482 | 2.587740852 |
| 79 | 157 | 3.347220372 | 2.789350310 | 2.603393623 |
| 80 | 159 | 3.305877040 | 2.754897534 | 2.571237698 |
| limit from (14) | -- | 3.368749448 | 2.807291207 | 2.620138460 |

The adjacent even/odd rows retain a visible lower-order parity effect. This
table is only a control; the parity theorem below is proved independently by
Euler--Maclaurin expansion.

## 3. Rigorous fixed-`q` asymptotic

This section is logically separate from the finite computation. No fitted
constant or finite-row trend is used in the proof.

For every fixed odd prime power `q`, as `n` tends to infinity with `M,L` as
in (1),

\[
\boxed{
 {Z_{q,n}\over q^M}={C_0\over M}+O_q(M^{-2}),}
\tag{13}
\]

and therefore

\[
\boxed{
 \delta_{q,n}={C_0\over(1-q^{-1})M}+O_q(M^{-2}).}
\tag{14}
\]

Here

\[
\begin{aligned}
 C_0={}&1+\log3+{1\over2}\bigl((\log3)^2-(\log2)^2\bigr)\\
 &+\operatorname{Li}_2(1/3)-\operatorname{Li}_2(1/2)\\
 ={}&2.24583296562735\ldots=4\omega(4),
\end{aligned}
\tag{15}
\]

where `Li_2(z)=sum_(k>=1) z^k/k^2` on this interval and `omega` is Buchstab's
function.

### Direct proof in this threshold range

By (11), the coefficient (6) is the sum of its one-, two-, and three-factor
parts. For fixed `q`, Möbius inversion gives

\[
 I_q(d)={q^d\over d}+O_q(q^{d/2}).
\tag{16}
\]

Every participating degree satisfies

\[
 d\ge L={M\over4}+O(1).
\tag{17}
\]

After division by `q^M`, replacing the exact irreducible counts by their
leading terms, and replacing falling factorials by ordinary powers, has total
error

\[
 O_q(M^2q^{-L/2}).
\tag{18}
\]

This is smaller than every fixed negative power of `M`. The remaining
one-, two-, and three-factor contributions are

\[
 {1\over M},
\tag{19}
\]

\[
 {1\over2}
 \sum_{\substack{a+b=M\\a,b\ge L}}{1\over ab}
 ={\log3\over M}+O(M^{-2}),
\tag{20}
\]

and

\[
 {1\over6}
 \sum_{\substack{a+b+c=M\\a,b,c\ge L}}{1\over abc}
 ={A_3\over M}+O(M^{-2}),
\tag{21}
\]

respectively. These are ordinary Riemann sums on regions bounded away from
the coordinate axes; moving `L/M` from `1/4` by `O(1/M)` changes them by only
`O(M^-2)`. The constants in (20)--(21) are

\[
 {1\over2}\int_{1/4}^{3/4}{dx\over x(1-x)}=\log3
\tag{22}
\]

and

\[
\begin{aligned}
 A_3
 &={1\over6}
 \iint_{\substack{x,y\ge1/4\\1-x-y\ge1/4}}
 {dx\,dy\over xy(1-x-y)}\\
 &={1\over2}\bigl((\log3)^2-(\log2)^2\bigr)
   +\operatorname{Li}_2(1/3)-\operatorname{Li}_2(1/2).
\end{aligned}
\tag{23}
\]

Adding (19)--(23) proves (13), and the exact identity
`q^M-q^(M-1)=q^M(1-q^-1)` proves (14).

### First parity correction

The same direct decomposition gives one further rigorous term. Write

\[
 \eta=L-{M\over4}=
 \begin{cases}
  5/4,&n\text{ even }(M\equiv-1\pmod4),\\
  3/4,&n\text{ odd }(M\equiv 1\pmod4).
 \end{cases}
\tag{24}
\]

Then

\[
 {Z_{q,n}\over q^M}
 ={C_0\over M}+{D_\varepsilon\over M^2}+O_q(M^{-3}),
\tag{25}
\]

where

\[
\boxed{
 D_{\rm even}=-4(1+\log2),\qquad
 D_{\rm odd}=-{4\over3}(1+\log2).}
\tag{26}
\]

Dividing (25) by `1-q^-1` gives the corresponding correction for
`delta_(q,n)`.

Here is the boundary calculation. The exact two-factor harmonic identity and
its expansion are

\[
 {1\over2}\sum_{\substack{a+b=M\\a,b\ge L}}{1\over ab}
 ={H_{M-L}-H_{L-1}\over M}
 ={\log3\over M}+{B_\eta\over M^2}+O(M^{-3}),
\tag{27}
\]

with

\[
 B_\eta={8-16\eta\over3}.
\tag{28}
\]

For the three-factor sum, scale `a,b,c` by `M` and put

\[
 f(x,y)={1\over xy(1-x-y)}.
\tag{29}
\]

Put `alpha_M=L/M` and

\[
 D_\alpha=\{(x,y):x,y,1-x-y\ge\alpha\},\qquad
 R_M={1\over M^2}\sum_{D_{\alpha_M}\cap M^{-1}\mathbf Z^2}f(x,y).
\tag{29a}
\]

The actual triangle `D_(alpha_M)` is lattice-aligned. The inclusive
two-dimensional trapezoidal formula therefore gives

\[
 R_M=F(\alpha_M)+{1\over2M}
 \sum_{E\subset\partial D_{\alpha_M}}\int_E^{\rm lat}f+O(M^{-2}),
 \qquad F(\alpha)=\iint_{D_\alpha}f.
\tag{29b}
\]

At the limiting cutoff `alpha_0=1/4`, each of the three lattice-coordinate
edge integrals is `(32/3)*log(2)`, so the half-boundary coefficient is
`16*log(2)`. Boundary variation contributes only `O(M^-2)` to `R_M`.
Moreover `F'(1/4)=-32*log(2)`, because increasing the cutoff moves all three
edges inward. Since `alpha_M=1/4+eta/M`, expanding (29b) and then restoring
the outer factor `1/(6M)` gives

\[
 {1\over6}\sum_{\substack{a+b+c=M\\a,b,c\ge L}}{1\over abc}
 ={A_3\over M}+{B_\eta\log2\over M^2}+O(M^{-3}).
\tag{30}
\]

Equations (27) and (30), together with the exact one-factor term `1/M`,
give `D_epsilon=B_eta*(1+log(2))`, which is (26). The summands are smooth on
this closed triangle, so the aligned one- and two-dimensional
Euler--Maclaurin remainders have the displayed order. The arithmetic error
(18) is exponential and is absorbed into `O_q(M^-3)`.

As a control only, define

\[
 R_{q,n}=M^2\left({Z_{q,n}\over q^M}-{C_0\over M}\right).
\tag{31}
\]

Using the exact stored values of `Z` and only rounding the final display gives

| parity row | target | `q=3` | `q=5` | `q=7` |
|:--|--:|--:|--:|--:|
| `n=79` odd | -2.257529574 | -2.253376622 | -2.253376619 | -2.253376619 |
| `n=80` even | -6.772588722 | -6.664475255 | -6.664475254 | -6.664475254 |

These two finite rows check the predicted parity direction and scale; they are
not used to prove (25)--(26).

The leading identification `C_0=4*omega(4)` is the standard
rough-polynomial Buchstab law. Panario and Richmond study precisely the
probability that a random polynomial over a finite field has no irreducible
factor below a degree cutoff and express its first-order behavior in terms of
Buchstab's function:
[D. Panario and B. Richmond, *Analysis of Ben-Or's polynomial
irreducibility test*, Random Structures & Algorithms **13** (1998),
439--456](https://doi.org/10.1002/%28SICI%291098-2418%28199810/12%2913%3A3/4%3C439%3A%3AAID-RSA13%3E3.0.CO%3B2-U).
A sharper general first-order treatment is given by
[A. Weingartner, *On the degrees of polynomial divisors over finite fields*](https://arxiv.org/abs/1507.01920).
No novelty is claimed for the leading `4*omega(4)/M` term. The squarefree
specialization and explicit parity-sensitive `M^-2` refinement are derived
here, but no external priority is claimed for the refinement without a
comprehensive literature review. The packet contribution also includes the
exact bounded DP and its source-locked identification with the closed-place
detector's structural-zero subset.

## 4. What the zero does and does not say

The source theorem concerns

\[
 S_{n,Q}=\sum_{D\in\mathcal H_n(q)}\psi_Q(D).
\tag{32}
\]

Thus every conductor counted by (6) has an exact zero **raw family sum**. The
source packet also proves that proper-subprofile contributions can leave a
connected cumulant of size `O_(n,profile)(q^-n)`. An exact raw zero therefore
does not imply an exact connected zero.

It also does not assert a zero of an individual `L`-function, special member
zero statistics, a memberwise sign, or an arithmetic motive. The count is not
evidence for a number-field transfer, RH, or GRH.

The asymptotic statement fixes `q` and lets the conductor degree grow. It is
not an asymptotic in `q`, and its `O_q` constant is not claimed uniform as `q`
varies. The finite JSON contains only `q=3,5,7` and `n<=80`; it is not used to
prove or extrapolate (13)--(14) or (25)--(26).

## 5. Source lock and resource contract

The only imported file is the committed closed-place weight-notch JSON at
commit `9716d2261e9e7843a6c1ffffd67ee8d6756060aa`, git blob
`964935a3a936f03011366546d966ef1473c4e832`, LF-normalized SHA-256
`3a024c4661a89d57943e15af829bffd2108b063156748322bb80637eed4e332b`,
payload SHA-256
`510f35eacebfdb18d5d5c622a37c2c43c687f960e3959684949d118a7106d4b3`,
and exact byte count `21,795`. The producer reads that content through
`git show`, not from an uncommitted working-tree replacement.

The replay is capped at 237 calculations and 45 expanded rows, `M<=159`, 160
coefficient cells per row, 100,000 DP transitions per row, 8,000,000
transitions in aggregate, 65,536 output bytes, and 32,768 source bytes. A
ten-second post-build acceptance ceiling includes source locks and packet-file
hashing; it detects an over-time build after construction and is not a
preemptive process timeout. The payload records the observed transition and
state counts. Its enumeration booleans are a recorded code-path ledger, not by
themselves a proof that hidden work is absent; that boundary is supplied by
source inspection and the packet hashes. The exact count path uses integer
arithmetic only.

Run the normal and optimized checks with

```text
python -B research/l-families/atlas/function_field/quadratic_family_closed_place_notch_density.py --check
python -O -B research/l-families/atlas/function_field/quadratic_family_closed_place_notch_density.py --check
python -B -m pytest -q tests/test_quadratic_family_closed_place_notch_density.py
python -O -B -m pytest -q tests/test_quadratic_family_closed_place_notch_density.py
ruff check research/l-families/atlas/function_field/quadratic_family_closed_place_notch_density.py tests/test_quadratic_family_closed_place_notch_density.py
```

The tests independently check the one-, two-, and three-factor formulas in
small degrees, rebuild all 237 rows by a separate irreducible-count recurrence
and direct multiset decomposition, attack the strict-cutoff boundary, verify
every expanded reduced fraction and the all-row digest, check the recorded
resource ledger, and replay the canonical source and file hashes without
Python `assert` dependence.
