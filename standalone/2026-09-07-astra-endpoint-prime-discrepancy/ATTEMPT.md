# End-to-end attempt: what closes and what does not

Status: the unconditional RH proof is NOT complete. No reviewer is being
asked to supply an unstated argument. Component proofs are in PROOF.md.

## The attempted chain

1. Recover the analytic first-prime derivative from its real boundary data.
2. Control its full causal norm at exactly Re(s)=1/2.
3. Use the literal factorial source to construct a domain vector agreeing
   with the derivative target on the complete arithmetic horizon.
4. Compare its future energy with the cost forced by any hypothetical zero.
5. Prove a subpower upper bound for the actual cost.

Steps 1-4 are supplied, with an explicit bandwidth price and no inward shift.
Step 5 is NOT supplied. The new positive-square formula gives a source-exact
quantity to estimate, but it does not estimate that quantity from above.

## What genuinely changed

The preceding entropy-to-domain theorem needed a fixed positive inward shift
sigma. Its lower bound charged every exponent nu<beta-1/2. Taking sigma=0 in
that theorem is invalid. Here a one-sided smooth Fourier multiplier reconstructs
the analytic derivative only from the finite first-prime band; the infinite
higher-prime-power tail is bounded separately. The result is a bound in the
original L2 metric at the actual critical line, charging beta-1/2 itself with
only a (log X)^(3/2) denominator. The domain identification is literal, not a
new metric, an isometric extension by declaration, or a zero-dependent source.

The physical phase correlations can also be eliminated from the notation
WITHOUT replacing the measure: their complete cosine Gram has the factorization
in PROOF.md (23). It yields the square of a signed weighted prime-discrepancy
tail. Independent prime phases, diagonal domination and a generic martingale
assumption are not used. The missing information remains genuinely arithmetic.

## The attempted upper estimate

Put Q(X)=R_X(1)^2+integral_1^X x R_X(x)^2 dx, with R_X exactly as in (20).
The proposed completion would need Q(X_j)=X_j^o(1) on an unbounded sequence,
or an alternative direct subpower bound for E or the parent's signed work.
Positive Q alone is irrelevant to that upper bound.

Stieltjes integration against the actual discrepancy Delta(x)=pi(x)-li_2(x)
retains BOTH endpoints and the entire cross contribution. The classical
unconditional PNT only pays

    Q(X) << 1+X exp(-c sqrt(log X)).

Even with an unspecified arbitrarily small positive c replaced by a stronger
known classical constant, the power of X does not disappear. Applying
Cauchy--Schwarz before the signed cancellation, using a mean-square theorem
for unrelated arithmetic progressions, or treating the actual phase Gram as
a product-measure Gram does not supply the missing bound.

Under RH, |Delta(x)|<<sqrt(x)log x does pay Q(X)<<log^3 X. This yields a
conditional improvement E(X)<<log^(3/2) X, NOT an unconditional theorem at
that growth rate. It is kept separate from the forward argument. No new
prime-counting error estimate is claimed.

## A precise test of the hypotheses used by that unsuccessful estimate

Here is a continuous control, NOT the ordinary primes, not an Euler product,
and not a counterexample to RH. On x>=2 let a positive counting density be

    dN(x)=dx/log x + eta x^(beta-1)dx,
    eta>0, 1/2<beta<1.

Its discrepancy from the continuum main term is eta(x^beta-2^beta)/beta.
It satisfies a classical-shaped bound O(x exp(-c sqrt(log x))) for any fixed
c>0, after adjusting the constant. Nevertheless its weighted tail is

    R_X(x)=eta/(3/2-beta) [x^(beta-3/2)-X^(beta-3/2)], x>=2,

and the SAME physical positive-square calculation gives

    Q(X) ~ [2eta^2/(4beta^2-1)] X^(2beta-1).

Indeed substitute x=Xv in integral x R_X(x)^2 dx. The finite contribution
from [1,2] is bounded; the remaining integral is
eta^2 X^(2beta-1)/(3/2-beta)^2 times

    integral_0^1 v(v^(beta-3/2)-1)^2dv
      =1/(2beta-1)-2/(beta+1/2)+1/2.

This simplifies to the stated positive constant. Dominated convergence is
legitimate because 2beta-2>-1. Thus positivity of a counting measure plus
that PNT-shaped error bound does not logically imply the desired subpower
square estimate. The test does not rule out using additional exact properties
of the ordinary prime measure; those would be the new proof ingredient.

## What to send to an independent reviewer

This packet is a COMPONENT submission, not a full proposed RH proof.
Review (i) the one-sided multiplier and every normalization in (11)-(14),
(ii) the separate higher-power bound, (iii) the literal critical-line causal
identification, (iv) the full multiplicity tail test, and (v) the complete
signed measure factorization (21). In particular the positive-square formula
must not be reduced to a prime diagonal, and its conditional upper bound
must not be fed into the unconditional implication.

The smallest unproved completion statement is precisely (OPEN) in Section 7.
No numerical or finite algebra check in this directory supplies it. The
current contribution closes a domain-of-estimate issue, not the full-domain
RH assertion. No unconditional new zero-free region is claimed.
