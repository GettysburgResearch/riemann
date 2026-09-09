# TPR26: the exact theta remainder is positive-real on a growing strip

Date: 2026-09-09. Proposed component proofs; independent review required.
The global complex Laguerre inequality for Xi and RH remain UNPROVED.
Parent: PR #835, 815ccae329a17327b873d21f05bc30c24db13e7e.
No earlier manuscript, source, or numerical receipt is modified.

This continuation attacks the omitted modular contribution itself. It proves
an all-frequency sign and a relative, not merely absolute, estimate for that
EXACT contribution. Its use as a positive-real function does not assert that
adding it to another function preserves real zeros. Classical convex-cosine,
Schwarz-Pick, Watson/Laplace, and Rouche arguments are proved at the needed
scope or credited below; no priority or independent-acceptance claim is made.

## 1. The unmodified source and the statements

Use the parent's analytic normalization

    F(z)=xi(1/2+iz)=2 integral_0^infinity Phi(u) cos(zu) du,
    Phi(u)=sum_(n>=1) phi_n(u),
    phi_n(u)=exp(u/2) (4Q^2-6Q) exp(-Q), Q=pi n^2 exp(2u).

The complete modular sum is even. Each phi_n is used only on u>=0 here.
For every integer N>=1 set

    F_N(z)=2 integral_0^infinity sum_(n<=N) phi_n(u) cos(zu) du,
    T_N(z)=F(z)-F_N(z),  n0=N+1,  q=pi n0^2>12.             (1)

All these transforms are entire. Local uniform convergence and all fixed
transform derivatives follow from the double-exponential tail, uniformly on
compact z sets. T_N is the COMPLETE sum n>N, not just its first term.

**TPR1 (growing positive-real strip).** For every N>=1,

    Re T_N(x+iy)>0 for ALL real x and |y|<=q.                (2)

In particular T_N is zero-free there. At real x,

    F_N(x)<F_(N+1)(x)<F(x).                                (3)

Each individual increment F_n-F_(n-1), n>=2, has positive real part
throughout |Im z|<=pi n^2. This is NOT a real-rootedness theorem for F_N.

**TPR2 (complete, all-height relative bounds).** Uniformly for ALL real x
and |y|<=1/2,

 q^3 exp(-q)/[18(4q^2+x^2)] <= Re T_N(x+iy)
       <= |T_N(x+iy)| <=256 q^3 exp(-q)/(4q^2+x^2).          (4)

Also, with the explicitly zero-free rational reference

    L_q(z)=16q^3 exp(-q)/(4q^2+z^2),

    |T_N(z)/L_q(z)-1| <=256/q,  |Im z|<=1/2.              (5)

For q<=256 the last error bound is deliberately larger than one; it must not
be used as a strict relative approximation there. The positive-real theorem
(2) has no such large-N restriction. Equations (4)-(5) retain unbounded real
frequency, every omitted theta index, and the original normalization.

**TPR3 (uniform truncation horizon).** There is an absolute C such that all
zeros of F_N in |Im z|<=1/2 satisfy

    |Re z| <=4(N+1)^2+(16/pi)log(N+1)+C.                    (6)

Outside a bound of this form Re F_N(z)<0. C is not numerically instantiated.
This is an upper limit on the band region described by the CHANGED finite
transform, not a zero-free theorem for Xi, nor a localization theorem for the
first spurious zero. It exhibits the square-root theta-index scale inherent
in raw approximation at growing frequency.

