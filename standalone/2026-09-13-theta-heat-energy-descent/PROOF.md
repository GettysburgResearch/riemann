# A positive heat-energy sequence with an exact angular growth law

Date: 2026-09-13. Proposed continuation of PR #842.
Frozen predecessor: 346f630299252183aec2d8c41a0f3b4027bb9d19.
Status: PROPOSED COMPLETE COMPONENT ARGUMENTS; independent review required.
**RH, native cofinal energy descent, and complete monotonicity remain unproved.**

The preceding packet constructs a reciprocal-xi subordinator and separates
positivity/decrease of its Levy kernel from complete monotonicity. This note
attacks the latter by a different positive quantity: the full squared norm of
each derivative, normalized by a gamma integral. The resulting sequence has
an exact growth law, not merely an upper estimate or a finite sign table.
If RH is false it eventually grows geometrically. If RH is true it decreases
at every step. Hence arbitrarily late downward steps suffice for RH.

That last source inequality is NOT proved here. This is not an RH proof with
a routine final lemma delegated to reviewers. The abstract tools (Laplace
integration, Gram matrices, spectral power dominance, Mellin Plancherel and
integration by parts) are classical; no external priority claim is made.

## 1. Fixed source and a fixed shift removing numerical prerequisites

Retain the unstandardized full-line theta density and the entire completion:

    Xi(z)=xi(1/2+iz)=integral_R phi(x) exp(izx) dx,
    phi(x)=sum_(n>=1) exp(x/2-Q_n)(4Q_n^2-6Q_n),
    Q_n=pi n^2 exp(2x), w=phi/Xi(0).

Jacobi inversion gives evenness; positivity on the positive half-line and
reflection give phi>0. Every fixed derivative has double-exponential tails.
These are the classical theta-source facts used throughout #842. No variance
standardization is made. Put M(h)=xi(1/2+h)/xi(1/2)=integral exp(hx)w(x)dx.

The usual strip theorem, conjugation/reflection and Hadamard product for xi
are the analytic inputs [D1,D2]. In particular the nontrivial zeros are
rho=beta+i gamma, 0<beta<1; take gamma>0 and retain analytic multiplicities.
There are no nontrivial real zeros (also immediate from M(h)>0 for real h).
Define one centered node per +/- pair of Xi zeros, and then its SHIFTED square:

    z_rho=gamma-i delta, delta=beta-1/2,
    a_rho=1+z_rho^2=x_rho+i y_rho,
    x_rho=1+gamma^2-delta^2>gamma^2+3/4,
    y_rho=-2 gamma delta.                                      (1)

Distinct nodes a_j are grouped, with their positive integer multiplicities m_j.
A noncentral quartet contributes BOTH conjugate nodes. All such nodes are
retained. Since Re z_rho>0 the squaring does not identify distinct upper-ordinate
zeros. No simplicity assertion is made.

Unlike the unshifted kernel, (1) needs NO finite verification of low zeros to
put all rates in the right half-plane. The shift is fixed at ONE throughout.
It is not a sequence of increasing shifts that could erase angular defects.
The exact algebraic identity

    x^2-3y^2 = [gamma^2-(1-delta^2)]^2
                  +4 gamma^2(1-4delta^2) > 0                (2)

shows |a|/x <= 2/sqrt(3). Also |a|/x ->1 as gamma->infinity.
The strict inequality in (2) holds for the actual open strip.

For completeness, the positive theta tail gives
log max_(|z|<=R)|Xi(z)|=O(R log(R+2)), by absolute integration and the
substitution u=exp(2|x|). The even function F(v)=Xi(sqrt(v))/Xi(0), defined
by its power series, therefore has order at most 1/2<1. Its normalized
Hadamard product is genus zero. Translation in v by one preserves this fact,
so sum_j m_j/|a_j|<infinity. By (2),

    S:=sum_j m_j/x_j <infinity.                             (3)

Put

    h(t)=exp(-t) H(t)=sum_j m_j exp(-a_j t), t>0,             (4)

where H is the parent's central zero heat trace. The series and every fixed
derivative converge absolutely on compact subsets of Re(t)>0: the leading
real growth is gamma^2, while the imaginary growth is at most gamma.
Conjugation makes h(t) real for positive real t. We do NOT assume its
higher derivatives have any signs.

