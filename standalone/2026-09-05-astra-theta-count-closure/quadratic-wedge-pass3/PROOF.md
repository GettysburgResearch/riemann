# A quadratic mixed-difference wedge from phase cancellation and local zero counts

Status: PROPOSED PROVED THEOREM; independent mathematical review required.
The unrestricted mixed inequality and RH remain UNPROVED.
Scope: the actual invariant xi function; one fixed scale v=1; all integers
 a>=0 and b>=10^8(a+1)^2. This is an infinite uniform region, not a finite scan.
Parent: PR #790, mixed-differences-pass2, at
 11f20a995d740347177bb39e378cf5261d25132b.
Original heat packet: bc3c35d8f434949748a2185783bf831d3afd9126.
Inputs: the parent's exact invariant-zero identity, V100 and Jensen count;
 the classical Rosser argument bound and the elementary Riemann--von Mangoldt
 remainder specified below. No sharp modern S(T) constant is used.
What was run: bounded exact rational algebra and constant checks in verify.py;
 these checks do not constitute a machine proof of the infinite argument.
Smallest remaining gap: source-specific control in the intermediate region,
 equivalently the full Laguerre-trace subexponential bound of pass2.
No external novelty or priority claim is made.

## 1. Statement

Use the same single-valued invariant entire function

    X(u)=xi(1/2+sqrt(u+1/4)),  h=X'/X,  X(0)=1/2.

Let rho=beta+i gamma run over ALL nontrivial zeros with gamma>0, including
multiplicity, and put A=rho(1-rho). An off-line quartet contributes two
conjugate invariant parameters. The parent proves the normally convergent
identity

    H_(a,b)(1) = sum_A A^b/(1+A)^(a+b+1).                     (1.1)

This is the same mixed Hausdorff difference as in the first two packets;
no new source or normalization is substituted. Every sum in this note is
real after conjugation, but individual terms need not be positive.

**Theorem ASTRA-QW-01.** Put n=a+1. For every integer n>=1 and integer
b>=10^8 n^2, set r=b/n and

    f_r(w)=w^b/(1+w)^(n+b),      w>0.

Then

    H_(a,b)(1) > (1/8) f_r(r) > 0.                           (1.2)

The constant 10^8 is deliberately conservative and is not claimed optimal.
The improvement over pass2 is quadratic rather than cubic index growth.
For n<12500 the earlier cubic threshold can still be smaller numerically;
use the UNION of the two regions, not a blanket replacement of constants.

We prove (1.2) by a positive block near gamma=sqrt(r), exact cancellation
of the linear phase at that block, and separate low/middle/high tail bounds.
The zeros in the positive block need NOT be on the critical line.

## 2. Exactly which classical count information is used

Let N(T) count zeros with 0<gamma<=T, with multiplicity. At ordinates that
are themselves zeros, use one-sided limits as specified below. The parent
proves

    N(T)<=T^2 for T>=100,
    N(T)=O(T log(T+2)),                                      (2.1)

by Jensen's formula, and imports V100: all zeros with 0<gamma<=100 lie on
the line. These are retained unchanged. No larger RH verification is used.

We additionally import the classical Rosser (1941) bound for the argument
S_arg(T), NOT the heat S(t):

    |S_arg(T)| <= .137 log T+.443 log log T+1.588, T>=1467.    (2.2)

Source: Rosser, Explicit bounds for some functions of prime numbers,
American Journal of Mathematics 63 (1941), 211--232, DOI 10.2307/2371291.
We read the reproduction of (2.2) in Table 1, page 1 of Trudgian,
arXiv:1208.5846v2; the original 1941 proof is imported, not independently
reproved here. The same v2 paper, page 3, equation (2.5), gives the elementary
completion remainder

    |N(T)-F(T)| <= |S_arg(T)|+.2/T,
    F(T)=T/(2pi) log(T/(2pi e))+7/8,        T>=1.              (2.3)

Both source pages were rendered and visually inspected in this pass.
We use neither that paper's sharper Theorem 1 nor its sharp Corollary 1.
This separates this theorem's dependency from pass2's sharper count import.
The original paper PDF bytes were not downloaded or hashed in this runtime.

Equations (2.2)--(2.3) imply the much weaker statement

    |N(T)-F(T)| < log T,                 T>=1467.             (2.4)

For completeness the gap is
 .863 log T-.443 log log T-1.588-.2/T.
It is increasing for T>=1467. At T=1467 it is positive using
 log1467>4, loglog1467<3, and .2/1467<.001: the remaining rational gap is
 .863*4-.443*3-1.589=.534>0.
