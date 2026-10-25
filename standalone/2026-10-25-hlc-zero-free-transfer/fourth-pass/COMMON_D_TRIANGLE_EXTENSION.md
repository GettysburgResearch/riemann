# Common-shared-list triangles with both endpoint lists retained

**Status: extension of the paid raw triangle class to different
endpoint lists.** This note retains the source root vector at both
ends: the integer position returns, while the complete prime lists
may change. It controls the whole three-edge raw subfamily whose
shared prime sets remain constant. The bound does not extend to
changing shared sets, arbitrary surrounding histories, centered
comparison kernels, or a complete even moment.

All source notation, state weights, root coordinates and the explicit
finite-residue premise are those of
[CLOSED_TRIANGLE_WEIGHT.md](CLOSED_TRIANGLE_WEIGHT.md). That note's
original list-diagonal theorem is retained unchanged. In particular
each prime has one line draw, every edge has the original `d_0/D`
factor, and no `1/Y` is inserted in an edge.

## 1. The full common-D class and its forced prime pattern

Keep an unordered J-element shared set `D_i` in every prime group.
The unshared primes now follow

$$
 b_i\longrightarrow a_i\longrightarrow c_i\longrightarrow d_i,
                    \qquad z_0=z_3=(1,0).
 \tag{1}
$$

Every adjacent replacement is legal. Write the products as
`D,a,b,c,d`, and retain `a,b,c,d in [Y,4Y]`, `d_0<=D<2d_0`.
The chronological determinants are exactly

$$
 j_0=D(b-a),\qquad j_1=D(a-c),\qquad j_2=D(c-d).
 \tag{2}
$$

All three are nonzero. The determinant sum need not vanish when the
final lists differ from the initial ones.

**Lemma 1 (the root line excludes the other repetitions).** A term
with nonzero active-line indicator cannot have `b_i=c_i` or `a_i=d_i`
in any group. Consequently every group has either three distinct
unshared primes with `b_i=d_i`, or four distinct unshared primes.

**Proof.** If `p=b_i=c_i`, it is active at `z_0` and `z_2`, so
their projective lines modulo p must agree. Since `z_3=z_0`, this
would give `p|det(z_2,z_3)`. But the last replacement is legal,
so `p` divides neither D nor d, and (2) gives
`j_2=D(c-d)=-Dd mod p`, nonzero. This is a contradiction.
Similarly, `p=a_i=d_i` would make the lines of `z_1` and the root
equal, while `j_0=D(b-a)=Db mod p` is nonzero. These arguments
use primitive vertices, whose reductions are nonzero. Together with
the three adjacent inequalities from legal edges, they leave only the
stated possible repetition. QED.

Let I be the set of returning groups and put

$$
 t=\prod_{i\in I}b_i=\gcd(b,d),\qquad b=t b',\quad d=t d'.
 \tag{3}
$$

When I is proper, `b'!=d'` by unique factorization and the disjoint
prime groups. Also a and c are coprime to t and to both b,d.
The distinct-prime active union is now `D a c t b'd'`; once-line
averaging is bounded by

$$
 \prod_{p\mid Dactb'd'}\frac1{p+1}
            \le\frac1{D a c t b'd'}=\frac{t}{Dabcd}.
 \tag{4}
$$

For nonreturning endpoint primes, the same position at the other end
can create inactive-vertex damping. That damping is retained as a
factor at most one; it is not asserted to equal one. The common-D
line consistency and all additional projectors are handled exactly
as in the prior note.

The two root coordinates in the normalized unordered basis are both
`sqrt(((J+1)!)^K product V_i^(-(J+1)))`, even when their list
labels differ. Thus their product and the three symmetric edge
weights still give precisely equation (5) of the prior note.
After summing the unordered shared sets, its prefactor remains

$$
                 (J+1)^{-2K}\prod_iV_i^{-4}.
 \tag{5}
$$

