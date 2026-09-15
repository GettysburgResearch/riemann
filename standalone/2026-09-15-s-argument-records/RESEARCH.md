# Record certificates, monotone defects and replay compression

**PROPOSED component proof; independent mathematical/code review required.**
The scalar calculations below are reproduced. Every conclusion about actual
zeros or S at the reported zeros is conditional on genuine Hardy-Z sign changes.
These primitive evaluations have NOT been performed in this packet.

## 1. Normalization and inputs

Let N^-(t) and N^+(t) count all nontrivial zeta zeros with positive ordinate
respectively below and at most t, WITH multiplicity. Put

\[
\theta(t)=\Im\log\Gamma(1/4+it/2)-(t/2)\log\pi,\qquad
F(t)=1+\theta(t)/\pi.
\]

Here log Gamma is analytic on the right half-plane and real on the positive
axis. It is not the principal argument of Gamma reset modulo 2*pi. Away from
zero ordinates, the classical counting identity is S(t)=N(t)-F(t); at a zero, write
S(t+0)=N^+(t)-F(t) and S(t-0)=N^-(t)-F(t).

Hardy's Z(t)=exp(i*theta(t))*zeta(1/2+it) is real on the real axis. Opposite
strict endpoint signs on a bracket imply at least one critical-line zero inside,
not initially uniqueness or simplicity. An off-line pair or additional
multiplicity must not be silently discarded.