Here log1467>4 follows from e<3, while log1467<8 follows from e>8/3 and
 (8/3)^8>1467; then loglog1467<log8<3. Thus this weakening needs no
floating-point logarithm evaluation.

Two simple consequences of (2.4) will be useful.

**Lemma QW-01a (local upper and lower counts).** For T>=2000:

    #{gamma in [T,T+1]} < 3 log(T+1),                         (2.5)
    #{gamma in [T,T+40]} > (1/4) log T.                       (2.6)

Proof. For (2.5), the main increment is at most log(T+1), since
 F'(t)=(1/(2pi))log(t/(2pi))<log(T+1) on [T,T+1]. The two errors total
 less than 2log(T+1). For (2.6), use pi<4 and T>=2000>64:

    F(T+40)-F(T)>5 log(T/8)> (5/2)log T.

The errors total at most 2log(T+40), which is less than 2log T+.7 for
T>=100, since log(7/5)<7/20. Therefore the increment is greater than
 .5log T-.7>.25log T. For endpoint zeros, first apply the upper bound to
(T-epsilon,T+1+epsilon), and the lower bound to slightly interior endpoints;
then let epsilon decrease to zero. Every endpoint is counted at most once
and multiplicities remain present. The strict estimates have slack, so
closed-interval versions follow. QED.

No simplicity, minimum spacing, or local critical-line proportion is used.

## 3. Exact phase and modulus estimates

Write A=x+i y, w=|A|, with y>=0 by conjugation. The strip gives

    x>=gamma^2,   y^2<=x,   w<=gamma^2+1/2,
    0<=w-x=y^2/(w+x)<=1/2.                                  (3.1)

Let N=n+b=n(1+r). The modulus of one term obeys, for w>=10000,

    |A^b/(1+A)^N| <= f_r(w) exp(N/(1+w)^2).                   (3.2)

Indeed |1+A|^2=(1+w)^2-2(w-x)>=(1+w)^2-1. Apply
 -log(1-z)<=2z for 0<=z<=1/2 to z=1/(1+w)^2 and the power N/2.
The reverse simple bound |A^b/(1+A)^N|>=f_r(w) follows from
 |1+A|<=1+w.

The continuously lifted phase of the term, beginning at y=0, is

    phi = b arg A-N arg(1+A)
        = integral_0^y
          [x(x+1)(b-nx)-(b+n(x+1))s^2]
          /[(x^2+s^2)((x+1)^2+s^2)] ds.                     (3.3)

This is direct differentiation in the imaginary coordinate; it is NOT a
principal-argument assertion that loses winding. Taking absolute values
only after combining the two fractions gives

    |phi| <= n|r-x|/x^(3/2)
                 +(b+n(x+1))/(3x^(5/2)).                    (3.4)

Here y<=sqrt(x) was used. The factor r-x is crucial: the linear phase
cancels at the real saddle x=r. Bounding b arg A and N arg(1+A) separately
would lose the quadratic result.

The real envelope has its maximum at w=r, since

    d/dw log f_r(w) = n(r-w)/(w(1+w)).                        (3.5)

Set

    C=10^8,      eta=r/n=b/n^2>=C,      q=sqrt(r)>=10000.       (3.6)

## 4. The positive block

Take all zeros with q<=gamma<=q+40. By (3.1),

    r<=x<=w<=r+81sqrt(r).                                    (4.1)

The last inequality uses q>=10000. Integrating (3.5), with denominator
at least r^2 on this interval, gives

    log(f_r(r)/f_r(w)) <= n(w-r)^2/(2r^2)
                         <= (6561/2)n/r < 1/2.              (4.2)

Thus f_r(w)>f_r(r)/2. Equation (3.4), using (4.1), gives

    |phi| < 83n/r < 1/2.                                    (4.3)

In bounding its second term, use x<=2r and b=nr; the displayed constant
has ample slack for r>=10^8. Consequently each selected zero term has
real part greater than f_r(r)/4. By (2.6), the TOTAL positive contribution
of the block is

    P > (log r) f_r(r)/32.                                  (4.4)

In particular at least one such term exists and contributes >f_r(r)/4.
All other positive terms may be discarded. In what follows, only genuinely
negative real parts are charged to the error budgets.

## 5. The middle negative tail: preserve the canceled phase

Consider unverified zeros with r/2<=x<=2r. From (3.4),

    |phi| <= 3n|x-r|/r^(3/2)+8n/r^(3/2).                     (5.1)

