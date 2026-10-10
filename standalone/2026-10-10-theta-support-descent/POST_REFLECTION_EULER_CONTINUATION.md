# Reflecting the conditioned divisor series across its former boundary

**Status:** source-conditional analytic continuation theorem, with an exact
good-prime scalar calculation and a normally convergent dual cusp series.
The full standard-face object continues meromorphically across `v=1`.
This does not prove a higher moment or identify a moment diagonal.

**Authorship:** gauss_analytic. Independent review is to be recorded
separately against the exact content hash.

**Dependencies:** the fixed source and definitions of
[DEFORMED_GAUSS_CONTINUATION.md](DEFORMED_GAUSS_CONTINUATION.md), Sections
1–3; the plus horizontal derivative and its normalization in
[HIGHER_ANGULAR_SECOND_MOMENT.md](HIGHER_ANGULAR_SECOND_MOMENT.md),
Sections 1–2; and the imported October 5 `paper2.tex` finite local
transform, reduced denominators, and three cusp expansions. The precise
source labels used here are `eq:ray-local-transform`,
`eq:ray-multiplier`, `eq:ray-additive-crt`,
`eq:theta-mellin-functional-equation`, and
`eq:dual-cusp-mellin-series`. The new good-prime computation uses local
exponents 3 and 4, so it is derived below rather than borrowed from the
exponent-1 calculation in the earlier scalar audit.

The meromorphic statement uses ordinary continuation of fixed finite
Hecke L-functions. A pole-free reciprocal statement in `Re(v)>beta`
additionally uses the inherited finite-order zero-free theorem there.
One may conservatively take `beta=11/12` from the imported mean-square
argument. This additional input is not needed for the meromorphic
continuation to `Re(v)>1/2`.

## 1. The exact object and new domain

Use the same primary-generator convention, fixed bad set S, fixed
finite ray characters eta and rho, and squarefree row k as in the
companion note. Write Q=Nk and

\[
\begin{gathered}
\chi^-_k=\eta\overline\alpha^3\chi_k^3,
\qquad \kappa=\eta\rho^3,
\qquad v=w+3s-\tfrac32,\\
x_p=\chi^-_k(p)(Np)^{-w},\qquad
z_p=\kappa(p)(Np)^{-v},\qquad
D_p=1-x_p+z_p.
\end{gathered}
\tag{1.1}
\]

All Euler products below omit the primes dividing kS. In particular the
displayed values of x and z are used only at good primes outside k.
Let

\[
P_k(w,v)=
\frac{L_{S,k}(v,\kappa)}{L_{S,k}(w,\chi^-_k)}
\mathcal E_{k,1}(w,v).
\tag{1.2}
\]

The old remainder has the exact good-prime factor

\[
\mathcal E_{k,1,p}=
\frac{D_p(1-z_p)}{1-x_p}.
\tag{1.3}
\]

It is holomorphic and uniformly bounded on compact subregions of
`Re(w)>0`, `Re(v)>1/2`, `Re(w+v)>1`. Its factor is not divided by
D_p in this assertion. Initially `Re(w),Re(s)>1`, the companion
conditioned identity is

\[
\mathscr R_k(w,s)=P_k(w,v)
\sum_d^*\frac{\mathfrak a_k(d)}{(Nd)^s}
\prod_{p\mid d}\frac{Np\,x_p}{D_p}
\mathcal T_{k,d}(s),
\tag{1.4}
\]

where

\[
\mathfrak a_k(d)=
\gamma_2(d)\rho(d)\vartheta(d)\alpha(d)\chi_k(d)^3,
\qquad
\vartheta(d)=\chi_d(\lambda)^{-2}.
\tag{1.5}
\]

Every d in (1.4) is squarefree and coprime to kS. The completed theta
series has finite good-prime exponents 3 at k and 4 at d, and angular
parameter +2. Its cube zero masks have already been included in (1.4).

### Theorem 1.1

Set

\[
\mathfrak D=
\left\{(s,v):\Re v>\tfrac12,
\quad \Re s<\min(0,\Re v-1)\right\},
\qquad w=v-3s+\tfrac32.
\tag{1.6}
\]

There is a finite family of finite-order ray characters zeta, with
conductors supported on a fixed bad modulus independent of k, such
that `R_k(v-3s+3/2,s)` has a meromorphic continuation to
mathfrak D. The only possible divisors of poles there are:

