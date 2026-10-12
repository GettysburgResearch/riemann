# Independent review of the complete infinite mixed cone

Verdict: ACCEPT MM1–MM4 at `../../operators/FINITE_CENSUS_MIXED_MOMENT_CONE.md`,
SHA `b904361d5af54885d6cd9bb1cfd730f11fdd05e6a0f2c1557328a92b5a40f166`,
and its checker SHA
`d8a34554b671de540d7e326f0b354a8261698bdb789c1483af9b13e8aaa90973`.
I independently read the full proof, code and imported head/count source
interfaces, then directly ran the exact checker normally and under -O.
The preserved `infinite_mixed_cone_normal.json` and optimized receipt are
byte-identical to the owner receipt, SHA
`bffb559967304c3ccb46c6a185d03bed376be5a46dd84394852c68bea39b427f`.
This is a rational-guard replay, not a root, moment or heat primitive run.

The exact finite binomial identity preserves every source occurrence:
`D_(n,j)=c^n sum m*(rho^2+A^2)^j/(rho^2+t^2)^(n+j+1)`.
For t512, A1/2 and every unknown gamma>5419, triangle and real-part bounds
give `|(rho^2+A^2)/(rho^2+t^2)|<=1`. Complete source counting, including
multiplicity and both positive-real conjugates, consequently gives the
whole absolute tail bound

\[
 T_n\le\frac{n+1}{n}Q^{-n}-cQ^{-n-1}<2Q^{-n},\qquad n\ge1.
\]

I checked the Stieltjes derivative, both endpoints, the exact antiderivative
and n=1. The closed head pays any atom at the cutoff. The upper endpoint
vanishes using the actual theta/Jensen `N(x)<=x^2` theorem. This theorem
does not call or import a historical zero-count routine.

One authenticated real root in (14,15) supplies the strictly positive
head term `a^j/B^(n+j+1)`; all other complete-head terms are nonnegative.
The exact rational criterion `2B(B/Q)^n(B/a)^j<1` therefore proves a whole
actual-source mixed sign. The three strict/base inequalities and forty
remainder inequalities imply every pair `40n>=61j+120` by writing j=40q+h.
No sample over an infinite index range replaces this induction.

All nine direct source hashes in the receipt were checked against current
files. The previous native count-free complete real5419 head and the
complete analytic theta/Jensen count are explicit imports; the checker
authenticates their frozen source contracts rather than proving the
infinite analytic arguments itself. Simplicity is unnecessary for this
cone theorem.

This is an infinite subset of the universal mixed criterion. The pairs
outside it remain open. It neither proves all mixed signs nor supplies
cofinal native progress, complete heat monotonicity or RH.
