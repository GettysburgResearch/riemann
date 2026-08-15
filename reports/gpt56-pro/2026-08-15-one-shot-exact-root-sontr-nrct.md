# One-shot exact-root SONTR/NRCT closure

PR #486 correctly recognized that the factor-67 arithmetic has a one-shot
implementation: every labelled causal child can remain inside one globally
quantized positive parent row. This successor hardens that implementation.

The two approximation layers are removed. Hall is a finite measurable map and
is integrated exactly; endpoint support is chosen as a union of complete
integer cells. The root construction therefore uses no activation collars and
no Hall mesh.

The auxiliary root port is also removed. The endpoint criterion is a direct
component-row packing problem, and every used generator is a physical
nonnegative row. Mismatch/collar/terminal objects are capacity comparisons,
not signed correction rows.

The exact positive dual prices the entire external slack:

```text
square-root thinning   <12012
nonterminal errors     <4 for X>=1e12
terminal comparison    <48972
omissions              <1
port/base               0
--------------------------------
total                  <61000
```

All causal children are internal colours, so no recursion remains. The complete
native gap is uniformly bounded and the prime-square endpoint theorem supplies
the proposed RH implication.