* `v=1`, if kappa is principal;
* zeros of one of the fixed functions `L_S(v,zeta)`.

The moving factors at primes of k have no zeros in this domain. If the
inherited common finite-order zero-free boundary is beta with
`1/2<beta<1`, the continuation is holomorphic on

\[
\mathfrak D_\beta=\mathfrak D\cap\{\Re v>\beta\}
\tag{1.7}
\]

unless kappa is principal, in which case its only possible pole is a
simple pole at v=1. Formula (5.2) below gives its residue as an explicitly
specified normally convergent finite sum of cusp series. The residue
may vanish. No equality with an initial Poisson diagonal is asserted.

The reflected series has the conductor factor `Q^(1-2 Re(s))`, up to
arbitrarily small powers of Q, on compact subsets avoiding its stated
polar divisors. On closed real subregions of mathfrak D_beta with
strict margins and bounded real coordinates it also has a joint
polynomial bound in `Im(s)` and `Im(v)`, after multiplication by v-1
when kappa is principal; see (4.15). In particular the theorem is a
continuation result, not a conductor-saving estimate.

## 2. The exact exponent-3 / exponent-4 scalar

Fix a finite Fourier label h0 and a residue class of kd modulo the
source's fixed large bad modulus. Its reduced denominator is

\[
c=c_0kd,\qquad t_0=\lambda^2c_0,
\tag{2.1}
\]

where the possible normalizing unit is included in the fixed c0 for
that branch. The cusp index, fixed additive phase, and kappa0 are
constant on this branch. All good primes of kd are active. For p|kd,
the local data are

\[
\sigma_p=\lambda^2c/p,
\qquad \epsilon_p=-\lambda^{-5}(c/p)^{-2},
\tag{2.2}
\]

and the scalar, apart from the common Mellin normalization and fixed
Fourier coefficient, is

\[
\alpha(c)^2
\prod_{p\mid k}\chi_p(\sigma_p)^{-2}\omega_{p,3}
\prod_{p\mid d}\chi_p(\sigma_p)^{-2}\gamma_4(p).
\tag{2.3}
\]

The plus derivative is essential for the sign of the infinity type in
alpha(c) squared. The finite local transform is unchanged.

For p|k, direct simplification gives

\[
\begin{aligned}
\chi_p(\sigma_p)^{-2}\omega_{p,3}
&=\gamma_3(p)\gamma_5(p)\chi_p(\lambda)^3\chi_p(c/p)^2\\
&=-\overline{\alpha(p)}\gamma_2(p)
\chi_p(-4)\chi_p(\lambda)^3\chi_p(c/p)^2.
\end{aligned}
\tag{2.4}
\]

Indeed the definition
`omega_(p,3)=chi_p(-1)^3 gamma_3(p) gamma_5(p)
chi_p(epsilon_p)^(-5)` gives exponents -2 on chi(-1), 21 on
chi(lambda), and 8 on chi(c/p). The identity `chi_p(-1)^2=1`
removes the first factor, and reduction modulo six of the other two
exponents gives the first line. For the second, use the source Gauss identities

\[
\gamma_1\gamma_2=-\alpha\chi_p(4)^{-1}\gamma_3,
\qquad \gamma_1\gamma_5=\chi_p(-1),
\tag{2.5}
\]

so `gamma_3 gamma_5=-bar-alpha chi_p(-4) gamma_2`.

The exact squarefree CRT identity is

\[
\gamma_j(a)=\prod_{p\mid a}\gamma_j(p)
                  \prod_{p\mid a}\chi_p(a/p)^j.
\tag{2.6}
\]

Consequently the product over k in (2.3), before alpha(c) squared, is

\[
\mu(k)\overline{\alpha(k)}\gamma_2(k)
\chi_k(-4)\chi_k(\lambda)^3\chi_k(c_0)^2\chi_k(d)^2,
\tag{2.7}
\]

and the product over d is

\[
\gamma_4(d)\chi_d(t_0k)^{-2}.
\tag{2.8}
\]

Cubic reciprocity for the chosen coprime primary k,d gives
`chi_k(d)^2=chi_d(k)^2`. Thus the k,d cross-symbols in (2.7) and
(2.8) cancel exactly. Define the unit-modulus row scalar

