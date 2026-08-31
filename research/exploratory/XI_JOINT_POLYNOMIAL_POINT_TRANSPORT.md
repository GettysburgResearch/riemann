# One source-exact polynomial remainder transport test

Status: bounded POST-QT / POST-JOINT-M3 experiment, design frozen BEFORE
evaluating the new polynomial-remainder criterion. This is not a blind
held-out point: index19 was selected because it had the best failing
joint-M3 ratio in the already observed fixed26-point comparison.

Exact source: QT `530732c5fd7f50364381f8af50e97ce809b674c5`.
Do not modify QT, the all-radius old-criterion obstruction or the joint-M3
packet. This experiment changes the remainder estimate, not source, gauge
or calibration.

## 1. Fixed finite experiment

Use ONLY zero-based QT critical-point index19, its full certified real
interval, lambda_(64), ratio r/y=1/2 and source precision512bits.
Use the inherited512-bit actual Xi coefficient array and its certified
complete16x16 outer-cover bound for R=7/8. These are accepted source
certificates subject to QT independent review, not new point/cover evaluations.

Use exactly N=32 terms of the joint companion remainder and exactly64
equal closed angular arcs covering the circle |w-i*y|=r. Each arc is
represented by outward512-bit sine/cosine intervals. Attempt all64 arcs,
including every failure. No alternate point, ratio, precision, Taylor
order, angular subdivision or source-parameter adjustment occurs.

## 2. Exact joint-polynomial remainder

Let g=f5, a=g(t), c=g''(t), with g'(t)=0 exactly at the inherited critical
point. Keep QT's q,d,y and quadratic P(w)=a+c*w^2/2-i*lambda*c*w.
If v_j=f^(j)(t)/j! are the literal Xi coefficients, then

    R(t+w)-P(w) = sum_(n=2..31) A_n w^n + tail,
    A_2 = -i*lambda*f8(t)/2,
    A_n = [f^(n+5)(t)-i*lambda*f^(n+6)(t)]/n!  (n>=3).

The zero constant and linear terms use the EXACT equation f6(t)=0;
they are not numerical midpoint substitutions. The quadratic f7 terms
cancel algebraically before interval evaluation. Coefficients are evaluated
over the entire unknown-t real interval.

For h>=|w| with h<R and x=h/R, a valid bound for the omitted tail is

    M*x^N * [5!*binom(N+5,5)/(R^5*(1-x)^6)
             +lambda*6!*binom(N+6,6)/(R^6*(1-x)^7)],

where M bounds literal Xi on the inherited outer rectangle around every
admissible t. This follows from Cauchy and the same binomial tail inequality
proved in QT. It bounds both entire companion tails, not f8 alone.

On each of the64 circle arcs, evaluate the polynomial by outward complex
Horner arithmetic and add the uniform scalar tail. Compare its upper
modulus with the uniform positive model margin
|c|*r*(d-r/2). ALL arcs must pass strictly to invoke Rouche.
Otherwise the experiment is UNRESOLVED, not a root nonexistence theorem.

If the full circle passes, separately require the complete known HA
root rectangle to lie inside the transport disc for ALL unknown t,y,r
in their source enclosures. Mere overlap is insufficient. A matched result
then inherits the already separate noncommon-root guards.

## 3. Evidence contract

The first output must retain the exact source identity, complete64 arc
stream, inherited critical/jet/cover identity, interval q/d/y/r, tail,
margin, every strict comparison and full-rectangle matching result.
Positive assertions require source authentication, resource/type guards,
fresh arithmetic replay in both modes and independent review.
Analytic Rouche/Cauchy review remains distinct from machine replay.

This tests one deliberately selected existing source point. It does not
give a cofinal theorem, an independent new zero census, general capture,
innerness, RH or novelty/priority. It is not excluded by the all-radius
obstruction to the DIFFERENT separate-triangle criterion.