**TPR4 (a source-level resolution of the parent's false candidate).** Let
z_c be the exact Gaussian rational in the authenticated parent receipt. On
D={z:|z-z_c|<10^-35}, F_3 has exactly one zero, counted with multiplicity,
whereas

    Re F(z)>7*10^-32 on the WHOLE disk D.                   (7)

The parent certificate is independently rerun as an implementation execution,
not reimplemented: its interval backend is the same pinned source. The new
Xi statement uses (4), elementary rational inequalities, and a global first-
derivative bound, NOT a numerical zeta oracle. It is one tiny actual-source
zero-free disk, not an extended zeta zero census.

## 2. Convexity after every permitted imaginary tilt

The derivative polynomials are

 P0(Q)=4Q^2-6Q,
 P1(Q)=-8Q^3+30Q^2-15Q,
 P2(Q)=16Q^4-112Q^3+165Q^2-(75/2)Q.                        (8)

Indeed phi_n^(r)(u)=exp(u/2-Q) P_r(Q), and

    P_(r+1)=2Q P_r'+(1/2-2Q)P_r.

For Q>=12, P0>0, P1<0, and

    -(P1+QP0)=Q(4Q^2-24Q+15)>0.

Thus R_Q(b)=P2+2bP1+b^2P0 is decreasing for 0<=b<=Q. At b=Q,

 R_Q(Q)=(Q/2)(2Q-5)(4Q^2-48Q+15)>0.                      (9)

The last factor is 4Q(Q-12)+15. All inequalities are exact polynomial facts.

For g(u)=phi_n(u)cosh(yu), put b=|y|. Whenever b<=pi n^2<=Q,

 g''(u)=exp(u/2-Q)cosh(bu)[P2+2bP1 tanh(bu)+b^2P0]
       >=exp(u/2-Q)cosh(bu)R_Q(b)>0.                     (10)

The sign in this estimate matters: P1 is NEGATIVE, and tanh(bu)<=1.
All g and their derivatives vanish rapidly at infinity. Twice integrating
by parts gives, for real x!=0,

 integral_0^infinity g(u)cos(xu)du
        =x^-2 integral_0^infinity g''(u)[1-cos(xu)]du>0.   (11)

We used integral g''=-g'(0), with the endpoint at zero retained. Strictness
follows because g''>0 and 1-cos(xu) is positive on a set of positive measure.
At x=0, the original positive integral gives strictness. Therefore each
summand's transform has positive real part in its stated strip. Normal
convergence permits summing all n>N and proves (2)-(3).

This is the elementary convex-cosine positivity mechanism. It is much more
specific than saying that a positive kernel has a positive Fourier transform:
(10), not positivity alone, provides the extra hypothesis.

## 3. A lower bound that includes arbitrarily high frequency

Here restrict |y|<=1/2. Monotonicity of R_Q(b) gives

 R_Q(b)>=R_Q(1/2)=16Q^4-120Q^3+196Q^2-54Q >=4Q^4,
                                                        Q>=12. (12)

For the FIRST omitted theta term take 0<=u<=h=1/(2q).
Then q<=Q=q exp(2u)<=q+2, since exp(1/q)<=1+2/q for q>=12.
Using e<3 in (10)-(12) yields

    [phi_(N+1)(u)cosh(yu)]'' >=(4/9)q^4 exp(-q).           (13)

For every real t, with sinc(0)=1,

    1-sinc(t) >= t^2/[8(1+t^2)].                          (14)

For |t|<=2 the alternating sine remainder gives
1-sinc(t)>=t^2/6-t^4/120 >=2t^2/15; for |t|>=2 use
sinc(t)<=1/|t|<=1/2. This proves (14) over the entire line.

Apply (11) to the full tail, retaining just the positive interval (13):

 Re T_N(x+iy)
   >=(8/9)q^4 exp(-q) x^-2 h[1-sinc(xh)]
   >=q^3 exp(-q)/[18(4q^2+x^2)].                          (15)

At x=0 this follows by continuity. The other omitted theta terms are retained
as nonnegative contributions; they are not approximated by zero in an identity.
This proves the lower half of (4).

## 4. Upper bounds and a zero-free normalization

Write a_N=-sum_(n>N)phi_n'(0)>0. For n>=2, consecutive terms q_n^j exp(-q_n),
q_n=pi n^2, j<=3, have ratio less than 1/2: bound the polynomial ratio by
(3/2)^6 and use pi>3, e>2. Hence

    a_N<=16q^3 exp(-q).                                  (16)

The substitution v=exp(2u), with v^(5/4)<=exp[5(v-1)/4], gives

 2 integral_0^infinity phi_n(u)du
        <=4q_n^2 exp(-q_n)/(q_n-5/4).

The consecutive ratios for the latter majorant are also below 1/2. Therefore

    T_N(0)<=8q^2 exp(-q)/(q-5/4)<10q exp(-q).              (17)

At real x, positivity and |cos|<=1 give T_N(x)<=T_N(0). Equation (11),
1-cos<=2, and (16) also give T_N(x)<=64q^3 exp(-q)/x^2. Splitting at |x|=2q
combines the bounds into

    0<T_N(x)<=128q^3 exp(-q)/(4q^2+x^2).                  (18)

For clarity, the needed elementary strip Schwarz lemma is as follows. If H
is holomorphic with Re H>0 on |Im z|<a, and H(x)>0 at real x, then

 |(H(x+iy)-H(x))/(H(x+iy)+H(x))|
                       <=tan(pi|y|/(4a)).                (19)

Compose the disk maps tanh(pi(z-x)/(4a)) and (H-H(x))/(H+H(x)), and use
Schwarz's lemma. For a=q>12 and |y|<=1/2, the right side is below 1/3;
therefore |H(x+iy)|<2H(x). With H=T_N, (18) proves (4).

These maps concern the EXACT tail, whose positive-real property was proved
without RH. They do not assert raw Xi innerness. Standard strip Schwarz-Pick
also gives |T_N'/T_N|<=4/q on the critical band. On the disk of radius q/4
about any such point the same crude bound holds, since its imaginary part
has magnitude at most q/2. Cauchy's estimate thus gives

 |(log T_N)''|<=16/q^2,   |T_N''/T_N|<=32/q^2.             (20)

All logarithms here are the unique branch with imaginary part in (-pi/2,pi/2).
The hyperbolic derivative bound used on |Im z|<=q/2 is
|H'|/Re H <=pi/[2q cos(pi Im z/(2q))]<4/q.

## 5. An all-frequency relative Laplace expansion

This section proves (5) with an explicit constant, including frequencies
arbitrarily larger than q. A fixed-frequency Watson expansion alone would
not suffice.

For n0=N+1 and v=2qu, put

 A_q(v)=phi_n0(v/(2q))/(4q^2 exp(-q)).

For r=0,1,2 its r-th v derivative is exp[-q(exp(v/q)-1)] times, respectively,

 r=0: exp(9v/(4q)) -(3/(2q))exp(5v/(4q));
 r=1: -exp(13v/(4q)) +(15/(4q))exp(9v/(4q))
                                      -(15/(8q^2))exp(5v/(4q));
 r=2: exp(17v/(4q)) -(7/q)exp(13v/(4q))
       +(165/(16q^2))exp(9v/(4q)) -(75/(32q^3))exp(5v/(4q)). (21)

Let E_q=A_q-exp(-v). For all v>=0, q>=12, and r=0,1,2,

    |E_q^(r)(v)| <= q^-1(8+5v+v^2)exp(-v/2).              (22)

To check this bound explicitly set R=q(exp(v/q)-1)-v. Then
0<=R<=v^2 exp(v/q)/(2q). For each leading term in (21), with c<=17/4,

 |exp(cv/q)exp(-R)-1|
            <=exp(cv/q)[cv/q+R].

After multiplying by exp(-v), the result is at most
q^-1[(17/4)v+v^2/2]exp(-v/2), since (c+1)/q<=7/16.
The sum of the absolute coefficients of the lower terms is at most 8/q;
for r=2 use 7+165/(16*12)+75/(32*12^2)<8. Their exponential factors leave
at least exp(-v/2). The r=0,1 bounds are smaller. This proves (22).
Also |E_q'(0)|<4/q directly from (21).

Put w=z/(2q). On the critical band |Im w|<=1/(4q)<=1/48. Therefore

 integral_0^infinity |E_q^(r)(v)|cosh(Im(w)v)dv <=123/q,

using exp(-v/2)cosh(v/48)<=exp(-v/3) and the exact moments
integral(8+5v+v^2)exp(-v/3)dv=24+45+54=123.
Writing I_q(w)=integral A_q(v)cos(wv)dv gives

 |I_q(w)-1/(1+w^2)| <=123/q;
 |I_q(w)-1/(1+w^2)| <=127/(q|w|^2), w!=0.                 (23)

The second bound follows by two integrations by parts, retaining E_q'(0).
As |1+w^2|<=1+|w|^2, split |w|<=1 and |w|>=1 to obtain

    |(1+w^2)I_q(w)-1| <=254/q.                           (24)

The first omitted transform is exactly 4q exp(-q)I_q(w).
The rest is T_(N+1). Applying (4) with q'=pi(n0+1)^2 shows its modulus,
divided by |L_q(z)|, is at most

    17(q'/q)^3 exp[-(q'-q)].

