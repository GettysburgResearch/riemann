# A row-dependent refinement of the effective full-support bound

This is an analytic corollary of EFFECTIVE_FULL_SUPPORT_THEOREM.md,
frozen at ae60a59d103a6696a667be4dbd0721387adc6a77. It keeps the exact
64 rows, (A,C) tensor coordinates, original current and physical weights.
The accepted local inverse certificate at
0103b95130de0f8151c529a0911a52842732227d supplies
B=483723248. No registered artifact, local shift or inverse is changed.

Put u_n=|[z^n]sqrt(1-z^2)|+|[z^n]sqrt(1-z)|.
The even subsequence u_(2k)=|c_k|+|c_(2k)| decreases for k>=1.
The odd subsequence is |c_(2k+1)| and also decreases. Consequently

    sup_(n>=1) u_n = sup_(n>=2) u_n = 5/8,
    sup_(n>=3) u_n = sup_(n>=4) u_n = 21/128.

The latter maximum is u_4=1/8+5/128; the largest eligible odd value
is |c_3|=1/16. Define e_1=e_2=5/8 and e_3=e_4=21/128.

For the already selected denominator b=product p_i^beta_i, with
beta_i in {1,2,3,4}, summing all column absolute values first gives

    row_tail_b <= H^(-1/2) sqrt(b)
                  sum_d ||v_d||_1 ||v_(db)||_1
               <= 64 H^(-1/2) product_i p_i^(beta_i/2) e_(beta_i).

This uses the established sum_d ||v_d||_1=64. Every exponent of db
is at least beta_i. All supported aliases remain present, and the
finite hyperbolic cutoff is not assumed to factor.

For each prime, an odd beta is dominated by the following even beta,
because its e value is the same. Among beta=2,4 the ratio of the latter
bound to the former is 21p/80. Thus the largest product over the fixed
64 rows is at beta=(2,2,4) for primes (2,3,5). Hence

    ||R_H-R_infinity||_infinity <= L_3/sqrt(H),
    L_3=64*(2*5/8)*(3*5/8)*(25*21/128)=39375/64.

With the same certified inverse norm bound B, define the exact integer

    H_3=floor((2 B L_3)^2)+1
       =floor((19046602890000/32)^2)+1
       =354270587548199562597657.

For every integer H>=H_3, the inverse comparison is strictly less
than 1/2. Therefore the same 64-row observation is invertible on the
complete tensor space, and its restriction distinguishes the twenty
actual current-variation directions. The nonzero physical row scaling
does not change this conclusion.

The arithmetic displayed above is an exact rational calculation, not
a new source acquisition or a new named acceptance test. The earlier
H0/H1/H2 bounds remain valid records; H3 is a separate stronger corollary.
It is still conservative and does not assert an optimal first horizon.
The verified finite interval through 2^48 remains separate; horizons
2^48<H<H3 are not settled here. This does not repair the old singular
limiting minor, identify the infinite optimizer, extend to all primes,
or identify the full retained-gamma source.
