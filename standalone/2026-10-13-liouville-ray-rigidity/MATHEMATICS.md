# Prime-preserving surgery for the native sextic moment

Status: PROPOSED component proofs and a changed analytic target. No improved
moment exponent, zero-free boundary, or RH proof is asserted. The author has
checked the arguments and finite algebra; independent mathematical review is
still required.

Scope: fixed Eisenstein field K=Q(omega); every fixed moment order; the actual
finite-height element rows; arbitrary original exclusion ideals. The first
three sections need no theta theorem, GRH, or large sieve. Section 4 uses only
the named classical fixed-field Hecke facts and prime ideal theorem.

## 1. An admissible change of coefficients

Let S contain the fixed bad primes. Fix an additional ideal Q and a unitary
finite-order ideal character nu outside S. Extend the native symbol to all
integral ideals by

    chi_n(u) = product_{p^e || n} chi_p(u)^e,
    xi_u(n) = nu(n) chi_n(u).

The extension is completely multiplicative in n, INCLUDING its zeros: a
positive multiple of six in the exponent does not turn a zero into one.
Use only ideals prime to SQ. All sums below include the unit ideal whenever
the test permits it. Let W be fixed, supported on [a,b] inside (0,infinity).
Define

    A_u(X) = sum_n mu_K(n) xi_u(n) W(Nn/X),
    B_u(X) = sum_n lambda_K(n) xi_u(n) W(Nn/X),
    lambda_K(n) = (-1)^{Omega_K(n)}.

A is the original polynomial. B changes only prime-power coefficients of
exponent at least two: lambda(p)=mu(p)=-1 at EVERY good prime. It is not a
prime-only selection or a random sign replacement.

### Theorem 1. Exact reversible square convolution

For every row, scale, test, and original exclusion,

    B_u(X) = sum_{(d,SQ)=1} xi_u(d)^2 A_u(X/(Nd)^2),                 (1)
    A_u(X) = sum_{(d,SQ)=1} mu_K(d) xi_u(d)^2 B_u(X/(Nd)^2).         (2)

All displayed sums are finite: Nd <= sqrt(bX). The shorter polynomial keeps
the SAME exclusion Q. There is NO additional condition between d and its
residual ideal.

Proof. The classical coefficient identities are

    lambda(n) = sum_{d^2|n} mu(n/d^2),
    mu(n) = sum_{d^2|n} mu(d) lambda(n/d^2).

At n=p^e the first sum has one nonzero term, with residual exponent zero or
one, giving (-1)^e. In the second sum only d=1 and, when e>=2, d=p
contribute. They cancel when e>=2; for e=0,1 they give 1,-1. Multiplicativity
proves both identities on ideals. Multiplying by xi_u(n) is valid even at
nonunits, since xi_u(n)=xi_u(d)^2 xi_u(n/d^2) literally. Insert the finite
weight and regroup. A factor of n is prime to SQ whenever n is, and the
converse holds for the reconstructed product. This proves (1)-(2).

Example: at n=p^3, the forward identity needs d=p and residual p. Adding
(d,residual)=1 would delete its only nonzero term. At n=p^2, the signed
inverse is 1-1=0; taking its absolute values changes the source.

The integer square-divisor identity is classical, not a discovery of this
packet; see NIST DLMF 27.6.1 and Mobius inversion. The contribution here is
its explicit same-height, zero-preserving use for the native family.

### Theorem 2. No power loss at any fixed moment order

Fix ANY nonnegative finite row measure w, the SAME at every column scale.
It can be the sharp element ball 0<Nu<=H or a summable smooth weight, with
all units and repeated-prime rows retained. Let p>=1, sigma>=1/2, and D>=1/b.
Define, with the original fixed Q and W,

    E_A(sigma,D;w) = sup_{1/b <= X <= D} X^{-sigma} ||A(X)||_{L^p(w)},

and define E_B similarly. Then

    E_B <= C_sigma(D) E_A,      E_A <= C_sigma(D) E_B,               (3)
    C_sigma(D) = sum_{Nd <= sqrt(bD)} (Nd)^{-2 sigma}.

In particular

    C_{1/2}(D) <= C_{K,b} log(2+D),
    C_{1/2+delta}(D) <= zeta_K(1+2 delta),   delta>0.               (4)

The constants are independent of H, Q, the chosen rows, and nu.

