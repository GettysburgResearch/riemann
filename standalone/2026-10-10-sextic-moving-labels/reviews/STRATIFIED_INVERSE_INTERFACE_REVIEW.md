# Review of the stratified inverse: exact masks, phases and support

**Reviewer role:** separate moving-label adapter author, reviewing the root author's new stratified inverse. This is an independent review of the composition and cutoff argument, not an independent review of the mixed completed estimate authored by this reviewer. The latter theorem requires its own separate review. The analytic sixth-power-free sieve and numerical optimization are also being reviewed separately.

**Target:** `SIXTH_POWER_STRATIFIED_INVERSE.md`, SHA-256 `f98cc20e361ebb99af7dbd4b5ffef83a8a55ca11c4d3f24da238bc24be4cb2e9`, read in full from the root author's working folder. The frozen version includes the explicit bounded nonempty inner-scale convention after equation (3.4). No source file was edited during this review.

**Verdict at stated scope:** the row identity, exclusion norm, exact inverse and regrouping, capped cutoff, and disjoint-sector summation preserve the necessary arithmetic data. I found no missing prime-overlap condition, misplaced character phase, or omitted cube mask in these steps. This verdict retains the stated mixed completed theorem and the separate sixth-power-free sieve as premises.

## 1. Sixth-power decomposition and character zeros

The decomposition

\[
k=u v^6 k_0
\]

uses the quotient and remainder of each prime valuation upon division by six. The labels \(v,k_0\) may overlap. The target explicitly preserves that overlap; imposing coprimality would omit rows of valuation seven and higher not divisible by six.

At every physical column \(n\) outside the fixed bad set,

\[
\chi_n(v^6)=\mathbf1_{(n,v)=1}.
\]

Hence the added exclusion is exactly the radical of the good part of \(v\). The pre-existing fourth-power twist at \(f\) already supplies zeros at primes of \(f\), so those primes are redundant in the combined exclusion. If \(q_*=q/(q,f)\), the new effective norm obeys

\[
Q_v\le (Nq_*)Nv=Q Nv.
\]

There is no loss from assuming \((v,k_0)=1\), because the target does not make that assumption. The physical variable height remains \(H/(Nv)^6\). The newly inserted principal mask is a column restriction, not a height change of the remaining variable row.

Bad-prime factors of \(v\) introduce no new column exclusion because physical columns already avoid the bad set. Their sixth powers have character value one there. The sixth-power-free remainder has only finitely many possible valuations at those fixed primes, retained by the cited sieve; units are also included.

## 2. The inverse has the right phase and both inner exclusions

For fixed \(v\), write \(q_v\) for the effective exclusion and let \(t\) be the cube-inverse index. The physical completed twist has cube coefficient

\[
\overline{\alpha(t)}^3\Psi_{k_0,af;q_v}(t)^3
=\lambda(t)^3\chi_t(k_0)^3
\mathbf1_{(t,afq_vS)=1}.
\]

Thus the external coefficient in the inverse is

\[
\mu(t)\lambda(t)^3\chi_t(k_0)^3/(Nt),
\]

with \((t,q_v fS)=1\) outside the outer sum and the necessary outer mask \((a,t)=1\) inside it. This exactly matches the target. The fourth-power auxiliary gives exponent twelve in this cube phase; its unit values become one, while its nonunit zeros are retained by the displayed exclusion. No auxiliary phase of nontrivial unit value is missing.

The original \(q_v\) mask acts on the completed squarefree index and its unrestricted physical cube index. The target explicitly requires both. Retaining only the squarefree mask would break the divisor cancellation after the physical cube expansion.

The row factors \(\chi_t(k_0)^3\) retain their zeros when \(t\) meets the varying row. They may be bounded as norm contractions only after fixing \(t\), which is the order used in the short inverse estimate.

## 3. Exact long-tail regrouping

After substituting the physical cube expansion into the long inverse, set \(d=t b\). There is no reason for \(t\) and \(b\) to be coprime, nor for \(d\) to be squarefree. Complete multiplicativity gives the single phase

\[
\lambda(d)^3\chi_d(k_0)^3,
\]

and the coefficient is exactly

\[
c_{R_v}(d)=\sum_{\substack{t\mid d\\Nt>R_v}}\mu(t).
\]

The raw child has outer mask \((a,d)=1\). The inner squarefree factor may overlap \(d\). The target retains each of these facts. The allowed physical \(d\) also obeys \((d,q_v fS)=1\), since both inverse and physical cube labels obey that exclusion. These are exactly the restrictions in the moving-label identity, with no extra coprimality assumption.

For fixed \(d\), every remaining \(q_v,f,d\) factor is a bounded row-independent part of the raw column coefficient, except the external phase which is a row contraction. This is the correct interface for a sixth-power-free row sieve. It is not an assertion that deleting arbitrary coefficients contracts the norm of the completed family.

## 4. The cap is required and correctly used

Compact physical support gives \(Nt,Nd\le K D^{1/3}\) for one fixed \(K\). The proposed choice

\[
R_v=\min(K D^{1/3},R Nv)
\]

therefore has two genuinely different cases:

- On uncapped strata, \(R_v=R Nv\), and the positive long-tail estimates may use that value.
- On capped strata, no inverse index satisfies \(Nt>R_v\); the long part is exactly empty.

The target treats the capped strata as empty and applies the identity \(R_v=R Nv\) only to the uncapped strata. Applying a reciprocal tail bound with \(R Nv\) after the cap without this distinction would not be justified. The target does not make that error.

For the short part, the inequality \(R_v\le R Nv\) is always valid and has the correct direction because its cutoff powers are nonnegative for \(1/2<\beta\le1\).

Bounded nonempty inner scales below one occur only within a fixed support-dependent range. They are expressly covered by the mixed completion's stated convention; they do not require an estimate at arbitrarily small analytic length.

## 5. Disjoint-sector summation

The original physical rows partition by \(v\), so the target sums their squared norms. It does not apply Minkowski over \(v\). The short-part weights have exponents

\[
-6,\qquad -13/2-3\beta,\qquad -17/3,
\]

and the uncapped tail weights have exponents

\[
-6,\qquad -3,\qquad -6.
\]

All are strictly below \(-1\). The ideal sums therefore converge. In particular the cubic decrease of the chosen inverse cutoff contributes the summable \((Nv)^{-3}\) in the length term that would otherwise have been repeated once per sixth-power copy. This is the arithmetic reason the direct all-row repetition cost disappears.

The variable labels satisfy a fixed polynomial ceiling in the common reference \(D\), since only \(Nv\ll H^{1/6}\) contribute. Choosing preliminary epsilon losses sufficiently small is consequently compatible with the source uniformity. This does not require a claim that the constants are uniform in unbounded moment order.

## 6. Scope retained

The target concerns the actual raw two-axis Gauss polynomial with its mixed labels. It does not substitute that polynomial for the original Möbius sum, remove the signed first-Poisson auxiliary sum, or estimate a centered product-column subtraction. Its statement of those remaining obligations is correct.

No Lean or infinite analytic verification was run in this review. The review checks the exact arithmetic composition and the displayed convergent summation, while retaining the source-qualified analytic premises stated in the target.
