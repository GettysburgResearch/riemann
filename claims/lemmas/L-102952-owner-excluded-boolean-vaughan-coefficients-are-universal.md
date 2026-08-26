# L-102952 — Owner-excluded Boolean Vaughan coefficients are universal

Claim ID: `L-102952`  
Status: **PROVED EXACT RESTRICTION/FUNCTORIALITY THEOREM**  
Created: 2026-08-25  
Depends on: PR #751 `L-106080`; `L-102887--L-102888`  
RH status: **not assumed**

Let `P` be any finite set of owner labels and let `B_P` be the Boolean algebra
of squarefree prime subsets disjoint from `P`. On the full finite prime set,
write `star` for disjoint-support convolution.

For a function `f` on squarefree subsets, let `Res_P f` denote restriction to
subsets disjoint from `P`.

## 1. Restriction commutes with Boolean convolution

If `S cap P` is empty, every disjoint decomposition

\[
S=A\sqcup B
\]

also has `A cap P=B cap P=empty`. Therefore

\[
\boxed{
\operatorname{Res}_P(f\star g)
=(\operatorname{Res}_P f)\star(\operatorname{Res}_P g).
}
\tag{L-102952.1}
\]

The same statement holds for any finite number of Boolean factors.

## 2. The truncation is also local

Let

\[
\mu_U(S)=(-1)^{|S|}\mathbf1_{\prod_{p\in S}p\le U}.
\]

For a subset `S` disjoint from `P`, both its parity and the inequality
`prod(S)<=U` are independent of whether the owner labels are present in the
ambient Boolean cube. Hence

\[
\boxed{
\operatorname{Res}_P\mu_U
=\mu_U^{(P)}.
}
\tag{L-102952.2}
\]

Put

\[
a_U=\varepsilon-\mu_U\star\mathbf1_{\rm sf}.
\]

Equations (L-102952.1)--(L-102952.2) give

\[
\boxed{
\operatorname{Res}_P a_U=a_U^{(P)}.
}
\tag{L-102952.3}
\]

Consequently the balanced coefficient

\[
b_U=a_U\star a_U\star\mu_{\rm sf}
\]

satisfies

\[
\boxed{
 b_U^{(P)}(S)=b_U(S)
 \qquad(S\cap P=\varnothing).
}
\tag{L-102952.4}

## 3. Meaning for the minimum-owner packet

After the horizon-safe owner pair is removed, the Boolean balanced core
coefficient is one universal function of the literal core. Owner exclusion
changes only:

```text
which core supports are allowed;
the physical owner shift;
the source owner and co-owner weights.
```

It does not change the Boolean Vaughan coefficient on an allowed core.

This removes one possible source mismatch in `T-106080`: the balanced
coefficient does not secretly depend on the selected owner pair.

## Scope

Universality of the coefficient is not the same as an owner-indexed physical
restriction theorem. The additive phase attached to a core still contains the
physical owner multiplier, and collapsing different owner fibres is not an
orthogonal operation. The remaining transport is isolated in `R-102875` and
`OICP102960`.
