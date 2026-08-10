# Anthropic zeta-23 source dossier

Status: **PINNED EXTERNAL RESULT — IMPORTED FOR REVIEW AND EXTENSION**  
Imported: 2026-08-10  
Source lock: [`SOURCES.lock.json`](SOURCES.lock.json)  
Scope: theorem/proof map and exact provenance; the upstream PDFs and Lean tree are not vendored here

## 1. Headline result

The imported paper proves, unconditionally,

\[
\liminf_{T\to\infty}\frac{N^*_{0}(T,2T)}{N(T,2T)}\ge \frac23,
\qquad
\liminf_{T\to\infty}\frac{N^s_{0}(T,2T)}{N(T,2T)}\ge \frac23,
\qquad
\liminf_{T\to\infty}\frac{N_d(T,2T)}{N(T,2T)}\ge \frac56.
\]

After optimizing the test window, the three constants become

\[
0.6725007036\ldots,
\qquad
0.6725007036\ldots,
\qquad
0.8362503518\ldots .
\]

The same architecture is stated for each fixed primitive Dirichlet \(L\)-function. The upstream revision also contains unconditional results for zeros of \(\xi'\).

This is not a proof of RH. It is a lower-bound theorem for the proportion of zeros that are simple and on the critical line.

## 2. Core mechanism

The paper compresses Weil's Hermitian form to a finite Gabor family. In the resulting Hermitian matrix:

- each distinct zero on the line contributes a positive rank-one atom;
- each functional-equation pair off the line contributes a pullback of a hyperbolic block of signature \((1,1)\);
- the first trace and Frobenius square are evaluated from the prime side using only bandwidth at most one;
- a rank--trace--inertia inequality converts those two moments and the block structure into counts of on-line, simple, and distinct zeros.

The load-bearing linear-algebra inequality is: if \(P\succeq0\), \(\operatorname{rank}P\le r\), and \(n_+(Q)\le b\), then for every \(c>0\),

\[
\|P+Q\|_F^2
\ge c\operatorname{tr}P-\frac{c^2}{4}r
   +2c\operatorname{tr}Q-c^2b.
\]

At \(c=2\), this is the matrix analogue of \(m^2\ge2m-1\). Regrouping the simple on-line atoms on the rank side gives the analogue of \(m^2\ge3m-2\).

For normalized bandwidth \(0<\lambda\le1\), a scalar window with profile \(v\ge0\) produces

\[
c_\lambda(v)
=\frac{\lambda(\int v)^2}
 {\int v^2+\lambda^2\iint |s-t|v(s)v(t)\,ds\,dt}.
\]

Its optimum is attained by

\[
v^*_{\lambda}(s)=\cos(\sqrt2\lambda s),
\qquad |s|\le\frac12,
\]

with

\[
c^*_{\lambda}
=\frac{\sqrt2\tan(\lambda/\sqrt2)}
 {1+(\lambda/\sqrt2)\tan(\lambda/\sqrt2)}.
\]

The on-line/simple certificate is \(2-1/c^*_{\lambda}\); the rank--trace distinct certificate is \((3-1/c^*_{\lambda})/2\), with the Cauchy branch \(c^*_{\lambda}\) retained when it is larger.

## 3. Verification state

The source lock pins the public Lean repository at commit
`3635e74826a4c1fcece7d1cd2b6fa75e43a00510`.
Its audit records:

- successful builds of the headline library and comparator solutions;
- no `sorry` under `Zeta23/` or the solution files;
- deliberate placeholders only in trusted challenge statement files;
- no project-specific axiom declarations;
- only Lean's standard `propext`, `Classical.choice`, and `Quot.sound` in the theorem axiom audit;
- successful comparator replay against Mathlib-only statement files.

That is unusually strong evidence. It does not eliminate the need for mathematical review of the modeling choices, definitions, and imported analytic statements, but it moves the result far beyond an ordinary unverified preprint claim.

## 4. Internal audit verdict

The imported argument's core geometry is coherent:

1. the critical-line and off-line-pair blocks have the claimed inertia;
2. the rank--trace inequality is valid and sharp in the stated information class;
3. the prime-side first and second moments use unconditional bandwidth-one input;
4. the taper and tail are essential and are handled explicitly;
5. the endpoint \(\lambda=1\) is reached with logarithmic, not power, savings.

The three places where a cold reviewer should still spend most time are:

- the exact Guinand--Weil normalization and conjugation conventions;
- the finite-grid-to-full-grid end and tail transfer;
- uniformity of the Montgomery--Vaughan error at the endpoint.

The full paper and Lean tree, not the five-page informal note, are the source of record.

## 5. Extensions in this branch

- `L-90301`: a co-lattice multiwindow collapse theorem. It proves that finitely many windows on the same critical modulation lattice reduce exactly to one aggregate scalar profile, so they cannot improve the optimized constant.
- `T-90301`: a short-window and hybrid-conductor extension. It replaces the dyadic budget by the general ratio
  \(\lambda\sim \log H/\log(qT)\), uniformly for \(H\ge T^\alpha\), \(q\le T^\theta\).
- `O-90302`: a numerical Fredholm/Nyström audit indicating that the upstream quartic \(\xi'\) window is already within a few parts in \(10^6\) of the scalar-window optimum.

All three retain the explicit boundary that RH remains unproved.
