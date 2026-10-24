# Actual cubic columns in the short sixth-power core

Status: proposed source-dependent analytic deduction, 23 October 2026.
Scope: the unselected inverse over the fixed Eisenstein field
`E=Q(omega)`. The main result bounds the complete short-core sector of its
first Poisson transform, including every common-support overlap, both signed
divisor variables, every extracted sixth power, moving punctures and fixed
finite-ray factors. There are no selected-prime marks. This is not an
estimate for the full inverse moment or a new zero-free boundary.

Write `H>=1` and `D>=1` for the original row and column scales, and let
`L>=1` cut off the sixth-power-free part of the actual dual frequency
`k=d'h'`. Let `T_short(H,D;L)` be the signed, principal-restored nonzero
component restricted by this cutoff, with the source's common smooth
kernel and original frequency mask retained. Then

\[
 \boxed{\quad |T_{\rm short}(H,D;L)|
 \ll_\epsilon (DH L N\mathfrak j)^\epsilon\mathcal S\,
                  H^{2/3}L^{4/3}.\quad}                 \tag{A}
\]

Here `mathfrak j` is the inherited fixed puncture and `mathcal S` is one
fixed finite profile seminorm, with polynomial dependence on the source's
norm-twist heights. This assertion uses the Euler-half-plane endpoint of
the cubic Type-I argument; it uses no zero-free half-plane premise.
Under the common finite-order Hecke zero-free input with boundary
`1/2<beta<1`, there is the further estimate, stronger when `L<=H`,

\[
 \boxed{\quad |T_{\rm short}(H,D;L)|
 \ll_\epsilon (DH L N\mathfrak j)^\epsilon\mathcal S\,
 H^{(3-\beta)/(5-2\beta)}L^{(7-3\beta)/(5-2\beta)}.\quad} \tag{B}
\]

Consequently this entire sector is at most the target row scale `H` for
`L<=H^(1/4)` in (A), or for
`L<=H^((2-beta)/(7-3beta))` in (B), with strict buffers for the small
power losses. The conditional input in (B) concerns finite-order cubic
characters and their fixed finite-ray twists. No angular zero-free
extension is used. Sections 1--7 prove these statements.

### The exact truncated expression

Here is a definition independent of any positive-child enlargement.
Use `q_a=Na` and fix one source ray summand and earlier norm-twist mode.
Put `A_*(z)=a0(z)nu_*(z)`. In the pinned source's
`eq:initial-formal-component`, set every selected-prime mark to one and
insert `1_(q_R(d'h')<=L)`. Explicitly the resulting expression is

