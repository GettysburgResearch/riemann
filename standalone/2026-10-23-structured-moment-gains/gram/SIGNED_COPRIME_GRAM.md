# A full coprime-pair estimate and the nonprincipal additive Gram term

Date: 23 October 2026.

**Status:** proposed analytic implications for independent mathematical
review. Sections 1--4 assume a stated common zero-free half-plane.
Section 5 imports the source's unmarked ordinary product moment M2;
its central-line conclusion does not assume that zero-free input.
Neither external analytic input is independently certified here.
No smaller zero-free boundary is proved.

**Scope:** a fixed number field, finite-order Hecke characters, full
coprime ordinary coefficient pairs, their actual zero extensions, and
the complete nonprincipal contribution to the additive Gram sum in
Liu's equation (13.7). A separate final improvement uses the source's
ordinary product moment M2 as an additional analytic input. Neither
column is a cubic Gauss coefficient or a
Möbius coefficient. Those different columns cannot be substituted.

**Source:** Baiying Liu, arXiv:2610.26835v1,
<https://arxiv.org/html/2610.26835v1>, Theorem 17.1 and Section 13.2,
especially Lemmas 12.10 and 13.1 and equations (13.5), (13.7). The arithmetic
finite-correlation identity, common-support extraction, common-profile
decomposition, and principal-frequency count used in Section 4 below
are imported from that exact source. The new steps are the signed
two-variable Mellin estimate, the multiplicative overlap mean obtained
from the full local correlation, and, in Section 5, an averaged Mellin
estimate using the source's Theorem 12.14 with no prime factors. The
fourth-moment passage there uses the ordinary approximate functional
equation and common profile separation, as in source Sections 14.2--14.3.

The conductor-uniform logarithm argument in PR #1009,
`standalone/2026-10-20-liu-all-field-artin-and-barrier/uniform_mobius_consequence.md`
at `d8e93ba4ab4dc593711c791ce3a002cb5d4796af`, is an earlier repository
proof of the underlying uniformization principle. We give the needed
steps here. This note is distinct from PR #1012's
`global/SIGNED_MOBIUS_GCD_TAIL.md`: that note estimates one long-divisor
sector of a cubic-Gauss pair, whereas the present theorem bounds an
entire coprime ordinary-character pair, including its short divisors.

## 1. The hypothesis and the two-variable theorem

Fix a number field F. Assume that, for one beta in [2/3,1), every
primitive finite-order Hecke function over F is zero-free in
Re(s)>beta. The principal simple pole at 1 is allowed. The constants
below may depend on F, beta and every displayed epsilon, but not on
the varying finite conductor or puncture.

Let chi be a primitive **nonprincipal** finite-order Hecke character,
with conductor norm q. Let R be a squarefree ideal containing all
additional primes to be deleted, and put

    lambda(a) = chi(a) 1_{(a,R)=1}.

The natural zeros of chi at its conductor primes are retained. Put
r = N rad(f_chi R); replacing r by q NR is harmless. For positive
scales N1,N2>=c>0 and a fixed smooth compactly supported function W
on (0,infinity)^2, define the finite sum

    C_lambda(N1,N2;W)
      = sum_{(a,b)=1} lambda(a) conjugate(lambda(b))
          W(Na/N1,Nb/N2).

**Proposition 1.** For every epsilon>0,

\[
 |C_\lambda(N_1,N_2;W)|
 \ll (q r N_1N_2)^\epsilon\,
       q^{\beta/2}(N_1N_2)^{\beta/2}\,
       \mathcal S_J(W).                                      \tag{1}
\]

Here J is a fixed finite derivative order, chosen after epsilon,
and S_J is a standard compact-box smooth seminorm. A family of
joint profiles with summable S_J norm is allowed. Fixed norm twists
in either variable have a fixed polynomial cost in their heights.
No arbitrary arithmetic coefficient depending on a or b is allowed.

The trivial bound O((N1N2)^(1+epsilon)) can always be combined with
(1) by taking the smaller bound. Unlike (13.5), (1) does not require
N1 or N2 to exceed the conductor scale.

