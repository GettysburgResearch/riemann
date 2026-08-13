# R-91305 — Hall positivity of every common corridor channel does not survive heterogeneous branch parameters

Claim ID: `R-91305`  
Status: **EXACT FINITE-WINDOW COUNTEREXAMPLE / SOURCE-TYPING FIREWALL**  
Created: 2026-08-12  
Corrects the possible overreading of: `L-91331`, `L-91332`  
RH status: **unproved**

## 1. Common-parameter theorem retained

For

\[
 w_a(x,n)=\frac{a\sqrt x}{n}-\frac1{\sqrt n},
\]

`L-91331` proves that, for every *common* parameter

\[
 \frac43\le a\le\frac32,
\]

the complete factor-54 parity state has a no-upward Hall transport.  The same
`a` weights every even capacity and every odd demand.

## 2. Heterogeneous worst-case margin

A branchwise mixture may present smaller parameters on even atoms and larger
parameters on odd atoms. The strongest naive uniform Hall margin would be

\[
 \mathcal H^{\rm het}_t(x)
 =\sum_{\substack{e\le t\\\mu(e)=1}}w_{4/3}(x,e)
 -\sum_{\substack{o\le t\\\mu(o)=-1}}w_{3/2}(x,o).
\tag{R-91305.1}
\]

If this were nonnegative, every arbitrary mixture of corridor parameters would
share one common no-upward transport.

## 3. Exact counterexample

Use the certified last reset endpoint

\[
 x_*=\left(\frac{1844367547103}{10^{14}}\right)^{-1}
\]

and the active odd threshold

\[
 t=31.
\]

Directed rational square-root enclosures of denominator `10^80` give

\[
 \boxed{
 \mathcal H^{\rm het}_{31}(x_*)<-\frac32<0.
 }
\tag{R-91305.2}

The retained interval is approximately

\[
 -1.538909794059801
 <\mathcal H^{\rm het}_{31}(x_*)
 <-1.538909794059800.
\]

No floating-point sign decision is used.

## 4. Consequence

The inference

```text
every common channel U_a, 4/3<=a<=3/2, is Hall-positive
    ->
an arbitrary positive mixture of independently parameterized branch states
has one Hall transport
```

is false.

The reason is that Hall cancellation pairs the even and odd masses belonging to
the **same** channel parameter. Forgetting that shared label permits the adverse
assignment

```text
small a on capacities;
large a on demands.
```

Therefore a valid all-generation projection must retain a positive measure on
paired channel states `(a,E_a,O_a)`, or first prove an exact recombination into
one common parameter before applying Hall. Positivity of the four coordinates
`(X_+,X_-,Y_+,Y_-)` alone is insufficient.

## 5. Effect on the uniform regeneration split

The matrix identity in `L-91332`

\[
 D_p=c_pI+R_p
\]

and its scalar corridor calculation remain exact. But the sentence that the
complementary state may automatically be sent through `L-91331` requires the
state to be a canonical paired Möbius channel. It is not valid for an arbitrary
restricted four-state branch.

Thus the typed least-prime subpartition in `L-91332` must include the stronger
property:

\[
 \boxed{
 z_b\text{ is represented by paired even/odd channel measures with one common }a_b.
 }
\]

## 6. Correct frontier

```text
common-a Hall corridor [4/3,3/2]          DIRECTED EXACT
heterogeneous corridor aggregation         FALSE
positive four-state semigroup               EXACT
paired-channel source typing                OPEN / LOAD-BEARING
common-parameter recombination              OPEN
Riemann Hypothesis                          UNPROVEN
```
