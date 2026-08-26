# Finite-abelian hard masks: relative projectors and subgroup compression

Status: **exact finite-abelian Fourier/torsor theorem; exact formal
checkerboard compression; growing-source realization and global estimates
remain open**

Exact replay:
[`ffps_finite_abelian_subgroup_mask_compression.py`](ffps_finite_abelian_subgroup_mask_compression.py)

## 0. Outcome

The cyclic relative-projector theorem extends to every finite abelian hard
mask.  The extension reveals a favorable feature of the many-factor
checkerboard which is invisible if geometric complexity is identified with
the number of local factors.

Let `G` be a finite abelian group of order `N`, let `A` be a nonempty subset
of size `s`, and normalize its hard weight by

\[
 w_A(g)={N\over s}{\bf 1}_A(g).
\tag{0.1}
\]

For a finite source atom set with phase map `Phi:Omega -> G`, average the
squared hard observation over every translate of `A`.  Then

\[
 \boxed{Q_A=Q_{\rm pr}+Q_{\rm sel},\qquad Q_{\rm sel}\ge0,}
\tag{0.2}
\]

and the total selected Fourier mass is

\[
 \boxed{u={N\over s}-1.}
\tag{0.3}
\]

On a `G`-torsor, (0.2) is the trace of an honest endomorphism identity

\[
 \boxed{\mathsf C_A-\mathsf S_A=\Pi_{\bf1}.}
\tag{0.4}
\]

If `A` is a coset of a subgroup of index `h`, Fourier support is exactly the
annihilator subgroup of order `h`, every supported coefficient has modulus
one, and

\[
 \boxed{
 \mathsf C_A=\sum_{\chi\in H^\perp}\Pi_\chi,
 \qquad
 \mathsf S_A=\sum_{\substack{\chi\in H^\perp\\\chi\ne\mathbf1}}\Pi_\chi.}
\tag{0.5}
\]

Thus an index-two mask has **one selected Fourier line**, regardless of the
number of ambient tensor factors.  For the global parity checkerboard on
`G=C_2^d`,

\[
 \boxed{\mathsf C_{\rm cb}=\Pi_{\bf1}+\Pi_{\chi_{\rm top}},
 \qquad \mathsf S_{\rm cb}=\Pi_{\chi_{\rm top}}.}
\tag{0.6}
\]

The formal restricted-Gram leverage can nevertheless improve exponentially
with `d`:

\[
 L_{\rm cb}={4N\over Q+P},\qquad
 L_{\rm full}={N\over Q},\qquad
 {L_{\rm cb}\over L_{\rm full}}={4Q\over Q+P},
\tag{0.7}
\]

where

\[
 N=\prod_i{p_i-1\over2},\quad
 Q=\prod_i{p_i+1\over2},\quad
 P=\prod_i p_i,
\]

and every `p_i=1 mod 4`.  Here the selected spectral rank, selected mass,
and sharp Wick diagonal repair are all exactly one.  What can grow is not
the rank but the ramification/Betti complexity of the tensor character and
the complexity of realizing a genuine many-factor physical source.

This sharpens the design target:

> Search for quotient-subgroup masks with small quotient order.  They can
> compress exponentially many ambient coordinates into a fixed number of
> selected rank-one systems.  The remaining question is whether their
> geometric conductor, cleanup, and source complexity grow slowly enough.

It does **not** prove such a source theorem, a varying-conductor estimate,
RH, or GRH.

## 1. Frozen dependencies and scope

| source | commit | git blob | role |
|---|---|---|---|
| `FFPS_CORRELATED_MASK_AMPLIFIER.md` | `6e4609dfe` | `4569c521e99e8c591f1694126605f8abee8a75f8` | formal product Gram and checkerboard leverage |
| `FFPS_CHECKERBOARD_SOURCE_BRIDGE.md` | `6e4609dfe` | `15c32de6182407e65a6d41d593f7542945bf704e` | exact two-prime physical realization and growing-`d` firewall |
| `FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md` | `464c3705f` | `ab16e6c0894e51303119692e67b2f2bf59ba73e4` | cyclic torsor convention and relative projector |
| `FFPS_WICK_CENTERED_DOMINATION_BOUNDARY.md` | `7ad6f127d` | `cde24e9ce59c064ddfd8b711a2d42fd4daa3ee60` | sharp centered collision cost |

The finite-abelian theorem below is independent of the FFPS source.  Formula
(0.7) is a formal product-Gram specialization.  The frozen source bridge
realizes only the bilateral two-prime checkerboard.  It explicitly does not
realize the many-factor asymptotic in the live source.

Throughout, the coefficient field has characteristic zero, contains the
values of the relevant characters, and `|G|` is invertible.  For a nonsplit
group scheme, individual character projectors need not descend; only sums
over Galois orbits are automatically defined over the ground field.

## 2. Arbitrary translated hard masks

Write `Ghat` for the character group and normalize

\[
 \widehat w_A(\chi)
 ={1\over N}\sum_{g\in G}w_A(g)\chi(g)^{-1}
 ={1\over s}\sum_{a\in A}\chi(a)^{-1}.
\tag{2.1}
\]

