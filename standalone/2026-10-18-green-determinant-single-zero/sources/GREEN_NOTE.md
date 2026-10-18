# On Landau-Siegel zeros — mathematical transcription of the supplied note

**Source, not a new Gettysburg theorem.** The five-page user-supplied PDF prints
BEN GREEN as author and `hexagon:2610.00311v1` as its identifier. Authorship and
publication provenance have not been independently authenticated. This file is
a mathematical transcription, not a byte-identical PDF or a verbatim prose
transcript. Its section order, claims, notation and proof steps follow the
supplied note. The unchanged PDF is bound by IMPORT.md and accompanies the
conversation's downloadable packet; it is not stored in this Git directory.
No license for the supplied note is inferred from the surrounding repository.

## 1. Introduction (source page 1)

The note describes a variant of OpenAI's proof of the nonexistence of
Landau-Siegel zeros. It reports a ChatGPT 6 Astra session followed by the
attributed author's rewriting, and claims no human originality. Its two
stated advantages are to work entirely in Q(sqrt(d)), rather than adjoining
sqrt(2), and to replace algorithmic linear-algebraic interpolation by an
explicit determinant and resultant argument. The Banks and Kerr expositions
are credited; Banks is described as explicit in constants and Kerr as six
pages modulo a result of Masser.

Throughout, chi is primitive, nonprincipal and real, of sufficiently large
conductor q, with chi(p)=(d|p) at primes not dividing q. C is a sufficiently
large multiple of 3. Put X=q^C.

**Theorem 1.1 (as supplied).**

    sum_(p<=X, chi(p)=-1) log(p)/p <= (3/4)log(X)+O_C(1).

The note compares this with the trivial leading coefficient 1 and refers to
OpenAI for the analytic deduction excluding Landau-Siegel zeros.

## 2. Sketch of the proof (source pages 1-2)

Set K=Q(sqrt(d)), R=X, S=floor(X/C), N=X^(2/3). Enumerate the N^2 points

    P_i=(x+y sqrt(d), x-y sqrt(d)), 0<=x,y<N, x,y integers.