The second constant follows by bounding x from below by r/2, above by 2r,
and using 2^(5/2)<6. In particular, if

    |x-r| <= r^(3/2)/(16n),                                  (5.2)

then |phi|<1/4, and the real part is positive. A negative middle term
therefore violates (5.2).

Put s=gamma-q. Since gamma<sqrt(2r)<(3/2)q and
 |x-r|<=|s|(gamma+q)+1/4, violation of (5.2) implies

    |s| > eta/80.                                           (5.3)

For example, subtract 1/4 from d=r^(3/2)/(16n), use d>=1 and
 gamma+q<(5/2)q; the resulting bound is at least eta/80.

On the middle range w lies in [r/2,3r]. Along the interval between r
and w, u(1+u)<=12r^2. Equation (3.5) gives

    log(f_r(r)/f_r(w)) >= n(w-r)^2/(24r^2).                   (5.4)

For a negative middle term, (5.3) also implies
 |w-r|>=|s|q-1/2>=|s|q/2.
The modulus boost in (3.2) is at most exp(8n/r)<2. Therefore

    |A^b/(1+A)^N| <= 2 f_r(r) exp(-s^2/(96eta)).              (5.5)

Partition the two sides of q into half-open unit intervals and retain only
those intersecting the middle range. Their lower endpoints exceed 2000
and their upper endpoints are below 2q+1<r. By (2.5), each contains fewer
than 3log r zeros, with multiplicity. For

    J=floor(eta/80)>=eta/160,

(5.3)--(5.5) thus bound the TOTAL negative middle contribution by

    12(log r) f_r(r) sum_(j>=J) exp(-j^2/(96eta)).             (5.6)

The numeric series is extended to infinity AFTER applying the local bound
to the intervals intersecting the middle range. We are not claiming that
3log r bounds the count in arbitrarily remote unit intervals.

Decreasing Gaussian tails give

    sum_(j>=J) exp(-j^2/(96eta))
      <=(1+48eta/J)exp(-J^2/(96eta))
      <8000 exp(-eta/2457600).                               (5.7)

Since eta>=10^8>40*2457600, e>2, and 128*96000<2^40, we obtain

    E_middle < (log r) f_r(r)/128.                           (5.8)

This bound is uniform in both unbounded indices. It does not assume that
individual nearby zeros are real, separated, or simple.

## 6. The low and high negative tails

### 6.1 Low: x<r/2 and gamma>100

Here 10000<=w<r/2+1/2<(3/5)r. Put

    g(w)=log f_r(w)+N/(1+w)^2.

Its derivative is positive in this range. After multiplying by the positive
factor w(1+w)^3/n, its numerator is

    (r-w)(1+w)^2-2(r+1)w
       >=(2r/5)w(w-10)>0.                                   (6.1)

Integrating (3.5) between (3/5)r and r gives a real-envelope loss at least
n/25: on that interval the denominator is at most 2r^2. At (3/5)r the
modulus boost is at most exp(6n/r)<2. Hence each low term has modulus at most
2 f_r(r)exp(-n/25). There are at most N(sqrt(r/2))<=r/2 such zeros, so

    E_low <= r f_r(r)exp(-n/25).                             (6.2)

All zeros with gamma<=100 were already positive by V100 and need no charge.

### 6.2 High: x>2r

For w>=2r, equation (3.5) yields

    d log f_r/d log w <=-n/3,
    f_r(2r)<=f_r(r)exp(-n/12).

The second bound follows by integrating with u(1+u)<=6r^2 on [r,2r].
Using (3.2) again, each high modulus is at most

    2 f_r(r)exp(-n/12) (w/(2r))^(-p),     p=n/3.              (6.3)

We use this bound only when n>12500, so p>2. Every high zero has
 gamma^2>2r-1/4>2r-1=B^2.
Since w>=gamma^2, Stieltjes integration using (2.1) gives

    sum_(gamma>B) (gamma^2/(2r))^(-p)
       <=[p/(p-1)] B^2(2r/B^2)^p < 8r.                       (6.4)

Indeed p/(p-1)<2, B^2<2r, and
 (2r/(2r-1))^p<=exp(p/(2r-1))<=exp(n/(3r))<2.
Consequently

    E_high < 16r f_r(r)exp(-n/12).                           (6.5)

## 7. Completing the uniform quadratic theorem

Two cases avoid any uncontrolled small-index exception.

### Case I: r>=8000n^2

Set T=b^(1/3)>=20n. Also T>100 because b>=10^8n^2. The phase estimate
from pass2 Section 4 (or integration of arguments as in (3.3)) shows
that every zero with gamma>=T has positive real part: its phase is
bounded by max(n/T,b/T^3)<=1. V100 pays gamma<=100.

