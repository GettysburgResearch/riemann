# Exact weighted label moments and a polynomial proof of the whole tail

Status: **Root-reviewed analytic and algorithmic component lemmas.** The final threshold
certificate is separate. Literal source labels, including both labels
at 67, are retained. No critical-power or RH claim is made here.

## 1. Exact finite weighted cumulative moments

For a labelled k-subset A, write n_A for its integer product. For any real
a and finite integer t, define

\[
 C_{k,j}(a,t)=\sum_{\substack{|A|=k\ n_A\le t}}n_A^{-a+j/2},
       \qquad 0\le j\le6.
 \tag{W1}
\]

These are finite positive sums, so no convergence condition on a-j/2
is needed. For k>=2 and t<=N, every participating label is at most N/2.
Thus a complete ordinary-prime sieve through floor(N/2), plus the extra
67 label, suffices for every selected level through four. For k=1 this
label set is complete only through B=floor(N/2), a restriction enforced
explicitly by `weighted_moments.py`.

That module sorts the labels and builds all seven directed cumulative
prime-weight sums. It recursively chooses the first k-1 label indices,
then sums the last index in one prefix subtraction. If the current
partial product is n and its last index is i, the allowed final indices
are i+1 through the last label <=floor(t/n). The prefix difference is
multiplied by n^(-a+j/2), separately for every j. Strictly increasing
indices enumerate each labelled subset exactly once, while equal-valued
67 indices remain distinct. Integer quotient floors are exact.

The recursion prunes only when the product of the smallest available
remaining labels exceeds the quotient. Sorting makes every later choice
larger, so this loses no active subset. This proves that each output is
exactly (W1), enclosed by directed operations. The moment-vector metadata
records a, t and k and is checked against the kernel exponent and active
cutoff by every normalization routine.

## 2. Positive-tail binomial bounds

Fix 1<m<2. For 0<=v<=3/4, the uniformly convergent binomial expansion is

\[
 (1-v)^m=1-mv+\sum_{j\ge2}b_j(m)v^j,
 \quad b_2=\frac{m(m-1)}2>0,
 \quad b_{j+1}=b_j\frac{j-m}{j+1}>0.
 \tag{W2}
\]

Every b_j for j>=2 is positive and decreases with j. Define

\[
 p_m(v)=1-mv+\sum_{j=2}^5 b_jv^j,
 \qquad q_m(v)=p_m(v)+4b_6v^6.
 \tag{W3}
\]

The omitted tail is bounded by
\(\sum_{j\ge6}b_jv^j\le b_6v^6/(1-v)\le4b_6v^6\), so
\(p_m(v)\le(1-v)^m\le q_m(v)\). Moreover p_m is decreasing on this
interval: its derivative is the exact negative kernel derivative minus
the positive derivative of its omitted tail. Thus an exact rational guard
p_m(3/4)>0 proves that both bounding polynomials are positive throughout
the activation domain. This guard is required at every fixed power used
by the certificate.

Put z=x^-1/2 and d_m(z)=(1-3z/4)^m. From (W1), selected products n<=t<=x
have normalized positive level bounds

\[
 \frac{P_{k,m,t}(z)}{d_m(z)}
 \le\sum_{\substack{|A|=k\n_A\le t}}r_{n_A}(m,x)
 \le\frac{Q_{k,m,t}(z)}{d_m(z)},
 \tag{W4}
\]

where P has coefficient
\(b_j(m)(3/4)^j C_{k,j}((m+1)/2,t)\) for j=0,...,5, with
b0=1,b1=-m, and Q adds the j=6 coefficient
\(4b_6(m)(3/4)^6 C_{k,6}\). All polynomial coefficient enclosures
use exact rational binomial factors and directed Arb moment values.

For an odd level, omitted products have r_n(m,x)<=n^(-(m+1)/2).
Therefore their total normalized mass is bounded by the complete Euler
elementary sum minus C_(k,0)(a,t). At k=1 the complete sum is W1(a);
at k=3 it is e3(a), given by (F4)--(F5). If t=x and the finite source
is complete through x, every omitted product is inactive and its bound
is zero. Even omitted levels are simply discarded in a lower bound.
This prices only finite kernel defects and the explicitly declared
remaining positive Euler mass; it does not assume cancellation in an
unsigned infinite tail.

