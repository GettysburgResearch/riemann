# Keeping two labels: global SHARP positivity for every m>=3/2

Status: **PROPOSED theorem with directed certificates; independent analytic
review requested.** Literal beta, duplicate source label at 67, and SHARP
kernel are unchanged. Critical positivity and RH remain open.

**Proposed theorem A-TL1.** For every real \(m\ge3/2\) and every real
\(x\ge1\), \(H_m(x)>0\), with the definitions in `POWER_THRESHOLD.md`.

This proof needs neither the squarefree estimates nor an eventual-positive
asymptotic. It retains the positive two-label level in the finite signed
source. The four exponent slabs and their interval inequalities are
certified with directed Arb, and the infinite prime mass uses the proved
prime-zeta tail contract (P10).

## 1. A three-level lower bound with a positive remainder

For the finite active labelled subsets A at endpoint x, retain
\(w_m(A)=n_A^{-1/2}T(x/n_A)^m\) and
\(M_k(m,x)=\sum_{|A|=k}w_m(A)\). These are positive level masses,
not the absolute coefficients after labels are projected to integers.
The two distinct 67 labels produce the exact beta coefficients, and
\(H_m=\sum_k(-1)^kM_k\). Put M_k=0 beyond the last active level.

As in A-HS2, define

\[
 r_n(m,x)=n^{-1/2}
      \left[\frac{T(x/n)}{T(x)}\right]^m,
 \qquad r_n(m,x)=0\ (x<n),\quad n\ge2.
 \tag{T1}
\]

For any fixed integer n>=2, r_n is nondecreasing in the real endpoint x,
including the positive activation jump, and nonincreasing in m>0.
The derivative of its kernel ratio, with v=sqrt(x), is
\(12(1-n^{-1/2})/(4v-3)^2>0\) on the active domain. The ratio there is
strictly between zero and one.

Write R_m(x) for the complete one-label removal mass in (H2), so
\(M_1/M_0=R_m(x)\). The exact removal inequality is

\[
 kM_k\le R_m(x)M_{k-1},\qquad k\ge1.
 \tag{T2}
\]

For an active extension A=B union {q}, its parent endpoint is y=x/n_B<=x;
thus its weight ratio is r_q(m,y)<=r_q(m,x). Sum over all k removals,
then allow every prime label in the upper bound. This proves (T2),
including empty levels. No distinctness restriction is lost in the
direction needed for the inequality.

**Lemma A-TL2.** If R_m(x)<=R<3 and
\(M_2(m,x)/M_0(m,x)\ge S\ge0\), then

\[
 \frac{H_m(x)}{T(x)^m}
       \ge1-R+(1-R/3)S.
 \tag{T3}
\]

Indeed M3<=R M2/3. Every later pair M_(2j)-M_(2j+1), j>=2,
is nonnegative by (T2), since R/(2j+1)<1. Retain the first two pairs:
\(H_m\ge M_0-M_1+(1-R/3)M_2\). Divide by M0=T(x)^m>0,
then use M1/M0<=R and the nonnegative coefficient 1-R/3. This gives
(T3). A final unmatched even level is also nonnegative.

## 2. Uniform bounds on an endpoint interval and on the whole tail

Let \(1<m_0\le m\le m_1\), \(1\le L\le x\le U\), and let

\[
 S_{m_1}(L)=\frac{M_2(m_1,L)}{T(L)^{m_1}}
  =\sum_{\substack{p<q\ \mathrm{ordinary}\ pq\le L}}r_{pq}(m_1,L)
      +\sum_{\substack{p\ \mathrm{ordinary}\67p\le L}}r_{67p}(m_1,L).
 \tag{T4}
\]

The second sum pairs the extra source label with every ordinary prime,
including p=67. Thus 134 and every 67p with p!=67 have multiplicity
two when they also occur in the first sum; 4489 has multiplicity one.
Ordinary equal-prime pairs are absent. This is exactly the finite
two-label level, not a squarefree-only substitute.

