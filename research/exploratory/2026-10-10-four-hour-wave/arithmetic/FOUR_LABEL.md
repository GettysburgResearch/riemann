# Retaining four labels: global SHARP positivity above 7/5

Status: **PROPOSED theorem, executed directed certificates; independent
analytic review requested.** Exact beta, duplicate 67 label and boundary
kernel are unchanged. No critical positivity or RH conclusion is asserted.

**Proposed theorem A-FL1.** For every real x>=1 and every real m>=7/5,
\(H_m(x)>0\).

This theorem retains the four-label positive mass, bounds the three-label
negative mass directly, and absorbs the five-label mass by removal. The
all-real interval argument from `TWO_LABEL.md` is preserved.

## 1. The level lower bound

Use the active subset masses M_k, normalized ratios r_n, and removal mass
R_m(x) from (T1)--(T2). For a fixed endpoint and power, suppose
R_m(x)<=R<5. Then

\[
 H_m(x)\ge M_0-M_1+M_2-M_3+(1-R/5)M_4.
 \tag{F1}
\]

Indeed (T2) gives M5<=R M4/5. Every later pair M_(2j)-M_(2j+1),
j>=3, is nonnegative because R/(2j+1)<1. The non-strict removal
inequality handles all empty levels, and a final unmatched even level is
nonnegative. This proves (F1) without an alternating-series assumption.

For a power slab [m0,m1] and an endpoint interval [L,U], set

\[
 O_1=\frac{M_1(m_0,U)}{T(U)^{m_0}},\quad
 O_3=\frac{M_3(m_0,U)}{T(U)^{m_0}},\quad
 E_2=\frac{M_2(m_1,L)}{T(L)^{m_1}},\quad
 E_4=\frac{M_4(m_1,L)}{T(L)^{m_1}}.
 \tag{F2}
\]

Each normalized level is a sum of the same r_n(m,x), one term for each
labelled subset. Therefore it is nondecreasing in x and nonincreasing in
m, including activation jumps. If O1<5, (F1) yields throughout the
entire real rectangle

\[
 \frac{H_m(x)}{T(x)^m}
       \ge1-O_1+E_2-O_3+(1-O_1/5)E_4.
 \tag{F3}
\]

All substitutions have the correct direction: negative odd levels use
upper bounds; positive even levels use lower bounds; the last coefficient
is nonnegative and is bounded below by 1-O1/5.

## 2. The infinite three-label majorant

For a>1, let the label weights be q^-a for every ordinary prime q plus a
second labelled 67 weight. Their power sums are

\[
 W_j(a)=P(ja)+67^{-ja},\qquad j\ge1.
 \tag{F4}
\]

Their third elementary symmetric sum is

\[
 e_3(a)=\frac{W_1(a)^3-3W_1(a)W_2(a)+2W_3(a)}6.
 \tag{F5}
\]

For a finite label set this is the usual expansion of the cube: subtract
three ordered equal-pair coincidences and add twice the all-equal term.
Since W1(a)<infinity, the positive triple sum and all displayed products
converge absolutely. Increasing finite label sets prove (F5) for the full
source. Duplicate 67 is a distinct label in both the power sums and the
elementary sum, so no equal-value coincidence is mistakenly removed.

For m>=m0, a0=(m0+1)/2, the strict active ratio bound (P4) implies

\[
 \frac{M_1(m,x)}{M_0(m,x)}\le W_1(a_0),\qquad
 \frac{M_3(m,x)}{M_0(m,x)}\le e_3(a_0).
 \tag{F6}
\]

For the second inequality, each active three-label term r_n(m,x) is
at most n^(-a0); allowing all inactive triples gives the positive complete
Euler elementary sum. Thus on x>=L and m in [m0,m1], write
O1=W1(a0), O3=e3(a0), and retain E2,E4 at (m1,L). Equations
(F1)--(F3) then hold on the entire unbounded endpoint interval.

## 3. Complete enumeration and the executed interval conditions

`verify_four_label.py` enumerates all labelled subsets through level four
with product <=1000000. A strictly increasing label-index recursion
preserves distinct labels, including both 67 labels; integer products may
repeat and are retained with their multiplicity. The complete source has
78498 ordinary primes (last 999983). Product-list counts are

| Level | Complete labelled product count |
|---:|---:|
| 1 | 78499 |
| 2 | 211614 |
| 3 | 210777 |
| 4 | 95714 |

The independent two-label construction reproduces the full level-two
multiset exactly. Small activation controls require the first level-three
products through 70 to be [30,42,66,70], and the level-four products
through 330 to be [210,330]. The 67 duplicate counts are checked. Every
product multiset is hashed in the result.

Arb at 192 bits evaluates normalized level masses and all strict margins.
For infinite odd majorants, each Wj uses the Möbius log-zeta series
through k=80 and the proved entire omitted-tail ball (P10), applied at
s=j a0. (F5) uses directed arithmetic on those balls. All domains, signs,
coverage, O1<5 and positivity comparisons are explicit guards.

The seven closed exponent intervals are

\[
 [1.4,1.405],\ [1.405,1.411],\ [1.411,1.420],\
 [1.420,1.434],\ [1.434,1.454],\ [1.454,1.484],\ [1.484,1.5].
 \tag{F7}
\]

For each interval the checker proves the entire-ball strict positivity of
the right side of (F3) on each consecutive endpoint interval in

\[
 1,10,20,40,80,160,320,640,1280,2560,5120,10240,
 20480,40960,81920,163840,327680,655360,1000000,
 \tag{F8}
\]

and on the unbounded interval [1000000,infinity), using (F6).
These 18 bounded intervals and one unbounded interval cover all real
x>=1 for each power slab. (F7) covers every real m in [1.4,1.5], and
the independently reviewed A-TL1 covers every m>=1.5. This proves A-FL1
subject to independent review and execution of the stated finite guards.

The certificate is the retained directed JSON, with normal and optimized
replay required to match byte for byte. Floating reconnaissance chose
the endpoint and power intervals only; it does not establish any margin.
This remains a bounded sufficient exponent improvement. Absolute Euler
power sums diverge as a approaches one, and neither (F3) nor a finite
number of retained levels controls the critical limit by itself.

The actual normal and optimized JSON receipts are byte-identical. The
seven unbounded margins are, in slab order, approximately
0.0126552982183, 0.0179815158731, 0.0200969730849, 0.0222090115480,
0.0293249172257, 0.0365720727527, and 0.0964606519531; the retained
balls, rather than these rounded values, are the acceptance evidence.
Three independent control groups pass in both modes: native trial-factor
Möbius projection through 1000, Newton's third elementary identity against
a positive coefficient update, and the four-level lower bound against
direct native signed sums. `FOUR_LABEL_EXECUTION.json` binds the runs.