The logarithmic derivative of the translated genus-zero product gives

    Q:=sum_j m_j/a_j
      = (1/2) xi'(3/2)/xi(3/2)
      = M'(1)/(2M(1)) >0.                                 (5)

Positivity follows from integral x sinh(x)w(x)dx>0. Since
1/x_j=(|a_j|/x_j)^2 Re(1/a_j), (2) gives S <=(4/3)Q.
This does not replace a signed zero sum by an absolute sum: every
Re(1/a_j)>0 and the displayed inequality is termwise.

The main results below use (1)--(5), NOT the parent's new all-time heat sign,
its numerical anchor, its PT finite census, or its probability construction.
Those proposed results supply interpretation but are not extra proof premises.

## 2. HE1: a finite full derivative energy at every order

For every integer n>=0 define

    E_n = 4^n/(2n+1)! integral_0^infinity
                          t^(2n+1) |h^(n)(t)|^2 dt.         (6)

It is a strictly positive number. The complete time interval is part of the
definition. No finite zero list, truncated moment vector, or approximation
index occurs in (6).

**HE1.** For every n>=0,

    E_n=sum_(j,k) b_jk w_jk^n,                              (7)
    b_jk=m_j m_k/(a_j+conj(a_k))^2,
    w_jk=4 a_j conj(a_k)/(a_j+conj(a_k))^2,

and the double series is absolutely convergent. Put R=sup_j |a_j|/x_j.
Then

    0<E_n <= (R^(2n)/4) S^2
            <= (4/3)^(n+2) Q^2/4.                         (8)

Proof. Expanding the MODULUS square retains all ordered pairs. The gamma
integral [D3] gives

 integral_0^infinity t^(2n+1) exp[-(a_j+conj(a_k))t]dt
       =(2n+1)!/(a_j+conj(a_k))^(2n+2).

For an absolutely justified expansion, first integrate the sum of absolute
values of the terms before taking any cancellation. Its normalized value is
bounded by

 sum_(j,k) 4^n m_jm_k |a_j|^n |a_k|^n/(x_j+x_k)^(2n+2)
 <= R^(2n) sum_(j,k) m_jm_k/(x_j+x_k)^2
 <= R^(2n) S^2/4.                                        (9)

Here 4x_jx_k <=(x_j+x_k)^2. Tonelli/dominated convergence prove (7),
including convergence in the weighted L2 norm of all finite-section derivatives.
If h^(n) were identically zero, h would be a polynomial; its decay at infinity
would force h=0. But integral h(t)dt=Q>0 by absolute convergence and (5).
Thus E_n>0. This also proves every claimed quotient below has nonzero denominator.

The estimate also gives a complete optional finite-section error. For any
conjugation-closed finite node set P, write S_P=sum_(j in P)m_j/x_j and assume
T >=sum_(j not in P)m_j/x_j. If E_n[P] uses the FULL norm of that finite
exponential sum, then

    |E_n-E_n[P]| <= R^(2n)(2S_P T+T^2)/4,                 (10)
    |sqrt(E_n)-sqrt(E_n[P])| <= R^n T/2.

This is not a positive lower bound from a positive prefix. In particular a
fixed T with R>1 cannot be ignored when n grows. No actual divisor truncation
or native E_n numerical enclosure is executed in this packet.

## 3. HE2: exact growth and ratio limits, retaining all multiplicities

Define the angular defect for THIS fixed shift by

    D_* = sup_rho [2 gamma (beta-1/2)
                     /(1+gamma^2-(beta-1/2)^2)]^2.         (11)

Then R^2=1+D_*, and 0<=D_*<=1/3. The supremum of real parts beta need not
be attained. Nevertheless, if D_*>0, the maximum in (11) IS attained by a
finite, nonempty node set: the ratio tends to zero as gamma->infinity and
there are only finitely many zeros in a bounded height region.

**HE2.** The actual positive energies have the unconditional limits

    lim_(n->infinity) E_(n+1)/E_n = 1+D_*,                  (12)
    lim_(n->infinity) log(1+E_n)/n = log(1+D_*).            (13)

More precisely, if D_*>0 and J_*={j:|a_j|/x_j=R}, then for some
0<=r<R^2 and finite B,

    E_n=C_* R^(2n)+O(B r^n),
    C_*=sum_(j in J_*) m_j^2/(4x_j^2)>0.                  (14)

