# Exact cancellation in a determinant bridge, with the memory retained

**Status.** This note proves an exact finite-field mechanism that is absent
from a single conditioned dirty edge: a complete three-edge determinant
bridge returning to one recorded projective line has a rank-one radial
kernel. Its correctly centered kernel is zero, even after arbitrary fixed
endpoint projections. The proof also gives the exact even-length
contraction, a quantitative error for internal projections, and the exact
short-return schedule that prevents using the result indiscriminately in
the HLC trace. A further source-level theorem proves that an immediate
return of a memory prime from the largest prime group forces an exact
integer backtrack of the entire list and position. That theorem uses the
source's complete good-state condition, not a hypothetical residue
completion. Restoration of a list means restoration as an unordered
list; the source's symmetrization can change its ordering.

These are finite operator theorems. This note does **not** establish the
residue completion for the integer HLC operator, a power-saving HLC
estimate, an improvement to the native middle band, or a new zero-free
region. The theorem identifies a positive, checkable source of cancellation
and states the additional comparison and short-return estimates it needs.

The previous pass is frozen at
`3a07737bb7b802a5671acaa22a8f86e6b0acbd40` in
`GettysburgResearch/riemann`. Its
[PROJECTED_AFFINE_OPERATOR.md](../third-pass/PROJECTED_AFFINE_OPERATOR.md)
proves that a single fixed-line dirty channel is an isometry. Nothing here
changes that result: the new cancellation occurs after a specific complete
multi-edge average.

## 1. The complete determinant operator

Let p be an odd prime, V=F_p^2 minus the zero vector, and use uniform
probability measure on V. For c nonzero in F_p put

$$
 (A_c f)(z)=\frac1p\sum_{\det(z,w)=c}f(w).
 \tag{1}
$$

Every determinant fibre has exactly p elements, so A_c is a Markov
operator and preserves the uniform measure. Write

$$
 (S_a f)(z)=f(az),\qquad
 (Bf)(z)=\sum_{w\in [z]\setminus\{0\}}f(w),\qquad
 (J_\Sigma f)(z)=\sum_{w\in V}f(w).
$$

Here B and J_Sigma are **unnormalized sums**. In particular they are not
orthogonal projections as written. Direct counting gives

$$
 \boxed{A_cA_d=\frac1pS_{-d/c}
                    +\frac1{p^2}(J_\Sigma-B).}
 \tag{2}
$$

To prove this, fix z,w. Intermediate y must satisfy
det(z,y)=c and det(y,w)=d. If z,w are independent there is exactly one y.
If w=a z, the two equations are compatible exactly when a=-d/c, and then
there are p choices. The sum of the two kernels in (2) has exactly those
entries, divided by p squared.

There is an orthogonal decomposition

$$
 L^2(V)=\mathbf C1\ \oplus\ H_{\rm line}\ \oplus\ H_{\rm radial},
 \tag{3}
$$

where H_line consists of functions constant on each projective line and
of overall mean zero, and H_radial consists of functions with sum zero
on every individual punctured line. Each A_c preserves these subspaces.
On constants it is the identity. On H_line it is multiplication by -1/p:
from a point z, the determinant fibre visits every projective line other
than [z] exactly once. On H_radial, (2) becomes

$$
 A_cA_d=p^{-1}S_{-d/c}.
 \tag{4}
$$

Since A_c^*=A_{-c}, its singular value on H_radial is exactly p^(-1/2).
Thus, if J_V is the **normalized** constant projection on V,

$$
 \|A_c-J_V\|_{2\to2}=p^{-1/2}.
 \tag{5}
$$

This bound is for the complete operator (1); it is not a bound for the
single-line pullback in the preceding pass.

## 2. Exact return to one recorded line

Fix a projective line ell, write Y=ell minus zero, and give Y its uniform
probability measure. Let E_ell extend functions on Y by zero to V and
R_ell restrict functions on V to Y. These particular maps are not being
called isometries; their normalization factors cancel in the explicit
kernel below. Set

$$
 K_{\boldsymbol c}
       =R_\ell A_{c_1}\cdots A_{c_k}E_\ell,
 \qquad c_1,\ldots,c_k\ne0.
 \tag{6}
