# Quartic all-row tail using the newer fixed-order sieve

23 October 2026. A proved component conditional on the cited primary large-sieve theorem. This strengthens the earlier tail notes; it does not supply their missing centered physical moment.

De Faveri, [arXiv:2610.04045v1, Theorem 1.1 and definition (1.2)](https://arxiv.org/html/2610.04045v1), gives the following norm for fourth-power-free quartic rows and columns over the Gaussian field, with arbitrary column coefficients:

\[
 \Theta_4(X,M)\ll(XM)^\epsilon
 [X+M+X^{3/4}M^{1/2}+X^{1/2}M^{3/4}]. \tag{A1}
\]

Arithmetic data and the bad-prime set are fixed. Restricting columns to squarefree ideals is permitted. Native residue-symbol orientation is obtained by the fixed reciprocity-sector partition, and conjugation permits the opposite common sign.

## All physical rows

Write each nonzero row uniquely as r=r0 d^4, with r0 fourth-power-free. The factor (d^4/m)_4 is exactly the zero mask 1_(d,m)=1, including when r0 and d share primes. For each fixed d this is a fixed column multiplier. Applying A1 and summing Nd<=X^(1/4) gives

\[
 \sum_{0<Nr\le X}\left|\sum_{m\ {\rm sf}}b_m(r/m)_4\right|^2
 \ll(XM)^\epsilon
 [X+MX^{1/4}+X^{3/4}M^{1/2}+X^{1/2}M^{3/4}]
 \sum_m|b_m|^2, \tag{A2}
\]

for Nm<=M. The three nonconstant d sums have exponents 4,3,2 and converge; the row-independent M term counts O(X^(1/4)) fourth-power parts. No coprimality between r0 and d is imposed.

## Physical cubic-numerator tail

Use exactly the definitions, local branches, arbitrary row-independent bounded weight xi(c), and support conventions of `QUARTIC_CUBIC_NUMERATOR_TAIL.md`, SHA256 `6388564e225d8c7ba4a696b6f66a016be2f7dd1ff03e00888c62af55845bae0b`. Replace its all-row sieve by A2. Then

\[
 \boxed{\sum_{0<Nk\le K}|T_R^{[3]}(k,D)|^2
 \ll(KD)^\epsilon\left[
 {K\over R}+{K^{3/4}D^{1/2}\over R^{5/2}}
 +{K^{1/2}D^{3/4}\over R^3}
 +{DK^{1/4}\over R^{7/2}}\right].} \tag{A3}
\]

The exact empty-tail conditions R>(bD)^(1/4) and R>K remain unchanged.

For completeness, in a branch with local row divisor rho and normalized magnitude w, the two new local masses are w^2/(Nrho)^(3/4)(Nq)^(1/2) and w^2/(Nrho)^(1/2)(Nq)^(3/4). At a nonprincipal modulus exponent e=3a+1, 4 not dividing e, the exponents of Np in their denominators are (6+9a)/4 and (7+11a)/4. The first possible a is 2. At the first Ramanujan branch e=4j they are (3/4)ceil(4j/3)+2j and (1/2)ceil(4j/3)+3j. At the second Ramanujan branch add 2 and replace 4j by 4j-1 inside the ceilings. The minima are 7/2 and 4, both attained at j=1 in the first branch. Summing over radicals larger than R gives R^-5/2 and R^-3. The volume and fourth-power-count masses remain those of the cited tail proof. Rowwise Cauchy costs only divisor factors because all supported powerful moduli have primes dividing k and bounded valuations in terms of k.

For K>=D and R>=1, the third term of A3 is at most the second, so it may be omitted in that range.

## Conditional reattachment

If a separate theorem bounds the full physical vector by K up to subpowers, the cross norm at K=D^2/H, with inverse prefactor H/D, is at most

\[
 (HD)^\epsilon\left[
 DR^{-1/2}+DH^{1/8}R^{-5/4}
 +D^{7/8}H^{1/4}R^{-3/2}
 +D^{3/4}H^{3/8}R^{-7/4}\right]. \tag{A4}
\]

For H=D^alpha, 0<=alpha<=1, the four cutoff conditions are

\[
 r\ge2-2\alpha,\quad r\ge{4\over5}-{7\alpha\over10},
 \quad r\ge{7\over12}-{\alpha\over2},
 \quad r\ge{3\over7}-{5\alpha\over14}. \tag{A5}
\]

At alpha=14/15 the largest is 11/75, improving the earlier 4/27. A separately proved physical low-divisor error H^(2-u)D^(u-1)R^gamma would then allow gamma<=(5/11)(1-u), with strict margins for losses. This is only a reattachment budget. Neither a full physical norm nor that low-divisor error has been proved here; the native numerator-k spectral formula cannot be substituted for the actual k^3 family.
