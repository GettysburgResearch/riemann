# L-family audit: why the new favorable divisor closure is special to zeta

**A bounded extension for #738. No GRH conclusion.** The inert-square removal,
auxiliary-sign individualization and central-singularity warnings from STC26
remain unchanged. The present result is a precise interface test: the new
zeta cancellation cannot be copied into the elliptic family by renaming mu.

## 1. Exact comparable-sector formula for a general real source

Let a be any real arithmetic source, h any real arithmetic weights with
h(1)=0, and A=h*a. For a positive observation kernel w(max(m,t)), set

$$d=1*a,\qquad 1*A=h*d.$$

Partition comparable pairs into m|t, including equality, and t|m with t<m.
The exact answer is

$$\boxed{P_{\rm div}(a,h)=\sum_n w(n)
 \left[A(n)d(n)+a(n)(h*d)(n)-a(n)A(n)\right].}\tag{1}$$

This is finite algebra, with no analytic hypotheses. With d=delta+e, it is

$$\sum_n w(n)a(n)[h(n)-A(n)]
 +\sum_n w(n)\{A(n)e(n)+a(n)(h*e)(n)\}.\tag{2}$$

The second sum is the exact divisor-defect correction. It is NOT optional.
For a=mu, e=0 and the prime-only nonnegative weights give PROOF.md's
nonnegative composite-squarefree expression.

For reciprocal coefficients nu of an elliptic L-series with base
coefficients a_E, the true inversion equation is a_E*nu=delta, NOT
1*nu=delta. Thus

$$e=1*\nu-\delta=(1-a_E)*\nu.$$

A weighted divisor closure involving a_E can preserve inversion, but it is
not the unweighted physical covariance considered here. Its insertion would
change the observable and require a new norm comparison.

## 2. Actual good-prime negative control from the reference curve E_17

The reference family remains the CM CUBIC-twist family associated with the
Sylvester paper, not the original quadratic-twist scope of #738.
At the good prime 7, direct counting on

$$E_{17}:y^2=x^3+17^2/4$$

over F_7 gives #E_17(F_7)=3 and a_7=5. Consequently its arithmetic reciprocal
local factor is

$$1-5T+7T^2,\qquad \nu(1)=1,\quad \nu(7)=-5.$$

Select the single prime in the transport, with the logarithmic GL(2) weight
h(7)=5 log 7. On 7<=x<8, A=h*nu has only its t=7 contribution, and the only
comparable m are 1 and 7. Therefore

$$\boxed{P_{\rm div}\text{ before integration}
 =(1-5)5\log7=-20\log7<0.}\tag{3}$$

This is not numerical evidence about zeros and not a GRH counterexample.
It is an exact local counterexample to the proposed automatic transfer of
DCN26-1. No information about other good or bad coefficients below 8 is
needed: they cannot occur in this selected-prime comparable sector.

For arithmetic center-one energy, integration on [7,8] uses dx/x^3 and
multiplies (3) by

$$1/(2\cdot7^2)-1/(2\cdot8^2)=15/6272.$$

After factoring out log 7, the integrated coefficient is -75/1568.
Using dx/x^2 instead would be a different energy; it would not change the
counterexample's sign, but we do not conflate those normalizations.

Equation (1) gives the same value: d(7)=1-5=-4, (h*d)(7)=5 log7, so the
extra d term is precisely where the native zeta proof ceases to apply.

## 3. What remains usable across families

The near-ratio harmonic envelope in PROOF.md assumes only a finite real
source c with an explicitly known coefficient cap. It can be applied as a
finite algebraic inequality to a coefficient packet satisfying that cap.
It does NOT thereby become an elliptic-L detector: an exact family-specific
kernel and energy consumer must still be supplied. Unit-normalized inverse
coefficients of a degree-two Euler product need not have one absolute cap
independent of n, so K cannot silently be replaced by zeta's cap 3.

The prior logarithmic-defect identity
L_A(N(c))=2e*L_A(c), the exact inert-square local factors, and STC26's
polylogarithmic deletion/restoration remain useful source-faithful tools.
The new contribution here is the explicit correction (1)-(2) and the
actual good-prime failure (3), which prevent a false transfer of the new
zeta sign theorem. No theorem in the earlier family packets is promoted.
