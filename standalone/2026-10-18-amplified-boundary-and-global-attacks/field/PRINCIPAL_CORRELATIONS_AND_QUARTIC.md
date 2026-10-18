# Principal correlations and a complete quartic Möbius codec

**Scope.** This note records two principal-target operations and a quartic
alternative tested during the present attack. The finite identities and
the explicitly conditional linear-algebra statement below are proved here
from the stated classical inputs. No new analytic bound is claimed in
this note. In particular, none of the obstructions rules out a different
coupled kernel or a compensated Rankin--Selberg construction.

## 1. Coupling the Mellin variables retains the target, but adds a jet

Use the original Eisenstein-field integral's Mellin variables $s,w,z$.
Its scale-dependent factor is

$$
X^{1/2-z}Z^{s+z-1}Y^{w-1}.
\tag{1.1}
$$

Let $I_\Pi$ denote an absolutely convergent initial-line integral with
**fixed** finite arithmetic probe data $\Pi$. Simultaneous dilation of
$X,Y,Z$ multiplies (1.1) by $t^{s+w-3/2}$. Consequently

$$
\int_0^1 t^{1/2}I_\Pi(tX,tY,tZ)\,\frac{dt}{t}
\quad\hbox{inserts}\quad \frac1{s+w-1},
\qquad \Re(s+w)>1.
\tag{1.2}
$$

This follows by Fubini on the absolute initial lines. If the original
construction chooses primes from a window depending on $Z$, those primes
and their coefficients must be frozen in (1.2); replacing them by the
window associated to $tZ$ would change the integrand. The old low-side
bound is therefore not automatically uniform for this new dilation
integral. At the principal $w=1$ residue the new multiplier is $1/s$,
which does retain that target for $0<\Re s<1$.

There is an exact correlation available for the principal target. Write
$L_u(s)=L_F^S(s,\overline{\chi_u})$. Its incomplete functional equation
has the form

$$
L_F^S(1-s,\chi_u)=D_u(s)L_u(s),
\tag{1.3}
$$

where $D_u$ contains the root number, conductor, gamma factors and the
finite Euler corrections; it is nonzero and holomorphic inside the
critical strip. For $\tau=s+w-1$,

$$
\frac{L_F^S(w,\chi_u)}{L_u(s)}
 =D_u(s-\tau)\frac{L_u(s-\tau)}{L_u(s)}.
\tag{1.4}
$$

Thus the ratio cancels on $\tau=0$ as a **meromorphic identity**. This
does not assign a numerical value to $0/0$ at a zero of $L_u$. A finite
twist in a particular row must have its actual functional-equation
partner; different twists cannot be identified merely because the
external target is principal.

The raw local Euler factor already has a pole along this same diagonal.
The repository's pinned resonant-jet calculation [R2] gives

$$
H_0(s,w,z)=\zeta_F^S(s+w)K_0(s,w,z).
\tag{1.5}
$$

For example, its stated normal-convergence region includes
$\Re s,\Re w>0$, $\Re z>1$, $2\Re s+\Re w>1$.
The following computation applies to any complete row factor
$H_u=\zeta_F^S(s+w)K_u$ wherever its finite corrections and $K_u$ are
holomorphic. It does not presume an unproved uniform bound for $K_u$
on a proposed lower contour.

Write, locally at $\tau=0$,

$$
\zeta_F^S(1+\tau)=\frac{r_S}{\tau}+c_S+O(\tau),\qquad
K_u(s,1-s+\tau,z)=k_0+\tau k_1+O(\tau^2).
$$

If the remaining holomorphic test factor is
$T(s,\tau)=T_0+\tau T_1+O(\tau^2)$, the coefficient of $\tau^{-1}$ in

$$
\frac{T(s,\tau)}{\tau}\,
\zeta_F^S(1+\tau)K_u(s,1-s+\tau,z)
D_u(s-\tau)\frac{L_u(s-\tau)}{L_u(s)}
$$

is exactly