$$

Let J_ell g=E_Y g, Pi_ell=I-J_ell, and retain S_a as the permutation
g(z) maps to g(az) of Y. Define

$$
 q_k=\frac{1+(-1)^k p^{1-k}}{p+1}.
 \tag{7}
$$

**Theorem 1 (complete line-return formula).** For odd k,

$$
 K_{\boldsymbol c}=q_k J_\ell.
 \tag{8}
$$

For k=2m,

$$
 K_{\boldsymbol c}
    =q_{2m}J_\ell+p^{-m}S_{\lambda}\Pi_\ell,
 \qquad
 \lambda=(-1)^m\frac{c_2c_4\cdots c_{2m}}
                         {c_1c_3\cdots c_{2m-1}}.
 \tag{9}
$$

All scalars in lambda are interpreted in F_p. In particular q_1=0;
one nonzero determinant step cannot return to the same projective line.

### Proof

Write g=bar(g)+g_0 on Y. The zero extension of g_0 is in H_radial.
For 2m steps, (4), grouped into adjacent pairs, gives p^(-m) S_lambda
on this subspace. An odd product is p^(-m) S_a A_b for suitable nonzero
a,b. Its kernel from Y to Y is zero: a nonzero determinant cannot join
two points on Y. This proves the radial terms in (8)-(9).

For the constant part, E_ell 1 has overall mean 1/(p+1). Its difference
from that constant is in H_line. The eigenvalue there is (-1/p)^k.
Restriction back to Y therefore gives

$$
 \frac1{p+1}+\left(-\frac1p\right)^k\frac p{p+1}=q_k.
$$

This proves the whole formula. It also proves that q_k is the return
probability to ell, independently of the initial nonzero point of ell.
QED.

For k at least two, q_k is positive. The conditional bridge operator,
given a return to ell, is C_c=K_c/q_k. Hence

$$
 \boxed{C_{\boldsymbol c}=J_\ell\quad(k\ge3\text{ odd}),}
 \tag{10}
$$

and for k=2m,

$$
 C_{\boldsymbol c}
    =J_\ell+\rho_{2m}S_\lambda\Pi_\ell,\qquad
 \rho_{2m}=\frac{p^{-m}}{q_{2m}}
          =\frac{(p+1)p^{m-1}}{p^{2m-1}+1}.
 \tag{11}
$$

Thus the correctly centered bridge has norm exactly rho_(2m). The first
cases make the distinction concrete:

| Number of steps | Return mass | Conditional centered norm |
|---|---:|---:|
| 2 | 1/p | 1 |
| 3 | (p-1)/p^2 | 0 |
| 4 | (p^2-p+1)/p^3 | p/(p^2-p+1) |
| 5 | (1-p^(-4))/(p+1) | 0 |
| 6 | (1+p^(-5))/(p+1) | p^2(p+1)/(p^5+1) |

In particular, an even gap of length at least four gives
rho_(2m) at most (1+1/p)p^(1-m). A three-step gap completely removes
the radial mean-zero part. Neither statement requires a bound for a
Kloosterman sum or an asymptotic limit.

### Zero determinant steps

If a complete step with determinant zero is needed, its Markov
normalization is

$$
 A_0 f(z)=\frac1{p-1}\sum_{a\in F_p^*}f(az).
 \tag{12}
$$

It fixes constants and H_line and annihilates H_radial. Consequently a
product containing A_0 has no radial part. If n of its other steps have
nonzero determinant, its same-line restriction is q_n J_ell, with
q_0=1. If n=1 there is no return. The change from p to p-1 in (12) is
essential; a zero determinant fibre has p-1 nonzero targets.

## 3. Fixed endpoint projectors and imperfect middle support

The complete three-step result remains useful with endpoint restrictions.
For arbitrary multiplication projectors P_0,P_3 on Y,

$$
 P_0(C_{c_1,c_2,c_3}-J_\ell)P_3=0.
 \tag{13}
$$

The subtraction is inside the endpoint projectors. No assertion that
projecting a mean-zero function preserves its mean is needed.

