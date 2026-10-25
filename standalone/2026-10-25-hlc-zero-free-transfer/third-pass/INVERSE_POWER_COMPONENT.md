# An enlarged, coherent component of the actual native inverse

**Status: proved source-dependent component estimate.** The main theorem
below bounds an exact smooth component of the original Möbius inverse,
including the nonsquarefree physical rows and their natural zeros. It
uses the imported finite-order Hecke cap and moment framework stated
below. It does not bound the complementary component and does not by
itself establish a new zero-free region.

Put

\[
 \Gamma_0=\frac{83}{24}-\frac{\sqrt{195}}6
          =1.13095999270517647\ldots .
 \tag{1}
\]

For the exact smooth Heath--Brown decomposition defined in Section 2,
the new estimate is

\[
 \boxed{\quad
 \sum_u w_U(u)|M_u^{\rm lo}(U,U^r,t;W)|^2
 \ll_\epsilon U^{\Gamma_0+\epsilon}
                   (1+|t|)^A p_J(W)^2 .
 \quad}                                                     \tag{2}
\]

Here the outer product of the two short Möbius factors is selected by
$\chi_0(N\mathfrak r/U^{13/20})$, where $\chi_0=1$ through one
and $\chi_0=0$ from two onward. The coherent complementary weight is
$1-\chi_0$. This smooth outer selector is part of the theorem.
It is not replaced by a sharp inequality.

At the previously critical inverse length
$r=1.163953576509010956\ldots$, the inherited complete-inverse exponent
is $1.136627980424175797\ldots$. Thus (2) saves
$0.005667987718999325\ldots$ on this actual component. Its support
extends beyond the short-factor scale $U^{r/2}$. The complementary
outer products, supported above $U^{13/20}$, remain in the exact
identity.

## 1. Exact premises and arithmetic scope

The pinned arithmetic source is

- `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`;
- `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`;
- Git blob `268c4e3206d460c617d3d2129742a72b831b3def`.

The following are explicit imported premises.

1. Its `thm:main` gives the cap $\operatorname{Re}\rho\le7/8$ for
   every finite-order Hecke character over $E=\mathbb Q(\omega)$.
   The boundary line is allowed. The complete external proof of this
   premise is not independently certified here.
2. The polynomial-height buffered bins and their physical-row count are
   those of Xu--Sang,
   [arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2),
   Lemma 6.2 and Proposition 6.3, with the order of choices stated there.
   The printed floor $a_0=51/100$ is sufficient for (2).
   The corresponding local reciprocal argument is written out in
   `second-pass/CAPPED_NATIVE_MOMENT.md`.