If D_*=0, every a_j is positive real and

    E_n strictly decreases to C_0=sum_j m_j^2/(4a_j^2)>0.  (15)

Proof. Formula (7) satisfies

 |w_jk| <= (|a_j|/x_j)(|a_k|/x_k)
                *4x_jx_k/(x_j+x_k)^2 <= R^2.             (16)

Equality at R^2 requires BOTH nodes to have ratio R, equal real parts, and
Im(a_j)=Im(a_k), since equality was also needed in
|a_j+conj(a_k)|>=x_j+x_k. Thus equality occurs precisely when j=k is a
maximal-ratio DISTINCT node. Its coefficient b_jj=m_j^2/(4x_j^2) is
strictly positive. Grouping multiplicities first is essential: these are
squared multiplicities in a squared-norm calculation, not a simplicity premise.

Choose r0 with 1<r0<R. Outside a finite node set, |a_j|/x_j<=r0.
Any pair having an index outside that set has |w_jk|<=R r0<R^2.
Inside the finite set, the maximum modulus of all remaining nonmaximal pairs
is strictly below R^2 by the equality conditions. This proves a UNIFORM gap
r<R^2 after retaining all maximal diagonals. Since sum |b_jk|<=S^2/4,
(14) follows, including the entire infinite real and nonreal tail.
It immediately implies (12)--(13) in this case.

When D_*=0, (7) has positive coefficients and
0<w_jk=4a_ja_k/(a_j+a_k)^2<=1, with equality just at j=k.
Dominated convergence yields (15). There are at least two distinct zeros
(in fact infinitely many), so off-diagonal terms make each decrease strict.
The positive limit gives the ratio limit 1 and logarithmic limit zero.

This proves the stated dichotomy. It is not a claim that D_* has been shown
zero, nor an effective numerical threshold for the asymptotic (14).
Hypothetical arbitrarily high/close-to-central zeros have a small but fixed
positive rate. The constants and first dominant n can depend on the full divisor.

## 4. HE3: infinitely many downward steps, rather than every sign, would suffice

The following are equivalent for the unchanged xi source:

  (a) RH;
  (b) E_(n+1)<=E_n for EVERY n>=0;
  (c) for EVERY N there is n>=N with E_(n+1)<=E_n;
  (d) liminf_(n->infinity) log(1+E_n)/n =0;
  (e) E_n=exp(o(n)).                                      (17)

Indeed (a) gives (15). If RH is false, D_*>0 and (14) makes E_(n+1)>E_n
for all sufficiently large n, while (13) is strictly positive. This proves
all the implications. The same conclusion follows from a subexponential
upper certificate on any UNBOUNDED subsequence, however sparse.

No rate of occurrence of the downward steps is required. This is an exact
relaxation of the stated proof target, not proof that the relaxed inequality
holds. The initial finite sequence, even if decreasing, cannot establish (c).
A sufficient convenient upper bound would be E_n<=C exp(sqrt(n)) eventually,
or any polynomial bound, but no such native estimate is supplied.

## 5. HE4: an exact logarithmic-frequency variational formulation

Let u be log time and put

    f_n(u)=exp((n+1)u) (-1)^n h^(n)(exp u),
    V_n= integral_R |f_n'(u)|^2du / integral_R |f_n(u)|^2du. (18)

Each f_n is real, lies in H1(R), and is nonzero. Its squared L2 norm is the
unnormalized integral I_n in (6). Direct differentiation gives

    f_(n+1)=(n+1)f_n-f_n'.                                (19)

HE1 for n and n+1 puts both terms on the right in L2. Thus f_n is in H1;
cutoff integration by parts gives Re integral f_n' conj(f_n)=0 without
assuming an unproved pointwise endpoint asymptotic. Consequently

    I_(n+1)=(n+1)^2 I_n+integral |f_n'|^2,
    E_(n+1)/E_n=[(n+1)^2+V_n]/[(n+1)(n+3/2)].             (20)

Hence the cofinal descent target has exactly the form

    V_n <=(n+1)/2 for arbitrarily large integers n.         OPEN-E

