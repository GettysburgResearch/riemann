# A conjugate pair of local Kummer transforms gives a stable arithmetic frame

9 November 2026. **Proved finite-field and tensor-product statements.**
These statements do not prove a new zero-free region. They provide an exact,
quantitatively invertible local adapter for the coupled kernel in the sibling
`coupled/` packet. Applying the adapter to a native Riemann source still requires
matching that complete source and estimating its actual transformed outputs.

The useful distinction is that this operator mixes an additive Fourier kernel
with multiplicative channels. It is not a scalar dilation of a Mellin profile.
Two conjugate sextic channels repair the weak nontrivial character channel of
either individual transform. The distinction survives tensoring with a
subpower loss in a squarefree conductor. All constant-coordinate and nonunit
sectors are identified below.

## 1. Local conventions, including every zero

Let F be a finite field of odd cardinality q>3, let e be a nontrivial additive
character, and let chi be a multiplicative character with chi != conjugate(chi).
A character of exact order six is the intended case. Extend **every**
multiplicative character, including the trivial character, by zero at 0.
Write U=F^times, and use the counting inner product on H=complex-valued
functions on U. The use of a probability inner product instead would change
none of the operator identities.

Set

\[
 S_\chi(z)=\sum_{x\in F}\chi(x)\overline{\chi(x-1)}e(zx),
 \qquad K_\chi(z)=q^{-1/2}S_\chi(z),
 \qquad B_\chi(h,t)=q^{-1}S_\chi(ht),\quad h,t\in U. \tag{1}
\]

Thus `(B_chi f)(h)=sum_(t in U) B_chi(h,t) f(t)`. In particular this is
the **product** kernel ht, not the ratio kernel h/t. Switching that convention
interchanges the labels chi and conjugate(chi) in the one-channel assertion.

For a multiplicative character psi on U, let P_psi be its orthogonal projector:

\[
 (P_\psi f)(t)=\frac{\psi(t)}{q-1}
                   \sum_{u\in U}\overline{\psi(u)}f(u). \tag{2}
\]

Denote P_1 by P and I-P by Q. The two zeros x=0,1 in (1) are never filled
in. The trivial vector in H is the constant **on units**, not a function
that has been assigned value one at a nonunit.

## 2. Exact singular values of one channel

### Theorem 1

The complete one-channel Gram operator is

\[
 B_\chi^*B_\chi
   =I-(1-q^{-2})P-(1-q^{-1})P_\chi. \tag{3}
\]

Also B_chi P=P B_chi=q^(-1)P. Consequently, after centering,

\[
 C_\chi:=B_\chi-q^{-1}P,
 \qquad C_\chi^*C_\chi
   =Q-(1-q^{-1})P_\chi. \tag{4}
\]

The singular values of B_chi are 1/q on constants, 1/sqrt(q) on chi,
and 1 on every other multiplicative character. Centering kills only the
constant channel; its exceptional nontrivial channel remains suppressed
by q^(-1/2).

### Proof by multiplicative Fourier analysis

The change of variable x/(x-1) shows S_chi(0)=-1. Additive orthogonality
then gives sum_(z in U) S_chi(z)=1. This proves the assertions involving P.

Put g(eta)=sum_(x in U) eta(x)e(x), and
J(eta,xi)=sum_x eta(x)xi(1-x), with the zero extensions already fixed.
For nontrivial eta, |g(eta)|=sqrt(q). This follows by expanding its squared
modulus and applying additive orthogonality. For nontrivial eta,xi,eta*xi,
the substitution (x,y)=(uv,u(1-v)) proves
g(eta)g(xi)=g(eta*xi)J(eta,xi), hence |J(eta,xi)|=sqrt(q).
If xi is nontrivial, J(1,xi)=-1.

For a nontrivial character psi,

\[
 \sum_{z\in U}\psi(z)S_\chi(z)
   =g(\psi)\overline{\chi(-1)}
                    J(\chi\overline\psi,\overline\chi). \tag{5}
\]