There is also an asymmetric version. With Nmax=max(N1,N2) and
Nmin=min(N1,N2), the right side of (1) may be replaced by

\[
 (q r N_1N_2)^\epsilon q^{\beta/2}
 N_{\max}^{1-\beta}N_{\min}^{2\beta-1}\mathcal S_J(W). \tag{1a}
\]

Its ratio to (1) is (Nmax/Nmin)^(1-3beta/2), at most one. It improves
unbalanced pairs but does not improve the frequency powers obtained
below: the full overlap sum includes D=E=1, where it gives no saving.

## 2. Exact Euler factorization, with all zero masks

In Re(s),Re(t)>1 the two-variable Dirichlet series is

\[
 D_\lambda(s,t)=
 \sum_{(a,b)=1}\frac{\lambda(a)\overline{\lambda(b)}}{(Na)^s(Nb)^t}.
\]

At a prime outside f_chi R, coprimality permits at most one positive
valuation. Thus its factor is

\[
 1+\sum_{j\ge1}\chi(p)^j q_p^{-js}
   +\sum_{k\ge1}\overline{\chi(p)}^k q_p^{-kt}
 =\frac{1-q_p^{-s-t}}
 {(1-\chi(p)q_p^{-s})(1-\overline{\chi(p)}q_p^{-t})}.
                                                               \tag{2}
\]

The numerator is exactly 1-q_p^(-s-t), because chi has unit modulus
there. At deleted or conductor primes the actual local series is 1.
Writing L^R for the primitive L-function with the extra factors R
removed, we obtain

\[
 D_\lambda(s,t)=
 \frac{L_F^R(s,\chi)L_F^R(t,\bar\chi)}{\zeta_F(s+t)}
 \prod_{p\mid f_\chi R}(1-q_p^{-s-t})^{-1}.                  \tag{3}
\]

Every finite correction in (3) is necessary; cancellation of character
phases does not restore a deleted prime. On fixed substrips Re(s)>0,
Re(t)>0, Re(s+t)>beta, the extra numerator Euler factors and the
displayed reciprocal finite factors cost r^epsilon. To see uniformity,
for any fixed a>0 the sums of q_p^(-a) over the prime divisors of R
are o(log NR), uniformly as NR grows: split at a fixed cutoff, use
q_p^(-a)<=delta log q_p for larger primes, and absorb the finitely
many smaller primes into the constant. The same argument controls
the reciprocal factors using -log(1-q_p^(-a)).

Since chi is nonprincipal, both numerator L-functions are entire.
The pole of zeta_F at 1 produces a zero of its reciprocal. It causes
no contour residue. Its possible zeros are excluded in Re(s+t)>beta
by the hypothesis. Thus (3) is holomorphic in the region needed below.

If chi were principal, the two numerator poles would be crossed and
would produce a main term. This is why the nonprincipal condition is
essential and why Section 4 leaves the principal Gram term intact.

## 3. Uniform bounds and the two contour shifts

The common half-plane hypothesis implies, for every fixed d>0 and
e>0,

\[
 |L_F(\sigma+iv,\chi)|+|L_F(\sigma+iv,\chi)|^{-1}
 \ll \{q(3+|v|)^{[F:\mathbb Q]}\}^{e},\qquad
 \sigma\ge\beta+d,                                      \tag{4}
\]

for the nonprincipal characters. For zeta_F the analogous reciprocal
bound includes its continued value zero at its pole.

Here are the uniformity details. A polynomial conductor bound for the
pole-removed Hecke function follows from the Euler product and its
functional equation. Its analytic logarithm exists in the stated
zero-free half-plane and has uniformly bounded values on Re(s)>=3/2.
Center disks at 2+iv. Borel--Caratheodory on a disk whose left edge
lies strictly to the right of beta gives O(log(q(3+|v|)^n)) control
of the logarithm. Hadamard three-circles between the Euler disk and
that disk gives O((log(q(3+|v|)^n))^theta) at beta+d, with theta<1.
Exponentiation yields both signs of (4). This uses a common zero-free
boundary and ordinary uniform growth, not uniform constants in the
original proof of zero-freeness.

