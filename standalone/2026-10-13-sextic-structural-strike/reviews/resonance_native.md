# Independent reconstruction: both actual trace resonances and the short-factor lower bound

**Reviewer:** native_structural_attack, 13 October 2026.

**Verdict:** the three frozen proof manuscripts below have a complete argument
for their stated scope. Two compose to refute the source's unfiltered
subcritical complementary-short-trace contract CT1 at every fixed k>=2;
the third independently refutes its original critical Euler trace P13 at
every fixed k>=1. Both refutations include every polynomially weakened
version of their respective contracts. This work does
not refute the norm-filtered moment and does not prove a new moment upper
bound, zero-free boundary, or RH.

**Exact review targets:**

| File | SHA-256 |
| --- | --- |
| `RESONANT_SHORT_TRACE.md` | `1c043c4650e72d9c78daef4111a3a2485c6f5d285a1ca2afee62283c9286a70f` |
| `SHORT_FACTOR_NONSMALLNESS.md` | `0af49f68a90bc19253e6543abd2e8d8af295a2bb133c5ebb59686e516655a935` |
| `EULER_TRACE_RESONANCE.md` | `c8931a93f3fc47805143ab4074ca4e315656a87e58abd5e0e7ba59c03079fb10` |

All three reside in `standalone/2026-10-13-sextic-structural-strike/` in the
shared repository. I computed the file hashes after reading them and read
the exact source definitions cited below. This review does not silently
bind a later edit of either target.

## Authorship and independence

I did not write any target, the all-k phase-cluster construction, the
short-factor interpolation argument, or the original-Euler construction.
Before the manuscripts were frozen,
the root described the proposed k=2 construction. I independently checked
its positivity, mask admissibility, quadratic sign and tube separation and
reported those checks; that early checking is disclosed here. I then
reconstructed the full all-order arguments from the written proofs. My
separate research in this pass concerned collision-free moment polynomials,
prime-selected native sectors, and coefficient perturbations; it is not a
premise of the reviewed result.

This is an internal mathematical AI-agent review. Same-model agreement is
not formal verification or external human acceptance. The evidence here
is the explicitly reconstructed argument and its source checks.

## 1. Source definitions were checked before the new estimate

I read the preserved versions from PR #911 at
`2f8b6a3898a722d0602a91dea73bac344a3bb7dd` of:

- `COMPLEMENTARY_SHORT_TRACE_CONTRACT.md`, in full;
- `SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md`, in full;
- `WIDE_SUBCRITICAL_TUBE.md`, in full;
- `PRIME_SLOT_CANCELLATION.md`, especially P1–P3 and P8.

I also read Section 2 of the parent
`standalone/2026-10-10-sextic-moment-conductor-core/CONDUCTOR_SECTORS.md`.
It explicitly chooses a nonnegative radial smooth majorant at least one
on the unit disk. This verifies the spatial positivity used in the new
argument; it is not inferred from an arbitrary Schwartz profile.

The source facts important to the verdict are these.

1. Every T_i is the literal norm truncation at the **common** Y, including
   its unit coefficient. A shorter physical length D/Nc_i is absent from
   the CT1 integrand and appears only in the later filtered integral.
2. CT1 is a pointwise assertion for every independent frequency vector
   outside the stated tube. The proof therefore needs only a vector on
   a paired subspace, provided it is outside that tube. It does not need
   a positive-measure set in all 2k frequency dimensions.
3. The incidence allocation is allowed whenever its q_I are pairwise
   coprime squarefree ideals and all Nc_i<=Y. Its exterior row factor is
   the literal product of the sextic symbols in its slots.
4. The true enlarged WT1 width is
   0<kappa<arcsin(1/sqrt(2k)). I checked this wider version, rather than
   using only the earlier narrower width.
5. The source distinguishes the complete filtered identity SC4 from
   pointwise equality of the short and Euler integrands. The reviewed
   theorem respects that distinction.

## 2. The fixed mask is legal and makes the complete trace positive