Then `w_A` has principal coefficient one and Parseval gives

\[
 \sum_{\chi\in\widehat G}
 \widehat w_A(\chi)\widehat w_A(\chi^{-1})
 ={N\over s}.
\tag{2.2}
\]

After choosing a complex embedding, each product in (2.2) is
`|hat w_A(chi)|^2`.  Hence the nontrivial sum is exactly (0.3).

Put

\[
 P=\sum_\omega z_\omega,\qquad
 H_\chi=\sum_\omega\chi(\Phi(\omega))z_\omega.
\]

For `h in G`, define

\[
 O_h=\sum_\omega w_A(h^{-1}\Phi(\omega))z_\omega.
\]

Fourier inversion expands this translate as

\[
 O_h=P+\sum_{\chi\ne\mathbf1}
 \widehat w_A(\chi)\chi(h)^{-1}H_\chi,
\tag{2.3}
\]

up to the harmless simultaneous inverse convention.  Character
orthogonality therefore gives

\[
 {1\over N}\sum_{h\in G}|O_h|^2
 =|P|^2+\sum_{\chi\ne\mathbf1}
 |\widehat w_A(\chi)|^2|H_\chi|^2.
\tag{2.4}
\]

This proves (0.2).  The corresponding autocorrelation trace function is

\[
 K_A(g)=\sum_\chi
 \widehat w_A(\chi)\widehat w_A(\chi^{-1})\chi(g)
 ={N\over s^2}|A\cap gA|,
\tag{2.5}
\]

with the inverse in `g` depending only on the chosen translation convention.
In particular `K_A(1)=N/s` and the selected kernel is `K_A-1`.

## 3. Honest endomorphism on a torsor

Let `pi:T -> U` be a torsor under the split constant group `G` and put
`H=pi_*E_T`.  With the right-regular deck action `rho`, define

\[
 \Pi_\chi={1\over N}\sum_{g\in G}\chi(g)^{-1}\rho(g).
\tag{3.1}
\]

The `Pi_chi` are pairwise orthogonal rank-one idempotents and sum to the
identity.  Define

\[
 \begin{aligned}
 \mathsf C_A
 &=\sum_\chi
 \widehat w_A(\chi)\widehat w_A(\chi^{-1})\Pi_\chi,\\
 \mathsf S_A
 &=\sum_{\chi\ne\mathbf1}
 \widehat w_A(\chi)\widehat w_A(\chi^{-1})\Pi_\chi.
 \end{aligned}
\tag{3.2}
\]

Because `hat w_A(1)=1`, subtraction proves (0.4) inside
`End_U(H)`.  This is not a virtual multiplicity statement.  It is an
identity of actual endomorphisms.  Any additive `E`-linear equivariant
derived operation preserves it, provided the same object, morphism, and
Frobenius convention are used on both sides.  Nonadditive cleanup and
changing open strata require a new proof.

At an unramified closed point whose torsor Frobenius is `phi_x in G`, the
trace functions are

\[
 \operatorname{Tr}(\mathsf C_A\operatorname{Frob}_x)=K_A(\phi_x),
 \quad
 \operatorname{Tr}(\mathsf S_A\operatorname{Frob}_x)=K_A(\phi_x)-1,
 \quad
 \operatorname{Tr}(\Pi_{\bf1}\operatorname{Frob}_x)=1.
\tag{3.3}
\]

Thus the scalar autocorrelation identity is the pointwise shadow of (0.4).

## 4. Subgroup-coset compression

Let `A=aH` for a subgroup `H<G` of index `h`.  Character orthogonality on
`H` gives

\[
 \widehat w_A(\chi)=
 \begin{cases}
 \chi(a)^{-1},&\chi|_H=1,\\
 0,&\chi|_H\ne1.
 \end{cases}
\tag{4.1}
\]

The annihilator `Hperp` has order `h`, so (0.5) follows.  This proves four
exact compression facts:

1. the number of selected character lines is `h-1`;
2. the total selected mass is `u=h-1`;
3. the answer is independent of the ambient order `N`;
4. translating the coset changes coefficient phases but not the covariance
   endomorphism.

More generally, if a mask is the inverse image of `B` under a quotient
`G -> Q`, every supported Fourier character comes by pullback from `Q`.
The selected mode count, mass, and relative projector can therefore be
bounded in the quotient, even when the ambient tensor has many factors.

This is the exact algebraic meaning of **quotient compression**.  It does
not bound the conductor of the pulled-back character sheaves.

## 5. Global parity on `C_2^d`

Take

\[
 G=C_2^d,\qquad
 \chi_{\rm top}(x_1,\ldots,x_d)=(-1)^{x_1+\cdots+x_d},
\]

and let `A=ker(chi_top)`.  Equations (4.1)--(0.6) show that the entire
selected object is one line.  If a product torsor splits as
`T=T_1 \times_U \cdots \times_U T_d`, then

\[
 \operatorname{im}\Pi_{\chi_{\rm top}}
 \simeq
 \mathcal L_{\chi_1}\otimes\cdots\otimes\mathcal L_{\chi_d}.
\tag{5.1}
\]

