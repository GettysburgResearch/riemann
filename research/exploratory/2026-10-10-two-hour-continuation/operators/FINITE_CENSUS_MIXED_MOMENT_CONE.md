# A complete finite census gives an infinite mixed-moment cone

Status: complete actual-source analytic theorem, with exact rational guards.
At the fixed physical shift t=512, EVERY complete Hausdorff mixed difference
D_(n,j) is strictly positive when n,j are nonnegative integers and

                         40*n >= 61*j + 120.

The whole unknown real and complex tail is included. No additional native
moment, heat integral or root computation is performed. This is an infinite
cone of mixed signs; the complementary pairs remain open, so it does not
establish the universal Hausdorff criterion or RH.

Imported source inputs: the independently accepted count-free complete real
head through R=5419; one actual real root gamma_* in (14,15); the complete
classical strip |Im rho|<=A=1/2; inverse-square summability; and the actual
theta/Jensen upper count N(x)<x*log(x)<=x^2 for x>=1024. The first two
inputs are the frozen sixteenth-moment census, not a historical zero count.
The direct source bindings and actual head contract are replayed by the
finite guard checker. Simplicity is unnecessary for this implication.

## MM1. Literal complete mixed coefficients

Represent every +/- pair by its positive-real member rho=gamma+i*beta,
retain both conjugate members separately, and use its positive integer
multiplicity m. Put c=t^2-A^2, and for n,j>=0 define

\[
 b_n=c^n\sum_\rho m_\rho(\rho^2+t^2)^{-n-1},\qquad
 D_{n,j}=\sum_{h=0}^j(-1)^h{j\choose h}b_{n+h}.
\]

The exact finite binomial identity gives

\[
 D_{n,j}=c^n\sum_\rho m_\rho
       \frac{(\rho^2+A^2)^j}{(\rho^2+t^2)^{n+j+1}}.                 \tag{MM1}
\]

These are the same complete mixed differences in the independently reviewed
Hausdorff and Laguerre heat identities. For every fixed n,j the series is
absolutely convergent: outside a finite head its summands are
O(m/|rho|^(2n+2)). No selected-root removal is made here.

## MM2. Entire tail and endpoint accounting

Assume generally t^2>=3*A^2, so c>=2*A^2. For gamma>R,

\[
 |\rho^2+A^2|\le|\rho|^2+A^2\le\gamma^2+2A^2,
 \quad |\rho^2+t^2|\ge\Re(\rho^2+t^2)\ge\gamma^2+c.
\]

Thus |(rho^2+A^2)/(rho^2+t^2)|<=1, and the absolute tail in
MM1 after removing its positive factor c^n is at most

\[
 T_n=\sum_{\gamma>R}m_\rho(\gamma^2+c)^{-n-1}.                  \tag{MM2}
\]

For n>=1, closed-head Stieltjes summation, with Q=R^2+c, gives

\[
 \begin{split}
 T_n&=-N(R)Q^{-n-1}
       +2(n+1)\int_R^\infty\frac{xN(x)}{(x^2+c)^{n+2}}\,dx\\
 &\le2(n+1)\int_R^\infty\frac{x^3}{(x^2+c)^{n+2}}\,dx\\
 &=\frac{n+1}{n}Q^{-n}-cQ^{-n-1}<2Q^{-n}.                     \tag{MM3}
 \end{split}
\]

The count N includes every real and off-real positive-real occurrence and
its multiplicity. The negative endpoint pays any atom at the cutoff;
all zeros at or below R belong to the complete real head. Its upper
endpoint vanishes by N(x)<=x^2. The integral and inequality are valid for
every integer n>=1, including the entire infinite tail. Dropping only the
nonpositive endpoint is safe.

## MM3. A complete real head dominates the unknown tail

All head terms in MM1 are nonnegative. The known gamma_* in (l,b)=(14,15)
supplies at least one positive occurrence. Define a=l^2+A^2 and B=b^2+t^2.
Its contribution after c^n is strictly greater than

\[
                         a^j B^{-n-j-1}>0.                     \tag{MM4}
\]

Conjugate pairing makes the complete D_(n,j) real, and MM3 bounds the
absolute contribution of the whole remaining source. Consequently every
pair satisfying

\[
        2B\left(\frac BQ\right)^n\left(\frac Ba\right)^j<1     \tag{MM5}
\]

has D_(n,j)>0. This exact sufficient criterion is useful independently
of the particular simpler cone below. It does not assume a real tail.

For actual Xi at t=512,R=5419,A=1/2,

\[
 a=785/4,\quad B=262369,\quad Q=118510819/4,
 \quad r=B/Q,\quad s=B/a.
\]

The checker verifies literal rational inequalities

\[
 0<r<1,\quad 2Br^3<1,\quad r^{61}s^{40}<1,
 \quad r^{\lceil61h/40\rceil}s^h\le1\ (0\le h<40).            \tag{MM6}
\]

Write j=40q+h,0<=h<40. If40n>=61j+120, then
n>=61q+ceil(61h/40)+3, hence

\[
 2Br^n s^j\le(2Br^3)(r^{61}s^{40})^q
                    r^{\lceil61h/40\rceil}s^h<1.              \tag{MM7}
\]

This proves the stated infinite cone without enumerating n,j. The three
principal bounds have approximate values r=.0088555,2Br^3=.3644064 and
r^61*s^40=.6671130; acceptance uses exact fractions, not these decimals.

## MM4. What this mechanism adds and leaves open

The finite native moment table covers a bounded triangle of mixed tests.
MM7 adds unbounded mixed degrees, with a whole-source tail theorem rather
than a new high-order jet. For example it proves all D_(2j+3,j)>0,
and the sharper displayed rational cone, for arbitrarily large j.
Its input is the complete finite real head, not scalar moment positivity.
The comparison shows why a dominant real spectral atom can enforce many
mixed signs while off-real atoms may still remain in the tail.

The universal criterion requires every pair n,j>=0. In particular, this
argument covers no unbounded family with n fixed and j->infinity. The
constructive finite negative-witness theorem remains compatible: any
hypothetical off-real occurrence must eventually violate a mixed test
outside this cone. No cofinal census, all-order actual Hankel positivity,
complete monotonicity of the heat trace, or RH is inferred.
