# Product-variety tensor family: a rank-three shadow inside `SO(8)`

**Packet status.**  Independently replay-audited.  The tensor polynomial, its
coefficient hypersurface, the compact-group comparisons, and the displayed
low moments are exact.  The
`q=3,5,7` laws are exact convolutions of source-locked histograms.  No field,
curve, or variety is enumerated by this packet.  The final section separates
open targets from proved statements.

The construction is deliberately different from another statistic on the
genus-two quintic family.  Pair a genus-one model and a genus-two model over
the same odd finite field,

\[
 E:Y^2=D_3(X),\qquad C:Y^2=D_5(X),
\]

and retain the primitive weight-two factor

\[
             H^1(E)\mathbin\otimes H^1(C).                              \tag{1}
\]

It has degree eight.  The complete `H^2(E x C)` factor also has two Tate
lines, so its local polynomial is `(1-qT)^2` times the polynomial below.
Keeping those lines separate prevents a trivial trace shift from being
mistaken for a monodromy signal.

## 1. Why the tensor image is orthogonal but not generic

Both `H^1` spaces carry alternating pairings.  Their tensor product is
symmetric, since

\[
 (v\otimes w,v'\otimes w')
 =\langle v,v'\rangle_E\langle w,w'\rangle_C
\]

is unchanged when both arguments are exchanged.  After normalization, the
compact image is therefore

\[
 \frac{USp(2)\times USp(4)}{\{(I,I),(-I,-I)\}}\longrightarrow SO(8).       \tag{2}
\]

The diagonal central pair is the kernel.  This also explains arithmetically
why simultaneously quadratic-twisting `E` and `C` leaves (1) unchanged.

The source has dimension `3+10=13` and rank `1+2=3`; `SO(8)` has dimension
28 and rank 4.  Thus an `SO(8)` functional equation is not evidence of
generic `SO(8)` monodromy.  Sections 3 and 5 give exact fingerprints of the
missing rank.

## 2. Tensor Frobenius polynomial

Let `t_E=q+1-#E(F_q)` be the geometric trace stored in the locked genus-one
fixture and put `A=-t_E`.  Use the resulting coefficient conventions:

\[
\begin{aligned}
 P_E(T)&=1+A T+qT^2=1-t_ET+qT^2,\\
 P_C(T)&=1+aT+bT^2+qaT^3+q^2T^4.
\end{aligned}                                                            \tag{3}
\]

If the Frobenius eigenvalues are `alpha_i` and `beta_j`, the tensor factor is

\[
 Q(T)=\prod_{i=1}^2\prod_{j=1}^4(1-\alpha_i\beta_jT).                     \tag{4}
\]

Its power sums satisfy the particularly cheap recurrence

\[
 p_n(E\otimes C)=p_n(E)p_n(C).                                            \tag{5}
\]

Newton's identities then give

\[
 Q(T)=1+c_1T+c_2T^2+c_3T^3+c_4T^4
      +q^2c_3T^5+q^4c_2T^6+q^6c_1T^7+q^8T^8,                            \tag{6}
\]

where

\[
\boxed{\begin{aligned}
 c_1={}&-Aa,\\
 c_2={}&A^2b+qa^2-2qb,\\
 c_3={}&Aaq(-A^2-b+3q),\\
 c_4={}&q^2(A^4+A^2a^2-4qA^2-2qa^2+b^2+2q^2).
\end{aligned}}                                                           \tag{7}
\]

The producer negates each stored genus-one trace key before applying these
formulas.  It implements (5) independently of (7), compares the two on locked
witnesses in every frozen field, and tests them on every source histogram atom
pair.  Equation (6) is the weight-two functional equation; no numerical root
approximation is involved.

## 3. An exact coefficient hypersurface

Normalize the first half of (6) by

\[
 u={c_1\over q},\qquad v={c_2\over q^2},\qquad
 w={c_3\over q^3},\qquad h={c_4\over q^4}.                               \tag{8}
\]

Also set

\[
 x={A^2\over q},\qquad y={a^2\over q},\qquad z={b\over q}.
\]

The coefficient map is

\[
 u^2=xy,\quad v=xz+y-2z,\quad w=u(x+z-3),
 \quad h=x^2+xy-4x-2y+z^2+2.                                            \tag{9}
\]

