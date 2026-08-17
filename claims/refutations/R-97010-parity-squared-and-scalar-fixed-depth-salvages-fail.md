# R-97010 — Parity-squared, grouped-annular, and scalar fixed-depth salvages fail

Claim ID: `R-97010`  
Status: **PROVED FROM PR #561 + EXACT LINEAR INTERFACE**  
Depends on: `L-97010`; PR #561 `R-96501`  
RH status: **unproved**

For fixed row `q>=2`, let `B_{L,X}(q)` be the signed current block obtained by
stopping every rough history at depth `L`, exactly as in PR #561. That PR proves

\[
\frac{B_{L,X}(q)}{\sqrt X}
=a_q\frac{(-1)^{L-1}}{(L-1)!}(\log\log X)^{L-1}
+O_{L,q}((\log\log X)^{L-2}),
\qquad a_q>0.
\tag{R-97010.1}
\]

Hence an even depth restores canonical parity on the recursive frontier only by
making the current block eventually negative. An odd depth leaves the current
leading sign positive only by exporting reversed recursive parity.

The complete-color grouping used in PR #556 is linear and diagonal in the
parity coordinate. By `L-97010`, it cannot alter (R-97010.1). Likewise the scalar

\[
\mathcal R_X=5c_X(2)+3c_X(3)
\]

of PR #559 preserves the same history character.

The depth-two failure is already explicit. PR #561 certifies directed intervals

\[
B_{2,200000}(2)<-11,
\qquad
B_{2,200000}(3)<-2.
\]

Using the retained upper endpoints gives the stronger scalar inequality

\[
\boxed{
5B_{2,200000}(2)+3B_{2,200000}(3)
<-62.7181678185658877324.
}
\tag{R-97010.2}
\]

Therefore none of the following is a valid closure mechanism:

1. observe every rough history after two levels;
2. group the `P_61` colors and then observe every two-level block;
3. apply the `5:3` scalar and then observe every two-level block;
4. replace depth two by any other fixed even depth.

This refutes fixed-depth positive decompositions, not the desired inequalities
`c_X(2)>=0`, `c_X(3)>=0`, or `mathcal R_X>=0`. Any surviving factor-67 proof
must use cancellation across unbounded rough depths before signed observation.
