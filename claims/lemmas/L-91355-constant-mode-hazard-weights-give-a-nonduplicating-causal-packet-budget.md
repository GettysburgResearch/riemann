# L-91355 — Constant-mode hazard weights give an exact nonduplicating causal-packet budget

Claim ID: `L-91355`  
Status: **PROVED EXACT POSITIVE BUDGET THEOREM — PACKET-TYPING HYPOTHESES EXPLICIT**  
Created: 2026-08-13  
Depends on: `L-91336`, `L-91352/L-91353`, `L-91354`, `T-91305`  
RH status: **unproved**

## 1. Ordered rough scales

Let

\[
 67\le p_1<p_2<\cdots<p_k,
 \qquad r_j=p_j^{-1/2}.
\]

Define the constant-mode survival probabilities

\[
 s_0=1,
 \qquad
 s_j=\prod_{i=1}^{j}(1-r_i),
\tag{L-91355.1}
\]

and the first-hazard weights

\[
 \boxed{
 \lambda_j=r_js_{j-1}.
 }
\tag{L-91355.2}
\]

Then

\[
 s_{j-1}-s_j=\lambda_j,
\]

so

\[
 \boxed{
 s_k+\sum_{j=1}^{k}\lambda_j=1.
 }
\tag{L-91355.3}
\]

Thus the `lambda_j` are a genuine subprobability partition of one parent packet,
not one full parent copy per rough prime.

## 2. Safe canonical child coefficients

Put

\[
 \boxed{
 \alpha_j=r_j\lambda_j
 =r_j^2s_{j-1}.
 }
\tag{L-91355.4}

The diagonal hidden least-prime hazards of `L-91336` are

\[
 h_j^X=r_j^2\prod_{i<j}(1-r_i^2),
 \qquad
 h_j^Y=r_j\prod_{i<j}(1-r_i)=\lambda_j.
\tag{L-91355.5}

Because

\[
 1-r_i\le1-r_i^2,
\]

one has

\[
 \boxed{
 0\le\alpha_j\le h_j^X,
 \qquad
 0\le\alpha_j\le h_j^Y.
 }
\tag{L-91355.6}

Consequently, for every positive physical state `u`, the canonical hidden child

\[
 \alpha_j I(u)
\]

is a coefficientwise subpacket of the exact hidden hazard packet `H_jI(u)`.
Unlike the maximal coefficient `min(h_j^X,h_j^Y)` of `L-91354`, the present
coefficient is chosen to satisfy the separate causal-parent budget below.

## 3. Exact causal-packet identity

Let `P_X` denote any packet at endpoint `X`, and let `A_pP_(X/p)` denote its
positive child placement in the parent coordinate. No positivity is assumed yet
for the difference packet.

For every `j`, define the causal residual

\[
 \mathcal C_j(P_X)
 =P_X-r_j\mathcal A_{p_j}P_{X/p_j}.
\tag{L-91355.7}

Since `alpha_j=lambda_j r_j`, one has identically

\[
 \lambda_j\mathcal C_j(P_X)
 +\alpha_j\mathcal A_{p_j}P_{X/p_j}
 =\lambda_jP_X.
\tag{L-91355.8}

Summing and using (L-91355.3) gives the exact packet equality

\[
\boxed{
 P_X
 =s_kP_X
  +\sum_{j=1}^{k}\lambda_j\mathcal C_j(P_X)
  +\sum_{j=1}^{k}\alpha_j\mathcal A_{p_j}P_{X/p_j}.
}
\tag{L-91355.9}

Every scalar coefficient in (L-91355.9) is nonnegative. The parent packet is
spent exactly once. In particular, this identity cannot suffer the
parallel-parent overdraw fenced by `R-91305`.

## 4. Strong child-mass contraction

Since the primes are increasing,

\[
 r_j\le r_1\le\frac1{\sqrt{67}}<\frac18.
\]

Therefore

\[
\boxed{
 \sum_{j=1}^{k}\alpha_j
 =\sum_jr_j\lambda_j
 \le r_1\sum_j\lambda_j
 <\frac18.
}
\tag{L-91355.10}

Thus all inherited children together carry less than one eighth of the parent
packet coefficient. Every child endpoint satisfies

\[
 X/p_j\le X/67<c_0X.
\]

This is substantially stronger than the coefficient-one hypothesis of the
branching consumer.

## 5. Measure-valued version

The construction is pointwise. Let a positive packet measure carry at each
source point a finite ordered list of active rough scales. Define `s_j`,
`lambda_j`, and `alpha_j` pointwise and integrate.

Monotone convergence gives

\[
 \mathfrak m_{\rm parent}
 =\mathfrak m_{\rm survival}
  +\sum_j\mathfrak m_{{\rm causal},j}
  +\sum_j\mathfrak m_{{\rm child},j}
\tag{L-91355.11}

as an equality of coefficient measures whenever the causal residuals are
admitted packet types. The total child measure is bounded by one eighth of the
parent measure.

The same identities hold after every linear endpoint, row, ordinary-column,
radix-four, target, or score map. Nonlinear Hall projection must be applied to
each causal packet before summation, or after a separately proved
sum-before-project theorem; this theorem does not silently commute Hall with the
rough tree.

## 6. Application to the live factor-54 route

For the `P_61` one-prime packets, `L-91352/L-91353` provide the current causal
packet candidates, and `L-91354` provides the hidden safe-child interpretation.
Equation (L-91355.9) supplies the missing nonduplication ledger:

```text
survival packet                         coefficient s_k;
current causal packets                  total parent coefficient <=1;
canonical contracted children           total coefficient <1/8;
parent duplication                       impossible by exact identity.
```

If the survival packet and every causal packet belong to the admissible
measure-valued cone of `T-91305` with uniformly bounded current debt, then
iteration gives

\[
 \mathfrak L_X
 \le \frac18\sup_{Y\le c_0X+O(1)}\mathfrak L_Y+O(1),
\]

and hence the RH consumer closes with room to spare.

The remaining theorem is packet typing, not mass accounting: one must place the
survival packet and the exact causal residuals into the same physical
ordinary/radix-four cone while retaining the literal component-row score.

## 7. Proof boundary

```text
constant-mode first-hazard partition             EXACT
safe canonical child lies in both hazard modes    EXACT
nonduplicating causal-packet identity              EXACT
all child coefficients sum to <1/8                 EXACT
measure-valued source ledger                       EXACT
causal packet target Hall                          AVAILABLE / L-91352
causal packet positive all-row candidate           AVAILABLE / L-91353
literal physical packet typing                     OPEN / LRPT
survival packet typing                             OPEN
Riemann Hypothesis                                 UNPROVEN
```
