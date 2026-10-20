# Independent review of the complete signed second origin

Reviewer: `/root/repo_routes_audit`, 20 October 2026.

Reviewed file: `SIGNED_SECOND_ORIGIN.md`, SHA-256
`34f88db8c28280ff45104cd4e86c7465112cc118babd6a3afa408757a4323725`.

Primary source checked: Liu, arXiv:2610.26835v1, Lemmas 12.9–12.10,
the exact first transform (12.2), and §§12.7.1–12.7.3, printed pp.72–78.
PDF SHA-256:
`5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`.
The source is an upstream analytic input, not a theorem independently
reproved in this review.

**Finding:** no blocking error found in the stated finite identities,
phase restoration, or the scope of the width calculation. The note
correctly stops short of an improved moment or numerical boundary.

## Normalizations and complete moduli

I reconstructed (1)–(4) using the full, zero-extended Gauss sums.
The unnormalized sum of `G_xi(r,h)` over `h mod r` is
`sqrt(Nr) xi(0)`. Because `(r,uv)=1`, CRT splits the complete sum
modulo `ruv` into that factor and the correlation modulo `uv`.
The prefactor `1/sqrt(Nr Nu Nv)` then leaves exactly
`xi(0) F(u,v;0)`. This agrees with the source's normalization of
`F(u,v;0)=1_{u=v} phi_F(u)` even when u,v share primes or contain
imprimitive powers. No primitive-conductor substitution is made.

For nonunit r, the retained zero at the additive origin makes xi(0)=0.
For r=1, the complete ideal Möbius sum on the remaining diagonal is
`sum_{s|u} mu_F(s)=1_{u=1}`. The surviving unit Euler factor is
`phi_F(1)=1`. This verifies (3), including its exact constant.

## CRT phases and the common child presentation

I independently expanded the variable
`x=uv x_r+rv x_u+ru x_v`. Its character factor is exactly
`C=xi(uv) chi_u(rv) conjugate(chi_v(ru))`; each cross argument is a
unit on the stated genuine locus. The positive finite Fourier
transform has the factor `C sqrt(Nr Nu Nv)`, giving (6).
The inverse transform therefore carries `C^(-1)` and the displayed
`1/sqrt(Nr Nu Nv)` normalization in (7).

Conjugating the v Gauss sum reverses its additive sign. The source's
`chi_v(-1)=1` identifies it with the displayed orientation; it does
not authorize discarding an unrelated root-number phase.

From the source presentations
`tau_C=tau chi_bullet(er) xi_r` and
`tau_D=tau chi_bullet(er) conjugate(xi_r)`, their product supplies
`xi_r(u) xi_r(v)` and the exact r-parts of C. Symmetric reciprocity
cancels `chi_u(v) conjugate(chi_v(u))`. Multiplication by (7) thus
gives the single child presentation `tau(n) chi_n(ej)` on both sides,
with xi_r(j) left as its bounded row phase, including its zeros.
These steps agree with (8)–(9). The note correctly limits that simple
CRT formula to genuine coprime columns; its Möbius projector must be
restored before it is used on an artificial extension.

## Convolution, row scale, and limits of the conclusion

Before separate norm bounds, the full coefficient and kernel in the
source stipulated extension are independent of the divisor label used
to express `1_{(u,v)=1}`. Recombining all exact divisor allocations
therefore preserves the finite cancellation. Applying absolute values
to allocations or changing the row tests separately would not.

The first dual norm scale is `T=Ne Nr Nu Nv/H`. Transforming it back
without a different enlargement gives `H/Ne`; the complete column
presentation has support charge `q+log_Z Ne`. Their row-plus-support
width is `m-log_Z Ne+q+log_Z Ne=M`. The r-part is an exact retained
row phase, not a deleted character factor. This is a scale identity,
not a claim that an indefinite row weight can be removed positively.

The final caution is material. The signed coprime form has opposite
eigenvalue signs already on two distinct coprime nonunit columns in
the common-presentation r=1 sector. Source positivity and row
enlargement cannot be imported solely from its vanishing second
origin. The separately reviewed alias calculation identifies the
compensating Fourier frequencies of exact sixth-power graph
amplification. Neither finite identity supplies the missing strict
width decrease or the proposed sixth-moment estimate.

This is a scoped team mathematical review of the exact file above.
It is not external referee approval, a formal proof-system check, or
a review of all upstream source theorems.