Moreover HE2 proves the UNCONDITIONAL limit

    lim_(n->infinity) V_n/(n+1)^2 =D_*.                    (21)

Under RH, V_n<=(n+1)/2 at every order. If RH is false, V_n is asymptotic
to the positive constant D_* times n^2. There is no intermediate exponent
for this particular source sequence. Merely showing V_n=o(n^2) along an
unbounded subsequence would also finish.

One may describe V_n as logarithmic-frequency energy. It is not a variance
of zeta ordinates or an assumed random-matrix model. A Fourier-Plancherel
identity makes the description literal. Define the convergent secondary sum

    Z_1(s)=sum_j m_j a_j^(-s), Re(s)=1,

using the principal argument of a_j in (-pi/6,pi/6). At each fixed imaginary
part this is absolutely convergent by (3). Termwise gamma integration gives

    Fourier(f_n)(v)=Gamma(n+1-i v) Z_1(1-i v),             (22)
    E_n=4^n/[(2n+1)! 2pi] integral_R
                   |Gamma(n+1+i v) Z_1(1+i v)|^2dv.

Absolute L1 for the termwise transform follows from
n! sum m_j |a_j|^n/x_j^(n+1)<=n! R^n S. H1-Plancherel also identifies V_n
with the v^2-weighted ratio of the integrals in (22). This does not make
Z_1 a positive Fourier measure: that would already assume all a_j real.

## 6. Source evaluation and relationship to the probability construction

There is no need to define h using a numerical zero table. The parent's exact
all-prime formula, multiplied by exp(-t), is

 h(t)=exp(-3t/4)
   +exp(-t)/(4sqrt(pi t)) [I(t)-gamma_E-log(pi)-2P(t)],
 I(t)=integral_0^infinity
       [exp(-v)-exp(-v/4-v^2/(16t))]/[1-exp(-v)]dv,
 P(t)=sum_(k>=2) Lambda(k)/sqrt(k) exp[-log(k)^2/(4t)].      (23)

The two numerator terms of I must stay combined at v=0, and every prime power
occurs. For each fixed derivative order, the series and integral may be
differentiated on compact subintervals of t>0: the Gaussian in log(k) or v
absorbs all finite polynomial derivative factors. This proves that (6) and
(18) are specified by the native arithmetic source, not fitted spectral data.