Its rank is one for every `d`.  Ramification does not disappear: singular
divisors, local conductors, boundary strata, and Betti numbers can accumulate
with the factors.  Rank compression is therefore a useful fact, not a
Deligne bound.

For the formal square-phase tensor with `m_i=(p_i-1)/2` and
`p_i=1 mod 4`, the constant and top-character eigenvalues are

\[
 \lambda_0=Q=\prod_i(m_i+1),\qquad
 \lambda_{\rm top}=P=\prod_i p_i.
\]

Since

\[
 {\bf1}_A={1\over2}({\bf1}+\chi_{\rm top}),
\]

its Gram energy is

\[
 E_A={N\over4}(Q+P).
\tag{5.2}
\]

The unique restricted optimum is the uniform retained weight two, and the
sharp leverage is (0.7).  Moreover

\[
 {P\over Q}=\prod_i{2p_i\over p_i+1}.
\tag{5.3}
\]

This product grows exponentially in `d` along ordinary prime panels, so the
formal leverage ratio in (0.7) decays exponentially.  Yet the spectral
ledger stays

\[
 (\text{selected rank},\text{selected mass},\text{Wick repair})=(1,1,1).
\tag{5.4}
\]

The first two entries follow from (0.6).  The last follows from the sharp
Wick-centering theorem: on two distinct source atoms with the same top
phase, the centered selected block is `J_2-I_2`, with eigenvalues `1,-1`.

## 6. What this changes for the research programme

The earlier cyclic Pareto theorem shows that retained density determines
total selected mass.  The present theorem adds a different coordinate:
**quotient order determines selected spectral rank** for subgroup masks.
An ambient high-dimensional mask need not create a high-rank selected
object.

This makes the global parity/checkerboard idea more attractive, but only
conditionally.  A successful arithmetic lift must still prove all of the
following:

1. a genuine many-factor physical orientation, not merely the frozen
   bilateral construction;
2. compatibility of that orientation as the closed places vary;
3. a common open stratum on which (0.4) survives every source cleanup;
4. a conductor/Betti bound for the rank-one tensor line in (5.1);
5. a globally recombined Wick-centered trace estimate;
6. survival of the hypothetical principal anomaly in the native source.

The key new possibility is that item 4 might be polynomial or additive in
the number/degree of marked places even though the formal leverage gain is
exponential.  That is now the most ambitious mask-design target.  It is a
conjectural opportunity, not a proved asymptotic family theorem.

## 7. Wick boundary for arbitrary `G`

Let `D=sum|z_omega|^2`.  The diagonal coefficients of (0.2) are

\[
 1,\qquad {N\over s}=1+u,\qquad u.
\]

After literal Wick subtraction,

\[
 Q_A^\circ=Q_{\rm pr}^\circ+Q_{\rm sel}^\circ,
 \qquad Q_{\rm sel}^\circ=Q_{\rm sel}-uD\ge-uD.
\tag{7.1}
\]

On `m` distinct atoms with the same `G`-phase, the selected block is

\[
 u(J_m-I_m),
\]

so the diagonal payment `u` is sharp.  Quotient compression can keep `u`
fixed while the ambient group grows; it cannot eliminate the centered
collision direction.

## 8. Proof ledger

| statement | grade |
|---|---|
| arbitrary finite-abelian covariance identity (0.2)--(0.3) | **PROVED EXACT** |
| torsor endomorphism and trace identity (0.4), (3.3) | **PROVED EXACT ON A SPLIT CONSTANT `G`-TORSOR** |
| subgroup-coset compression (0.5) | **PROVED EXACT** |
| one-line checkerboard selector (0.6) | **PROVED EXACT FORMAL/TORSOR ALGEBRA** |
| product-Gram leverage (0.7) | **PROVED EXACT IN THE FROZEN FORMAL TENSOR** |
| two-prime physical checkerboard | **IMPORTED EXACT FROM FROZEN SOURCE BRIDGE** |
| growing-`d` physical source | **OPEN** |
| rank-one conductor/Betti growth | **OPEN** |
| varying-conductor trace estimate, RH, or GRH | **OPEN / RH-BEARING** |

No external novelty or priority claim is made.

## 9. Reproduction

The replay checks the Walsh support, autocorrelation, and Wick spectrum for
`C_2^d`, `1<=d<=8`, plus six small exact prime panels.  It performs fewer
than 180,000 Walsh summands and no conductor, curve, character-family, or
L-function-zero enumeration.

~~~powershell
python research/l-families/atlas/function_field/ffps_finite_abelian_subgroup_mask_compression.py --check
python -O research/l-families/atlas/function_field/ffps_finite_abelian_subgroup_mask_compression.py --check
python -m unittest tests.test_ffps_finite_abelian_subgroup_mask_compression
python -O -m unittest tests.test_ffps_finite_abelian_subgroup_mask_compression
python -m ruff check research/l-families/atlas/function_field/ffps_finite_abelian_subgroup_mask_compression.py tests/test_ffps_finite_abelian_subgroup_mask_compression.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_finite_abelian_subgroup_mask_compression.py tests/test_ffps_finite_abelian_subgroup_mask_compression.py
~~~
