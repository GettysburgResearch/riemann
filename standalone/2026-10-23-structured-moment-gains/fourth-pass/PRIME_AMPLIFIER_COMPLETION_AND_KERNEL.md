# Quartic prime amplifiers: an exact completion cutoff and the changed Fourier kernel

Status: proved finite/local identities and an exact finite Fourier obstruction;
exploratory analytic consumer. No smaller zero-free boundary is proved.
Scope: the physical numerator is `k^3` throughout. The amplifier rows are
literal primary prime fourth powers, not arbitrary fourth-power-free rows.
Date: 24 October 2026.

## 1. Inputs and the question answered

The quartic Gauss convention is DDHL,
[arXiv:2306.11875v5](https://arxiv.org/html/2306.11875v5), equations
(3.4)--(3.7). Work over `O=Z[i]`, omit the fixed bad prime, and use primary
generators. Put `alpha(c)=c/|c|` and

\[
 g_4(n,c)=\sum_{x\bmod c}\chi_c(x)\check e(nx/c),\qquad
 \gamma(c)=g_4(1,c)/\sqrt{Nc}.
\]

In the source-compatible fixed ray sectors,
`gamma(c)^2=mu(c)alpha(c)` on squarefree `c`. Consequently the physical
first-Poisson coefficient with a Mobius factor is the conjugate of a
quartic Gauss coefficient with numerator **`k^3`**. This is retained from
the second-pass note at `GettysburgResearch/riemann@884230ea56eca4ce9f59bbc293c5f4d92e4a708d`.

The comparison point is PR1019 at
`3bcc1daaeb51c71cb2785b9744cde0d641f68f4c`:

* `PHYSICAL_QUARTIC_CUBIC_ROW_MEAN.md`, blob
  `3d3d1e148a7e2c4cad639c2f1d68b3f2c89299be`;
* `QUARTIC_CUBIC_NUMERATOR_TAIL.md`, blob
  `61559d39f12eab4c5d6562fee3d5f23c8cbbe620`;
* `FINITE_CUBE_FREQUENCY_TRACE.md`, blob
  `5d99d9436c237a286c5c186d0c7e4769e98841a6`.

The first of these obtains a source-dependent squarefree-row mean
`K + K^(13/8-3 delta)` at normalized real part `1/2+delta`. Its annular
consumer pays `D^(2 delta)` and optimizes at `D^(17/12)`. That established
limitation is not rederived as new progress here.

The new questions are narrower:

1. Can projecting onto the principal amplifier rows `u=pi^4` eliminate
   the powerful completion terms exactly?
2. If it does at the local paired-kernel level, does the ordinary short
   Poisson scale `K=D^2/H` survive the projection?

The answers are: a useful local cutoff does hold; the short Fourier
kernel does not survive. The distinction is quantified below.

## 2. A local support theorem for every pair of modulus exponents

Let `p` be a good prime of residue cardinality `q`, and put

\[
 F_j(x)=q^{-j}g_4(x^3,p^j),\qquad F_0(x)=1.
\]

For nonnegative integers `j,l`, define the normalized finite Fourier
coefficient using the **product-modulus period**:

\[
 \mathcal B_{j,l}(u)
 =q^{-(j+l)}\sum_{x\bmod p^{j+l}}
       F_j(x)\overline{F_l(x)}\,e_{p^{j+l}}(-ux).       \tag{2.1}
\]

The additive pairing is perfect and fixed. Multiplying its parameter
`u` by a local unit does not change any of the valuation-support claims.
Such unit changes are exactly what arises when applying CRT to global
coprime factors. Angular factors and reciprocity phases independent of
`x` also do not change support.

**Local theorem.** Suppose at least one of `j,l` is at least two.

* If `v_p(u)=0`, then `B_{j,l}(u)=0`.
* If `v_p(u)=4`, then a nonzero value is possible only for
  `(j,l)=(7,0)` or `(0,7)`.

This statement includes both-powerful products, and not merely a
powerful term paired with the squarefree head.

### 2.1 Exact local functions

If `4` does not divide `j`, DDHL's local formula implies that `F_j` is
zero unless

\[
 j=3a+1,\qquad v_p(x)=a.                            \tag{2.2}
\]

For `x=p^a r` with `r` a unit it is a nonzero constant, independent of
`r`, times `chi_p(r)^j`. In particular it is periodic modulo
`p^(a+1)`. Here the exponent of the character is correct because
`bar(chi_p(r)^3j)=chi_p(r)^j`.

For `j=4b`, the exact Ramanujan formula is

\[
 F_j(x)=1_{p^{\lceil j/3\rceil}\mid x}
       -q^{-1}1_{p^{\lceil(j-1)/3\rceil}\mid x}.     \tag{2.3}
\]

Thus every `F_j` is periodic modulo `p^t`, where

\[
 t=\lceil j/3\rceil.                              \tag{2.4}
\]

The functions `F_2,F_3,F_5,F_6` are zero. Every nonzero `F_j` with
`j>=2` has `j>=4` and is supported on `p|x`. By contrast `F_1` is
supported on the units. Hence

\[
 F_j\overline{F_1}=0\quad(j\ge2).                 \tag{2.5}
\]

### 2.2 Periodicity pays the full valuation cost

If a function modulo `p^m` is periodic modulo `p^t`, its normalized
Fourier coefficient at `u` vanishes unless `p^(m-t)|u`. Apply this to
the product in (2.1), with

\[
 m=j+l,\qquad
 t=\max\{\lceil j/3\rceil,\lceil l/3\rceil\}.       \tag{2.6}
\]

If both factors are powerful and nonzero, `j,l>=4`, so

\[
 j+l-t\ge6.                                      \tag{2.7}
\]

This excludes valuations zero and four. If the other factor has
exponent one, (2.5) applies. It remains to pair a powerful term with
`F_0`.

For `j>=8`,

\[
 j-\lceil j/3\rceil\ge5,                         \tag{2.8}
\]

so valuation four is excluded. The only remaining exponents are four
and seven. At four,

\[
 F_4(x)=1_{p^2\mid x}-q^{-1}1_{p\mid x}.
\]

Its Fourier coefficient modulo `p^2` is

\[
 q^{-2}(1-1_{p\mid h}).                            \tag{2.9}
\]

In the product-modulus period `p^4` this is supported on **exactly**
`v_p(u)=2`, so it contributes nothing at valuation four. At seven,

\[
 F_7(p^2r)=q^{-1/2}\gamma_3(p)\chi_p(r)^3
       \quad((r,p)=1),                            \tag{2.10}
\]

and it is zero elsewhere. Its Fourier transform modulo `p^3` is
supported on unit frequencies and is a nonzero constant times
`chi_p(h)`. In the period `p^7`, therefore, it is supported on
**exactly** `v_p(u)=4`. This proves the theorem.

### 2.3 Why the literal row label matters

For the `p^7` branch, writing the local Fourier transform in its smaller
period `p^3` produces a unit frequency `h`. The frequency in (2.1) is
nevertheless

\[
 u=p^4h.                                         \tag{2.11}
\]

The quartic character of `p^4h` agrees with that of `h` away from `p`.
Erasing `p^4` from the arithmetic character is permissible only if the
row profile is rescaled too. Erasing it from the *row label* would
incorrectly claim that this branch affects prime fourth powers
coprime to `p`. Its actual support forces `p|u`.

For the first powerful branch `p^4`, the same calculation produces
`u=p^2h` with `h` a unit. This is the exact local cancellation found
in the previous finite-trace note, now placed in the product-modulus
Fourier transform.

## 3. Consequence for a finite paired completion

For any good moduli `c,d`, the function

\[
 k\longmapsto {g_4(k^3,c)\over Nc}
           \overline{{g_4(k^3,d)\over Nd}}
\]

is periodic modulo `cd`. Its normalized Fourier coefficient at `u`
factors, by CRT and twisted Gauss multiplicativity, into local
coefficients of the form (2.1), multiplied by explicit nonzero constants
and with local unit changes in `u`. The support theorem therefore gives:

**Finite completion cutoff.** Let `Nc,Nd<=D_0`, and let `pi` be a good
primary prime with

\[
 (N\pi)^7>D_0.                                   \tag{3.1}
\]

At the literal Fourier row `u=pi^4`, every term for which either `c`
or `d` is nonsquarefree vanishes. Hence a finite sum of these paired
Fourier coefficients can be completed from squarefree to arbitrary
moduli, with no error at that row, provided the other coefficient and
profile factors are independent of `k`.

Proof: a powerful prime different from `pi` meets the first case of the
local theorem. A powerful factor at `pi` can contribute only with
exponent seven in one modulus and exponent zero in the other. This is
excluded by (3.1). The proof includes any number of powerful primes and
all both-powerful products.

For an annulus `Nc,Nd<=C D` and prime amplifiers `Npi~Q`, (3.1) holds
throughout the amplifier for sufficiently large `D` if

\[
 Q=D^{a/4},\qquad a>4/7.                          \tag{3.2}
\]

In particular it holds with room to spare at the quartic target
`a=14/15` corresponding to boundary `17/20`.

**Scope of this corollary.** This is a statement about the paired finite
Fourier kernel just displayed. The full raw inverse moment has a
separate common-divisor correction. One cannot replace that correction
by the naive product of two Gauss coefficients. If the correction has
first been retained, the corollary applies to its unshared coprime
modulus factors, at primes outside the fixed correction modulus.
It does not itself identify that corrected object with a positive
ordinary cube-row norm.

For example, at a prime shared by two squarefree original moduli, the
original row function is `1_(p not dividing u)`. Its Fourier coefficient
in the product period `p^2` is

\[
 1_{p^2\mid k}-q^{-1}1_{p\mid k},                  \tag{3.3}
\]

whereas the product of the two normalized squarefree Gauss factors is
a scalar times `1_(p not dividing k)`. These are different functions.
Equation (3.3), or its exact gcd/divisor expansion, must remain in the
global formula.

## 4. The exact global prime-amplifier identity

Let `P` be a finite collection of good primary primes of norms comparable
to `Q`, and let `w_pi>=0`. For one fixed smooth annular profile write

\[
 M_u(D)=\sum_c {\mu(c)\nu(c)\chi_c(u)\over\sqrt{Nc}}
                       W(Nc/D),\qquad
 \mathcal I_P(D)=\sum_{\pi\in P}w_\pi|M_{\pi^4}(D)|^2.          \tag{4.1}
\]

All common-prime zeros are retained. If
`a_c=mu(c)nu(c)W(Nc/D)/sqrt(Nc)`, then the exact global paired formula is

\[
 \mathcal I_P(D)
 =\sum_{c,d}a_c\overline{a_d}
    \sum_{\substack{\pi\in P\\(\pi,cd)=1}}w_\pi.              \tag{4.2}
\]

For every pair `c,d`, set `m=cd`, and define on `O/m`

\[
 \theta_{c,d}(u)=\chi_c(u)\overline{\chi_d(u)},\qquad
 \widehat\theta_{c,d}(k)
 ={1\over Nm}\sum_{u\bmod m}\theta_{c,d}(u)e_m(-ku),
\]

\[
 \mathcal K_{P,m}(k)
 =\sum_{\pi\in P}w_\pi e_m(k\pi^4).               \tag{4.3}
\]

Finite Fourier inversion gives the exact Poisson-side version of (4.2):

\[
 \boxed{\quad
 \mathcal I_P(D)
 =\sum_{c,d}a_c\overline{a_d}
       \sum_{k\bmod cd}\widehat\theta_{c,d}(k)
                            \mathcal K_{P,cd}(k).
 \quad}                                                        \tag{4.4}
\]

This formula includes the original diagonal `c=d`, every common divisor,
the principal frequency, and every other frequency. It does not require
assigning a nonzero phase at a character zero. Local evaluation of
`widehat theta` gives the usual Gauss factors at unshared primes and
(3.3) at shared primes. Thus (4.4) is also an exact way to audit any
subsequent Gauss-series completion.

The kernel in (4.4) is a prime fourth-power exponential sum. It is not
the Fourier transform of a smooth dense row annulus. In particular,
the identity does not justify replacing it by a common rapidly
decreasing profile at `K=D^2/Q^4`.

## 5. A quantitative obstruction to preserving the short dual range

Let `M=Nm`. Suppose the residues `pi^4 mod m` are distinct. This holds,
for example, when `m=cd`, `Nc,Nd~D`, and `Q^4=o(D^2)`: the norm of the
difference of two distinct fourth powers in the fixed prime annulus is
`O(Q^4)`, whereas a nonzero multiple of `m` has norm at least `M~D^2`.
Primary representatives also remove associate collisions.

Put

\[
 L_1=\sum_{\pi\in P}w_\pi,\qquad
 L_2=\sum_{\pi\in P}w_\pi^2,\qquad
 R_P=L_1^2/L_2.
\]

Orthogonality and the triangle inequality give the exact identity and
bound

\[
 \sum_{k\bmod m}|\mathcal K_{P,m}(k)|^2=M L_2,
 \qquad
 \sup_k|\mathcal K_{P,m}(k)|\le L_1.                \tag{5.1}
\]

Consequently, for **every** subset `T` of frequencies,

\[
 {\sum_{k\in T}|\mathcal K_{P,m}(k)|^2
       \over\sum_{k\bmod m}|\mathcal K_{P,m}(k)|^2}
 \le {|T|R_P\over M}.                             \tag{5.2}
\]

If `H=Q^4` and `T` has the ordinary short dual size `O(M/H)`, then

\[
 {\text{Fourier mass in }T\over\text{total Fourier mass}}
 \ll {R_P\over H}\le {|P|\over Q^4}\ll Q^{-3}.     \tag{5.3}
\]

The last inequality only needs the elementary lattice count `|P|<<Q`.
It does not need a prime-ideal theorem or an estimate for exponential
sums over primes. In the customary unit-weight amplifier,
`|P|~Q/log Q` is available in a fixed ray class, but that refinement is
unnecessary here.

Thus a proportion `1-O(Q^-3)` of the squared Fourier mass lies outside
the ordinary dual range. Any set carrying a fixed positive proportion
of the mass has cardinality at least

\[
 \gg {M\over R_P}\ge {M\over |P|}
 \gg {D^2\over Q}.                                \tag{5.4}
\]

For `Q=D^(a/4)`, compare

\[
 K_{\rm dense}=D^{2-a},\qquad
 |T|_{\rm necessary}\gg D^{2-a/4}.                \tag{5.5}
\]

The exponent difference is `3a/4`. This is not a small loss which can
be hidden in smooth seminorms or an epsilon power.

The same issue can be stated as an operator identity. Multiplication by
the indicator of the prime fourth powers is an orthogonal projection
in the original finite row space. After the unitary finite Fourier
transform it becomes a convolution operator with kernel
`K_(P,m)/M`; it is not diagonal frequency restriction. Its operator norm
is one, but this does not preserve a short frequency support. Replacing
the convolution by a diagonal or positive short-row average is exactly
the unsupported step that (5.2) rules out.

## 6. The principal consumer and what remains useful

For the principal Gaussian inverse (`nu=1`), the exact prime puncture
identity is

\[
 M_1(D;W)=M_{\pi^4}(D;W)
       -(N\pi)^{-1/2}M_{\pi^4}(D/N\pi;W).          \tag{6.1}
\]

It follows by separating multiples of `pi` in the Mobius sum. With the
usual common-profile Sobolev argument for the varying length `D/Npi`, a
bound of the strength

\[
 \mathcal I_P(D)\ll D^\epsilon Q^4
 \quad\text{at }Q=D^{a/4}                         \tag{6.2}
\]

for the required profiles and smaller lengths would imply

\[
 |M_1(D;W)|^2\ll D^{3a/4+\epsilon},\qquad
 \zeta(s)\ne0\quad(\Re s>1/2+3a/8).               \tag{6.3}
\]

The transfer uses `zeta_(Q(i))(s)=zeta(s)L(s,chi_-4)`, as usual; the
finite omitted Euler factors are nonzero in the positive half-plane.
For example `a=14/15` would yield `17/20`. No claim of (6.2) is made.

The local theorem removes a real complication from a future proof of
(6.2): in a finite paired completion at the literal principal rows,
powerful branches are absent once `(Npi)^7` exceeds the column cutoff.
One need not pay the generic all-row primitive-tail Cauchy budget for
that particular paired kernel.

The remaining analytic object is precisely (4.4), with the broad
prime-fourth-power kernel and the shared-prime factors intact. A useful
new theorem would estimate this actual bilinear pairing, or its
Fourier-conjugated projection on the completed cube-coefficient vector,
by the right side of (6.2). The ordinary positive cube-row mean does not
provide this theorem: it controls diagonal row energy and does not
control the coherent off-diagonal convolution produced by the projector.

Applying the short Mobius identity before the Gauss conversion does
expose Type-I numerators `k a^2`, since quartic twisted multiplicativity
introduces only a quadratic symbol in the new factor. Balanced Type-II
pieces can then use the quadratic large sieve. However, a rowwise
Cauchy treatment still pays a full positive diagonal; no centered
estimate for (4.4) follows from that decomposition alone. This is a
possible route to the required pairing, with the exact target now
identified, rather than a completed improvement.

## 7. Outcome and limits

The new result in this pass is the all-exponent local support theorem
and its `Q^7>D` principal-amplifier cutoff. The new obstruction is the
exact Fourier mass bound (5.3): projecting onto prime fourth powers
cannot retain the ordinary dense-annulus dual range.

Neither result changes the reported zero-free boundary. No remote files
were modified, no frozen earlier proof was edited, and no finite check
is being promoted to an analytic estimate. The proofs above use exact
finite Fourier orthogonality and DDHL's local Gauss formula; the open
step is the analytic bound for the full paired kernel (4.4).

## 8. The actual broad operator and rough amplifiers

The length `D^2/Q` in (5.4) is a **necessary cardinality**, not an upper
bound for the effective Fourier support. In particular one may not
truncate the broad kernel there merely because that choice makes a
subsequent exponent calculation favorable.

There is also an exact operator calculation that treats all its
frequencies together. Take unit amplifier weights, `Q=D^q` with fixed
`q>0`, and let `C` be a set of `n` squarefree column ideals of norms at
most `C_0D`. Its prime-amplifier Gram matrix is

\[
 \Gamma_{c,d}
 =\sum_{\pi\in P}1_{(\pi,c)=1}1_{(\pi,d)=1}
 =L-E_{c,d},\qquad L=|P|.                         \tag{8.1}
\]

Every `c` has at most `log(C_0D)/log(Q)` prime divisors from `P`, up to
the harmless fixed constants of the annulus. Thus

\[
 0\le E_{c,d}\le C_q,
 \qquad
 n(L-C_q)\le\|\Gamma\|_{\rm op}\le nL,\qquad
 n(L-C_q)\le\|\Gamma\|_{\rm HS}\le nL.             \tag{8.2}
\]

The operator lower bound uses the normalized constant vector; the upper
bound follows from the row sums. The Hilbert--Schmidt bounds follow
entrywise. Equivalently,
`||Gamma-L 11*||_op <= C_q n`. For `L` tending to infinity the
operator is asymptotically a rank-one operator of size `Ln`.

For a positive-density annular squarefree column set, `n=D^(1+o(1))`.
The actual normalized inverse coefficients have squared `ell^2` norm
`D^o(1)`. A coefficient-independent operator or Hilbert--Schmidt bound
therefore gives only

\[
 \mathcal I_P(D)\ll L D^{1+o(1)}.                 \tag{8.3}
\]

Dividing by the amplifier size gives `|M_1(D)|^2<<D^(1+o(1))`, the
trivial unnormalized Mobius exponent one. Optimizing `Q` does not
change this conclusion. Passing to a common finite row modulus and
performing a unitary finite Fourier transform preserves the Gram
matrix, so its broad Fourier representation has the same operator
obstruction. Unit-modulus column changes of basis likewise preserve
both norms. This is a calculation for the complete operator, not an
assertion that the particular Mobius coefficient vector attains its
largest eigenvalue.

It leaves open a coefficient-sensitive estimate for the particular
angular Gauss vector. Such an estimate needs a mixed correlation with
the broad kernel; it is not supplied by an ordinary diagonal second
moment together with a generic kernel operator norm. A scalar Weyl
bound for (4.3) also does not by itself give a separated common-profile
norm: its modulus `cd` changes with both columns. Completing the
amplifier sum introduces quartic complete exponential sums with their
own moving Gauss factors.

### 8.1 A rough amplifier does not flatten the principal Gram matrix

For any amplifier integers `r`, the row `r^4` gives
`chi_c(r^4)=1_(r,c)=1`. Suppose every prime dividing an amplifier has
norm at least `R=D^rho`, where `rho>0` is fixed, and the amplifier norms
are `O(Q)`. For each column pair, only `O_rho(1)` prime divisors can
exclude an amplifier. The number of Gaussian integers of norm `O(Q)`
divisible by one such prime is `O(Q/R+1)`. Thus a unit-weight rough
amplifier of cardinality `L` has

\[
 \Gamma_{c,d}=L+O_\rho(Q/R+1).                    \tag{8.4}
\]

If `L=Q D^o(1)`, the same rank-one conclusion follows. A nonnegative
bounded sieve weight has the same upper bound for the excluded mass,
with its total weight in place of `L`.

Moreover, retaining the exact completion cutoff by requiring every
amplifier prime factor to exceed `D^(1/7+eta)` forces an amplifier of
norm below `D^(2/7+2eta)` to have at most one prime factor. Thus in the
range `Q` close to `D^(1/4)`, that rough construction is already a prime
amplifier; it does not provide a new dense polynomial kernel.

### 8.2 The complete integer-amplifier main term retains the inverse

There is an exact positive decomposition of the complete local-density
Gram matrix. Define

\[
 \rho(n)=\prod_{p\mid n}(1-(Np)^{-1}),\qquad
 h(e)=\prod_{p\mid e}(Np-1)^{-1}\quad(e\text{ squarefree}).
\]

Uniformly averaging `1_(r,cd)=1` over a full residue system modulo a
common squarefree multiple of the columns gives `rho(cd)`. For any
finite column coefficients,

\[
 \boxed{\quad
 \sum_{c,d}a_c\overline{a_d}\rho(cd)
 =\sum_{e\ {\rm sf}}h(e)
      \left|\sum_{e\mid c}a_c\rho(c)\right|^2.
 \quad}                                                       \tag{8.5}
\]

Indeed `rho(cd)=rho(c)rho(d)/rho((c,d))`, and
`1/rho(g)=sum_(e|g)h(e)` on squarefree `g`. The `e=1` term is already
the square of a weighted Mobius inverse when the physical coefficients
are inserted.

Its Dirichlet series is

\[
 \sum_n{\mu(n)\rho(n)\over(Nn)^s}
 ={1\over\zeta_{\mathbb Q(i)}^S(s)}\,
 \prod_{p\notin S}
 \left(1+{(Np)^{-s-1}\over1-(Np)^{-s}}\right).       \tag{8.6}
\]

The correction product is holomorphic and nonzero for `Re(s)>0`.
Absolute local uniform convergence follows from the exponent `1+Re(s)`.
Its local numerator `1-(1-1/Np)(Np)^(-s)` has zeros only in the negative
half-plane, and its denominator has zeros on the imaginary axis.
Thus the weighted inverse has exactly the same possible poles from
zeros of the Dedekind zeta function in the positive half-plane.

Conditioning the amplifier to be coprime to a fixed finite set `T`
replaces `rho` by
`rho_T(n)=prod_(p|n,p notin T)(1-1/Np)` and removes those primes from
the correction product. Equations (8.5)--(8.6) have the corresponding
restricted version. The remaining product and its reciprocal are
uniformly bounded on each fixed right half-plane `Re(s)>=delta>0`,
independently of the finite set `T`. Consequently a growing roughness
condition does not remove the inverse appearing in the complete main
term.

These identities do not forbid a coefficient-sensitive cancellation
argument. They locate the term that such an argument must actually
estimate; a coefficient-blind operator norm, complete-amplifier main
term, or uncertainty-based truncation cannot supply the smaller
boundary.
