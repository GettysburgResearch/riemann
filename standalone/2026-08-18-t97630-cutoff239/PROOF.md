# Proof extract

**Evidence status:** reconstructed candidate extract. The unavailable original
full finite sweep and analytic-tail proof are not implemented by the included
lightweight C++ replay.

The corrected finite theorem is
\[
F(x)\ge0\quad(1\le x<239),
\]
\[
\frac1{40}M(x)\le F(x)\le\frac18M(x)\quad(x\ge239).
\]

Low children are recombined before observation:
\[
\lambda(P-rSAP_y)+\lambda rSAP_y=\lambda P.
\]

High children have total unsigned mass `h<M/8`. Therefore
\[
f(P_x)\ge\frac1{40}(M-h)-\frac16h>\frac1{960}M.
\]

The exact annular Mellin multiplier is zero-safe in `Re s>0`. The only remaining
load-bearing theorem is the literal atomwise source-tree realization of the
current/high-child identity.
