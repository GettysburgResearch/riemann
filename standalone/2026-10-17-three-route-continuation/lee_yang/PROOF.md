# A connected theta moment realization and a negative compensated edge

Status: **proposed computer-assisted finite component theorems; independent
mathematical and code review required. RH is not proved.**

Scope: one exact realization of the original theta moments through degree
16, on a connected ferromagnetic tree with quantitatively positive edges;
and one strictly negative derivative of the 18th moment along the exact
lower-16 moment fiber at the D16 source realization. The constructed tree
does not match degree 18. No cofinal moment ladder or target-reaching
extension theorem is asserted.

Primitive dependency: [PR #886, commit
`d998605c0718e332ac503baf078704b862f8250e`](https://github.com/GettysburgResearch/riemann/tree/d998605c0718e332ac503baf078704b862f8250e/standalone/2026-09-13-astra-theta-degree-sixteen).
Its `primitive.py` and `parameters.json` are copied without alteration as
`pr886_primitive.py` and `pr886_parameters.json`. Both checkers authenticate
the inherited primitive by its exact SHA-256. The edge checker also
authenticates the inherited parameters. This is the same integer interval
backend, with an explicitly extended theta-index range, not an independent
transcendental implementation.

## 1. Exact source and statements

For real $t\geq0$, let

$$
\Phi(t)=\sum_{n\geq1}
 \left(4q_n^2e^{9t/2}-6q_ne^{5t/2}\right)e^{-q_ne^{2t}},
\qquad q_n=\pi n^2,
$$

and extend evenly to the real line. We use the classical theta Fourier
representation, with the convention

$$
\Xi(z)=\int_{\mathbb R}\Phi(t)e^{izt}\,dt,
\qquad
\frac{\Xi(z)}{\Xi(0)}
 =\frac{\xi(1/2+iz)}{\xi(1/2)}.
$$

The normalized identity fixes the convention independently of any constant
used to define $\xi$. The summands on $t\geq0$ are positive, because
$q_ne^{2t}>3/2$. Write

$$
Z=\int_{\mathbb R}\Phi(t)\,dt,\quad
\rho_\theta(dt)=Z^{-1}\Phi(t)\,dt,\quad
v=\mathbb E_{\rho_\theta}T^2,\quad T_*=T/\sqrt v.
$$

The complete source has every exponential moment. The finite source replay
below encloses every even moment through order 18, including normalization,
and verifies $1/25<v<1/20$.

Let $c_n$ be the cumulants of a fair sign, computed by the exact recursion
in Section 3. Put

$$
s_r=\frac{\kappa_{2r}(T_*)}{c_{2r}},\qquad 1\leq r\leq9.
$$

All nine denominators are nonzero integers. In particular,
$c_{18}=209865342976$. Cumulants here are formal derivatives at zero;
no logarithm across unknown zeros of $\Xi$ is used.

### Theorem T16C: a quantitatively connected realization

There is a zero-field ferromagnetic Ising measure on a tree with 281
vertices and 280 edges, and a nonnegative weighted spin observable $Y$,
such that

$$
\mathbb E Y^{2r}=\mathbb E T_*^{2r}\quad(1\leq r\leq8),
\qquad \mathbb E Y^{2r+1}=0\quad(r\geq0).
\tag{1}
$$

Every physical edge coupling satisfies the strict bounds

$$
\frac1{200000}<J_e<\frac14.
\tag{2}
$$

Every observed spin has strictly positive weight. A single auxiliary hub
has weight zero. The characteristic function of $Y$ has only real zeros.

The next standardized moment is separated from the target:

$$
\frac{34}{1000}
 <\mathbb E Y^{18}-\mathbb E T_*^{18}
 <\frac{35}{1000}.
\tag{3}
$$

The weighted observables of the two designated large dimers have covariance
strictly greater than $1/60000$. Thus the construction includes a quantified
nonzero correlation between distinct old components.

The parameters are the unique root in the eight-coordinate box specified
by `tree_parameters.json`, with radius $10^{-30}$ and active coordinates
$0,1,2,3,4,5,6,8$. This is uniqueness in that box only. The corresponding
physical observable $X=\sqrt vY$ exactly matches the original, unstandardized
theta moments through degree 16.

### Theorem CER: a decreasing next-moment direction

At the exact D16 realization of PR #886, connect the roots of the dimers
with squared-amplitude indices 6 and 7 by an edge of coupling $J$, and set
$h=\tanh J$. There is a real analytic germ of positive observable weights
at $h=0$ preserving every theta moment through degree 16, with the same
eight active coordinates as D16. Along this germ,

$$
-\frac{785}{1000}
 <\left.\frac{d}{dh}\left(\mathbb E Y_h^{18}
                 -\mathbb E T_*^{18}\right)\right|_{h=0}
 <-\frac{784}{1000}.
\tag{4}
$$

Consequently some sufficiently small positive ferromagnetic edge decreases
the next-moment discrepancy while preserving all the lower prescribed
moments. No quantitative interval reaching discrepancy zero follows from
this germ, and none is claimed. The separately certified tree in T16C is
the finite construction achieved here.

## 2. The complete tree measure

The 17 parameters are

$$
z=(a_0,\ldots,a_{10},\eta,p_0,\ldots,p_4).
$$

There are six sign groups of multiplicities
$\nu=(256,10,1,1,1,1)$, five dimers, and one auxiliary hub $\varepsilon$.
Each sign connects directly to the hub. The first spin $\sigma_j$ of every
dimer $(\sigma_j,\tau_j)$ connects to the hub; the second connects to the
first. This gives $270+10+1=281$ vertices, $270+5+5=280$ edges, and a tree.

For component types $i=0,\ldots,10$, define

$$
k_i=\begin{cases}3&i=6,7,\\1/100&\text{otherwise},\end{cases}
\qquad m_i=\eta k_i a_i.
$$

The hub edge of component type $i$ has coupling $\operatorname{atanh}m_i$.
Dimer $j$ has internal coupling $\operatorname{atanh}(2p_j-1)$. The exact
box checks ensure $0<m_i<1$ and $1/2<p_j<1$, so these are finite, positive
couplings. The observable is

$$
Y=\sum_{i=0}^{5}a_i\sum_{\ell=1}^{\nu_i}\sigma_{i\ell}
    +\sum_{j=0}^{4}\frac{a_{6+j}}2(\sigma_j+\tau_j).
\tag{5}
$$

The hub is absent from (5). Its weight is zero, not a missing vertex or an
omitted interaction. For orientation only, the center parameters are
approximately

| Parameter | Approximate value |
|---|---:|
| $a_0$ | 0.0235623104560 |
| $a_1$ | 0.1057541468311 |
| $a_2$ | 0.2429999227587 |
| $a_3$ | 0.2921154609050 |
| $a_4$ | 0.3475952070635 |
| $a_5$ | 0.5169675707248 |
| $a_6,a_7$ | 0.3001150930396, 0.2914611062796 |
| $a_8,a_9,a_{10}$ | 0.2359688705215, 0.2903191367936, 0.2359688705215 |
| $\eta$ | 0.0286805336872 |
| $p_0,p_1$ | 0.5898152853161, 0.6079659190867 |
| $p_2,p_3,p_4$ | 0.5143486219554, 0.6107894280098, 0.5143486219554 |

The table is not the parameter definition. The exact terminating-rational
centers, the active box, and the moment equations define the result.

### Conditional factorization includes every configuration

Condition on the hub being $+1$. A sign of type $i$ has mean $m_i$. For a
dimer, summing over its second spin gives $2\cosh J_j$, independent of its
root spin. Its root therefore also has mean $m_i$. The alignment variable
$r=\sigma_j\tau_j$ is independent of that root, with
$\mathbb P(r=1)=p_j$. Thus $W_j=(\sigma_j+\tau_j)/2$ equals $\sigma_j$ when
$r=1$ and zero otherwise.

Write $q_i=1$ for sign types and $q_{6+j}=p_j$ for dimers. The conditional
raw moments of a single component contribution are exactly

$$
M_{i,0}=1,\qquad
M_{i,n}=\begin{cases}
q_i a_i^n&n\text{ even},\\
q_i m_i a_i^n&n\text{ odd}.
\end{cases}
\tag{6}
$$

Conditional on the hub, all 275 components are independent. Summing the
component partition functions also shows that the hub marginal is a fair
sign. Switching the hub changes every component observable to its negative
in distribution. The unconditional even moments are the conditional even
moments; every unconditional odd moment is zero. Equation (6) therefore
accounts for the complete $2^{281}$-configuration measure without an
enumeration or state cutoff.

For the two large dimers, conditional independence gives

$$
\operatorname{Cov}(a_6W_0,a_7W_1)
 =p_0p_1a_6a_7m_6m_7.
\tag{7}
$$

The interval checker proves the strict lower bound on (7). It also checks
the bounds in (2): for $0<c<1$,
$c\leq\operatorname{atanh}c\leq c/(1-c^2)$; every checked lower and upper
comparison has a strict margin.

## 3. Exact moment equations and root certification

For a raw moment list $M_0=1,M_1,\ldots,M_n$, compute cumulants by

$$
K_n=M_n-\sum_{j=1}^{n-1}\binom{n-1}{j-1}K_jM_{n-j}.
\tag{8}
$$

Apply (8) to (6), add the component cumulants with their integer
multiplicities, and recover the conditional moments from

$$
M_n=\sum_{j=1}^{n}\binom{n-1}{j-1}K_jM_{n-j}.
\tag{9}
$$

Set the odd moments to zero and apply (8) again. If $A_r(z)$ denotes the
resulting $2r$th cumulant divided by $c_{2r}$, the finite equations are

$$
G_r(z)=A_r(z)-s_r=0,\qquad1\leq r\leq8.
\tag{10}
$$

Every $A_r$ is a polynomial over the rationals in the declared parameters.
Equations (8) and (9) are triangular identities, so (10) implies (1).
`flexible_tree.py` implements these equations, and forward differentiation
in `tree_core.py` evaluates their Jacobian with the same exact polynomial
operations.

Let $c$ be the exact rational center and $B$ its specified active box,
with common radius $\rho=10^{-30}$. The nine inactive parameters remain
fixed at their rational centers. The checker computes the exact rational
Jacobian $J_0=DA(c)$ in the eight active variables, inverts it over the
rationals, and verifies both matrix products are the identity. Write its
inverse as $R$. Directed interval arithmetic gives

$$
\beta\geq\|RG(c)\|_\infty,\qquad
L\geq\sup_{z\in B}\|I-RDA(z)\|_\infty.
$$

The acceptance predicates are the strict rational inequalities

$$
L<10^{-3},\qquad\beta<\rho/1000,\qquad
\rho-\beta-L\rho>99\rho/100.
\tag{11}
$$

Their diagnostic approximations in the produced receipt are
$\beta\approx5.13\cdot10^{-44}$ and $L\approx4.38\cdot10^{-15}$.
The diagnostics are not used for acceptance. The map $z\mapsto z-RG(z)$
is a strict contraction of $B$ into itself by (11). Banach's theorem gives
a unique fixed point there, and invertibility of $R$ makes it a root of
(10). Every positivity assertion is checked throughout the box.

The checker separately encloses $c_{18}(A_9(z)-s_9)$ and the direct raw
moment difference $M_{18}(z)-\mathbb E T_*^{18}$ throughout $B$. Each lies
strictly in $(34/1000,35/1000)$. At the root the cumulant and raw differences
are identical, because all lower cumulants agree. This proves (3) without
depending on an approximate solver residual.

As an independent finite check of the model encoding, `controls.py`
enumerates all 128 configurations of a seven-spin tree containing two
signs of a common type and two dimers. It compares every exact raw moment
of orders 0 through 18 with the same conditional moment code, verifies
normalization, and rejects the incorrect formula omitting the dimer factor
$1/2$. This checks multiplicities, the hub conditioning, and the observable
normalization. It does not replace the source replay or contraction proof.

## 4. Complete six-index theta replay

This section rederives the remainder bounds after extending the inherited
explicit theta range from four indices to six. No stored moment receipt is
read by either checker to establish the target.

For $n=1,\ldots,6$, integrate to

$$
U_n=(2,3/2,1,3/4,1/2,3/8)_n.
$$

Use width-$1/16$ cells, with midpoint $c$ and half-width $h=1/32$.
There are respectively $(32,24,16,12,8,6)$ cells, 98 in total. Expand each
source summand in $(t-c)/h$ through degree $D=120$ and integrate its
product with each $t^j$, $j=0,2,\ldots,18$, exactly at the polynomial level.
The full-line factor two is retained.

### Taylor remainder, including the enlarged index range

On the complex circle $|t-c|=1/8$, one has
$|\operatorname{Im}t|\leq1/8$, hence $\operatorname{Re}e^{2t}>0$ and
$|e^{-q_ne^{2t}}|\leq1$. Also $\operatorname{Re}t<17/8$ and, now for every
explicit index $n\leq6$, $q_n<144$. Using $e<3$, the prefactor modulus is
bounded by

$$
4\cdot144^2\cdot3^{10}+6\cdot144\cdot3^6<10^{11}.
$$

Thus the same convenient majorant remains valid after the index extension.
Cauchy's coefficient estimate bounds the remainder on a real cell by
$10^{11}4^{-121}/(1-1/4)$. All real cells lie in $[0,2]$, so $t^j\leq2^j$.
The sum of the full-line integration lengths is $2\sum_nU_n=49/4<16$.
A valid total moment error is therefore

$$
E_j=\frac{16\cdot10^{11}\cdot2^j}{4^{121}(3/4)}.
\tag{12}
$$

### All six time tails

For $t=U+u$, let $q=\pi n^2$, $E=e^{2U}$, and
$\lambda=2qE-9/2>0$. Dropping only the negative second prefactor term and
using $e^{2u}\geq1+2u$ gives the complete full-line tail bound

$$
T_{n,j}=8q^2e^{9U/2-qE}
 \sum_{k=0}^j\binom jk U^{j-k}\frac{k!}{\lambda^{k+1}}.
\tag{13}
$$

All six bounds (13) are included for every declared moment.

### Every omitted theta index

The same bound from $U=0$ gives
$8\pi^2n^4e^{-\pi n^2}j!/(2\pi n^2-9/2)^{j+1}$ for index $n$.
For $n\geq7$, the ratio of the numerator at $n+1$ to that at $n$ is at most
$(8/7)^4e^{-15\pi}<1/2$, and the denominator increases. The whole sum over
$n\geq7$ is consequently bounded by

$$
N_j=\frac{16\pi^2\,7^4e^{-49\pi}j!}{(98\pi-9/2)^{j+1}}.
\tag{14}
$$

No discarded theta summand or time tail is set to zero. Positivity makes
(13) and (14) one-sided additions to the upper bound; (12) is paid on both
sides of the polynomial integral. Normalization and variance divisions are
then performed outward, followed by the exact recursions (8).

### Arithmetic contract

All interval endpoints are integers divided by $2^{320}$. Addition is
exact at that scale; multiplication and division use integer floor and
ceiling; square roots use integer square root with an upward correction.
The primitive allows only integers, rational `Fraction` values, and these
intervals. No binary or decimal floating-point value enters acceptance.

The inherited $\pi$ enclosure uses Machin's identity and 96-term alternating
arctangent series, with the first omitted term included. To enclose an
exponential, scale its nonnegative argument into $[0,1/8]$, use 96 positive
Taylor terms and the geometric bound starting with term 97, then repeatedly
square outward; use an outward reciprocal for a negative argument.
The polynomial exponential recursions and all cell integrations use these
same directed operations. These facts justify the enclosures used in
(12)--(14) and in the finite moment map.

## 5. Lee--Yang with a zero-weight hub

The imported theorem is the finite, zero-field ferromagnetic Lee--Yang
theorem with arbitrary nonnegative real observable weights. One explicit
statement is Newman and Wu, *Constants of de Bruijn--Newman type in analytic
number theory and statistical physics*, [arXiv:1901.06596v2, Section 2.5,
equation (21) and the following display](https://arxiv.org/html/1901.06596v2#S2.SS5).
It gives only real Fourier zeros for a finite Gibbs measure with
$J_{ij}\geq0$ and weights $\lambda_i\geq0$. Unequal and irrational weights
are permitted.

For clarity, even the version requiring strictly positive weights suffices
here. Add weight $\delta>0$ to the hub, keeping all couplings and other
weights fixed. Each resulting characteristic function has no zeros in
either open half-plane. As $\delta\downarrow0$, the finite configuration sum
converges uniformly on every compact subset of $\mathbb C$ to the
characteristic function of (5). The limit is entire and takes the value
one at zero. It therefore cannot be identically zero in either half-plane:
the identity theorem would contradict its value at zero. Hurwitz's theorem
now implies that the limit has no zeros in either open half-plane. This
justifies the zero observable weight on the hub without deleting it or
changing the interaction graph. Multiplying $Y$ by $\sqrt v>0$ preserves
the real-zero property.

This is a real-zero statement about the constructed finite-spin function.
Its eight even-moment constraints end at degree 16, and its degree-18
discrepancy is explicitly positive. It is not identified with $\Xi/Z$.

## 6. Proof of the compensated-edge theorem

Let $x=(x_0,\ldots,x_{10})$ be the squared-amplitude coordinates of D16,
with the inherited fixed coordinates $6,8,10$ and active coordinates
$0,1,2,3,4,5,7,9$. Each dimer has alignment probability $p=3/5$.
If $d_{2r}$ are the cumulants of the dimer variable $W$, define
$\alpha_r=d_{2r}/c_{2r}$. Its disconnected moment equations are

$$
A_r(x)=\sum_{i=0}^5\nu_ix_i^r
        +\alpha_r\sum_{i=6}^{10}x_i^r=s_r.
\tag{15}
$$

`edge_parameters.json` gives a newly refined radius-$10^{-30}$ box for this
same source root. The checker verifies that its fixed coordinates are
exactly the inherited ones, that the entire new box lies inside the
original D16 radius-$10^{-14}$ box, and that the source-replayed equations
(15) have a unique root in the new box. The same rational-inverse
contraction argument used in Section 3 proves this assertion directly.

For a dimer of amplitude $a$, write its moment generating function and
root-spin weighted moment generating function as

$$
M_a(t)=1-p+p\cosh(at),\qquad N_a(t)=p\sinh(at),\qquad
R_a(t)=N_a(t)/M_a(t).
$$

At $h=0$, the two dimers are independent, their root spins have mean zero,
and adding the edge factor $1+h\sigma_0\sigma_1$ leaves its normalization
equal to one. The joint moment generating function of these two dimer
contributions becomes exactly

$$
M_{a_6}(t)M_{a_7}(t)+hN_{a_6}(t)N_{a_7}(t).
$$

Consequently the derivative at zero of its formal cumulant generating
function is $R_{a_6}(t)R_{a_7}(t)$. Define

$$
D_r(x)=\frac{(2r)!}{c_{2r}}[t^{2r}]
                 R_{\sqrt{x_6}}(t)R_{\sqrt{x_7}}(t).
\tag{16}
$$

The denominator series has constant term one, so all coefficients required
in (16) through degree 18 are obtained by finite exact divisions of formal
series. Square roots of positive boxed coordinates are enclosed outward.
The normalized lower Jacobian at the source root is

$$
J_{r,k}=r(\nu_k\mathbf1_{k<6}+\alpha_r\mathbf1_{k\geq6})x_k^{r-1}.
$$

Its invertibility follows from the root contraction. The analytic implicit
function theorem provides a real analytic germ $x(h)$ preserving (15) for
$r\leq8$, with
$x'(0)=-J^{-1}(D_1,\ldots,D_8)^\mathsf T$. All weights remain positive for
sufficiently small $|h|$. For $h>0$ sufficiently small, the new edge has
positive coupling $J=\operatorname{atanh}h$, so it is admissible.

Since the first eight even cumulants are fixed, the derivative of the raw
18th moment equals that of its cumulant. It is exactly

$$
c_{18}\left(D_9-J_9J^{-1}(D_1,\ldots,D_8)^\mathsf T\right).
\tag{17}
$$

Here $J_9$ is the ninth row of the same normalized derivative formula.
To enclose the inverse response without substituting the rational center
for the actual root, the checker uses $R=J_0^{-1}$ and the already bounded
$E=I-RJ$, with $\|E\|_\infty\leq L<1$. Write $w=-RD$ and
$u=-J^{-1}D$. Since $u=w+Eu$,

$$
\|u-w\|_\infty\leq\frac{L}{1-L}\|w\|_\infty.
\tag{18}
$$

Both $w$ and $J_9$ are evaluated on the entire source root box. Adding the
explicit error (18) and evaluating (17) yields the strict interval (4).
The diagnostic interval is approximately
$(-0.784428553114283,-0.784428553114266)$, and the exact integer endpoints
are in `edge_certificate.json`. The old discrepancy is independently
checked to remain in $(169/1000,170/1000)$.

## 7. What the finite result leaves open

The new graph reaches the degree-16 target with every edge bounded below,
and its next-moment discrepancy is smaller than the previous D16 box.
The edge theorem proves that compensated ferromagnetic perturbations can
move that discrepancy in the needed direction at this actual source
point. These are exact finite statements.

No theorem here shows that the remaining positive discrepancy can be
removed while preserving positivity and the lower moments. The failed
searches recorded in `EXPLORATION.md` are not separating inequalities and
do not rule out any full architecture. In particular, a local inverse
Jacobian does not give a global continuation interval.

The Lee--Yang route to RH still requires finite ferromagnets reaching the
original theta moment targets at unbounded orders, with the convergence
and source-identification hypotheses of the separate all-order consumer.
Neither a fixed finite realization, its numerical next-moment improvement,
nor graph connectivity supplies those quantifiers.

## 8. Reproduction and review boundary

Run, in the packet directory, using standard Python 3:

```sh
sha256sum --check SHA256SUMS
python3 certify_tree.py --check tree_certificate.json
python3 certify_edge.py --check edge_certificate.json
```

The first command authenticates the frozen packet. Each checker regenerates
the complete theta source and its remainders, recomputes the exact rational
inverse and interval inequalities, and compares its complete result with
the declared receipt. `certify_tree.py` also runs the full seven-spin exact
enumeration. Ordinary high-precision optimizers were used only to propose
rational centers; their outputs are not accepted as roots or as moment
data. The proof claim depends on the source analysis, polynomial identities,
and strict replay predicates above, followed by independent review of the
frozen packet.
