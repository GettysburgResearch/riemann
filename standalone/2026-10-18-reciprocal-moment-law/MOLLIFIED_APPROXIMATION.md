# A source-preserving mean-square approximate inverse

Status: PROPOSED complete deduction from de Faveri's fixed-order large sieve
and the classical Hecke functional equation. Independent review is required.
This is a bound for `L M - 1`, not an unconditional pointwise bound for `1/L`.
No CT theta theorem, proposed quasi-RH conclusion, or inverse-moment hypothesis
is used. Parameters and field data below are fixed; constants are not uniform
in the character order, field, or distance from the critical line.

## 1. Family and statement

Fix n>=3, a number field F containing mu_n, and the admissible fixed S and
ray/generator data in de Faveri, arXiv:2610.04045, Sections 2.1--2.5.
The row a is an n-th-power-free integral ideal outside S, ordered by its FULL
ideal norm. Let psi be a fixed finite-order S-supported Hecke twist. Write

 L_a(s)=L_F^S(s,psi chi_a),
 M_A(s,a)=sum_{Nd<=A, (d,S)=1} mu_F(d) psi(d) chi_a(d) (Nd)^(-s).

Every nonunit zero and every ideal, including distinct ideals of equal norm,
is retained. The inducing conductor Q_a is O(Na), not necessarily comparable
with Na. Fixed S-local and gamma types may be partitioned into their finite list.

Fix s=sigma+it, 1/2<sigma<1, put d0=2sigma-1, and let

              0<a0<=d0/2,       A=U^a0,       X=U^(1/2).

For every epsilon>0,

 sum_{Na<=U}^{n-free} |L_a(s)M_A(s,a)-1|^2
       << U^(1-d0*a0+epsilon).                              (1)

The estimate is uniform for t in any fixed compact interval. Constants may
also be taken polynomial in a growing height, but no optimized height power
is asserted or needed in this packet. Finitely many inducing-principal rows
can be included at a fixed s in the open strip; their contribution is bounded
separately. Formula (1) is a full-family error estimate, not a selected mean.

## 2. The precise sieve used

The imported bound is on BOTH n-th-power-free indices:

 sum_{Na<=U}^{flat} |sum_{Nb<=V}^{flat} z_b chi_a(b)|^2
  << (UV)^epsilon K_n(U,V) sum_b |z_b|^2,
 K_n(U,V)=U+V+U^(1-1/n)V^(2/n)+U^(2/n)V^(1-1/n).             (2)

For U>=2 define k_n(v)=log_U K_n(U,U^v), up to a bounded multiplicative
constant, by taking the maximum of its four monomial exponents. On 0<=v<=1,

 k_n(v)=1,                         0<=v<=1/2;
 k_n(v)=1-1/n+2v/n,                1/2<=v<=1.               (3)

The following full-column consequence will be used repeatedly. If common
coefficients on V<Nb<=2V have modulus <=(Nb)^(-u+epsilon) times any FIXED
order divisor function, their squared row norm is

                    << (UV)^epsilon V^(1-2u)K_n(U,V).      (4)

Indeed write b=c e^n with c n-free; DO NOT impose (c,e)=1. Exactly
chi_a(c e^n)=chi_a(c)1_{(a,e)=1}. The coefficient square mass for fixed e
is O(V^(1-2u+epsilon)/(Ne)^n). Apply (2) on the indicated row subset and
Minkowski in the row norm. The sum (Ne)^(-n/2+epsilon) converges for n>=3.
All fixed twists go into common coefficients. Empty subunit c ranges vanish.
The bound also applies to the conjugate character matrix. This deduction is
credited to the earlier complete-column adapters, including #968 and #979.

## 3. An exact flat cutoff preserves the low-coefficient cancellation

Choose once a smooth V0 on (0,infinity) with V0=1 on (0,1], V0=0 on [2,infinity).
It need not be nonnegative. Its Mellin transform has just one simple pole,
at zero with residue one, and rapid vertical decay on each fixed strip away
from that pole. Put

 P_X(s,a)=sum_b (psi chi_a)(b)(Nb)^(-s) V0(Nb/X).

For an inducing-nonprincipal row the standard functional-equation calculation
in Section 4 gives L_a=P_X+R_X exactly. More importantly,

 P_X M_A - 1 = sum_{A<Nb<=2AX} (psi chi_a)(b)(Nb)^(-s) h(b),
 h(b)=sum_{e|b, Ne<=A} mu_F(e) V0(Nb/(Ne X)).              (5)

For 1<Nb<=A all divisors are present and V0=1, since A<=X. Thus h(b)=0
by Mobius inversion. The unit contribution is exactly one. This cancellation
is before any absolute value, and uses complete multiplicativity including
zeros. For larger b, |h(b)|<=C d_2(b); no fictitious further cancellation is
assumed. The cutoff in (5) is literal, not a formal AFE length with tails lost.