Fix a small d>0. The functional equation transports (4) from
sigma_+=beta+d to 1-sigma_+, giving the conductor factor
q^(sigma_+-1/2), times a fixed polynomial in the height. Interpolation
across this fixed strip gives

\[
 |L_F(\sigma+iv,\chi)|
 \ll q^{(\sigma_+-\sigma)/2+e}(3+|v|)^A,
 \qquad 1-\sigma_+\le\sigma\le\sigma_+.                    \tag{5}
\]

The exponent 1/2 is exact: the endpoint conductor exponent
sigma_+-1/2 divided by strip width 2sigma_+-1 is 1/2.
Finite-order infinity types range over a finite set; F is fixed.
Standard completed-function growth justifies this strip interpolation.

Choose sigma=beta/2+d, decreasing d relative to the desired epsilon.
Because beta>=2/3, this line lies within the strip of (5). Each
numerator in (3) costs q^(beta/4+e), while Re(s+t)=beta+2d
lies in the zero-free half-plane. Consequently

\[
 |D_\lambda(\sigma+iu,\sigma+iv)|
 \ll (qr)^e q^{\beta/2}(1+|u|+|v|)^A.                    \tag{6}
\]

Double Mellin inversion on initial lines (2,2) expresses the actual
sum as

\[
 \frac1{(2\pi i)^2}\int\!\int
 \widehat W(s,t)N_1^sN_2^tD_\lambda(s,t)\,ds\,dt.          \tag{7}
\]

First shift s to sigma with Re(t)=2; then shift t to sigma. In the
first shift Re(s+t)>beta, and in the second its minimum is
2sigma>beta. Neither shift crosses a numerator pole or a reciprocal
zeta pole. Rapid joint Mellin decay and the polynomial bounds remove
the horizontal segments. Use (6), choose enough fixed derivatives of
W, and absorb the positive powers d,e into epsilon. This proves (1).
All signs and the entire common-divisor identity have been retained.

For (1a), put the real part 1-beta+d on the variable of larger scale
and 2beta-1+d on the smaller. Their sum is beta+2d. Both lines lie
within the interpolation strip when beta>=2/3, and the total conductor
exponent in (5) is still beta/2 up to the allocated loss. The same
contour argument applies.

## 4. Full local overlap summation in the additive Gram bound

Use exactly Liu's variables in (13.7): Y=Y', Q=Q', and P=Y^2/Q.
The following statement concerns the actual common additive factor
after its original joint-profile separation and positive row majorant.
For P below the fixed nonzero dual-norm threshold there is no
nonzero-frequency contribution. Assume P>=c>0 otherwise.

The finite-correlation identity and complete common-support extraction
in the source give

    s1=D a, s2=E b, (a,b)=1, (ab,DE)=1,
    rad(D)=rad(E), C=gcd(D,E), C divides j.

The residual columns have scales N1~Y/ND, N2~Y/NE. Their character is
lambda(a) conjugate(lambda(b)), with every natural and common-prime
zero retained. The primitive conductor times the extra unramified
radical is O(Nj), apart from fixed source data. This is exactly the
source's qualification before (13.5). The separated profile is common
before D,E,j are fixed, and has finite weighted Mellin seminorm.

For nonprincipal inducing characters, Proposition 1 gives, before the
unchanged squared normalization Q/Y^3,

\[
 \ll Z^\epsilon Y^\beta
 \sum_{0<Nj\le cP}(Nj)^{\beta/2} A_\beta(j),            \tag{8}
\]

where the positive full-overlap majorant is

\[
 A_\beta(j)=
 \sum_{\substack{\operatorname{rad}(D)=\operatorname{rad}(E)\\
                         (D,E)\mid j}}
 \frac{|\mathcal F(D,E;j)|}{(ND\,NE)^{\beta/2}}.       \tag{9}
\]

Actual columns have ND,NE=O(Y). Extending this positive majorant to
all exponents can only increase it. The extension converges locally
because beta>0. Neither D nor E is made squarefree, and both unequal
orientations are present.

### 4.1. Exact local factor

Let p have norm q, let t=v_p(j)>=1, and write c=min(v_p(D),v_p(E)).
The source's Lemma 12.10 gives these absolute local correlations:

