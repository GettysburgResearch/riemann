# L-106020 — Square phases are an exact even-character L-family moment

Claim ID: `L-106020`  
Programme aliases: `LFAM1.SQUARE_PHASE_GAUSS_MELLIN`, `LFAM2.KUMMER_FOURIER_LOCAL_MODEL`, `STRESS.SHARP_PHASE_EMBEDDING`  
Status: **PROVED EXACT HILBERT-VALUED IDENTITY**  
Created: 2026-08-24  
Depends on: finite additive and multiplicative character orthogonality  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let `p` be an odd prime, let `H` be a complex Hilbert space, fix
`u in F_p^*`, and let `(v_n)` be a finite `H`-valued packet supported on
integers coprime to `p`. Put

\[
F_h=\sum_n v_n e_p(h u n^2),
\qquad h\in\mathbf F_p,
\tag{L-106020.1}
\]

and for every even multiplicative character

\[
\eta(-1)=1
\]

define

\[
M_\eta=\sum_n v_n\eta(n).
\tag{L-106020.2}
\]

Repeated residue classes are allowed; all sums are interpreted after
aggregation modulo `p`.

## 1. Additive-to-multiplicative Gauss transform

Let `chi` range over all multiplicative characters of `F_p^*` and let

\[
\tau(\chi)=\sum_{x\in\mathbf F_p^*}\chi(x)e_p(x).
\]

Multiplicative Fourier inversion applied to the pushforward under

\[
n\longmapsto u n^2
\]

gives

\[
F_h={1\over p-1}
\sum_\chi
\tau(\chi)\overline{\chi(h u)}M_{\chi^2}
\qquad(h\ne0).
\tag{L-106020.3}
\]

Therefore multiplicative orthogonality in `h` yields

\[
\sum_{h=1}^{p-1}\|F_h\|^2
={1\over p-1}
\sum_\chi |\tau(\chi)|^2\|M_{\chi^2}\|^2.
\tag{L-106020.4}
\]

The principal Gauss sum is `-1`, while every nonprincipal Gauss sum has squared
modulus `p`.

The square map on the character group has kernel

\[
\{1,\kappa_p\},
\]

where `kappa_p` is the quadratic character, and its image is exactly the even
characters. Grouping the two square roots of every even character gives the
exact identity

\[
\boxed{
\sum_{h=1}^{p-1}\|F_h\|^2
={p+1\over p-1}\|F_0\|^2
+{2p\over p-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}
\|M_\eta\|^2.
}
\tag{L-106020.5}
\]

This is a positive moment formula over the complete even Dirichlet-character
family modulo `p`.

## 2. Sharp principal embedding

Every term on the second line of (L-106020.5) is nonnegative, hence

\[
\boxed{
\|F_0\|^2
\le {p-1\over p+1}
\sum_{h=1}^{p-1}\|F_h\|^2.
}
\tag{L-106020.6}
\]

There is no factor `p`.

Moreover, because `p` divides none of the physical residues `u n^2`, the prime
Ramanujan identity gives termwise

\[
\boxed{
\sum_{h=1}^{p-1}F_h=-F_0.
}
\tag{L-106020.7}
\]

Thus the norm of the coherent sum of all nonzero additive phases is controlled
by their square energy with a strict constant smaller than one:

\[
\left\|\sum_{h=1}^{p-1}F_h\right\|^2
\le {p-1\over p+1}
\sum_{h=1}^{p-1}\|F_h\|^2.
\tag{L-106020.8}
\]

Ordinary Cauchy would insert the factor `p-1`; on square-supported physical
packets that loss is nonphysical.

## 3. Tensor form

For distinct odd primes `p_1,...,p_k`, define the corresponding product phase
packet `F_(h_1,...,h_k)`. Iterating (L-106020.5) gives

\[
\boxed{
\|F_{\mathbf0}\|^2
\le
\prod_{j=1}^k{p_j-1\over p_j+1}
\sum_{h_1\ne0}\cdots\sum_{h_k\ne0}
\|F_{\mathbf h}\|^2.
}
\tag{L-106020.9}
\]

The tensor identity is exact at the level of positive operators. In residue
coordinates modulo sign, the one-prime operator is

\[
pI-J,
\]

whose eigenvalue on the constant vector is `(p+1)/2` and whose orthogonal
eigenvalue is `p`.

## 4. L-family meaning

For a physical squareclass `N=P n^2`, the multiplicative transform in
(L-106020.3) is

\[
\chi(N)=\chi(P)\chi^2(n).
\]

Thus the nonzero additive owner phases already form, after an exact Gauss
change of basis, a moment of the even Dirichlet `L`-channels `chi^2`.
The principal and quadratic square roots both map to the untwisted core
channel; every other square root gives a nonprincipal even core character.

The owner-conductor Vaughan interpretation is made explicit in `L-106022`.
The identity proves no global owner summation and no RH result.