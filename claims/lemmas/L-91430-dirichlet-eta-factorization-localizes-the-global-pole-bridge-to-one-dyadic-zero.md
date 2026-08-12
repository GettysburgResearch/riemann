# L-91430 — Dirichlet eta factorization localizes the global pole bridge to one dyadic zero

Claim ID: `L-91430`  
Status: **PROVED EXACT ANALYTIC FACTORIZATION AND POLE-COEFFICIENT IDENTITY**  
Created: 2026-08-12  
Depends on: `L-91330` on PR #403  
RH status: **unproved**

## 1. Paired eta function

Let

\[
 \eta_D(s)
 =(1-2^{1-s})\zeta(s).
 \tag{L-91430.1}

\]

For `Re s>0`, Dirichlet pairing gives the locally uniformly and absolutely
convergent series

\[
 \boxed{
 \eta_D(s)
 =\sum_{m\ge1}
  \left[(2m-1)^{-s}-(2m)^{-s}\right].
 }
 \tag{L-91430.2}

Indeed

\[
 (2m-1)^{-s}-(2m)^{-s}
 =s\int_{2m-1}^{2m}x^{-s-1}dx,
 \tag{L-91430.3}

\]

so on every compact subset of `Re s>0` the summand is
`O(m^{-1-Re s})`.

The conditional alternating Dirichlet series has therefore become an
absolutely convergent paired channel throughout the hard strip needed below.

## 2. Exact horizontal Jordan factorization

For `0<omega<1/2`, put

\[
 C_\omega(s)
 =\frac{\zeta(s-\omega)}
        {\zeta(s+\omega)}.
 \tag{L-91430.4}

\]

Whenever the denominator is nonzero and initially for `Re s>1+omega`,

\[
 \boxed{
 C_\omega(s)
 =\frac{\eta_D(s-\omega)}
        {\eta_D(s+\omega)}
  \frac{1-2^{1-s-\omega}}
       {1-2^{1-s+\omega}}.
 }
 \tag{L-91430.5}

\]

Both sides continue meromorphically, so (L-91430.5) holds wherever defined.

This factorization separates the global Jordan channel into

```text
an absolutely convergent paired all-integer ratio;
one explicit dyadic rational factor.
```

## 3. The pole node

The free archimedean endpoint of `L-91330` has its unstable pole at

\[
 s_0=1-\omega.
 \tag{L-91430.6}

\]

At this point

\[
 1-2^{1-s_0-\omega}=0,
 \tag{L-91430.7}

\]

while

\[
 1-2^{1-s_0+\omega}
 =1-2^{2\omega}\ne0.
 \tag{L-91430.8}

\]

Moreover

\[
 \eta_D(s_0-\omega)=\eta_D(1-2\omega),
 \qquad
 \eta_D(s_0+\omega)=\eta_D(1)=\log2.
 \tag{L-91430.9}

\]

Thus the zero of the positive forward Jordan factor at the pole node is
carried entirely by one dyadic factor; the paired eta ratio is finite.

## 4. Exact coefficient-one cancellation

Differentiating the dyadic numerator at `s_0`,

\[
 \frac d{ds}
 \left(1-2^{1-s-\omega}\right)_{s=s_0}
 =\log2.
 \tag{L-91430.10}

\]

Therefore

\[
\boxed{
 \lim_{s\to s_0}
 \frac{C_\omega(s)}{s-s_0}
 =\frac{\eta_D(1-2\omega)}
        {1-2^{2\omega}}
 =\zeta(1-2\omega).
 }
 \tag{L-91430.11}

\]

The final equality is the defining eta identity.  Equation (L-91430.11) is
exactly the coefficient in the Jordan zero

\[
 C_\omega(s)
 =\zeta(1-2\omega)(s-s_0)+O((s-s_0)^2)
 \]

used in `L-91330` to cancel the free gamma pole.

Hence the global coefficient-one pole-zero cancellation admits the exact
reorganization

\[
 \boxed{
 \text{paired eta channel}
 \times
 \text{one dyadic zero}
 \times
 \text{free gamma pole}.
 }
 \tag{L-91430.12}

## 5. Why this does not contradict the finite-Euler firewall

Finite positive Euler products amplify the pole residue, as proved in
`L-91330`.  The eta factorization is not a limit of those products in the same
positive Fock sector.  It performs an all-integer odd/even pairing before the
Hilbert norm is taken and therefore changes representation.

The construction is a candidate sector-changing bridge, not a repair by one
independent `p=2` factor appended after the prime product.

## 6. Exact boundary

```text
paired eta series on Re s>0                    ABSOLUTELY CONVERGENT
horizontal Jordan eta/dyadic factorization     EXACT
dyadic factor zero at the pole node            EXACT
local zero coefficient = zeta(1-2omega)        EXACT
free gamma-pole coefficient-one cancellation   EXACT
positive source-to-Hardy realization            OPEN
Riemann Hypothesis                              UNPROVED
```