Proof. Multiplication by xi_u(d)^2 has operator norm at most one on L^p(w).
Apply Minkowski to (1) or (2), use |mu(d)|<=1, and put Y=X/(Nd)^2.
Terms with Y<1/b are zero. Every remaining Y is inside the SAME envelope;
X^{-sigma}Y^sigma=(Nd)^{-2sigma}. This proves (3). Fixed-field ideal
counting # {n:Nn<=T}=O_K(T), followed by partial summation, proves the first
bound in (4). The second follows from the absolutely convergent defining
series of zeta_K; no zero-free assertion is used.

For p=2k this compares the complete normalized moment envelopes in both
directions with factor O(log(2+D)^{2k}). Thus a bound

    sum_u w_H(u)|A_u(X)|^{2k} <= C H X^k D^{e_k+epsilon}
    for ALL 1/b<=X<=D at this SAME H                              (5)

transfers to B with the SAME power excess e_k, after an arbitrarily small
adjustment of epsilon; the converse also holds. A family of tests with a
common support can be put under the supremum without changing the argument.
Moment order k is fixed before D grows.

IMPORTANT: an estimate available only at H=X^h does NOT supply (5) at the
larger fixed height H=D^h. This theorem does not solve that adapter problem.
The same-height issue was already emphasized in PR #916. It is explicit here
rather than hidden in the scale change.

## 2. Exact tensor collapse, without collision repairs

For arbitrary fixed profiles W_i and lengths X_i, set

    d_{W,X}(n) = sum_{n_1 ... n_k=n} product_i W_i(Nn_i/X_i),

where the sum is over ordered factorizations, NOT coprime factorizations.
Every factor and product is prime to the original SQ. Complete
multiplicativity now gives the exact identity

    product_i B_u(X_i;W_i)
      = sum_n lambda_K(n) nu(n) chi_n(u) d_{W,X}(n).                (6)

Proof. Expand the finite left side and regroup by the PRODUCT IDEAL. The
product of the Liouville signs is lambda_K(n), even when factors share
primes; the product of the symbols is chi_n(u), including zero values.
The residual coefficient is precisely d_{W,X}. Distinct ideals of equal
norm are not identified. No coefficient averaging or absolute value is used.

For equal profiles and lengths this gives

    sum_u w_H(u)|B_u(X)|^{2k}
      = sum_u w_H(u)|sum_n lambda_K(n)nu(n)chi_n(u)d_{k,W,X}(n)|^2. (7)

When W>=0 the divisor profile is nonnegative, but the displayed Dirichlet
polynomial still has its exact Liouville signs. It is supported at product
norm comparable to X^k, and |d_{k,W,X}(n)|<=||W||_infinity^k d_k(n).
Replacing it by an arbitrary bounded coefficient sequence is NOT licensed.

Equations (3) and (7) provide a coefficient-specific second-moment target
for the full 2k-th moment. They remove squarefreeness and the need to
separate tensor factors by new gcd masks BEFORE estimating the full norm.
They do not remove the long product support or prove its signed covariance
small. Nor is the physical product diagonal the only complete-residue
principal correlation: sixth-power aliases still have to be retained.

## 3. Prime rooting with its entire companion

Let aX>1, so the unit ideal has no contribution. Put

    V_X(t) = W(t)/log(Xt) on the support of W, zero elsewhere.

This is smooth there. The following finite identity has no new p-exclusion:

    B_u(X;W)
      = sum_{p not dividing SQ} sum_{j>=1}
          (log Np) (-xi_u(p))^j B_u(X/(Np)^j; V_X).                (8)

Proof. For n=p^j m, complete multiplicativity makes its coefficient
lambda(n)xi_u(n). Its weights sum to

    [sum_{p^j|n} log Np]/log Nn = 1.

The equality is the elementary prime-power identity for log Nn. It remains
valid when p divides m and when the row is nonunit at p. The j>=2 terms and
the m=1 endpoint must not be dropped. This is the Liouville counterpart of
PR #933's native prime-rooting identity, retaining the entire composite
companion without its changing coprimality mask.

For Re(s)>1, the associated Euler series is

    sum_n lambda(n)xi_u(n)(Nn)^(-s)
       = L^{SQ}(2s,xi_u^2)/L^{SQ}(s,xi_u).                        (9)

