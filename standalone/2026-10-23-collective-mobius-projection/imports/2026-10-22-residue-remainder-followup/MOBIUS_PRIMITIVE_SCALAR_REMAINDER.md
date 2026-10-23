# The full primitive scalar remainder on the Möbius coefficient

22 October 2026. Status: proposed theorem; independent review pending.
Scope: a scalar pairing with the original Möbius coefficient, including
every divisor and Euler factor from primitive inversion. This is not an
operator estimate on arbitrary label combinations and does not bound the
full inverse moment or its complementary row space. No smaller zero-free
boundary is claimed.

## 1. Statement, notation, and exact inputs

Use the normalizations and the fixed modulo-36 original section family
of `MOBIUS_FULL_SERIES_SCALAR_REMAINDER.md`, frozen SHA256
`b45267a73c0123cb0a1d83c161ae5fe995e4493d7395bfcb21a67a790d54fcaf`.
The completed-reflection kernel is the companion
`COMPLETED_FE_KERNEL.md`, frozen SHA256
`6f050d0e66769b4989a4b7c42f1a555ee10a2ee05a14ea1585595c784425066e`.
It records the finite bad-prime unit quotient used to resolve the
functional-equation source's inconsistent displayed h-index.
The full-series scalar theorem is not used as a black box here: we use
its finite-vector completed reflection, finite full-modulus extraction,
and the inherited inverse estimate, retaining their dependence on all
new parameters. The primary functional-equation source is
Bröker--Hoffstein, <https://arxiv.org/html/1312.0568v1>, (3.1),
(3.8)--(3.10) and the local gamma formulas following (3.10).

Primitive inversion is paper 10 version 2, (3.6)--(3.7), snapshot
SHA256 `525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`:

<https://rstation.ai/api/v1/papers/riemann_hypothesis_10/versions/2/download>.

The residue density at every numerator valuation is paper 8 version 1,
Section 3, snapshot SHA256
`f1f9aed624908ccb9b6842911d898916230545ff76dc123187d7eadc3558def1`:

<https://rstation.ai/api/v1/papers/riemann_hypothesis_8/versions/1/download>.

The exact inverse input is the inherited adapter
`standalone/2026-10-20-boundary-iteration/mixed/MARKED_CANONICAL_MEAN.md`,
Sections 1--3, at commit
`64cb43c038d1828a478cb97cbc32e435e111d2d2`, SHA256
`3e3c8c123f29fdedcf6afd987341ba31b481be096f3d421be4b7409dfe8234d9`.
Set its prime-label parameter to one; its Section 3 retains all rows and
the fixed-during-the-row-sum puncture. Its primary input is Liu,
<https://arxiv.org/html/2610.26835v1>, Theorem 11.2, with the stated
smooth norm-twist uniformity.

All ideals below are good and represented multiplicatively. **Within
real powers and length inequalities, a lowercase ideal symbol denotes
its norm.** Thus `d=f d_0` is an ideal factorization, while `d^2 k^6`
in a physical length means `(Nd)^2(Nk)^6`. This convention keeps the
parameter accounting readable. The capital letter D is the column
length and is never an ideal.

Fix smooth annular `W,w`, a fixed finite ray character `nu_0`, a
puncture Q fixed during every row average, and an optional fixed
numerator-sector restriction. Put

\[
 b_n=1_{(n,Q)=1}\frac{\mu(n)\nu_0(n)}{\sqrt{Nn}}W(Nn/D),
 \qquad
 \mathcal P(U)=\sum_n b_n\mathcal E_U[H_\nu(n,\cdot)],
                                                               \tag{1}
\]

where `E` denotes the Mellin integral on `Re u=1+eta`,
`0<eta<1/12`, with kernel `widehat w(u-1/2)U^(u-1)`. The primitive
series is the one with the literal modulus exclusion `(c,n)=1`.

**Theorem.** For every `epsilon>0`, uniformly for `U,D>=1`,

