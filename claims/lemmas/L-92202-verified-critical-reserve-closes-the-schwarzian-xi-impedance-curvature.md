# L-92202 — The verified critical reserve closes the Schwarzian Xi-impedance curvature

Claim ID: `L-92202`  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: `L-92200/L-92201`; the same external verified-height/local-count lock  
RH status: **unproved**

## 1. The next complete-Bernstein shadow

Retain

\[
 p(t)=\sum_\alpha\frac{w_\alpha}{t+s_\alpha},
 \qquad
 Z(t)=\frac1{p(t)},
 \qquad t>1/4.
\]

A direct differentiation gives the Möbius-invariant identity

\[
\boxed{
 2Z'Z'''-3(Z'')^2
 =\frac{2p'p'''-3(p'')^2}{p^4}.
}
\tag{L-92202.1}
\]

For a Stieltjes admittance, the right-hand numerator is a positive Hankel
minor.  It is the infinitesimal condition for matrix monotonicity of order two.

## 2. Pairwise fourth-power dispersion

Using

\[
 p'=-\sum_\alpha\frac{w_\alpha}{u_\alpha^2},
 \quad
 p''=2\sum_\alpha\frac{w_\alpha}{u_\alpha^3},
 \quad
 p'''=-6\sum_\alpha\frac{w_\alpha}{u_\alpha^4},
 \quad
 u_\alpha=t+s_\alpha,
\]

one obtains exactly

\[
\boxed{
 2p'p'''-3(p'')^2
 =6\sum_{\alpha,\beta}
 w_\alpha w_\beta
 \frac{(s_\alpha-s_\beta)^2}
 {u_\alpha^4u_\beta^4}.
}
\tag{L-92202.2}
\]

For one unordered pair the coefficient is twelve.

As in `L-92200`, every real-real term is nonnegative, while a conjugate
off-line pair has a negative internal interaction.

## 3. Verified-anchor domination

Use the same verified real squared pole `r_0<=H^2/4` of weight `w_0=2` and
the same notation

\[
 s_i=c_i+id_i,
 \qquad
 B=b_i>H,
 \qquad
 A_i=t+c_i.
\]

### Anchor term

The denominator rotation now has power four.  The argument bound becomes

\[
 2\arctan\frac{3}{2B}
 +4\arctan\frac2B<\frac\pi2.
\]

Therefore the unordered anchor interaction is at least

\[
\boxed{
 P_i^{(4)}(t)
 \ge\frac{16}{3}\,w_i\frac{B^4}{A_i^8}.
}
\tag{L-92202.3}
\]

### Local negative row

Pairs with height separation at least two remain nonnegative: the numerator
angle is below `2 arctan(0.501)` and the total denominator rotation is below
`8/H`.

For a local pair, `|s_i-s_j|^2<=30B^2` and
`|t+s_j|>=A_i/2`, so

\[
 \left|
 \frac{(s_i-s_j)^2}{u_i^4u_j^4}
 \right|
 \le480\frac{B^2}{A_i^8}.
\]

Including the coefficient twelve and the local pole-weight bound
`W_B<=4 log(B+3)` gives

\[
\boxed{
 N_i^{(4)}(t)
 \le23040\,w_i
 \frac{B^2\log(B+3)}{A_i^8}.
}
\tag{L-92202.4}

At the verified height,

\[
 B^2>4320\log(B+3)
\]

with a margin exceeding `10^20`.  Hence

\[
 P_i^{(4)}(t)>N_i^{(4)}(t)
\]

for every possible nonreal pole and every safe `t`.

Summing as in `L-92201` gives

\[
\boxed{
 2p'(t)p'''(t)-3p''(t)^2>0
 \qquad(t>1/4).
}
\tag{L-92202.5
}

## 4. Schwarzian and concave reciprocal slope

Since `Z'(t)>0`, put

\[
 g(t)=\frac1{\sqrt{Z'(t)}}.
\]

Then

\[
 \boxed{
 g''(t)
 =-\frac{2Z'Z'''-3(Z'')^2}{4(Z')^{5/2}}<0.
 }
\tag{L-92202.6}

Thus the reciprocal square root of the Xi impedance slope is strictly
concave throughout the safe axis.

Equivalently, the Schwarzian derivative satisfies

\[
 \boxed{
 \mathcal S Z
 =\frac{Z'''}{Z'}-\frac32\left(\frac{Z''}{Z'}\right)^2>0.
 }
\]

## 5. Boundary

```text
fourth-power pairwise dispersion identity       EXACT ALGEBRA
verified-anchor domination                       PROPOSED COMPLETE
positive Schwarzian of the safe Xi impedance     PROPOSED UNCONDITIONAL
matrix monotonicity of order two                  NEXT THEOREM
matrix monotonicity of order three and higher     OPEN / RH-BEARING
complete Bernstein Xi impedance                   OPEN / RH-EQUIVALENT
Riemann Hypothesis                               UNPROVED
```