The eta product is now `eta(a/Y)^2 eta(c/Y)^2 eta(b/Y) eta(d/Y)`.
Its absolute value is at most `||eta||_infty^6`. Raw `psi_1` is
still one on all three differences.

## 2. The closed-position congruence supplies an extra restriction

For fixed labels, the integer parametrization is

$$
 z_1=(h_0,j_0),\qquad
 z_2=\left(-\frac{j_1+h_0j_2}{j_0},-j_2\right).
 \tag{6}
$$

It is integral only if `gcd(j_0,j_2)|j_1`. When this holds, h_0
runs through one residue class modulo `|j_0|/gcd(j_0,j_2)`.
The exact global-root candidate-count integral of the first position
window is therefore

$$
 W\frac{g}{|b-a|},\qquad
 W=255/16,\quad g=\gcd(|b-a|,|c-d|),
 \tag{7}
$$

and it is zero if the congruence is insoluble. This retains every
integer candidate, with no minimum with one.

For a proper returning set I, define the nonzero differences
`h=b-a`, `k=c-d`. Since `(a,t)=1`, the integer h, and hence g,
is coprime to t. Also

$$
       a-c=t(b'-d')-(h+k).
$$

Since g divides h and k, the congruence condition in (6) is
equivalent to

$$
                          g\mid b'-d'.
 \tag{8}
$$

This is a restriction on the two endpoint products. It cannot be
discarded before the gcd is summed. It is available here precisely
because the position, rather than merely a projective line, closes.

## 3. An exact numerical upper bound for each returning set

For fixed t, put `B=Y/t`. In a nonempty original family with I
proper, b',d' are distinct positive odd integers at least three.
Their larger value is at least five and is at most `4Y/t`, so
`t<=4Y/5`, in particular `B>=1`.

After the genuine line weight (4) and congruence (8) have been
obtained, enlarge a,c to all integers in `[Y,4Y]` and b',d' to
all distinct integers in `[B,4B]`, keeping h,k nonzero and (8).
Each quadruple is counted once. Let `S_t` be this enlarged sum of

$$
               \frac1{a c t b'd'}\frac{g}{|h|}.
$$

**Lemma 2 (nonreturning endpoint sum).** For `Y>=1`, `t<=Y`,

$$
                      S_t\le\frac{288}{tY}(1+\log(3Y)).
 \tag{9}
$$

**Proof.** In the stated ranges, first use
`1/(a c t b'd')<=1/(Y^2 t B^2)=t/Y^4`.
This bound is taken before any further enlargement of the position
of a or c. It remains to bound the unweighted sum of `g/|h|`.
Fix signed differences `0<|h|,|k|<=floor(3Y)` and
put `g=gcd(|h|,|k|)`. For each b' there are at most
`2 floor(3B/g)` different d' in its congruence class in the allowed
interval. There are at most `3B+1<=4B` choices of b'. Thus the
number of pairs is at most

$$
                          24B^2/g.
$$

Each such pair determines `a=t b'-h`, `c=k+t d'` uniquely.
Ignoring their further range restrictions only enlarges the count.
Writing `H=floor(3Y)`, the sum of `g/|h|` is therefore at most

$$
 24B^2\sum_{0<|h|,|k|\le H}\frac1{|h|}
       =96B^2H\sum_{n\le H}\frac1n
       \le288\frac{Y^3}{t^2}(1+\log(3Y)).
$$

Multiplication by the already taken factor `t/Y^4` proves (9).
This numerical enlargement does not assign
the prime-level weight to any new source path. QED.

For fixed I, the actual t values are products of one prime from each
returning group. Hence

$$
             \sum_{t}\frac1t\le\prod_{i\in I}V_i.
 \tag{10}
$$

There is no new factorization multiplicity in (10), since the groups
are disjoint. Other prime exclusions and all smooth cutoffs may only
reduce the positive upper sum.

## 4. The whole common-D raw root return is paid