$$
\boxed{
T_0D_u(c_Sk_0+r_Sk_1)
-r_ST_0D'_uk_0
-r_ST_0D_uk_0\frac{L'_u}{L_u}(s)
+r_ST_1D_uk_0.}
\tag{1.6}
$$

To prove it, multiply the four Taylor expansions and use
$L_u(s-\tau)/L_u(s)=1-\tau L'_u(s)/L_u(s)+O(\tau^2)$
away from its zeros, then continue meromorphically. The extra Cauchy
factor makes the existing simple diagonal pole double. Its residue
therefore contains the logarithmic derivative, with coefficient
$-r_ST_0D_uk_0$; it cannot be discarded without proving that the
coefficient vanishes or controlling the resulting term. The earlier
repository jet result is explicitly credited, rather than reintroduced
as a new zero-detection theorem.

There is also a scale cost. Writing the conductor part of $D_u(s-\tau)$
as $Q_u^{s-\tau-1/2}$, its product with $Y^{w-1}$ contains

$$
(Y/Q_u)^\tau.
\tag{1.7}
$$

Moving the transverse contour to $\Re\tau=-\varepsilon$ costs
$(Q_u/Y)^\varepsilon$. In the present scales
$U=Z^d$, $Y=Z^{\ell_y}$, the binding range includes conductors of
order $U$ with $d=h$ and $h-\ell_y=2\ell>0$.
Thus reflection does not make that transverse integral decay for free.

**Remaining estimate for this construction.** One needs a complete
signed estimate for the transverse row integral, its residue (1.6),
all finite prime corrections and contour tails, together with a
low-side bound uniform under the frozen-data dilation (1.2). The
diagonal identity alone supplies none of these bounds. It is still
possible that another coupled kernel controls the complete combination.

## 2. A precise limitation of homogeneous cross-scale cancellation

The exceptional sixth-power count in the original Gram estimate [R1]
has diagonal scale

$$
\frac QY\left(\frac{Y^2}{Q}\right)^{1/6}
   =Q^{5/6}Y^{-2/3},\qquad Q=XY.
\tag{2.1}
$$

**Conditional linear-algebra statement.** Suppose, in addition to
(2.1), that the leading cross-scale Gram term at fixed $Q,Z$ were
a nonzero rank-one kernel

$$
C Q^{5/6}(Y_1Y_2)^{-1/3},\qquad C>0.
\tag{2.2}
$$

Then a finite signed probe combination annihilates this term precisely
when $\sum_j w_jY_j^{-1/3}=0$. But its principal Mellin coefficient is

$$
X^{1/3}Z^{s-5/6}
  =Q^{1/3}Y^{-1/3}Z^{s-5/6}.
\tag{2.3}
$$

The same condition annihilates (2.3) for every $s$. In particular,
$A(Y)-c^{1/3}A(cY)$ removes both terms under (2.2).
This proves the conditional statement directly by factoring the
rank-one quadratic form and the linear target.

**The premise (2.2) has not been proved.** A diagonal upper bound does
not establish it. This observation only prevents the proposed
homogeneous rank-one cancellation, even in its favorable hypothetical
form, from being presented as a target-preserving gain. It says nothing
against probes with a genuinely different target-to-nuisance ratio.

## 3. Quartic Gauss sums encode the full Gaussian-field Möbius function

Let $F=\mathbb Q(i)$, $\lambda=1+i$, and let $S=\{(\lambda)\}$.
Each integral ideal prime to $S$ has a unique primary generator
$c\equiv1\pmod{\lambda^3}$. All sums in this section use these
generators, including $c=1$; there is no extra unit multiplicity.
Adopt the DDHL normalization [R3]

$$
g_4(c)=\sum_{d\bmod c}\left(\frac dc\right)_4
 \exp\!\left(2\pi i\left(\frac dc+\frac{\overline d}{\overline c}\right)\right),
\qquad
\widetilde g_4(c)=\frac{g_4(c)}{\sqrt{N(c)}}.
$$

Here the symbols in the exponential are ordinary quotients, while
the parenthesized symbol outside it is the quartic residue symbol.
Set $g_4(1)=1$ and

$$
\epsilon(c)=\left(\frac{-1}{c}\right)_4\frac{c}{|c|}.
$$

**Proposition.** For every primary $c$,

$$
\boxed{\widetilde g_4(c)^2=\mu_F(c)\epsilon(c).}
\tag{3.1}
$$

The multiplier $\epsilon$ is multiplicative of modulus one; its
angular factor must be retained by any analytic implementation.

**Proof.** DDHL (3.11) gives, for a degree-one primary prime $\pi$,

$$
\widetilde g_4(\pi)^2
  =-\left(\frac{-1}{\pi}\right)_4\frac{\pi}{|\pi|}.
$$

For an inert rational prime $p\equiv3\pmod4$, its primary generator
is $\pi=-p$. DDHL (3.8) gives $\widetilde g_4(\pi)=1$.
Furthermore $(-1/\pi)_4=1$, since $(p^2-1)/4$ is even, and
$\pi/|\pi|=-1$. Thus the same prime identity holds at degree two.
These primes must not be discarded in a reciprocal-zeta identity.

For coprime primary $a,b$, the CRT factor in DDHL (3.5) is
$(a/b)_4(b/a)_4$. By quartic reciprocity (3.2) it equals
$(-1)^{C(a,b)}(b/a)_4^2$, so its square is $1$.
Consequently the square of the normalized Gauss sum is multiplicative
on squarefree primary moduli, and the prime identities prove (3.1)
there. DDHL (3.7) gives $g_4(1,\pi^e)=0$ for every $e\ge2$.
The CRT relation then makes both sides of (3.1) zero at every
nonsquarefree modulus. At $c=1$ both sides equal $1$. $\square$

In particular the exact signed diagonal is

$$
\boxed{
\mathscr D(s)=
\sum_{c\ {\rm primary}}
\frac{\widetilde g_4(c)^2\epsilon(c)^{-1}}{N(c)^s}
=\frac1{\zeta_F^S(s)},\qquad \Re s>1.}
\tag{3.2}
$$

The missing ramified factor is explicit:
$\zeta_F^S(s)=(1-2^{-s})\zeta_F(s)$. A theorem for the full
Gaussian-field target would transfer to ordinary zeta through
$\zeta_F(s)=\zeta(s)L(s,\chi_{-4})$; the second factor is entire.
Equation (3.2) is an encoding identity, not such a theorem.

Replacing the signed square by a norm gives instead

$$
\sum_{c\ {\rm primary}}\frac{|\widetilde g_4(c)|^2}{N(c)^s}
 =\sum_c\frac{\mu_F(c)^2}{N(c)^s}
 =\frac{\zeta_F^S(s)}{\zeta_F^S(2s)},\qquad \Re s>1.
\tag{3.3}
$$

Thus a positive Rankin--Selberg norm loses exactly the Möbius signs
needed in (3.2).

## 4. The square-index pairing: what it selects and what it does not

Put $\beta_0=1$, $\beta_1=1+\lambda^3=-1+2i$ and

$$
\boldsymbol\psi(\nu)=
\begin{pmatrix}\psi^{(4)}_{\beta_0}(\nu)\\
\psi^{(4)}_{\beta_1}(\nu)\end{pmatrix},
\qquad
\psi^{(4)}_\beta(\nu)
=\operatorname*{Res}_{v=5/4}\psi^{(4)}_\beta(v,\nu,0).
$$

Suzuki's square-index identity in the DDHL sign convention, (4.38),
gives for squarefree primary $m$

$$
\boldsymbol\psi(m^2)
 =\frac{\overline{\widetilde g_4(m)}}{N(m)^{1/4}}\,
 R(m)\boldsymbol\psi(1),\qquad
R(m)=
\begin{cases}
I,&m\equiv1\pmod4,\\
\begin{pmatrix}0&1\\-1&0\end{pmatrix},
 &m\equiv\beta_1\pmod4.
\end{cases}
\tag{4.1}
$$

The minus sign follows from $N(\beta_1)=5$. No nonvanishing or
normalization of $\boldsymbol\psi(1)$ is presumed here. The actual
theta coefficients also have a fixed cusp-volume normalization and
sign: DDHL (4.35) gives
$\mathcal V\tau_{i_1}=\psi_{\beta_0}$ and
$\mathcal V\tau_{i_2}=-\psi_{\beta_1}$. These factors cannot be
discarded when making an automorphic vector from (4.1).

At a common cusp, after choosing compatible additive lattices, write
the complete Fourier expansions, with zero modes included, as

$$
\theta_4(z,y)=\sum_\nu A_\nu(y)e_\Lambda(\nu z),\qquad
\theta_2(z,y)=\sum_m B_m(y)e_\Lambda(m^2z).
$$

For the usual one-dimensional quadratic Weil theta, this square
support is the defining additive Fourier expansion; multiplicities
from $m$ and $-m$ remain in the sum. Torus orthogonality gives exactly

$$
\operatorname{CT}(\theta_4\overline{\theta_2})
  =\sum_m A_{m^2}(y)\overline{B_m(y)}.
\tag{4.2}
$$

So the proposed pairing really does select square indices at a cusp.
After the fixed Whittaker normalization, (4.1) shows that its
squarefree part contains **one** conjugated quartic Gauss sum,
not its square. Mellin integration of the radial factors does not
change that coefficient degree.

There are two further exact constraints.

First, in a common fourfold cover use the convention that a genuine
quartic theta has central weight $1$ on $\mu_4$. The quadratic theta
pulled back along $\zeta\mapsto\zeta^2$ has weight $2$. Then
$\theta_4\overline{\theta_2}$ has weight $-1$, so it does not define
an untwisted scalar period on the base quotient. Its integral over
the full cover is zero whenever integration, or regularization,
is invariant under the central group. Conjugating the quartic
convention changes the odd weight but not this mismatch.

The product $\theta_4^2\overline{\theta_2}$ does have weight zero.
Its constant term, however, is

$$
\operatorname{CT}(\theta_4^2\overline{\theta_2})
 =\sum_m\sum_{\nu_1+\nu_2=m^2}
 A_{\nu_1}(y)A_{\nu_2}(y)\overline{B_m(y)}.
\tag{4.3}
$$

This is an additive convolution. It does not impose
$\nu_1=\nu_2=m^2$, and hence is not the signed diagonal in (3.2).

Second, (4.2) includes nonsquarefree $m$. They do not automatically
vanish: DDHL (4.36) gives
$\boldsymbol\psi(\pi^4)=\boldsymbol\psi(1)$ for a primary prime
$\pi$, whereas $\mu_F(\pi^2)=0$. Inserting a squarefree mask into
the coefficients would itself require an automorphic implementation
or a complete decomposition with controlled correction terms.

### A compensated period remains a real possibility

The central-character mismatch is **not** an obstruction to every
Rankin--Selberg construction. An Eisenstein series of genuine
central weight $1$ makes

$$
E_4\,\theta_4\,\overline{\theta_2}
\tag{4.4}
$$

have total central weight zero. Appropriate sections and compatible
archimedean types could therefore support an unfolded square-index
period. One must still establish its convergence or regularization,
all cusp terms and its scattering equation. No such complete
period identity is asserted here. In particular, central
compatibility alone does not establish it.

Even if (4.4) unfolds as hoped, the basic square-index coefficient
is the linear one in (4.1). It has not yet produced the second
Gauss factor required by (3.2).

There is also a specific denominator to keep in a proposed
Eisenstein transform. In DDHL (4.23)--(4.27), the completed
coefficient is

$$
\widehat\psi^{(4)}_{i1}(v,\nu,\ell)
 =G_\infty(v,\ell)\,
 \zeta_{F,\lambda}(4v-3,\ell)
 \psi^{(4)}_{i1}(v,\nu,\ell),
\tag{4.5}
$$

and its reflection includes

$$
N(\nu)^{1-v}\left(\frac{\overline\nu}{|\nu|}\right)^\ell
\sum_{j=1}^{24}A_{ji}(2^{-v},\ell)
\widehat\psi^{(4)}_{j1}(2-v,\nu,-\ell).
\tag{4.6}
$$

The constant-term scattering entries involve, up to stated local
rational factors,
$\zeta_{F,\lambda}(4v-4,\ell)/\zeta_{F,\lambda}(4v-3,\ell)$.
For $\nu=m^2$ the conductor factor in (4.6) is
$N(m)^{2(1-v)}$. Holomorphy of the completed expression cannot be
turned into a bound for the uncompleted one by silently dividing
by zeta in a region where its nonvanishing is the question.
Indeed DDHL's proof of (4.28) divides only on
$\Re v>1+\varepsilon$, where the Euler product licenses that step.

Known mixed-cover integrals do not settle this particular adapter.
For example Friedberg--Ginzburg [R4] construct a fourfold/twofold
integral on higher-rank groups, with compatible covering data, over
a field containing $\mu_8$ and with a genuine cuspidal input.
Those hypotheses and Fourier coefficients do not allow its direct
substitution for (4.4) with the noncuspidal Gaussian-field
quadratic theta. This is a concrete distinction between the
available theorem and the proposed period, not a general
impossibility assertion.

## 5. The exact missing signed square-index adapter

There is a normalization-free way to specify the desired coefficient
object. Write $v_0=\boldsymbol\psi(1)$. Equation (4.1) implies on
squarefree primary $m$ that

$$
N(m)^{1/4}R(m)^{-1}\overline{\boldsymbol\psi(m^2)}
  =\widetilde g_4(m)\,\overline{v_0}.
$$

Consequently the **bilinear, not Hermitian**, tensor diagonal obeys

$$
\boxed{
\sum_{\substack{m\ {\rm primary}\\m\ {\rm squarefree}}}
\frac{\epsilon(m)^{-1}N(m)^{1/2}}{N(m)^s}
\left(R(m)^{-1}\overline{\boldsymbol\psi(m^2)}\right)^{\otimes2}
=\frac{\overline{v_0}^{\otimes2}}{\zeta_F^S(s)},
\qquad \Re s>1.}
\tag{5.1}
$$

This follows coefficient by coefficient from (3.1); absolute
convergence is immediate. If a nonzero component of $v_0$ is used
to normalize a scalar detector, its nonvanishing must be supplied.
Formula (3.2) itself has no such normalization issue.

The concrete missing construction is an automorphic kernel or
period that realizes (5.1), or directly (3.2), with its two
**equal** square indices, residue-class matrices, angular twist
and nonsquarefree corrections, and has a proved reflection plus
a complete uniform estimate that saves a binding exponent.
Equations (4.2) and (4.4) only address linear selection;
(4.3) imposes a different index relation; a Hermitian norm gives
(3.3). None is that signed diagonal adapter.

This is where dropping the all-number-fields requirement leaves
a genuine opening: the quartic encoding needs only
$\mathbb Q(i)$ and uses the square of a quartic Gauss sum. The
unproved part is the transformation and estimate for this
specific signed coefficient object, not the Möbius encoding
or a claimed shortage of generality in an existing theorem.

## Pinned sources and attribution

- **[R1]** OpenAI, *The Quasi-Riemann Hypothesis*, original source
  pinned at commit
  [adc7f1241b42e322a6451854ab7e4b4c146bf78a](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
  The displayed Mellin integral and the exceptional sixth-power
  Gram count are the inputs used in Sections 1--2. No claim is
  made here to independently prove its analytic framework.
- **[R2]** Repository resonant transverse jet,
  [PROOF.md at edbc27b61208ccc7ee1fa99fa3f4e861f5a03452](https://github.com/GettysburgResearch/riemann/blob/edbc27b61208ccc7ee1fa99fa3f4e861f5a03452/standalone/2026-10-18-resonant-transverse-jet/PROOF.md).
  The raw factorization (1.5) and its stated convergence domain
  are inherited from that component calculation.
- **[R3]** C. David, A. Dunn, A. Hamieh, H. Lin,
  [*Quartic Gauss sums over primes and metaplectic theta functions*,
  arXiv:2306.11875v2](https://arxiv.org/html/2306.11875v2),
  10 May 2025; equations (3.2), (3.5), (3.7)--(3.12),
  (4.23)--(4.28), (4.34)--(4.38).
  These classical identities are imported, not claimed as new.
- **[R4]** S. Friedberg, D. Ginzburg,
  [*Metaplectic Theta Functions and Global Integrals*,
  arXiv:1403.3929v1](https://arxiv.org/pdf/1403.3929v1),
  Sections 2--5, especially their covering compatibility
  condition (3) and unfolded coefficient series (8).