\[
 \boxed{\qquad
       |\mathcal P(U)|^2
          \ll_\epsilon(UDNQ)^\epsilon\bigl(U+D^{11/12}\bigr).
       \qquad}                                             \tag{2}
\]

All constants have the sources' fixed ray and smooth-seminorm
dependence. No premise about a new zero-free boundary enters the proof.

We use the inverse polynomial bound in the precise coefficient class

\[
 I(H,A;Q')\ll(HA NQ')^\epsilon
                    \bigl(H+H^{1/6}A^{5/6}\bigr),          \tag{3}
\]

including fixed ray partitions, smooth annular profiles, and their
norm twists. We also use the reference-scale primitive pole bound

\[
 \left|\sum_m\frac{\mu(m)\xi(m)}{\sqrt{Nm}}V(Nm/A)
          1_{(m,Q')=1}\rho_{\rm prim,\nu}(mR)\right|^2
       \ll(A NR NQ')^\epsilon A^{2/3}(NR)^{1/3}.          \tag{4}
\]

Its proof is the companion note
`MOBIUS_PRIMITIVE_POLE_REFERENCE_SCALE.md`; it chooses reference row
scale `T=A sqrt(NR)` in the exact primitive adjoint identity and uses
paper 10's continuous mean. No primitive-inversion branch is substituted
for the entire pole in that argument.

## 2. A full-residue progression bound

For a squarefree good ideal q, let

\[
       P_q(D)=\sum_{q\mid n}b_n\rho_{\rm full,\nu}(n).
\]

Then

\[
                 |P_q(D)|^2
             \ll(DqNQ)^\epsilon D^{2/3}q^{-4/3}.         \tag{5}
\]

If `(q,Q)>1` the expression is zero. Otherwise put `n=qm`, with
`(q,m)=1`. Paper 8 gives
`rho_full(n)=rho_prim(n) prod_(p|n)(1+1/Np)`. Separate the q-factor
and expand the m-factor as `sum_(r|m)1/r`. On putting `m=r l`, the
scalar outside the normalized Möbius coefficient in l is
`q^(-1/2) r^(-3/2)`, up to unit factors and a q-subpower. Its length
is `D/(qr)`, label is `qr`, and puncture is `Qqr`. By (4) its squared
size is

\[
     \ll(DqNQ)^\epsilon q^{-1}r^{-3}
                (D/(qr))^{2/3}(qr)^{1/3}
       =(DqNQ)^\epsilon D^{2/3}q^{-4/3}r^{-10/3}.
\]

The square roots sum absolutely in r, proving (5). This proof keeps
the modulo-36 section scope of paper 8; it does not require a density
identity for every component appearing only on the reflected side.

## 3. Exact primitive and completion expansions

For squarefree n, paper 10 gives

\[
 H_\nu(n,u)=E_n(u)^{-1}\sum_{d\mid n}
      \sigma_d(n)d^{3/2-2u}D_\nu(nd^2,u),
\quad
 \sigma_d(n)=\mu(d)\nu(d)^2\gamma_2(d)
                          \overline{\chi_d(n/d)}^2,
\]

\[
 E_n(u)=\prod_{p\mid n}(1-(Np)^{5-6u}),\qquad
 E_n(u)^{-1}=\sum_{k\mid n^\infty}k^{5-6u}.              \tag{6}
\]

The factor `nu(p)^6` is one in the fixed section family. All these
Euler series converge absolutely on the original line. The monomials
in (6) change the physical scale and outside scalar exactly as

\[
 d^{3/2-2u}k^{5-6u}U^{u-1}
        =d^{-1/2}k^{-1}\bigl(U/(d^2k^6)\bigr)^{u-1}.
                                                               \tag{7}
\]

Write `Z_n= zeta_S(6u-5)D_n`. For fixed squarefree d and arbitrary k,
define the completed scalar block at external scale T by

\[
 F_{d,k}(T)=d^{-1/2}k^{-1}
   \sum_{\substack{d\mid n\\\operatorname{rad}(k)\mid n}}
       b_n\sigma_d(n)
          \mathcal E_{T/(d^2k^6)}[Z_\nu(nd^2,\cdot)].    \tag{8}
\]

Its n-sum is still squarefree. The exact right-line reciprocal Euler
identity now reads

\[
            \mathcal P(U)
       =\sum_{d\ {\rm sf}}\sum_k\sum_{a\ {\rm good}}
                      \frac{\mu(a)}a F_{d,k}(U/a^6).
                                                               \tag{9}
\]

No k or a scale is discarded. Initially (9) follows by absolute
convergence on the original Mellin line, with the finite n-sum kept
inside. The bounds below also give absolute convergence after the
specified finite/reflected decompositions.

## 4. The exact free inverse coefficient in both finite expansions

Fix d,k and put

\[
       v=\operatorname{rad}(k)/(\operatorname{rad}(k),d).
\]

The squarefree numerator then has `n=d v l`, with its three factors
pairwise coprime. In a nonzero full Gauss term, write

\[
       d=f d_0,\qquad c=e^2f^4c_0,\qquad e\mid n/d,
\quad e_0=(e,v),\quad e=e_0e_1,\quad v=e_0v_0,
\quad l=e_1l_0.                                         \tag{10}
\]

All displayed squarefree factors of n are pairwise coprime after
their repeated e0 occurrence is resolved. In particular
`n=f d_0 e v_0 l_0`. The residual modulus `c_0` is squarefree and
prime to n. These are precisely the possible nonzero modulus
valuations: exponent two at selected primes of `n/d`, exponent four
at selected primes of d, and exponent one elsewhere.

Here is the character check before any absolute estimate. At primes
of e the local Gauss sum supplies
`overline(chi_e(l_0))^2`. At primes of f it supplies
`overline(chi_f(l_0))^4`. The primitive coefficient in (6) supplies
`overline(chi_f(l_0))^2 overline(chi_(d_0)(l_0))^2`.
The f-powers multiply to the sixth-power **zero mask**. The remaining
squarefree modulus supplies `overline(chi_(c_0)(l_0))`. Squared
reciprocity, and a fixed ordinary reciprocity-sector partition,
therefore give the free column character

\[
                 \overline{\chi_{l_0}(c_0(e d_0)^2)}.
                                                               \tag{11}
\]

The free coefficient is exactly `mu(l_0)` times a fixed ray character.
Every other arithmetic factor is outside its sum, and has modulus at
most one after the explicit local Gauss norms are extracted. Punctures
at all fixed factors and Q remain. The residue at a nonunit is never
replaced by a unit character value.

The free column length and the scalar left after Cauchy in c0 are

\[
       A=\frac{D}{e f d_0v_0},\qquad
       \lambda=k^{-1}e^{-1}f^{-3/2}d_0^{-1}v_0^{-1/2}.
                                                               \tag{12}
\]

On the original finite side, the physical modulus scale is
`T/(d^2k^6)`; on the reflected finite side it is
`D d^4 k^6/T`. Since the inverse row in (11) has norm
`Nc_0 (e d_0)^2`, the corresponding row lengths are exactly

\[
       H_o=\frac{T}{k^6 f^6},\qquad
       H_r=\frac{Dk^6d_0^6}{T}.                         \tag{13}
\]

Thus each finite contribution is bounded in amplitude by
`lambda sqrt(I(H_o,A))` or `lambda sqrt(I(H_r,A))`, respectively.
The full-series completion introduces an additional variable b with
outside weight `1/b` and replaces the row length by `H/b^6`.
The volume and non-volume square-root weights are respectively `b^-4`
and `b^-3/2`; both sum absolutely. Bad-prime completion factors on the
reflected side are retained as in the companion kernel lemma.

The shared kernels involve only fixed annular norm coordinates.
Their common Mellin/Fourier separation and smooth seminorm bounds are
those verified in the full-series note. On the reflected side the
kernel is `O(x^(1/6-delta))` at zero and rapidly decreasing at infinity.
Modulus dyads therefore sum with (13), including subunit effective
scales. The source's polynomial norm-twist dependence is paid by the
same common smooth transform. No arithmetic coefficient depending on
the free column is inserted into (3).

## 5. The balanced a split and the non-volume sums

For each fixed d,k use the cutoff

\[
        A_{d,k}=U^{1/6}D^{-1/12}k^{-1}d^{-1/2},
 \qquad B=U^{1/3}D^{-1/6},\qquad
        A_{d,k}\ge1\ \Longleftrightarrow\ dk^2\le B.     \tag{14}
\]

If `A_(d,k)>=1`, use completed reflection for `a<=A_(d,k)` and
the original finite-minus-pole expansion for `a>A_(d,k)`. If the
cutoff is below one, use the original expansion for every a. The
cutoff depends only on the frozen d,k and the fixed length parameters,
not on the current n or the extracted e.

After multiplication by the reciprocal-completion scalar `1/a`, the
non-volume square-root term of (3) is, on the reflected side,

\[
 D^{1/2}U^{-1/12}a^{-1/2}k^{-1/2}
       e^{-17/12}f^{-23/12}d_0^{-11/12}v_0^{-11/12},
                                                               \tag{15}
\]

and on the original side it is

\[
 D^{5/12}U^{1/12}a^{-3/2}k^{-3/2}
       e^{-17/12}f^{-29/12}d_0^{-17/12}v_0^{-11/12}.
                                                               \tag{16}
\]

The elementary ideal sums of `a^-1/2` up to the cutoff and of
`a^-3/2` above it show that their combined amplitude is at most

\[
       D^{11/24}k^{-1}e^{-17/12}f^{-13/6}
                         d_0^{-7/6}v_0^{-11/12},         \tag{17}
\]

apart from subpowers. If `A_(d,k)<1`, the full original sum (16) is
smaller than (17) by the factor `A_(d,k)^(1/2)`, so (17) remains a
valid bound in that case.

The weight in (17) is absolutely summable over the **actual** k
support. To see this without losing its support information, extend
the permitted pairwise-coprime factors positively and inspect one
good prime of norm q. If it belongs to d0, f, or e, the local costs are
respectively

\[
    \frac{q^{-7/6}}{1-q^{-1}},\qquad
    \frac{q^{-13/6}}{1-q^{-1}},\qquad
    \frac{q^{-17/12}}{1-q^{-1}}.
\]

These include every possible k-valuation. If the prime is in none of
these factors but occurs in k, it must belong to v0, and its cost is

\[
                     \frac{q^{-23/12}}{1-q^{-1}}.
\]

Thus the whole sum is bounded by the convergent Euler product with
local factor one plus these four quantities. Its smallest exponent
is `7/6>1`. Choosing smaller internal subpowers preserves convergence.
The total non-volume amplitude is therefore `O(D^(11/24+epsilon))`.

## 6. The volume terms

After the same split, when `dk^2<=B`, the reflected head and original
tail volume amplitudes are both at most a constant times

\[
                D^{1/4}k^{-1}e^{-1}f^{-3}
                                      d_0^{1/2}v_0^{-1/2}.
                                                               \tag{18}
\]

For example the reflected term before summing a is
`sqrt(D/U) a^2 k^2 e^-1 f^-3/2 d_0^2 v_0^-1/2`;
`sum_(a<=A) a^2 << A^3` gives (18). The original tail uses
`sum_(a>A) a^-4 << A^-3` and gives the same power.

Drop `v_0^-1/2<=1`, use `e<=C D`, and sum first in
`d_0<=B/(f k^2)`. The total is bounded by

\[
 D^{1/4}(\log(2D))B^{3/2}
                 \sum_k k^{-4}\sum_f f^{-9/2}
                         \ll U^{1/2}\log(2D).           \tag{19}
\]

When `dk^2>B`, only the original expansion is used. Its full a-sum
volume amplitude is at most

\[
                    U^{1/2}k^{-4}e^{-1}f^{-9/2}
                                      d_0^{-1}v_0^{-1/2}.
\]

The e and d0 sums cost logarithms; k and f sum absolutely. This
range also contributes `O(U^(1/2)(UDNQ)^epsilon)`. If `B<1`, the
range in (19) is empty and this last argument applies to every d,k.

## 7. The partial pole terms and their exact signs

At theta, paper 8's density and the paired local inversion give

\[
       \sigma_d(n)\rho_{\rm full,\nu}(nd^2)
                      =\mu(d)d^{-1/6}\rho_{\rm full,\nu}(n).
                                                               \tag{20}
\]

Indeed at one selected prime the identity
`D_1=H_1+a_1 H_3`, together with
`rho_Hj=q/(q+1) rho_Dj`, gives
`a_1(theta)rho_D3=q^-1 rho_D1`; the factor in sigma differs from
`a_1(theta)` by `-q^(5/6)`. Iterating retains the phases of paper10
(3.7) and proves (20). This statement concerns the original section,
before its functional equation is applied.

Consequently the completed pole in `F_(d,k)(T)` is, up to the fixed
scalar `zeta_S(2) widehat w(2/3)`, exactly

\[
                  T^{1/6}\mu(d)d^{-1}k^{-2}P_{dv}(D).
                                                               \tag{21}
\]

In the original expansion it appears with a minus sign. The proof
retains that sign; only the subsequent upper bound takes its absolute
value. Equation (5) bounds its amplitude at T=U by

\[
                     U^{1/6}D^{1/3}
                                     d^{-5/3}k^{-2}v^{-2/3}.
                                                               \tag{22}
\]

The additional a-scalar and the pole scaling give `a^-2`, not `a^-1`.
The original-branch a-set therefore contributes at most
`min(1,A_(d,k)^-1)` times (22), with a fixed harmless constant. Since
this is at most `A_(d,k)^-1`, its amplitude is bounded by

\[
                         D^{5/12}d^{-7/6}k^{-1}v^{-2/3}.
                                                               \tag{23}
\]

This too sums absolutely with the actual support `v=rad(k)/(rad(k),d)`.
At a prime dividing d the local cost is
`q^-7/6/(1-q^-1)`; at a prime outside d that occurs in k the cost is
`q^-5/3/(1-q^-1)`. Both form a convergent Euler product. Thus all
partial original-branch poles contribute `O(D^(5/12+epsilon))`
in amplitude, smaller than the non-volume bound in (17).

The cutoff (14) is independent of n, so (21) genuinely contains the
same progression pairing `P_(dv)` throughout the partial a-sum.
There is no row-dependent selector inside (5). Scales below the first
possible modulus are covered exactly: the original finite sum is then
empty and only its negative pole remains.

## 8. Conclusion and boundary of the result

Combining (17), (19), and (23) gives

\[
       |\mathcal P(U)|
       \ll(UDNQ)^\epsilon
             \bigl(U^{1/2}+D^{11/24}+D^{5/12}\bigr),
\]

which proves (2) after choosing smaller internal epsilon losses.
All prime branches, primitive Euler powers k, global completion powers
a, and reflected completion powers remain in the argument.

Together with the entire primitive pole bound, the actual Gauss-vector
pairing therefore has squared upper bound

\[
          (UDNQ)^\epsilon
                \bigl(U+ D^{11/12}+U^{1/3}D^{2/3}\bigr).
                                                               \tag{24}
\]

This is a statement about one scalar projection. The exact inverse
moment is a squared norm over all rows. A smaller upper bound for a
projection does not bound its orthogonal complement. To improve the
zero-free boundary, a further theorem must insert these estimates into
the entire signed first-Poisson return, with its common-divisor
projector and all shared profiles, or must control the full
complementary operator. Neither implication is asserted here.
