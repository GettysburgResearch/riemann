# Original theta moments through22 in a connected positive ferromagnet

Status: **PROPOSED computer-assisted finite theorem.** An independently
reviewed exact frozen source is still required. This is not a cofinal model
construction, a new zeta zero-free boundary, or a proof of RH.

Source dependencies: #994 degree20 and its primitive at
`c93ca65a510b6acaf167f929b9bf7e67d742b05a`; #981's cofinal consumer at
`cf41f3f94a0f1df2bb503d22ab384bfc69288f33`. `INHERITED.json` records the copied
source-file paths and SHA256 identities. The only directed transcendental
backend is the unchanged pinned #994 primitive. Independent special-function
source checks, when run, are separate evidence described in the root packet.

## 1. Exact theorem and normalization

For `t>=0` write `q_n=pi*n^2` and

\[
 \Phi(t)=\sum_{n\ge1}(4q_n^2e^{9t/2}-6q_ne^{5t/2})e^{-q_ne^{2t}},
\]

extend it evenly, normalize `d rho(t)=Phi(t)dt/Z`, let `T` have this law, and
put `v=E T^2` and `T_*=T/sqrt(v)`. Every summand is positive on the half-line,
and the source has all exponential moments. The classical theta identity is

\[
 \mathbb Ee^{izT}=\xi(1/2+iz)/\xi(1/2).
 \tag{1}
\]

**Theorem T22S.** There exists a zero-field ferromagnetic Ising measure on a
connected tree with **307 vertices and306 edges**, and a nonnegative weighted
spin observable `Y`, with the following properties:

* 306 observed vertices have strictly positive observable weights; one hub has
  observable weight0.
* Every edge has a strictly positive finite coupling `J_e`, with
  `10^-11<J_e<12`.
* `E Y^(2r)=E T_*^(2r)` for `1<=r<=11`; all odd moments vanish.
* `|Y|<12` on every configuration, `Var(Y)=1`, and the entire characteristic
  function of `Y` has only real zeros.
* In the11 active coordinates specified below there is exactly one solution
  in the closed cube of radius `10^-30` about `parameters22.json`, with every
  other coordinate fixed at its stated terminating rational value.

The uniqueness assertion is confined to this specified chart and cube.
Scaling the observable by `sqrt(v)` matches the original unstandardized
theta moments through22. No higher-order equality is asserted.

## 2. Complete finite graph and its exact moment polynomial

There are17 component types with multiplicities

\[
 (m_0,m_1,\ldots,m_{16})=(256,10,1,\ldots,1).
\]

Type0 is one spin of weight `A_0`, with passive coordinates `B_0=0,p_0=1`.
Each other type is a dimer, with root/child weights

\[
 u_i=(A_i+B_i)/2,\qquad w_i=(A_i-B_i)/2,
\]

and internal edge correlation `q_i=2p_i-1`. The certified whole-cube
conditions are `A_i>|B_i|` and `1/2<p_i<1`. **The inner amplitude `B_i` may be
negative.** Its sign is retained in every odd power; both physical observable
weights nevertheless remain strictly positive.

Add one fair hub with zero observable weight and join it to every component
root with correlation `eta=10^-10`. There are256 single spins,25 dimers,
281 hub edges and25 internal edges. Hence there are307 vertices and306
edges, and the graph is connected and acyclic.

For a full spin configuration `s`, its exact probability is

\[
 2^{-307}\prod_{ab\in E}(1+q_{ab}s_as_b).
 \tag{2}
\]

Choose the hub uniformly and the edge products independently with their
stated means. On a tree this gives a bijection with all full configurations,
proving normalization of (2). Since `q=tanh J`, this is precisely the
zero-field Ising Gibbs law. No spin or edge is removed in the calculation.

Conditional on hub `+1`, every component root has mean `eta`, and all
components are independent. A dimer with root `+1` has observable value `A_i`
with probability `p_i`, and value `B_i` with probability `1-p_i`. Its exact
conditional raw moments therefore are

\[
 M_{i,0}=1,\qquad
 M_{i,n}=[p_iA_i^n+(1-p_i)B_i^n]
 \begin{cases}1&n\text{ even},\\\eta&n\text{ odd}.\end{cases}
 \tag{3}
\]

For type0 the bracket is `A_0^n`. For any raw moments `M_0=1`, cumulants and
their inverse are given by the finite triangular recurrences

\[
 K_n=M_n-\sum_{j=1}^{n-1}\binom{n-1}{j-1}K_jM_{n-j},\qquad
 M_n=\sum_{j=1}^{n}\binom{n-1}{j-1}K_jM_{n-j}.
 \tag{4}
\]

Apply (4) to (3), add the conditional cumulants with every multiplicity, and
invert (4). Averaging the hub signs preserves the resulting even moments and
sets the odd moments to0. A final (4) gives the unconditional cumulants.
`model.py` implements precisely these complete polynomial operations over
Fractions or outward intervals. Its direct-series assembly is a separately
written raw-moment multiplication of all component generating series.

The support radius is bounded by the whole-cube sum `sum_i m_i A_i<12`.
The checker bounds every correlation by `10^-11<q<1-10^-9`, so
`atanh(q)>q>10^-11` and
`atanh(q)<(1/2)log(2*10^9-1)<12`. The last elementary inequality follows
from the rational lower Taylor sum for `exp(24)` through degree24 exceeding
`2*10^9`; it is also executed in the finite controls.

## 3. Exact source equations and strict contraction

Let `c_{2r}` be the fair-sign cumulants from (4), and set

\[
 s_r=\kappa_{2r}(T_*)/c_{2r},\qquad
 B_r(z)=\kappa_{2r}(Y_z)/c_{2r},\quad1\le r\le11.
\]

