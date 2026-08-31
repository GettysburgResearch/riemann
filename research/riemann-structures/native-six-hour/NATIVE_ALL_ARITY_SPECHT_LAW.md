# All-arity irreducible characters of the native curvature source

This proof concerns the actual polynomial curvature carrier for a fixed
number of independent schedule variables. It does not identify their
permutation action with an arithmetic Galois action, Boolean Walsh
characters, or a symmetry of the fixed-prime physical metric.

The exact source sequence is proved in
NATIVE_S3_CURVATURE_ISOTYPES.md at
cb9278bec3844cc3fd8072987a6890f1df32a368. Its notation is

\[
 V_r=\operatorname{span}\{u^a:a\in\{0,1\}^r\},\qquad
 B_r=\bigoplus_i\operatorname{span}\{u^{d-e_i}du_i:
                    d_i=1,\ d_j\in\{0,1,2\}\ (j\ne i)\},
\]
\[
 W_r=\operatorname{im}(f\wedge g\mapsto2\,df\wedge dg),\qquad
 0\longrightarrow V_r/\mathbb Q\overset d\longrightarrow B_r
       \overset d\longrightarrow W_r\longrightarrow0.       \tag{1}
\]

All statements below are over characteristic zero. The tools are the
classical Schur--Weyl decomposition and the ordinary one-box branching
rule for symmetric groups; the new input to which they are applied is
the specified native quotient (1). No computational discovery or
numerical census is claimed in this note.