\[
\begin{split}
T_{\le L}={}&
\sum_{\substack{C\ {\rm sf},\ d'\mid C\\h'\ne0}}
 \mu(d')\,b(C,d',h')\,1_{q_{R(d'h')}\le L}
 \sum_{\substack{z_1,z_2\ {\rm sf}\\(z_1,z_2)=1\\(z_1z_2,C\mathfrak j)=1}}
 A_*(z_1)\overline{A_*(z_2)}\\
&\quad\times\overline{\chi_{z_1}(d')}\chi_{z_1}(h')
              \chi_{z_2}(d')\overline{\chi_{z_2}(h')}
 W(q_Cq_{z_1}/D)\overline{W(q_Cq_{z_2}/D)}\\
&\quad\times\frac{H}{Dq_{d'}\sqrt{q_{z_1}q_{z_2}}}
 \mathcal K\!\left(\frac{Hq_{h'}}{q_{d'}q_{z_1}q_{z_2}}\right).
\end{split}                                                   \tag{C}
\]

The bounded outer coefficient `b` is exactly the source's fixed ray
Fourier coefficient, original individual dyad cutoffs, retained frequency
ball and `1_(C,mathfrak j)=1`; it has no dependence on `z1,z2` or on the
divisor `s` introduced later. The complete source partitions are summed.
`T_short` is (C) summed over its finite ray/unit sectors and integrated
against its one common weighted Fourier measure. The estimates also
apply to one such term with its own seminorm factor.

The ideal `R(k)` is the unique sixth-power-free part of the full nonzero
frequency ideal `(k)` in `(k)=R(k)e^6`, after clearing the source's fixed
lattice denominator if needed. It is the core of `k=d'h'`, not of `h'`.
Prime powers at the fixed excluded set are included in this definition.
Their valuations in `R(k)` range from zero to five, so their contribution
to the finite-ray character belongs to one fixed finite family. All higher
valuations remain in `e`; they are counted, not omitted.

Expression (C) includes the restored nonzero principal pairs
`z1=z2=1`. It excludes the original zero-frequency term and the raw
ratio tail discarded before the source's displayed identity. When (C)
is used to bound the original nonprincipal inverse, the separate cost
of adding or removing the restored principal pairs must still be included.
No assertion in this note identifies (C) with the full inverse moment.

## 1. The exact coefficient dictionary

The source is `openai/math` at
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
SHA256 `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
The relevant formulas are `eq:signal`, `eq:initial-formal-component`,
`eq:initial-common-extraction` and `eq:initial-outer-arithmetic`.

On good squarefree ideals, its literal Gauss identities give

\[
 \gamma_1(n)\gamma_2(n)=\mu(n)\alpha(n)G(n),\qquad
 \mu(n)\gamma_{-1}(n)
 =\bar\alpha(n)\gamma_2(n)\chi_n(-1)\overline{G(n)}.
\tag{1}
\]

The function `G` and the displayed minus-one character are fixed finite-ray
data. After the source's finite Fourier expansion, the actual transformed
column is

\[
 a_0(n)\nu_*(n),\qquad a_0(n)=\bar\alpha(n)\gamma_2(n).
\tag{2}
\]

Thus the transformed Möbius coefficient is an angular cubic Gauss coefficient,
not an arbitrary vector and not the sextic primitive residue pairing in PR1019.
The angular order is minus one when the original inverse has finite-order
coefficient. In particular its theta series has no spherical main pole.

For the exact match with the cubic source, put `lambda=sqrt(-3)`,
`alpha(n)=n/|n|`, and use primary generators `n=1 mod 3` and
`Nn=|n|^2`. The source's
`eq:reflection-cubic-sextic-conversion` is

\[
 \widetilde g_3(n)=\chi_n(\lambda)^{-2}\gamma_2(n),\qquad
 a_0(n)\nu_*(n)=\widetilde g_3(n)\alpha(n)^{-1}
                     [\chi_n(\lambda)^2\nu_*(n)].       \tag{2a}
\]

The bracket is a fixed finite-ray character on the actual good-prime
support. Its supplementary-law modulus is fixed, and all its natural
zeros are kept. The symbol orientation therefore agrees with
Dunn--Radziwill's normalized cubic Gauss sum, rather than merely agreeing
in absolute value. Ideals and their allowed generators differ by only the
fixed unit sectors used in the source.

## 2. A row bound with its exact effective conductor

Fix a finite-ray character `nu`, a good squarefree label `f`, a moving
puncture `Q`, and a sixth-power-free good ideal `R`. Put

\[
 L_{R,e,f}(N)=N^{-1/2}\sum_n a_0(n)\nu(n)
    \chi_n(Rf^4)\mathbf1_{(n,Qe)=1}W(Nn/N).
\tag{3}
\]

The fixed smooth test is annular; uniformly bounded families in the necessary
finite test seminorm are permitted. Natural zeros remain at every prime
dividing `Rf`, even if the primitive local character becomes principal.
The squarefree support of `n` comes from the cubic Gauss coefficient.
Bounded nonempty endpoint scales `N<1` are absorbed by a profile-dependent
constant; below the fixed lower scale imposed by the support the sum is empty.

For the primitive character induced by `chi_n(Rf^4)` after a fixed reciprocity
partition, let `C0` be the product of the good primes with local digit four,
and `C1` the product of the good primes with local digit one, two, three or
five. Digit-zero primes that occur in `Rf` are retained in the puncture.
Here and below an ideal in a real power denotes its absolute norm.

The Euler-only case of Theorem T in PR1010,
`a1afee36313ff5994dad7b97983948113571965e`,
`standalone/2026-10-20-primitive-twist-type-i/PROOF.md`, yields

\[
 |L_{R,e,f}(N)|^2
 \ll_\epsilon (NRe f Q)^\epsilon C_0^{1/2}C_1.
\tag{4}
\]

No quasi-RH premise is used in (4). Theorem T itself states `beta<1`;
we use its proof directly at the Euler endpoint, rather than invoke an
endpoint not present in its statement. Take
`p=1/2`, `q=1/4`, and shift the cubic variable only to
`Re s=1/2+eta`. Its completion is an ordinary Hecke function evaluated at
`Re(3s-1/2)>1`, so its reciprocal is controlled by the absolutely convergent
Euler product. The nonzero angular order removes the possible theta pole.
The primitive periodic transform gives the effective conductor `C0 C1^2`;
it does not permit replacing `C1` by its square root.

Here are the analytic details required from that proof. If
`psi` is the primitive moving twist and `ell=-1`, write

\[
 R_{\psi,\ell}(z)=\sum_n\widetilde g_3(n)\psi(n)
             \alpha(n)^\ell(Nn)^{-z},\qquad
 Q_{\psi,\ell}(z)=L^{\rm del}(3z-1/2,\psi^3\alpha^{3\ell})
                       R_{\psi,\ell}(z).
\tag{4a}
\]

Fixed finite-ray factors are included in `psi` here; `del` deletes every
prime required by its original presentation. The squarefree/cube
coefficient identity is literal, with no coprimality condition between
the squarefree and cube indices. At a moving good prime the finite
transform is the Gauss transform of `psi_p*kappa_p`, multiplied by the
primitive Gauss factor of `psi_p`. A matching prime has transform modulus
`q^(1/2)|c_p(v)|`, where `c_p` is the Ramanujan sum. A nonmatching prime
has modulus `q 1_(p does not divide v)`. All frequencies, including zero,
are included. The dual cusp coefficients have magnitude at most a fixed
constant times `3^(k/6)(Nb)^(1/2)` at an index `lambda^k zeta a b^3`,
with `a` squarefree and arbitrary overlap between `a,b`.

At real `z>=1`, the entire matching-prime dual local majorant is

\[
 F_q(z)=1+(q-1)q^{-z}
 +(q-1)(1+q^{-z})\frac{q^{1/2-3z}}{1-q^{1/2-3z}},
 \qquad F_q(1)<2.
\tag{4b}
\]

The unramified dual series is therefore bounded on `Re z=1+eta` by
`C0^(1/2+epsilon) C1`, up to fixed height factors. The general
periodic-twist functional equation and interpolation between `-eta`
and `1+eta` give

\[
 |Q_{\psi,-1}(\sigma+it)|
 \ll (C_0C_1)^\epsilon
     C_0^{(1-\sigma)/2+O(\eta)}
     C_1^{1-\sigma+O(\eta)}(1+|t|)^A.                   \tag{4c}
\]

The angular order is nonzero, so there is no theta residue. On
`sigma=1/2+delta`, the completion in (4a) is evaluated at
`Re(3z-1/2)=1+3delta`; its reciprocal is bounded by its absolutely
convergent Euler product, uniformly in the moving character. Extra
deleted Euler factors cost only a subpower. Mellin inversion on this
line, with sufficiently many fixed test derivatives, yields an
unnormalized bound
`N^(1/2+epsilon) C0^(1/4+epsilon) C1^(1/2+epsilon)`.
This is (4) after central normalization and squaring. The analytic
inputs in this paragraph are the periodic-twist functional equation,
cusp expansions and pole statement of Dunn--Radziwill, Section 5,
as used with exact formulas in PR1010, Sections 2--5. These source
identities are imported, not certified by a finite calculation.

Theorem T is printed for a primitive squarefree good modulus. A fixed
finite-ray factor at the excluded primes changes this proof only by a fixed
finite transform: decompose its finite periodic profile once, retain that
fixed transform on both sides of the completed functional equation, and
keep its finitely many local completion factors. Their conductor and
transform norms are constants. At each moving good prime the transform and
its `C0/C1` distinction are unchanged. The cube coefficient is the cube of
the actual fixed character, so its completion remains an ordinary Hecke
function on the Euler half-plane. This justifies the fixed finite-ray
version of (4), without treating a moving good-prime twist as fixed.
The exact fixed-prime construction used here is the pinned source's
`eq:reflection-local-fourier`, `eq:reflection-translated-theta`, and
`eq:reflection-cusp-expansion`: a fixed finite Fourier sum of theta
translates has a fixed finite collection of cusp coefficient bounds.
The CRT transform at a moving good prime remains the one above.

The mask `e` is handled by the exact divisor expansion in Theorem T section 8.
A selected divisor `d` of its radical contributes a matching cubic twist and
scale `N/d`; at the Euler exponents its weight is `d^(q-p)=d^(-1/4)`.
The divisor sum costs only a subpower. Shared primes already excluded by
the primitive conductor or a natural zero are simply still excluded.

## 3. Sum every extracted sixth power and every short core

For `X,L,N>=1`, with `L<=X`, define the explicit nonnegative packet

\[
 \mathcal S_f(X,L,N;Q)=
 \sum_{\substack{R\ {\rm sixth\!\!free}\\NR\le L}}
 \sum_{N(R e^6)\le X}|L_{R,e,f}(N)|^2.
\tag{5}
\]

The sum includes arbitrary common primes between `R`, `e`, and `f`.
The only zeros involving `n` are exactly those in (3).
Then

\[
 \boxed{\quad
 \mathcal S_f(X,L,N;Q)
 \ll_\epsilon (XLNfQ)^\epsilon f^{1/2}X^{1/6}L^{11/6}.
 \quad}
\tag{6}
\]

**Proof.** Define `c(R)=C0(R)^(1/2)C1(R)` without the fourth-power label.
At a prime of `f`, let `j=v_p(R)` run from zero through five. Adding the
fourth-power label changes its digit to `j+4 mod 6`. In the six cases the
ratio `c(Rf^4)/c(R)` is respectively

\[
 q^{1/2},\quad1,\quad q^{-1},\quad1,\quad q^{1/2},\quad1.
\]

Therefore `c(Rf^4)<=f^(1/2)c(R)`. The case with new digit zero retains its
natural puncture; only its primitive conductor is removed from this weight.

There are `O((X/NR)^(1/6))` ideals `e` for each `R`, by fixed-field ideal
counting. Write uniquely

\[
 R=r_1r_2^2r_3^3r_4^4r_5^5
\]

with squarefree pairwise coprime `r_j`. Then
`c(R)=r_1r_2r_3r_5 r_4^(1/2)`. Drop pairwise restrictions only in this
positive majorant. Sum first over `r1` using
`sum_(Nr1<=Y) (Nr1)^(5/6) << Y^(11/6)`.
The remaining exponents on `r2,r3,r4,r5` are respectively

\[
 -3,\qquad -5,\qquad -15/2,\qquad -9.
\]

All four ideal sums converge. This proves
`sum_(NR<=L) (NR)^(-1/6)c(R) << L^(11/6)`, hence (6), after taking smaller
internal epsilon losses. Every extracted sixth power is included; no
unproved orthogonality among distinct labels is needed. QED.

For the actual frequency, `R=R_S R_good`, with the `S`-supported
sixth-free part `R_S` ranging over a fixed finite set. Its symbol is
absorbed into the finite family of `nu` in (3), as licensed by the
source's `eq:row-fixed-ray-reduction`. Apply (6) to `R_good` with
`X/NR_S,L/NR_S`, and sum that finite set. The `S`-part of `e` is
unrestricted in the ideal count. Thus (6) holds for the full core
defined in (C), with only a fixed change in its constant.

## 4. The scale of the actual first-Poisson consumer

In the trivial-overlap unselected component `C=d'=s=1`, the source has
dual row length `X=D^2/H`, normalized column length `N=D`, and outside
factor `H/D`. The component with sixth-free dual core at most `L` is
therefore bounded by

\[
 \boxed{\quad H^{5/6}D^{-2/3}L^{11/6+\epsilon}.\quad}
\tag{7}
\]

The same assertion holds for the fully separated smooth kernel with the
source's common weighted Fourier seminorm: apply (4) to each of its two
column profiles, then Cauchy in the common frequency rows, and finally
integrate that single finite seminorm. It does not replace the common
kernel by unrelated tests before deriving the identity.

In particular all these cores contribute at most the target row scale `H`
when

\[
 L\le H^{1/11}D^{4/11}
\tag{8}
\]

with the usual strict buffers for arbitrary positive losses. For the example
`H=D^(6/7)`, taking `L=D^(1/2)` instead gives `D^(27/28+epsilon)`, which
is below the inherited full inverse resource `D^(41/42+epsilon)` by
`D^(1/84)`. This comparison applies to this entire truncated core sector,
not to the full inverse vector.

## 5. The other common-divisor components

For a fixed actual overlap `C`, a divisor `d'|C`, and the signed common
divisor `s`, the exact source variables are

\[
 N=D/(Cs),\qquad f=d's,\qquad
 X=\frac{D^2(d')^2}{HC^2},\qquad
 \hbox{outside factor}=\frac{H}{D d's}.
\tag{9}
\]

These come from `k=d'h'`, the full root normalization, and the physical
kernel, not from a new row enlargement. Here `C` is squarefree,
`d'|C`, and `s` is squarefree and prime to `C`. These facts come from
the original squarefree columns and the complete Mobius projector.
They imply that `f=d's` is squarefree, as required in (3).
The puncture is `Q=rad((C/d') mathfrak j)`, in addition to the natural
zeros at `d',s,h'`. The outer factor `1_(s,h')=1` is also retained.
The finite unit class of `k=Re^6` gives a fixed finite-ray twist;
`chi_n(e^6)` is exactly `1_(n,e)=1`, even at a shared prime.
There is no assertion that `R,e,f` are pairwise coprime.

Dropping the divisibility
restriction `d'|k` only after taking a positive majorant, (6) yields

\[
 \frac{H^{5/6}}{D^{2/3}C^{1/3}(d')^{1/6}s^{1/2}}
 L^{11/6+\epsilon}
\tag{10}
\]

for that fixed component's truncated-core part. It does not assert
cancellation in the outer signs `mu(d')mu(s)`.
Absolute summation over `NC~C0`, `Ns~S0` and `d'|C` costs, in a coarse
bound,

\[
 H^{5/6}D^{-2/3}C_0^{2/3}S_0^{1/2}L^{11/6+\epsilon}.
\tag{11}
\]

Thus (7) cannot be silently summed with its trivial-overlap constant.
The changing fourth-power labels and the signed common-divisor sum are
substantive arithmetic data.

For the rest of the proof write `C,S` for these two dyad centers and
`T(C,S;L)` for their actual signed contribution with the common core
cutoff `N(R(k))<=L`. Formula (11) says

\[
 |T(C,S;L)|\ll Z^\epsilon\mathcal S\,A(C,S),\quad
 A(C,S)=H^{5/6}D^{-2/3}C^{2/3}S^{1/2}L^{11/6}.
\tag{13}
\]

Here and below `Z^epsilon` abbreviates an arbitrarily small power of
the displayed moving scales and the inherited puncture. If `X<1`,
the nonzero original frequencies have a positive lower norm and the
Schwartz decay of the actual kernel supplies the same estimate.
For `Nk>X`, decompose into common dyads and absorb their powers by
that same decay. This proves the weighted form of (13) for the full
source kernel and retained outer ball, not only for a hard row cutoff.

## 6. A core count with the original row divisibility

For a good squarefree ideal `a`, `X>0`, and `L>=1`, the required
count is

\[
 \sum_{\substack{R\ {\rm sixthfree},\ NR\le L\\e\ne0,
                    \ a\mid Re^6}}
 \left(1+\frac{N(Re^6)}X\right)^{-A_0}
 \ll_\epsilon (2+X+Na+L)^\epsilon
             \frac{X^{1/6}L^{5/6}}{Na},\qquad A_0>2.
\tag{14}
\]

The same proof permits the factor `(Na)^epsilon` in place of the
displayed harmless small power. The count includes all integral ideals,
including the fixed excluded prime set. The fixed lattice denominator
and finite unit multiplicity are absorbed in the constant.

First, for squarefree `b`,

\[
 \sum_{\substack{R\ {\rm sixthfree},\ NR\le Y\\b\mid R}}
                   (NR)^{-1/6}
 \ll_\epsilon Y^{5/6}(Nb)^{-1+\epsilon}.                \tag{15}
\]

To prove this, write `R=r1 r2^2 r3^3 r4^4 r5^5`, as above, and
assign each prime of `b` to the unique nonzero valuation digit
`1,...,5`. If `b=b1 b2 b3 b4 b5` is one resulting ordered
factorization, the sum over `r1`, with `b1|r1`, is at most
`Y1^(5/6)/(Nb1)`. After this sum the remaining variables have
weights `(Nrj)^(-j)`, `j=2,...,5`. Restricting `bj|rj` costs at
most a constant times `(Nbj)^(-j)`, hence at most `(Nbj)^(-1)`.
The unrestricted zeta sums converge. The number of assignments is
`5^omega(b)`, which is a subpower of `Nb`. This proves (15).

Since `a` is squarefree, `a|Re^6` implies that, for
`b=gcd(a,rad(R))`, one has `b|R` and `a/b|e`. For a hard cutoff
`N(Re^6)<=X`, ideal counting gives at most
`(X/NR)^(1/6)/(N(a/b))` choices of `e`. Sum this over every
`b|a`, using (15). Each term is at most
`X^(1/6)L^(5/6)/(Na)` times a subpower, so their complete divisor
sum proves the unweighted version of (14). A decomposition into
dyads of `N(Re^6)/X` proves its weighted version. When `X<1`, begin
at the first nonempty dyad; the decay only improves the bound.

This argument is valid when `R` and `e` share primes. It preserves
the density `1/Na`; discarding `a|Re^6` would lose that density.

## 7. Keep the signed divisor sum and assemble all overlaps

The old signed long-gcd argument is proved in PR1012 at
`64cb43c038d1828a478cb97cbc32e435e111d2d2`,
`standalone/2026-10-20-boundary-iteration/global/SIGNED_MOBIUS_GCD_TAIL.md`.
Here is its exact use with the new core cutoff. Freeze
`C,d',h',n1,n2`. The arithmetic dependence on `s` is

\[
 \mu(s)\chi_{n_1}(s)^4\overline{\chi_{n_2}(s)^4}
                       1_{(s,C\mathfrak jh')=1}.       \tag{16}
\]

Its inducing character is finite order; conductor drops retain all
original zero primes in the puncture. A common finite-order zero-free
half-plane `Re z>beta` gives the punctured Mobius estimate
`sum_(Ns<=y) mu(s) psi(s)1_(s,Q)=1
 << (conductor(psi) NQ)^epsilon y^(beta+epsilon)`.
Its conductor-uniform proof uses the reciprocal Hecke Euler product,
the zero-free logarithm, uniform polynomial growth and Perron. The
moving conductor divides `rad(n1 n2)` up to fixed data. For `beta=1`
use the unconditional absolute bound `O(y)` instead.

The complete profile in this sum contains

\[
 \frac1{Ns}W\!\left(\frac{NC\,Ns\,Nn_1}D\right)
 \overline{W\!\left(\frac{NC\,Ns\,Nn_2}D\right)}
 \mathcal K\!\left(\frac{HNh'}{Nd'\,(Ns)^2Nn_1Nn_2}\right).
\tag{17}
\]

Its Euler derivatives on `Ns~S` are at most
`S^(-1)(1+Nk/X)^(-A0)` times a fixed seminorm, where
`k=d'h'` and `X=D^2(Nd')^2/(H(NC)^2)`.
Partial summation therefore contributes
`S^(beta-1)(1+Nk/X)^(-A0)`.
The cutoff `N(R(k))<=L` depends only on `d',h'`; in particular
it is independent of both `s` and the residual columns. It does
not alter this partial summation or its derivatives. Neither the
signed sum nor the common profile has been separated into unrelated
positive children before this step.

Afterward the two residual column sums may be bounded absolutely:
`(sum_(n~D/(CS)) (Nn)^(-1/2))^2 << D/(CS)`.
The full frequency count gives the inherited estimate

\[
 |T(C,S;L)|\ll Z^\epsilon\mathcal S\,B_{\rm full}(C,S),
 \qquad B_{\rm full}=D^2 C^{-2}S^{\beta-2}.             \tag{18}
\]

It remains valid for the restricted frequencies because all frequency
counts at this stage are positive. Alternatively, keep `d'|k` and
apply (14) with `a=d'`. For one fixed actual overlap and divisor,
the factors are

\[
 \frac H{D\,Nd'}\cdot\frac D{NC\,S}\cdot S^{\beta-1}
 \cdot\frac{[D^2(Nd')^2/(H(NC)^2)]^{1/6}L^{5/6}}{Nd'}
 =H^{5/6}D^{1/3}(NC)^{-4/3}(Nd')^{-5/3}
                         S^{\beta-2}L^{5/6}.          \tag{19}
\]

The divisor sum over `d'|C` is subpower; the `O(C)` ideals in the
overlap dyad then give the new second signed estimate

\[
 |T(C,S;L)|\ll Z^\epsilon\mathcal S\,B_{\rm short}(C,S),
 \qquad B_{\rm short}=H^{5/6}D^{1/3}C^{-1/3}
                               S^{\beta-2}L^{5/6}.     \tag{20}
\]

All three estimates (13), (18), and (20) apply to the same signed
component and cutoff. Set

\[
 a=\frac{4-2\beta}{5-2\beta},\qquad
 b=\frac{4\beta-2}{5(5-2\beta)},\qquad
 c=\frac{7-4\beta}{5(5-2\beta)}.
\tag{21}
\]

For `1/2<=beta<=1` these are nonnegative and sum to one. Hence

\[
 |T(C,S;L)|\ll Z^\epsilon\mathcal S\,
 A(C,S)^aB_{\rm short}(C,S)^bB_{\rm full}(C,S)^c
 =Z^\epsilon\mathcal S\,
 H^{(3-\beta)/(5-2\beta)}L^{(7-3\beta)/(5-2\beta)}.
\tag{22}
\]

The powers of `D,C,S` cancel exactly. The finitely many logarithmic
dyads from the original column support cost only a small power.
Integrating the common weighted Fourier seminorm and summing the
fixed ray and unit sectors proves (B). Taking `beta=1` with absolute
Mobius counting proves (A). As in definition (C), the restored nonzero
principal pairs are inside this signed expression. The source's separate
cost of adding/removing them remains necessary when returning to the
original nonprincipal inverse. The original zero-frequency term and the
discarded raw ratio tail are outside (C) and retain their source estimates.

## 8. Optimizing against the available long-core resource

The complementary cores `NR>L` remain. The all-length positive canonical
estimate has a formal diagonal of size `X=D^2/H`, which after multiplication
by `H/D` costs `D`; this is larger than `H` when `D>H`. Its cancellation
requires the entire signed common-divisor projector before the separate
positive-child inequalities. Nothing in (6) or (7) supplies that cancellation
on the long-core part. Even in the trivial-overlap sector the supplied
positive long-core resource is only
`(H/D)J_long(D^2/H,D) << D`, granting the all-length theorem
`J(X,D)<<X`. Combining this resource with the independently controlled
short sector incurs the comparison cost

\[
 \mathcal B_{\rm splice}(H,D;L)=H+
 H^{(3-\beta)/(5-2\beta)}L^{(7-3\beta)/(5-2\beta)}+D,
\tag{23}
\]

with separate profile losses suppressed. This is the size of the
available upper-bound resource, not a lower bound for an actual moment
and not an asserted new full-inverse theorem. The `D` term does not depend on `L`.
For `H<D`, minimizing (23) over `L` therefore cannot improve the
inherited inverse bound `H^(1/6)D^(5/6)`. It is not legitimate to
subtract the upper bound for the short sector from an upper bound
for all rows. The new result isolates the remaining problem to
long sixth-free cores after a complete, quantitatively controlled
short-core reassembly.

The diagonal cancellation itself still holds separately on either
core sector: for fixed `C,d',h'`, its selector is independent of `s`,
and the full reassembled diagonal is its common weight times
`sum_(s|z) mu(s)=1_(z=1)`. The missing estimate is the long-core
signed two-column form with this cancellation preserved, including
the common kernel, punctures, outer `mu(d')`, fourth-power labels,
and `d'|k`. A separately bounded positive long-core norm does not
provide it.

One must also not substitute the rapid large-length decay of an ordinary
nonprincipal Hecke-character polynomial for (4). The actual raw cubic series
has completion

\[
 R_{\psi,-1}(z)=
 \frac{Q_{\psi,-1}(z)}{L(3z-1/2,\psi^3\alpha^{-3})}.
\tag{24}
\]

The numerator has no spherical pole, but that alone supplies no zero-free
claim for the denominator left of its Euler half-plane. Removing cube
completion restores every divisor scale. Consequently an ordinary
character-sum argument with arbitrary decay in `N/conductor` is not a
licensed bound for these columns.

No full inverse improvement, smaller fixed zero-free boundary, or RH proof
is concluded here. The positive contribution is the exact cubic dictionary,
the conductor-sensitive row estimate, the complete extracted-power count
with its row divisibility, and the fully reassembled estimates (A)--(B).

## 9. Sources and finite checks

The analytic sources are the pinned Ope26a file and formula labels in
Section 1; Dunn--Radziwill, *Bias in cubic Gauss sums: Patterson's
conjecture*, arXiv:2109.07463v3, Section 5 and Appendix A; and the two
precisely pinned repository deductions PR1010 and PR1012 identified
above. A substitution of `beta=B_flat` in (B) retains Liu's imported
finite-order theorem and its source dependencies. It does not
independently certify that theorem.

`check_short_core.py` checks the local digit costs, every displayed
reassembly exponent, the divisibility-selector implication, and the
numerical cutoff exponents using exact rational arithmetic where
applicable. Its finite checks do not prove the functional equation,
the contour shifts, the uniform Mobius theorem, or any zero-free bound.
The acceptance predicates raise explicit exceptions and remain active
under Python optimization. The commands
`python3 -I -S -B check_short_core.py` and
`python3 -I -S -B -O check_short_core.py` produced byte-identical output,
saved as `short_core_check_report.json`.
