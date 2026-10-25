# Coherent logarithmic transport of the actual inverse coefficients

Status: exploratory analytic reduction, with complete elementary identities;
no new zero-free half-plane is claimed.

Scope: one fixed number field, its integral ideals outside a fixed finite set
\(S\), and a unitary completely multiplicative character presentation,
including its original zeros on nonunits. In particular
\(|\psi(\mathfrak n)|\le1\). All identities are finite before any analytic
estimate. The rational version is obtained by replacing ideals by positive
integers. Every ideal sum and Euler product below uses this same omitted set
\(S\); the character's additional nonunit zeros are also retained throughout.

Sources: Liu, arXiv:2610.26835v1, Sections 13.3--13.4 and 15.2; the standard
Dirichlet-convolution identities, proved below. The use proposed here is to
couple the detectors at different cutoffs before taking their separate bounds.
This note does not claim priority for the logarithmic Möbius identity or for
Buchstab decomposition.

What was run: `check_log_transport.py` in ordinary and optimized isolated
Python. The exact formal-logarithm checks cover 1,536 coefficient predicates
through integer 512, 2,560 rough-splitting predicates, and 3,280 products of
a character retaining its nonunit zeros. Eight prime-only mutations are
rejected. These finite checks do not certify an analytic moment or boundary.

Smallest remaining gap: a signed joint estimate for the prime/short-inverse
products at the *same character and the same Mellin frequency*. Applying the
currently supplied inverse moment separately to these products does not
improve the long-column exponent.

## 1. Why this tests a different mechanism

Liu's critical-count min--max allows a zero detector at each cutoff to choose
its own adverse length split. His Section 15.2 explicitly distinguishes an
improvement based on additional relations between those choices from another
optimization of the marginal bounds. A genuine Möbius coefficient cannot
choose its values independently at all scales. The following transport
identity is one exact relation. It preserves the actual coefficient, rather
than replacing it by an arbitrary vector or a Gauss-weighted vector.

Let \(\mu_F\) and \(\Lambda_F\) denote the ideal Möbius and von Mangoldt
functions. For a common zero-extended character \(\psi\), every scale
\(H>0\), and \(W\in C_c^\infty((1,2))\), put

\[
 M_H[W;\psi]
 =H^{-1/2}\sum_{\mathfrak n}\mu_F(\mathfrak n)\psi(\mathfrak n)
                       W(N\mathfrak n/H).
\]

This definition includes the shorter scales below \(2\) that occur in the
transport identity. Take \(D\ge2\) and
\(V\in C_c^\infty((1,2))\). Set

\[
 V_D(x)=\frac{\log D}{\log(Dx)}V(x).
\tag{1.1}
\]

For every fixed derivative order, the smooth seminorms of \(V_D\) are bounded
by a constant times the corresponding finite seminorms of \(V\), uniformly
for \(D\ge2\). The denominator is at least \(\log D\) on this support.

### Proposition 1: exact transport, without a logarithmic remainder

\[
 \boxed{
 M_D[V;\psi]=-
 \frac1{\log D}\sum_{\mathfrak p}\sum_{j\ge1}
 \frac{\log N\mathfrak p\,\psi(\mathfrak p)^j}
      {(N\mathfrak p)^{j/2}}
 M_{D/(N\mathfrak p)^j}[V_D;\psi].}
\tag{1.2}
\]

Only prime powers of norm below \(2D\) occur. In particular the infinite-looking
sum is finite. No primitivity, deletion of nonunit zeros, or coprimality
replacement is involved.

**Proof.** Differentiating \(\mu_F*1=\delta\), with the derivation
\((\partial a)(\mathfrak n)=a(\mathfrak n)\log N\mathfrak n\), gives
\((\partial\mu_F)*1+\mu_F*(\partial1)=0\). Convolving with \(\mu_F\)
and using \(\mu_F*\partial1=\Lambda_F\) yields