The imported analytic input is Trudgian, *Improvements to Turing's method*,
[arXiv:0903.1885v3](https://arxiv.org/abs/0903.1885v3), Theorem 2.2, printed page 3:

\[
\left|\int_u^v S(t)dt\right|\le 2.067+0.059\log v,
\qquad v>u>168\pi. \tag{1}
\]

We use B=2.067+0.059*log(t0+20) for every subwindow in this packet. All endpoints
are below t0+20 and vastly above 168*pi. This established theorem is an imported
input, not a newly proved improvement of Turing's analytic constant.

## 2. An explicit theta remainder; no black-box gamma evaluation

Define

\[
g(t)=\frac{t}{2\pi}(\log(t/(2\pi))-1)+\frac78,
\quad a=g'(t_0)=\frac{\log(t_0/(2\pi))}{2\pi},
\quad b=n-g(t_0).
\]

For t>0 a convenient conservative bound is

\[
|F(t)-g(t)|<\frac1{\pi t}. \tag{2}
\]

Here is a derivation with a complete remainder. The complex Stirling remainder
bound in [DLMF 5.11(ii)](https://dlmf.nist.gov/5.11.ii), applied with the first
Bernoulli term omitted, gives

\[
\log\Gamma(z)=(z-1/2)\log z-z+\tfrac12\log(2\pi)+R(z),
\qquad |R(z)|\le\frac{\sec^2(\arg(z)/2)}{12|z|}.
\]

For z=1/4+it/2, sec^2(arg(z)/2)<2 and |z|>t/2, so |R(z)|<1/(3t).
The imaginary part of the elementary expression differs from
(t/2)*log(t/(2*pi))-t/2-pi/8 by exactly

\[
\frac t4\log(1+1/(4t^2))+\frac14\arctan(1/(2t)),
\]

which lies between zero and 3/(16t). Thus its total error is less than
25/(48t)<1/t, proving (2). The branch is fixed throughout the right half-plane.

Since g''(t)=1/(2*pi*t), Taylor's theorem gives, for |x|<=20,

\[
|F(t_0+x)-g(t_0)-ax|\le
\varepsilon=\frac{101}{\pi(t_0-20)}. \tag{3}
\]

The factor 101 pays 20^2/4 for the Taylor error and one for (2).
On an interval of length h, the integral error is at most h*epsilon. This is a
full uniform error bound, not an assertion that higher terms look negligible.

`check.py` evaluates all elementary quantities by integer outward arithmetic at
384 fractional bits. Machin's identity computes pi from two arctangent series;
log uses binary range reduction and the convergent 2*atanh series. Both include
explicit complete tails. Large integer cancellation is performed at that precision,
not in binary64. No mpmath, gamma, zeta or precomputed theta oracle enters acceptance.

## 3. The monotone-defect lemma: why completeness need not be assumed

Fix t0, integer n, and positive padding lengths L,R. Suppose a collection of
disjoint genuine Z sign brackets lies in (t0-L,t0) union (t0,t0+R). Choose ONE
actual root from each bracket. Define the step count C by C(t0)=n and one upward
unit jump at each selected root, in both directions from t0. Set D=N-C.

**D is nondecreasing, not necessarily constant.** Each selected root removes one
unit from the corresponding actual zero multiplicity. Every unselected root,
remaining multiplicity, or off-line zero contributes a nonnegative jump. There
is no requirement to have already found every zero. No selected root is at t0.

Write J_- = integral from t0-L to t0 of (C-F), and J_+ = integral from t0 to
t0+R of (C-F). Suppose our enclosures provide J_-<=U_Jminus and
J_+>=L_Jplus, and define

\[
U_-=B+U_{Jminus},\qquad U_+=B-L_{Jplus}.
\]

From monotonicity and (1),

\[
-\frac{U_-}{L}\le D(t_0-0)\le D(t_0+0)\le\frac{U_+}{R}. \tag{4}
\]

Indeed integral D on the left is at most L*D(t0-0) and at least -B-J_-;
on the right it is at least R*D(t0+0) and at most B-J_+.

If U_-<L and U_+<R, with both budgets nonnegative, both one-sided integer
values in (4) are zero. This establishes the anchor count and excludes a zero
at the anchor. It does not assume the supplied n is correct.

There is also a **complete inner census**, without verifying every padding zero:

\[
D(t)=0\quad\hbox{for } t-t_0\in(U_--L,\ R-U_+). \tag{5}
\]

For x>0, an unselected unit jump by t0+x forces D>=1 for the remaining length
R-x. Consequently integral D>=R-x, contradicting integral D<=U_+ whenever
x<R-U_+. For x<0, D<=-1 before t0+x forces integral D<=-(L+x), contradicting
integral D>=-U_- whenever x>U_--L. Taking one-sided limits excludes jumps
inside this open core as well. Hence all zeros there are the selected simple
critical-line zeros; no unseen zero or multiplicity can remain there.

This is a reconstruction and application of classical Turing reasoning, not a
new general zero-counting principle or a claim of external priority. The explicit
small certificate extracted from these supplied records is the present addition.

## 4. Computing the integrals from uncertain roots

Let a selected root offset r_j belong to [l_j,u_j], with midpoint m_j and
half-width e_j. In the positive half-window of length h,

\[
J_+=hb-ah^2/2+\sum_{r_j>0}(h-r_j)+\delta_+;
\]

in the negative half-window,

\[
J_-=hb+ah^2/2-\sum_{r_j<0}(h+r_j)+\delta_-;
\qquad |\delta_\pm|\le h\varepsilon. \tag{6}
\]

Replace r_j by m_j and add a symmetric error sum e_j + h*epsilon. All selected
brackets must lie completely within their half-window; `check.py` enforces that.
The formulas remain valid for the actual chosen roots, not just their midpoints.

At h=20 the supplied counts split as 217 left / 210 right for record 1, and
205 left / 212 right for record 2. Thus the printed E values are exactly .217,
.210 and .205,.212, respectively. The independently reconstructed midpoint
integrals round to the posted seven places. The true analytic B values lie below
the posted outward numbers by less than 10^-7, and the reconstructed defect
intervals lie inside the posted intervals. In particular both anchors are isolated
as integers, CONDITIONAL on the corresponding selected sign changes.

With all original coarse brackets the derived complete inner cores are

| Record | Safe complete core, relative to t0 |
|---|---|
| 1 | [-13.191322627, 13.914008492] |
| 2 | [-13.549062568, 12.853536263] |

These are strictly interior decimal endpoints. We do NOT declare all of
[t0-20,t0+20] complete from the stated information.

## 5. Compression to 310 brackets

Use L=7,R=7.32 for record 1 and L=7.67,R=7.34 for record 2. Keep precisely the
supplied brackets wholly inside each padding interval, replacing each coarse
record bracket by its supplied fine refinement. Reconstruct (6), (4), and (5).

| Record | Left count | Right count | Safe complete core |
|---|---:|---:|---|
| 1 | 78 | 75 | [-1.001862683, 1.008402874] |
| 2 | 77 | 80 | [-1.010014783, 1.008373582] |

Every full interval [t_i-1,t_i+1] lies in its open core. The fine record root is
therefore unique and simple if the selected signs are genuine. No discarded
bracket is a premise of this compressed certificate. The 310 selected indices
are machine-readable in `results.json`, and `--jobs` emits the exact endpoint
worklist. The two fine brackets replace their coarse parents; they are not counted
twice. Exactly 620 distinct endpoint evaluations are needed by this worklist.

A preliminary non-rigorous mpmath/decimal-grid scout suggested these padding
lengths. It is NOT an acceptance dependency. The fixed rational lengths and all
reported conclusions are independently reconstructed by the directed checker.
No smallest possible subset or optimal computing-time claim is made.

## 6. Record values and local geometry

The first fine root is the last selected root below its anchor, so
N(gamma1+0)=n1. The second is the first above its anchor, so N(gamma2-0)=n2.
Equation (3) applied to the fine brackets gives the following OUTWARD intervals:

\[
S(\gamma_1+0)\in[4.184313790968,4.185379642172],
\]
\[
S(\gamma_2-0)\in[-4.338683949971,-4.338370564460].
\]

They strictly imply both posted one-sided inequalities and lie strictly inside
the posted finer S ranges. These are conditional deductions, not fresh Z values.

The core also contains the next zero after gamma1 and the previous zero before
gamma2. With the normalization a=log(t_i/(2*pi))/(2*pi), their consecutive gaps
have the following conditional enclosures:

| Local gap | Raw length | Length in local mean-spacing units |
|---|---|---|
| gamma1 to its next zero | [.369303,.371403] | [3.936220465868,3.958603341119] |
| previous zero to gamma2 | [.535698,.537728] | [5.595999696119,5.617205448956] |

The density is evaluated at the integer anchor; this table defines the precise
normalization rather than silently substituting an unfolded theta difference.
The record excursion and these adjacent gaps provide useful targets for a local
prime-phase/zero-displacement model. They do not constrain every high zero.

## 7. Research ownership: next experiments and acceptance gates

The immediate objective is a fully reproducible computational result, not a new
RH-equivalent positivity conjecture.

**Primitive replay first.** Recover or implement a source-pinned high-height
Hardy-Z evaluator with an explicit Riemann-Siegel/accelerated-sum remainder and
directed rounding. Run the exact 620 endpoints. Archive every Z enclosure,
precision, source SHA, command and mathematical remainder; require strict
opposite signs within each pair. Independently rerun at least the four delicate
fine endpoints using a different evaluation path. An external JSON file claiming
signs is not by itself a primitive certificate and cannot enable a trusted status.
No such backend or completed replay is included here.

An ordinary Riemann-Siegel sum has floor(sqrt(t/(2*pi))) terms. At these heights
that is roughly 10^14 terms per naive evaluation. Bober and Hiary's accelerated
and multi-evaluation methods are directly relevant; a call to an arbitrary-
precision elementary library is not a substitute for this work. The reduced
endpoint count is not a promise of a proportional speedup for a shared-block
multi-evaluation engine.

**Then exploit the complete inner windows.** Refine the fine roots by interval
bisection to report narrower S enclosures; compare a completed count residual
C-F against a fixed, explicitly truncated prime-phase model. Keep the prime tail
error separate from fitted residuals. The two normalized gaps above supply
already specified targets, rather than a visually selected after-the-fact test.

**Then hunt new candidates.** A finite prime-phase resonance search can propose
new heights and target both positive and negative S excursions. Every candidate
must pass a source-faithful Z replay and the same count/completeness certificate.
Publish unsuccessful candidate heights and work budgets as well as records.
This search heuristic does not prove a tail estimate, RH, or a universal bound
on S. The present packet does not claim to have executed that campaign.

## 8. Attribution, comparison and mathematical scope

The 2016 comparison is documented in Jonathan W. Bober and Ghaith A. Hiary,
*New computations of the Riemann zeta function on the critical line*,
[arXiv:1607.00709v1](https://arxiv.org/abs/1607.00709v1), Table 2, printed page 7:
a one-sided value 3.3455. The table and its one-sided convention were visually
inspected. This authenticates the historical comparison, not a complete survey
of all records since then. The new quoted magnitudes are more than 25% and 29%
larger than 3.3455, respectively, conditional on the new claims.

The source announcement and computation remain credited to their author; our
work is scalar reconstruction, explicit local-completeness accounting and the
310-bracket replay reduction. The general counting and asymptotic tools are
classical. Independent review and primitive replay are separate remaining tasks.
No finite window here proves RH or extends a verification from height zero all
the way to either anchor.
