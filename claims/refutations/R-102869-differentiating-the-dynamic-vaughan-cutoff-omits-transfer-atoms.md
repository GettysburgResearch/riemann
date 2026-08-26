# R-102869 — Differentiating the dynamic Vaughan cutoff omits transfer atoms

Claim ID: `R-102869`  
Status: **PROVED EXACT MOVING-SOURCE FIREWALL**  
Created: 2026-08-24  
Depends on: corrected `L-102881`  
RH status: **unproved**

The pointwise stopped Vaughan decomposition uses

\[
U(Y)=\lfloor Y^{1/6}\rfloor.
\]

For a fixed external cutoff `U`, differentiation of the kernel gives the corresponding `K_L` channel.  Along the dynamic schedule, however,

\[
D[T_R(Y;U(Y))]
\ne T_K(Y;U(Y))
\]

and

\[
D[B_R(Y;U(Y))]
\ne B_K(Y;U(Y))
\]

separately.

At every jump `U-1 -> U`, the two channels exchange the exact atom

\[
\Delta_U T_R(U^6)\,\delta_{\log U^6}.
\]

Their transfer atoms have opposite signs and cancel only after the Type-I and Type-II rows are recombined:

\[
\Delta_U B_R=-\Delta_U T_R.
\]

Thus the complete derivative identity survives, while the two separate dynamic derivative identities are false.

Any proof which takes an absolute value, negative part, regional norm or reserve charge before this recombination duplicates or loses the cutoff-transfer source.