This has absolute value sqrt(q) when psi=chi, and q otherwise.
For psi=1 the sum is 1. Acting on psi with the product kernel in (1)
returns conjugate(psi), multiplied by q^(-1) times the left side of (5).
The images of distinct character vectors are therefore orthogonal.
Their squared norms give (3), and subtracting q^(-1)P gives (4). QED.

Equivalently the exact entrywise identity is

\[
 \sum_{t\in U}\overline{S_\chi(th)}S_\chi(tk)
 =q^2\mathbf1_{h=k}-q\chi(h/k)-(q+1). \tag{6}
\]

The sibling checker independently evaluates (1) and (6) in exact cyclotomic
arithmetic, including nonprime finite fields and both sextic orientations.

## 3. The conjugate pair repairs the exceptional character

Define the two-output analysis map

\[
 A_\chi f=2^{-1/2}(C_\chi f,C_{\overline\chi}f),
 \qquad g_q=\frac{1+q^{-1}}2. \tag{7}
\]

### Theorem 2: uniform local frame

For chi != conjugate(chi),

\[
 G_\chi:=A_\chi^*A_\chi
 =Q-\frac{1-q^{-1}}2(P_\chi+P_{\overline\chi}),\qquad
 g_q Q\le G_\chi\le Q. \tag{8}
\]

In particular A_chi kills constants exactly, and preserves every mean-zero
source with

\[
 g_q\|Qf\|^2
 \le\frac{\|C_\chi f\|^2+\|C_{\overline\chi}f\|^2}{2}
 \le\|Qf\|^2. \tag{9}
\]

The lower constant is sharp: it is attained on either chi or its conjugate.
On their orthogonal complement inside QH, equality holds in the upper bound.

An explicit decoder is

\[
 D_\chi=R_\chi A_\chi^*,\qquad
 R_\chi=Q+\frac{q-1}{q+1}(P_\chi+P_{\overline\chi}),
 \qquad D_\chi A_\chi=Q,\quad \|D_\chi\|=g_q^{-1/2}<\sqrt2. \tag{10}
\]

**Proof.** Average (4) for chi and conjugate(chi). These two character
projectors are distinct and orthogonal by the hypothesis. The three
nonzero eigenspaces have eigenvalues g_q,g_q,1. Formula (10) is the
inverse on QH followed by the adjoint analysis map. QED.

This is a positive operator statement for arbitrary complex local source
vectors. It does not replace a specified source by an arbitrary vector in
an application: its two actual outputs and the lost constant component
must all remain attached to that same source.

**Why a quadratic character is different.** If chi=conjugate(chi), the two
channels coincide; the exceptional eigenvalue in (8) is 1/q, not g_q.
The claimed uniform repair would be false. Nonreality, supplied here by
sextic characters, is a necessary hypothesis of this two-channel adapter.

In a native sextic physical expression, a local exponent three can produce
a quadratic character. Such a sector is therefore outside the uniform
two-channel repair and must retain its exact 1/q squared gain or receive
another argument. Replacing it by a new nonreal auxiliary character would
require a separate source-preserving identity; it is not an automatic
application of this theorem.

### Corollary: any two distinct nontrivial characters suffice

If chi and kappa are distinct nontrivial characters, the same argument gives

\[
 \frac{C_\chi^*C_\chi+C_\kappa^*C_\kappa}{2}
 =Q-\frac{1-q^{-1}}2(P_\chi+P_\kappa), \tag{10a}
\]

with exactly the same lower gain g_q and decoder, replacing P_bar(chi)
by P_kappa. Thus a quadratic native character can be supplemented by a
distinct cubic or sextic character on the good fields in question. This
adds a genuinely new transformed output of the **same source**, which
requires its own bound. It does not license replacing the original
quadratic phase or assuming its auxiliary output is already controlled.
All tensor and sector statements below also hold for these distinct pairs.

## 4. Squarefree-conductor tensoring and its exact loss

Let a squarefree ideal conductor be a product of r distinct good prime
ideals p. Put q_p=Np, assume each local field admits a nonreal chi_p,
and write