For the imported tensor decomposition and dimension formula, see
Etingof et al., [Introduction to Representation Theory, Corollary
5.19.2 and Theorem 5.22.1](https://math.mit.edu/~etingof/representationtheorybook.pdf).
For the symmetric-group branching rule, see Okounkov and Vershik,
[A New Approach to the Representation Theory of the Symmetric Groups,
II](https://arxiv.org/abs/math/0503040). The source identifications,
multiplicity specialization and consequences below are derived here.

## 1. A closed multiplicity formula

Write \([\lambda]\) for the Specht representation of \(S_r\), for a
partition \(\lambda\vdash r\). Put \(s_q(\lambda)=\dim\mathbb S_\lambda
\mathbb Q^q\), taking it to be zero if \(\lambda\) has more than \(q\)
rows. The empty partition has dimension one. If \(\mu\nearrow\lambda\)
means that \(\mu\) is obtained by removing one removable corner, then

\[
 \boxed{\displaystyle
 [W_r:[\lambda]]=
     \sum_{\mu\nearrow\lambda}s_3(\mu)
        -s_2(\lambda)+\mathbf1_{\lambda=(r)}.}              \tag{2}
\]

Each distinct predecessor partition occurs once. In particular, equal
row lengths must not be treated as multiple removable corners.

To prove (2), identify a monomial in \(V_r\) with its binary exponent
word. Permuting coordinates permutes tensor factors, giving
\(V_r\cong(\mathbb Q^2)^{\otimes r}\) as an \(S_r\)-module. The
summand of \(B_r\) whose differential index is \(r\) has a ternary
exponent word on the other coordinates. Its stabilizer is \(S_{r-1}\),
and the \(r\) differential-index summands are permuted transitively.
Thus

\[
 B_r\cong\operatorname{Ind}_{S_{r-1}}^{S_r}
                    (\mathbb Q^3)^{\otimes(r-1)}.          \tag{3}
\]

There is no sign twist in (3): this is a single differential index,
and coordinate permutations send \(du_i\) to \(du_{\sigma(i)}\).
Schur--Weyl decomposition gives multiplicities \(s_2(\lambda)\) in
the binary tensor power and \(s_3(\mu)\) in the ternary one. Induction
adds one box by the branching rule. Taking multiplicities in (1)
subtracts the binary power and restores its constant line, proving
(2). Nonnegativity follows from the actual quotient (1), rather than
from a numerical check of this subtraction.

The dimensions in (2) are explicit. For partitions padded with zeros,

\[
 s_2(a,b)=a-b+1,\qquad
 s_3(a,b,c)=\frac{(a-b+1)(a-c+2)(b-c+1)}2.                 \tag{4}
\]

These are the usual Weyl dimension formulas. Formula (2), with (4)
and the removable-corner rule, determines every irreducible multiplicity
for every arity without constructing an exponentially large matrix.

## 2. Four-row support and distinguished sectors

Every predecessor contributing positively in (2) has at most three
rows. Consequently

\[
                  [W_r:[\lambda]]=0\quad
                       \text{if }\ell(\lambda)>4.          \tag{5}
\]

This bound is sharp at every \(r\ge4\). For
\(\lambda=(r-3,1,1,1)\), only removal of the bottom corner leaves at
most three rows. Formula (4) gives

\[
 [W_r:[r-3,1,1,1]]=s_3(r-3,1,1)
                         =\binom{r-2}{2}>0.              \tag{6}
\]

For \(r=4\) the shape is \((1,1,1,1)\), with just its bottom removable
corner; the same formula applies. There is no subtraction term from
the binary tensor power for these four-row shapes.

Three familiar sectors also admit closed formulas:

\[
 \begin{aligned}
 [W_r:\mathbf1]&=\binom r2 &&(r\ge1),\\
 [W_r:\operatorname{sgn}]&=\binom3{r-1}-\binom2r
                                                    &&(r\ge2),\\
 [W_r:[r-1,1]]&=\frac{(r-1)(3r-2)}2 &&(r\ge2).
 \end{aligned}                                           \tag{7}
\]

For the invariant sector, the sole predecessor is \((r-1)\), so the
calculation is \(\binom{r+1}{2}-(r+1)+1=\binom r2\).
For the sign sector, the predecessor is \((1^{r-1})\), and exterior
powers of \(\mathbb Q^3\) and \(\mathbb Q^2\) give the second line.
Binomial coefficients outside their range are zero. The ordinary sign
multiplicity is therefore \(2,3,1,0,0,\ldots\) at arities
\(2,3,4,5,6,\ldots\). It is absent at every arity at least five.

For \(r\ge3\), the standard shape has predecessors \((r-1)\) and
\((r-2,1)\). Their ternary dimensions are \(\binom{r+1}{2}\) and
\(r(r-2)\), while the binary dimension of \((r-1,1)\) is \(r-1\).
Their difference gives the third line. At \(r=2\), the standard shape
is the sign shape and its sole predecessor gives \(3-1=2\), also
agreeing with the formula. At \(r=1\), \(W_1=0\); its coincident
trivial/sign conventions are kept separate from the stated ranges.

Absence of the ordinary sign representation at high arity does not say
that signed arithmetic cancellation vanishes. That would identify
different operations and different group actions.

## 3. Two complete higher-arity decompositions

For four variables, (2) gives the following complete table.

| Partition | Specht dimension | Multiplicity in \(W_4\) |
|---|---:|---:|
| \((4)\) | 1 | 6 |
| \((3,1)\) | 3 | 15 |
| \((2,2)\) | 2 | 7 |
| \((2,1,1)\) | 3 | 9 |
| \((1,1,1,1)\) | 1 | 1 |

The ternary dimensions at size three are \(10,8,1\), at shapes
\((3),(2,1),(1,1,1)\). Induction gives multiplicities
\(10,18,8,9,1\); subtracting binary multiplicities \(5,3,1,0,0\)
and restoring the constant gives the table. Its weighted dimension is
\(6+45+14+27+1=93=4\cdot3^3-2^4+1\).

For five variables, the complete nonzero table is

| Partition | Specht dimension | Multiplicity in \(W_5\) |
|---|---:|---:|
| \((5)\) | 1 | 10 |
| \((4,1)\) | 4 | 26 |
| \((3,2)\) | 5 | 19 |
| \((3,1,1)\) | 6 | 18 |
| \((2,2,1)\) | 5 | 9 |
| \((2,1,1,1)\) | 4 | 3 |

The remaining partition \((1^5)\) has multiplicity zero. The ternary
dimensions at size four are \(15,15,6,3\), at shapes
\((4),(3,1),(2,2),(2,1,1)\). Applying the same one-box rule and
subtracting binary dimensions \(6,4,2\) gives the displayed entries.
Their weighted sum is
\(10+104+95+108+45+12=374=5\cdot3^4-2^5+1\).

These are exact consequences of the source sequence and classical
representation formulas, not two held-out numerical experiments.

## 4. What this decomposition supplies

The decomposition identifies canonical isotypic summands in the native
curvature carrier and shows that its symmetry is much more constrained
than an arbitrary representation of the same dimension. It supplies
neither a canonical splitting of the multiplicity spaces nor a legal
operation projecting one monotone path to another.

It also does not make the physical metric permutation invariant.
The frozen predecessor proves that all three central projectors at
arity three fail to preserve the horizon-25 physical observation kernel.
Formula (2) cannot remove that obstruction. Any bridge to a Wick or
Walsh decomposition must still specify an intertwining source map and
verify compatibility with the original observation and its measure.