There is also an explicit bound when the two intermediate vertices are
restricted. Put X=V minus ell. The first and last nonzero determinant
conditions force both intermediate vertices to lie in X. Let P_1,P_2
be arbitrary multiplication projectors on X, with deleted densities

$$
 \delta_i=\frac{|\{z\in X:P_i(z)=0\}|}{p(p-1)}.
$$

Use the original return normalization even after the restrictions:

$$
 C(P_1,P_2)=q_3^{-1}
   R_\ell A_{c_1}P_1 A_{c_2}P_2 A_{c_3}E_\ell.
 \tag{14}
$$

In particular we do **not** divide by a new endpoint-dependent surviving
mass. The restricted operator is substochastic.

**Theorem 2 (projection error for the three-step bridge).** With all
three c_i nonzero,

$$
 \boxed{\|P_0\{C(P_1,P_2)-J_\ell\}P_3\|_{2\to2}
       \le\min\{1,\sqrt{\delta_1+\delta_2}\}.}
 \tag{15}
$$

For bounded endpoint functions f,g one also has

$$
 |\langle f,P_0\{C(P_1,P_2)-J_\ell\}P_3g\rangle|
       \le(\delta_1+\delta_2)\|f\|_\infty\|g\|_\infty.
 \tag{16}
$$

### Proof

For fixed endpoints z,w on Y, the bridge equations admit exactly p
pairs (y,t). Indeed choose y on det(z,y)=c_1, giving p choices. Since
y and w are independent, the equations det(y,t)=c_2 and det(t,w)=c_3
then determine t uniquely. The kernel of (14), relative to uniform
probability on Y, is therefore

$$
 K(z,w)=\frac1p\sum_{\substack{\det(z,y)=c_1\
              \det(y,t)=c_2,\ \det(t,w)=c_3}}
                       P_1(y)P_2(t).
 \tag{17}
$$

It lies in [0,1], and the complete kernel is identically one.
When both endpoints are uniform on Y and one of the p bridge pairs is
chosen uniformly, each intermediate marginal is uniform on X. For y,
there is exactly one initial z on Y with det(z,y)=c_1; each of the p-1
final w gives one t. Thus each y has p-1 preimages among the
p(p-1)^2 bridge tuples. The argument for t is the reverse count.

Consequently the mean of D(z,w)=1-K(z,w) is at most delta_1+delta_2
by the union bound. Since 0 at most D at most 1, its squared mean is at
most min(1,delta_1+delta_2). The Hilbert--Schmidt bound gives (15).
Multiplication by either endpoint projector is a contraction. The same
mean bound, with absolute endpoint functions, proves (16). QED.

The exceptional densities in this theorem are conditional densities on
the indicated finite bridge. An unconditional exceptional-measure bound
in the real root variable is not silently substituted for them. If
projectors depend on an auxiliary label, apply the theorem after fixing
that label only when the conditional complete bridge law is valid there.

For an actual normalized three-step operator B, a proved comparison

$$
 \|P_0\{B-C(P_1,P_2)\}P_3\|_{2\to2}\le\varepsilon
 \tag{18}
$$

would therefore give

$$
 \|P_0(B-J_\ell)P_3\|_{2\to2}
       \le\varepsilon+\sqrt{\delta_1+\delta_2}.
 \tag{19}
$$

This is a concrete usable comparison target. It retains the entire
endpoint projection and the normalization of the constant channel.

## 4. Two-step returns survive the same projection test

For two nonzero determinant steps, a same-line endpoint must be
w=lambda z with lambda=-c_2/c_1. There are p intermediate points and no
other possible endpoint. If P is an intermediate projector on X, the
conditional two-step bridge is

$$
 C_2(P)g(z)=a(z)g(\lambda z),\qquad
 a(z)=\frac1p\sum_{\det(z,y)=c_1}P(y).
 \tag{20}
$$

The fibres in this formula partition X, so E_Y a=1-delta, where delta
is the deleted density of P on X. For a nonprincipal multiplicative
character chi on F_p^*, transported to Y using any generator of ell,
chi has mean zero and constant modulus one. Formula (20) gives