- Equal valuations c<t contribute q^(c-1)(q-1).
- Equal valuations c=t with 6 not dividing t contribute q^(t-1).
- Equal valuations c=t with 6 dividing t contribute q^(t-1)(q-2).
- Unequal valuations c and c+a, a>=1, contribute zero unless c=t and
  6 divides t; then their absolute value is q^(t-1)(q-1).

The last case has two orientations. CRT phases have absolute value one;
the finite unit sector does not change these valuations. Thus A_beta is
multiplicative on exterior ideals, with A_beta(p^0)=1 and

\[
\begin{aligned}
 A_\beta(p^t)={}&1+(1-q^{-1})
                   \sum_{c=1}^{t-1}q^{c(1-\beta)}\\
 &+1_{6\nmid t}q^{t(1-\beta)-1}\\
 &+1_{6\mid t}q^{t(1-\beta)}
 \left(1-\frac2q+
    2(1-q^{-1})\frac{q^{-\beta/2}}{1-q^{-\beta/2}}\right).
                                                               \tag{10}
\end{aligned}
\]

In particular A_beta(p)=1+q^(-beta). The saving at this local factor
is substantial: when D=E=j=p, the actual finite correlation is -1
up to a unit phase, whereas its crude bound NC is q. The principal
sixth-power local case is different and is explicitly retained in (10).

### 4.2. First and second means of the overlap weight

For every fixed beta in [2/3,1),

\[
 \sum_{Nj\le P} A_\beta(j)\ll P,
 \qquad
 \sum_{Nj\le P} A_\beta(j)^2\ll P.                    \tag{11}
\]

The constants may depend on the fixed field and beta. A convenient
proof also covers beta=1, which will be used in Section 5.

Put a=1-beta. For 0<a<=1/3, the nonterminal part of (10), at t>=2,
is O_beta(q^((t-1)a)), and the additional terminal part is
O_beta(1_{6|t}q^(ta)). The constants are uniform in q>=2. Consequently

\[
 \sum_{t\ge1}\frac{|A_\beta(p^t)^2-1|}{q^t}
 \ll_\beta
 q^{-1-\beta}+q^{-2\beta}+q^{-6(2\beta-1)}.           \tag{12}
\]

For t=1 use A_beta(p)=1+q^(-beta); for t>=2 sum the two geometric
series just displayed, including their cross term by 2xy<=x^2+y^2.
All three prime sums converge when beta>=2/3. At beta=1 the regular
part is O(t), its squared tail is O(q^(-2)), and the sixth-power
terminal part remains bounded, so the same convergence conclusion
holds.

For completeness, define the multiplicative coefficients
b_r=mu_F*(A_beta^r), r=1,2, where the power is pointwise. At a prime
power b_r(p^t)=A_beta(p^t)^r-A_beta(p^(t-1))^r. Equation (12) and its
first-power counterpart imply

    sum_d |b_r(d)|/Nd < infinity.

Use A_beta^r=1*b_r and ordinary ideal counting to obtain (11).
This argument keeps the whole prime-power overlap; it is not a count
of squarefree substitutes.

By (8) and the first estimate in (11), the complete nonprincipal
contribution is therefore

\[
 \boxed{\quad
 \frac QY\frac{P^{1+\beta/2}}{Y^{2-\beta}}Z^\epsilon.
 \quad}                                                   \tag{13}
\]

The zero-frequency and principal-inducing-frequency estimates are
unchanged. Hence the source-dependent Gram bound obtained from the
common zero-free hypothesis alone is

\[
 \boxed{\quad
 \sum_{[k]\ne0}|\widetilde A_{[k]}|^2
 \ll \frac QY
 \left(1+P^{1/6}+\frac{P^{1+\beta/2}}{Y^{2-\beta}}\right)
 Z^\epsilon.
 \quad}                                                   \tag{14}
\]

Using only |F(D,E;j)|<=NC and Rankin's supported-pair count instead
would give P^(2-beta/2)/Y^(2-beta). The exact local sum (10) gains the
additional factor P^(1-beta). No new analytic input is needed for this
additional gain.

