# R-103300 — Local transition positivity is not an invariant native cone

Claim ID: `R-103300`  
Status: **PROVED EXACT COUNTEREXAMPLE**  
Created: 2026-08-21  
Depends on: `L-103302`  
RH status: **not assumed**

Let

\[
D_5g=(I-V_5)(I-5^{-1}V_5)g
\]

for the normalized cubic `g` of `L-103302`.  The local theorem gives
`D_5g>0` everywhere.

Apply the two carrier-normalized native factors

\[
\mathsf H_{2,1}={I-2^{-1}V_2\over1-2^{-1}},
\qquad
\mathsf H_{3,1}={I-3^{-1}V_3\over1-3^{-1}}.
\]

At the exact physical point `y=25/4` one obtains

\[
\begin{aligned}
(\mathsf H_{2,1}\mathsf H_{3,1}D_5g)(25/4)
={}&-{97\over30}-{\sqrt{30}\over20}
-{7\sqrt6\over120}+{\sqrt3\over10}+{\sqrt2\over8}\\
&+{\sqrt{15}\over5}+{12\sqrt5\over25}
+{9\sqrt{10}\over20}.
\end{aligned}
\tag{R-103300.1}
\]

Directed radical evaluation gives

\[
\boxed{
-0.029166
<
(\mathsf H_{2,1}\mathsf H_{3,1}D_5g)(25/4)
<
-0.029165.
}
\tag{R-103300.2}
\]

Thus the positive local generator leaves its cone after only two native prime
factors.  Any proof of the full homotopy must retain phase/coboundary
cancellation or a same-occurrence energy; it cannot iterate pointwise local
transition positivity.

## Scope

The separator uses the small labels `2` and `3`, which are present in the full
duplicate-67 Euler source.  It refutes a universal invariant cone.  It does not
refute the stronger rough-only statement obtained after freezing all labels
below `67`; that rough invariant-cone statement remains open and, by the fixed-
tail Mellin audit, is itself conclusion-bearing.
