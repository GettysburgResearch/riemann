# L-98072 — Subpower negative scalar mass suffices, and one prefix exceedance controls it

Claim ID: `L-98072`  
Status: **PROVED CONDITIONAL CONCLUSION THEOREM + EXACT REDUCTION**  
RH status: **unproved**

Let `A_X` denote the native annular scalar and
\[
\mathcal N(T)=\int_1^T A_X^-\,dX/X.
\]

If for some `theta>=0`
\[
\mathcal N(T)=O_\epsilon(T^{\theta+\epsilon})
\]
for every `epsilon>0`, then the negative-part Mellin transform is holomorphic
in `Re s>theta`. The positive part has nonnegative density, so Landau's theorem
forces the full zero-safe reciprocal-zeta transform to be holomorphic there.
Thus zeta has no zero with real part `>1/2+theta`. In particular
\[
\mathcal N(T)=T^{o(1)}\Longrightarrow RH.
\]

Now put
\[
B_{1/2}(t)=\sum_{n\le t}\frac{\mu(n)}{\sqrt n},
\qquad
\mathcal D(t)=6B_{1/2}(t)-\frac9{\sqrt2}B_{1/2}(t/2)
+\frac32B_{1/2}(t/4).
\]
The exact scalar coefficient prefix is `C(t)=6-D(t)` and
\[
A_X=\int_{X/4}^X C(t)\,dt/t.
\]
Hence
\[
A_X^-\le\int_{X/4}^X(\mathcal D(t)-6)_+\,dt/t
\]
and Fubini gives
\[
\mathcal N(T)\le(\log4)\int_{1/4}^T(\mathcal D(t)-6)_+\,dt/t.
\]

Therefore
\[
\int_1^T(\mathcal D(t)-6)_+\,dt/t=T^{o(1)}
\]
is a sufficient one-sided criterion for RH (`DPE67`).