For 100<gamma<T, direct algebra gives

    log(|1+A|/|A|)>.99/gamma^2.

This follows from log(1+z)>=z/(1+z), (3.1), and
 (1+3/20000)^2<100/99. The function
 gamma^(-2n)exp(-.99b/gamma^2) increases up to T because .99T>=n.
Using N(T)<=T^2, all possible negative terms total at most

    E <= T^(2-2n)exp(-.99T).                                 (7.1)

This short argument is reproduced here; it does NOT import pass2's
additional dyadic-zero-existence premise.

On the other hand,

    f_r(r)=r^(-n)(1+1/r)^(-n(1+r))>=r^(-n)exp(-2n).

Therefore

    E/f_r(r)<=T^2(T/n)^n exp(2n-.99T)
             <=400n^2(20 exp(-17.8))^n
             <400n^2(20/2^17)^n<=125/2048<1/16.              (7.2)

The first expression decreases for T>=20n. The last estimate uses
 n^2<=4^(n-1) for all integers n>=1, proved by induction. At least one
zero in the positive block contributes >f_r(r)/4 by Section 4. Subtracting
(7.2) proves H>f_r(r)/8 in Case I.

### Case II: r<8000n^2

Since r>=10^8n, this case requires n>12500. Thus all three tail bounds
in Sections 5--6 apply. Their far part satisfies

    (E_low+E_high)/f_r(r)
       <17r exp(-n/25)
       <136000n^2 exp(-n/25)
       <136000*12500^2*2^(-500)<1/128.                        (7.3)

The function n^2exp(-n/25) decreases for n>=12500, and the last bound is
an exact integer comparison. As log r>1, equations (5.8) and (7.3) make
the full negative contribution less than (log r)f_r(r)/64. Subtracting
from (4.4) gives

    H>(log r)f_r(r)/64>f_r(r)/8,

because r>=10^8 and log r>8 (e<3 and 3^8<10^8). This proves Case II
and completes Theorem ASTRA-QW-01. QED.

## 8. What this does and does not close

Combine this theorem with the UNCHANGED pass2 results. At v=1, H>0 in

    a<=19, every b>=0;
    a>=2, b<=100a;
    b>=max(10^6,8000(a+1)^3);
    b>=10^8(a+1)^2.

The pass2 phase rectangle gives additional cells. Its every-scale theorem
also proves all a>=0, 0<=b<=22, v>0. These are proved infinite regions,
subject to their explicit imported classical inputs and independent review.

They do not cover all (a,b). A possible negative cell at v=1 must still
lie, at least, in the infinite set

    a>=20,
    100a<b<min(max(10^6,8000(a+1)^3),10^8(a+1)^2).             (8.1)

A different bound on constants does not remove this infinite region.
The quadratic theorem uses only strip geometry, V100, and count information;
it does not yet exploit enough literal theta/Euler arithmetic to exclude
an individually resolved off-line pair in that region.

The exact row-variation identity from pass2 remains the end-to-end test:

    limsup_N [sum_(a=0)^N binom(N,a)|H_(a,N-a)(v)|]^(1/N)
         = sup_A (v+|A|)/|v+A|.

Thus subexponential source-side control of the complete rows would prove
ALL mixed inequalities and RH. That source estimate is not established by
this note. The quadratic envelope neither assumes nor proves it.

## 9. Attempt ledger and review targets

The advance came from combining the two phase fractions BEFORE estimating,
then using a local count rather than a single distant zero. The earlier
crude phase cutoff was at b^(1/3). The canceled phase now places all possible
negative middle terms at distance at least eta/80 from the saddle ordinate,
while the envelope is Gaussian with width proportional to sqrt(eta).
Local positive mass and local negative mass both carry a log r factor;
retaining that factor on both sides makes the threshold uniform in n.

The attempt to finish RH by iterating these estimates stops at eta=r/n
not being large. There the argument does not give a source-positive block
large enough to defeat every allowed phase. It would be incorrect to
extrapolate (1.2), use a changing v to evade the fixed-scale criterion, or
replace the unknown signed central sum by its absolute value.

Priority review: phase numerator and its continuous argument; local count
endpoints/multiplicity; positive-block constants; extending only the NUMERIC
Gaussian majorant to infinity; low-modulus monotonicity; high-tail exponent
p=n/3; the two-case boundary n=12500; and the explicit distinction between
this theorem's Rosser input and pass2's sharper imported bound.
