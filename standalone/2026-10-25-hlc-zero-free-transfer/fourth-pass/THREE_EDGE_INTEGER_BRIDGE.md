# An exact three-edge bridge and its root-phase measure

**Status.** This note proves a divisor parametrization of an integer
three-edge determinant bridge with fixed endpoints. For nonresonant fixed
data, averaging the actual, unwrapped root phase gives an inverse-
determinant measure bound. The same argument over the Eisenstein integers
gives an inverse-norm area bound. These are algebraic and measure
theorems, not bounds for the complete HLC path operator or for the native
inverse moment. A separate exact multiplicity calculation proves a
weighted closed-triangle sum with a power saving. Equal endpoints and
immediate-return resonances are retained explicitly.

The source comparison is to Lü--Wang--Wu,
[arXiv:2610.20242v1](https://arxiv.org/pdf/2610.20242), pp. 22--24,
Proposition 4.4 and equations (4.29)--(4.31), and p. 28, equation (4.40).
The PDF used in this pass has SHA256
`32ef255566d4f3611d2d89c3a5f3db94c792883cc713d77a7f9d33b163f55e88`.
No change of the original kernel normalization is used.

## 1. Fixed-endpoint integer parametrization

Fix primitive vectors \(z_0,z_3\in\mathbf Z^2\), a fixed complement
\(w_0\in\mathbf Z^2\) with \(\det(z_0,w_0)=1\), and three
nonzero integers \(j_0,j_1,j_2\). Write

\[
 z_3=A z_0+B w_0,\qquad
 z_1=h z_0+j_0w_0,\qquad z_2=xz_0+yw_0.                 \tag{1}
\]

The fixed data are \(z_0,z_3,w_0,j_0,j_1,j_2\); in particular they do
not vary with a real root parameter introduced later. A bridge means
primitive integer intermediate vectors satisfying

\[
 \det(z_0,z_1)=j_0,\quad \det(z_1,z_2)=j_1,
 \quad \det(z_2,z_3)=j_2.                                \tag{2}
\]

Define

\[
       \Delta=Bh-Aj_0,\qquad N=Bj_1+j_0j_2.              \tag{3}
\]

The two remaining determinant equations are
\(hy-j_0x=j_1\) and \(Bx-Ay=j_2\). Their exact consequences are

\[
       \Delta y=N,\qquad \Delta x=Aj_1+h j_2.            \tag{4}
\]

**Theorem 1 (nonresonant bridge).** If \(B\ne0\) and \(N\ne0\),
all integer bridges are enumerated by the following finite procedure:

1. Choose a nonzero signed divisor \(\Delta\mid N\).
2. Retain it only if \(B\mid\Delta+Aj_0\), and set
   \(h=(\Delta+Aj_0)/B\).
3. Retain it only if \(\Delta\mid Aj_1+h j_2\), and set
   \(x=(Aj_1+h j_2)/\Delta\), \(y=N/\Delta\).
4. For primitive bridges, also retain
   \(\gcd(h,j_0)=\gcd(x,y)=1\). Any position, parity, list or
   good-state restrictions are imposed on these actual candidates.

In particular, the number of integer bridges is at most

\[
                         2\tau(|N|).                    \tag{5}
\]

**Proof.** A solution cannot have \(\Delta=0\), by the first equation
in (4). Thus \(\Delta\mid N\), and (3)--(4) give precisely the
displayed values and divisibility conditions. Conversely substituting
these values into the two linear determinant equations proves (2).
Since \(B\ne0\), distinct values of \(\Delta\) give distinct h,
so a signed divisor determines at most one bridge. Primitivity in the
chosen unimodular basis is exactly the pair of gcd conditions. QED.

This is a count of integer vectors. It neither completes a residue fibre
nor drops the dependence of the actual positions on the root.

## 2. The two resonances

Assume in this section that there is one real linear functional \(\tau\)
with \(\tau(z_i)>0\) for all four vertices. The source position window
has this property. Positivity is needed to turn a primitive proportional
return into literal equality rather than equality up to sign.

### Nonparallel endpoints and N=0

Suppose \(B\ne0\) and \(N=0\). If \(\Delta\ne0\), then
\(y=0\). Primitivity gives \(z_2=\pm z_0\), and positivity gives

\[
             z_2=z_0,\qquad j_1=-j_0,\qquad j_2=B.       \tag{6}
\]

This is a first-two-edge geometric backtrack. If \(\Delta=0\),
\(z_1\) and \(z_3\) are proportional primitive integer vectors;
positivity gives

\[
             z_1=z_3,\qquad j_0=B,\qquad j_2=-j_1.       \tag{7}
\]

This is a last-two-edge geometric backtrack. These alternatives include
their intersection. They exhaust the resonance. Restoration of prime
lists or Fock memory is not a consequence of this geometric argument;
the stronger source-level immediate-memory-return theorem in
`HLC_PATH_CANCELLATION.md` has its own hypotheses.

### Parallel endpoints: closed triangles remain

If \(B=0\), primitivity and positivity give \(z_3=z_0\), so A=1.
Now \(\Delta=-j_0\) is a fixed nonzero integer, even though
\(N=j_0j_2\ne0\). It does **not** determine h. The exact equations
instead give

\[
 y=-j_2,\qquad
 x=-\frac{j_1+h j_2}{j_0},\qquad
                 h j_2\equiv-j_1\pmod {j_0}.            \tag{8}
\]

Put \(g=\gcd(|j_0|,|j_2|)\). There are solutions for h precisely
when \(g\mid j_1\); then they form one residue class modulo
\(|j_0|/g\), before the two primitive-vector conditions and the
position windows are imposed. These are closed three-edge paths, not
the nonresonant divisor family in Theorem 1.

The distinction is necessary even for positive primitive vertices. For
any odd prime q, set

\[
 z_0=z_3=(1,0),\quad
 (j_0,j_1,j_2)=(q,-2q,q),\quad
 z_1=(h,q),\quad z_2=(2-h,-q).                            \tag{9}
\]

Use \(\tau_R(a,b)=a+bR\), with \(0\le R<1\). On each interval
\(qR\in[n+1/4,n+3/4]\), choose \(h=1-n\). Both intermediate
positions then have \(\tau_R\) in \([1/4,7/4]\). They are
primitive unless \(n\equiv1\) or \(-1\pmod q\). Consequently
the union of valid root intervals has measure at least

\[
                         \frac{q-2}{2q}.                 \tag{10}
\]

It does not tend to zero with q. This is a geometric example, not a
lower bound for an HLC pairing or a construction of its prime lists.
It explains why the equal-endpoint case cannot be erased from an
operator-level application.

## 3. A nonresonant root-phase measure bound

Keep the fixed data of Theorem 1, with \(B,N\ne0\). Normalize a
varying real linear functional by its value at z_0 and put

\[
 R=\frac{\tau(w_0)}{\tau(z_0)}.
\]

Then the first intermediate position obeys

\[
              \frac{\tau(z_1)}{\tau(z_0)}=h+j_0R.        \tag{11}
\]

Here R is an **unwrapped real coordinate**. It is not replaced by its
fractional part in a fixed bounded position window.

**Theorem 2 (fixed-data phase bound).** For a fixed interval
\(I=[a,b]\) of length W and any measurable real set E, the measure of
R in E for which some bridge from Theorem 1 has \(h+j_0R\in I\)
is at most

\[
       \min\left\{|E|,\frac{2W\tau(|N|)}{|j_0|}\right\}. \tag{12}
\]

All additional position windows, primitive/parity conditions, list
restrictions or good-state tests may be retained: they only decrease
this event. In particular, \(\tau(z_3)/\tau(z_0)=A+BR\)
depends on R; it is not being treated as a root-independent endpoint
window.

**Proof.** There are at most \(2\tau(|N|)\) fixed candidate values
of h. For each one, (11) belongs to I on an interval of length
\(W/|j_0|\). The union bound proves (12). QED.

### The source's root coordinate and its Jacobian

The source uses

\[
 \tau_\xi(z)=z_1-2\xi z_2,\qquad 0\le\xi<1,
 \qquad R(\xi)=\frac{\tau_\xi(w_0)}{\tau_\xi(z_0)}.
\]

Because \(\det(z_0,w_0)=1\), its exact derivative is

\[
                 R'(\xi)=-\frac{2}{\tau_\xi(z_0)^2}.    \tag{13}
\]

This is the source's equation (4.31). On the actual support,
\(1/16\le\tau_\xi(z_0)\le16\). That support is contained
in a single interval on which R is monotone, and
\(d\xi\le128\,|dR|\). The actual first-edge ratio is in
\([1/16,16]\), of length \(255/16\), by equation (4.40).
Thus the set of roots supporting a bridge with these fixed endpoints
and determinant labels has measure at most

\[
 \boxed{\quad
   \min\left\{1,\frac{4080\tau(|N|)}{|j_0|}\right\}.
 \quad}                                                  \tag{14}
\]

If this bridge starts at the global root \(z_0=(1,0)\), choose
\(w_0=(0,1)\). Then R=-2\xi exactly, and the constant improves to

\[
            \min\left\{1,\frac{255\tau(|N|)}{16|j_0|}\right\}.
                                                               \tag{15}
\]

No periodicity is used in (14) or (15). Passing to R modulo one before
the position test would require tracking its integer translates and
would not justify the displayed estimate on its own.

The bound holds after fixing the other continuous source root
coordinates, because their position restrictions only reduce the
event. If they are integrated over \(s\in[1,16]\),
\(t_0\in[1,2]\), their finite total volume is at most 15. The source
root density \(1/(3\zeta(2))\) in (4.29) is a separate factor;
it has not been confused with the original operator state measure.

### The exact power consequence and its scope

For every \(\varepsilon>0\), \(\tau(n)\ll_\varepsilon
n^\varepsilon\). Thus if the fixed data satisfy
\(|j_0|\ge X^a\), \(|N|\le X^C\), where a,C are fixed positive
constants, (14) is \(O_{a,C,\varepsilon}(X^{-a+\varepsilon})\),
after renaming epsilon. In the raw source term
\(j_0=D(b-a)\), so a nonzero edge has \(|j_0|\ge d_0\).
This last fact alone does not make d_0 a fixed power of the source's x;
the original source uses its stated logarithmic hierarchy.

### A separate payment for closed triangles with small gcd

The B=0 family in (8) also admits a useful bound, using its congruence
rather than Theorem 1. Put \(g=\gcd(|j_0|,|j_2|)\). If
\(g\nmid j_1\), there are no integer bridges. Otherwise the possible
h form one residue class modulo \(M=|j_0|/g\). For a fixed interval
I of length W, the projected event

\[
 \text{there exists }h\equiv h_0\pmod M
                  \text{ with }h+j_0R\in I
\]

is periodic in the **unwrapped** real variable R with period \(1/g\).
It is a union of intervals of width \(W/|j_0|\) spaced by \(1/g\).
Its density in a period is exactly

\[
                        \rho=\min\{1,Wg/|j_0|\}.         \tag{15a}
\]

For a bridge starting at the global root, \(R=-2\xi\),
\(0\le\xi<1\), covers exactly 2g periods. Consequently the root
measure of this projected event is exactly rho. Imposing primitivity,
the later position windows and other restrictions can only decrease
it. With the actual first-edge window, this proves

\[
 \boxed{\quad
 \operatorname{meas}_{\xi}\{\text{closed triangle with the fixed labels}\}
 \le \min\left\{1,\frac{255g}{16|j_0|}\right\}
 \quad(z_0=(1,0),\ g\mid j_1).
 \quad}                                                   \tag{15b}
\]

There is also a uniform version at an arbitrary fixed source vertex.
If the second coordinate of z_0 is nonzero, the determinant-one
relation gives

\[
 R(\xi)=\frac{(w_0)_2}{(z_0)_2}
              -\frac1{(z_0)_2\tau_\xi(z_0)}.
\]

The positive retained tau window therefore maps into an interval of
length at most \((16-1/16)/|(z_0)_2|<16\). If that coordinate is
zero, primitivity and positivity give \(z_0=(1,0)\), and the image
length is at most two. In either case the image is covered by at most
17 integer unit intervals. Since the projected event above is also
one-periodic and \(|d\xi/dR|\le128\), its source-root measure is
at most \(2176\rho\), capped by one. In particular,

\[
 \operatorname{meas}_{\xi}\{\text{closed triangle with the fixed labels}\}
                  \le\min\{1,34680g/|j_0|\}.             \tag{15c}
\]

Thus a fixed-power bound \(g/|j_0|\le X^{-a}\) gives a fixed-power
payment for these closed triangles as well. The large-gcd family (9)
has g=q and is correctly left uncontrolled by this estimate. Neither
(15b) nor (15c) pays the number or weights of all determinant labels.

### Multiplicity and a summed weighted triangle theorem

Keeping the multiplicity of h rather than taking its union gives a
stronger summation interface. If \(g\mid j_1\), then exactly

\[
 \boxed{\quad
 \int_0^1\sum_{h\equiv h_0\ (\mathrm{mod}\ |j_0|/g)}
              1_I(h-2j_0\xi)\,d\xi
                       =\frac{Wg}{|j_0|}.
 \quad}                                                   \tag{15d}
\]

There is **no minimum with one** in this count. To see this, integrate
the periodic interval count over one period of length 1/g in R. Its
integral is W/|j_0|, whether or not different intervals overlap.
The interval R in [-2,0] comprises 2g periods, and the Jacobian from
R to xi is 1/2. This proves (15d). Every h determines exactly one
integer pair z_1,z_2 in (8); imposing primitivity and the other
windows can only reduce the sum.

Here is a genuinely summed consequence that no longer holds all three
determinant labels fixed. Fix a positive integer D and Y at least one.
For pairwise distinct integers \(a,b,c\in[Y,4Y]\), let
\(C_{D;a,b,c}(\xi)\) count primitive bridges rooted at
\(z_0=z_3=(1,0)\), with determinant labels

\[
 (j_0,j_1,j_2)=\sigma D(b-a,a-c,c-b),\qquad \sigma\in\{1,-1\},
\]

where sigma is fixed. For sigma=1 this is the source's old-minus-new
convention for chronological products \((Db,Da,Dc,Db)\). Swapping
the last two determinant labels gives the same gcd ratio and the
same bound. Require the first position ratio to belong to
I, and retain any additional restrictions by factors between zero
and one. These may include every other position, parity, list and
good-state condition. Then

\[
 \boxed{\quad
 \sum_{\substack{a,b,c\in\mathbf Z\cap[Y,4Y]\\
                       a,b,c\ \mathrm{pairwise\ distinct}}}
 \frac1{abc}\int_0^1 C_{D;a,b,c}(\xi)\,d\xi
       \le \frac{48W}{Y}\bigl(1+\log(3Y)\bigr)^2.
 \quad}                                                   \tag{15e}
\]

The bound is independent of D. Any root-independent nonnegative
weight bounded by K_0/(abc) costs at most the factor K_0.

**Proof.** The common D cancels in

\[
 \frac{\gcd(|j_0|,|j_2|)}{|j_0|}
       =\frac{\gcd(|b-a|,|c-b|)}{|b-a|}.
\]

The closed congruence is solvable because the three determinant labels
sum to zero. Formula (15d) bounds each integral by W times this ratio.
Put \(H=\lfloor3Y\rfloor\). For fixed b, enlarge the two nonzero
differences to all signed integers of size at most H. Since

\[
 \sum_{d=1}^H\gcd(h,d)
 \le\sum_{e\mid h}e\lfloor H/e\rfloor\le H\tau(h),
 \qquad
 \sum_{h=1}^H\frac{\tau(h)}h
   =\sum_{uv\le H}\frac1{uv}
   \le\left(\sum_{u=1}^H\frac1u\right)^2
   \le(1+\log H)^2,
\]

the sum of the ratios for each b is at most
\(4H(1+\log H)^2\). There are at most 3Y+1 at most 4Y
possible b, and \(1/(abc)\le Y^{-3}\). Using H at most 3Y
proves (15e). The enlargement includes some forbidden coincidences;
these are only additional terms in a nonnegative numerical upper
bound, not extra source paths. QED.

For the actual first-edge window, \(48W=765\). This is a
\(Y^{-1}(\log Y)^2\) payment for a weighted family of closed
triangles. Applying it to a source operator requires deriving its
weight K_0/(abc) from the original state and once-only line measure;
there is no such factor in an individual raw edge. The separate
`CLOSED_TRIANGLE_WEIGHT.md` provides that source derivation
for its explicitly identified common-shared-list three-edge class.
Its hypotheses and all its remaining normalizers are necessary for
that application.

### Remaining summation and conditioning costs

For the nonresonant fixed-data result, the more general summation
interface is as follows.
To average it over many data sets with nonnegative root-independent
weights \(c_\gamma\), the exact consequence is only

\[
 \int\sum_\gamma c_\gamma\mathbf1_{\text{bridge }\gamma}\,d\xi
 \le 4080\sum_\gamma c_\gamma
                    \frac{\tau(|N_\gamma|)}{|j_{0,\gamma}|}.
                                                               \tag{16}
\]

The total coefficient mass on the right must still be paid. If a
conditional root distribution has density at most H relative to
Lebesgue measure, multiply the right side by H. Without a density
bound, a history conditioned on its positions or recorded memory need
not retain this saving. Several bridges using the same root are not
independent, so their measure bounds cannot be multiplied.

## 4. The Eisenstein integer bridge

Let \(\mathcal O=\mathbf Z[\omega]\), \(\omega=e^{2\pi i/3}\),
with field norm \(\mathrm N(a+b\omega)=a^2-ab+b^2\) and covolume
\(c_{\mathcal O}=\sqrt3/2\) in the complex plane. A vector in
\(\mathcal O^2\) is primitive if its coordinates generate the unit
ideal. The Euclidean algorithm gives a complement w_0 of every
primitive z_0 with determinant one. Use (1)--(4) in this ring, with
nonzero \(j_i\) and primitive endpoints. Write \(\tau_{\mathcal O}((N))\)
for the number of integral ideal divisors of the nonzero principal
ideal (N).

**Theorem 3 (Eisenstein bridge).** If \(B,N\ne0\), there are at most

\[
                         6\tau_{\mathcal O}((N))          \tag{17}
\]

integer-ring bridges. An exact enumeration takes every element divisor
\(\Delta\mid N\), checks \(B\mid\Delta+Aj_0\), defines h,
checks \(\Delta\mid Aj_1+h j_2\), defines x,y as above, and
retains the two primitive conditions and the actual additional
restrictions.

**Proof.** The Cramer identities (4) hold in the fraction field and
give the same necessity and sufficiency as over the integers. Every
ideal divisor of (N) is principal, since this ring is Euclidean, and
has exactly six generator associates. These are precisely the six
element divisors contributed by that ideal. Each determines at most
one h because B is nonzero. QED.

The N=0 resonances now give **unit-proportional** returns. If
\(\Delta\ne0\), primitivity gives \(z_2=\epsilon z_0\) for a
unit epsilon, hence \(j_1=-\epsilon j_0\), \(j_2=\epsilon B\).
If \(\Delta=0\), then \(z_1=\epsilon z_3\), hence
\(j_0=\epsilon B\), \(j_2=-\epsilon^{-1}j_1\). There is no
positive-real-vector argument selecting epsilon=1 in this complex
setting. For B=0, write \(z_3=\epsilon z_0\); then

\[
 y=-\epsilon^{-1}j_2,\qquad
 x=-\frac{j_1+\epsilon^{-1}h j_2}{j_0},\qquad
       h j_2\equiv-\epsilon j_1\pmod {j_0}.              \tag{18}
\]

It is an ideal-congruence family and is excluded from (17).

### Complex root averaging

Fix a fundamental parallelogram Q of \(\mathcal O\), with its
normalized area measure \(dA/c_{\mathcal O}\). Let R vary in Q
and use the complex linear functional characterized by
\(\tau_R(z_0)=1\), \(\tau_R(w_0)=R\). Fix a measurable bounded
region \(\Omega\subset\mathbf C\), independently of R. With all
endpoint and determinant data also fixed independently of R, (17)
gives

\[
 \boxed{\quad
 \Pr_{R\in Q}\{\text{some bridge has }h+j_0R\in\Omega\}
 \le \min\left\{1,
   \frac{6\tau_{\mathcal O}((N))\operatorname{area}(\Omega)}
        {c_{\mathcal O}\,\mathrm N(j_0)}\right\}.
 \quad}                                                   \tag{19}
\]

Indeed, multiplication by j_0 scales real area by \(|j_0|^2=
\mathrm N(j_0)\). For each of the at most (17) candidate h, the
preimage of \(\Omega-h\), intersected with Q, has area at most
\(\operatorname{area}(\Omega)/\mathrm N(j_0)\). The union bound
and division by the area of Q prove (19).

The window \(h+j_0R\in\Omega\) is unwrapped in the complex
plane. Replacing it by a condition modulo \(\mathcal O\) changes
the problem: multiplication by j_0 on the torus is a covering map,
and there is then no general inverse-norm area saving.

The elementary divisor bound
\(\tau_{\mathcal O}((N))\ll_\varepsilon\mathrm N(N)^\varepsilon\)
gives the same fixed-power consequence as above, with norm bounds
\(\mathrm N(j_0)\ge X^a\), \(\mathrm N(N)\le X^C\).
For completeness, in the ideal factorization the divisor count is
\(\prod_{\mathfrak p}(e_{\mathfrak p}+1)\). For prime ideals of
sufficiently large norm, \(e+1\le2^e\le\mathrm N(\mathfrak p)^{\varepsilon e}\).
Only finitely many smaller prime ideals remain, and the supremum of
\((e+1)/\mathrm N(\mathfrak p)^{\varepsilon e}\) is finite for
each of them. This proves the estimate, with the identical argument
over the rational integers.

This field-compatible lemma supplies neither a complex root measure
for the native inverse detector nor a comparison between its
Möbius/Hecke coefficients and HLC path weights. Those would be
additional analytic constructions. No native moment improvement or
new zero-free region follows from (19) alone.

## 5. Reproducible checks and their limits

`check_three_edge_integer_bridge.py` independently enumerates small
integer determinant bridges, checks the exact signed-divisor procedure,
classifies the positive N=0 alternatives, checks the B=0 congruence,
and integrates finite first-position interval unions and multiplicity
counts with rational arithmetic. It checks the closed-triangle family
(9)--(10), the exact gcd-density and weighted label sums, the exact
Jacobian identity, and exact Eisenstein ring determinant and divisibility
examples, including the six-associate count. Explicit failures remain
enabled under `python -O`.

These checks verify finite algebra and the constants used in the
measure estimates. They do not prove the asymptotic divisor bound,
the source root-averaging theorem, a conditional history-density bound,
or any summed HLC/native moment. The proofs and scope of those claims
are stated separately above.