This is an Euler-factor calculation, not an assertion of convergence on the
critical line. In Re(s)>1/2 the numerator's Euler product is holomorphic and
nonzero. Thus it cannot cancel a pole caused by a zero of the denominator in
that half-plane. The change of coefficients preserves, rather than resolves,
the zero-free problem.

**Attempt boundary.** Taking a generic large-sieve norm of (7) forgets the
Liouville/divisor-profile structure and leaves the length X^k. Taking
absolute values in (8) forgets the prime-composite cancellation. Neither
operation has produced a power saving in this pass. The new target is (7)
with bound H X^{k+epsilon}, at all shorter X and the original common H.

## 4. A rigidity theorem for changes at the primes

This explains why the prime-preserving change above is fundamentally safer
than changing the prime signs themselves.

Fix a finite abelian quotient G of a ray class group of K. Let g(n) be its
ideal class map and include its modulus primes in S. Let a:G->C satisfy
|a(g)|<=1. Define the squarefree multiplicative function

    f_a(n) = mu_K(n)^2 product_{p|n} a(g(p)),     (n,S)=1.

For eta in the character group of G, set

    T_{eta,u}(D) = sum_n f_a(n) conjugate(eta(g(n))) chi_n(u) W(Nn/D),
    M_{eta,2k}(D,H) = sum_{0<Nu<=H}|T_{eta,u}(D)|^{2k},
    c_eta = (1/|G|) sum_g a(g) conjugate(eta(g)).

Here W is fixed, nonzero, nonnegative, and smooth of compact support in
(0,infinity). All these eta are fixed finite-order twists permitted by the
native setup. No growing modulus or growing field is involved.

### Theorem 3. Finite-ray rigidity

If, for one fixed integer k>=1 and one fixed 0<h<6k/5, EVERY eta satisfies

    M_{eta,2k}(D,D^h) = O_{eta,epsilon}(D^{h+k+epsilon})
    for every epsilon>0,                                        (10)

then necessarily

    a(g) identically 0, OR a(g) = -eta_0(g) for one character eta_0. (11)

This is a NECESSARY classification. It does NOT assert (10) for the
remaining Mobius-character functions. In the nonzero case,
f_a(n)=mu_K(n)eta_0(g(n)) exactly.

More quantitatively, whenever c_eta is not a nonpositive integer,

    limsup_{D->infinity} log(1+M_{eta,2k}(D,D^h))/log D
        >= 2k+h/6                                               (12)

for every fixed h>0 and k>=1.

### Proof of the rigidity theorem

**Step 1: isolate each Fourier coefficient analytically.** For Re(s)>1,

    F_eta(s) = sum_n f_a(n) conjugate(eta(g(n))) (Nn)^(-s)
             = product_p (1+a(g(p)) conjugate(eta(g(p))) (Np)^(-s)).

Fourier inversion a(g)=sum_psi c_psi psi(g) gives

    F_eta(s) = E_eta(s) product_psi L^S(s,psi conjugate(eta))^{c_psi}. (13)

For E_eta the linear terms of each local logarithm cancel. Its logarithm
is a normally convergent sum of O((Np)^(-2 Re(s))) on each half-plane
Re(s)>1/2+delta. All local factors are nonzero near s=1 since |a|<=1
and Np>=2. Its germ is therefore holomorphic and nonzero there.

The classical fixed-field facts used here are: the Dedekind zeta function
has a simple pole of positive residue at one; nontrivial finite-order Hecke
L-functions are holomorphic and nonzero at one. The latter nonvanishing also
follows from the abelian class-field zeta factorization: the product over
nontrivial characters is a ratio of two Dedekind zeta functions with finite
nonzero limit at one, and each factor is holomorphic there. These are named
classical inputs, not consequences of any imported quasi-RH manuscript.
After continuation from real s>1 to a sufficiently small slit neighborhood,
(13) has the form

    F_eta(s) = (s-1)^(-c_eta) U_eta(s),       U_eta(1) != 0.         (14)

This germ can be holomorphic across one only if -c_eta is a nonnegative
integer. Indeed a nonzero holomorphic germ has an integer zero order m,
whereas (s-1)F'_eta/F_eta tends to -c_eta. No branch choice changes this
logarithmic derivative. A positive integer c_eta instead gives a pole.

