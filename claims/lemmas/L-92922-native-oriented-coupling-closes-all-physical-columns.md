# L-92922 — The native-oriented coupling closes every physical column and rejects the rough-lift mutation

Claim ID: `L-92922`  
Status: **CANDIDATE-COMPLETE ALL-COLUMN THEOREM ON FROZEN ANALYTIC ESTIMATES — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Primary inputs: `L-91733`, `L-91754`, terminal omission, positive radix-four inverse, `L-91852`, `L-92921`, `R-92920`  
RH status: **unproved**

## 1. Native ideal reference

Let `d_X^ideal` be the output marginal of the oriented coupling before the one
global quantizer and scalar thinning.  By `L-92921`, its typed reference is the
native datum rather than the `P_61` rough lift.

Use the complete tagged cells

\[
 K+2\le n\le X-10003,
 \qquad
 K=\left\lfloor X/67\right\rfloor+1,
\]

and one label-blind martingale quantizer.  Let `e_X` be the signed retained-cell,
collar and terminal observation error, and let `u_X` be the positive unused
native capacity from common thinning and literal bottom/top omission.

## 2. Nonterminal columns

For every `2<=q<=X/4`, the frozen all-column estimate gives

\[
 \frac{|e_X(q)|}{\Omega_X(q)}
 <\frac{129}{\sqrt K}.
\tag{L-92922.1}
\]

With

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130},
\]

one obtains

\[
 \Xi(d_X;q)
 <\tau_K\left(1+\frac{129}{\sqrt K}\right)
  \Omega_X(q)
 =\frac{\sqrt K+129}{\sqrt K+130}\Omega_X(q)
 <\Omega_X(q).
\tag{L-92922.2}
\]

This includes the formerly delicate range `2<=q<K`.

## 3. Terminal and ordinary columns

The fixed top omission dominates the terminal comparison by

\[
 5033X^{-3/2}-4452X^{-3/2}
 =581X^{-3/2}>0.
\tag{L-92922.3}
\]

Above retained support the physical response is zero.  Therefore

\[
 \boxed{
 r_X(q)=\Omega_X(q)-\Xi(d_X;q)\ge0
 \qquad(q\ge2).
 }
\tag{L-92922.4}
\]

Positive radix-four inversion gives simultaneously

\[
 \boxed{C_{d_X}(q)\le w_X(q)\qquad(q\ge2).}
\tag{L-92922.5}
\]

The signed finite/continuum comparison remains an observation vector; it is not
called positive source.

## 4. The `q=2` discriminator

The native-oriented branch satisfies (L-92922.4).  If the orientation labels
are deleted and the ideal marginal becomes the full rough lift, then at
`X=10^16` `R-92920` proves

\[
 \frac{\Xi(d_X;2)-\Omega_X(2)}{\Omega_X(2)}
 >\frac{109}{1200}.
\tag{L-92922.6}
\]

Thus `q=2` is a fail-closed normalization test, not a heuristic.  The same
certificate cannot pass both branches.

## 5. Source ownership

Every source occurrence has exactly one of the following owners:

```text
Hall edge;
Hall residual/current bonus;
first-owner oriented actual child;
literal bottom/top discard;
common thinning discard;
one quantized physical state.
```

The signed comparison has one correction owner but no arithmetic source owner.
No root operation is copied to an internal child.

## 6. Boundary

```text
precomparison normalization                   native / L-92921
rough-lift normalization                      rejected at q=2
all nonterminal columns                       strict
terminal annulus                              strict margin 581 X^-3/2
ordinary columns                              positive inverse
source ownership                              explicit
exported recursion                            empty
auxiliary Schur port                          zero
native cost                                   next lemma
Riemann Hypothesis                            unproved
```
