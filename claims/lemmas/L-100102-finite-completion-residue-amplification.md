# L-100102 — Finite Euler completion alternately amplifies and suppresses off-line residues

Claim ID: `L-100102`  
Status: **PROVED ASYMPTOTIC THEOREM ON THE CLASSICAL PNT**  
Created: 2026-08-20  
Depends on: `L-100101`; the classical prime number theorem  
RH status: **not assumed**

Fix `k>=2` and

\[
z=\beta+i\gamma,
\qquad
\frac12<\beta<1,
\qquad
\gamma\ne0.
\]

Let `mathcal A_(Z,k)(z)` be the finite completion multiplier of
`L-100101`.

For all sufficiently large primes,

\[
\log(1+p^{-z}+\cdots+p^{-(k-1)z})
=p^{-z}+O_{z,k}(p^{-2\beta}).
\]

Since `2 beta>1`, the accumulated error converges.  The exceptional `67`
factor changes only the bounded constant, and therefore

\[
\log\mathcal A_{Z,k}(z)=\sum_{p\le Z}p^{-z}+O_{z,k}(1).
\tag{L-100102.1}

Partial summation with the prime number theorem gives

\[
\boxed{
\log\mathcal A_{Z,k}(z)
=
\frac{Z^{1-z}}{(1-z)\log Z}
+O_{z,k}\!\left(\frac{Z^{1-\beta}}{(\log Z)^2}\right).
}
\tag{L-100102.2}

A continuous logarithm is legitimate because the finite multiplier is
zero-free in `Re z>0`.

Writing

\[
\theta_Z=\gamma\log Z+\arg(1-z),
\]

we obtain

\[
\log|\mathcal A_{Z,k}(z)|
=
\frac{Z^{1-\beta}}{|1-z|\log Z}\cos\theta_Z
+O_{z,k}\!\left(\frac{Z^{1-\beta}}{(\log Z)^2}\right).
\tag{L-100102.3}

Hence there are sequences `Z_m^+` and `Z_m^-` tending to infinity and a
constant `c_z>0` such that

\[
\boxed{
|\mathcal A_{Z_m^+,k}(z)|
\ge
\exp\!\left(c_z\frac{(Z_m^+)^{1-\beta}}{\log Z_m^+}\right),
}
\tag{L-100102.4}

and

\[
\boxed{
|\mathcal A_{Z_m^-,k}(z)|
\le
\exp\!\left(-c_z\frac{(Z_m^-)^{1-\beta}}{\log Z_m^-}\right).
}
\tag{L-100102.5}

Thus varying a **finite** completion cutoff alternately amplifies and suppresses
an off-line residue on a superpolynomial scale.

If `rho` is a zero of zeta with `Re rho>1/2`, every finite completed cubic
transform retains the pole at `s=rho-1/2`, with residue multiplied by

\[
\mathcal A_{Z,k}(\rho)\ne0.
\tag{L-100102.6}

For fixed `Z,k`, Landau therefore forbids eventual nonnegativity of that
completed scalar.  Let

\[
N_{Z,k}=\inf\{X\ge1:(\mathscr A_{Z,k}\mathcal C_3)(X)<0\},
\tag{L-100102.7}

where `C3` is PR #676's cubic critical scalar.  Under failure of RH,
`N_(Z,k)<infinity`, while `L-100101` gives

\[
N_{Z,k}>Z^A\qquad(A<A_k^*)
\tag{L-100102.8}

for all sufficiently large `Z`.

The remaining issue is not multiplier cancellation.  It is a uniform
moving-cutoff Perron theorem showing that an amplified pole dominates the
other poles and contour remainder at some `X<Z^(A_k^*-o(1))`.