## 5. A stronger averaged consumer of the source's unmarked M2

This section additionally assumes Liu's Theorem 12.14 with z=0,
including its arbitrary bounded ordinary lengths, natural zeros,
finite-order coefficient group, polynomial norm-twist bounds, and
common profile uniformity. This is an external analytic input; the
present note does not supply an independent proof of M2.

The field and arithmetic data are now those of the source's comparison:
a fixed cyclotomic field containing mu_12, its fixed finite set S and
finite unit sectors. The ordinary approximate functional equation and
the same common-scale profile decomposition give, for
1/2<=sigma<=3/5,

\[
 \sum_{\substack{0<Nu\le V,\ u\ \text{sixth-power-free}\\
                         \chi_u^*\ne1}}
 |L_F(\sigma+it,\chi_u^*)|^4
 \ll V^{1+\epsilon}(1+|t|)^A.                           \tag{15}
\]

Here chi_u^* denotes the primitive inducing character with its actual
unit sector. This moment is ordered by the norm of the Kummer row u,
not by an unconstrained conductor family.

### 5.1. Justification of the L-function moment

At sigma>=1/2 an approximate-functional-equation annulus of ordinary
length D has a factor D^(1/2-sigma) relative to a centrally normalized
plain polynomial. It is at most one on nonempty annuli D>=c, up to a
fixed profile constant. The dual half has factor
q_f^(1/2-sigma)D^(sigma-1/2) and D at most sqrt(q_f), up to height
scales; this is again at most one up to a fixed polynomial height
factor. Fixed S factors have bounded cost on these strips.

For sixth-power-free u, all exterior primes dividing u genuinely
ramify in chi_u^*: source (14.12) identifies the primitive function
with the same ordinary row presentation outside S. Each fourth power
of a plain annulus is precisely M2 with its two ordinary factors equal
and no prime factors. The source's common-scale supremum and weighted
Fourier measure deal with conductor-dependent AFE profiles before the
positive row norm. They have finite seminorms and polynomial height
cost. Hilbert-space triangle over the dyadic annuli costs only a
subpower factor. The rapid AFE tails are summed before positivity.
These are the same fourth-moment steps used in the proof of source
Proposition 14.3, with its selected prime product empty.

Thus (15) includes varying conductors, zeros, and the finite unit
classes. It does not assert a fourth moment for arbitrary column
coefficients. Bounded nonprincipal unit rows have fixed primitive
conductors and satisfy the same bound directly. For V>=2 and |t|<=V,
the analytic conductor is at most a fixed power of V, so every
retained AFE length is in M2's bounded exponent range; all profile
orders and norm twists have the supplied polynomial height bounds.
For |t|>V, a uniform growth bound of the form
q_f^A(1+|t|)^A absorbs q_f<=O(V) into an increased height power.
Summing over O(V) rows proves (15) for these heights as well.
Thus the argument handles the entire Mellin integral, rather than
requiring a height cutoff such as |t|<=V^(1/100).

Every integral frequency has the unique ideal decomposition j=u e^6
with u sixth-power-free. The primitive inducing character is that of
u, up to its retained finite unit sector. Summing (15) over e, using
sum_e(Ne)^(-6)<infinity, gives

\[
 \sum_{\substack{0<Nj\le P\\\chi_j^*\ne1}}
 |L_F(\sigma+it,\chi_j^*)|^4
 \ll P^{1+\epsilon}(1+|t|)^A.                           \tag{16}
\]

The extra zeros contributed by e are still retained in the original
pair. On every positive real strip their finite Euler factors cost
(Nj)^epsilon, so using the primitive L-values for this majorant does
not discard them or alter the exact Euler factorization.

### 5.2. Averaging before paying the conductor factor

Return to double Mellin inversion for the full nonprincipal Gram
sum, with the original common smooth profile kept until this point.
For this reflected variant take 4/5<=beta<1, which includes the
inherited B_flat and keeps the reflected values within the exact
strip of the source's AFE lemma. Section 5.3 has no such hypothesis.
Move both variables to Re(s)=Re(t)=beta/2+d. All puncture factors and
the reciprocal zeta factor are bounded as in Sections 2--3. Apply the
functional equation separately to both primitive numerator functions.
Their combined conductor factor is at most

    (Nj)^(1-beta+epsilon) <= P^(1-beta+epsilon),