This is less than 1/q for EVERY n0>=2. Indeed, q<4n0^2, q'-q>3(2n0+1),
e>2, and (q'/q)^3<=729/64 bound q times that expression by

    17*(729/64)*4n0^2/2^(6n0+3)<1.

The expression decreases with n0 and is already below one at n0=2.
Adding this remainder to (24) proves (5), with room in 256/q.

For orientation only, expansion of (21) to first order gives the normalized
correction

 integral exp(-v)[(9/4)v-(1/2)v^2-3/2]cos(wv)dv
                 =-(1+15w^4)/[4(1+w^2)^3].               (25)

This identity is exact rational algebra. We do NOT state an unproved numeric
second-order remainder constant. The certified all-frequency estimate is (5).

## 6. A uniform upper horizon for band zeros of the raw truncation

The only external analytic inputs to this section are the classical
Euler-Maclaurin representation of zeta and Stirling's gamma estimate (DLMF
25.2(iii), 5.11). They give an absolute C0 with

    |F(x+iy)| <=C0(1+|x|)^3 exp(-pi|x|/4), |y|<=1/2.     (26)

For completeness, take s=1/2-y+ix, 0<=Re s<=1 and |x|>=1. Euler-Maclaurin
with one Bernoulli correction and cutoff ceil(|x|)+1 bounds zeta(s) by C|x|
uniformly in this strip: its integral remainder is bounded by
C|s(s+1)| N^(-Re s-1)/(Re s+1), and its finite sum by N. Stirling gives
|Gamma(s/2)|<=C|x|^(Re s/2-1/2)exp(-pi|x|/4). The polynomial prefactor
s(s-1) proves (26); bounded |x| is covered by continuity of the ENTIRE xi.