$$
 \|\{C_2(P)-J_\ell\}\chi\|_2^2
      =E_Y a^2\ge(1-\delta)^2.
 \tag{21}
$$

This is an exact lower bound for this finite conditional bridge. It is
not a lower bound for the integer HLC operator. It shows why merely
retaining most intermediate states does not turn a two-step return into
the cancellation in Theorem 2.

The distinction persists over many returns. Suppose a recorded line is
imposed at times 0,2,4,...,2m. Conditioning at every one of these times
composes m two-step bridges, not one uninterrupted 2m-step bridge. With
no intermediate projectors the result is the radial permutation
S_(lambda_1...lambda_m). Its centered norm is one. Formula (11) for an
uninterrupted 2m-step bridge cannot be used after adding those extra
line conditions.

## 5. The short-return pattern in the HLC memory rules

The source is Lü--Wang--Wu,
[arXiv:2610.20242v1](https://arxiv.org/html/2610.20242v1), especially
(4.37)--(4.40) and (4.47)--(4.50). The exact source premises used here are
the raw equation det(z_j,z_(j+1))=G_j-G_(j+1), where G_j is the complete
active-list product; one recorded line per prime; and the rule that
moving a recorded pair back to a list is not a new prime selection.
The independent line factor is paid once for that prime. These premises
are documented with their measures in the preceding pass's operator
note. The following consequences are new deductions from those rules.

Suppose a prime p is active at two vertices separated by one inactive
vertex. Then G_0=G_2=0 modulo p and G_1 is nonzero modulo p. The two
determinants are

$$
 c_1=-G_1,\qquad c_2=G_1\pmod p.
$$

Thus lambda=-c_2/c_1=1. The conditional two-step return is the identity,
not merely some nontrivial radial permutation. In particular its failure
to mix is compatible with the **actual telescoping determinant values**;
it does not depend on choosing unrelated artificial determinants.

More generally fix shared lists with product D, and disjoint unshared
prime products a,b, each taking one prime from each group. Alternate the
complete active products Db,Da,Db,Da,...,Db. The following memory
schedule is permitted by the stated local transfer and distinctness rules:

1. Start with b active and empty memory. On the first edge, record b and
   draw a freshly.
2. On the next edge, record a and restore b from memory.
3. Continue interchanging the two recorded groups. On the last edge,
   discard the departing a rather than recording it, and restore b.

Initial and final memory are empty. Every prime in b was selected in the
initial list, and every prime in a was drawn once on the first edge.
Later uses transfer existing coordinates. Thus the schedule violates no
global distinctness rule on **new selections**. This is a combinatorial
compatibility statement; it does not assert a lower density of integer
paths satisfying all archimedean good-state tests.

For p dividing b, all even vertices have its line and all odd vertices
have a different line, because the adjacent determinant is nonzero
modulo p. Its complete local factor is therefore

$$
 \frac1{p+1}\,V_i^{-\kappa_p},
 \tag{22}
$$

before the common extracted b'_p is allocated between factors. Every
inactive-vertex damping term is exactly one. The corresponding statement
holds for primes dividing a with odd and even exchanged. Hence the
local damping expansion does not cancel this schedule. An additional
factor 1/(p+1) at each return would count the same line draw repeatedly.

This observation does not lower-bound the full raw-minus-major-arc
trace: other prime factors, other paths, comparison terms, signed
endpoint coefficients and the integer geometry remain. It does prove
that a claim that every long memory path contains the three-step
cancellation is false without further restrictions.

### 5.1 A largest-group immediate return forces a complete backtrack

The preceding obstruction can be refined using more of the actual
good-state condition. This refinement holds for the integer path itself.

**Theorem 3 (largest-group immediate return).** Consider two consecutive
raw edges z_0 to z_1 to z_2 in the source's conjugated list model. Assume
the middle complete list state passes its full good-state test, and the
same position and complete-list restrictions of the source are retained.
Suppose a prime p from the largest group P_K is the unshared departing
prime on the first edge, is recorded with line [z_0]_p, and supplies the
incoming unshared prime on the second edge. Then, for sufficiently large
source parameters, the second edge restores every **unordered complete
list** at z_0, and z_2=z_0 as integer vectors.

The theorem does not assume in advance that the lower-group incoming
primes are returns from the previous edge. It proves that their prime
values must be those previously departed. Under the global distinctness
condition on new prime selections, those values must be supplied by
existing memory coordinates, if the path is to be nonzero.

#### Proof

Let G_1 be the complete active product at z_1. On the second edge let D
be the shared-list product and let Z be the product of all incoming
unshared primes in groups 1 through K-1. Its full incoming product is
p D Z, and its raw determinant is

$$
 j=G_1-pDZ.
 \tag{26}
$$

Choose an integer complement w_1 with det(z_1,w_1)=1 and put
R=tau(w_1)/tau(z_1). Every integer endpoint has the form
z'=j w_1+h z_1. Since p is not in the complete list at z_1,
j=G_1 is nonzero modulo p. The recorded line [z']_p=[z_0]_p fixes one
residue h=h_* modulo p, independently of D,Z. Writing h=h_*+pn,
the source's position ratio restriction gives

$$
 \left\|DZ R-\frac{G_1R+h_*}{p}\right\|_{\mathbb R/\mathbb Z}
                      \le\frac{16}{p}.
 \tag{27}
$$

Now use the good-state test with I={1,...,K}, even if the actual edge
uses a proper subset of these groups for memory transfers. In this test
the fresh-prime product T_f is empty. Its only choice has mass one, so
it cannot be included in an exceptional set whose allowed mass is
strictly below one. The test therefore separates **all** distinct D Z
formed from an allowed shared product and arbitrary lower-group prime
choices:

$$
 \|(DZ-D'Z')R\|\ge100\exp(-L^{a_K})
                      \qquad(DZ\ne D'Z').
 \tag{28}
$$

Let D_0 be the shared product on the previous edge, and let Z_0 be the
product of its departed primes in groups below K. The reversed previous
edge, with endpoint z_0, is a valid candidate for the same geometric
phase equations: its product is p D_0 Z_0, its recorded p-line is
[z_0]_p, and it satisfies the original position restrictions. This
candidate is used only for comparison in (27)-(28); no assumption about
the availability of its lower primes in memory is needed.

Both D Z and D_0 Z_0 therefore satisfy (27). Their difference has
distance at most 32/p from an integer. Since p is at least
exp(L^(a_K)), this contradicts (28) unless D Z=D_0 Z_0.
Every prime of D or D_0 belongs to the complete middle list. Every
prime of Z or Z_0 is outside that list by the cross-edge restrictions.
Unique factorization first gives D=D_0 and Z=Z_0. The disjoint group
sets then identify every individual lower-group incoming prime with
its departed predecessor. The full list product is restored:
G_2=p D_0 Z_0=G_0. In fact each unordered list is restored, not just
its product.

It remains to identify the position over the integers. The two raw
determinants are now j_0=G_0-G_1 and -j_0. Hence

$$
 \det(z_1,z_2-z_0)=0.
$$

Primitivity of z_1 implies z_2-z_0=k z_1 for an integer k. The common
positive tau-window bounds |k| by an absolute constant; the source's
ratio window permits the conservative bound |k| at most 255. Reduction
modulo p and the two common recorded lines give

$$
 0=\det(z_0,z_2)=k\det(z_0,z_1)\pmod p.
$$

The second factor is nonzero modulo p. Thus p divides k, and p>255
forces k=0. Therefore z_2=z_0. QED.

This proves that the top-group two-step memory return can be identified
as an actual diagonal contraction in the original position-and-list
graph. It is stronger than saying that its finite-field conditional
kernel is an isometry.

There are two limits to the conclusion. First, the Fock memory after
these edges need not equal its initial value: the intermediate departing
primes may be recorded or discarded. It would be incorrect to replace
the complete two-edge **Fock** operator by the identity without summing
those choices and their weights. Second, a diagonal contraction inside
a longer trace is not automatically a diagonal of the original native
Möbius moment. The exact identification of the whole native kernel must
still be supplied.

For paths with these full geometric backtracks removed, a largest-group
memory prime cannot return after just two edges. Its first possible
nontrivial return has length at least three, which is the range in which
Theorems 1--2 supply a genuine complete-residue contraction. This gives
a sharper division of the remaining arithmetic work: sum the exact
backtrack contractions with their actual memory weights, and complete
the surviving longer returns. It does not assert that either step has
already been bounded with a fixed power.

### 5.2 The required separation can itself be power-good

There is a quantitative statement for the particular full-I condition
used in Theorem 3. Fix the complete middle lists and let mathcal X be
the finite set of distinct integer products D Z considered there.
Write M=|mathcal X| and P_min=min P_K. For a uniform real phase R
modulo one, the exceptional set on which some distinct x,y in
mathcal X satisfy

$$
 \|(x-y)R\|<100/P_{\min}
$$

has measure at most

$$
 \boxed{\min\{1,100M(M-1)/P_{\min}\}.}
 \tag{29}
$$

For P_min at least 200, each unordered pair has failure measure at
most 200/P_min, because multiplication by the nonzero integer x-y
preserves Haar measure on the circle. The union bound over M(M-1)/2
pairs proves (29); the trivial bound one handles the other range.

There are at most (J+1)^K shared-product choices and at most
product_(i<K)|P_i| choices of the other incoming primes. Consequently

$$
 M\le(J+1)^K\prod_{i<K}|\mathcal P_i|.
 \tag{30}
$$

For fixed K,J, polynomial prime bands with
|P_i| at most x^(epsilon_i) and P_min at least x^(epsilon_K) therefore
give exceptional measure

$$
 O_{J,K}\left(x^{-\gamma}\right),\qquad
 \gamma=\epsilon_K-2\sum_{i<K}\epsilon_i>0.
 \tag{31}
$$

For example epsilon_i=3^(i-1)epsilon_1 gives gamma=epsilon_1 for
every largest-group index. This is a proved power estimate for this
one separation test. It needs no prime-number theorem: the displayed
prime-set cardinality bounds suffice.

This does not yet prove a polynomial-strength root replacement.
In particular, (29) is a real-phase measure, not the conditional
finite-bridge densities delta_i of Theorem 2. Other good-state tests,
the many-prime damping expansion, actual root discrepancy, complete
endpoint lists and moment normalization still have to be paid in any
combined application. Keeping those distinctions is essential when
using (31) as a component of a redesign.

## 6. A pointwise norm constraint on the original list operator

There is a second useful check before attempting to strengthen every
edge norm. In the original (non-Fock) list space, each ordered state has
the same measure sigma=product_i V_i^(-(J+1)). Pass to unit vectors
supported on the permutations of one unordered list state. If two
unordered states differ in exactly one prime per group, only the
ordering putting that prime in the departing slot contributes to their
matrix entry. The fraction of such orderings is (J+1)^(-K).

Consequently, provided both states pass the good-state projection, their
matrix entry in G S T_1 S G is exactly

$$
 (J+1)^{-K}\left(\prod_iV_i^{-1}\right)
                 K_1(P,Q;D,a,b).
 \tag{23}
$$

This follows by counting (J!)^K compatible orderings among
((J+1)!)^K orderings; the equal state measures cancel. It is also valid
when the entry is complex. The operator norm is at least the absolute
value of this one entry.

There is no additional factor 1/Y in (23). The original K_1 contains
d_0/D, while a 1/Y factor appears only in the separately converted
clean auxiliary kernel. Transporting that factor to the original
unordered-state norm would produce an unsupported power gain.

At a raw edge, the bracket in K_1 is one minus its major-arc integral;
the integral has absolute value at most the measure of the major arcs.
Thus any retained edge for which the full remaining nonnegative
multiplier `(d_0/D) eta(a/Y) eta(b/Y) psi_1(t/Y) rho^(...)` is at
least c_0 gives

$$
 \|G S T_1 S G\|\ge
 c_0(J+1)^{-K}\left(\prod_iV_i^{-1}\right)
                    (1-|\mathfrak M_1|).
 \tag{24}
$$

The hypothesis that such a good raw edge exists is part of this
statement. No existence or density theorem for good integer edges is
being inferred from finite-field counting. Subject to that explicit
hypothesis, fixed K,J and fixed positive V_i cannot yield a uniform
prime-power-small norm for this **whole** operator. A proposed
polynomial-strength redesign must either let the number of choices
grow, isolate exceptional localized states, or estimate the actual
structured endpoint coefficients. Improving every raw edge uniformly
is a stronger demand than proving the required arithmetic pairing.

This does not contradict a possible power saving for the bounded
product-form Möbius endpoints in the paper: a matrix-entry test vector
is not a proof that those endpoints have a large pairing.

The same normalization gives an exact check on paying the integer
backtracks. Let T_raw denote the original unordered-list operator with
only the raw kernel, including its good-state projection and all
cutoffs. In the orthonormal unordered-state basis, its diagonal
two-edge contraction is

$$
 (T_{\rm raw}T_{\rm raw}^*)_{s,s}
                         =\sum_t|(T_{\rm raw})_{s,t}|^2.
 \tag{32}
$$

Under the retained-edge hypothesis just used, this is at least
`c_0^2 (J+1)^(-2K) product_i V_i^(-2)`. Thus the exact backtrack
identified in Theorem 3 is not automatically a prime-power-small
operator after it is contracted. A useful estimate for the actual
arithmetic pairing would have to exploit the measure of these states,
their coefficient structure, or another signed cancellation. This
diagonal identity does not lower-bound the full raw-minus-comparison
arithmetic sum or the native inverse moment.

## 7. What the three-step theorem would change in a polynomial redesign

The earlier source audit identified the dirty raw edge estimate as the
part that only saves a power of the number of list choices. Theorem 2
offers a different route for a selected **block** of edges. If a
polynomial-scale memory prime p is at least x^a, a comparison error
epsilon at most x^(-eta), and conditional deleted density
delta_1+delta_2 at most x^(-2eta), would give an x^(-eta) centered
block norm. For a completed even gap of length four, (11) instead gives
a radial factor at most 2x^(-a), before comparison errors.

This requires two genuinely new arithmetic facts to be proved together:

- completion of the actual weighted, restricted integer bridge to the
  complete determinant law, with its constant channel matched to the
  actual major-arc comparison;
- a bound for the remaining short-return schedules, or a decomposition
  in which their full signed contribution is separately controlled.

The prescribed polynomial residue modulus budget does not prohibit
every such block. If a proposed root count has error
S^5 N_0^(-1/100), write S at most x^s and N_0 at least x^n. That
particular error is at most x^(-eta) whenever

$$
 5s+\eta\le n/100.
 \tag{25}
$$

For example n=1/4, s=1/10000 and eta=1/1000 leave a margin 1/1000
in this **single** exponent comparison. This is not a verification of
the other root-count, boundary, list-supply or moment parameters. It
shows that a fixed small collection of polynomial primes is not ruled
out merely by this inequality; the obstruction in Sections 4--6 is
different and must be handled rather than omitted.

In the source's actual raw geometry, fixing the determinant restricts
the next vertex to O(1) possible integer positions after the real
position window is imposed. It therefore does not automatically supply
the p intermediate choices in the proof of (17). The proposed
completion must obtain them by a real arithmetic averaging argument.
Replacing that missing argument by the finite theorem would be a gap.

## 8. Verification and scope

`check_hlc_path_cancellation.py` uses integer path counts and exact
rationals. It verifies the two-step product formula, the full same-line
formula for differing nonzero determinants, paths containing a zero
determinant, both intermediate marginals, the projector error bound,
the two-step retained channel, the alternating active-line schedule,
the largest-group separation argument and integer backtrack lemma,
and the list-symmetrization factor. Its negative controls detect the
false claims that a two-step return is uniform and that a four-step
bridge can ignore an extra middle line condition. All acceptance
checks remain active under `python -O`.

The finite computations exercise identities proved above. They do not
verify the source's full 52-page proof, complete the integer bridge, or
prove any Möbius correlation estimate. The new usable result is the
exact three-step cancellation with its retained projection error; the
unresolved application is stated in Section 7.
