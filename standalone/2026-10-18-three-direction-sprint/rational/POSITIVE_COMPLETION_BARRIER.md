# The diagonal price of a completed positive dual square

**PROPOSED exact estimate-class obstruction.** This is not a lower bound
for the actual mixed mean or its large-conductor part. It explains a
specific loss caused by completing a restricted signed Poisson form into
an unrestricted positive square. The complete shared-prime corrections
must be centered before that completion can give a useful estimate.

## 1. Precise square and assumptions

Use the actual corner D=U, N=U^(1/2), and put

    L=DN=U^(3/2),       H=L^2/U=U^2.                    (1)

The clean primitive Poisson normalization is U/L times a square of
centrally normalized product coefficients, at dual norm scale H. Here
is an exact statement about ANY proposed positive square with that
normalization. Let w>=0 be a fixed smooth annular weight, positive on a
nonempty norm interval. Let beta_A be product-column coefficients for
which the following actual isolated semiprime coefficients remain:

    |beta_(PQ)| >= c/sqrt(L),                           (2)

for all good prime ideals P,Q in fixed nonempty relative intervals
NP≈U, NQ≈sqrt(U). The intervals are disjoint for large U. The same
fixed primary ray and excluded finite prime set may be imposed on dual
rows. Consider the completed square

    Z=(U/L) sum_h w(Nh/H)
                    |sum_A beta_A chi_A(h)|^2.          (3)

All characters have their original zero extension. Other fixed common
unit phases may be incorporated in beta_A. The claim below assumes
(2); it does not silently identify every separated Poisson component
with (3).

Condition (2) holds for the actual nonzero corner profiles on suitable
prime intervals: the ONLY divisor pair of PQ in the specified inverse
and plain annuli is d=P,n=Q. Its Mobius coefficient is -1. Any primitive
Gauss or reciprocity factors on this clean squarefree product have
modulus one. Thus there is no cancellation inside this particular
coefficient. This is the same complete-coefficient observation proved
in `HYPERBOLA_COMPLETION_OBSTRUCTION.md`, not a contraction selecting
one of several terms at the same product.

## 2. Exact nonnegative diagonal resource

Expansion of (3) has the following diagonal summand:

    D_Z=(U/L) sum_A |beta_A|^2
                 sum_h w(Nh/H) 1_((h,A)=1).             (4)

This is an exact algebraic identity for the diagonal part; every mask
is still displayed. It is not asserted that Z>=D_Z, since the remaining
correlations may be negative.

For A=PQ in (2), the inner sum in (4) is >>H, uniformly in P,Q. Indeed
the fixed-ray weighted ideal lattice count is c_w H+O(sqrt(H)+1), with
c_w>0. Rows divisible by P or Q contribute at most

    O(H/NP+sqrt(H/NP)+1
      +H/NQ+sqrt(H/NQ)+1)=o(H).

The fixed excluded primes change only the positive density constant.
All constants depend solely on the fixed ray, exclusions and weight.
The fixed-modulus prime-number theorem gives
`>>U/log U` eligible P and `>>sqrt(U)/log U` eligible Q. Consequently

    D_Z >> (U/L) H/(log U)^2
          = L/(log U)^2
          = U^(3/2)/(log U)^2.                          (5)

The prime count is the same fixed-modulus-3 input documented in
`HYPERBOLA_COMPLETION_OBSTRUCTION.md`; no moving-ray or short-interval
prime theorem is required. The dual lattice counts used here are
elementary fixed-lattice counts, including their boundary term.

## 3. What this rules out, and what it leaves open

In the clean sector where the four original variables d1,n1,d2,n2
are pairwise coprime, a common nonunit product A1=A2 is absent. Dropping
the cross-coprimality restrictions to form (3) inserts precisely such
collisions. If an estimate pays the resulting diagonal (4) separately
and nonnegatively, it already spends at least (5). It therefore cannot
obtain a U^(q+epsilon) budget with q<3/2 solely by that uncentered
positive completion. Recovering a smaller budget requires retaining
the exact correction to those inserted collisions, or cancellation
within a centered dual covariance estimate. A bound for the
uncentered square alone does not supply that correction.

There are two distinct diagonals. The TRUE primitive-principal sector
of the original complete masked source is paid by the gcd/sixth-power
count in `MIXED_CONDUCTOR_SECTOR.md` and
`ACTUAL_SIXTHFREE_SECTOR.md`, at cost U^(1+epsilon). Equation (5)
describes an ARTIFICIAL resource introduced by unrestricted positive
completion of a different restricted dual form. It is not a new
U^(3/2) lower bound for the original principal sector, the original
mean, or its signed complement.

Thus the unresolved task is a source-specific centered correlation
estimate with all collision and shared-prime terms retained. This
note proves neither that such cancellation is unavailable nor that
the full target bound is false.