\[
 \mathcal H=\bigotimes_{p\mid\mathfrak q}\mathbb C[F_{q_p}^\times],
 \quad P_{\rm prim}=\bigotimes_{p\mid\mathfrak q}Q_p,
 \quad \gamma(\mathfrak q)=\prod_{p\mid\mathfrak q}\frac{1+q_p^{-1}}2.
 \tag{11}
\]

The label `prim` in (11) means orthogonality to constants at **each** local
coordinate. It is a tensor-space label, not a claim about the primitive
conductor of an arbitrary original arithmetic coefficient.

For epsilon in {+,-}^r let
C_epsilon=tensor_p C_(chi_p^(epsilon_p)). The tensor version of (9) is

\[
 \gamma(\mathfrak q)\|P_{\rm prim}f\|^2
 \le 2^{-r}\sum_{\epsilon\in\{+,-\}^r}\|C_\epsilon f\|^2
 \le\|P_{\rm prim}f\|^2. \tag{12}
\]

Its exact Gram operator is tensor_p G_(chi_p). Its decoder is the tensor
of (10) and has norm gamma(q)^(-1/2)<=2^(r/2). The 2^r transformed
channels cannot see a vector that is constant in even one coordinate.
That is an exact kernel of the construction, not an allowed deletion.

### Restoring all the missing constant-coordinate sectors

Adjoin P_p as a third local output:

\[
 \widetilde A_p f=(P_p f,\,C_{\chi_p}f/\sqrt2,
                              C_{\overline\chi_p}f/\sqrt2). \tag{13}
\]

Then

\[
 \widetilde A_p^*\widetilde A_p=P_p+G_{\chi_p},\qquad
 g_{q_p}I\le P_p+G_{\chi_p}\le I. \tag{14}
\]

The tensor of (13) has 3^r channels, including their displayed weights,
and provides **full** reconstruction with the same lower bound gamma(q).
Its inverse Gram is

\[
 \widetilde R=\bigotimes_{p\mid\mathfrak q}
 \left[I+\frac{q_p-1}{q_p+1}
                       (P_{\chi_p}+P_{\overline\chi_p})\right]. \tag{15}
\]

For explicit bookkeeping, decompose the source into the orthogonal sectors

\[
 f=\sum_{S\subseteq\{p\mid\mathfrak q\}}P_Sf,
 \qquad P_S=\bigotimes_{p\in S}Q_p\otimes\bigotimes_{p\notin S}P_p. \tag{16}
\]

The sector S uses 2^|S| sign channels, has lower gain
product_(p in S) g_(q_p), and retains the P_p outputs at its other primes.
Thus sum_S 2^|S|=3^r. Formula (16) also describes exactly what the
2^r-only bank loses.

If the intended nuisance is only the **globally constant** vector, omit
the single all-P_p output from (13). The remaining 3^r-1 channels kill
exactly P_empty= tensor_p P_p and reconstruct every other sector:

\[
 \gamma(\mathfrak q)\|(I-P_\varnothing)f\|^2
 \le\sum_{\text{all labels except all-P}}\|\widetilde A_{\text{label}}f\|^2
 \le\|(I-P_\varnothing)f\|^2. \tag{17}
\]

Their decoder is (15) followed by the adjoint retained bank. It returns
(I-P_empty)f exactly. One must not infer (17) from the 2^r bank alone.

### Conductor, masks and subpower accounting

CRT identifies the local unit spaces with the units of O/q. Opposite
sextic orientations have the same local conductor. A sign channel in
(12) therefore uses no new prime or higher conductor exponent. In a
sector S, the nontrivial multiplicative characters have conductor
dividing product_(p in S)p; primes outside S are still **natural zero
masks** on the original unit domain. In particular their redundant
radical is not erased. The product of this good primitive conductor
and its redundant radical divides q, not q^2.

Here this is a statement about the finite characters and original unit
domains, not a claim that an arbitrary global automorphic conductor has
already been computed.

