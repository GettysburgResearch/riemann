# Root and recorded-line averaging for the actual cofactor phases

**Status: exact averaging identities, quantitative joint-event bounds,
and a fixed-path arithmetic bound.** This note uses the cofactor
frequencies occurring when a departing prime is omitted from a complete
list. It retains the moving center in the dirty phase equation and pays
the recorded-line average exactly once. It does not prove a complete
multi-edge law for the HLC integer paths or a new zero-free region.

The precise remaining issue is conditional: after a prime's line has
already been recorded, its value and the current root phase are coupled
to the preceding path. The joint estimates below can be used after that
conditioning only when the past event and its mass have also been
identified. An explicit repeated-event example shows why this cannot
be omitted.

The source geometry and measures are those of
[Lü--Wang--Wu, arXiv:2610.20242v1](https://arxiv.org/html/2610.20242v1),
equations (4.35)--(4.40) and (4.47)--(4.50), as retained and checked in
[HLC_PATH_CANCELLATION.md](HLC_PATH_CANCELLATION.md). This note is
separate from that frozen operator review.

## 1. Exact cofactor averaging

Let p_1,...,p_m be distinct primes, P their product, and n_i=P/p_i.
For bounded measurable one-periodic functions f_i,

$$
 \boxed{
 \int_0^1\prod_{i=1}^m f_i(n_i R)\,dR
 =\int_0^1\prod_{i=1}^m
   \left\{\frac1{p_i}\sum_{b=0}^{p_i-1}
                f_i\left(\frac{s+b}{p_i}\right)\right\}\,ds .}
 \tag{1}
$$

Split R=(s+k)/P, with 0<=s<1 and 0<=k<P. Then n_i R=(s+k)/p_i.
The residues k modulo the distinct p_i are independent under uniform
k by the Chinese remainder theorem. This proves (1), including its
normalizing factors. A common nonzero integer multiple of all n_i leaves the
left integral unchanged after a measure-preserving circle map.

For smooth functions, the same identity describes the exact Fourier
resonances. A relation sum_i h_i n_i=0 forces p_i to divide h_i,
by reducing modulo p_i. Writing h_i=p_i a_i leaves sum_i a_i=0.
Thus

$$
 \int_0^1\prod_i f_i(n_iR)\,dR
       =\sum_{a_1+\cdots+a_m=0}\prod_i\widehat f_i(p_i a_i).
 \tag{2}
$$

The nonzero resonances in (2) need not vanish. It is incorrect to call
the whole phase vector independent. What is exact is independence of
the grid residues conditional on the common microphase s in (1).

For an arc I of length ell, a translated grid of p equally spaced
points meets I in at most p ell+1 points. Therefore (1) gives

$$
 \int_0^1\prod_i1_{I_i}(n_iR+\theta_i)\,dR
                  \le\prod_i\left(\ell_i+\frac1{p_i}\right).
 \tag{3}
$$

There is also the lower bound given by the product of
max(0,ell_i-1/p_i). Arc endpoints have measure zero and do not affect
these assertions.

For short arcs with ell_i<=1/p_i, formula (1) is even more explicit:
each grid average is p_i^(-1) times the indicator of the dilated arc
p_i(I_i-theta_i) modulo one. The whole integral is P^(-1) times the
measure of the intersection of these dilated arcs. This exhibits the
remaining correlation instead of suppressing it. When every
ell_i=1/p_i, each grid average is exactly 1/p_i almost everywhere,
so the product integral is exactly 1/P for every translation.

## 2. The moving dirty center and its one line average

Fix another prime p_0, not among the p_i, and integers C,H such that

$$
 (p_0,HP)=1,\qquad(C,P)=1.
$$

Set

$$
 G=HP,\qquad n_i=C P/p_i,\qquad
 A_i=p_0 n_i-G=(P/p_i)(p_0C-Hp_i).
 \tag{4}
$$

The A_i are nonzero: A_i=0 would imply p_0 divides G. Let R be
uniform on [0,1] and h uniform modulo p_0, initially independent.
For fixed one-periodic test functions, define

$$
 \mathcal I=\frac1{p_0}\sum_{h=0}^{p_0-1}\int_0^1
 \prod_i f_i\left((n_i-G/p_0)R-h/p_0+\theta_i\right)\,dR.
 \tag{5}
$$

**Theorem 1 (the recorded-line root average).** Exactly,

$$
 \mathcal I=\int_0^1\prod_i f_i(A_i t+\theta_i)\,dt
 \tag{6}
$$

and

$$
 \mathcal I=\int_0^1\prod_i
 \left\{\frac1{p_i}\sum_{b=0}^{p_i-1}
 f_i\left(\frac{p_0C-Hp_i}{p_i}s+\frac b{p_i}+\theta_i\right)
 \right\}\,ds.
 \tag{7}
$$

In particular, for arcs I_i of lengths ell_i,

$$
 \boxed{\Pr(E_1\cap\cdots\cap E_m)
                  \le\prod_i(\ell_i+1/p_i),}
 \tag{8}
$$

where E_i is the corresponding event in (5).

### Proof and normalizers

Integer translation R by j changes every argument with h=0 by
-jG/p_0 modulo one. Since G is invertible modulo p_0, these p_0
translations permute all the h choices. Thus (5) is precisely

$$
 \frac1{p_0}\int_0^{p_0}
     \prod_i f_i((n_i-G/p_0)R+\theta_i)\,dR.
$$

Put R=p_0 t. The factor p_0 from this change of variable cancels the
normalizer, proving (6). No extension from one root interval to p_0
intervals has been made without paying the line average.

Now split t=(s+k)/P. Since

$$
 A_i t=\frac{p_0C-Hp_i}{p_i}s+\frac{p_0Ck}{p_i}-Hk,
$$

the integer Hk drops out. Multiplication by p_0 C permutes residues
modulo each p_i, and the Chinese remainder theorem gives (7).
The translated-grid bound proves (8). QED.

The smooth Fourier version retains the exact resonant lattice:

$$
 \sum_i h_iA_i=0
 \quad\Longleftrightarrow\quad
 h_i=p_i a_i\ (1\le i\le m),\qquad
 \sum_i a_i(p_0C-Hp_i)=0.
 \tag{9}
$$

The implication from left to right again follows by reduction modulo
each p_i; the converse follows by substitution. This is the precise
replacement for an assumption that no phase relation exists.

### Which source cofactors have this form

Hold fixed the omissions and incoming choices in the lower prime
groups, and vary which prime p_i is omitted from one complete list in
the largest group. Its complete product is P. If H is the product of
the other complete lists, the current full product is G=HP. The
product of the fixed lower shared entries and the fixed lower incoming
entries is C. The possible incoming full products for a fixed memory
prime p_0 are p_0 C P/p_i. The raw equation and recorded line yield

$$
 \left\|n_iR-\frac{GR+h}{p_0}\right\|\le16/p_0,
 \tag{10}
$$

which is exactly the phase in (5), with an arc of length at most
32/p_0. All primes in C are in other groups; p_0 is excluded from the
complete current list. Thus the stated coprimalities are the actual
ones. If extra restrictions delete candidates, the upper bound remains
valid.

For a fixed current vector z and complement w with det(z,w)=1,
the line of Gw+hz runs through every projective line except [z] as
h runs through F_(p_0). The excluded line cannot solve a nonzero
determinant equation. Therefore the original uniform projective-line
average is

$$
 \frac1{p_0+1}\sum_{h\bmod p_0}(\cdots)
      =\frac{p_0}{p_0+1}\,E_h(\cdots).
 \tag{11}
$$

The factor in (11) is paid once. It is not an extra factor at every
reuse of a recorded line. Theorem 1 is first a statement with the
uniform real phase measure in (5). The following conversion pays its
change of measure for fixed source labels; conditioning on a past path
remains a separate issue.

### Conversion to the actual real root

In the source's equation (4.29), the real root variable has measure
dr on [0,1]. For fixed u,v and fixed primitive integer z with a fixed
integer complement w, det(z,w)=1, its equation (4.28) gives

$$
 \tau_r(z)=z_1-2rz_2,\qquad
 R(r)=\frac{\tau_r(w)}{\tau_r(z)},\qquad
 R'(r)=-\frac{2}{\tau_r(z)^2}.
 \tag{11a}
$$

The sign is negative with the source's convention for tau. The
retained position range (4.33), together with
`1<=u/(d_0YM)<=16`, implies `1/16<=tau_r(z)<=16`.
Its allowed r set is an interval; remaining position and good-state
projectors may restrict it further. On that interval,

$$
 \frac1{128}\le |R'(r)|\le512,
                    \qquad \left|\frac{dr}{dR}\right|\le128.
 \tag{11b}
$$

The image interval has length at most 512 by the derivative bound.
Integrality improves this to less than 16 when z_2 is nonzero:

$$
 R(r)=\frac{w_2}{z_2}-\frac1{z_2\tau_r(z)},\qquad
 |R(I)|\le\frac{16-1/16}{|z_2|}<16.
$$

When z_2=0, primitivity and positive tau imply z_1=1, and the image
length is at most two. Thus in either case at most 17 consecutive
integer unit intervals cover the image. The h-averaged nonnegative
event density in (5) is one-periodic in R: unit translation permutes
h because G is invertible modulo p_0. Combining (8), (11), and the
Jacobian bound proves, with `C_root=2176=128*17`,

$$
 \boxed{
 \int_{I_z}\frac1{p_0+1}\sum_{h\bmod p_0}
   \Psi(r,h)\prod_i1_{E_i(r,h)}\,dr
 \le C_{\rm root}\frac{p_0}{p_0+1}
                        \prod_i(\ell_i+1/p_i).}
 \tag{11c}
$$

Here `0<=Psi<=1` may include every retained endpoint or good-state
projector, and I_z is the r interval allowed by the tau range.
The data z,w,p_0,p_i,C,H and the arc translations are held fixed
independently of r. The other source variables u,v are fixed at this
step; their displayed measure in (4.29) can subsequently be integrated
without any new prime-dependent normalizer. This is an unnormalized
root-and-line average. No marginal equality, or conditional-history
lower bound, is asserted for this restricted source measure.

### Averaged ambiguity among different omissions

For m current-list omissions, put N=sum_i 1_(E_i). With the uniform
measure of (5),

$$
 \mathbb E\{N(N-1)\}
 \le\sum_{i\ne j}(\ell_i+1/p_i)(\ell_j+1/p_j).
 \tag{11d}
$$

This follows by expanding N(N-1) and applying (8) to each distinct
pair with the same fixed labels and the same one line draw. For the
actual source root-and-line measure the right side acquires at most
the factor `C_root*p_0/(p_0+1)`, by (11c). Since
`1_(N>=2)<=N(N-1)/2`, if all p_i are at least c p_0 for a fixed
c>0 and all dirty arcs have length at most 32/p_0, then

$$
 \int_{I_z}\frac1{p_0+1}\sum_h
       \Psi(r,h)1_{N(r,h)\ge2}\,dr
 \le C_{\rm root}\frac{p_0}{p_0+1}
          {m\choose2}\frac{(32+c^{-1})^2}{p_0^2}.
 \tag{11e}
$$

This is a genuine averaged uniqueness estimate for this fixed
cofactor family. A polynomial p_0 and subpower m give a fixed-power
bound for this unnormalized ambiguous mass. It is stronger than
requiring separation of all candidate phases for every good root.
For a nonnegative weighted family of such fixed-label tests, Tonelli
gives the same bound multiplied by the total family weight. Controlling
that weight in the complete path expansion, or dividing by the mass
of a previous history, is still necessary before a whole-operator
conclusion. In particular (11e) is not an operator-norm estimate.

## 3. A rigorous conditional two-window bound

Take two distinct current-list cofactors, with associated p_1,p_2.
Each marginal in (5) has exactly its arc length ell_i, by (6) and
the nonzero integer frequency A_i. Consequently, if ell_1>0,

$$
 \boxed{\Pr(E_2\mid E_1)
       \le\frac{(\ell_1+1/p_1)(\ell_2+1/p_2)}{\ell_1}.}
 \tag{12}
$$

If ell_i p_i is at least c>0 for each i, the right side is at most
`(1+1/c)^2 ell_2`. Thus the dirty-window scale ell_i comparable to
1/p_0 is permitted when the two current cofactor primes are comparable
to p_0. No high-frequency tail estimate or smoothing loss is needed
for this upper bound.

Suppose instead that an actual past event A is a subset of E_1 with
relative mass rho=Pr(A)/Pr(E_1)>0. Then

$$
 \Pr(E_2\mid A)
       \le\rho^{-1}
          \frac{(\ell_1+1/p_1)(\ell_2+1/p_2)}{\ell_1}.
 \tag{13}
$$

This is a concrete conditional interface: the geometry of the past
event and its relative mass must both be proved. Arbitrary endpoint
or good-state projectors bounded between zero and one can be retained
in an **unnormalized** joint-event upper bound, since they only delete
mass. Dividing by the surviving mass requires precisely the factor
displayed in (13).

The case of a repeated phase is completely different. If E_2=E_1,
then Pr(E_2|E_1)=1, however short the interval is. The largest-group
two-step backtrack identified in `HLC_PATH_CANCELLATION.md` has exactly
this kind of resonance: its reversed previous edge supplies the same
phase candidate. It must not be assigned the bound for two distinct
cofactors.

The hypotheses do not say that successive HLC edges automatically
produce two events of the form (5) with common fixed data. They prove
the estimate **when** that exact identification is available. In a
general recorded path, the current relative vector, its complement,
and the residue h are functions of earlier choices. The missing
arithmetic task is to identify a class of surviving non-backtracking
paths for which those dependencies admit (13) with a sufficiently
large rho, or another explicitly controlled density. This note does
not make that identification for the full source operator.

## 4. A second actual arithmetic gain after fixing a path

There is a simple power bound for a recorded prime joining two fixed
distinct primitive integer vertices. Let tau be a real linear form
positive on z,z', and suppose both are primitive. If det(z,z')=0,
their rational proportionality and primitivity give z'=z or z'=-z;
positivity excludes the second option. Hence distinct vertices have

