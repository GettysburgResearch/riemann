# Full native-family moments at every fixed order, with the unsaved terms intact

Status: PROPOSED source-qualified deductions from DF Theorem 1.1. Not independently
reviewed. This is a genuine all-order upper estimate for coefficient sums,
without a Mellin-twist average. It is NOT the diagonal-power theorem needed for RH.
The extension and its explicit lost terms, not global literature priority, are
recorded here. Constants depend on each fixed order.

## 1. The family and the literal zero convention

Use the fixed n-th order ideal family of ALL_NUMERATOR_MOMENTS.md, n>=3.
Unless the physical-row extension in Section 3 is invoked, every row and column
ideal is outside the same fixed S. Every full row ideal m has a unique decomposition m=a b^n, a n-free. Define

  chi_hat_m(I)=chi_a(I) 1_((b,I)=1).                     (1)

The mask in (1) matters: a sixth-power physical row is NOT the constant character
at primes dividing its generator. This is the imprimitive zero extension appropriate
to the literal power-residue source, not the primitive-character convention on full indices used in BGL.
Both conventions are legitimate, but they are different arithmetic objects.

Let |v(I)|<=1 be any common column array (native choice v=mu_F), optionally
including further fixed omissions and unit-modulus common twists. For bounded
W supported in (0,1], define

 A_m(X)=sum_I v(I) chi_hat_m(I) W(NI/X),
 M_(2k)(X,H)=sum_(Nm<=H) |A_m(X)|^(2k).                 (2)

Here X,H>=2 and k>=1 is FIXED. Ideals, not rational norms, index both sums.
Thus equal-norm conjugate ideals remain separate. A fixed S-supported twist is
allowed as a common column factor. Fixed finite ray-class/allowed-generator
subdivisions can be included: first split the column/row classes, pay the finite
Holder factor and apply the same bound to each common coefficient array.

## 2. Full moment theorem

For every epsilon>0,

 M_(2k)(X,H) << ||W||_infinity^(2k) (HX)^epsilon [
       H X^k + H^(1/n) X^(2k)
       + H^(1-1/n) X^(k(1+2/n))
       + H^(2/n) X^(k(2-1/n)) ].                      (3)

This includes every row and every 2k-tuple. It has no frequency average, no
prime randomization, and no missing high prime-power columns. It is uniform
in the common array v with |v|<=1, not a use of its Mobius signs.
For n=6 the four terms are

  H X^k, H^(1/6)X^(2k), H^(5/6)X^(4k/3), H^(1/3)X^(11k/6). (4)

**Long-row diagonal corollary.** For EVERY fixed k and H>=X^(2k),

 M_(2k)(X,H) << ||W||_infinity^(2k) (HX)^epsilon H X^k. (4a)

Indeed all three ratios of the other terms in (3) to H X^k are at most one:
X^k/H^(1-1/n), X^(2k/n)/H^(1/n), and
X^(k(1-1/n))/H^(1-2/n), with n>=3. This is a complete diagonal-power
all-order theorem, but its ROW HEIGHT grows with the order. It does not supply
the fixed-height-exponent hypothesis of CRITICAL_ROUTE. The height cost cannot
be relabeled as a harmless constant or as a column-scale-independent average.

### Proof

Fix the full-row factor b, and put U=H/(Nb)^n. Raising A_(a b^n)(X) to power k
is an EXACT finite ideal convolution, supported on NJ<=X^k. Its coefficients
are

  c_(k,X)(J)=sum_(I_1...I_k=J) product_j v(I_j)W(NI_j/X).

They satisfy |c_(k,X)(J)|<=||W||_infinity^k d_k(J), where d_k counts ordered
ideal factorizations. There is no coprimality restriction among the I_j.
The product of their b-masks is exactly 1_((b,J)=1). Divisor bounds give
|c_(k,X)(J)|<<_(k,delta) ||W||^k (NJ)^delta.

Split NJ into dyads V. Write J=c e^n, c n-free, without imposing (c,e)=1.
The resulting polynomial on a is

  sum_e 1_((a,e)=1) sum_c c_(k,X)(c e^n)
                          chi_a(c)1_((b,c e^n)=1).       (5)

For fixed e, (5)'s coefficient square mass is O(V^(1+O(delta))/(Ne)^n).
Apply DF's sieve to c and Minkowski in the a-l2 norm across e. The summable
root weight (Ne)^(-n/2+O(delta)) retains ALL e. This proves the n-free-row bound

  sum_(Na<=U)^flat |A_(a b^n)(X)|^(2k)
    << ||W||^(2k)(UX)^epsilon X^k K_n(U,X^k),          (6)