Choose P0 with 2k q^(-sigma)<=1/2 for q>P0. The product Q of all good
prime ideals with norm at most P0 is a **fixed** squarefree ideal. It may
be large, but its size is independent of Y. The assignment
q_{ {1,k+1} }=Q and all other q_I=1 is a genuine cross-pair incidence.
It becomes eligible at Y>=NQ. There is no moving-source or arbitrary-row
selector hidden in this choice.

At nu=1, the exterior arithmetic factor is exactly

\[
 \chi_Q(u)\overline{\chi_Q(u)}=\mathbf1_{(u,Q)=1}.
\]

The two copies of its Möbius sign multiply to one. At primes of Q
meeting a row, the row term is zero rather than an artificial one.

On the paired plane t_{k+j}=-t_j, the local variables occur in conjugate
pairs. Therefore the numerator of the collision factor is
1-2x Re(sum_j v_j), which is at least 1-2kx>=1/2. Its denominator is
the product of the positive numbers |1-xv_j|^2. At a good prime dividing
the row, every local variable is zero and that local factor is exactly
one. Thus the positive sign is valid for **every** nonzero arithmetic
row, not just row one.

The literal short factors pair into products of squared moduli. The
exterior mask and the source spatial majorant are nonnegative. Hence
the complete CT1 row sum is a sum of nonnegative real terms on this
plane. Its convergence at each fixed Y is justified by a row-uniform
finite bound on the factors and the Schwartz row weight. The retained
unit row has weight at least one. Extracting its contribution is therefore
a valid lower bound for the whole trace, without discarding possible
negative row contributions.

This step is essential. A large positive single row in a general signed
trace would not suffice. Here the complete-row positivity was actually
proved from the source factors.

## 3. I reconstructed the all-k collision growth

For n_+=ceil(k/2), n_-=floor(k/2), and d=n_+-n_-, the model signs have
2n_+ plus entries and 2n_- minus entries. The exact pair sum is

\[
 \frac{(2d)^2-2k}{2}=-(k-2d^2)=-\gamma.
\]

For even k, gamma=k; for odd k>=3, gamma=k-2>=1. Thus the sign works
for every fixed k>=2, including the least-margin case k=3. It does not
accidentally claim the same construction at k=1.

With delta_Y=pi/logY, epsilon_k=1/(100k^2), and
a_k=1-1/(100k^2), the actual phases at primes in [Y^(a_k),Y]
are within (1+pi)/(100k^2) of their designated signs for the full central
interval |t|<=epsilon_k/logY. Each pair product changes by at most twice
this amount. Thus its total change is less than

\[
 2\binom{2k}{2}\frac{1+\pi}{100k^2}<\frac15<\frac\gamma2.
\]

The strict first inequality follows already from pi<4 and 2k-1<2k.
Since the paired pair sum is real, it remains at most -gamma/2.

The logarithmic expansion was also checked directly:

\[
 \log\frac{1-x\sum_i v_i}{\prod_i(1-xv_i)}
       =-x^2\sum_{i<j}v_iv_j+O_k(x^3).
\]

The linear terms cancel. The quadratic coefficient is negative the
complete pair sum, not only the cross-pair sum. Pairing the denominator
logarithms avoids a logarithm-branch issue. The cutoff gives a uniform
Taylor remainder, and sum_p (Np)^(-3sigma) converges because sigma>1/3.

Put rho=1-2sigma>0. Primes in [Y/2,Y] are eventually inside
[Y^(a_k),Y]; the fixed deleted primes have disappeared below its lower
endpoint. The classical fixed-field prime ideal theorem gives
gg Y/logY primes there, so their total positive quadratic contribution
is gg Y^rho/logY. The entire adverse lower-prime contribution costs at
most O(Y^(a_k rho)) by ideal counting. This is smaller since a_k<1
is fixed. All cubic remainders cost O(1). Hence the stated uniform
positive collision exponent follows.

