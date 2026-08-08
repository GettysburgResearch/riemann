# Addendum — cofinal finite crossing closes; endpoint domination is the sole hinge

Date: 2026-08-08  
Agent: `gpt56-pro`  
PR: #291  
Status: **one explicit RH-bearing theorem remains; RH unproved**

## New closure

The first draft reduced finite shell-crossing to a bounded transition collar and finitely many low coordinates. `L-27904` now closes those gates cofinally.

The proof combines:

```text
normalized continuum moat at theta=0;
strictly positive Hurwitz-zeta limits for every fixed q;
uniform O(q^-3/2) floor error;
strict negative derivative in quotient cell 7;
negative continuum moats in cells 2,...,6;
an elementary exact outer-cell inequality.
```

Therefore every sufficiently large finite dyadic shell residual has exactly one sign transition and

```text
q_*(X)/X -> 0.1408520350138...
```

without using a finite scan.

## Consequence

The canonical WSTS charge is now exactly

```text
B_X=[Delta_X-Delta_floor(X/2)]_+,
```

where

```text
Delta_X=J_(P,X)(b_X^(0))-P_X.
```

There is no longer a family of tail cuts and no finite crossing theorem left open.

## Sole remaining theorem

```text
EPD:
partial_(log X)Delta_X
=sum_(p<=X)log(p)[v_p(dot b_X)-p^(-1/2)]
<=0.
```

The preferred construction remains `ESC`, the endpoint squarefree collector. A reflected boundary proof is the alternative.

## Exact status

```text
continuum one-crossing                 proposed complete
uniform shell error                    proposed complete
cofinal finite shell-crossing          proposed complete
WSTS tail collapse                     proposed complete
EPD / ESC                              open / RH-bearing
EPD -> zero WSTS debt -> RH            proposed complete
RH                                     unproved
```