\[
\Gamma_{c_0}(k)=
\mu(k)\alpha(k)\gamma_2(k)
\chi_k(-4)\chi_k(\lambda)^3\chi_k(c_0)^2.
\tag{2.9}
\]

Then (2.3) is exactly

\[
\alpha(c_0)^2\Gamma_{c_0}(k)
\alpha(d)^2\gamma_4(d)\chi_d(t_0)^{-2}.
\tag{2.10}
\]

On the other hand, multiplying the d coefficient in (1.4) by the
numerators of its local factors gives

\[
\frac{\mathfrak a_k(d)}{(Nd)^s}
\prod_{p\mid d}Np\,x_p
=
\frac{\gamma_2(d)\eta(d)\rho(d)\vartheta(d)
           \overline{\alpha(d)}^{\,2}}
     {(Nd)^{w+s-1}}.
\tag{2.11}
\]

Here the two quadratic row values multiply to the literal sixth
power, which equals one precisely because (d,k)=1. Combining
(2.10) and (2.11) cancels both the angular factor and
`gamma_2(d) gamma_4(d)=1`. The remaining d phase is

\[
\eta(d)\rho(d)\vartheta(d)\chi_d(t_0)^{-2}.
\tag{2.12}
\]

This is a fixed finite ray character on each fixed branch. It need not
be eta rho cubed. The residue-class condition on d will produce further
finite characters; it is retained below.
Since `t0=lambda^2 c0` and `vartheta(d)=chi_d(lambda)^(-2)`,
the product `vartheta(d) chi_d(t0)^(-2)` also equals
`chi_d(c0)^(-2)`: its lambda exponent is -6, and all d here avoid S.
Thus (2.12) can equally be written `eta(d) rho(d) chi_d(c0)^(-2)`.

The local dual factors are exactly

\[
B_{p,3}(m)=\chi_p(m),\qquad
B_{p,4}(m)=q^{-1/2}\bigl(-1+q\mathbf1_{p\mid m}\bigr),
\qquad m=\lambda^4\ell.
\tag{2.13}
\]

In particular, d coprime to m contributes the sign mu(d). A principal
positive divisor series cannot be substituted for this local factor.
Its norm combines with (2.11) and `(Nd)^(1-2s)` from the functional
equation to give

\[
(Nd)^{-(w+s-1)}(Nd)^{1-2s}(Nd)^{-1/2}
=(Nd)^{-v}.
\tag{2.14}
\]

## 3. An exact reflected representation

Here are precise finite labels and the Mellin constant, so the residue
in Section 5 is a specified function rather than an unspecified scalar.

The initial periodic multiplier is
`phi_rho(x)=rho(x)` on good primary x and zero otherwise: the factor
vartheta in (1.5) is already in the standard theta coefficient, so it
cancels the supplementary factor used to define the source multiplier.
Its normalized finite Fourier coefficients are

\[
\widehat\phi_\rho(h_0)=\frac1{NL}
\sum_{x\bmod L}\phi_\rho(x)e(-h_0x/L).
\tag{3.1}
\]

Choose a fixed bad modulus M large enough for all supplementary
characters and all source residue data, and put G=(O/M)^*. After
fixing a source branch h0 and a residue u in G for d, all of
`c0`, `sigma`, `psi`, and `kappa0` are fixed (with dependence on the
residue of k retained). Insert

\[
\mathbf1_{d\equiv u\ (M)}
=\frac1{|G|}\sum_{\xi\in\widehat G}\overline{\xi(u)}\xi(d).
\tag{3.2}
\]

The primary condition merely restricts the nonempty residue classes;
using the full unit group in (3.2) is still the exact identity. Enlarge
M, if necessary, so the character `d -> chi_d(t0)^(-2)` factors
through it. This is legitimate by the fixed supplementary laws and
the fact that t0 is supported at S. For the finite label b=(h0,u,xi),
set

\[
\begin{aligned}
\zeta_b(d)&=\eta(d)\rho(d)\vartheta(d)
                \chi_d(t_{0,b})^{-2}\xi(d),\\
K_b(s,k)&=\frac{\overline{\xi(u)}}{|G|}
  \widehat\phi_\rho(h_0)\overline{\kappa_{0,b}}
  \alpha(c_{0,b})^2(Nc_{0,b})^{1-2s}\Gamma_{c_{0,b}}(k),\\
H(s)&=\frac{i}{3^{5/2}}27^{-s}(2\pi)^{4s-2}
 \frac{\Gamma(4/3-s)\Gamma(5/3-s)}
      {\Gamma(s+1/3)\Gamma(s+2/3)}.
\end{aligned}
\tag{3.3}
\]

