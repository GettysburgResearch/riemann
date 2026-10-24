# Natural presentation radicals with any fixed power gap below the column length

24 October 2026. Status: proposed source-dependent strengthening,
submitted for independent review. This is a new result after the frozen
fourth-pass commit; no earlier mathematical file is edited. The saving
is existential and depends on the fixed conductor gap. No improved
global zero-free boundary is claimed.

## 1. Exact inputs, scope, and theorem

The mathematical parent is
`GettysburgResearch/riemann@8c88fd23300bba093ce2f78295c4e27dbd60147d`,
under `standalone/2026-10-23-structured-moment-gains/fourth-pass/`.
The two directly extended files are:

* `MOBIUS_DIVISOR_COEFFICIENT_ADAPTER.md`, SHA256
  `8d2b8e49149008a4541b8d6e8b993254252f124c2259241d24d65f4d6ce1bb7d`;
* `NATURAL_PRESENTATION_TWIST_EXTENSION.md`, SHA256
  `fda494d598fa01a5f6c652b9bf503bad2fc95f4fe1a3af7e594b41b43ce6775f`.

The underlying source remains `openai/math` at
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`. Its cubic paper's
`sections/dual.tex` has byte-exact SHA256
`1209fd17cee79f4a21b71d66d3d8b60b210216fa783ec555959d2ebff2fba483`,
and `sections/background-type1.tex` has SHA256
`1c7be908c862dc440772964cfdd59e095e7b0f079cec11d99f5c7a9644198dd1`.
The natural reflection uses the quasi-Riemann source's
`old-eq:2.1c`--`old-eq:2.1d`, with its fixed-angular extension and
exact source bindings in the parent packet. These source statements
are imported premises, not reproved global results here.

Work in the inherited Eisenstein primary-ideal convention. Fix:

* an integer \(K\ge1\);
* an angular type \(\ell\), initial omitted primes, and finite ray data;
* a real number \(0<\sigma<1\), independently of all lengths;
* the parent's fixed smooth test class, with \(W\ge0\).

Let \(R\) be a squarefree good ideal. The complete natural
presentation \(\vartheta_R\) has a sextic unit character of any
exponent at each prime of \(R\), including exponent zero, and
vanishes on nonunits there. Thus \(R\) contains every moving good
primitive conductor prime and every moving good redundant zero.
The fixed-prime data range over the fixed family. Put

\[
 \theta_R=\Theta_\ell\nu\vartheta_R,
 \qquad a_K(n)=\mu(n)d_K(n)=\mu(n)K^{\omega(n)}.
\]

The presentation is common to a row mean. Define

\[
 J_{K,R}(A,B)=\sum_aW(a/\sqrt A)
 \left|\sum_n\frac{a_K(n)\theta_R(n)G(n)}{\sqrt{Nn}}
             \overline{\chi_n(a)}V(Nn/B)\right|^2,        \tag{1}
\]

with the cubic character and normalized cubic Gauss coefficient of
the source. All natural zeros are retained, and the primary rows
\(a\) have no squarefree restriction.

**Theorem.** Assume the parent's \(\mathrm{ZF}_\beta\) hypothesis
for every primitive finite-character twist of the fixed angular type,
with a possible principal pole, for a fixed \(1/2<\beta<1\).
Together with the pinned source estimates, this implies that some
\(\eta=\eta(\sigma,K,\beta)>0\) satisfies, for every
\(\epsilon>0\),

\[
 \boxed{\quad
 J_{K,R}(A,B)\ll (AB)^\epsilon
       \{A+(AB)^{2/3-\eta}\},\qquad
 A\ge B\ge2,\quad NR\le B^{1-\sigma}.
 \quad}                                                   \tag{2}
\]

The constants may depend on the fixed arithmetic data and test class,
in addition to the displayed fixed parameters; they are uniform in
the allowed presentation \(R,\vartheta_R\). The gap \(\sigma\)
is fixed before the constants, neighborhoods, heights, and outer
cutoffs are chosen. No uniformity as \(\sigma\downarrow0\) is
claimed. In particular this does not assert the endpoint \(NR\le B\)
or a subpower gap such as \(NR\le B/\log B\).

The case \(NR\le1\) is already included by taking any fixed
\(\sigma\) in this interval. A restriction with \(\sigma>1\)
and \(B>1\) has no admissible radical.

## 2. The only new exceptional full-factor budget

First consider ordinary exceptional character sums with coefficient
\(\mu^{*K}\). Fix an auxiliary slack
\(0<\lambda\le1/2\). We claim that there exist
\(\delta_0,\eta_0>0\) for the source's two endpoint
neighborhoods, uniformly under

\[
 NR\le Y^{1-\lambda},\qquad
 1+|u|\le Y^{\lambda/16},\qquad Nv,Ne\le Y^{\delta_0}.
                                                               \tag{3}
\]

The norm height \(u\) is part of the smooth full-factor profile;
it is not absorbed into the fixed arithmetic data. The endpoint
pairs are

\[
 (\log_Y P,\log_Y Q)=(1,0),\qquad (1/3,1/3).
\]

### Principal rows and the short identity

Separate primitive-principal inducing rows before any reflection.
There are none at nonzero fixed angular type. Otherwise every good
prime of \(pq\) must divide \(R\operatorname{rad}v\), since
the cubic local character outside this union is nonprincipal. The
number of coprime squarefree pairs is therefore at most
\(3^{\omega(R\operatorname{rad}v)}\ll Y^\epsilon\).
Each original \(\mu^{*K}\) polynomial is bounded by
\(Y^{1+\epsilon}\), so these rows cost \(Y^{2+\epsilon}\).
The same bound will apply to an original \(a_K\) polynomial.

Apply the exact identity \(\mu=2m-m*m*1\), with the truncated
\(m\) supported up to a fixed multiple of \(Y^{1/2}\), to
each of the \(K\) convolution factors. Common Mellin separation
gives at most \(3K\) factors in each product, with every truncated
Möbius factor of length at most \(Y^{1/2+o(1)}\). Thus a factor
whose limiting length exponent is one is a full smooth sum. This is
the parent's proved coefficient reduction.

Truncate the additional common Mellin shifts at
\(Y^{\lambda/16}\). The number of shifts is fixed. For sufficiently
large \(Y\), the total norm height in a full factor is at most
\(Y^{\lambda/8}\). The omitted tails have arbitrary power decay
after choosing finitely many smooth orders. No growing-height cost is
hidden in a test seminorm: the pure norm twists are translated in
their Mellin variables as in the exact source full-sum lemma.

### Natural reflection of a limiting full factor

Let \(Z=Y^{1+o(1)}\) be the full-factor length. The reviewed natural
functional equation retains the common conjugate natural character
and every zero. If \(Q_\psi\) is the primitive conductor norm and
\(R_0\) the redundant natural radical, then

\[
 Q_\psi\,NR_0\ll N(Rvpqe).
\]

The symmetry-line Euler quotient has arbitrarily small power norm,
uniformly in this radical. On each retained dual dyad of length \(J\)
the amplitude is \(Y^\epsilon\sqrt{Z/J}\), and the common largest
dual cutoff is

\[
 J\ll Y^\epsilon N(Rvpqe)(1+|u_{\rm total}|)^2/Z.       \tag{4}
\]

Root numbers, conductor phases, and the Euler quotient are bounded
row scalars outside the polynomial. The common norm-shift measure is
the one in the natural-reflection input; no enumeration of the
row-dependent redundant factors is introduced.

Set

\[
 q_\lambda=1-\lambda+2(\lambda/8)
            =1-3\lambda/4<1.                            \tag{5}
\]

In the limiting first configuration \(P=Y^{1+o(1)}\),
\(Q=Y^{o(1)}\), equation (4) gives
\(J\le Y^{q_\lambda+o(1)}\). The unrestricted-inner cubic
sieve, including the squared reflection amplitude, bounds the
full-factor moment by

\[
 Y^{1+o(1)}\{Y+J+(YJ)^{2/3}\}.
\]

Since \(q_\lambda\ge5/8\), its exponent is at most

\[
 1+\frac23(1+q_\lambda)
     =\frac73-\frac\lambda2.                            \tag{6}
\]

In the second configuration \(P=Q=Y^{1/3+o(1)}\), the dual
cutoff is \(J\le Y^{q_\lambda-1/3+o(1)}\). A trivial dual
sum of length \(J\), multiplied by \(\sqrt{Z/J}\), has size
\(\sqrt{ZJ}\). Sum its square over \(Y^{2/3+o(1)}\) rows:
the resulting exponent is at most

\[
 \frac23+1+q_\lambda-\frac13
      =\frac73-\frac{3\lambda}{4}.                    \tag{7}
\]

Thus both dominant-full-factor cases have a strict positive gap for
each fixed \(\lambda>0\). These are the changes to the old
numerical \(.70/.74\) budget. They do not require that convenient
fixed budget.

### The remaining product configurations

If every limiting factor length is less than one, the source's
ordinary and cubic sieve inequalities and off-diagonal Gram argument
are unchanged. The whole natural character, including its zeros,
belongs to the common coefficient vector in the unpunctured ambient
Hilbert space. These estimates do not depend on \(NR\).

At the first endpoint the multiplicity inequalities give
\(d_i=v_i-5a_i/6\le0\) and hence row exponent \(r\ge2/3\).
For a positive factor with \(a_i\le1/2\), omission gives
\(d_i\ge0\), so this selected factor has \(d_i=0\).
Fixed copies reach a length strictly between \(4/3\) and 2; the
Gram contradiction remains valid at \(r\ge2/3\). At the second
endpoint the original repeated-factor ordinary-sieve contradiction
applies. The count \(3K\) is fixed, so the source's compactness
argument yields uniform positive \(\delta_0,\eta_0\).

Equations (6)--(7), the same product argument, and the separated
principal rows therefore prove the claimed exceptional estimate for
\(\mu^{*K}\) under (3). Only the full-factor cases have used the
new conductor-gap budget.

## 3. Transfer to the squarefree divisor coefficient

For every fixed \(0<\sigma<1\), there exist
\(\delta,\eta_{\rm exc}>0\) such that

\[
 \sum_{p,q}\left|\sum_{(n,e)=1}a_K(n)\theta_R(n)
       (Nn)^{iu}W_0(Nn/Y)\chi_n(vpq^2)\right|^2
      \ll Y^{7/3-\eta_{\rm exc}}                       \tag{8}
\]

in the two \(\delta\)-endpoint neighborhoods, uniformly for

\[
 NR\le Y^{1-\sigma},\qquad
 1+|u|\le Y^{\sigma/64},\qquad Nv,Ne\le Y^\delta.    \tag{9}
\]

Use the exact parent identity

\[
 a_K=\mu^{*K}*h_K,
 \qquad \sum_{j\ge0}h_K(p^j)x^j=\frac{1-Kx}{(1-x)^K}.
                                                               \tag{10}
\]

The coefficient \(h_K\) is supported on powerful ideals and has
\(\sum_d|h_K(d)|(Nd)^{-s}<\infty\) for every fixed real
\(s>1/2\). As before, the primitive-principal rows are removed
before this identity, at cost \(Y^{2+\epsilon}\).

For \(Nd\le Y^\rho\), set \(Z=Y/Nd\) and use Section 2 with
\(\lambda=\sigma/2\). Choose, in this order, its positive
neighborhood \(\delta_0\), then

\[
 0<\rho<\min(\sigma/4,\delta_0/10),
\]

and then \(\delta>0\) sufficiently small. One has

\[
 Y^{1-\sigma}\le Z^{1-\sigma/2},\qquad
 Y^{\sigma/64}\le Z^{\sigma/32}.                      \tag{11}
\]

The first follows from
\(\rho(1-\sigma/2)<\sigma/2\), and the second from
\(\rho<1/2\). The endpoint lengths and the small \(v,e\) data
also remain in the selected \(\delta_0\)-neighborhoods relative
to \(Z\). Freezing \(d\) changes only a scalar and the common
norm scale; it introduces no \((n,d)=1\) condition or new inducing
character. All original zeros distribute multiplicatively.

Minkowski bounds the square-root moment of these small-divisor terms
by

\[
 \sum_{Nd\le Y^\rho}|h_K(d)|
       (Y/Nd)^{7/6-\eta_0/2}
 \ll Y^{7/6-\eta_0/2},                                  \tag{12}
\]

after decreasing \(\eta_0\) below \(1/10\). The coefficient
mass in (12) converges absolutely.

The parent proof's large-divisor bounds require no restriction on
the common moving natural character. For \(Nd\asymp D\ge
Y^\rho\), fixing \(d\) and using the unrestricted-inner cubic
sieve followed by Minkowski gives respectively

\[
 Y^{O(\delta)+\epsilon}
  \{Y^2+Y^2/D+Y^{7/3}D^{-2/3}\},                       \tag{13}
\]

and

\[
 Y^{O(\delta)+\epsilon}
  \{Y^{5/3}+Y^{7/3}/D+Y^{20/9}D^{-2/3}\}.             \tag{14}
\]

The entire \(\theta_R\), and all exclusions, are in the common
coefficient vector. Choose \(\delta\) and the internal losses
small compared with \(\rho\); sum the logarithmically many
dyads. Equations (12)--(14) prove (8). The exponent
\(\eta_{\rm exc}\) remains existential, depending on
\(\sigma,K\) and the fixed test data.

## 4. Full-moment handoff with explicit choices

The full Poisson assembly, original pair diagonal, and all
\(f,m,l\) masks remain the parent's literal ones. The co-deleted
Euler identity for \(a_K\) still gives the required uniform
Möbius cancellation under \(\mathrm{ZF}_\beta\): it uses
\(L(s,\psi)^{-K}\), ordinary deleted Hecke factors, and the
co-deleted absolutely convergent \(H_K\) product. No factor
\((1-K\psi(p)(Np)^{-s})^{-1}\) is bounded separately.
The larger \(R\) is still polynomial in \(AB\), so all its
arbitrarily small conductor/radical powers are absorbed in the
requested \((AB)^\epsilon\).

The short-dual range is handled exactly as before. In the remaining
range one has \(B\le A\le B^{2\beta}\), and may use
\(X=AB\) and \(c=1/4\). After the standard small outer cuts,
the exceptional column length is

\[
 Y=B/(FL),\qquad F,L\le X^{\delta_{\rm out}},\qquad
 Y\ge X^c.
\]

Apply Section 3 with its conductor gap \(\sigma/2\), and call its
neighborhood radius \(\delta_{\rm exc}\). In addition to the
source's earlier \(\beta\)-dependent restrictions choose

\[
\begin{split}
 \delta_{\rm out}&\le
    \min\{c\sigma/16,\ c\delta_{\rm exc}/100,\ 1/100\},\\
 \rho_{\rm freq}&\le\delta_{\rm exc}/10,\\
 \delta'&\le
    \min\{\delta_{\rm out}/100,\ c\sigma/512\}.
\end{split}                                                \tag{15}
\]

Then the full presentation radical satisfies

\[
 NR\le B^{1-\sigma}
      =Y^{1-\sigma}(FL)^{1-\sigma}
 \le Y^{1-\sigma+2\delta_{\rm out}(1-\sigma)/c}
 \le Y^{1-7\sigma/8}
 <Y^{1-\sigma/2}.                                        \tag{16}
\]

The last weak inequality uses (15) and \(1-\sigma\le1\).
The inherited small-label handoff is

\[
 Nv\le Y^{4\delta_{\rm out}/c},\qquad
 Ne\ll Y^{\rho_{\rm freq}+(7\delta_{\rm out}+2\delta')/(3c)}.
                                                               \tag{17}
\]

Both exponents are strictly below \(\delta_{\rm exc}\) with the
choices (15). The common Mellin shifts can be truncated at
\(X^{\delta'}\le Y^{\sigma/512}\); their fixed number and
bounded initial heights put the total input height below
\(Y^{\sigma/256}\) for large \(Y\). This is inside the
Section 3 allowance \(Y^{(\sigma/2)/64}=Y^{\sigma/128}\).
The smooth tails are negligible after choosing the fixed derivative
orders. These height choices are made before asserting uniformity.

Thus (8) supplies the two exceptional estimates needed in the full
moment. All generic large-conductor and large-common-divisor bounds
use common divisor-bounded coefficients and are unchanged. The same
source compactness assembly supplies a positive full-moment
\(\eta(\sigma,K,\beta)\). This proves (2), with its original
diagonal term \(A\) and all frequencies retained.

## 5. Rectangular consequence

Decrease \(\eta\) below \(1/12\) if necessary. For
\(1\le A\le B\), choose
\(C\asymp(B/A)^{1/3}\), with the same fixed endpoint enlargement
as in the parent cubic-power amplifier. The exact identity for the
\(a_K\)-weighted column and the divisor-bounded fibre proof are
unchanged. A branch with divisor \(d\mid\operatorname{rad}c\)
has column length \(B/Nd\) and row scale \(A C^3 Nd\).
The new full-moment input is therefore valid in every branch under
the sufficient restriction

\[
 NR\le(B/C)^{1-\sigma},                                \tag{18}
\]

with the parent's fixed constant adjustment for the endpoints of the
\(c\)-window. Equivalently, one may replace \(C\) in (18) by its
fixed upper window endpoint. The result is

\[
 \boxed{\quad
 J_{K,R}(A,B)\ll(AB)^\epsilon
   \{A^{1/3}B^{2/3}+A^{1/3}B^{1-2\eta}\},\qquad
 1\le A\le B,
 \quad}                                                   \tag{19}
\]

under (18). The presentation is not changed or unmasked in a
shortened branch; every moving prime is still charged to the same
\(R\). This is a conductor-range strengthening, not a stronger
size exponent at a fixed \(A,B\).

## 6. One consumer translation, without a new boundary claim

In the frozen fourth-moment component notation, \(B=U\),
\(A=(X/T)^{1/2}\), and the moving squarefree core has norm
\(NR\asymp T\). The new shortened-column condition is, up to
fixed endpoint factors and a strict margin,

\[
 T\le U^{4(1-\sigma)/(7-\sigma)}
          X^{(1-\sigma)/(7-\sigma)}.                    \tag{20}
\]

At \(X\asymp U^2\) it becomes
\(T\le U^{6(1-\sigma)/(7-\sigma)}\). This approaches the
exponent \(6/7\) as a *fixed* \(\sigma\) is chosen small.
It only enlarges the conductor range in which the existing component
argument may be applied. That argument's size bound remains
\(U^{1-\eta}X^{-1/6}T^{2/3}\), with the new existential
\(\eta\). Its power-saving core cutoff and its remaining signed
complement are not eliminated by (20).

At the excluded conductor endpoint, the limiting full-factor dual
exponent can reach one. The first endpoint's reflected sieve bound
then reaches \(7/3\), as does the second endpoint's trivial dual
bound. The proof here gives no uniform saving there. This is the
precise endpoint limitation of this argument, not an impossibility
statement about a stronger moment or a global consumer.