and their reflected real parts are at least 1/2 when d is chosen
small. The remaining numerator factors have the fourth moments (16).
After the positive full-overlap sum, Cauchy--Schwarz and (11) give

\[
\begin{aligned}
 &\sum_{Nj\le P,\ \chi_j^*\ne1}
 A_\beta(j)
 |L_F(1-s,\bar\chi_j^*)L_F(1-t,\chi_j^*)|\\
 &\quad\le
 \left(\sum_{Nj\le P}A_\beta(j)^2\right)^{1/2}
 \left(\sum_{Nj\le P,\ \chi_j^*\ne1}
       |L_F(1-s,\bar\chi_j^*)L_F(1-t,\chi_j^*)|^2
       \right)^{1/2}\\
 &\quad\ll P^{1+\epsilon}(1+|\Im s|+|\Im t|)^A.      \tag{17}
\end{aligned}
\]

The last product moment follows by a further Cauchy--Schwarz from (16)
at the two heights; conjugation changes the height sign and preserves
the common allowed presentation. Mellin decay absorbs the displayed
height cost. The resulting full nonprincipal term is

\[
 \boxed{\quad
 \frac QY\left(\frac PY\right)^{2-\beta}Z^\epsilon.
 \quad}                                                   \tag{18}
\]

All D,E prime powers and all frequency powers were summed in (10),
(11) and (16). There is no remaining short-common-divisor sector in
this ordinary-pair estimate.

### 5.3. Central-line consequence requiring no zero-free input

There is an especially simple version of the averaged argument. Move
both Mellin variables to Re(s)=Re(t)=1/2+d. Their sum is strictly
larger than 1, so 1/zeta_F(s+t) is bounded by its absolutely convergent
Euler product. No zero-free hypothesis is used. The numerator values
already lie on the lines covered by (16), so no functional equation
or conductor factor is needed. The full-overlap weight is at most
A_1(j); the beta=1 case of (11) gives its second moment O(P).
Alternatively (10) gives A_1(p^t)<=C(t+1), hence
A_1(j)<<_epsilon(Nj)^epsilon by the usual divisor-product bound;
the ordinary numerator moments alone then finish this central case.
The complete nonprincipal contribution is

\[
 \boxed{\quad
 \frac QY\frac PY Z^\epsilon= Z^\epsilon,
 \quad P=Y^2/Q.\quad}                                   \tag{19}
\]

Consequently the same original additive Gram sum satisfies, under
unmarked M2 and the source's local identities,

\[
 \boxed{\quad
 \sum_{[k]\ne0}|\widetilde A_{[k]}|^2
 \ll\left\{\frac QY(1+P^{1/6})+1\right\}Z^\epsilon.
 \quad}                                                   \tag{20}
\]

In the source's physical tuple range, Q/Y=X'>=1 because l_x>ell
and the selected-subset length d<=ell. The final 1 in (20) is then
absorbed by the zero-frequency bound. Thus the nonprincipal term
places no extra length restriction on that direct estimate.

This central-line statement uses the source's M2 theorem but not the
common zero-free half-plane from Proposition 1. Formula (18) remains
a stronger numerical estimate when P<Y and that common half-plane is
also supplied.

## 6. Exact comparison and the boundary that does not move

With beta=B_flat=0.874886647039964..., the source's nonprincipal factor
P^2/Y is successively improved to

    common zero-free input, exact local sum:
        P^(1.437443323519982...)/Y^(1.125113352960036...),
    plus the source's unmarked M2:
        (P/Y)^(1.125113352960036...),
    unmarked M2 alone, central lines:
        P/Y.

The first ratio to the source bound is
P^(-(1-beta/2))Y^(beta-1). The ratio of the second to the first is
P^(1-3beta/2), a further saving because beta>2/3.

At the empty selected subset, P=Z^b and Y=Z^l_y. The condition making
the first new nonprincipal term no larger than the principal P^(1/6)
term is