\[
 \mu_F(\mathfrak n)\log N\mathfrak n
 =-\sum_{\mathfrak d\mid\mathfrak n}
                  \mu_F(\mathfrak n/\mathfrak d)\Lambda_F(\mathfrak d).
\tag{1.3}
\]

Multiply by \(\psi(\mathfrak n)V(N\mathfrak n/D)/\log N\mathfrak n\),
then write \(\mathfrak n=\mathfrak p^j\mathfrak m\). Complete
multiplicativity, including zero values, gives
\(\psi(\mathfrak p^j\mathfrak m)=\psi(\mathfrak p)^j\psi(\mathfrak m)\).
The identity
\((N\mathfrak p)^{-j/2}(D/(N\mathfrak p)^j)^{-1/2}=D^{-1/2}\)
gives precisely (1.2). This also proves the asserted normalization. \(\square\)

The simpler identity with \(V\) instead of \(V_D\) has an additional term
\(-M_D[(\log x)V]/\log D\). It cannot simply be discarded when upper and
lower zero-detector estimates have opposing \(U^\varepsilon\) losses.
Definition (1.1) removes it exactly.

## 2. The prime-power terms and a precise maximum-envelope absorption

The terms \(j\ge2\) are essential to the exact identity. At
\(\mathfrak n=\mathfrak p^2\), the terms with divisors
\(\mathfrak p\) and \(\mathfrak p^2\) cancel. Keeping only primes would
give the false coefficient \(+\log N\mathfrak p\) on the right of (1.3).

They can nevertheless be bounded in an appropriate weighted envelope. Fix
\(a>1/2\), a finite smooth-seminorm norm \(\|\cdot\|_{\mathcal V}\), and
a constant \(C_{\mathcal V}\) for which
\(\|V_D\|_{\mathcal V}\le C_{\mathcal V}\|V\|_{\mathcal V}\).
For a fixed character and horizon \(X\), define

\[
 E_a(X;\psi)
 =\sup_{0<H\le X}\ \sup_{\|W\|_{\mathcal V}\le1}
 H^{1/2-a}|M_H[W;\psi]|,
\tag{2.1}
\]

where all profiles have the same support in \([1,2]\). This is finite:
for \(H<1/2\) the source is zero, and the remaining sums are finite.
No assertion that \(E_a\) is bounded as \(X\to\infty\) is being made.

Let \(\mathcal P_{\ge2,D}\) be the contribution of \(j\ge2\) to the
right side of (1.2). Then

\[
 |\mathcal P_{\ge2,D}|
 \le \frac{C_{\mathcal V}K_F(a)}{\log D}
       D^{a-1/2}E_a(D;\psi)\|V\|_{\mathcal V},
\quad
 K_F(a)=\sum_{\mathfrak p}\sum_{j\ge2}
                \frac{\log N\mathfrak p}{(N\mathfrak p)^{ja}}<\infty.
\tag{2.2}
\]

Indeed each shorter term is bounded by the envelope, and its remaining
prime-power factor is \((N\mathfrak p)^{-ja}\). Convergence follows from
\(2a>1\) and elementary ideal counting. At a horizon/profile satisfying
\(D^{1/2-a}|M_D[V]|\ge E_a(D;\psi)/2\), with
\(\|V\|_{\mathcal V}\le1\), the prime powers consume at most half its
magnitude once \(\log D\ge4C_{\mathcal V}K_F(a)\).

This is a legitimate maximum-envelope argument. It is not an absorption at
every zero-detected annulus. The definition (2.1) and its factor-two hypothesis
must be retained whenever (2.2) is used that way.

## 3. A simultaneous witness, and the actual existing length budget

After an exact smooth dyadic partition of the prime powers, there are
\(O(\log D)\) nonempty norm blocks. Equation (1.2) implies that at least one
block has absolute size \(\gg |M_D[V]|\), when the block includes its
\(\log N\mathfrak p\) weight and the constants of the partition. If (2.2)
has been absorbed at an envelope maximum, one can choose a block consisting
of first powers of primes.