For a fixed number field, for every delta>0 there is a constant C_delta
such that

\[
 3^{\omega(\mathfrak q)}\le C_\delta(N\mathfrak q)^\delta,
 \qquad \gamma(\mathfrak q)^{-1}\le2^{\omega(\mathfrak q)}.
 \tag{18}
\]

Indeed, 3<=(Np)^delta at every sufficiently large prime ideal, and there
are only finitely many smaller prime ideals. Thus the inverse loss and
channel count are subpower. `Fixed number field` and `distinct prime
ideals` matter; arbitrarily many abstract copies of F_7 do not satisfy
this arithmetic assertion.

If a later estimate is applied separately to every channel, its 3^r
summation cost must still be included. It is subpower by (18), not free.

The subpower bounds here concern **algebraic reconstruction**, not an
analytic bilinear estimate for a composite modulus. A fixed-rank
prime-field trace-function theorem and a CRT object of growing complexity
are distinct inputs. In particular, no polynomial dependence of FKMS
constants on conductor/rank is assumed here, and tensoring this frame does
not establish such dependence or a composite-modulus power saving.

## 5. Nonunit coordinates are additional sectors, not deletions

The preceding theorem is exactly on the unit domain. If the source has
coordinates at 0 in F_q, put E_0 for the orthogonal projector onto the
delta-at-zero vector, extend all unit operators by zero, and use the
four-output local bank

\[
 (E_0,\ P,\ C_\chi/\sqrt2,\ C_{\overline\chi}/\sqrt2). \tag{19}
\]

Its Gram is E_0+P+G_chi, bounded between g_q I and I on the full field.
Tensoring yields 4^r source-faithful channels; (18) holds with 4 instead
of 3. Every choice of zero-coordinate subset is retained explicitly.

The full original coupled kernel also has axes h=0 or t=0. Their exact
values are evaluated in the sibling packet. Formula (19) is source
reconstruction across zero coordinates, not a claim that those original
axes vanish or equal the unit kernel.

## 6. What this does and does not separate

The theorem provides a bounded inverse for a specific finite arithmetic
analysis map. It repairs the one-channel exceptional-character loss.
It gives a well-defined way to remove a known constant local component
without hiding other local components, subject to (12), (16), or (17)
as appropriate.

It does not show that the global theta contribution is constant in this
parameter. It does not show that the actual Mobius source has zero
projection onto any discarded sector. It does not convert a source mu
into mu*gamma_2 by multiplying a norm-preserving diagonal. Nor does it
bound any output of the analysis map. A source-specific saving must be
proved for the **same complete vector**, with all masks and sector
pairings kept, before (10) or (15) can transfer it back.

The exact usable next estimate is now a vector estimate for these
specified channels, with the scalar constant/zero-coordinate sectors
separately retained. A theorem about arbitrary coefficients is not
asserted; the present frame identity is unconditional finite algebra.

## 7. Relation to the repository

- PR #1020, frozen at `de3403df774ae0eaddfaeb9bae045ea7c9250b69`,
  `fifth-pass/PR1019_COEFFICIENT_TRANSFER_AUDIT.md`, proves that the raw
  post-Poisson inverse has coefficient gamma_2*alpha^(-1)*conjugate(G),
  without the extra mu required by its new mu*gamma_2 theorem. This note
  preserves that distinction; it supplies a different local frame.
- The same commit's `SEXTIC_ROW_PHASE_CANCELLATION.md` retains natural
  zeros even when local phases cancel. Sections 4–5 above use precisely
  that discipline.
- PR #1002, frozen at `1319373815ee408146705b25a426fba6b22ed755`,
  `PAIRED_PROBES.md`, already treats source-preserving scalar scale
  notches. The operator in (1) instead contains a nontrivial finite-field
  additive transform and its two conjugate multiplicative channels.

No novelty claim is made for general frame theory or classical
Gauss–Jacobi identities. The contribution here is their exact combined
adapter, the exceptional-channel repair, and its complete source and
conductor accounting for this proposed route.