These are formal moment/cumulant identities at the origin; no logarithm is
taken across unknown xi zeros. Every denominator `c_{2r}` is the explicitly
computed nonzero integer for its order. The exact source system is
`F_r(z)=B_r(z)-s_r=0`.

The flattened parameter list has51 entries `(A_i,B_i,p_i)`. The active list is

\[
 (6,0,15,21,3,27,48,9,12,5,42).
\]

The remaining40 entries are fixed. Let `c` be the terminating-rational center
and `C` the closed active cube of radius `r_0=10^-30`. The checker forms the
exact rational Jacobian `J_0=DB(c)`, its exact rational inverse `R`, and verifies
both inverse identities entry by entry.

Using newly reconstructed directed intervals for every actual `s_r`, it
computes rational upper bounds

\[
 \beta\ge\|RF(c)\|_\infty,\qquad
 L\ge\sup_{z\in C}\|I-RDB(z)\|_\infty.
\]

The accepting predicates require

\[
 L<10^{-3},\quad\beta<r_0/1000,\quad
 r_0-\beta-Lr_0>0.99r_0.
 \tag{5}
\]

The fresh accepting run gave

\[
 \beta<3.277\cdot10^{-37},\qquad L<3.075\cdot10^{-8}.
\]

`certificate22.json` contains the complete exact rational bounds and source
intervals; the checker does not read these values as mathematical premises.
The map `z -> z-RF(z)` is a strict self-contraction of `C`. Banach's theorem
therefore gives a unique fixed point in `C`, and invertibility of `R` gives
the exact source equations. The triangular identities (4) establish every
moment equality in the theorem. Mere interval overlap is diagnostic and is
not used to infer an equality or existence.

## 4. All original-theta tails are retained through22

`source_extended.py` extends the #994 six-index source protocol only by the
finite list of requested even moments. For each `n=1,...,6` it uses

\[
 U_n=(2,3/2,1,3/4,1/2,3/8)_n,
\]

with98 cells of width1/16 and degree120 Taylor density polynomials. Each
polynomial is multiplied by the exact `t^j` and integrated on its complete
cell, including the full-line factor2. The three remainder classes for
every `j=0,2,...,22` are as follows.

On the complex Cauchy circle of radius1/8 about a cell center, the density
prefactor is at most `10^11`, `Re exp(2t)>0`, the radius ratio is1/4, real
`t^j<=2^j`, and the full integration length is below16. Hence the density
Taylor error contributes at most

\[
 E_j=\frac{16\cdot10^{11}2^j}{4^{121}(3/4)}.
 \tag{6}
\]

For each of the six time tails put `q=pi*n^2`, `E=exp(2U)` and
`lambda=2qE-9/2>0`. Dropping only the negative density-prefactor term and using
`exp(2u)>=1+2u` gives the complete full-line tail

\[
 T_{n,j}=8q^2e^{9U/2-qE}
 \sum_{k=0}^j\binom jk U^{j-k}\frac{k!}{\lambda^{k+1}}.
 \tag{7}
\]

For all indices `n>=7`, consecutive positive numerator terms have ratio at
most `(8/7)^4 exp(-15pi)<1/2`, and the positive denominator increases.
The entire omitted-index tail is therefore bounded by

\[
 N_j=\frac{16\pi^2 7^4e^{-49\pi}j!}{(98\pi-9/2)^{j+1}}.
 \tag{8}
\]

Subtract (6) from the finite polynomial lower bound; add (6), all six (7),
and (8) to its upper bound. Positivity justifies this one-sided treatment of
the time/index tails. These formulas are valid for each fixed nonnegative
integer `j`; extending from20 to22 introduces no unestimated tail sector.
Divide by the enclosed positive mass and powers of the enclosed variance,
then apply (4). The complete accepting run reconstructs every primitive
interval and all these tails afresh.

The pinned primitive uses320-bit outward integer endpoints. Products,
reciprocals and squaring round outward by integer floor/ceiling. Pi comes
from Machin's identity with96-term alternating arctangent sums and first
omitted-term bounds. Exponentials use argument reduction to `[0,1/8]`,96
positive Taylor terms with a bound beginning at term97, and outward squaring;
negative arguments use outward reciprocals. This is the same imported
arithmetic backend, not an independently developed implementation.

## 5. Real zeros and scope

The classical weighted finite ferromagnetic Lee--Yang theorem applies to the
finite zero-field model with every nonnegative observable weight, including
unequal irrational weights at the actual root. If one uses its strictly
positive-weight statement, give the hub a weight `epsilon>0` and send it to0.
The finite configuration sums converge locally uniformly; their normalized
limit is1 at0. Hurwitz then preserves zero-freeness off the real axis.

The finite model's entire function has real zeros and matches the first22
theta moments. It is not identified with the theta entire function. The
#981 cofinal consumer still requires feasibility or moment convergence at
unbounded orders. The successful amplitude-zero dimer append does not prove
that this step can be repeated indefinitely.

## 6. Executed evidence

The first full accepting run completed with exit0 in58.2046seconds. Its
canonical JSON with one LF newline SHA256 was
`9ea999e723d33ebacf210862da31d154f79107c4375897b16182d97d25b3206e`.
The actual Windows CRLF file-byte SHA256 is
`48870713100c7f6e41d75c5c6b99680f373a75584c7f1609f7573ee85452c7b0`.
Input-file hashes recorded inside the certificate use actual file bytes.
The command was

```
python certify.py --emit certificate22.json
```

`python certify.py --check certificate22.json` is the fresh-source replay.
Its independent finite assembly and adversarial controls are specified in
`finite_controls.py`; actual terminal outcomes are retained in the packet's
validation receipts. A passed replay authenticates the stated finite
calculation, rather than a global RH conclusion or a review verdict.