If F_N(x+iy)=0, then F=T_N there. Comparing (4) and (26) gives

 pi|x|/4 <=q+3log(1+|x|)+log(4q^2+x^2)-3log q+O(1).      (27)

First, in the case |x|>=q, a fixed inequality 5log(1+t)<=t/8+C shows
|x|=O(q). Substitute this back into (27) to get

    |x| <=(4/pi)q+(8/pi)log q+O(1).

When |x|<q the same bound holds after enlarging the constant. This is (6).
The very same comparison makes |F|<Re T_N outside such a bound, whence
Re F_N<0 there. No value of C0 or C has been certified here. This concerns
raw truncations; it does not exclude any actual Xi zero at large height.

## 7. The old false candidate is now excluded for the COMPLETE source

The parent's exact Gaussian-rational center is

 x_c=67.8801896551476196444591034890974615868760577967044779253851906685118397,
 y_c=0.4773438417708229856896978584442346997998462219509442426117227298339156.

Its source-pinned 384-bit integral replay proves

 |F_3(z_c)|<2*10^-57, |F_3'(z_c)|>17*10^-21,
 sup_(|Im z|<=1/2)|F_3''(z)|<1000.

On the smaller radius r=10^-35,

    2*10^-57+500r^2 <17*10^-21 r,

so the same Rouche argument gives exactly one F_3 zero in that disk.
For the full source, q=16pi satisfies 48<q<64. Since |x|<68 throughout
the disk, (4) and e<3 give

 Re T_3(z) > 48^3/[18(4*64^2+68^2)3^64] >8*10^-32.       (28)

A coarse GLOBAL first-derivative estimate is sufficient here. For |Im z|<=1/2,

 |F_3'(z)| <=8pi^2 sum_(n=1)^3 n^4 exp(-pi n^2)/(2pi n^2-5)^2
             <128 sum_(n=1)^3 n^4/(6n^2-5)^2 <1000.       (29)

The inequality exp(2u)>=1+2u and integral u exp(-au)du=1/a^2 prove it.
Along each segment from z_c to the disk, (29) therefore gives

 |F_3(z)|<2*10^-57+1000r.

Combining with (28) proves Re F(z)>7*10^-32 throughout the disk. This is a
strict all-points disk certificate for the unmodified Xi. It uses no sampled
zero set and no numerical gamma/zeta evaluation. It is not a major zero-free
range; it resolves the interpretation of one changed-source root.

## 8. Direct return to the full Laguerre sign: what is STILL missing

The global target remains

 L_F(z)=|F'(z)|^2-Re(F''(z)conjugate(F(z))) >=0,
                                           |Im z|<=1/2. (G)

As in the parent (classical complex Laguerre), this would prove RH by vertical
convexity of |F|^2 and conjugation of any hypothetical nonreal zero.

Since T_N has no zeros on the band, Q_N=F/T_N is an admissible exact
normalization, with precisely the same zeros and multiplicities. Put
 a=T_N'/T_N, b=T_N''/T_N. Direct differentiation gives

 L_F/|T_N|^2=L_(Q_N)+(|a|^2-Re b)|Q_N|^2
                        +4 Im(a) Im(Q_N' conjugate(Q_N)). (30)

Equation (20) bounds the difference from L_(Q_N) by

    (48/q^2)|Q_N|^2+(16/q)|Q_N'||Q_N|.                   (31)

This is a proved normalization error bound, NOT a proof of the sign of
L_(Q_N). Q_N=1+F_N/T_N retains the delicate cancellation in its numerator.
At large real frequency F_N/T_N tends to -1, so a small relative approximation
of T_N alone need not give a small relative approximation of Q_N or F.

Neither Re T_N>0 nor its Schwarz-Pick bounds control the mixed term in (30)
with the necessary sign. For the simpler normalization F=U+T, the exact
Laguerre expansion is

 L_F=L_U+L_T+2Re[U' conjugate(T')]
                      -Re[U'' conjugate(T)+T'' conjugate(U)]. (32)

The mixed term remains. This pass does not prove it nonnegative or bounded
by the other terms for the actual modular source. Equations (30)-(32) are
the specific point where the attempted full proof remains unfinished.
The global bound (5) cannot bridge this by fixing N: its residual is still
algebraic in x while the entire Xi envelope in (26) is exponentially small.

The contribution is a global positive-real theorem and a complete relative
control of the EXACT modular remainder, not a completed RH proof or a claim
that the unknown Laguerre sign has become routine.
