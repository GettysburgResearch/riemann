# L-105423 — One-sided frame dimension and record threshold

On `(0,L_T)`, the exponentials

\[
L_T^{-1/2}e^{i(T+2\pi k/L_T)u}
\]

are orthonormal. The number with frequencies in `[T,2T]` is

\[
\boxed{d(T,L_T)=TL_T/(2\pi)+O(1).}
\]

For `L_T=lambda log(T/2pi)`,

\[
\boxed{d(T,L_T)=(\lambda+o(1))N_1(T,2T).}
\]

After the T-105310 multiplicity/nonreal budget, positivity on this subspace
would give

\[
\liminf N_0/N\ge2\lambda-1-821/5000.
\]

This exceeds `269/400` exactly when

\[
\boxed{\lambda>18367/20000=0.91835.}
\]

A smooth taper of the same nominal dimension needs a separate uniform Gram
conditioning theorem.