Monotonicity in (T1) gives

\[
 R_m(x)\le R_{m_0}(U),\qquad
 \frac{M_2(m,x)}{M_0(m,x)}\ge S_{m_1}(L).
 \tag{T5}
\]

Therefore the entire real rectangle of endpoints and powers is positive
whenever

\[
 R_{m_0}(U)<3,\qquad
 1-R_{m_0}(U)+(1-R_{m_0}(U)/3)S_{m_1}(L)>0.
 \tag{T6}
\]

For an unbounded endpoint interval x>=L, use instead

\[
 V_0=P((m_0+1)/2)+67^{-(m_0+1)/2}.
 \tag{T7}
\]

The strict kernel comparison (P4) gives R_m(x)<=V0 for every x and
m>=m0. The same proof gives positivity on the whole tail if

\[
 V_0<3,\qquad 1-V_0+(1-V_0/3)S_{m_1}(L)>0.
 \tag{T8}
\]

The strict kernel bound is not required to provide the margin: the
certificate proves the non-strict majorant expression itself positive.
Every use of (T6) or (T8) is an analytic interval implication, not an
inference from the signs of finitely many H_m values.

## 3. Finite directed certificate and full interval coverage

`verify_two_label.py` sets Arb to 192 bits, uses exact rational power
endpoints, and enumerates all ordinary primes through 100000 (9592,
last 99991). It forms the complete multiset of two-label products through
100000: 23550 entries, including all duplicate-67 multiplicities.
The sorted multiset is hashed in the execution result. Independent controls
require the product list at 10 to be [6,10], and multiplicities 2 at
134 and 1 at 4489.

For each of the four exponent slabs

\[
 [1.5,1.52],\quad[1.52,1.56],\quad
 [1.56,1.64],\quad[1.64,1.81],
 \tag{T9}
\]

the checker proves (T6) on every consecutive interval in the chain

\[
 1,10,20,40,80,160,320,640,1280,2560,5120,10240,
   20480,40960,81920,100000.
 \tag{T10}
\]

It also proves (T8) with L=100000. Infinite P(a) is enclosed by the
Möbius log-zeta series through k=80, plus the explicit entire omitted-tail
ball (P10). Euler product convergence holds because each a>1.
The extra 67 term is added once. Domain, coverage, R<3 and positivity
comparisons are explicit guards, all of which must hold for entire Arb
balls. No Python assertion or ordinary floating value enters acceptance.

The retained `results/two-label.normal.json` and optimized replay contain
every interval margin and the four unbounded margins. Their strict
positivity, (T6), and (T8) cover every real x>=1 for every real
m in [1.5,1.81]. The exact rational A-SP1 threshold 1.80206853774<1.81
covers all larger m. This proves A-TL1 subject to independent review of
the displayed analytic level argument.

| Power slab | Unbounded certificate margin, scale decimal |
|---|---:|
| [1.5,1.52] | 0.00754409984518 |
| [1.52,1.56] | 0.0152333892298 |
| [1.56,1.64] | 0.0315038299446 |
| [1.64,1.81] | 0.0626361582465 |

Normal and optimized checker JSON files are byte-identical. Four independent
control groups also pass in both modes: recursive label-subset projection
against trial-factor Möbius coefficients through the repeated-label square
4489, pair enumeration against recursive subsets, native signed sums against
level sums, and the full removal inequalities. The k=1 inequality is checked
as equality, because R=M1/M0 exactly; higher active levels are strict in
these finite controls. The proofs still use the non-strict form at all
levels, including empty ones. `TWO_LABEL_EXECUTION.json` records the runs.

Ordinary floating reconnaissance was used to choose the four slabs and
the endpoint chain. It is not retained as a certificate and supplies no
acceptance condition. The checked proof requires no finite zeta census,
zero-free input, Mertens bound, or critical-power limit.
