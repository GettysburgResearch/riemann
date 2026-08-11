# R-91001 — Every fixed analytic radius at or below three quarters is blind to RH

Claim ID: `R-91001`  
Status: **EXACT METHOD FIREWALL**  
Created: 2026-08-11  
Depends on: `T-91001`  
RH status: **unproved**

Let `z=d+ir` be the centered coordinate of any nontrivial zeta zero relative to a real centre. Since `|d|<1/2`,

\[
 \Re(1-z^2)=1-d^2+r^2>\frac34.
\]

Therefore

\[
\boxed{
 |1-z^2|>\frac34
}
\tag{R-91001.1}
\]

for every zero coordinate, independently of RH. The generating function `A_x(w)` of `T-91001` is consequently holomorphic in

\[
 |w|<\frac34
\]

for every centre `x` in every logically possible zero configuration in the open critical strip.

Hence:

```text
unit-disc/Stieltjes control on one fixed disk |w|<R<=3/4
    cannot detect any off-line zero;

control on one fixed R<1
    excludes only depths y>sqrt(1-R);

full RH requires a cofinal radius R->1.
```

This is the generating-function counterpart of the finite-bandwidth and fixed-nonlinear-degree firewalls elsewhere in the repository. It does not refute the complete unit-disc criterion; it proves that the radial quantifier is load-bearing.