Zero Fourier coefficients and empty branch classes are harmless. The
number of labels and their fixed moduli are independent of k. The
characters zeta_b range over a fixed finite family as k varies, because
all bad data depend only on finitely many residues of k.

For nonzero `ell` in `lambda^(-4) O`, define `m=lambda^4 ell` and

\[
\begin{aligned}
\mathcal D_{\zeta,k,m}(w,v)
&=\sum_{(d,kS)=1}^*
\frac{\zeta(d)}{(Nd)^v}
\prod_{p\mid d}\frac{-1+Np\,\mathbf1_{p\mid m}}{D_p},\\
\mathcal C_b(s,w,v;k)
&=\sum_{0\ne\ell\in\lambda^{-4}O}
d_{\sigma_b}(\ell)\psi_b(\lambda^4\ell)
\overline{\alpha(\ell)}\chi_k(\lambda^4\ell)
(N\ell)^{s-1}
\mathcal D_{\zeta_b,k,\lambda^4\ell}(w,v).
\end{aligned}
\tag{3.4}
\]

The exact reflected identity is

\[
\boxed{
\mathscr R_k(w,s)=
P_k(w,v)H(s)Q^{1-2s}\sum_bK_b(s,k)\mathcal C_b(s,w,v;k).}
\tag{3.5}
\]

It holds first for `Re(s)<0`, `Re(v)>1`, by continuation of (1.4)
through its normally convergent completed-divisor domain and the theta
functional equation. In that region the double series in (3.4) is
absolutely convergent, as the estimates in Section 4 also show, so the
order of its sums may be interchanged.

For completeness, the sign in H follows from the explicit primal
normalization

\[
J_+(s)=-\frac{3^{5/2}}4
\left(\frac{27}{(2\pi)^2}\right)^s
\Gamma(s+1/3)\Gamma(s+2/3)\mathcal T_{k,d}(s).
\tag{3.6}
\]

The plus-derivative functional equation has the sign minus and the
factor alpha(c) squared, while the dual minus Mellin series has the
factor `i/[4(2pi)^(2-2s)]`. These two minus signs cancel, giving
(3.3). The gamma ratio is holomorphic for Re(s)<0 and has polynomial
vertical growth on every fixed closed left strip. Its reciprocal
denominator gamma factors create zeros, not poles.

## 4. Resumming the signed divisor Euler product

For any zeta from the finite family, put `u_p=zeta(p)q^(-v)` and
retain the literal omissions at kS. In `Re(v)>1`, the local factor of
mathcal D in (3.4) is

\[
\begin{cases}
1-u_p/D_p,&p\nmid m,\\
1+(q-1)u_p/D_p,&p\mid m.
\end{cases}
\tag{4.1}
\]

Extract the reciprocal finite L-function by defining

\[
\mathcal E_{\zeta,k,m}(w,v)=\prod_{p\nmid kS}E_{p,m},
\quad
E_{p,m}=
\begin{cases}
\displaystyle\frac{D_p-u_p}{D_p(1-u_p)},&p\nmid m,\\[6pt]
\displaystyle\frac{D_p+(q-1)u_p}{D_p(1-u_p)},&p\mid m.
\end{cases}
\tag{4.2}
\]

Then the exact identity is

\[
\boxed{
\mathcal D_{\zeta,k,m}(w,v)
=\frac{\mathcal E_{\zeta,k,m}(w,v)}{L_{S,k}(v,\zeta)}.}
\tag{4.3}
\]

The factor at p not dividing m satisfies the more informative identity

\[
E_{p,m}-1=
\frac{u_p(-x_p+z_p)}{D_p(1-u_p)}.
\tag{4.4}
\]

Throughout mathfrak D one has `Re(w)>2`, since
`w=v-3s+3/2`, `Re(v)>1/2`, and `Re(s)<0`. Thus, for every prime
norm q>=2,

\[
|x_p|+|z_p|<2^{-2}+2^{-1/2}<1.
\tag{4.5}
\]