Let `T_common(s,t_0)` be the absolute three-edge raw root contribution
with common shared sets, now summing both initial and final complete
lists against the actual source root vector. Retain all original
positions, parity, good-state projectors and damping before taking
the root-and-line average. Put `H_Y=1+log(3Y)`.

**Theorem 1 (both endpoint lists).** Uniformly in the other normalized
root variables,

$$
 \boxed{
 \begin{split}
 T_{\rm common}(s,t_0)
 \le{}&\frac{W\|\eta\|_\infty^6}{Y}
       (J+1)^{-2K}\left(\prod_iV_i^{-4}\right)\\
 &\cdot\left[
 48H_Y^2+288H_Y\left\{\prod_i(1+V_i)-\prod_iV_i\right\}
 \right].
 \end{split}}
 \tag{11}
$$

**Proof.** Lemma 1 deletes every forbidden cross repetition exactly.
For I equal to all groups the lists return, so the unchanged theorem
in `CLOSED_TRIANGLE_WEIGHT.md` supplies the first term. For each
proper I, combine (4)--(10) with the original orbit/edge weights and
the shared-list sum. This gives the second term with factor
`product_(i in I) V_i`. Summing the proper subsets I gives exactly
`product_i(1+V_i)-product_i V_i`. QED.

All coefficients are bounded in absolute value before the numerical
enlargements. The assertion neither supposes independent endpoints
nor replaces the source root vector by a basis vector. It pays both
endpoint list choices for the stated common-shared-list class.

## 5. The conservative discrete-root corollary

Retain precisely the finite-residue premise (15) and fixed-parameter
hypotheses (16) of `CLOSED_TRIANGLE_WEIGHT.md`. This section uses
that original Appendix A estimate, independently of any later
refinement of its exponent.

There are at most J+4 distinct used primes per group. Both the
modulus and the number of label families are therefore bounded by
`x^((J+4) beta)`. The first position window still leaves at most
`O(x^((J+1) beta))` h_0 candidates per family. For each retained
primitive candidate all used-prime lines are prescribed and its
first position test is a single root interval. The same positive
enlargement as in the prior note therefore gives the total
discrepancy

$$
 x^{(J+4)\beta}\,x^{(J+1)\beta}\,
 x^{5(J+4)\beta-\delta/100}
            =x^{(7J+25)\beta-\delta/100}.
 \tag{12}
$$

For fixed J,K and V_i bounded below, (11) is
`O(x^(-alpha+epsilon))`; an upper bound for V_i is not additionally
needed, since the fixed-degree expression in (11) has at most one
positive V_i power against its factor `V_i^(-4)`.

Consequently the original arithmetic common-D triangle contribution,
with the source root-sum normalization, satisfies

$$
 \boxed{
 T_{\rm common}^{\rm arith}
 \ll x^{-\alpha+\epsilon}
                  +x^{(7J+25)\beta-\delta/100}.}
 \tag{13}
$$

This is source-dependent through its stated finite-residue premise,
and uses fixed J,K with polynomial bands as a parameter variant of
the finite-path model. It is not the paper's full growing-depth
parameter scheme. In the previous explicit example
`J=K=1`, `delta=1/4`, `alpha=1/80000`, `beta=1/40000`, the
new discrepancy is `x^(-17/10000)`, leaving the main saving unchanged.

## 6. Verification and remaining classes

`check_common_d_triangle_extension.py` checks the exact impossible
line patterns, the surviving partial-return classifications, the
closed congruence and candidate-count formula, original once-line
weights with both root lists, the finite numerical bound and the
conservative discrepancy budget. Its requirements remain enabled
under `python -O`.

The result enlarges a paid list-diagonal subfamily to all common-D
three-edge root returns. The changing-shared-list classes, immediate
two-edge contractions, the signed major-arc comparison and the
complete native coefficient matching still require additional work.
Attaching an arbitrary surrounding path changes the root distribution
and endpoint weights; no free extension to that situation is asserted.