For clarity, (23) can be reconstructed independently from

 integral_0^infinity exp(-s t) h(t)dt
       = [xi'/xi(1/2+sqrt(1+s))]/[2sqrt(1+s)], s>=0.       (24)

Insert the Euler logarithmic derivative at Re(1/2+sqrt(1+s))>1 for s>=0,
use the standard digamma integral and the Gaussian Laplace identity. At the
origin v=0 retain the difference before Tonelli/Fubini; split the numerator
as in the preceding proof. The strip (1), absolute reciprocal summability,
and Laplace uniqueness identify this formula with (4). No higher-order sign
is used in this derivation.

The entire time integral in (6), including its small-time end, is paid by
(9), not by numerical quadrature. This packet gives no practical all-n
native integration algorithm or new native value of E_n.

If the predecessor's proposed heat positivity is accepted, h is the Levy
kernel of the exponentially tilted reciprocal-xi subordinator, with exponent

 Psi_1(s)=Psi(s+1)-Psi(1)
         =log[xi(1/2+sqrt(1+s))/xi(3/2)].                 (25)

Thus exp(-tau Psi_1(s)) is an exact Laplace transform. This probabilistic
interpretation is additional context, not a premise of HE1--HE4.
Complete monotonicity of h is equivalent to RH: its positive exponential
representation under RH is explicit, while a positive Laplace-mixture
representation would make (24) Stieltjes, excluding its nonreal poles.
The new cofinal energy criterion tests the SAME fixed source property but
requires neither an Ising realization nor every individual derivative sign.

## 7. A completely accounted test of the tempting automatic descent

Positivity and decrease of a heat kernel do not prove OPEN-E. The exact
synthetic kernel used in the parent is

    h_*(t)=2 exp(-t)+2 exp(-2t) cos(t).                    (26)

It is positive for t>0, since exp(t)+cos(t)>0. Also -h_*'>0: for
0<t<=1, 2exp(t)+4cos(t)+2sin(t)>0 using cos(t)>=1/2 and sin(t)>=0;
for t>=1, 2exp(t)>2e>5>sqrt(20), which dominates |4cos(t)+2sin(t)|.
This is a legitimate positive decreasing kernel, not the theta kernel.

Its distinct rates are 1 (multiplicity 2), 2+i and 2-i (multiplicity 1).
The complete integral, with NO time cutoff, has the rational closed form

 E_n^*=53/50+(1/8)(5/4)^n
          +8 Re{ d r^n },
 d=(4+3i)/50, r=(22+4i)/25.                              (27)

Here |d|=1/10, |r|=2/sqrt(5)<9/10, |r-1|=1/5. Hence

 E_(n+1)^*-E_n^*
   >=(1/32)(5/4)^n-(4/25)(9/10)^n>0,  n>=5.             (28)

The last inequality holds rationally at n=5 and its first-to-second-term
ratio increases thereafter. E_n^*/(5/4)^n ->1/8 and V_n^*/(n+1)^2 ->1/4.
For example E_0^*=73/40. Thus even an exactly constructed positive decreasing
Levy kernel and all the parent's factorial-weighted positivity cannot supply
a universal derivative-energy descent theorem.

This synthetic law is not xi, is not asserted to be an original theta
magnetization, and does not refute the native estimate. It tests one inference.
The new direct attempt was to turn the original positive-process structure
into the reverse weighted inequality I_(n+1)<=(n+1)(n+3/2)I_n. Integration
by parts gives only the equality (20), with the nonnegative but uncontrolled
V_n. Discarding V_n reverses the required estimate. No native upper bound
V_n=o(n^2), or a proof of cofinal OPEN-E, was obtained.

## 8. Repository synthesis and honest completion boundary

The parent at 346f630 supplies a positive process and exact source identity;
its derivative-sign endpoint remains open. #881 at ab663f7 supplies a DIFFERENT
nonlocal similarity-energy objective. That manuscript was read for comparison;
no metric inequality is imported here. #875's latest Newton-tail and #869's
four-route entries were read at PR-description level only; no full theorem
from those changing branches is silently used. The earlier #379 all-center
heat criterion and the #839/#841/#842 cumulant-index programmes are credited
as background; this is not a claim to have discovered heat or moment RH tests.

The addition is the explicit full two-index energy formula, exact angular
asymptotic including the infinite tail, and the cofinal-descent/Fourier-energy
consumer for the unchanged source. It is not a finite-Hankel certificate,
a numerical evaluation of the native angular defect, a new zero-free strip,
or a proof of an energy upper bound at the needed asymptotic strength.

The remaining sufficient statement is precisely

    for every N there is n>=N with V_n <=(n+1)/2,

or, more permissively, V_(n_j)=o(n_j^2) on some unbounded sequence. All quantities
are specified in (18),(23). Their exact limit exists by HE2, but has not been
shown zero. The easy upper estimate (8) is geometric, not subexponential.
Reviewers are asked to reconstruct the component proof, especially the
maximal-pair gap and infinite dominated convergence, NOT to supply OPEN-E.

## References / attribution

[D1] NIST DLMF 25.10(i), critical strip, conjugation/reflection, infinitude.
https://dlmf.nist.gov/25.10
[D2] NIST DLMF 25.4.3--4, entire xi normalization and reflection; the classical
Hadamard theorem is applied to the source-derived order<1 entire function.
https://dlmf.nist.gov/25.4
[D3] NIST DLMF 5.9.1, gamma integral for positive real part of the rate.
https://dlmf.nist.gov/5.9
[D4] Konstantopoulos--Patie--Sarkar, Ann. Inst. Fourier 74 (2024), 377--421,
DOI 10.5802/aif.3600. Context for van Dantzig versus Lee--Yang; no theorem
from this paper is required for HE1--HE4.
[P] PR842, standalone/2026-09-12-theta-reciprocal-subordinator/PROOF.md,
commit 346f630299252183aec2d8c41a0f3b4027bb9d19. Full local manuscript read;
source identity reconstructed above. No predecessor numerical campaign rerun.

The finite checker tests rational model identities, complete finite-exponential
integrals, multiplicity grouping, the logarithmic derivative identity, strip
geometry and tail-majorant algebra. It does not machine-prove the infinite
arguments or compute the actual theta energies.