Both D_p and `1-u_p` are nonzero, uniformly away from zero on the
closed subregions used below. No division through a possible zero of
D_p has been made outside this explicit domain.

On each compact subregion, (4.4) gives

\[
E_{p,m}=1+O\!\left(q^{-\Re w-\Re v}+q^{-2\Re v}\right)
\quad(p\nmid m).
\tag{4.6}
\]

The prime sums converge locally normally because `Re(v)>1/2` and
`Re(w)>2`. At a prime dividing m, (4.2) gives

\[
|E_{p,m}|\le C\,q^{\max(0,1-\Re v)}.
\tag{4.7}
\]

Separate finitely many small primes and use the standard bound for a
fixed constant raised to the number of distinct prime divisors. For
every epsilon>0 this proves the uniform estimate

\[
\boxed{
|\mathcal E_{\zeta,k,m}(w,v)|
\ll (Nm)^{\max(0,1-\Re v)+\epsilon}.}
\tag{4.8}
\]

Here m is a nonzero integral element; its possibly repeated prime
factors cause no difficulty, as only its radical appears. The bound is
uniform in k and the vertical parameters on any fixed closed real
subregion with strict margins. The infinite products over primes not
dividing m are bounded by the same normally convergent majorant when
primes of k or m are removed. No division by their possibly vanishing
factors is needed.

Let a=`max(0,1-Re(v))`. The source cusp coefficients, with their full
ramified and unit support, obey

\[
\sum_{0\ne\ell\in\lambda^{-4}O}
|d_\sigma(\ell)|(N\ell)^{-u}<\infty
\qquad(u>1),
\tag{4.9}
\]

uniformly for the three fixed cusps. This follows from their stated
support `ell=unit lambda^j n b^3`, squarefree n, coefficient bound
`O(3^(j/6)(Nb)^(1/2))`, and a convergent geometric ramified sum. The
fixed finitely many lowest ramified exponents are included. Since
`Nm=81 Nell`, (4.8) and (4.9) show that

\[
\begin{aligned}
\mathcal B_b(s,w,v;k)=
\sum_{0\ne\ell\in\lambda^{-4}O}
&d_{\sigma_b}(\ell)\psi_b(\lambda^4\ell)
\overline{\alpha(\ell)}\chi_k(\lambda^4\ell)\\[-2pt]
&\hspace{12mm}\cdot(N\ell)^{s-1}
\mathcal E_{\zeta_b,k,\lambda^4\ell}(w,v)
\end{aligned}
\tag{4.10}
\]

converges locally normally under the sufficient condition

\[
1-\Re s-a>1,
\quad\text{that is}\quad
\Re s<\min(0,\Re v-1).
\tag{4.11}
\]

No converse about conditional convergence is claimed. On each compact
subregion choose epsilon smaller than the strict margin in (4.11).
The row character has modulus at most one,
so the bound for mathcal B is uniform in k. It is also uniform in the
vertical parameters on fixed closed real subregions, since all
oscillatory powers have modulus controlled by their real parts.

Combining (3.5), (4.3), and (4.10) gives the final representation

\[
\boxed{
\mathscr R_k(w,s)=
P_k(w,v)H(s)Q^{1-2s}
\sum_b\frac{K_b(s,k)\mathcal B_b(s,w,v;k)}
                   {L_{S,k}(v,\zeta_b)}.}
\tag{4.12}
\]

The factors mathcal B are holomorphic on mathfrak D by normal
convergence. The finite reciprocals in (4.12) are taken after that
summation, so their ordinary meromorphic continuation suffices for the
meromorphic part of Theorem 1.1. The overlap `Re(s)<0,Re(v)>1` is
nonempty and connected to the previous completed-divisor domain; thus
(4.12) continues the same function, not a newly assigned series.

The remaining factors have no additional poles on mathfrak D:
`Re(w)>2` puts `1/L(w,chi^-_k)` in its Euler half-plane;
mathcal E_(k,1) is holomorphic by (1.3); and H is holomorphic for
Re(s)<0. Also

\[
L_{S,k}(v,\zeta)
=L_S(v,\zeta)\prod_{p\mid k}(1-\zeta(p)q^{-v}),
\tag{4.13}
\]