On a prime block \(N\mathfrak p\asymp P\), write \(N=D/P\). Mellin
inversion of \(V_D(xy)\), with a harmless compact cutoff in each variable,
expresses that block as an integral of

\[
 \left(P^{-1/2}\sum_{\mathfrak p}
       \log N\mathfrak p\,\psi(\mathfrak p)
       W(N\mathfrak p/P)(N\mathfrak p/P)^{it}\right)
 \left(N^{-1/2}\sum_{\mathfrak m}
       \mu_F(\mathfrak m)\psi(\mathfrak m)
       W_1(N\mathfrak m/N)(N\mathfrak m/N)^{it}\right),
\tag{3.1}
\]

against a rapidly decreasing density with bounded weighted \(L^1\) norms.
Both factors retain the same character and the same Mellin frequency. A
moment estimate applied to (3.1) must preserve this coupling.

Now take the row scale \(U\), \(D=U^r\), and \(P=U^z\).
The inverse factor has length exponent \(r-z\), and the new prime factor
has exponent \(z\). The first currently supplied M1 inequality is

\[
 (r-z)+2z<1,\qquad\hbox{that is,}\qquad r+z<1.
\tag{3.2}
\]

For the adverse long range \(r>1\), it never holds. If pre-existing selected
prime factors have total length \(z_0\), the condition is still worse:
\(r+z+2z_0<1\). The second M1 inequality becomes
\(2r+6z+8z_0<3\). Replacing a long inverse factor by one prime and a
shorter inverse therefore does **not** bring it into the current M1 domain.

This calculation rules out a particular naive application of the identity;
it is not an arithmetic impossibility theorem. A new joint estimate, using
the signed integral (3.1) before positive majorization, would change the input.

## 4. Repeated logarithmic transport does not force short prime factors

Repeated derivatives produce exact Bell-polynomial convolutions. Writing
\(\Lambda_j(\mathfrak n)=\Lambda_F(\mathfrak n)(\log N\mathfrak n)^j\),
the first three are

\[
 \mu_F\log=-\mu_F*\Lambda_0,
\]
\[
 \mu_F\log^2=\mu_F*(\Lambda_0*\Lambda_0-\Lambda_1),
\]
\[
 \mu_F\log^3=\mu_F*(-\Lambda_0^{*3}
                         +3\Lambda_0*\Lambda_1-\Lambda_2).
\tag{4.1}
\]

These formulas follow by applying the logarithmic derivation to the preceding
line. They contain prime powers of every size allowed by the product support.
There is always a one-factor term \(-\mu_F*\Lambda_{k-1}\) at derivative
order \(k\). It includes a prime of norm comparable to the whole annulus.
Consequently even arbitrarily high fixed logarithmic order cannot, by algebra
alone, force every summand to contain many small primes.

Here is a different exact way to expose that residual. Let
\(P_Y\) be the product of prime ideals of norm at most \(Y\), and define

\[
 R_H(Y;\psi)=H^{-1/2}\sum_{(\mathfrak m,P_Y)=1}
                   \mu_F(\mathfrak m)\psi(\mathfrak m)V(N\mathfrak m/H).
\]

Unique factorization into its small-prime part and its \(Y\)-rough part gives

\[
 M_D[V;\psi]=\sum_{\mathfrak d\mid P_Y}
 \frac{\mu_F(\mathfrak d)\psi(\mathfrak d)}{\sqrt{N\mathfrak d}}
 R_{D/N\mathfrak d}(Y;\psi).
\tag{4.2}
\]

Only \(N\mathfrak d<2D\) contributes. The term \(\mathfrak d=1\) is
the complete rough inverse source. Repeated extraction of small primes does
not eliminate it.

