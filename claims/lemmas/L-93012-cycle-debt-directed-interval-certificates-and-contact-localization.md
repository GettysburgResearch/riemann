# L-93012 — Directed interval certificates make Cycle Debt fail-closed, sparse, and contact-localized

Claim ID: `L-93012`  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: `L-93010`, `L-93011`; finite LP strong duality  
Scope: exact finite certification for the actual irrational capacity objective; no cofinal Möbius estimate or RH conclusion

## 1. Exact source coordinates, irrational costs

Use the two-channel action notation of `L-93010`. For an action
\(e=(n,j)\), let

\[
 A_e=\mathbf e_n-P_e
\tag{L-93012.1}
\]

be its size-weighted source column. The entries of every \(A_e\) are rational.
Let nonnegative action masses \(x_e^+,x_e^-\) satisfy the exact source identity

\[
 \boxed{
 s=\sum_e x_e^+A_e-\sum_e x_e^-A_e.
 }
\tag{L-93012.2}
\]

The true normalized capacity cost is

\[
 c_e=\omega_e/n>0,
\tag{L-93012.3}
\]

which is generally irrational because \(\omega_e\) contains square roots.
Choose directed rational enclosures

\[
 \boxed{
 c_e^-\le c_e\le c_e^+.
 }
\tag{L-93012.4}
\]

No common denominator or floating-point identification of \(c_e\) is assumed.

## 2. Directed dual certificate

Let \(f\) be a rational potential and put

\[
 \Delta_f(e)=f(n)-P_ef.
\tag{L-93012.5}
\]

Assume the stronger, rationally checkable inequalities

\[
 \boxed{
 0\le\Delta_f(e)\le c_e^-
 \qquad(e\in E).
 }
\tag{L-93012.6}
\]

Since \(c_e^-\le c_e\), this is a genuine feasible dual for the true Cycle-Debt LP. Define

\[
 D=-\langle s,f\rangle
\tag{L-93012.7}
\]

and the directed primal upper value

\[
 C^+=\sum_e x_e^-c_e^+.
\tag{L-93012.8}
\]

Then the true optimum \(\mathfrak N(s)\) obeys the rigorous bracket

\[
 \boxed{
 D\le\mathfrak N(s)\le C^+.
 }
\tag{L-93012.9}
\]

The lower bound is exact dual feasibility. The reconstructed signed flow is an
exact primal candidate with true cost \(\sum_ex_e^-c_e\le C^+\).

## 3. Exact three-part gap identity

Pairing (L-93012.2) with \(f\) gives

\[
 -D
 =\sum_ex_e^+\Delta_f(e)-\sum_ex_e^-\Delta_f(e).
\]

Therefore

\[
\boxed{
\begin{aligned}
 C^+-D
 ={}&\sum_ex_e^+\Delta_f(e)\\
 &+\sum_ex_e^-\bigl(c_e^--\Delta_f(e)\bigr)\\
 &+\sum_ex_e^-\bigl(c_e^+-c_e^-\bigr).
\end{aligned}
}
\tag{L-93012.10}
\]

Every term is nonnegative. The certificate width separates exactly into:

```text
positive-support complementarity defect;
negative-support complementarity defect;
directed capacity-enclosure uncertainty.
```

This identity is fail-closed. Dropping an action, reversing a sign, using an
inner rather than outer enclosure, or hiding an interval width makes the
computed bracket invalid or enlarges its explicit gap.

## 4. Quantitative contact localization

For \(\eta>0\), define the lower- and upper-contact sets

\[
 \mathcal C_\eta^+
 =\{e:\Delta_f(e)<\eta\},
\tag{L-93012.11}
\]

\[
 \mathcal C_\eta^-
 =\{e:c_e^--\Delta_f(e)<\eta\}.
\tag{L-93012.12}
\]

If

\[
 \varepsilon=C^+-D,
\]

then (L-93012.10) gives

\[
 \boxed{
 \sum_{e\notin\mathcal C_\eta^+}x_e^+
 \le\varepsilon/\eta,
 }
\tag{L-93012.13}
\]

and

\[
 \boxed{
 \sum_{e\notin\mathcal C_\eta^-}x_e^-
 \le\varepsilon/\eta.
 }
\tag{L-93012.14}
\]

Likewise, on the set where \(c_e^+-c_e^-\ge\eta\),

\[
 \boxed{
 \sum x_e^-\le\varepsilon/\eta.
 }
\tag{L-93012.15}
\]

Thus a near-optimal certificate must concentrate positive mass near the lower
Bellman envelope, negative mass near the upper envelope, and charged mass on
well-resolved capacity columns. This is a quantitative version of the exact
bang-bang theorem `L-93011`, not a heuristic about solver output.

## 5. Global sparsity of an exact optimum

Let \(A\) be the finite matrix with columns \(A_e\), and put

\[
 r_A=\operatorname{rank}A.
\]

The two-channel LP is

\[
 \min\sum_ec_ex_e^-
 \quad\text{subject to}\quad
 A x^+-A x^-=s,
 \qquad x^\pm\ge0.
\tag{L-93012.16}
\]

Whenever it is feasible, its objective is bounded below by zero and an optimum
exists. Choose an optimum with the smallest number of positive coordinates. If its
active signed columns were linearly dependent, there would be a nonzero vector
\(h\) supported on them with zero source. Both sufficiently small perturbations
\(x\pm th\) remain nonnegative. If the objective derivative along \(h\) is
nonzero, choose the decreasing sign; if it is zero, choose either sign. Continue
until one active coordinate vanishes. The result is feasible, has no larger
cost, and has smaller support, a contradiction. Therefore the active signed
columns are linearly independent and their number is at most

\[
 \boxed{r_A}.
\tag{L-93012.17}
\]

Common positive and negative mass on the same action can be cancelled first.
Hence there is an optimal signed fragmentation supported on at most \(r_A\)
signed action columns globally.

The size vector lies in the left kernel of \(A\), so

\[
 r_A\le X-1.
\tag{L-93012.18}
\]

The action matrix and critical source are rational. Every basic feasible
solution is therefore rational, even though the objective coefficients \(c_e\)
are irrational. Irrationality is confined to selecting and certifying the
optimal vertex, and is handled by (L-93012.4)--(L-93012.10).

## 6. Proof-producing consequence

A complete finite Cycle-Debt certificate may now consist of:

```text
at most rank(A) rational signed action masses;
one exact rational source identity;
one rational dual potential;
rational outward intervals for every used or dual-tested capacity;
one exact gap decomposition.
```

If the displayed gap is \(\varepsilon_X\), then the true Cycle Debt is trapped
in an interval of width \(\varepsilon_X\). A cofinal family with

\[
 C_X^+=X^{o(1)}
\]

already gives the required upper theorem; a family with both endpoints
subpower and shrinking relative gap gives a reproducible primal-dual closure.
Neither family is constructed here.

## 7. Proof boundary

Established exactly:

1. directed rational primal/dual bracket for irrational capacities;
2. exact three-part certificate-gap identity;
3. quantitative lower/upper contact localization;
4. uncertainty-mass localization;
5. existence of a globally rank-sparse optimal signed action support;
6. rationality of an optimal basic action mass vector.

Open:

1. export and solve the actual critical finite certificates cofinally;
2. prove subpower negative-channel cost;
3. Cycle Debt and RH.
