# L-103300 — Critical-carrier normalization exposes the exact balanced homotopy generator

Claim ID: `L-103300`  
Status: **PROVED EXACT FINITE OPERATOR THEOREM**  
Created: 2026-08-21  
Depends on: PR #695 `L-100701--L-100704`  
RH status: **not assumed**

Let

\[
P(X)=\sqrt X,
\qquad
(V_pg)(X)=g(X/p),
\qquad
a_p=p^{-1}.
\]

PR #695 uses the balanced local factor

\[
H_{p,t}=I-tp^{-1/2}U_p-(1-t)p^{-1}U_{p^2},
\qquad 0\le t\le1.
\]

Since

\[
U_p(Pg)=p^{-1/2}PV_pg,
\qquad
U_{p^2}(Pg)=p^{-1}PV_p^2g,
\]

one has

\[
\boxed{
H_{p,t}(Pg)=P N_{p,t}g,
\qquad
N_{p,t}=I-ta_pV_p-(1-t)a_p^2V_p^2.
}
\tag{L-103300.1}
\]

The eigenvalue on the critical carrier is

\[
\boxed{
h_p(t)=1-ta_p-(1-t)a_p^2
=(1-a_p)(1+a_p(1-t))>0.
}
\tag{L-103300.2}
\]

Define the carrier-normalized factor

\[
\mathsf H_{p,t}=h_p(t)^{-1}N_{p,t}
\tag{L-103300.3}
\]

and the normalized balanced transition

\[
\mathsf T_p
=\frac{a_pV_p-a_p^2V_p^2}{a_p-a_p^2}
=\frac{V_p(I-a_pV_p)}{1-a_p}.
\tag{L-103300.4}
\]

A direct coefficient comparison gives

\[
\boxed{
\mathsf H_{p,t}-\mathsf T_p
=\frac{(I-V_p)(I-a_pV_p)}{h_p(t)}.
}
\tag{L-103300.5}
\]

Differentiating (L-103300.3) and using
`h_p'(t)=-a_p(1-a_p)` gives

\[
\boxed{
\partial_t\mathsf H_{p,t}
=\frac{a_p(1-a_p)}{h_p(t)^2}
 (I-V_p)(I-a_pV_p).
}
\tag{L-103300.6}
\]

Equivalently,

\[
\boxed{
\partial_t\mathsf H_{p,t}
=\frac{a_p(1-a_p)}{h_p(t)}
 (\mathsf H_{p,t}-\mathsf T_p).
}
\tag{L-103300.7}
\]

Thus, after the exact critical carrier is removed, every homotopy derivative
contains the cancellation factor `I-V_p`.  It annihilates the neutral mode
before any inequality is applied.

For a finite labelled prime set `Lambda`, including the second labelled copy of
`67`, put

\[
\mathsf H_{\Lambda,t}=\prod_{p\in\Lambda}\mathsf H_{p,t}.
\]

Commutativity gives the exact finite generator

\[
\boxed{
\partial_t\mathsf H_{\Lambda,t}
=\sum_{p\in\Lambda}
\frac{a_p(1-a_p)}{h_p(t)^2}
(I-V_p)(I-a_pV_p)
\prod_{q\ne p}\mathsf H_{q,t}.
}
\tag{L-103300.8}

No alternating inverse, endpoint-dependent Mellin multiplier, or post-hoc
carrier subtraction is used.  This is the normalized source identity behind
the balanced completed-minus-transition cancellation of PR #695.