**Step 2: the singularity forces large principal sums.** If c_eta is not a
nonpositive integer, T_{eta,1}(D) is not O(D^{1-delta}) for ANY delta>0.
Otherwise its Mellin integral in D would be holomorphic for Re(s)>1-delta
and equal to W_hat(s)F_eta(s) for Re(s)>1. Since W_hat(1)>0, this would
extend F_eta through one, contradicting (14). The integral has no small-D
problem because the compact support makes the sum vanish below 1/b.

**Step 3: retain literal sixth-power copies.** Put Y=D^{h/6}. For every
prime ideal r outside S with Y/2<Nr<=Y, choose a generator r (K has class
number one) and the element row u=r^6. The six possible unit choices give
the same sixth power; distinct prime ideals give distinct rows. On these
rows chi_n(r^6)=1_{(n,r)=1}, including the zero at r. Since |f_a(n)|<=1,

    |T_{eta,r^6}(D)-T_{eta,1}(D)| <= C_W(D/Nr+1),                 (15)

with the left side exactly zero if Nr>bD. Fixed-field ideal counting
proves (15). The prime ideal theorem gives at least cY/log Y such rows.
For arbitrarily large D, Step 2 gives |T_{eta,1}(D)|>D^{1-delta}.
Choose 0<delta<min(1,h/6); (15) is smaller than half this value eventually.
Positivity of the FULL moment then gives, on those scales,

    M_{eta,2k}(D,D^h) >= c D^{2k(1-delta)+h/6}/log D.

Let delta tend to zero after taking the upper limit. This proves (12).
It uses only ordinary prime ideal counting in a fixed field, NOT a prime
ideal theorem with moving ray classes. The amplification mechanism is
credited to PR #933, Section 4; the Fourier classification is its extension.

**Step 4: Fourier integrality is rigid.** Since h<6k/5, (10) contradicts
(12) for any illegal coefficient. Hence every c_eta is a nonpositive
integer. Parseval gives

    sum_eta |c_eta|^2 = (1/|G|) sum_g |a(g)|^2 <= 1.

Thus all coefficients are zero, or exactly one is -1 and all others are
zero. Fourier inversion is precisely (11). This completes the proof.

### Consequences and limitations

* A continuous family of such prime patterns, on a connected parameter
  interval, cannot move while satisfying (10) at every parameter: its values
  are confined to the finite set (11). Constants in (10) need not be uniform
  in the parameter for this conclusion.
* In particular an admissible nonzero prime pattern has modulus one at
  EVERY ray class. Uniformity over a large box of unrelated prime phases
  is not a harmless strengthening of the native conjecture.
* This does not classify arbitrary a(p) varying on infinitely many classes,
  a growing ray modulus, a single untwisted moment, or higher-prime-power
  Euler coefficients. The latter are precisely where (1)-(2) make an actual
  change possible without touching the rigid first-degree data.
* Liouville transfer and the rigidity argument are separate component
  theorems. Neither implies that the remaining arithmetic moment is small.

## Sources, reading scope, and priority

- PR #933, 8685591132bc6f283f670d252121c1629df3a208,
  `standalone/2026-10-13-sextic-structural-strike/PRIME_DEGREE_COHERENCE.md`:
  actual text read, including the scalar deformation, sixth-power copying,
  and rooted companion. The singularity/copy mechanism is credited there.
- PR #916: PR description read for the common-height envelope warning and
  prior collision removal; its detailed proof is not an input to this note.
- PRs #930, #932, #934: descriptions read for adjacent scope; no analytic
  theorem from them is invoked. #934's limitations within one exponent
  bookkeeping architecture do not refute a sufficiently strong moment
  criterion in a different extraction argument.
- Historical PR #356 already uses Liouville and convolution descendants in
  a different positivity problem; only its description was read. No claim
  to first use of Liouville or of convolution in this repository is made.
- Classical square-divisor identity: https://dlmf.nist.gov/27.6 (27.6.1).
  The ideal version and the inverse used here are proved above.
- Fourier orthogonality, fixed-field ideal counting, the prime ideal theorem,
  and finite-order Hecke theory at s=1 are named classical inputs. No
  Selberg-Delange asymptotic, large sieve, or theta transformation is used.

The specific physical-envelope transfer and finite-ray necessity deduction
are proposed here for review. A global literature or all-branch priority
search was not performed. The full generalized moment and RH remain open.
