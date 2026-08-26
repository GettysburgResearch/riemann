# L-102838 — Every four-owner cross term has a double nonzero-phase representation

Claim ID: `L-102838`  
Status: **PROVED EXACT TWO-MODULUS DISPERSION IDENTITY**  
Created: 2026-08-24  
Depends on: `T-102850`; `L-102835`  
RH status: **not assumed**

Work in the direct hard sector of `T-102850`. Thus

\[
N=pq\,a^2,
\qquad
M=rs\,b^2,
\]

and the four owner primes `p,q,r,s` are physically distinct. Let

\[
\ell_1>\ell_2
\]

be the two largest of these four primes.

Each `ell_j` belongs to exactly one owner pair. Since square cores have even
valuation and contain only primes below their second owner,

\[
\ell_j\mid N
\quad\Longleftrightarrow\quad
\ell_j\nmid M.
\]

Consequently

\[
N-M\not\equiv0\pmod{\ell_j}
\qquad(j=1,2).
\]

For

\[
e_\ell(x)=\exp(2\pi i x/\ell),
\]

the two prime Ramanujan sums each equal `-1`:

\[
\sum_{h=1}^{\ell_j-1}e_{\ell_j}(h(N-M))=-1.
\]

Multiplying gives

\[
\boxed{
1=
\sum_{h_1=1}^{\ell_1-1}
\sum_{h_2=1}^{\ell_2-1}
 e_{\ell_1}(h_1(N-M))
 e_{\ell_2}(h_2(N-M)).
}
\tag{L-102838.1}

Thus every four-owner cross coefficient is an exact packet with **both** phase
coordinates nonzero. Neither coordinate has a principal frequency.

The identity is valid whether the two largest owners lie on the same physical
product or on opposite products. It retains the four owner labels, both square
cores, every source region and the fixed ratio-eight observation.

## Meaning

The direct four-owner sector has two independent arithmetic phase directions,
matching the two-owner degree of the Wick source. `L-102839` gives the exact
square-core energy attached to this two-dimensional phase packet.