whose moving factors cannot vanish for Re(v)>0. At a principal pole
the reciprocal in (4.12) has a zero. This proves the asserted polar
divisor statement, and the inherited common zero-free result proves
its refinement on mathfrak D_beta.

On compact subregions away from these divisors the fixed finite
L-functions and their reciprocals are bounded. Their moving Euler
factors and reciprocal moving factors cost only Q^epsilon, by the
fixed-small-prime argument. All K_b have bounded absolute value there,
apart from fixed s-dependent factors, and (4.10) is uniform in k.
Hence the conductor bound stated in Theorem 1.1 is

\[
\mathscr R_k(v-3s+\tfrac32,s)
\ll Q^{1-2\Re s+\epsilon}
\tag{4.14}
\]

on such compact subsets.

### 4.1 Joint vertical bound in the zero-free refinement

Let e_kappa be one if kappa is principal and zero otherwise. Fix a
closed real subregion with bounded real coordinates and strict positive
margins in `Re(v)>beta`, `Re(s)<0`, and `Re(s)<Re(v)-1`. For every
epsilon>0 there is a finite exponent A such that

\[
\boxed{
|(v-1)^{e_\kappa}\mathscr R_k(v-3s+\tfrac32,s)|
\ll Q^{1-2\Re s+\epsilon}
        (2+|\Im s|+|\Im v|)^A.}
\tag{4.15}
\]

The constants depend on the margins, fixed real bounds, finite ray
family and epsilon, but not on k or either imaginary part. Since
`Im(w)=Im(v)-3 Im(s)`, this also controls the w variable.

Here is a justification of the needed reciprocal bound, including the
principal case. For each fixed finite character zeta, define

\[
F_\zeta(v)=
\begin{cases}
L_S(v,\zeta),&\zeta\text{ nonprincipal},\\[2pt]
\displaystyle\frac{v-1}{v+1}L_S(v,1),&\zeta\text{ principal}.
\end{cases}
\tag{4.16}
\]

The inherited zero-free statement makes F holomorphic and nonzero on
`Re(v)>beta`; the removable value at v=1 is nonzero. Ordinary Hecke
functional equations and the Euler bound give polynomial growth of F
on every fixed closed real strip. Alternatively this growth is one of
the usual finite-order continuation bounds for the fixed finite
L-functions; no moving character is involved here.

For a target line at distance delta>0 from beta, center a disk at
`A0+i Im(v)`, where A0 is a fixed real number at least two and to the
right of all target real parts. Choose its outer radius
`A0-beta-delta/4` and an inner radius containing all the target
real parts, with a fixed positive gap to the outer circle. On the
center line the Euler product and the rational factor in (4.16) put F
in a fixed compact annulus. Choose the analytic logarithm on the disk
whose central value has bounded imaginary part. Its real part satisfies
`log|F| <= C log(2+|Im(v)|)` throughout the disk by the polynomial
upper bound. Borel–Caratheodory therefore gives the same order bound
for its absolute value on the inner disk. Exponentiating its negative
shows

