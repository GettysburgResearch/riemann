# Exact causal orbits and the cost of a dense zero-sharing family

**Status:** proposed proved classification and comparison-model theorems.
No new arithmetic fourth moment, generalized moment, zero-free boundary,
or RH theorem is claimed.

**Scope:** the literal Möbius/sextic family over
\(K=\mathbb Q(\sqrt{-3})\), with fixed finite-order Hecke data, every
nonzero element row, and every nonunit zero retained. The causal
classification concerns a fixed linear dilation operator with finite
weighted total variation. It includes continuous dilation measures and
accounts for the fact that radial smoothing cannot distinguish a Hecke
character from its field conjugate. The later finite group calculations
use an independent local Haar comparison model; they assert no
independence for growing prime sets on a finite physical row ball.

**What is proved.** For a fixed causal dilation measure with finite
weighted total variation at some \(0<\sigma\le1\), only two Kummer
classes can be connected to one fixed row, or four if complex
conjugation of the sum is also allowed. This is a total-variation
statement, not a general classification of bounded operator norms. The
classes contain only \(O(H^{1/6})\) physical rows of norm at most \(H\).
A different construction places the target reciprocal in every member
of a dense family: multiply the six power twists. An exact exterior-power
identity shows that this target reciprocal survives in the Haar mean.
For every fixed \(k\ge1\), the Haar \(2k\)-th moment has the desired
\(D^{k+\epsilon}\) bound if and only if the target has no zero to the
right of \(1/2\). More generally, this moment bound is unconditional
for every finite-group representation with no invariant vector. A
normalized independent-product argument proves all the sufficiency
statements; it does not replace the physical row measure by Haar measure.

**Smallest remaining gap:** an arithmetic estimate controlling signed
correlations between distinct Kummer classes, or a new estimate on the
invariant part of an enlarged family. The comparison-model
classification does not supply either arithmetic estimate.

## Sources and distinctions from preceding work

1. PR #929, final commit
   97bf40329489992e9384c34d7595af6d01a40774,
   [GAUSSIAN_SAMPLED_MOMENTS.md](../2026-10-10-conductor-averages/GAUSSIAN_SAMPLED_MOMENTS.md),
   SHA-256
   53625b2fc8da8162792bb40cbb329cd609ddf152d362f05fad32ac7b841d41d4,
   Sections 1 and 6: Gaussian detector, primitive character, finite Euler
   correction, and causal sixth-power replicas.