3. The pinned source's `lem:plain`, equation `old-eq:2.1`, with an empty
   prime-slot list, gives
   \[
    \sum_u w_U(u)
       |S_{\psi_u^0}(N;V_1)S_{\psi_u^0}(N';V_2)|^2
      \ll_\epsilon U^{1+\epsilon}
          (1+|\mathbf t|)^A p_J(V_1)^2p_J(V_2)^2               \tag{3}
   \]
   on nonprincipal inducing rows, for every prescribed bounded pair of
   nonnegative log-lengths. Its zero-slot case has no conductor lower
   bound and no positive-prime-slot length restriction. Taking the two
   factors equal supplies the ordinary fourth moment used below.
4. The ordinary primitive Hecke functional equation, its finite-seminorm
   smooth-duality calculus, ideal counting, and the source's common
   smooth-profile and Sobolev calculus are retained. The primitive
   equation and its normalization were also read in the same pinned
   repository's
   `preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex`,
   Git blob `e93fbddf626ab532b7e8fbfac830f1b45370b0e3`.
   Only the ordinary equation is used; no metaplectic moment is
   transferred to this family.

Physical rows are the original sixth-power-free Eisenstein ideals or their
fixed primary representatives, $Nu\asymp U$. Fix a finite group of
finite ray characters whose conductor primes belong to a fixed set $S$
containing the primes above six. Fix a member $\nu$ and an orientation
$\varsigma\in\{1,-1\}$. Put

\[
 \psi_u^0(n)=\nu(n)\chi_n(u)^\varsigma,\qquad
 \psi_u(n)=\psi_u^0(n)1_{(n,Q)=1}.                            \tag{4}
\]

All powers retain zero on nonunits. Every original natural zero remains.
The extra puncture $Q$ is common within the row mean and may satisfy
$N\operatorname{rad}Q\le U^{C_Q}$ for any prescribed fixed $C_Q$.
The constants can depend on $C_Q$. Bounded nonnegative physical row
weights and common row restrictions are permitted.

The retained inducing characters are nonprincipal. For large $U$
this excludes no good physical row: at a prime outside $S$ every
positive valuation of a sixth-power-free row lies in $\{1,\ldots,5\}$,
so its nontrivial local character cannot be canceled by the fixed ray
factor. Any bounded exceptional principal presentations are treated in the
complete source expression before invoking this nonprincipal component
theorem. No assertion that includes such rows silently deletes them.

Fix $C\ge1$ and let $D=U^r$ with $1\le r\le C$. The theorem
is uniform over a common annular profile $W$ supported in $(1,2)$,
and over a common norm height $t$. We use

\[
 V_t(x)=x^{it}W(x),\qquad
 M_u(D,t;W)=D^{-1/2}\sum_n\mu_E(n)\psi_u(n)V_t(Nn/D).          \tag{5}
\]

Using $(Nn)^{it}$ instead multiplies this by the common unit-modulus
factor $D^{it}$. There are no nonzero angular characters in the
zero-free premise used here. A fixed finite family of the presentations
(4) is allowed; this does not grant unrelated character choices within a
single detected witness.

## 2. The exact smooth identity and its coherent pieces

Choose once and for all smooth functions $w_0,\chi_0:[0,\infty)\to[0,1]$
equal to one on $[0,1]$ and zero on $[2,\infty)$. Set

\[
 y=\sqrt{2D},\qquad
 m_y(a)=\mu_E(a)w_0(Na/y),\qquad
 a_y(r)=\sum_{ab=r}\mu_E(a)\mu_E(b)w_0(Na/y)w_0(Nb/y).
 \tag{6}
\]

The ideals $a,b$ need not be coprime. In particular $a_y$
contains essential repeated-prime terms, and $|a_y(r)|\le d_E(r)$.

**Exact convolution identity.** Since $\mu_E-m_y$ is supported above
$y$, the square of
$\delta_1-m_y*1=(\mu_E-m_y)*1$ vanishes through norm $y^2$.
Convolving by $\mu_E$ and expanding gives

\[
              \mu_E=2m_y-m_y*m_y*1
                       \qquad (Nn\le y^2=2D).              \tag{7}
\]

For $D>8$, the term $2m_y$ vanishes on $(D,2D)$ because
$2y<D$. Bounded $D$ is absorbed in the constants. Therefore

\[
 M_u(D,t;W)
 =-D^{-1/2}\sum_{r,c}a_y(r)\psi_u(r)\psi_u(c)V_t(NrNc/D).
 \tag{8}
\]

This is an ordinary full convolution. It is not a unitary convolution or
a sum only over coprime factorizations.

For a common smooth dyadic window $\eta_R(Nr/R)$, let
$M_{u,R}$ denote (8) with that window inserted. At
$R_0=U^{13/20}$ define

\[
\begin{split}
 M_u^{\rm lo}
  &=-D^{-1/2}\sum_{r,c}a_y(r)\chi_0(Nr/R_0)
               \psi_u(r)\psi_u(c)V_t(NrNc/D),\\
 M_u^{\rm hi}
  &=-D^{-1/2}\sum_{r,c}a_y(r)[1-\chi_0(Nr/R_0)]
               \psi_u(r)\psi_u(c)V_t(NrNc/D).
\end{split}                                                   \tag{9}
\]

Thus $M_u=M_u^{\rm lo}+M_u^{\rm hi}$ exactly. The low piece is
supported in $Nr<2R_0$, and the high piece is supported in
$Nr>R_0$. Their transition ranges overlap with complementary
weights. A smooth dyadic partition of the low selector has
$O(\log U)$ nonempty windows with $R\ll R_0$ and uniformly
bounded logarithmic derivatives.

The mean in (2) is the norm of the coherent low sum, not the sum of
individual dyadic squared norms. Minkowski's inequality will recover
the coherent estimate from the dyadic estimates. There is no assertion
that a bounded estimate for an unsigned sum controls these signed pieces.

## 3. Buffered inverse products and their fourth-moment envelope

Write $\delta=2a-1$ for a buffered bin. With the printed floor, bottom
bins have $\delta_0=1/50$ and at most $O(U)$ rows. The above-floor
bins have

\[
 \#\mathcal B_{i,a}\ll_\epsilon U^{\mathcal R(\delta)+\epsilon},
 \qquad
 \mathcal R(\delta)=\frac{15-16\delta}{15-6\delta}
                  =1-\frac{10\delta}{15-6\delta}.            \tag{10}
\]

The imported cap gives $\delta\le3/4$, so the second density branch
above $\delta=5/6$ is not needed here. The bound counts original
physical rows, including their powerful factors; it is not a squarefree
row count reused without its row ledger.

On each such bin, the local reciprocal argument gives, for a common
smooth inverse block of bounded log-length $\alpha\ge0$,

\[
 \left|A^{-1/2}\sum_a\mu_E(a)\psi_u(a)V(Na/A)\right|
   \ll_\epsilon U^{\delta\alpha/2+\epsilon}
                  (1+|v|)^{A_1}p_{J_1}(V),
 \quad A=U^\alpha,                                         \tag{11}
\]

where $v$ denotes a pure norm height separated from the untwisted
profile. This is also valid with the common extra puncture in (4).
Indeed its Euler deletions are nonzero in $\operatorname{Re}s>0$
and have polynomial-size radical. The zero-free disk, its Euler-normalized
logarithm, and the three-circles argument therefore give a subpower
reciprocal on the buffered line, as in the cited second-pass proof.

Here and below all orders are fixed before $U$ varies. Internal source
detector and moment orders are chosen first, then the positive polynomial
buffer height, then external Mellin-tail orders. Formula (11) holds in the
buffered height range by contour shifting. For greater heights the trivial
inverse bound is absorbed by increasing the fixed polynomial height order
$A_1$. Thus weighted full Fourier integrals may use (11) without
extending the zero-free rectangle to infinite height. When several
frequencies enter one $L$-argument their sum is the height in (11).
Their budgets are not spent separately inside the same argument.

Define the actual normalized smooth outer polynomial

\[
 A_{y,R,u}(V)
    =R^{-1/2}\sum_r a_y(r)\psi_u(r)V(Nr/R).                  \tag{12}
\]

**Lemma 1.** On a buffered bin, uniformly for all the bounded-power
scales in (6),

\[
 |A_{y,R,u}(V)|^2
       \ll_\epsilon U^{\delta\rho+\epsilon}
                  (1+|\mathbf v|)^{A_2}p_{J_2}(V)^2,
 \qquad R=U^\rho.                                         \tag{13}
\]

**Proof.** Split $a,b$ smoothly into $Na\asymp A$ and
$Nb\asymp B$. A nonempty pair in (12) has $AB\asymp R$.
Its common profile is a fixed annular product times

\[
       w_0(Ax/y)w_0(By/y)V((AB/R)xy).                       \tag{14}
\]

All invoked logarithmic derivatives are uniform. A derivative of either
cutoff is supported where its displayed argument is bounded, and
$AB/R$ lies in a fixed compact range. Logarithmic Fourier separation
of the common product profile makes the pair an integral of products of
two actual normalized Möbius blocks for the same $\psi_u$. The
normalization contributes $\sqrt{AB/R}\asymp1$. Apply (11) to each
block, with their actual total frequencies. Their exponents add to
$\delta(\log_UA+\log_UB)/2=\delta\rho/2+O(1/\log U)$.
The weighted Fourier $L^1$ norms are bounded by a fixed finite number
of derivatives of (14). Equivalently one may truncate at a fixed fraction
of the buffered height and choose the external tail order last. The
$O((\log U)^2)$ pairs cost an arbitrarily small power.

This proof does not require $R\le y$. Both short-factor cutoff
transitions remain smooth when $R>y$. That is the reason for using
(6), rather than inserting the hard truncation into a pointwise inverse
estimate. QED.

For $s\ge0$ put

\[
\begin{split}
 \mathcal E(s)
 &=\max_{0\le\delta\le3/4}
                    \{\mathcal R(\delta)+s\delta\}\\
 &=
 \begin{cases}
  1,&0\le s\le2/3,\\
  \displaystyle\frac83+\frac{5s}{2}
                         -\frac{10}{\sqrt6}\sqrt s,
          &2/3\le s\le200/147,\\
  \displaystyle\frac27+\frac{3s}{4},&s\ge200/147,
 \end{cases}\\
 \mathcal E_{.51}(s)&=\max\{1+s/50,\mathcal E(s)\}.
\end{split}                                                   \tag{15}
\]

The extended interval down to zero only enlarges the above-floor
maximum. Since
$\mathcal R'(\delta)=-150/(15-6\delta)^2$ and
$\mathcal R''(\delta)<0$, the interior maximizer is
$\delta_*(s)=5/2-5/\sqrt{6s}$. Its contacts with zero and $3/4$
give the two thresholds in (15).

Raise (13) to the second power, sum over the bins using (10), and include
the bottom bins. This proves

\[
 \sum_u w_U(u)|A_{y,R,u}(V)|^4
 \ll_\epsilon U^{\mathcal E_{.51}(2\rho)+\epsilon}
                   (1+|\mathbf v|)^{A_3}p_{J_3}(V)^4.
 \tag{16}
\]

For every $R\ll U^{13/20}$, the right side is bounded by its fixed
endpoint

\[
 E_*=\mathcal E(13/10)
       =\frac{71}{12}-\frac{\sqrt{195}}3
       =1.26191998541035294\ldots .                          \tag{17}
\]

The floor competitor is at most $1+13/500=513/500$, up to a
harmless constant-factor rescaling. It is strictly smaller than (17):
even the legal competitor $\delta=1/2$ gives
$\mathcal R(1/2)+(13/10)(1/2)=37/30>513/500$.
Thus no adjustable-floor extension is needed for (16) at this endpoint.

## 4. Primitive reflection with the natural dual still present

Let $\psi_u^*$ be the primitive inducing character and
$q_u=N\mathfrak f_u$ its primitive conductor norm. In the source's
normalization write

\[
                  \mathcal C_u=\frac{3q_u}{(2\pi)^2}.
 \tag{18}
\]

One may instead absorb the fixed field constant into the transform.
What matters is that $q_u\ll_S U$ and that the puncture conductor
does not enter $\mathcal C_u$.

Every good prime dividing the actual sixth-power-free row has conductor
exponent one. Therefore, after a fixed finite division into bad-place
sectors, the redundant zeros of $\psi_u^0$ relative to $\psi_u^*$
belong to one fixed subset $S_0\subset S$. Let $Q_s$ be the
squarefree union of this subset and $\operatorname{rad}Q$.

For a normalized ordinary sum put

\[
 T_{u,Q}(X)=X^{-1/2}\sum_c\psi_u(c)V_t(Nc/X),\qquad
 T_u^*(X)=X^{-1/2}\sum_c\psi_u^*(c)V_t(Nc/X).
\]

Exact deletion of the redundant zeros gives

\[
 T_{u,Q}(X)
   =\sum_{e\mid Q_s}
      \frac{\mu_E(e)\psi_u^*(e)}{\sqrt{Ne}}\,
          T_u^*(X/Ne).                                    \tag{19}
\]

The value here is the primitive $\psi_u^*(e)$, not the original
value that has been set to zero at a deleted prime. If $e$ meets
the primitive conductor its coefficient is already zero. No
coprimality condition between $e$ and its quotient is inserted.

For the nonprincipal primitive character, the ordinary functional equation
gives

\[
 T_u^*(X)=\varepsilon_u\,
          \overline T_u^*(\mathcal C_u/X;\Phi_t),
 \qquad
 \overline T_u^*(L;\Phi_t)
      =L^{-1/2}\sum_n\overline{\psi_u^*(n)}\Phi_t(Nn/L).
 \tag{20}
\]

The bar on $\overline T$ indicates the conjugate character. It does
not conjugate the common profile. The transformed profile and its Euler
derivatives are bounded at zero and rapidly decreasing at infinity, with
a fixed polynomial dependence on $1+|t|$ and fixed finite seminorms
of $W$. Formula (20) reflects a full $L$-function; it does not
move a reciprocal contour through its zeros.

To use (3), restore only the fixed bad-place zeros on the dual side:

\[
 \overline T_u^*(L;\Phi_t)
  =\sum_{\operatorname{rad}h\subset S_0}
       \frac{\overline{\psi_u^*(h)}}{\sqrt{Nh}}\,
           \overline T_u^0(L/Nh;\Phi_t),\qquad
 \overline T_u^0(Y;\Phi_t)
       =Y^{-1/2}\sum_n\overline{\psi_u^0(n)}\Phi_t(Nn/Y).
 \tag{21}
\]

This identity is the exact local Euler expansion. Its scalar mass is
bounded by the fixed product
$\prod_{p\in S_0}(1-(Np)^{-1/2})^{-1}$. The primitive local
values and their conjugates are retained. A good row prime never enters
this restoration: its primitive character already vanishes there.
There is no separately chosen row-dependent mask or column sequence.

Substitution into the component of (8), with $X=D/Nr$, gives

\[
\begin{split}
 M_{u,R}
  ={}&-\varepsilon_u\sum_{e\mid Q_s}
        \sum_{\operatorname{rad}h\subset S_0}
       \frac{\mu_E(e)\psi_u^*(e)\overline{\psi_u^*(h)}}
                         {\sqrt{Ne\,Nh}}\\
     &\quad\times\sum_r
       \frac{a_y(r)\eta_R(Nr/R)\psi_u(r)}{\sqrt{Nr}}\,
       \overline T_u^0\!
          \left(\frac{\mathcal C_uNrNe}{D\,Nh};\Phi_t\right).
\end{split}                                                   \tag{22}
\]

All signs, original row phases, natural zeros, and the root number are
still present. In unnormalized dual notation, the product of the displayed
normalizers is exactly $\sqrt{D/\mathcal C_u}/(Nr\,Ne)$, as in
`SIGNED_NATIVE.md`, equation (11). In particular the factor $Ne^{-1/2}$
in the normalized expression cannot be dropped when a puncture changes
the dual length.

## 5. Coupled profiles, the small dual scale, and the row norm

Divide the rows into dyadic primitive-conductor sectors
$\mathcal C_u\asymp\mathcal C_*$. There are $O(\log U)$ such
sectors. Fix $e,h,R,\mathcal C_*$ and write

\[
 L_0=\frac{\mathcal C_*R\,Ne}{D\,Nh},\qquad
 z=\mathcal C_u/\mathcal C_*,\quad x=Nr/R,\quad y'=Nn/N.
 \tag{23}
\]

Split the dual $n$-sum by a fixed smooth partition into $Nn\asymp N$,
with $N\ge1$ up to an immaterial fixed lower endpoint. Its contribution
to the inner line of (22) has the exact form

\[
 \sqrt{\frac N{L_0}}\,
 R^{-1/2}N^{-1/2}
  \sum_{r,n}a_y(r)\psi_u(r)\overline{\psi_u^0(n)}
      F_{N/L_0}(z,Nr/R,Nn/N),                               \tag{24}
\]

where, including the common annular cutoffs,

\[
 F_v(z,x,y')
       =z^{-1/2}x^{-1}\eta_R(x)\vartheta(y')
                      \Phi_t\!\left(\frac{v y'}{zx}\right).
 \tag{25}
\]

The extra factors in (25) record both central normalizations; they are
smooth on the fixed compact box. For any prescribed orders $K,B$,

\[
 \|F_v\|_{C_{\log}^K}
   \ll_{K,B}(1+|t|)^{A_{K,B}}p_{J_{K,B}}(W)(1+v)^{-B}.
 \tag{26}
\]

After extending by common cutoffs on a slightly larger box, logarithmic
Fourier separation in $z,x,y'$ expresses (24) as a weighted integral
of an outer polynomial (12), an ordinary dual polynomial
$S_{\overline{\psi_u^0}}(N;\cdot)$, and a scalar
$z^{i\xi_0}$ of modulus one. The row dependence in the conductor is
exactly this scalar. The separated column profiles are common to the
row sum. They are not independently chosen for different rows.

Apply Hölder to each such product, then (16) and (3):

\[
\begin{split}
 \sum_u w_U(u)|A_{y,R,u}S_{\overline{\psi_u^0}}(N)|^2
 &\le
   \left(\sum_u w_U(u)|A_{y,R,u}|^4\right)^{1/2}
   \left(\sum_u w_U(u)|S_{\overline{\psi_u^0}}(N)|^4\right)^{1/2}\\
 &\ll_\epsilon
       U^{[1+\mathcal E_{.51}(2\rho)]/2+\epsilon}
                  (1+|\mathbf v|)^A\,(\text{profile seminorms})^2 .
\end{split}                                                   \tag{27}
\]

The fixed Fourier weighted $L^1$ norms and (26) absorb those frequency
and seminorm factors. The bound applies to the conductor sector by
positivity; no new large-sieve inequality for row-selected coefficients is
being asserted.

The exact dual prefactor in (24) is essential. For $B>1/2$,

\[
 \sup_{L_0>0}
   \sum_{N\ge1\ {\rm dyadic}}
       \sqrt{N/L_0}\,(1+N/L_0)^{-B}<\infty.                 \tag{28}
\]

For $N\le L_0$ the lower annuli sum geometrically; for $N>L_0$
rapid decay does the same. If $L_0<1$ every term belongs to the
second range, and their total is $O(L_0^{B-1/2})$. A spurious
constant contribution at every small-scale dyad would lose this fact.

The source moment in (3) only claims prescribed bounded-power lengths,
so its use on the infinite dual tail needs one additional step.
Here $L_0\le U^{C_1}$ for a fixed $C_1$ depending only on the
prescribed ranges and $C_Q$; $h$ can only decrease it. Use (3)
through $N\le U^{C_1+2}$. Beyond this point use the elementary bound
$|S_{\overline{\psi_u^0}}(N)|\ll\sqrt N$ and choose the decay
order $B$ in (26) sufficiently large. That remainder has any
desired negative $U$-power, uniformly in $e,h$. This choice is
a finite external transform order, not an enlargement of the source
height range or its moment assertion.

Finally, Minkowski over (22) costs

\[
 \sum_{e\mid Q_s}(Ne)^{-1/2}\ll_\epsilon U^\epsilon,\qquad
 \sum_{\operatorname{rad}h\subset S_0}(Nh)^{-1/2}\ll_S1.
 \tag{29}
\]

The first bound follows from the elementary deleted-Euler-factor product
for $NQ_s\le U^{C_Q+O(1)}$. Its loss is allocated from the final
epsilon. The primitive phases multiplying these terms have modulus at
most one and are retained as row scalars. They do not become
row-dependent column coefficients.

Equations (22)--(29), followed by the logarithmic number of conductor
sectors, prove the general dyadic component bound

\[
 \boxed{\quad
   \sum_u w_U(u)|M_{u,R}|^2
   \ll_\epsilon
     U^{[1+\mathcal E_{.51}(2\rho)]/2+\epsilon}
                    (1+|t|)^A p_J(W)^2.
 \quad}                                                     \tag{30}
\]

For the low selector in (9), $R\ll U^{13/20}$. Use (17) in
(30) and Minkowski over its smooth dyads. Since
$(1+E_*)/2=\Gamma_0$, this proves (2).

All final finite profile and height orders are selected before a consumer
chooses its small allowed polynomial height. The pointwise input handles
each actual total norm frequency. The separation and transform arguments
use common profiles and finite weighted Fourier norms. This includes the
source's finite-dimensional smooth detector-profile families: applying
the same estimates to the finitely many parameter derivatives and then
the source Sobolev inequality permits its rowwise choice of scale, norm
height, and profile parameter at a fixed polynomial cost. It does not
permit arbitrary rowwise coefficients or arbitrary unrelated tests.

## 6. Inverse powers and the separate adjustable-floor consequence

This section is not needed for the fixed-cutoff theorem (2). It records
a useful consequence of the same bin mechanism, including a precise
explanation of the floor modification.

For a fixed integer $j\ge1$ let $\mu_j=\mu_E^{*j}$ and put

\[
 A_{j,u}(R;V)=R^{-1/2}\sum_n\mu_j(n)\psi_u(n)V(Nn/R).
 \tag{31}
\]

**Theorem 2.** For any fixed $p\ge1$, prescribed bounded
$\rho\ge0$, and $\epsilon>0$, the re-run of the source detector
with an adjustable fixed floor described below gives

\[
 \sum_u w_U(u)|A_{j,u}(U^\rho;V)|^p
   \ll_\epsilon U^{\mathcal E(p\rho/2)+\epsilon}
                 (1+|t|)^A p_J(V)^p.                       \tag{32}
\]

In particular the moment has the row-volume bound
$U^{1+\epsilon}$ when

\[
                         \rho\le \frac4{3p}.                \tag{33}
\]

The constants may depend on $j,p$ and the prescribed ranges.
The same conclusion applies to the smooth outer polynomial (12), by
the proof of Lemma 1. Thus the reflected component has row-volume
second moment for $R\le U^{1/3}$. Its original natural dual,
punctures, and common-profile scope are precisely those in Sections
4--5; no primitive dual is silently replaced by a differently masked
family.

**Proof and scope of the floor modification.** The printed source uses
$51/100$. Here one re-runs its proof with
$a_\nu=1/2+\nu$, for any fixed $\nu>0$. This is a deduction
from its proof and original moments, not a citation of a printed theorem
already uniform as $\nu\downarrow0$.

The buffered maxima and pigeonhole rounding are unchanged, with constants
allowed to depend on $\nu$. The zero-free disks stay to the right
of $1/2+\nu$, so their local logarithmic argument applies verbatim.
Above the floor, the same smooth zero detector gives simultaneous
witnesses of lengths $r,m$ satisfying
$r\le t+o(1)$, $r+m\ge t-o(1)$ and the lower bounds
$|M_r|^2\gg U^{\delta r-o(1)}$,
$|S_m|^2\gg U^{\delta m-o(1)}$.
Saturation uses $\delta\ge2\nu$ in place of $1/50$;
choose its preliminary losses smaller than $\nu$ times the
requested final loss. The external detector contour at
$\operatorname{Re}z=-1/4$ still has
$\operatorname{Re}(\rho+z)\ge1/4+\nu>0$. The source error is
$U^{-3+t(5/4-\operatorname{Re}\rho)+o(1)}T_1^2$.
For $t\le3/2$ its exponent before the fixed height factor is at most
$-15/8$. With $T_1\le U^{1/100}$ the full error is therefore at most
$U^{-371/200+o(1)}=o(1)$. Thus the fixed height factor is retained,
and this contour move causes no new near-half-plane error in the
floor re-run.

For completeness, the density calculation needs only the original
unmarked inverse moment
$U^{\max(1,(1+5r)/6)+\epsilon}$ and (3).
When $r\le1$, Hölder bounds
$\sum|M_rS_m|^{4/3}\ll U^{1+\epsilon}$, hence the short-witness
count is at most $U^{1-2\delta t/3+\epsilon}$.
For $r\ge1$ and $\delta\le5/6$ the inverse witness alone
gives at most $U^{1/6+(5/6-\delta)t+\epsilon}$. Their crossing
is $t=5/(5-2\delta)$ and yields exactly (10).
For $\delta\ge5/6$ choose $t=3/2$; both sides give
$U^{1-\delta+\epsilon}$. Dyadic meshes, common-character
labels, and Sobolev losses are allocated exactly as in the source before
choosing its small polynomial height. No new marked moment is needed.

On a bin the Dirichlet series in (31) is
$L_{\rm orig}(s,\psi_u)^{-j}$. Raise the local reciprocal estimate
to this fixed power and use the same truncated contour. On the absolute
line its coefficients are bounded by a fixed divisor function, so
external tails require only a larger fixed derivative order. Thus
$|A_{j,u}|^p\ll U^{(p\rho/2)\delta+\epsilon}$.
The bottom bin contributes
$U^{1+p\rho\nu+\epsilon_1}$. Choose the fixed $\nu$
sufficiently small after the desired final epsilon and bounded length
range, then choose the remaining small losses and orders. The above-floor
maximum is (15), proving (32).

The row-volume conclusion (33) itself does not require the $7/8$
cap: throughout the uncapped range,

\[
 \frac{15-16\delta}{15-6\delta}
       \le1-\frac{2\delta}{3}\quad(0\le\delta\le5/6),
 \qquad
 1-\delta\le1-\frac{2\delta}{3}\quad(5/6\le\delta\le1).
 \tag{34}
\]

Hence any slope $p\rho/2\le2/3$ leaves the above-floor exponent
at most one. The same smooth-factor proof gives the corresponding
statement for (12), and (27)--(29) give its reflected row-volume
component for $\rho\le1/3$. QED.

## 7. What this component forces at the detector lengths

The inherited complete inverse exponent is
$e_0(r)=(1+5r)/6$ for $r\ge1$. At every
$r\ge29/25$,

\[
 e_0(r)-\Gamma_0
   \ge\frac{17}{15}-\Gamma_0>\frac1{1000}.                  \tag{35}
\]

The last comparison is exact. It is equivalent to
$\sqrt{195}>3489/250$, and

\[
              195-(3489/250)^2=\frac{14379}{62500}>0.       \tag{36}
\]

If a compatible detected row has
$|M_u(U^r)|^2\gg U^{\delta r-\epsilon}$ and its high component
is smaller than half this witness in absolute value, then its low
component has at least half the witness. The source's common-profile
and Sobolev calculus, followed by (2), therefore bounds the number of
such rows by

\[
                     U^{\Gamma_0-\delta r+\epsilon}.
 \tag{37}
\]

All other detected rows have a large coherent witness in
$M_u^{\rm hi}$ from (9). Thus (35) improves the count of the
low-supplied witnesses by at least $1/1000$ compared with the old
inverse count in this range. It does not improve the count of the
remaining high witnesses. Prime amplitudes or numerator labels, if
present, remain fixed to the source-compatible character relations; this
argument moves no amplitude from one presentation to another.

For comparison with the presently critical scalar class, Liu's
[arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1),
Lemma 14.9 and Sections 14--15, give the relevant values

\[
\begin{split}
 \kappa_c&=0.749773294079928261889\ldots,\\
 \delta_c&=0.469344858698143067494\ldots,\qquad x_c=1/2,\\
 r_c&=1.163953576509010956315\ldots,\\
 R_c&=0.590332353526355793593\ldots .
\end{split}                                                   \tag{38}
\]

These are used here as scalar comparison data; Liu's Part II field
premises are not being transferred to the Eisenstein family.
They satisfy $R_c+\delta_cr_c=e_0(r_c)$. Therefore the count
in (37) at this class is smaller by

\[
 e_0(r_c)-\Gamma_0=0.005667987718999325243\ldots .            \tag{39}
\]

The exact checker verifies the bracket
$29/25<r_c<117/100$ from rational enclosures of the source's
quartic and critical quadratic. The decimal values in (38)--(39) are
illustrative, not the proof of the margin in (35).

More generally, on $1\le r\le58/49$, the contact of the optimistic
floor-free component envelope with $e_0(r)$ occurs at

\[
                 \rho_*(r)=\frac{(1+\sqrt{r-1})^2}{3}.
 \tag{40}
\]

This follows by substituting the interior branch of (15) into
$(1+\mathcal E(2\rho))/2=e_0(r)$. At (38),
$\rho_*(r_c)=0.657925734336014348\ldots$; the rational cutoff
$13/20$ leaves a definite margin. Neither (40) nor this numerical
comparison is used to claim that the complementary range is controlled.

The remaining arithmetic target is consequently concrete: improve the
second moment of the single coherent high term in (9) on the needed
short interval of inverse lengths, with the same masks, row family,
height orders and profiles. `CONDITIONAL_CONSUMER.md` states and
certifies one sufficient tail hypothesis. That hypothesis is still open.
The present component estimate supplies its complementary low term.

## 8. Verification boundary

`check_inverse_power_component.py` checks the exact convolution identity
on finite multiplicative examples, its repeated-prime negative control,
the normalized reflection prefactors, the rational density envelope and
its contacts, the exact radical margin, and a rational enclosure placing
the critical scalar length in the stated interval. Its predicates remain
active under `python -O`.

These finite checks do not prove the imported cap, polynomial-height
density, ordinary fourth moment, Fourier separation, or the functional
equation. Those are the stated premises and the analytic arguments above.
The new estimate is a coherent component theorem within that source
scope; it is not a proof of RH or an unconditional improved zero-free
region.
