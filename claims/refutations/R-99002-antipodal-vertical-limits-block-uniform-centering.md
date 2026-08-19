# R-99002 — Antipodal vertical limits block every uniform-center fractional heat estimate

Claim ID: `R-99002`  
Status: **COMPLETE BOHR/ARITHMETIC NO-GO**  
Created: 2026-08-18

Let `lambda(n)=(-1)^Omega(n)` be the Liouville function.  Twisting the Euler
variables of

\[
B_\diamond(s)=\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}
\]

by `lambda` gives

\[
 \boxed{
 B_{\diamond,\lambda}(s)
 =\frac{\zeta(s)}{\zeta(2s)}
  (1+2^{-s})(1+2^{-s-1}).
 }
\tag{R-99002.1}
\]

It has a simple pole at one.  Hence its fractional power has a pole branch of
order `theta`, and its critical heat energy has exponential rate `1/2`.

For any finite prime set, the numbers `{log p}` are rationally independent over
`Q`: an integer relation would exponentiate to a nontrivial equality of prime
products.  Kronecker approximation therefore supplies ordinates `tau_j` for
which

\[
 p^{-i\tau_j}\longrightarrow-1
\]

simultaneously on the finite set.  Truncating the heat packet first in total
log-energy and then in the prime alphabet shows that the original packet has
vertical limits equal to the Liouville-twisted packet.

Consequently every upper bound uniform in the center `tau_0` must pay the
antipodal real-pole rate `1/2`, independently of `theta`.

The scalar pole-centering factor

\[
 C_\theta(s)=\left(\frac{s}{s-1}\right)^\theta
\]

does not repair this uniform problem: for fixed `sigma>1`,

\[
 C_\theta(\sigma+i\tau_j)\longrightarrow1
\qquad(|\tau_j|\to\infty).
\]

Thus the same antipodal vertical limit survives.  A viable theorem may be
center-specific, but it cannot be uniform in all real centers with a tunable
rate below `1/2`.