2. PR #913, commit 6498d6cc2eded03159c7332b25fd224ad07f89c1,
   [GENERAL_MOMENT_ATTACK.md](https://github.com/GettysburgResearch/riemann/blob/6498d6cc2eded03159c7332b25fd224ad07f89c1/standalone/2026-10-10-sextic-moment-descent/GENERAL_MOMENT_ATTACK.md),
   Section 6: positive-density extraction and the cardinality limitation
   for weights on sixth-power copies. This note extends that restriction
   to the stated class of fixed causal dilation measures; it does not
   rule out every possible amplification.
3. PR #927, commit f9939c957f5aac6b2099b591e4988991700a152b,
   [MIXED_CUBIC_REPLICATION.md](https://github.com/GettysburgResearch/riemann/blob/f9939c957f5aac6b2099b591e4988991700a152b/standalone/2026-10-10-sextic-signed-reunion/MIXED_CUBIC_REPLICATION.md):
   its integer copies are copies of physical cubic polynomial factors,
   not extra rows with the same fixed primitive reciprocal. Section 7
   explicitly retains the all-singleton obstruction.
4. PR #916, commit dd70e580a5ffdbe5b140784ba6cebd173cb84792,
   [DEFECT_BOOTSTRAP.md](https://github.com/GettysburgResearch/riemann/blob/dd70e580a5ffdbe5b140784ba6cebd173cb84792/standalone/2026-10-10-all-order-collision-removal/continuation-balanced-closure/DEFECT_BOOTSTRAP.md):
   a reusable fractional saving would bootstrap, but that saving is a
   separate arithmetic hypothesis. The finite-group determinant below is
   not a new claim to preceding collision, cycle, Witt, or necklace
   factorizations.
5. P. Stevenhagen, *Class Field Theory*, Oberwolfach seminar notes,
   November 7, 2002,
   [author-hosted PDF](https://websites.math.leidenuniv.nl/algebra/cft.pdf),
   Theorem 3.1 and Proposition 3.10: Kummer duality and the Artin
   interpretation of the power-residue symbol. Only unramified primes are
   used; the notes' excluded-prime convention is not substituted for the
   native zero extension.
6. J. S. Milne, *Class Field Theory*, version 4.03, August 6, 2020,
   [author-hosted PDF](https://www.jmilne.org/math/CourseNotes/CFT.pdf),
   V.3.23 and VIII.7.4: unconditional Chebotarev density, with the
   prime-count asymptotic in VIII.7.5. No conductor-uniform or effective
   Chebotarev estimate is required or claimed.
7. PR #913, commit 6498d6cc2eded03159c7332b25fd224ad07f89c1,
   [FOURTH_MOMENT_ATTACK.md](https://github.com/GettysburgResearch/riemann/blob/6498d6cc2eded03159c7332b25fd224ad07f89c1/standalone/2026-10-10-sextic-moment-descent/FOURTH_MOMENT_ATTACK.md),
   Section 8: the lattice-count and Borel--Carathéodory adapter
   from a zero-free half-plane to reciprocal growth. Section 7 below
   reproduces only its fixed-character polynomial-growth part.
   No new claim to that analytic adapter is made.
8. PR #911, commit 2f8b6a3898a722d0602a91dea73bac344a3bb7dd,
   [MOBIUS_CRT_TRANSLATION.md](https://github.com/GettysburgResearch/riemann/blob/2f8b6a3898a722d0602a91dea73bac344a3bb7dd/research/exploratory/2026-10-10-four-hour-wave/correlations/MOBIUS_CRT_TRANSLATION.md):
   the complete-residue sextic law, its exact Möbius translation
   retaining all nonunits, and the distinction from a short row ball.
   The rank-one example at the end of Section 7 is a classical
   Haar-orthogonality consequence, consistent with that prior identity;
   it is not presented as a new physical averaging theorem.

The proofs use these standard algebraic and density results, elementary
ideal counting, and finite-dimensional character orthogonality. They use
neither the imported quasi-Riemann theorem nor a native inverse second
moment.

## 1. The native radial family and its primitive reciprocal

Fix the finite excluded-prime set \(S\) and finite-order Hecke datum
\(\nu\) before any scale or row varies. In the native sextic
convention \(S\) includes the primes above \(6\). Put

\[
G(y)=\frac1{\sqrt{2\pi}}\exp\!\left(-\frac{(\log y)^2}{2}\right),
\qquad
A_r(D)=
\sum_{(\mathfrak n,S)=1}\mu_K(\mathfrak n)\nu(\mathfrak n)
 \left(\frac r{\mathfrak n}\right)_6 G(N\mathfrak n/D).
\tag{1.1}
\]

Rows \(r\) are nonzero elements of \(\mathcal O_K\). The symbol is zero
if the column meets \(r\), including when a row valuation is divisible
by six.

Let \(\eta_r\) be the completely multiplicative, zero-extended column
function in (1.1), and \(\psi_r\) its primitive inducing finite-order
Hecke character. With \(T_r\) the finite set of deleted primes,

\[
I_r(s):=\sum_{\mathfrak n}\mu_K(\mathfrak n)\eta_r(\mathfrak n)
                 (N\mathfrak n)^{-s}
=\frac{E_r(s)}{L_K(s,\psi_r)},\qquad \Re s>1,
\tag{1.2}
\]

\[
E_r(s)=\prod_{\mathfrak p\in T_r}
 \left(1-\psi_r(\mathfrak p)(N\mathfrak p)^{-s}\right)^{-1}.
\tag{1.3}
\]

A primitive ramified value is zero, so its factor in (1.3) is one.
Every factor and its reciprocal is holomorphic and nonzero in
\(\Re s>0\). This retains every row-dependent Euler deletion.

Elementary ideal counting and the Gaussian give, uniformly in the row,

\[
|A_r(D)|\ll_K D,\qquad
A_r(D)=O_{K,B}(D^B)\quad(0<D\le1)
\tag{1.4}
\]

for every \(B>0\), and

\[
\int_0^\infty A_r(D)D^{-s}\frac{dD}{D}
=e^{s^2/2}I_r(s),\qquad \Re s>1.
\tag{1.5}
\]

No weighted integrability at infinity below exponent one is assumed.

Write \(\psi^c(\mathfrak a)=\psi(\overline{\mathfrak a})\).
Changing the ideal variable to its conjugate gives

\[
L_K(s,\psi^c)=L_K(s,\psi).
\tag{1.6}
\]

Here \(c\) is conjugation of the field, not complex conjugation of the
character values.

## 2. A causal measure is forced to be the Euler-ratio measure

For a locally finite complex Radon measure \(\lambda\) on
\([1,\infty)\), define

\[
\|\lambda\|_{\sigma_0}
=\int_{[1,\infty)}t^{-\sigma_0}\,d|\lambda|(t),\qquad
(T_\lambda f)(D)=\int_{[1,\infty)}f(D/t)\,d\lambda(t).
\tag{2.1}
\]

The operator is fixed in \(D\) and causal. If its displayed variation
is finite for some \(\sigma_0>0\), the low-scale bound (1.4) makes
\(T_\lambda A_r(D)\) absolutely convergent for every \(D>0\).

### Lemma 2.1. Uniqueness of the dilation measure

Fix rows \(r,u\). Suppose \(\|\lambda\|_{\sigma_0}<\infty\) for some
\(\sigma_0>0\), and

\[
A_u(D)=T_\lambda A_r(D)\qquad(D>0).
\tag{2.2}
\]

Then

\[
\lambda=\sum_{m\ge1}c_m\delta_m,\qquad
\sum_{m\ge1}c_m m^{-s}
=\frac{E_u(s)}{E_r(s)}
  \frac{L_K(s,\psi_r)}{L_K(s,\psi_u)}
\quad\bigl(\Re s>\max(1,\sigma_0)\bigr).
\tag{2.3}
\]

The \(c_m\) are rational-integer Dirichlet coefficients, with all ideals
of a common norm grouped. They are not individual ideal coefficients.

**Proof.** For real \(s>\max(1,\sigma_0)\), the absolute Mellin
interchange is justified by

\[
\begin{aligned}
&\int_{[1,\infty)}\int_0^\infty
 |A_r(D/t)|D^{-s}\frac{dD}{D}\,d|\lambda|(t)\\
&\qquad=
\left(\int_0^\infty|A_r(x)|x^{-s}\frac{dx}{x}\right)
\int t^{-s}\,d|\lambda|(t)<\infty.
\end{aligned}
\tag{2.4}
\]

Equation (1.5), whose factors are nonzero in \(\Re s>1\), gives

\[
\int t^{-s}\,d\lambda(t)=I_u(s)/I_r(s).
\tag{2.5}
\]

The Euler ratio on the right has absolutely convergent Dirichlet
coefficients \(c_m\) for every real \(s>1\), after grouping by norm.
To exclude a continuous measure with this same transform, fix
\(s_1>\max(1,\sigma_0)\). Weight the difference between \(\lambda\)
and \(\sum c_m\delta_m\) by \(t^{-s_1}\), then push it forward under
\(t\mapsto1/t\) to a finite complex measure on \([0,1]\).
Equation (2.5) at \(s=s_1+n\), \(n=0,1,\ldots\), makes all of its
polynomial moments zero. Density of polynomials in the continuous
functions on \([0,1]\) makes that measure zero. Remove the positive
weight on each compact subset of \([1,\infty)\). This proves equality
of the locally finite measures in (2.3). No integrability of
\(A_r(D)D^{-\sigma_0}\) at infinity was assumed. \(\square\)

## 3. Classification in the critical analytic range

### Theorem 3.1. Maximal fixed causal orbit

For fixed nonzero rows \(r,u\), the following are equivalent:

1. Identity (2.2) holds for a measure with
   \(\|\lambda\|_{\sigma_0}<\infty\) for some \(0<\sigma_0\le1\).
2. The primitive characters satisfy
   \[
   \boxed{\psi_u=\psi_r\quad\hbox{or}\quad\psi_u=\psi_r^c.}
   \tag{3.1}
   \]
3. Identity (2.2) holds for a discrete finite-Euler correction measure
   with finite weighted variation for every \(\sigma_0>0\).

The physical masks remain in \(E_u/E_r\). The field-conjugate
alternative is essential because this is a theorem for radial sums.

**Proof of \(1\Rightarrow2\).** Lemma 2.1 forces the Euler-ratio
coefficients. At a rational prime \(p\) outside the finitely many
ramified or deleted primes, put

\[
a_r(p)=\sum_{N\mathfrak p=p}\psi_r(\mathfrak p).
\tag{3.2}
\]

It is zero at inert primes and the sum of the two ideal values at
split primes. The coefficient in (2.3) is

\[
c_p=a_r(p)-a_u(p).
\tag{3.3}
\]

Choose a finite Galois extension \(F/\mathbb Q\) containing \(K\)
through which both finite-order characters and their field conjugates
factor: take the compositum of their abelian class fields over \(K\)
and the conjugate fields. Write
\(\Gamma=\operatorname{Gal}(F/\mathbb Q)\),
\(\Delta=\operatorname{Gal}(F/K)\), so \([\Gamma:\Delta]=2\),
and let \(\theta_r,\theta_u\) be the corresponding one-dimensional
characters of \(\Delta\). Fix \(\tau\in\Gamma\setminus\Delta\).
The induced character is

\[
\Theta_r(g)=
\begin{cases}
\theta_r(g)+\theta_r(\tau g\tau^{-1}),&g\in\Delta,\\
0,&g\notin\Delta.
\end{cases}
\tag{3.4}
\]

At unramified rational primes it equals (3.2): the split case gives
the two conjugate prime ideals, and the inert case gives zero on
both sides. Thus the needed trace identity is explicit; no strong
multiplicity-one theorem is assumed.

If \(\Theta_r-\Theta_u\) were nonzero, it would be nonzero on a
conjugacy class of the finite group \(\Gamma\). Chebotarev gives
a positive-density set of rational primes on which \(|c_p|\) is
bounded below by a fixed positive constant. Consequently

\[
\sum_p|c_p|/p=\infty.
\tag{3.5}
\]

This contradicts
\(\sum_p|c_p|/p\le\sum_m|c_m|m^{-\sigma_0}<\infty\).
Hence \(\Theta_r=\Theta_u\). Restriction to \(\Delta\) gives

\[
\theta_r+\theta_r^\tau=\theta_u+\theta_u^\tau.
\tag{3.6}
\]

Orthogonality of the distinct one-dimensional finite-group
characters makes the two multisets equal, including repeated-member
cases. Thus \(\theta_u=\theta_r\) or \(\theta_u=\theta_r^\tau\),
which is (3.1).

**Proof of \(2\Rightarrow3\).** By (1.6) the primitive \(L\)-functions
are equal. The ratio in (2.3) is \(E_u/E_r\), a product of finitely
many factors \((1-\alpha p^{-fs})^{\pm1}\), with \(f=1\) or \(2\)
and \(|\alpha|\le1\). Geometric expansion gives finite weighted
coefficient norm at every \(\sigma_0>0\). The Euler identity proves
equality of grouped Dirichlet coefficients; absolute Gaussian
summation gives (2.2). Finally \(3\Rightarrow1\) is immediate.
\(\square\)

### Corollary 3.2. The boundary at exponent one is sharp

For every pair of fixed rows, the Euler-ratio coefficients define a
causal transfer with finite weighted variation at every
\(\sigma_0>1\). If (3.1) fails, their variation is infinite for every
\(0<\sigma_0\le1\).

**Proof.** The first assertion is absolute Euler convergence, and
the second is Theorem 3.1. \(\square\)

For a quantitative fixed-pair version, the prime-count form of
Chebotarev and (3.3) give, when (3.1) fails,

\[
\sum_{m\le X}|c_m|m^{-\sigma}
\gg_{r,u,\nu,\sigma}\frac{X^{1-\sigma}}{\log X}
\quad(0<\sigma<1),\qquad
\sum_{m\le X}|c_m|/m\gg_{r,u,\nu}\log\log X
\tag{3.7}
\]

for sufficiently large \(X\). Restrict to the positive-density
prime set in \([X/2,X]\) for the first bound and use partial
summation for the second. Neither constants nor thresholds are
claimed uniform for moving rows or conductors.

## 4. Two Kummer classes, or four with conjugation

### Lemma 4.1. Ideal-character equality detects sixth powers

For nonzero \(u,r\in K\), the two residue characters agree outside
a finite prime set if and only if

\[
u/r\in K^{\times6}.
\tag{4.1}
\]

**Proof.** Multiplicativity gives one direction. Conversely put
\(\alpha=u/r\). The Kummer-Artin identity says that
\((\alpha/\mathfrak p)_6=1\) outside a finite set precisely makes
those Frobenius elements act trivially on \(\alpha^{1/6}\).
If \(K(\alpha^{1/6})/K\) were nontrivial, Chebotarev would give
primes with nontrivial action. Hence \(\alpha^{1/6}\in K\).
\(\square\)

With \(\nu,r\) fixed, \(\psi_u=\psi_r\) specifies one Kummer class.
If \(\psi_u=\psi_r^c\) has any solution, all its solutions form one
further Kummer class: dividing two solutions cancels \(\nu\), and
Lemma 4.1 applies. This second class can be absent or coincide with
the first.

For a class containing an integral row, choose its unique
sixth-power-free integral representative \(r_0\), retaining its
unit. Every prime valuation is between zero and five. Class
number one makes the ideal sixth root principal. Every integral
row in the class is

\[
u=r_0v^6,\qquad v\in\mathcal O_K,
\tag{4.2}
\]

with no condition \((r_0,v)=1\). A negative valuation of \(v\)
would make that of \(u\) negative. Sixth powers are independent
of the unit representative of \((v)\), and distinct ideals give
distinct rows in (4.2). Thus their count for \(0<Nu\le H\) is

\[
J_K((H/Nr_0)^{1/6})
=\kappa_K(H/Nr_0)^{1/6}
 +O_K((H/Nr_0)^{1/12}+1),
\tag{4.3}
\]

when the argument is at least one, and zero otherwise. The ideal
count is elementary lattice counting divided by the six units.

### Corollary 4.2. Cardinality of the maximal causal orbit

For fixed \(\nu,r\), rows reachable under Theorem 3.1 lie in at
most two Kummer classes and number \(O_{\nu,r}(H^{1/6})\) in the
physical ball. If identities
\(A_u=T_\lambda\overline{A_r}\) are also allowed, the only additional
primitive character targets are \(\overline{\psi_r}\) and
\((\overline{\psi_r})^c\). There are then at most four Kummer
classes, still numbering \(O_{\nu,r}(H^{1/6})\).

**Proof.** The first assertion follows from Theorem 3.1 and
(4.1)--(4.3). The Gaussian is real, so conjugating \(A_r\) replaces
its primitive reciprocal by \(L_K(s,\overline{\psi_r})^{-1}\)
with the conjugated finite Euler correction. Repeat the same
argument. Each additional character target either has no row in
the fixed-\(\nu\) family or one Kummer class. \(\square\)

For example, when \(\nu=1\), the linear field-conjugate partner of
the class of \(r\) is the class of \(\overline r^{-1}\), represented
integrally by \(\overline r^5\), since

\[
\left(\frac r{\overline{\mathfrak n}}\right)_6
=\overline{\left(\frac{\overline r}{\mathfrak n}\right)_6}.
\tag{4.4}
\]

This is different from ordinary complex conjugation of the sum.

### What the count does and does not forbid

For \(N\) copies and weights of total sum one, Hölder gives
\(\|\lambda\|_{p/(p-1)}\ge N^{-1/p}\), using the maximum norm at
\(p=1\). Therefore direct weighted extraction using only the
moment budget \(M_{2k}(D,H)\ll HD^{k+\epsilon}\) and the number
of these causal copies cannot improve the cardinality factor

\[
D^{1/2+\epsilon}H^{5/(12k)}.
\tag{4.5}
\]

Positive-density sixth-power bases already attain its count
exponent. Replacing their Euler operations by arbitrary fixed
absolutely summable causal dilations does not enlarge the power
of \(H\).

This does not exclude signed averages of different primitive
characters, nonstationary scale-dependent operators, operators
controlled by cancellation instead of total variation, nonlinear
identities, or new relations between zeros of different
\(L\)-functions. Those require additional arithmetic information.
Equation (4.5) is not a lower bound for actual Möbius sums.

## 5. A genuinely dense family sharing the target poles

There is an alternative to enlarging the old causal orbit. Fix a
primitive finite-order target \(\nu_0\), include its conductor in
\(S\), and for each nonzero physical row \(u\) put

\[
\mathcal D_u(s)=
\prod_{\substack{\mathfrak p\notin S\\\mathfrak p\nmid u}}
\prod_{j=0}^{5}
\left(1-\nu_0(\mathfrak p)
 \left(\frac u{\mathfrak p}\right)_6^j
 (N\mathfrak p)^{-s}\right),\qquad \Re s>1.
\tag{5.1}
\]

At a prime dividing \(u\), every factor is deleted, including
\(j=0\). That power means the principal zero extension, not an
unmasked constant character.

Each of the six factors in (5.1) is the primitive reciprocal
induced by
\(\nu_0(\mathfrak n)(u/\mathfrak n)_6^j\), with its finite
Euler correction. In particular the \(j=0\) factor is

\[
\prod_{\substack{\mathfrak p\notin S\\\mathfrak p\nmid u}}
 (1-\nu_0(\mathfrak p)(N\mathfrak p)^{-s})
=\frac{E_{u,0}(s)}{L_K(s,\nu_0)}.
\tag{5.2}
\]

Thus every member contains the target reciprocal. A nontrivial
target zero \(\rho\), \(0<\Re\rho<1\), is a pole of every
\(\mathcal D_u\). The other five factors cannot cancel it:
finite-order Hecke \(L\)-functions have no poles in this open
strip, and finite Euler corrections are nonzero there. Their
reciprocals can only add poles or take finite nonzero values.
The possible principal pole at \(s=1\) lies outside this argument.

For exact-order-six characters, this is the inverse
regular-representation Artin product, up to the displayed target
twist and deletions. For smaller orders some factors repeat.
The identity uses no exact-order restriction. It really does
share the target pole among all physical rows, beyond the
sparse causal orbit of Section 4.

The next calculation locates what becomes harder after changing
the family this way.

## 6. Exterior powers identify the invariant part of the Haar mean

Let \(\mathcal G\) be a finite group and
\(\rho:\mathcal G\to\operatorname{GL}(V)\) a fixed complex
representation of dimension \(d\ge1\). Average an inner product
so that \(\rho\) is unitary. Define

\[
m_0=\dim V^{\mathcal G},\qquad
P_\rho(x)=\frac1{|\mathcal G|}
 \sum_{g\in\mathcal G}\det(I-x\rho(g)).
\tag{6.1}
\]

### Lemma 6.1. The determinant average

\[
\boxed{
P_\rho(x)=
\sum_{j=0}^{d}(-x)^j
 \dim\bigl((\mathop{\bigwedge}\nolimits^j V)^{\mathcal G}\bigr)
=(1-x)^{m_0}Q_\rho(x),
}
\tag{6.2}
\]

where \(Q_\rho\) is a polynomial satisfying

\[
Q_\rho(0)=1,\qquad Q_\rho'(0)=0.
\tag{6.3}
\]

**Proof.** The coefficient of \((-x)^j\) in the determinant is
the trace of \(\bigwedge^j\rho(g)\). The average of these
representation matrices is the projection onto invariant
vectors; its trace is their dimension. This proves the first
equality. Split
\(V=V^{\mathcal G}\oplus V_1\) into invariant subspaces.
The first summand contributes \((1-x)^{m_0}\) to every
determinant. The second has no invariant vector, so the
linear coefficient of its averaged determinant is zero.
This proves the factorization and (6.3). \(\square\)

### A local model retaining every nonunit mask

At every good prime ideal \(\mathfrak p\), independently of all
other primes, put \(q=N\mathfrak p\), and choose:

- a deletion with probability \(1/q\), whose local determinant
  is one;
- otherwise a uniform \(g_{\mathfrak p}\in\mathcal G\), whose
  local determinant is
  \(\det(I-\nu_0(\mathfrak p)q^{-s}\rho(g_{\mathfrak p}))\).

Call this product probability space \(\Omega\). For
\(\mathcal G=C_6\) in its regular representation, the
one-prime law is exactly the sextic-symbol law of an
additive Haar row in \(\mathcal O_{K,\mathfrak p}\):
nonunits have measure \(1/q\), and the six symbols are
equally likely among the units. This is a comparison
measure. It has not been substituted for a finite physical
row ball, and no uniform equidistribution over a growing
prime set is asserted.

The mean local polynomial is

\[
\Phi_{\rho,q}(x)
=\frac1q+\left(1-\frac1q\right)P_\rho(x).
\tag{6.4}
\]

Its normalized factor is, by (6.2),

\[
\begin{aligned}
R_{\rho,q}(x)
&=\frac{\Phi_{\rho,q}(x)}{(1-x)^{m_0}}\\
&=\left(1-\frac1q\right)Q_\rho(x)
 +\frac1q(1-x)^{-m_0}\\
&=1+O_\rho(q^{-1}|x|+|x|^2),\qquad |x|\le1/2.
\end{aligned}
\tag{6.5}
\]

This is the exact mask correction. Treating \(j=0\) as
unmasked would give a different local mean.

Let \(\mathcal D_\omega(s)\) be the product of these local
determinants. It and its expectation converge absolutely in
\(\Re s>1\), locally uniformly, because the nonconstant
local absolute coefficient mass is \(O_\rho(q^{-\Re s})\).

### Theorem 6.2. Mean of an inverse-determinant family

Enlarge \(S\) by a fixed finite set of small primes depending
on \(\rho\). There is a function
\(\mathcal H_{\rho,S,\nu_0}\), holomorphic and nonzero in
\(\Re s>1/2\), such that

\[
\boxed{
\mathbb E_\Omega\mathcal D_\omega(s)
=
\frac{\mathcal H_{\rho,S,\nu_0}(s)}
 {L_K(s,\nu_0)^{m_0}},\qquad \Re s>1.
}
\tag{6.6}
\]

The right side meromorphically continues the mean. When
\(m_0>0\), its holomorphy throughout \(\Re s>1/2\) is
neither assumed nor concluded.

**Proof.** Absolute convergence permits expectation prime by
prime. Equations (6.4)--(6.5) give

\[
\mathbb E\mathcal D_\omega(s)
=
\prod_{\mathfrak p\notin S}
 (1-\nu_0(\mathfrak p)q^{-s})^{m_0}
\prod_{\mathfrak p\notin S}
 R_{\rho,q}(\nu_0(\mathfrak p)q^{-s}).
\tag{6.7}
\]

For \(\Re s\ge1/2+\delta\), the sum of absolute errors
in the second product is at most

\[
C_\rho\sum_{\mathfrak p\notin S}
 (q^{-3/2-\delta}+q^{-1-2\delta})<\infty.
\tag{6.8}
\]

Choose the finite small-prime deletion so that every remaining
\(q\) satisfies
\(|R_{\rho,q}(x)-1|<1/2\) whenever \(|x|\le q^{-1/2}\).
Equation (6.5) makes this possible. Thus every local factor
is nonzero for \(\Re s>1/2\), and the normally convergent
product is holomorphic and nonzero there.

The first product in (6.7) is

\[
L_K(s,\nu_0)^{-m_0}
\prod_{\mathfrak p\in S}
 (1-\nu_0(\mathfrak p)q^{-s})^{-m_0}.
\tag{6.9}
\]

The finite correction is nonzero in \(\Re s>0\);
primitive ramified values are zero and contribute one.
Absorb it into the product from (6.8). This proves
(6.6), without a zero-free premise. \(\square\)

### The explicit sextic example

For the regular representation of \(C_m\), an element
of order \(a\mid m\) has determinant polynomial
\((1-x^a)^{m/a}\); there are \(\varphi(a)\) such elements.
Therefore

\[
P_{\mathrm{reg},C_m}(x)
=\frac1m\sum_{a\mid m}\varphi(a)(1-x^a)^{m/a}.
\tag{6.10}
\]

For \(m=6\), the exact calculation is

\[
\begin{aligned}
P_{\mathrm{reg},C_6}(x)
&=\frac{(1-x)^6+(1-x^2)^3
             +2(1-x^3)^2+2(1-x^6)}6\\
&=1-x+2x^2-4x^3+3x^4-x^5\\
&=(1-x)(1+2x^2-2x^3+x^4).
\end{aligned}
\tag{6.11}
\]

The exterior invariant dimensions in degrees zero through
six are \(1,1,2,4,3,1,0\). Including the nonunit event,

\[
\Phi_{\mathrm{reg},q}(x)
=\frac1q+\left(1-\frac1q\right)
 (1-x+2x^2-4x^3+3x^4-x^5).
\tag{6.12}
\]

The all-row local model uses (6.12), not just (6.11).
After division by \(1-x\), its extra first-order term is
\(q^{-1}x\), summable over primes for \(\Re s>0\).
The remaining quadratic errors are summable for
\(\Re s>1/2\). The dense lift therefore retains one
complete target reciprocal in its Haar mean.

## 7. An exact classification of every fixed Haar moment

Expand the determinant products as ideal Dirichlet series:

\[
\mathcal D_\omega(s)
=\sum_{\mathfrak n}b_\omega(\mathfrak n)(N\mathfrak n)^{-s},
\qquad
\mathcal B_\omega(D;G)
=\sum_{\mathfrak n}b_\omega(\mathfrak n)G(N\mathfrak n/D).
\tag{7.1}
\]

Their local coefficients satisfy

\[
|b_\omega(\mathfrak p^j)|\le{d\choose j}\quad(0\le j\le d),
\qquad b_\omega(\mathfrak p^j)=0\quad(j>d).
\tag{7.2}
\]

In particular
\(|b_\omega(\mathfrak n)|\le d_{d,K}(\mathfrak n)\)
uniformly in \(\omega\), where \(d_{d,K}\) is the
coefficient of \(\zeta_K(s)^d\).
This gives absolute Gaussian convergence and a uniform
polynomial bound at large \(D\). It also gives
\(\mathcal B_\omega(D;G)=O_{B,d}(D^B)\) for every
\(B>0\) when \(0<D\le1\): choose
\(B'>\max(B,1)\), bound \(G(y)\ll_{B'}y^{-B'}\),
and sum the convergent \(d_{d,K}\)-series at \(B'\).

Expectation and Mellin integration can therefore be
interchanged in \(\Re s>1\). With
\(\mathcal M(D)=\mathbb E_\Omega\mathcal B_\omega(D;G)\),
Theorem 6.2 gives

\[
\int_0^\infty\mathcal M(D)D^{-s}\frac{dD}{D}
=e^{s^2/2}
 \frac{\mathcal H_{\rho,S,\nu_0}(s)}
 {L_K(s,\nu_0)^{m_0}},\qquad \Re s>1.
\tag{7.3}
\]

### Theorem 7.1. Dense-family Haar second moment implies zero exclusion

Assume \(m_0\ge1\), choose \(S\) as in Theorem 6.2, and
suppose the following new estimate holds for every
\(\epsilon>0\):

\[
\boxed{
\mathbb E_\Omega|\mathcal B_\omega(D;G)|^2
\ll_{\rho,S,\nu_0,\epsilon}D^{1+\epsilon}
\qquad(D\ge2).
}
\tag{7.4}
\]

Then

\[
L_K(s,\nu_0)\ne0\qquad(\Re s>1/2).
\tag{7.5}
\]

Estimate (7.4) is not established unconditionally when
\(m_0\ge1\). The converse proved below identifies its
exact difficulty. It is not deduced from native second
moments, character sieves, or Haar orthogonality.

**Proof.** Jensen gives, after renaming the arbitrarily
small loss,

\[
|\mathcal M(D)|
\le(\mathbb E|\mathcal B_\omega(D;G)|^2)^{1/2}
\ll_\epsilon D^{1/2+\epsilon}.
\tag{7.6}
\]

Together with the uniform low-scale bound after (7.2),
this makes the Mellin integral in (7.3) holomorphic for
\(\Re s>1/2\). On each compact subset choose epsilon
smaller than its distance from the boundary to obtain
absolute domination. The right side meromorphically
continues there by Theorem 6.2. Its Gaussian and
\(\mathcal H\) factors are nonzero. Because \(m_0\ge1\),
a target zero would give a pole, contradicting the
identity theorem and the holomorphic integral. A
principal pole at \(s=1\) creates a zero of the
reciprocal, so it causes no exception. \(\square\)

The converse rests on a positive statement about the
noninvariant fluctuations. In fact it works in every
fixed \(L^{2k}(\Omega)\).

### Theorem 7.2. All normalized Haar moments converge above one half

Make one further fixed finite enlargement of \(S\), if needed,
depending only on \(\rho\). Write the random local factor and
its deterministic mean as

\[
f_{\mathfrak p,\omega}(s)=
\begin{cases}
1,&\text{at the deletion event},\\
\det(I-\nu_0(\mathfrak p)q^{-s}\rho(g_{\mathfrak p})),
   &\text{otherwise},
\end{cases}
\qquad
\mu_{\mathfrak p}(s)=\mathbb E f_{\mathfrak p,\omega}(s).
\tag{7.7}
\]

Then each local mean \(\mu_{\mathfrak p}\) is nonzero
throughout \(\Re s\ge1/2\).
For every fixed integer \(k\ge1\), the products

\[
Z_{\mathfrak p,\omega}(s)
=\frac{f_{\mathfrak p,\omega}(s)}{\mu_{\mathfrak p}(s)},
\qquad
X_{\mathcal P}(s)
=\prod_{\mathfrak p\in\mathcal P}Z_{\mathfrak p,\omega}(s),
\tag{7.8}
\]

over finite sets of good primes converge in
\(L^{2k}(\Omega)\), uniformly on every closed half-plane
\(\Re s\ge\alpha>1/2\), to a holomorphic
\(L^{2k}(\Omega)\)-valued function \(X(s)\). The limits
for different \(k\) agree under the usual inclusions of
these spaces. Moreover

\[
\mathbb E X(s)=1,\qquad
\sup_{\Re s\ge\alpha}\|X(s)\|_{2k}
\ll_{\rho,k,\alpha}1.
\tag{7.9}
\]

**Proof.** Unitarity and the determinant coefficient bounds give,
uniformly in the local event and in the argument of \(q^{-s}\),

\[
|f_{\mathfrak p,\omega}(s)-1|
+|\mu_{\mathfrak p}(s)-1|
\ll_\rho q^{-\Re s}.
\tag{7.10}
\]

Choose the fixed small-prime deletion so that each mean differs
from one by less than \(1/2\) for \(\Re s\ge1/2\).
Put \(W_{\mathfrak p}=Z_{\mathfrak p}-1\). Then

\[
\mathbb E W_{\mathfrak p}=0,\qquad
|W_{\mathfrak p}(s)|\ll_\rho q^{-\Re s}.
\tag{7.11}
\]

For nonnegative integers \(j,\ell\le k\), expand the finite
polynomial
\((1+W_{\mathfrak p})^j(1+\overline W_{\mathfrak p})^\ell\).
The linear terms have expectation zero. Every remaining
nonconstant term has total degree at least two. Therefore

\[
\mathbb E
 \bigl[Z_{\mathfrak p}(s)^j
       \overline{Z_{\mathfrak p}(s)}^\ell\bigr]
=1+O_{\rho,k}(q^{-2\Re s}).
\tag{7.12}
\]

In particular independence gives

\[
\mathbb E|X_{\mathcal P}(s)|^{2k}
\le\prod_{\mathfrak p\in\mathcal P}
 (1+C_{\rho,k}q^{-2\alpha})
\ll_{\rho,k,\alpha}1
\qquad(\Re s\ge\alpha),
\tag{7.13}
\]

since the prime-ideal sum at exponent \(2\alpha>1\) converges.
For nested finite sets \(\mathcal P\subseteq\mathcal Q\), let
\(Y_{\mathcal P,\mathcal Q}
=\prod_{\mathfrak p\in\mathcal Q\setminus\mathcal P}Z_{\mathfrak p}\).
Each mixed moment of \(Y_{\mathcal P,\mathcal Q}\), with exponents
\(j,\ell\le k\), differs from one by at most
\[
C_{\rho,k,\alpha}
\sum_{\mathfrak p\in\mathcal Q\setminus\mathcal P}q^{-2\alpha}.
\]
Indeed use (7.12), independence, and
\(\left|\prod(1+e_{\mathfrak p})-1\right|
\le\exp(\sum|e_{\mathfrak p}|)-1\).
Expand
\((Y_{\mathcal P,\mathcal Q}-1)^k
 (\overline Y_{\mathcal P,\mathcal Q}-1)^k\).
The constant contributions of all its mixed moments cancel:
their signed binomial sum is \((1-1)^{2k}=0\).
Consequently

\[
\begin{aligned}
\|X_{\mathcal Q}(s)-X_{\mathcal P}(s)\|_{2k}^{2k}
&=\mathbb E|X_{\mathcal P}(s)|^{2k}
  \mathbb E|Y_{\mathcal P,\mathcal Q}(s)-1|^{2k}\\
&\ll_{\rho,k,\alpha}
 \sum_{\mathfrak p\in\mathcal Q\setminus\mathcal P}q^{-2\alpha},
\qquad \Re s\ge\alpha.
\end{aligned}
\tag{7.14}
\]

This is uniform Cauchy convergence along any exhaustion of
the prime ideals; comparison through unions makes its limit
independent of that exhaustion. Each finite product is
holomorphic with values in \(L^{2k}(\Omega)\), since its
finitely many local possibilities are holomorphic and its
deterministic denominators are nonzero. Locally uniform
convergence in this Banach space preserves holomorphy,
as follows directly by passing to the limit in the Cauchy
integral formula. Equations (7.9) follow from (7.13) and
continuity of expectation. Uniqueness in \(L^2\) identifies
the limits for all \(k\). No almost-sure convergence
theorem is required. \(\square\)

At \(k=1\), (7.14) also has the exact second-moment form
\[
\mathbb E|X_{\mathcal Q}-X_{\mathcal P}|^2
=
\left(\prod_{\mathfrak p\in\mathcal P}
          \mathbb E|Z_{\mathfrak p}|^2\right)
\left(\prod_{\mathfrak p\in\mathcal Q\setminus\mathcal P}
          \mathbb E|Z_{\mathfrak p}|^2-1\right).
\]
This displays explicitly the summable variance that
controls the normalized fluctuations.

### Lemma 7.3. Fixed-character reciprocal growth under zero exclusion

Let \(\nu_0\) be a fixed primitive finite-order Hecke character
over \(K\). If \(L_K(s,\nu_0)\) has no zero in \(\Re s>1/2\),
then for every \(\alpha>1/2\) there are constants
\(A,C\), depending on \(\nu_0,\alpha\), such that

\[
|L_K(s,\nu_0)^{-1}|
\le C(2+|\Im s|)^A
\qquad(\Re s\ge\alpha).
\tag{7.15}
\]

At a principal pole the reciprocal is its analytic
continuation, with value zero. The constants are for
this fixed character; no moving-conductor assertion is used.

**Proof.** Here is the fixed-character part of the existing
adapter in PR #913, Section 8. Because \(K\) has class number
one, a nonprincipal finite-order character becomes a
unit-invariant residue character on the Eisenstein lattice
modulo its fixed conductor, with zero sum on a complete
residue cell and zero values at nonunits. Complete cells
inside the norm disk cancel. The number of boundary cells
is \(O_{\nu_0}(\sqrt x)\), and each contains a fixed bounded
number of lattice points. Dividing by the six generators
of each ideal gives
\[
\sum_{N\mathfrak a\le x}\nu_0(\mathfrak a)
=O_{\nu_0}(\sqrt x)\qquad(x\ge1).
\]
For the primitive principal character the ideal count is
\(\kappa_K x+O_K(\sqrt x)\).

Partial summation thus continues a nonprincipal \(L\) to
\(\Re s>1/2\) by
\[
L_K(s,\nu_0)
=s\int_1^\infty
 \left(\sum_{N\mathfrak a\le x}\nu_0(\mathfrak a)\right)
 x^{-s-1}\,dx.
\]
For the principal character the same formula, after
subtracting \(\kappa_K x\), leaves the explicit term
\(\kappa_K s/(s-1)\). Define
\[
\widetilde L(s)=
\begin{cases}
L_K(s,\nu_0),&\nu_0\text{ nonprincipal},\\
\dfrac{s-1}{s+1}\zeta_K(s),&\nu_0\text{ principal}.
\end{cases}
\]
It is holomorphic and nonzero in \(\Re s>1/2\) under the
lemma's hypothesis, including at \(s=1\).
The preceding integrals give, for each
\(\beta>1/2\),
\[
|\widetilde L(\sigma+it)|
\ll_{\nu_0,\beta}2+|t|
\qquad(\beta\le\sigma\le4).
\tag{7.16}
\]
The principal pole has been removed before using this bound.

Choose the analytic logarithm \(g=\log\widetilde L\) on the
simply connected half-plane \(\Re s>1/2\), agreeing with
the Euler logarithm on \(\Re s>1\), together with the
displayed rational factor in the principal case. Absolute
Euler convergence at \(2+it\) shows
\(|g(2+it)|\ll_{\nu_0}1\); the rational factor's
logarithm is uniformly bounded there as well.

It suffices to take \(1/2<\alpha<2\). Put
\(\beta=(\alpha+1/2)/2\), and apply
Borel--Carathéodory on the disk centered at \(2+it\),
with outer radius \(R=2-\beta\) and inner radius
\(r=2-\alpha<R\). The outer disk lies in the region
of (7.16), where
\(\Re g=\log|\widetilde L|
\ll_{\nu_0,\alpha}\log(2+|t|)\).
The center value is bounded. The inequality therefore gives
\[
|g(\sigma+it)|
\ll_{\nu_0,\alpha}\log(2+|t|)
\qquad(\alpha\le\sigma\le2).
\]
Exponentiating \(-\Re g\) proves a polynomial bound for
\(\widetilde L^{-1}\) on this strip. In the principal
case multiply it by \((s-1)/(s+1)\), whose modulus is
at most one in the right half-plane, to recover \(L^{-1}\).
For \(\Re s\ge2\), absolute Euler convergence already
bounds \(L^{-1}\) uniformly. This proves (7.15).
\(\square\)

### Theorem 7.4. Every fixed even Haar moment: equivalence and an unconditional case

Fix \(\mathcal G,\rho,\nu_0\), and \(S\) as in
Theorems 6.2 and 7.2. For an integer \(k\ge1\), write
\(\mathrm{HM}_{2k}\) for the assertion that, for every
\(\epsilon>0\),

\[
\boxed{
\mathbb E_\Omega|\mathcal B_\omega(D;G)|^{2k}
\ll_{\rho,S,\nu_0,k,\epsilon}D^{k+\epsilon}
\qquad(D\ge2).
}
\tag{7.17}
\]

If \(m_0=0\), then \(\mathrm{HM}_{2k}\) holds
unconditionally for every fixed \(k\ge1\).
If \(m_0\ge1\), then, for each fixed \(k\ge1\),
\[
\boxed{
\mathrm{HM}_{2k}
\quad\Longleftrightarrow\quad
L_K(s,\nu_0)\ne0\ \text{for all }\Re s>1/2.
}
\tag{7.18}
\]
Thus any one of these fixed even moments implies all the others
in the comparison model. This is not a statement about the
finite physical row measure.

**Proof of sufficiency.** The normal product in Theorem 6.2
and its finite Euler correction are bounded uniformly in
\(t\) on each closed half-plane
\(\Re s\ge\alpha>1/2\). This follows from (6.8);
the same finite small-prime deletion bounds each reciprocal
local factor as well. Define

\[
F(s)=
\frac{\mathcal H_{\rho,S,\nu_0}(s)}
     {L_K(s,\nu_0)^{m_0}}\;X(s).
\tag{7.19}
\]

When \(m_0=0\), this is a holomorphic
\(L^{2k}(\Omega)\)-valued function in \(\Re s>1/2\)
without any zero-free hypothesis. When \(m_0\ge1\),
the zero-exclusion hypothesis and Lemma 7.3 give the same
holomorphy, including at a principal pole. In either case,
for every closed vertical strip
\(\alpha\le\Re s\le c\), with \(1/2<\alpha<c<\infty\),
\[
\|F(s)\|_{2k}\ll_{\rho,S,\nu_0,k,\alpha,c}
(2+|\Im s|)^A
\tag{7.20}
\]
for a fixed exponent \(A\); in the invariant-free case
one may take \(A=0\).

For \(\Re s>1\), the raw determinant products converge
absolutely uniformly in \(\omega\). Their finite mean
products converge to the deterministic factor in (7.19),
and the normalized products converge by Theorem 7.2.
Hence \(F(s)=\mathcal D_\omega(s)\) as elements of
\(L^{2k}(\Omega)\) in this original half-plane.
Equation (7.19) is its analytic continuation. In particular,
for \(m_0>0\) no convergence of the unnormalized finite
Euler products below their absolute-convergence region
is inferred from (7.19).

For any \(c>1\), (7.2) and absolute Gaussian Mellin
inversion give the following convergent Bochner integral
in \(L^{2k}(\Omega)\):
\[
\mathcal B_\omega(D;G)
=\frac1{2\pi}
\int_{\mathbb R}
 e^{(c+it)^2/2}D^{c+it}F(c+it)\,dt.
\tag{7.21}
\]
Indeed the Dirichlet coefficient absolute majorant at \(c\)
is \(\zeta_K(c)^d\), and the Gaussian transform decays as
\(e^{-t^2/2}\); this justifies termwise inversion and
identifies the integral with the original sum (7.1).

Choose any \(1/2<\alpha<c\). Apply the Banach-valued
Cauchy theorem on the rectangle with real edges
\(\alpha,c\) and imaginary edges \(\pm T\) to
\(e^{s^2/2}D^sF(s)\). Equivalently apply the scalar
theorem after every bounded linear functional on
\(L^{2k}(\Omega)\), using the norm bounds for passage
to the Bochner integrals. For each fixed \(D>0\),
(7.20) bounds the horizontal integrals by
\[
C_{\rho,S,\nu_0,k,\alpha,c,D}
(2+T)^A e^{-T^2/2},
\]
which tends to zero. Both vertical integrals converge
absolutely in norm. Letting \(T\) tend to infinity
therefore shifts (7.21) to \(\Re s=\alpha\), and gives
\[
\begin{aligned}
\|\mathcal B_\omega(D;G)\|_{2k}
&\le\frac{D^\alpha e^{\alpha^2/2}}{2\pi}
 \int_{\mathbb R}e^{-t^2/2}\|F(\alpha+it)\|_{2k}\,dt\\
&\ll_{\rho,S,\nu_0,k,\alpha}D^\alpha .
\end{aligned}
\tag{7.22}
\]
Taking \(\alpha=1/2+\epsilon/(2k)\), and then choosing
\(c>\max(1,\alpha)\), proves (7.17).
There has been no contour passage through a target pole:
holomorphy in the strip used for the shift was proved
under precisely the hypothesis stated above.

**Proof of necessity when \(m_0\ge1\).** If (7.17)
holds for a fixed \(k\), Hölder gives
\[
\mathbb E|\mathcal B_\omega(D;G)|^2
\le
\left(\mathbb E|\mathcal B_\omega(D;G)|^{2k}\right)^{1/k}
\ll D^{1+\epsilon/k}.
\]
Renaming the arbitrary loss gives (7.4), so Theorem 7.1
excludes all target zeros in \(\Re s>1/2\).
\(\square\)

### Three concrete sextic comparisons

For the regular sextic representation \(m_0=1\).
One can replace sparse-copy geometry by a dense family
sharing the target poles, but every one of its desired
fixed Haar moments is exactly as difficult as the
target's zero exclusion. For the principal target over
\(K\), that exclusion implies RH for
\(\zeta_{\mathbb Q}\), because
\(\zeta_K(s)=\zeta_{\mathbb Q}(s)L(s,\chi_{-3})\)
and the usual functional equation reflects the
zero-free right half of the critical strip.
No estimate (7.17) for this regular family has been
proved unconditionally.

Remove the trivial representation instead and use the
five-dimensional representation
\(\rho^\circ=\operatorname{reg}(C_6)\ominus\mathbf1\).
Its local unit determinant is
\[
\prod_{j=1}^{5}(1-\nu_0(\mathfrak p)g_{\mathfrak p}^j q^{-s}),
\]
with the same deletion event at a nonunit. Now \(m_0=0\),
and (6.11) gives
\[
P_{\rho^\circ}(x)=1+2x^2-2x^3+x^4.
\tag{7.23}
\]
Theorem 7.4 proves all its fixed Haar bounds
\(\mathbb E|\mathcal B_\omega^\circ(D;G)|^{2k}
\ll D^{k+\epsilon}\) unconditionally.
In this case the finite mean products themselves
converge normally for \(\Re s>1/2\), because their
local linear terms vanish, so the unnormalized random
products also converge in every fixed \(L^{2k}\) there.
This positive result isolates the invariant constituent
as the complete target-zero obstruction in this
comparison model. Removing it also removes the
explicit common target factor from the dense
construction (5.1); no physical-row transfer follows.

Finally, the original one-dimensional sextic representation
\(\rho_1(g)=g\) already has \(m_0=0\) and
\(P_{\rho_1}(x)=1\). Its local masked mean is exactly one.
Here the coefficients in (7.1) are precisely
\(\mu_K(\mathfrak n)\nu_0(\mathfrak n)
 \chi_\omega(\mathfrak n)\), where the completely
multiplicative random character has prime value zero with
probability \(1/q\) and each sextic unit value with
probability \((1-1/q)/6\), independently at different primes.
Theorem 7.4 recovers all fixed even Haar moments for
this original comparison family unconditionally.
At order two the stronger exact diagonal calculation is
\[
\mathbb E_\Omega|\mathcal B_{\rho_1,\omega}(D;G)|^2
=
\sum_{\substack{\mathfrak n\ {\rm squarefree}\\
                (\mathfrak n,S)=1}}
 \left(\prod_{\mathfrak p\mid\mathfrak n}
                 (1-(N\mathfrak p)^{-1})\right)
 G(N\mathfrak n/D)^2
\ll_K D .
\tag{7.24}
\]
For distinct squarefree ideals there is a prime occurring
on only one side, whose mean character value is zero.
Identical ideals contribute the displayed nonunit
probabilities. Absolute Gaussian convergence justifies
expanding the expectation, and elementary ideal counting
proves the last bound.

This rank-one orthogonality is classical; the exact finite
complete-residue law and its signed translation already
appear in PR #911. The two arithmetic obligations can now
be stated separately. The original Haar comparison has
the desired moments, but its transfer to the physical short
row measure is unproved. The dense regular-representation
family shares the target poles, but its Haar mean itself
contains the target zero problem.

## 8. Consequences for the next arithmetic attack

The sixth-power count is not an artifact of prime
bases. In the class of fixed causal operations with
finite weighted variation in the critical range,
the native radial orbit keeps the same \(H^{1/6}\)
power after all its conjugate partners are included.

A representation-theoretic enlargement can create
many more members sharing a target pole. The
exterior-power identity finds the target in the
trivial constituent. Its independent local mean
retains the target reciprocal, up to an analytic
nonzero correction to the right of \(1/2\).
After division by that mean, the independent
fluctuations have all fixed even moments bounded
on every closed half-plane to the right of \(1/2\).
The exact classification in Theorem 7.4 follows:
all fixed Gaussian Haar moments have square-root
scale unconditionally in the invariant-free case,
and are equivalent to target zero exclusion when
an invariant constituent is present.

The two constructions leave precise places for
new work: signed coupling between different
primitive Kummer characters in the original
family, or a source-specific estimate on the
invariant component of the dense family.
Neither is resolved by rearranging positive
norm inequalities. Nothing here forbids a new
arithmetic identity or cancellation beyond what
weighted total variation can detect.

No numerical experiment, finite zero census,
proof-assistant build, or replay of the imported
quasi-Riemann result is part of these proofs.
Polynomials (6.11) and (7.23) are exact finite
calculations. The new unconditional all-order
theorem concerns the independent Haar model
with its invariant part absent, not the native
physical-row moment hierarchy.