Eliminating `x,y,z` gives the memberwise identity

\[
\boxed{u^2h-u^4+2u^2v+u^2-2uw-w^2=0.}                                  \tag{10}
\]

No division by `u` is used, so (10) includes the trace-zero locus and shows
directly that `u=0` forces `w=0`.  In integral coefficients it is

\[
\boxed{
c_1^2c_4-q^2c_1^4+2q^2c_1^2c_2+q^4c_1^2-2q^2c_1c_3-c_3^2=0.}           \tag{11}
\]

This is not a fitted correlation.  It is the algebraic shadow of the
rank-three torus in (2), occupying a hypersurface in the rank-four
coefficient space of `SO(8)`.  A family with nonzero defect in (10) cannot
consist solely of these tensor lifts.

## 4. Exact all-`q` product-family moments

Uniform independent monic squarefree models give the product of the two
natural stabilizer-weighted model/stack laws.  Quadratic-twist symmetry kills
all odd trace moments.  The locked genus-one formulas are

\[
 \mathbb E\left[(A/\sqrt q)^2\right]={q^2-1\over q^2},\qquad
 \mathbb E\left[(A/\sqrt q)^4\right]={2q^3-3q-1\over q^3},               \tag{12}
\]

and the locked genus-two formulas are

\[
\begin{aligned}
 \mathbb E\left[(a/\sqrt q)^2\right]
 &= {q^4-q^3+q^2+q-2\over q^4},\\
 \mathbb E\left[(a/\sqrt q)^4\right]
 &= {3q^5-7q^4+5q^3+12q^2-14q-11\over q^5}.
\end{aligned}                                                            \tag{13}
\]

Since the normalized tensor trace is `Aa/q=-u`, its moments through four
are exactly

\[
\boxed{\begin{array}{c|c}
 k&\mathbb E[(Aa/q)^k]\\ \hline
0&1\\
1&0\\
2&{(q^2-1)(q^4-q^3+q^2+q-2)\over q^6}\\
3&0\\
4&{(2q^3-3q-1)(3q^5-7q^4+5q^3+12q^2-14q-11)\over q^8}.
\end{array}}                                                             \tag{14}
\]

The same locked low-weight input moments give three coefficient averages:

\[
\boxed{\begin{aligned}
 \mathbb E[v]
 &=-{(q-1)(q^3-q^2+q+1)\over q^6},\\
 \mathbb E[h]
 &={q^6-2q^5+q^4-2q^2-2q+2\over q^6},\\
 \mathbb E[uw]
 &={(q-1)(q+1)^2(q^4-4q^3+5q^2-q-5)\over q^7}.
\end{aligned}}                                                           \tag{15}
\]

Thus the first corrections to the product-Haar values are

\[
 \mathbb E[h]-1=-{2\over q}+{1\over q^2}-{2\over q^4}
                 -{2\over q^5}+{2\over q^6},                             \tag{16}
\]

and

\[
 \mathbb E[uw]-1=-{3\over q}+{7\over q^3}-{7\over q^4}
                 -{9\over q^5}+{6\over q^6}+{5\over q^7}.               \tag{17}
\]

Equations (14)--(17) hold for every odd prime power, conditional only on the
already locked source theorems; the frozen histograms are regression checks,
not proof inputs.

## 5. Product Haar versus generic `SO(8)`

For a product element, the trace factors.  Standard-representation Haar
moments through degree six are

| order | `USp(2)` | `USp(4)` | product image | generic `SO(8)` |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 | 0 |
| 2 | 1 | 1 | 1 | 1 |
| 3 | 0 | 0 | 0 | 0 |
| 4 | 2 | 3 | **6** | **3** |
| 5 | 0 | 0 | 0 | 0 |
| 6 | 5 | 14 | **70** | **15** |

The symplectic entries count closed add/remove-box paths for the standard
representation.  Below tensor degree eight, the `SO(8)` entries are the
linearly independent Brauer pair contractions.  In particular, the earliest
trace-moment fingerprint is rigorously the fourth:

\[
 \dim\operatorname{Inv}((V_2\otimes V_4)^{\otimes4})
 =2\cdot3=6,qquad
 \dim\operatorname{Inv}(V_8^{\otimes4})=3.                               \tag{18}
\]