\[
L_S(v,\zeta)^{-1}
\ll (2+|\Im v|)^{A_0'}
\quad(\Re v\ge\beta+\delta)
\tag{4.17}
\]

on the bounded real strips in question. In the principal case the
factor `(v-1)/(v+1)` multiplying `1/F` is bounded there. The finite
family makes the exponent and constants uniform across all labels.

The moving reciprocal factors from (4.13) have absolute value at most
`prod_(p|k)(1-q^(-beta-delta))^(-1)`, which is O(Q^epsilon).
The moving factors in L(v,kappa) obey the same bound with a plus in
place of the inverse minus. The product
`(v-1)^e_kappa L_S(v,kappa)` has polynomial vertical growth, while
`1/L(w,chi^-_k)` has a uniform Euler bound because Re(w)>2. The old
remainder and the cusp sum (4.10) have uniform bounds independent of
both imaginary parts by their absolute majorants. Finally Stirling
gives polynomial growth for H(s), with size
`O((2+|Im(s)|)^(2-4 Re(s)))` on a fixed closed left strip, and all
other s-dependent constants have bounded modulus there. These bounds
prove (4.15). This polynomial vertical assertion is confined to the
zero-free refinement; the raw meromorphic continuation does not
silently supply uniform bounds near its possible reciprocal poles.

## 5. A convergent formula for the possible residue

Suppose kappa is principal, and put

\[
\mathfrak r_{S,k}
=\mathop{\rm Res}_{v=1}L_{S,k}(v,1)
=\mathop{\rm Res}_{v=1}\zeta_K(v)
       \prod_{p\mid kS}(1-(Np)^{-1}).
\tag{5.1}
\]

Repeated factors in kS are included only once. For every Re(s)<0,
set `w0=5/2-3s`. On a neighborhood of `(s,v=1)` inside
mathfrak D_beta, multiply (4.12) by v-1 and take v to 1. Normal
convergence justifies the limit inside each cusp series. One obtains

\[
\boxed{
\begin{aligned}
\mathop{\rm Res}_{v=1}
\mathscr R_k(v-3s+\tfrac32,s)
={}&\mathfrak r_{S,k}
\frac{\mathcal E_{k,1}(w_0,1)}
     {L_{S,k}(w_0,\chi^-_k)}
H(s)Q^{1-2s}\\
&\quad\times
\sum_b K_b(s,k)
\left[L_{S,k}(v,\zeta_b)^{-1}\right]_{v=1}
\mathcal B_b(s,w_0,1;k).
\end{aligned}}
\tag{5.2}
\]

The bracket means the analytic reciprocal value. It is zero if
zeta_b is principal; for a nonprincipal zeta_b it is the usual
reciprocal of L(1,zeta_b), with all masks retained. Thus a principal
reflected divisor component cannot supply an additional pole. There
can also be cancellation among nonprincipal components. Formula
(5.2) specifies the possible residue completely in terms of finite
Fourier data, the source's three fixed cusp sequences, convergent
Euler products, and finite L-values. It does not assert nonvanishing.

For example, if one label happens to have `zeta_b=kappa`, its
reciprocal cancels the corresponding numerator L(v,kappa) in (4.12).
At good primes not dividing m the complete combined local factor
reduces to `1-x_p`. At primes dividing m it is
`1-x_p+q z_p`. This is the exact sign-sensitive cancellation suggested
by the local Ramanujan factor. The full family cannot be replaced by
this special case unless its fixed finite Fourier data are shown to
force zeta_b=kappa.

## 6. What crosses the boundary, and what remains

The earlier absolute d-summation required Re(v)>1 on the left of the
theta functional equation. Equations (4.3) and (4.12) cross that
boundary by keeping the negative Ramanujan terms: their finite-order
Möbius series is a reciprocal L-factor. The continuation accounts for
all three reflected cusp expansions and all repeated prime factors
of their Fourier indices, even though the object being continued is
the original complete standard face.

This theorem does not authorize a favorable contour shift for the
desired moment. Under the balanced Mellin substitution, the scalar
factor from the companion note is `D^(w+s-3/2)=D^(v-2s)`, after
the displayed k conductor factors cancel in that scalar calculation.
In the new part with `Re(v)<=1`, the condition
`Re(s)<Re(v)-1` gives

\[
\Re(v-2s)>2-\Re v\ge1.
\tag{6.1}
\]

For Re(v)>1 and Re(s)<0 it is larger than Re(v), also larger than
one. Thus the absolute dual-theta estimate in this proof gives a
power of D strictly worse than D throughout its domain. Furthermore
the surviving good-prime row factor is the sextic character
`chi_k(lambda^4 ell)`, not the earlier quadratic factor; a subsequent
row estimate must use its actual coefficient class. Identifying the
residue in (5.2) with any signed initial diagonal would require an
additional equality of the complete finite rays, scales, and weights.
No such equality, generalized moment estimate, or improvement of the
zero-free exponent is claimed here.

There is nevertheless a nonempty part of the new region inside the
literal Mellin convergence domain of the already used first-derivative
reflected weight. Its first possible numerator gamma pole is at
`t=-5/6`; with `s=1/2+t`, staying in that domain means taking
`Re(s)>-1/3`. This is a condition on the weight's standalone Mellin
integral, not an asserted obstruction after multiplication by H(s),
whose reciprocal gamma factors may cancel those poles.
For any real v with `max(beta,2/3)<v<1`, choose
`-1/3<Re(s)<v-1`. This crosses v=1 without crossing that kernel
obstruction. The strict lower bound (6.1) still holds, so avoiding a
kernel pole does not produce a moment saving.
