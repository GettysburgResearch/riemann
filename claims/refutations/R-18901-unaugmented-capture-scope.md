# R-18901 — A positive augmented complement does not prove unaugmented capture

Claim ID: `R-18901`  
Title: Canonical finite augmentation closes the complement while leaving a genuinely negative finite block  
Status: `PROVED EXACT SCOPE CORRECTION`  
Authoring agent: `gpt56-03-n`  
Created: 2026-07-31  
Dependencies: none  
Scope: interpretation of `L-18901/T-18901`

## Exact model

On `R^4`, let

\[
 D=\operatorname{diag}\left(0,\frac52,\frac32,\frac14\right),
 \qquad
 g=2,
\]

and put

\[
 A=gI-D
 =
 \operatorname{diag}\left(
 2,-\frac12,\frac12,\frac74
 \right).
\]

Take the initial packet

\[
 U_0=\operatorname{span}\{e_1\}
\]

and request the floor

\[
 \Gamma=1.
\]

Then

\[
 A\succeq gI-D
\]

with equality, but

\[
 A|_{U_0^\perp}\not\succeq I
\]

because

\[
 \langle Ae_2,e_2\rangle=-\frac12.
\]

The danger threshold is

\[
 g-\Gamma=1.
\]

The compressed deficit has exactly two eigenvalues above this threshold,
`5/2` and `3/2`. Hence the canonical augmentation is

\[
 W=\operatorname{span}\{e_2,e_3\},
\]

and

\[
 U=U_0\oplus W
 =\operatorname{span}\{e_1,e_2,e_3\}.
\]

Now

\[
 U^\perp=\operatorname{span}\{e_4\}
\]

and

\[
 \boxed{
 A|_{U^\perp}
 =\frac74I
 \succeq I.
 }
\]

Thus:

1. the unaugmented capture claim is false;
2. the canonically augmented complement floor is exact;
3. the full operator remains indefinite because the negative direction has
   merely been moved into the finite packet.

## Consequence

One may not infer RH, global positivity, or radical capture from

\[
 A|_{U^\perp}\succeq\Gamma I
\]

unless the finite block `U` is also controlled. The complement theorem and the
finite-kernel theorem are logically separate.

`X-18901` replays this model using exact rational arithmetic.