## 3. One polynomial for the entire unbounded endpoint interval

Take 1<m0<=m1<2 and N>=4, with B=floor(N/2). At m0 retain the complete
selected level one through B and level three through N. At m1 retain
levels two and four through N. Let exact directed upper endpoints obey

\[
 T_1\ge W_1((m_0+1)/2)-C_{1,0}((m_0+1)/2,B),\quad
 T_3\ge e_3((m_0+1)/2)-C_{3,0}((m_0+1)/2,N),
\]
\[
 V\ge W_1((m_0+1)/2),\quad V<5,\qquad
 c_0=1-T_1-T_3>0,\quad c_4=1-V/5>0.
 \tag{W5}
\]

All these domains and signs are explicit finite guards. For every x>=N
and m in [m0,m1], the normalized odd upper bounds are
\(T_1+Q_1(z)/d_{m_0}(z)\) and
\(T_3+Q_3(z)/d_{m_0}(z)\), while the even lower bounds are
\(P_2(z)/d_{m_1}(z)\) and \(P_4(z)/d_{m_1}(z)\).
This follows from (W4) and the monotonicity of each normalized subset
term in endpoint and power. The global removal majorant V absorbs M5
by V M4/5 and pairs all later levels, exactly as in (F1). Consequently

\[
 \frac{H_m(x)}{T(x)^m}\ge
 c_0-\frac{Q_1(z)+Q_3(z)}{d_{m_0}(z)}
                +\frac{P_2(z)+c_4P_4(z)}{d_{m_1}(z)}.
 \tag{W6}
\]

Every selected kernel is positive by the guard after (W3). Multiplying
by the positive d_(m0)d_(m1), let D_i^- and D_i^+ be the lower and upper
polynomial enclosures (W3) for d_(mi)(z), obtained by substituting v=3z/4.
Then the resulting numerator is bounded below by the collected polynomial

\[
 \mathcal P(z)=c_0D_0^-(z)D_1^-(z)
      -[Q_1(z)+Q_3(z)]D_1^+(z)
      +[P_2(z)+c_4P_4(z)]D_0^-(z).
 \tag{W7}
\]

All directions are justified by positivity: the first and third terms
use lower denominator bounds, while the negative second term uses an
upper denominator bound. The polynomial has degree at most twelve.
Thus strict positivity of P on the entire interval
\(0\le z\le N^{-1/2}\) proves the whole tail x>=N, uniformly over
the real power slab. Its constant coefficient is a genuine infinite-limit
margin; z=0 is included in the finite proof of polynomial positivity.

## 4. Directed Bernstein positivity, with exact subdivision

For a polynomial p(z)=sum_(j=0)^d a_j z^j and an exact dyadic interval
[L,U], set z=L+(U-L)t. Its transformed power coefficients are

\[
 \widetilde a_k=(U-L)^k\sum_{j=k}^d a_j\binom jk L^{j-k}.
\]

The Bernstein coefficients on 0<=t<=1 are

\[
 B_i=\sum_{k=0}^i\widetilde a_k\frac{\binom ik}{\binom dk},\quad
 p(L+(U-L)t)=\sum_{i=0}^d B_i\binom di t^i(1-t)^{d-i}.
 \tag{W8}
\]

The Bernstein basis is nonnegative and sums to one. Entire-ball strict
positivity of every directed B_i therefore proves positive p throughout
the interval. `polynomial_tail.py` uses the exact directed upper endpoint
of N^-1/2 as its initial interval cap; this contains the actual domain.
If a coefficient is not proved positive, it bisects at an exact dyadic
midpoint and checks both halves. Every accepted leaf covers its entire
interval, and the subdivision tree preserves complete coverage. A finite
depth and leaf limit causes explicit failure if the tail is not certified.
There is no floating endpoint selection or positivity acceptance step.

The coefficient collection before (W8) retains algebraic cancellations
between the selected odd and even activation defects. This is why the
tail proof can be substantially stronger than separately bounding their
absolute variations or evaluating a coarse interval extension of (W6).
It does not claim a uniform limit as m decreases to one: the cutoff N,
the signed Euler baseline and all remaining masses are fixed finite
inputs in each certificate, and critical positivity remains an unpaid
source theorem.