There are two equally early coefficient fingerprints.  Here `h` is the
character of `exterior^4(V_2 tensor V_4)`, while `uw` is the product of the
standard and third-exterior characters.  The exterior Cauchy identity shows

\[
 \dim\operatorname{Inv}(\mathop{\bigwedge}^4(V_2\otimes V_4))=1,
 \qquad
 \dim\operatorname{Hom}(V_2\otimes V_4,
                  \mathop{\bigwedge}^3(V_2\otimes V_4))=1.               \tag{19}
\]

For generic `SO(8)`, `exterior^4 V_8` has no invariant and `exterior^3 V_8`
does not contain `V_8`.  Hence

\[
 (\mathbb E[h],\mathbb E[uw])_{\rm product}=(1,1),\qquad
 (\mathbb E[h],\mathbb E[uw])_{SO(8)}=(0,0).                             \tag{20}
\]

This verifies the compact-group comparison rather than inferring it from
small finite fields.

## 6. Frozen laws without a new finite-field scan

For each of `q=3,5,7`, the producer reads:

- the complete genus-one model trace histogram from
  `genus1_cubic_family_laws.json`, converted from `t_E` to the polynomial
  coefficient `A=-t_E`; and
- the complete genus-two joint `(a,b)` histogram from
  `balanced_control_family_scan.json`.

It takes their Cartesian convolution, applies (7), and combines identical
coefficient tuples.  Across all three fields this is only 2,471 histogram
atom pairs, below the hard 20,000-operation cap.  The JSON retains:

- the complete compressed `(c1,c2,c3,c4)` law;
- the normalized trace law and moments through degree eight;
- the normalized middle-coefficient law;
- frozen second moments of the centered detectors `h-1` and `uw-1`; and
- three recurrence witnesses per field.

The exact compression sizes are:

| `q` | product model pairs | source atom pairs | coefficient atoms | trace atoms | `h` atoms |
|---:|---:|---:|---:|---:|---:|
| 3 | 2,916 | 224 | 112 | 13 | 41 |
| 5 | 250,000 | 729 | 354 | 27 | 106 |
| 7 | 4,235,364 | 1,518 | 751 | 45 | 236 |

Every accepted quantity is an integer or rational pair.  There are no
floating-point roots, random samples, or field-arithmetic calls.

## 7. Model/stack law is not a uniform coarse law

The histogram convolution weights independent marked equations uniformly.
Equivalently, it is the product of the two stabilizer-weighted curve-stack
laws on ordered factor pairs.  It is not the uniform law on coarse
product-variety isomorphism classes.

This distinction is especially sharp for twists:

- square-affine changes preserve each signed trace and describe the relevant
  curve-isomorphism quotients;
- a nonsquare full-affine change flips the corresponding `H^1` trace;
- `c2,c4` survive forgetting the two twist signs independently, but `c1,c3`
  do not; and
- a *simultaneous* twist of both factors fixes the complete tensor polynomial,
  matching the diagonal kernel in (2).

The locked genus-two artifact has a full-affine branch-orbit census but not a
complete square-affine joint `(a,b)` coarse histogram.  This packet therefore
refuses to fabricate a signed coarse tensor law.  It records the exact input
total-variation discrepancies and an upper bound for the even-coefficient
pushforward only.

## 8. Strange next targets and firewall

The following are nominated computations, not asserted theorems:

1. Prove all-`q` variances for `h-1` and `uw-1`, then decompose their first
   corrections into automorphic character channels.
2. Use the defect in (10) as a detector for hidden tensor lifts inside larger
   orthogonal families.
3. Couple `E` and `C` through a shared cover, isogeny, or correspondence.  The
   hypersurface remains pointwise, but factorization of the family moments can
   fail and expose mixed monodromy.
4. Classify the singular trace-zero stratum `u=w=0`: separate ordinary twists,
   supersingular factors, and endomorphism-enhanced products.

Nothing in this packet proves equidistribution, a convergence rate, generic
`SO(8)` monodromy, a number-field family theorem, RH, or GRH.  The frozen
three-field laws are exact examples, not interpolation data.  The exact
hypersurface in fact proves that this particular tensor family cannot have a
generic `SO(8)` coefficient distribution.
