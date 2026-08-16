# L-94122 — The projectively glued source gives one direct native row with deficit below 3457

Claim ID: `L-94122`  
Status: **PROPOSED COMPLETE COMPOSITION ON FROZEN DIRECTED ANALYTIC INPUTS**  
Created: 2026-08-16  
Inputs: `L-93920--L-93922` at `4275fe97aa5ba885210abb6296c7048386e5909d`; `L-94120--L-94121`  
RH status: **unproved pending review**

Let `X>=10^12`,

\[
K=\lfloor X/67\rfloor+1,
\qquad
W_X=6\lceil\sqrt K\rceil+4.
\]

Use the moving anchored/bulk partition of PR #513.  On the anchored cells,
replace the formerly asserted leaf sum by the projective source realization of
`L-94121`; call its finite row `d_(X,A)`.  Its exact source marginal gives

\[
d_{X,A}=c_{X,A}\ge0.
\]

On complete outer cells, use the direct Volterra row

\[
d_{X,I}
 =\sum_{m\in I_X}\int_m^{m+1}
  \frac{2L(X/s)}s p_s\,ds\ge0,
\]

where `1<X/s<67` and the directed outer theorem gives `L(X/s)>159/500`.
Define one row before any comparison:

\[
d_X^0=d_{X,A}+d_{X,I}\ge0.
\]

The exact hybrid identity is

\[
c_X=d_X^0+\mathcal R E_X^I,
\]

with `E_X^I` a signed retained-cell defect, not source.  Apply the single
thinning

\[
\tau_K=\frac{\sqrt K}{\sqrt K+24}
\]

to the total row.  Ordinary `q` and `4q` are evaluated on this same row and
only then is

\[
\Xi(q)=C(q)-2C(4q)
\]

formed.

The moving-top-anchor estimate covers every `q>=2`, including `q<K` and terminal
columns, and gives

\[
C_{d_X}(q)\le w_X(q),
\qquad
\Xi_{d_X}(q)\le\Omega_X(q).
\]

The native sparse-dual ledger is unchanged:

```text
one common thinning                 <3456
one signed retained-cell mismatch      <1
port / recursive correction             0
------------------------------------------
native Y4 deficit                    <3457
```

Thus

\[
0\le J_\Lambda(X)-\mathcal H(d_X)<3457=o(\log^2X).
\tag{L-94122.1}
\]

No rough child is observed separately, no full child capacity is substituted,
no signed error is called source, and no `J_Lambda-4sqrt(X)` estimate is used.