I opened A. Burgin's primary manuscript
[arXiv:2406.08565v2](https://arxiv.org/html/2406.08565v2) and checked
Theorem 1, Lemma 1, and the ideal-count statement in Section 1.3.
The prime ideal theorem remains a named classical input. I did not
independently reprove its full argument or claim an effective threshold.

## 4. I reconstructed the actual short-factor lower bound

The lower-bound lemma is unusually useful because it does not require
any special Möbius cancellation or nonvanishing hypothesis. Its proof
uses the unit coefficient, a uniform absolute-chamber anchor, and finite
exponential type.

For individual ideals over the Eisenstein field, the coefficient of
integer norm n in zeta_K is at most d(n), as is checked at split, inert,
and ramified rational primes. Consequently

\[
 |T(4+i\tau)-1|\le\zeta_K(4)-1
 \le\zeta(4)^2-1
 \le(53/48)^2-1=505/2304<1/4.
\]

The bound is unchanged by row zeros, exclusions, arbitrary unit phases,
or imaginary shifts. A product of m such factors therefore has modulus
at least (3/4)^m at s=4. In particular, there is no gap from a possible
zero of a short Möbius polynomial on the target subcritical line.

For Re s>=sigma, each derivative of order N multiplies a coefficient
by at most (m logY)^N. The absolute coefficient mass is at most
C_(K,sigma)^m Y^(m(1-sigma)). This gives a derivative estimate with its
full explicit dependence on N; it remains valid when N grows as logY.

At N=ceil(100m logY) equally spaced nodes on the vertical segment of
length epsilon/logY, all distances to the anchor are at most five.
The complex divided-difference remainder is bounded by the derivative
supremum times 5^N/N!. Its barycentric integral formula is valid on
the convex hull of the complex nodes and anchor, so no false real
mean-value theorem is used. Since N!>=(N/e)^N, the remainder is at
most

\[
 C^mY^{m(1-\sigma)}(5em\log Y/N)^N=o(1).
\]

The node separation is epsilon/((N-1)logY), and the Lagrange coefficient
sum is at most (10e logY/epsilon)^(N-1). Thus at least one actual
product value at a prescribed node is at least
exp[-C logY loglogY]. The successful node can depend on the arithmetic
coefficients, as is allowed when refuting a statement uniform over all
frequencies. The grid itself is prescribed without using them.

For the root's product one takes m=k and repeats the two shifts with
multiplicities n_+, n_-. This handles their simultaneous non-smallness
as one product. It does not multiply separate lower bounds at different
frequencies.

I also checked the optional one-dimensional positive-measure corollary.
The first derivative bound produces a neighborhood of the successful
central node on which half the lower modulus survives; its length costs
only another exp[-C logY loglogY]. The manuscript correctly says that
this is not a full-dimensional signed-integral lower bound. This
corollary is not needed for CT1's pointwise refutation.

## 5. The short-trace composition and its precise endpoint

At the successful node, the complete trace is bounded below by

\[
 \exp\left(cY^{1-2\sigma}/\log Y
                      -C\log Y\log\log Y\right).
\]

The first term dominates the second at every fixed sigma<1/2, yielding
the displayed superpolynomial lower bound after reducing c. This is
uniform along every sufficiently large Y, although the chosen grid node
can change with Y.

The two nonempty left-frequency clusters are separated by pi/logY.
If one vector belonged to WT1, that separation would be at most
2kappa/logY. The source requires kappa<arcsin(1/sqrt(2k))<pi/2,
so membership is impossible. Every chosen frequency is itself
O_k(1/logY), making the allowed polynomial frequency weight bounded.
Since H=D^h and Y=bD, every fixed H D^a remains polynomial in Y.
This completes the contradiction to CT1, including its original
1<h<=11/10 range and any fixed-power relaxation.

The following conclusions are **not** included in this review:

- A contradiction to the exact filtered identity SC4. Its simultaneous
  norm tests can annihilate the large out-of-horizon coefficients.
- A lower bound for the complete multivariate frequency integral. The
  paired locus alone does not give one.
- A contradiction to the earlier common-tube decay. The constructed
  frequencies are outside that tube.
- A refutation of the critical-line P13 contract **by the short-trace
  argument alone**. Its second-order mechanism changes at sigma=1/2;
  P13 is instead refuted by the independent argument reviewed below.
- A new native generalized-moment estimate, or a zero-free/RH result.

The smallest load-bearing external input for the asymptotic resonance
is a fixed positive-density supply of prime ideals in [Y/2,Y]. The
smallest source-fidelity requirement is that CT1 estimates its actual
unfiltered short trace for the legal fixed cross-pair mask. Both are
explicit in the frozen targets. I found no missing local mathematical
step at the stated scope.

## 6. Independent check of the original Euler-trace resonance

I read the entire separate `EULER_TRACE_RESONANCE.md` at the hash in
the target table. Its object is the original finite polynomial
\(\mathcal C\), not \(Q_{\rm coll}\prod_iT_i\). Its proof uses the
same legal cross-pair mask to make \(\mathcal C\) positive for every
row on every paired frequency vector. That source specialization also
works at k=1, where the only cross-pair consists of the two slots.

The prescribed frequency is t_Y=pi/logY on every left slot and its
negative on every right slot. On the unit row, the local factor is

\[
 1-2kq^{-\sigma_0}\cos(\pi\log q/\log Y).
\]

For q in (Y^(3/4),Y], the cosine is at most -1/2, so its logarithm
is at least (k/2)q^(-sigma_0). The two numerical inequalities used
are valid on their full claimed intervals: log(1+z)>=z/2 for 0<=z<=1,
and log(1-z)>=-2z for 0<=z<=1/2. The fixed mask ensures the arguments
lie in those intervals. On all smaller eligible primes, the logarithm
is at least -4kq^(-sigma_0), regardless of the cosine's sign.

The top prime dyad therefore contributes
gg Y^(1-sigma_0)/logY, while ideal counting bounds every possible
negative lower-prime contribution by O(Y^((3/4)(1-sigma_0))).
The latter is smaller for every fixed 0<sigma_0<1. This argument uses
exact logarithm inequalities, so it needs no cubic-remainder convergence
and legitimately extends below sigma_0=1/3.

The unit row lower bound is a lower bound for the **complete positive
row trace**, giving exp(cY^(1-sigma_0)/logY). It is at least one in
the spatial majorant once H>=1. The finite Euler product has a uniform
row bound at fixed Y, so its complete row sum converges. At sigma_0=1/2
the lower bound is exp(c sqrtY/logY), which exceeds every proposed fixed
power of D and H at the prescribed small frequency. This directly
refutes the actual original P13 with its original source data and no
short-polynomial replacement.

Unlike the CT1 resonance, this vector lies on the common conjugate slice.
There is no contradiction with the known collision-ratio decay there:
the original numerator \(\mathcal C\) includes its exponentially large
individual finite Euler factors, while the ratio theorem divides them
out. I checked that the source P13 actually estimates \(\mathcal C\)
and not that ratio. The distinction is explicitly preserved in the
reviewed manuscript.

The first-order Euler proof is consequently independent of the
short-factor interpolation proof. Conversely, it alone does not refute
the shortened CT1 object. The two theorems expose two separate failures,
and their shared fixed mask does not identify the two functions.

## Work performed and limits

I read and reconstructed the analytic proofs and checked the source
specializations just listed. I compared the frozen short-factor file
byte-for-byte with the complete extraction-agent manuscript I had read;
they agree. I computed all three target hashes. The CT1 target's revision
from `f76370ff79f9ff5be3fd13dc440b4801e4bb8b2db7363a6c143d6cd3cbb41459`
corrects opening TeX delimiters, adds the fixed-Y convergence paragraph,
and references the new separate P13 theorem; I checked those additions
and the resulting final text. I did not run a zeta-zero
calculation, infer an asymptotic theorem from a finite experiment, review
new computation code for the root packet, or perform a Lean build.
Any separately committed diagnostic has its own narrower review boundary.