For 0<=r<R, 0<=s<S define the row of N^3 ordinary derivatives

    v_(r,s)=(partial_z^j [z^r (z')^s](P_i))_(i<=N^2, 0<=j<N).

The Gram matrix G has rational integer entries, using the coordinatewise
pairing <alpha,beta>=Tr_(K/Q)(alpha conjugate(beta)), where the bar means
complex conjugation. The proof establishes det(G)>0, an archimedean upper
bound, and high p-adic divisibility at inert primes. The positive integer
determinant is at least the product of its known prime-power divisors.

## 3. The Gram matrix is nonsingular (source pages 2-3)

**Lemma 3.1 (as supplied).** Suppose P_i=(z_i,z'_i), 1<=i<=n, have pairwise
distinct second coordinates and, for every nonzero F in C[z,w],

    #{i:F(P_i)=0} <= N deg(F).                             (3.1)

If

    n > 2RS/N + R + S,                                   (3.2)

then the RS rows of ordinary jets of z^r(z')^s, with i<=n and j<N,
are linearly independent. For the quadratic grid the incidence bound is
Schwarz-Zippel after an invertible linear change of variables, and the
chosen parameters satisfy (3.2).

Proof. A dependence gives a nonzero polynomial F of separate degrees at
most (R,S), all of whose z-derivatives of orders j<N vanish at every P_i.
Factor over C as

    F(z,z')=F_0(z') product_(ell=1)^k F_ell(z,z'),

with repeated irreducible factors permitted and d_ell=deg_z(F_ell)>0.
Write d'_ell=deg_(z')(F_ell), including ell=0. Then

    sum_(ell>=1)d_ell <= R,  sum_(ell>=0)d'_ell <= S.       (3.4)

No specialization F_ell(z,z'_i) is the zero polynomial. For each such
irreducible factor, the resultant inequality is

    ord_(z=z_i) F_ell(z,z'_i)
       <= 1+ord_(z'=z'_i) Res_z(F_ell,partial_z F_ell).    (3.5)

The source at this point prints the unresolved reference “Appendix ??”;
its following page identifies Appendix A and Lemma A.1. The resultant is
nonzero, of z'-degree at most 2d_ell d'_ell. Incidence (3.1), distinctness
of the z'_i, and (3.5) give

    sum_i ord_(z=z_i)F_ell(z,z'_i)
       <= N(d_ell+d'_ell)+2d_ell d'_ell.                  (3.6)

Remove the at most d'_0 indices at which F_0 vanishes. At all remaining
indices F has z-multiplicity at least N. Summing the preceding bound over
factors yields

    N(n-d'_0) <= N(R+S-d'_0)+2RS,

using sum d_ell d'_ell <= (sum d_ell)(sum d'_ell). This contradicts
(3.2). Therefore the rows are independent and their Gram determinant is
positive. QED.

## 4. Archimedean bound (source page 3)

Hadamard gives det(G)<=product_(r,s)||v_(r,s)||_2^2. The points satisfy
|x +/- y sqrt(d)|<=N(1+sqrt(|d|))<=2N sqrt(q). The note uses the bound
R^N(2N sqrt(q))^(r+s) for the size of a derivative entry, so that

    ||v_(r,s)||_2 << N^(3/2) R^N (2N sqrt(q))^(r+s).

Consequently it displays

    log det(G) <= 3RS log(N)+2NRS log(R)
                    +RS(R+S)log(2N sqrt(q))
               =RS(R+S)log(2N sqrt(q))+O(X^3).            (4.2)

These are the source's bounds; constants and its displayed coarse
inequality have not been silently strengthened in this transcription.

## 5. p-adic bound (source pages 3-4)

For odd p with chi(p)=-1 let e_p=v_p(det G).

**Lemma 5.1 (as supplied).**

    e_p >= 2 sum_(0<=r<R,0<=s<S) min(floor(r/p),S-1-s).

Proof. Order rows by increasing r. Put psi(z,z')=z^p-z'. At each grid point
psi(P_i) lies in p Z[sqrt(d)], by

    (sqrt(d))^p = d^((p-1)/2)sqrt(d) == -sqrt(d) (mod p),
    (x+y sqrt(d))^p == x-y sqrt(d) (mod p).

For fixed r,s let h=min(floor(r/p),S-1-s), and replace the row by jets of

    z^(r-ph) psi(z,z')^h (z')^s.                          (5.1)

Every entry of this replacement is divisible by p^h: both psi(P_i) and
every positive ordinary z-derivative of psi are divisible by p, and the
repeated product rule retains one such factor for each of the h copies.
Expanding psi^h shows exactly

    vtilde_(r,s)=v_(r,s)+sum_(i=1)^h (-1)^i binom(h,i)v_(r-pi,s+i).

All indicated indices lie in the original rectangle. This is a unipotent
triangular row transformation. Its corresponding Gram congruence preserves
the determinant. From the new Gram entry one may extract p^h from the
row and the analogous power from the column. The total extracted exponent
is twice the sum of h, proving the lemma. QED.

## 6. Completion of the proof (source pages 4-5)

Combining the two bounds gives

    sum_(p<=X,chi(p)=-1) log(p) sum_(r,s)min(floor(r/p),S-1-s)
       <= (1/2)RS(R+S)log(2N sqrt(q))+O(X^3).             (6.1)

The note uses

    sum_(0<=s<S) min(k,S-1-s) >= Sk-k^2

and replaces floor(r/p) by r/p, at total cost O(X^3). It obtains a lower
bound (1/2)SR^2 sum_(p<=X,chi(p)=-1)log(p)/p-O(X^3) for the left side.
Substituting R=X, S approximately X/C, N=X^(2/3), q=X^(1/C) yields

    sum_(p<=X,chi(p)=-1)log(p)/p
       <= (1+1/C)(2/3+1/(2C))log(X)+O_C(1).

Taking C sufficiently large gives Theorem 1.1. The source's final display
for this step suppresses the harmless integer rounding of S.

## Appendix A. Resultants (source page 5)

For f,g in k[z] of degrees d,e, the Sylvester matrix represents

    Phi:k[z]_<e direct_sum k[z]_<d -> k[z]_<d+e,
    Phi(P,Q)=fP+gQ

in descending monomial bases. Its determinant Res_z(f,g) vanishes exactly
when f,g have a nonconstant common factor.

For irreducible f in C[z,z'] of separate degrees (d,d'), d>0, with
k=C(z') and g=partial_z f, the resultant is nonzero. Its (2d-1)-square
Sylvester matrix has polynomial entries of z'-degree at most d', whence

    deg_(z')Res_z(f,partial_z f) <= 2dd'.                  (A.1)

**Lemma A.1 (as supplied).** If f(z,z'_0) is not identically zero and has
a root of multiplicity mu>=1 at z_0, then

    ord_(z=z_0) f(z,z'_0)
       <= 1+ord_(z'=z'_0)Res_z(f,partial_z f).

Proof. After specialization, both f and its derivative have the factor
(z-z_0)^(mu-1), so the image of Phi has dimension at most
(2d-1)-(mu-1)=2d-mu. There are mu-1 independent left-null vectors of the
specialized Sylvester matrix. Complete them to an invertible constant
row-basis matrix U. The first mu-1 rows of U S(z') are all divisible by
z'-z'_0. Thus its determinant, and hence det S up to the nonzero factor
det U, vanishes to order at least mu-1. QED.

## References printed in the source

1. W. D. Banks, On the OpenAI proof that Landau-Siegel zeros do not exist,
   arXiv:2610.15483.
2. B. Kerr, A simpler proof that there are no Landau-Siegel zeros,
   arXiv:2610.21099.
3. OpenAI, Uniform exclusion of Landau-Siegel zeros, OpenAI Math Release
   preprint (2026), “Available online”.

The source prints ben.green@maths.ox.ac.uk as the contact address.
References 1 and 2 are preserved as source bibliography, not represented
as newly fetched, checked, or imported papers.
