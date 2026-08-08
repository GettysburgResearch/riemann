# L-30503 — Eta-resolvent recombination is exactly the unique central producer

Claim ID: `L-30503`  
Title: Summing every unshifted eta stage before taking negative parts yields one explicit central-only flow, and that flow is exactly the canonical central-halving producer  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-30502`; PR #272 central trees; PR #247 central producer  
Scope: arbitrary finite target; no positivity or RH assertion

## 1. Finite eta resolvent

Let `w` be any finite target supported on `2,...,X`. Define the unshifted eta operator

\[
(\mathcal Uw)(q)
=\sum_{m\ge2}(-1)^m w(mq),
\tag{L-30503.1}
\]

with terms outside the endpoint omitted. Since `mathcal U` halves support, the finite Neumann sum

\[
\boxed{
R_w=\sum_{j\ge0}\mathcal U^jw
}
\tag{L-30503.2}
\]

terminates and satisfies

\[
\boxed{
(I-\mathcal U)R_w=w.
}
\tag{L-30503.3}

This is the finite reciprocal-eta resolvent.

## 2. One recombined flow

For a finite sequence `r`, let

\[
\operatorname{Cen}(r)
=\sum_{n=2}^{X}[r(n)-r(n+1)]
[n,\lfloor n/2\rfloor]
\tag{L-30503.4}
\]

and define

\[
\sigma_r(m)=r(2m-1)-r(2m),
\tag{L-30503.5}
\]

\[
\Phi(r)=\sum_m\sigma_r(m)(T_m-T_{m-1}).
\tag{L-30503.6}
\]

`L-30502` proves

\[
L(\operatorname{Cen}(r)+\Phi(r))=r-\mathcal Ur.
\tag{L-30503.7}
\]

Applying this to `R_w` and using (L-30503.3) gives the exact flow

\[
\boxed{
D_w^{\eta}
=\operatorname{Cen}(R_w)+\Phi(R_w),
\qquad
L(D_w^{\eta})=w.
}
\tag{L-30503.8}

By linearity, this is also the complete recombination of all stage flows from `L-30502`:

\[
\boxed{
D_w^{\eta}
=\sum_{j\ge0}
\left[
\operatorname{Cen}(\mathcal U^jw)
+\Phi(\mathcal U^jw)
\right].
}
\tag{L-30503.9}

Thus all repeated central and adjacent-tree destinations may be combined before a negative part is taken.

## 3. The flow uses only central edges

Every edge in `Cen(r)` is the canonical central split

\[
h_n=[n,\lfloor n/2\rfloor].
\]

Every adjacent commutator

\[
T_m-T_{m-1}
\]

is a signed combination of the same canonical central edges. Consequently

\[
\boxed{
D_w^{\eta}\in\operatorname{span}\{h_2,\ldots,h_X\}.
}
\tag{L-30503.10}

The divergences of the `h_n` are triangular and form a basis of the size-zero node space. Therefore there is exactly one central-only split flow with carry target `w`.

It follows that

\[
\boxed{
D_w^{\eta}=D_w^{\rm central},
}
\tag{L-30503.11}

where `D_w^(central)` is the descending pure-central producer of PR #247.

## 4. Explicit descending recurrence

Write

\[
D_w^{\rm central}
=\sum_{n=2}^{X}d_w(n)h_n.
\]

If `r^w` is the exact node divergence of the target, triangular descent gives

\[
\boxed{
 d_w(n)
 =r^w(n)
 +2d_w(2n)
 +d_w(2n-1)
 +d_w(2n+1),
}
\tag{L-30503.12]

with terms outside the endpoint zero. The closing bracket in the tag is typographical only.

Equation (L-30503.11) provides a second exact formula for the same coefficients through the reciprocal-eta resolvent `R_w`.

## 5. Consequence for proof search

The shift-terminalized construction is valuable because it preserves the correct analytic cancellation and gives an exact finite source map. But after complete stage recombination it does not evade the pure-central positivity problem.

In particular:

```text
pointwise nonnegativity of D_w^eta
<=> pointwise nonnegativity of the pure central producer;

negative capacity of D_w^eta
= negative capacity of that same central producer.
```

Any genuine improvement must use a noncentral Pascal-cycle deformation before the negative part, or prove the subpower negative debt of the central producer itself.

## 6. Proof boundary

Closed exactly:

1. finite eta resolvent identity;
2. all-stage flow recombination;
3. central-edge support;
4. equality with the unique central producer;
5. descending coefficient recurrence.

Not proved:

1. positivity or subpower debt of the central producer;
2. a cycle repair;
3. RH.