Apply (4) and Cauchy over the O(log U) norm bands in (5). Its exponent is the
maximum of k_n(v)-d0*v for a0<=v<=a0+1/2. By (3), before 1/2 it is at most
1-d0*a0. Beyond 1/2 either its slope is nonpositive, or its largest value is

 1-d0/2+(2/n-d0)*a0 <= 1-d0*a0,

because 2a0/n<=d0/2 follows from a0<=d0/2 and n>=3. Constants such as 2 in
2AX, divisor bounds, and logarithms are absorbed into the prescribed epsilon.
Consequently the full squared main-error norm is O(U^(1-d0*a0+epsilon)).

## 4. The complete dual, including small actual conductors

For clarity first take a primitive nonprincipal character without finite
Euler omissions. On a right line, Mellin inversion expresses P_X as the
integral of L_a(s+z) X^z V0hat(z). Move the line to Re z=-B, with B large.
Only the pole of V0hat at zero is crossed. Nonprincipal L is entire, and
rapid Mellin decay and polynomial strip bounds justify horizontal limits.
The functional equation on the new line then gives

 R_X(s,a)=epsilon_a Q_a^(1/2-s)
             sum_c conjugate((psi chi_a)(c)) (Nc)^(s-1)
                            V_s(Nc X/Q_a),              (6)

where the sign can be included in V_s. The dual weight is defined by the
complete Mellin integral, not a truncated dual series. It and the needed
logarithmic derivatives are bounded for 0<y<=1 and decrease faster than
any fixed power as y tends to infinity. For large y, move its Mellin line
further left. For small y, move it a fixed distance to the right of zero,
less than 1-sigma; retain the crossed residue. Gamma poles begin to the
right of that line. Stirling and the rapid decay of V0hat give the required
bounds uniformly on fixed t compacts. They also justify all summations below.

The row-dependent Q weights are separated AFTER grouping actual Q into
dyads. Fourier separation in log Q and log Nc on each localized pair of
dyads has bounded integrable norm, with the same rapid large-argument decay.
This follows by two derivatives and integration by parts in a compact
logarithmic coordinate. Gamma/S types form a finite list. The modulus-one
root number is outside the polynomial. Thus (4) is applied only to common
coefficient arrays, not to coefficients chosen separately for every row.

On a Q range, the effective dual length is L0=Q/X. A C band in (6) costs
in squared row norm

                 << U^epsilon Q^(-d0) C^d0 K_n(U,C)
                                   min(1,(C/L0)^(-J)),   (7)

with arbitrarily large fixed J, enlarged if necessary when squaring Fourier
norms. If L0>=1, sum the C bands using the four monomials of K_n. Their
positive C powers, d0>0, and the rapid tail give

 Q^(-d0)L0^d0 K_n(U,L0)=X^(-d0)K_n(U,L0) << U X^(-d0),

since Q<=C_F U and L0<=C_F sqrt(U). If L0<1, all C>=1 are in the tail;
the sum is O(U Q^(-d0)(Q/X)^J)<=O(U X^(-d0)) when J>d0.
This includes subunit effective lengths, not just Q comparable with U.

For L^S, write the primitive functional equation with its fixed finite
Euler polynomial at S. Each of its finitely many terms rescales X by a
fixed factor. Split a dual ideal into its S-part and exterior part. Its
S-part carries (Nc_S)^(sigma-1); the sum of these absolute weights converges
because S is fixed and sigma<1. Its extra dilation only shortens the dual
length; the same estimates apply. Original zeros at S and exterior nonunits
are preserved in the reconstructed expression. This supplies (6)--(7) for
the original incomplete source, up to fixed finite sums and convergent tails.

We conclude sum_a |R_X(s,a)|^2 << U^(1-d0/2+epsilon). Now use ONLY
|M_A|<<A^(1-sigma), valid with the literal masks, to obtain

 sum_a |M_A R_X|^2 << U^(1-d0/2+(1-d0)a0+epsilon)
                         <= U^(1-d0*a0+epsilon).         (8)

The last inequality is exactly a0<=d0/2. IMPORTANT: the dual involves
conjugate(chi_a(c)) whereas M_A involves chi_a(e). They are NOT combined
into chi_a(ce). Doing that would be false for n>2. This proof avoids that
false mixed-character simplification by the pointwise mollifier bound.

Combining (5) and (8) proves (1). For the finitely many principal rows,
|L_a(s)M_A-1|^2<<_s 1+A^(2-2sigma); this fits (1) because a0<1.

## 5. What (1) does and does not say

The actual signed convolution approximates one in mean square, with power
error, at EVERY fixed sigma>1/2. In particular the estimate is not obtained
by independently bounding the full L numerator and the full mollifier norm.
At an actual zero its error is one; (1) allows some such rows. It supplies
no pointwise assertion for a prescribed member and no native critical
Mobius moment at sigma=1/2. RECIPROCAL_MOMENTS.md uses (1), a sparse-zero
exclusion, and complete character averages to obtain a negative-moment law.