If \(Y=D^\theta\), each rough ideal in the annulus has at most
\(\lfloor\log(2D)/\log Y\rfloor\) prime factors, but its volume is not
power-small. For fixed \(0<\theta<1\), all prime ideals in a fixed interior
subannulus are rough for sufficiently large \(D\); the prime ideal theorem
gives \(\gg_F D/\log D\) such ideals. Their character-weighted sum may of
course cancel. Cardinality alone supplies no fixed power saving.

## 5. What the inherited zero-free premise says about that rough remainder

Here \(L_F(s,\psi)\) denotes precisely the Euler product
\(\prod_{\mathfrak p\notin S}
(1-\psi(\mathfrak p)(N\mathfrak p)^{-s})^{-1}\), with the same omitted
finite primes and nonunit zeros as the coefficient sums. It is not silently
replaced by a primitive inducing \(L\)-function with different Euler factors.

For \(\Re s>1\), its Dirichlet series is exactly

\[
 \sum_{(\mathfrak n,P_Y)=1}
          \mu_F(\mathfrak n)\psi(\mathfrak n)(N\mathfrak n)^{-s}
 =\frac1{L_F(s,\psi)}
       \prod_{N\mathfrak p\le Y}
                  (1-\psi(\mathfrak p)(N\mathfrak p)^{-s})^{-1}.
\tag{5.1}
\]

For any fixed \(1/2<\sigma<1\), the elementary absolute Euler estimate is

\[
 \left|\prod_{N\mathfrak p\le Y}
                  (1-\psi(\mathfrak p)(N\mathfrak p)^{-s})^{-1}\right|
 \le \exp\!\left(C_{F,\sigma}
                     \frac{Y^{1-\sigma}}{\log(2Y)}\right).
\tag{5.2}
\]

One proves (5.2) by expanding \(-\log(1-z)\), separating its convergent
higher-power part, and using the elementary prime-ideal upper bound in the
first-power sum. If one imports the usual reciprocal bound on a line strictly
to the right of the family's zero supremum, a Mellin shift for (5.1) therefore
has this extra cost. For \(Y=(\log D)^A\), it is \(D^{o(1)}\) whenever
\(A(1-\sigma)\le1\). For \(Y=D^\theta\), this *supplied majorant* is
superpolynomial in \(D\).

This does not prove that the actual Euler correction is always large. It
identifies exactly why the existing zero-free premise plus separate absolute
Euler bounds does not eliminate the fixed-power rough cutoff in (4.2).
For \(\sigma\) just to the right of \(B_\flat\), the polylogarithmic
cutoff threshold is near \(A=1/(1-B_\flat)\), approximately 7.99; such a
cutoff still leaves an unbounded number of rough prime factors as \(D\to\infty\).

## 6. A local analytic consistency check

The transport identities themselves cannot contradict a hypothetical zero.
Indeed if \(L(s)=(s-\rho)^m h(s)\), \(m\ge1\), \(h(\rho)\ne0\), then

\[
 (1/L)'=-\left(\frac m{s-\rho}+\frac{h'}h\right)(1/L).
\]

Its repeated derivatives have leading Laurent term
\((-1)^k(m)_k h(\rho)^{-1}(s-\rho)^{-m-k}\), exactly consistent with
(4.1). This is not an arithmetic counterexample to a future joint moment.
It prevents treating differentiation or repeated logarithmic transport, by
itself, as the missing cancellation.

## 7. Concrete research target

The next meaningful task is a mean bound for the *sum over prime blocks* in
(1.2), or for its coupled products (3.1), that is strictly stronger than the
sum of their marginal M1 bounds in the adverse region \(r>1\). It should
retain the row character, common frequency, signed prime phases, and the rough
\(\mathfrak d=1\) term in (4.2). An estimate for a different Gauss coefficient,
or a proof that only small-prime branches have been treated, does not close it.

Liu's theorem and the recent repository projection theorems do not supply
that estimate. The route is a source-faithful proposed attack on cross-cutoff
dependence, with its first naive closure disproved by the length calculation.