$$
                       \Delta=\det(z,z')\ne0.
$$

The common recorded line condition for a prime p is exactly
p divides Delta. If every prime in a set mathcal P is at least P_min
and its original selection weight satisfies
nu(p)<=C/(V p), then

$$
 \boxed{\sum_{\substack{p\in\mathcal P\\[z]_p=[z']_p}}\nu(p)
      \le\frac C{V P_{\min}}
                  \frac{\log|\Delta|}{\log P_{\min}}.}
 \tag{14}
$$

The right side is interpreted as zero when |Delta|=1. Every distinct
prime divisor counted on the left contributes at least log P_min to
log|Delta|, proving the formula. If a prime divides both coordinates
of a vertex the projective line would be undefined, but primitivity
excludes that case.

For |Delta|<=x^C_1, P_min>=x^a, and V^(-1)=x^(o(1)), (14) is
at most x^(-a+o(1)). This charges the original prime-selection
weight once. There is no independent prime redraw at the return.
The exact repeated-position case Delta=0 is the resonance for which
this divisor estimate supplies no saving.

### Why the O(1) successor count does not yet sum (14)

The source's raw successor with incoming memory prime p has the form

$$
 j(p)=G-pDZ,\qquad z'(p)=j(p)w_z+h(p)z,
 \tag{15}
$$

where h(p) lies in an interval of bounded length centered near
-j(p)tau(w_z)/tau(z). There are O(1) h values **after p is fixed**.
For an earlier recorded vertex z_old, the determinant needed in (14)
is now

$$
 \Delta(p)=j(p)\det(z_{\rm old},w_z)
                       +h(p)\det(z_{\rm old},z).
 \tag{16}
$$

The integer h(p), and therefore Delta(p), varies with the prime being
summed. Even modulo p, the second term retains this dependence. A
bound on the number of divisors of one fixed Delta cannot be applied
to that family of different integers. Conversely, fixing all path
vertices first makes (14) valid but loses the O(1)-successor
summation order; the resulting number of possible relative paths
must then be bounded separately.

This is the exact unresolved dependency, rather than a claim that
the divisor estimate fails or that future completion is impossible.
The root-phase theorem and the fixed-path divisor theorem supply two
different genuine gains, but combining them requires a proof that
does not change the conditioning midway through the count.

## 5. The same cofactor identity over the Eisenstein field

There is also an exact field-compatible version. It uses Haar measure
on an explicitly stated complex torus; it does not supply a root
distribution for the native inverse detector.

Let `O=Z[omega]`, `omega=exp(2 pi i/3)`, and let Q be a fundamental
parallelogram, with normalized measure `dA/c_O`, where
`c_O=sqrt(3)/2`. Let pi_1,...,pi_m be nonassociate prime elements,
put `P=product pi_i`, and take another prime element pi_0. Require
`(pi_0,HP)=O` and `(C,P)=O`. Put

$$
 G=HP,\qquad n_i=CP/\pi_i,\qquad
 A_i=\pi_0n_i-G,\qquad q_i=\mathrm N\pi_i.
$$

For O-periodic bounded measurable f_i, exactly

$$
 \begin{split}
 &\frac1{q_0}\sum_{h\in O/(\pi_0)}\int_Q
   \prod_i f_i((n_i-G/\pi_0)R-h/\pi_0+\theta_i)
                                      \frac{dA(R)}{c_O}\\
 &=\int_Q\prod_i f_i(A_it+\theta_i)\frac{dA(t)}{c_O}\\
 &=\int_Q\prod_i\left\{
    \frac1{q_i}\sum_{b\in O/(\pi_i)}
    f_i\left(\frac{\pi_0C-H\pi_i}{\pi_i}s
                         +\frac b{\pi_i}+\theta_i\right)
                         \right\}\frac{dA(s)}{c_O}.
 \end{split}
 \tag{17}
$$

To prove the first equality, multiplication by G permutes the
residues modulo pi_0. Translates `Q+j`, for representatives
`j in O/(pi_0)`, form a fundamental domain for the sublattice
pi_0 O. The product integrand with h=0 is pi_0 O-periodic, so the
sum of these integrals equals its integral over pi_0 Q. The change
`R=pi_0 t` multiplies real area by q_0 and cancels the displayed
normalizer. For the second equality use the degree-NP covering of the
torus by multiplication by P, namely `t=(s+k)/P` with
`k in O/(P)`. The integer-ring term `Hk` vanishes by periodicity,
and the CRT independently permutes `pi_0 Ck mod pi_i`. This proves
all normalizers in (17) without assuming independent continuous
phases.

For a geometric bound, let each f_i be the indicator of an embedded
torus disk of radius r_i<1/4. A translate of the pi_i-torsion grid
has at most

$$
                (2r_i\sqrt{q_i}+1)^2
$$

points in that disk. Indeed, lift the disk to the complex plane.
Distinct lifted grid points are separated by at least `1/sqrt(q_i)`,
because the shortest nonzero Eisenstein lattice vector has length one.
Disjoint disks of radius `1/(2 sqrt(q_i))` around these points lie
in the disk of radius `r_i+1/(2 sqrt(q_i))`. Comparing ordinary
Euclidean areas proves the count. Consequently (17) gives

$$
 \boxed{\Pr\Bigl(\bigcap_i E_i\Bigr)
          \le\prod_i(2r_i+q_i^{-1/2})^2.}
 \tag{18}
$$

The marginal equals the normalized area of its disk, since each
nonzero A_i induces a measure-preserving covering of the torus.
Thus the conditional two-window statement also follows by dividing
the two-window upper bound by the first disk's actual normalized
area. If `q_i>=c q_0` and `r_i<=L/sqrt(q_0)`, (18) is at most
`(2L+c^(-1/2))^(2m) q_0^(-m)`. There is again a genuine joint
power at the natural local scale.

Over the residue field of pi_0, the q_0 admissible residues h label
all projective lines other than the source line. A uniform
projective-line average therefore contributes `q_0/(q_0+1)` times
the normalized h average, once. This local factor does not establish
a complex-root law for the original Eisenstein inverse family or a
comparison of its arithmetic coefficients with these path weights.
Those are additional missing hypotheses for a native application.

## 6. Verification and research consequence

`check_hlc_root_averaging.py` checks the lifting normalizer (5)--(6),
the translated-grid formula (7), exact arc intersection measures,
conditional bounds, retained-projector upper bounds, cofactor Fourier
relations, the source-root Jacobian and exact rational pullback
integrals, the factorial ambiguity bound, the Eisenstein CRT and
Fourier lifting normalizers, and the fixed-integer determinant divisor estimate. It
also rejects repeated-event independence and a false extra line
normalizer. Every acceptance remains active under `python -O`.

The new usable results include a conditional two-window power bound
for actual omitted-list cofactor phases and an unnormalized ambiguity
bound for the actual source-root measure, with the moving dirty center
and the one line average retained. The existing source root replacement
does not by itself establish the conditional history hypothesis (13)
for every recorded path. No complete residue bridge, full HLC power
estimate, native middle-band estimate or new zero-free region is
claimed here.