with constants independent of b. Nonnegative row masks were discarded only
inside a positive norm; column masks stay in a common array. The finitely many
dyads add logarithms absorbed in epsilon. If 1<=U<2 the same expression covers
the unit row, by the trivial coefficient bound or the valid sieve at U>=1.
If U<1 there is no row.

Now sum b with Nb<=H^(1/n). The four terms of K_n produce, respectively,

  H sum_b (Nb)^(-n) << H,
  X^k sum_(Nb<=H^(1/n))1 << H^(1/n) X^k,
  H^(1-1/n)X^(2k/n) sum_b (Nb)^(-(n-1)) << H^(1-1/n)X^(2k/n),
  H^(2/n)X^(k(1-1/n)) sum_b (Nb)^(-2) << H^(2/n)X^(k(1-1/n)).

Fixed-field ideal counting and n>=3 justify every convergence. Multiplication
by the external X^k proves (3). QED.

## 3. Physical Eisenstein rows and Gaussian weights

For the Eisenstein field, an integral ideal has six generators modulo units.
Writing u=epsilon alpha beta^6 with ideals (alpha)=a, (beta)=b gives exactly
(1), together with one of the six fixed unit twists. Reciprocity introduces only
fixed ray-class column/row factors for the admissible choices in DF Section 2.
Partitioning these finite classes before powering therefore gives (3), with
a fixed constant, for the usual literal sextic source on 0<Nu<=H and (u,S)=1.
To include rows meeting S as well, write their S-valuations modulo six: the
remainders give a FINITE list of fixed S-supported factors, hence fixed
S-supported character twists on the exterior columns. The remaining sixth
powers join b, now allowed to meet S; their masks on exterior columns are one.
The same four convergent/counting sums over b remain upper bounds when these
primes are admitted. The finite residual S factors only decrease the available
row height up to fixed constants. Thus the same bound includes all nonzero
Eisenstein rows in the norm ball. This adapter requires those admissible fixed choices; no assertion is made about an arbitrary
uninspected theta profile or a norm-only element ball in a positive-unit-rank field.

The same bound, with a constant depending on c,k instead of ||W||, holds for

  W_c(y)=y^(-c) exp[-(log y)^2/4]/(2 sqrt(pi)).          (7)

Proof: split y into dyadic annuli. Their suprema decay faster than any fixed
power of 2^(-|j|). Apply (3) to each annulus at scale 2^j X and use Minkowski
in the COMBINED row l_(2k) norm. Each of the four root terms has a fixed power
of 2^j, so all annuli sum. Empty annuli with upper norm below 1 are genuinely
empty; the one crossing the unit norm is retained. Constants depend on k,c.
This is not a square expansion followed by deletion of cross-annulus terms.

Keeping the SAME H at every X, the cumulative Gaussian energy also satisfies

  integral_0^D M_(2k)(X,H) dX/X^(k+1)
   << (DH)^epsilon [H + H^(1/n)D^k
            + H^(1-1/n)D^(2k/n) + H^(2/n)D^(k(1-1/n))]. (8)

Integrate the four terms for X>=1, absorbing the first logarithm. For 0<X<1,
ideal counting and (7) give |A_m(X)|<=C_B X^B for each fixed B; choose 2kB>k.
Summing the O(H) rows proves the finite lower tail. No scale-dependent row measure
has been substituted.

## 4. The exact lost exponent, not a declaration of RH

For H=X^h, write (4) as X^(h+k+e_k+epsilon). It gives

 e_k(h)=max(0, k-5h/6, k/3-h/6, 5k/6-2h/3).           (9)

For every FIXED h, e_k(h)/k tends to 1, not 0. The principal row alone therefore
extracts an exponent tending to 1, not 1/2. In fact h+e_k(h)>=k+h/6>=k
for EVERY h>=0, by the second entry of (9), so optimizing h with k cannot
make that extraction subcritical either. Even the older sixth-power-replica
extraction cannot manufacture a saving from this envelope: the retained term
k-5h/6 exactly cancels its replica gain.

The H^(1/6)X^(2k) term is the result of paying the length part of the sieve
separately for each full-row sixth-power cofactor. It must not be identified
term-by-term with only the principal physical rows. Nonprincipal rows remain in
that sieve bound too. Deleting the principal row does not delete this operator
norm contribution.

An unsigned common array already makes the unit-row value of a nonnegative
hard-window source of order X; its 2k-th power is of order X^(2k). Thus an
unrestricted common-array argument cannot erase all such terms. A stronger
native theorem must use actual Mobius cancellation, or a source-specific signed
projection, rather than renaming (3) a diagonal bound. The present result is
not the desired sublinear-excess hierarchy.