\[
 l_y\ge\frac{5/6+\beta/2}{2-\beta}b,                 \tag{21}
\]

in place of l_y>=11b/6. The coefficient in (21) is about 1.12947,
compared with 1.83333 in the source. Under M2, (20) removes this
additional restriction whenever X'>=1.

For a selected subset of length d, the exponent using (14) is

\[
 L_{\rm new}(d)=l_x/2-d+(d+5\ell-1)_+/8
   +\frac12\max\left(0,b/6,
        (1+\beta/2)b-(2-\beta)(l_y-d)\right).          \tag{22}
\]

Both positive-part terms are Lipschitz, so

    L_new(d)-L_new(0) <= (1/8-beta/2)d < 0.

For (20) in the physical range, the last maximum reduces to
max(0,b/6), and the corresponding slope bound is -7d/8. In either
case the empty subset remains the worst tuple.

The principal P^(1/6) term survives. Already D=E=1 has local overlap
weight one, and a principal frequency is a sixth power up to the
fixed unit data. Its residual character pair has two numerator poles
and a genuine main term, so neither Proposition 1 nor (15) applies
to it. Averaging the exact local overlap therefore cannot delete this
term.

At the inherited B_flat optimizer the source's former nonprincipal
term was already smaller than its principal term. The operator gain
above is real, but it does not lower the optimized zero-free boundary.
The completed-theta norm (13.6) and the high-side detected-row
remainder are unchanged. In the same balanced geometry the direct
exponent still contains (5ell-1)_+/8. Its boundary contribution is

    11/12-ell/4+(5ell-1)_+/8,

whose minimum on the original physical range is 13/15 at ell=1/5.
Thus this additive-Gram improvement alone does not supply 5/6.

The gain is active in other physical regimes. For example, with
beta=7/8, ell=1/6, b=2/5, one has l_x=13/60>ell and l_y=37/60.
The source's nonprincipal Gram exponent is 11/60, larger than its
principal exponent 1/15. Formula (14) lowers that nonprincipal exponent
to -19/160, and (20) removes it entirely from the direct maximum.
The direct bound improves from Z^(1/5+epsilon) to
Z^(17/120+epsilon), a fixed saving of Z^(7/120).
This is a comparison of proved direct upper bounds; the separate
high-side closure conditions have not been asserted at that point.

Applying any of these estimates to the centered inverse projector's
residual cubic Gauss columns would be invalid. Those columns have a
different Dirichlet series with genuine completion-factor poles;
their signed long-divisor estimate in PR #1012 does not make them
ordinary character columns. The present M2 consumer likewise uses
only ordinary Hecke polynomials and makes no inverse-moment claim.

The companion `check_signed_coprime_gram.py` enumerates 2,298 exact
finite-field correlations covering both unequal orientations, principal
sixth-power branches and zero strata, independently compares 42 small
original-modulus sums, and checks all six character powers in the
coprime Euler identity with deleted-prime corrections. It also checks
the preceding newly active exponent regime with rational arithmetic.
The recorded run is in `SIGNED_COPRIME_GRAM_CHECK.txt`. These finite
diagnostics check arithmetic transcription and expose the role of the
zero masks; they do not certify the imported analytic inputs or a
zero-free theorem.

## 7. Heath--Brown decomposition check (exploration, not a theorem here)

For mu_X supported on norms at most X, the exact Dirichlet-convolution
identity on norms n<=X^J is

    mu = sum_{j=1}^J (-1)^(j-1) binom(J,j)
             mu_X^{*j} * 1^{*(j-1)}.

Indeed the omitted term is mu*(delta-1*mu_X)^{*J}; each nonzero
factor in the final power has norm>X. Applying unmarked M2 to this
identity would require a moment estimate for products of truncated
inverse polynomials. The j=J, all-inverse dyadic sector, with every
ordinary variable of bounded norm and inverse factors near X, has
total inverse length comparable to D=X^J. M1 does not automatically
control that product, and M2 applies to its ordinary factors rather
than to mu_X. For fixed J the X-smooth support has no fixed power
scarcity as D grows. This identifies the unresolved sector; it is
not a proof of impossibility for a signed multivariate argument.

