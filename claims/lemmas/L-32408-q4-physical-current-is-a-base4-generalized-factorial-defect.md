# L-32408 — Scope correction: the base-4 generalized factorial is an extra-floor transform, not the physical current

Claim ID: `L-32408`  
Status: **SUPERSEDED AS A PHYSICAL-CURRENT CLAIM; SECONDARY EXACT TRANSFORM RETAINED**

The original version of this file applied a divisor/floor transform to

\[
 c_4=e_4*\Lambda_4,
\]

and called the resulting carry row the `Q=4` physical current. That typing is incorrect. The pole-preserving physical current `E_4L_4N_theta` uses `c_4` against the centered-interval kernel; at an integer split its value is the prefix defect

\[
 G_4(n)-G_4(j)-G_4(n-j),
 \qquad G_4(N)=\sum_{m\le N}c_4(m),
\]

as corrected in `L-32407`.

The extra-floor transform

\[
 A_4(N)=\sum_qc_4(q)\lfloor N/q\rfloor
\]

is still a valid secondary arithmetic object. For it, the previously derived identities remain exact:

\[
 A_4(N)=\log(N!)-3\sum_{r\ge1}\log(\lfloor N/4^r\rfloor!)+3\log4\sum_{r\ge1}r\lfloor N/4^r\rfloor,
\]

and, with

\[
 \mathfrak F_4(N)=N!\prod_{r\ge1}\frac{4^{3r\lfloor N/4^r\rfloor}}{(\lfloor N/4^r\rfloor!)^3},
\]

\[
 A_4(N)=\log\mathfrak F_4(N),
\]

\[
 \mathfrak F_4(N)=\mathfrak F_4(\lfloor N/4\rfloor)
 \frac{N!}{(\lfloor N/4\rfloor!)^4}
 4^{4\lfloor N/4\rfloor-s_4(\lfloor N/4\rfloor)}.
\]

This secondary transform inserts an additional zeta factor in Dirichlet series and therefore cancels the nontrivial zeta-zero poles. It is not part of the RH-sensitive physical proof spine.

The corrected physical collar is given separately after `L-32407`; no reviewer should use this file as a physical-current identity.
