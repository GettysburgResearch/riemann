# Genus-two Sym12 conditional endoscopic closure

Status: **EXACT STABLE-CHANNEL CLOSURE; ONE EISENSTEIN GATE REMAINS**
Scope: formal trace-channel algebra for the ambient stack
`A_2(w^1)`, with a source-locked exact marked modular zero
Exact repository sources: committed Sym12 inventory, finite scout, and corrected
marked-valuation certificate
Runtime: finite branching and integer algebra only; no web, database, field,
polynomial, curve, or modular-form-space query
Smallest remaining gap: resolve the nonregular one-Tate Eisenstein discrepancy
as an actual compact-support Galois Euler class

The replay is `genus2_sym12_conditional_endoscopic_closure.py`; its canonical,
self-hashed output is `genus2_sym12_conditional_endoscopic_closure.json`.

## 1. Master defect identity and one-gate closure

Let `f_+` and `f_-` be the normalized Fricke-positive and Fricke-negative
rational newforms of weight 14 and level 2. Define

\[
 \varepsilon_{\rm Eis}
 =e_{\rm Eis}^{S_5}-(2-5\mathbb L),
\]

and let `G` denote the positive stable/general `S5`-invariant Galois channel,
so its contribution to the compact-support Euler characteristic is `-G`.
The theorem-supported endoscopic specialization in Section 3 and the
committed project ambient identity then give the exact defect reduction

\[
\boxed{
 \widehat H_{12}
 =-\mathbb Lf_-+\varepsilon_{\rm Eis}-G.
}
\tag{1}
\]

The corrected marked-valuation packet and the primary form-to-cohomology
adapter now prove the second formerly open statement:

\[
\boxed{G=0.}
\tag{2}
\]

The source-locked proof is
[`GENUS2_SYM12_MODULAR_ZERO_GENERAL_CHANNEL_ADAPTER.md`](GENUS2_SYM12_MODULAR_ZERO_GENERAL_CHANNEL_ADAPTER.md).
It uses the exact marked cusp-space zero together with Roesner's
arbitrary-weight stable direct-sum theorem. It does not use the conjectural
`k=3` isotypical formula or an Eisenstein continuation.

The desired final closure therefore uses only one additional statement:

1. the nonregular compact-support Eisenstein formula continues with the BFG
   convention, so `epsilon_Eis=0`;

Under that one unresolved premise, (1)--(2) become

\[
\boxed{\widehat H_{12}=-\mathbb L f_-.}
\tag{3}
\]

For `q=p^r`, the first term in (1) means

\[
 -p^r(\alpha_{-,p}^r+\beta_{-,p}^r),
\]

with the other two channels evaluated by their `F_p^r` traces. It does not
mean `-p^r` times a naive composite-index Fourier coefficient. Equation (1)
is an exact source-relative reduction, equation (2) is theorem-grade, and
equation (3) is not yet an
unconditional all-odd-prime-power theorem.

## 2. Exact `S6 -> S5` branching

For the standard subgroup `S5` fixing one of six labels, the branching rule is

\[
\operatorname{Res}^{S_6}_{S_5}s[\lambda]
=\sum_{\mu} s[\mu],
\]

where `mu` runs over the partitions obtained by removing one corner from
`lambda`. An `S5`-fixed vector is therefore a copy of the trivial
representation `s[5]`. Removing one box gives `[5]` precisely from

\[
\lambda=[6]\quad\text{or}\quad\lambda=[5,1],
\]

once in either case. The producer generates all eleven partitions of six,
removes every valid corner, and verifies

\[
\dim s[\lambda]^{S_5}=
\begin{cases}
1,&\lambda=[6],[5,1],\\
0,&\text{otherwise}.
\end{cases}
\]

This part is exact representation theory and has no conjectural input.

## 3. Endoscopic specialization

Bergström--Faber--van der Geer (BFG), Conjecture 8.1, applies to `l != m`.
Set

\[
(l,m)=(12,0),\qquad k=l+m+4=16,\qquad k'=l-m+2=14.
\]

The elementary multiplicities are

\[
\tau_{1,16}=\tau_{2,16}=\tau_{16}^{+}=1,
\qquad \tau_{16}^{-}=0,
\]

and

\[
S_{14}(\mathrm{SL}_2(\mathbf Z))=0.
\]

The exact `S5` projection has these surviving pieces:

- the full level-2 newspace occurs once and equals `f_+ + f_-`;
- its Fricke-positive channel has coefficient zero on `[5,1]`;
- its Fricke-negative channel occurs once more on `[5,1]`;
- the level-4 terms have no `[6]` or `[5,1]` channel;
- the level-1 weight-14 space is zero.

Consequently the expression inside BFG's leading `-L` is

\[
(f_++f_-)+f_-=f_++2f_-,
\]

so the specialization is

\[
\boxed{e_{\mathrm{endo}}^{S_5}
=-\mathbb L(f_++2f_-).}
\]

Source grade matters. This formula is conjectural as an invocation of BFG.
However, the semisimplified inner/endoscopic mechanism is independently
theorem-supported for nonregular weights by Rösner, Theorem 5.13, pp. 97--98,
and Shmakov, Theorem 4.6.4, p. 366. That later theorem support does **not**
prove the compact-support Eisenstein term used below.

## 4. Nonregular Eisenstein gate

Formally specialize BFG's `A_2(w^1)` Eisenstein expression:

\[
\dim S_{14}(\Gamma_0(2))
-\dim S_{16}(\Gamma_0(2))\mathbb L
+2(S[2]+1).
\]

The dimensions are

\[
\dim S_{14}(\Gamma_0(2))=2,
\qquad
\dim S_{16}(\Gamma_0(2))=3,
\]

and BFG's nonregular convention is `S[2]=-L-1`. Hence

\[
2-3\mathbb L+2(-\mathbb L)=2-5\mathbb L.
\]

But this is not a theorem in BFG. Their Eisenstein theorem is stated for
regular weights; for `m=0` the paper says the continued formula is expected,
and the corresponding equivariant decomposition is also conjectural.

There is a concrete later-literature gate. Direct `S5` specialization of
Shmakov's printed formulas gives

\[
\begin{array}{c|c}
\text{piece}&\text{specialization}\\ \hline
\text{Siegel Eisenstein}&2-2\mathbb L\\
\text{Klingen}&0\\
\text{Borel}&-2\mathbb L
\end{array}
\]

and therefore `2-4L`, not `2-5L`. The missing term is one
`[5,1] tensor L` copy tied to the unique Fricke-positive weight-16 level-2
newform. Rösner constructs the natural `S6` action from the six Weierstrass
points, so this cannot presently be dismissed as an outer-automorphism
convention. Connecting-morphism assumptions do not alter the Euler
characteristic, although a Galois-action caveat remains.

Thus

\[
(2-5\mathbb L)-(2-4\mathbb L)=-\mathbb L
\]

is an unresolved one-Tate discrepancy. BFG defines
`A_2(w^1)=A_2[2]/S5`, exactly the ambient stack used by the project, and the
Shmakov specialization uses the same natural `S5` invariants. No
open-versus-ambient correction resolving the discrepancy has been identified.
The open `M_2(w^1)` would require a separate boundary subtraction and is not
the object compared here.

## 5. Stable/general channel

The corrected two-orientation valuation packet proves

\[
S_{12,3}(\Gamma_2(w^1))=0.
\]

This is the whole natural marked cusp space: the pre-holomorphic space has
dimension `66`, the exact corrected matrix has rank `66`, and odd scalar
weight gives `M=S`.

The primary adapter is exact at the semisimplified stable level:

1. Bergstrom--Clery decompose the cusp space orthogonally into general and
   Yoshida Arthur summands.
2. BFG and Shmakov define the positive general Galois channel from the
   general-type Hecke eigenforms, with one four-dimensional representation per
   eigenvector.
3. Roesner's Corollary 5.20 applies to every `l>=m>=0`, including `(12,0)`:
   stable inner cohomology is a direct sum of four-dimensional irreducible
   Galois representations with matching holomorphic Hodge components.
4. Taking natural `S5` invariants is exact in characteristic zero.

Therefore the marked modular zero forces

\[
\boxed{G=(S_{\rm gen,\Gamma(2)}[12,3])^{S_5}=0.}
\]

Endoscopic, Saito--Kurokawa, Soudry, and Eisenstein terms cannot leak into
`G`: they are separate summands, and Roesner proves the possible level-two
Soudry contribution is zero. The conclusion concerns the positive
semisimplified stable channel; it does not settle nonsemisimple boundary
extensions or the Eisenstein Galois class.

As independent corroboration, the conditional official `k=3` query returns
only

```text
[3,1^3], [2^3], [2^2,1^2], [2,1^4], [1^6].
```

None is `[6]` or `[5,1]`, so their implemented decomposition has zero `S5`
invariant. The producer freezes those five rows, recomputes their Specht
dimensions as `10+5+9+5+1=30`, and projects their invariant multiplicities to
zero. Those rows remain conditional corroboration, not a premise. The exact
proof uses the marked rank certificate, so the full-level dimension `30` need
not determine an isotypical decomposition.

## 6. Exact ambient comparison

Work in the free trace-channel module on

```text
1, L, L*f_+, L*f_-, Hhat_12, Epsilon_Eis, Genuine.
```

The committed project inventory proves the source-relative ambient identity

\[
E_{\mathrm{proj}}
=\widehat H_{12}+2-5\mathbb L-\mathbb L(f_++f_-).
\]

Before applying the exact stable specialization, the cohomological target is

\[
E_{\mathrm{cond}}
=2-5\mathbb L+\varepsilon_{\rm Eis}
 -\mathbb L(f_++2f_-)-G,
\]

and exact subtraction gives

\[
E_{\mathrm{proj}}-E_{\mathrm{cond}}
=\widehat H_{12}+\mathbb Lf_-
 -\varepsilon_{\rm Eis}+G.
\]

This proves (1). The exact result `G=0` first gives

\[
\widehat H_{12}=-\mathbb Lf_-+\varepsilon_{\rm Eis}.
\]

After imposing the one remaining premise `epsilon_Eis=0`,

\[
E_{\mathrm{proj}}=E_{\mathrm{cond}}
\quad\Longleftrightarrow\quad
\widehat H_{12}=-\mathbb Lf_-.
\]

The one-Tate discrepancy is load-bearing. Shmakov's printed `2-4L` gives
`epsilon_Eis=L`, and hence

\[
\widehat H_{12}=\mathbb L-\mathbb Lf_- -G.
\]

The exact result `G=0` makes this
`Hhat_12=L-L*f_-`. The producer verifies the master, BFG-closed, and both
Shmakov-branch subtractions coefficientwise.

## 7. Finite combined-branch contradiction only

The committed finite scout directly replays the raw values
`T_(12,0)(p)` from stored complete joint laws. It then applies the separately
locked arithmetic-inventory identity to derive the displayed `Hhat_12` values.
Thus the following table is an exact consequence of **raw `T_(12,0)` plus the
inventory**, not an independent central-`Q_5` enumeration and not an
independent audit of the master adapter:

| `p` | `Hhat_12(p)` | `a_p(f_-)` | BFG-required `-p a_p(f_-)` | `2-4L`-required `p-p a_p(f_-)` |
|---:|---:|---:|---:|---:|
| 3 | -3,708 | 1,236 | -3,708 | -3,705 |
| 5 | 287,250 | -57,450 | 287,250 | 287,255 |
| 7 | -449,624 | 64,232 | -449,624 | -449,617 |

With `G=0`, the `2-4L` branch misses the combined arithmetic branch by exactly
`+p` in every row. The same contradiction can be written without treating
`Hhat_12` as directly observed:

\[
 T_{(12,0)}(p)+9+p+4\tau(p)+a_p(f_{8,2})+a_p(g_{10,2})
 +p\,a_p(f_-)=-p,
 \qquad p=3,5,7.
\]

This raw-`T` form still uses the exact inventory coefficients, but makes the
provenance separation explicit. Without the exact stable vanishing, the
`2-4L` branch could formally assign the discrepancy to `Tr(F_p,G)=p`. The
exact adapter removes that escape. The rows are not a premise of the formal
reduction, do not independently validate the inventory, do not realize the
Eisenstein Galois channel, and cannot prove any fourth `q` or prime-power row.

## 8. Locked repository inputs and runtime caps

The producer content-locks the canonical JSON and transitively verifies the
note/producer/test manifests of:

1. `genus2_sym12_arithmetic_inventory.json`, commit
   `482e32c53f26517906143cd0d99c74d8b4edf3be`, git blob
   `68907aa3ee65ced500807c79123f116da05f0ece`, LF SHA-256
   `94f0647a91aff299c62f24019947846e6923863f3ecba3c2f9cf95008407d4f6`,
   payload SHA-256
   `fba1c85c8dc3d60b276635ae5e3ed84db3ded06f4960afeaa9b92b4055f9211f`;

2. `genus2_sym12_finite_cusp_trace_scout.json`, commit
   `c463d4896e62057139454cb0ae2beb868506fee4`, git blob
   `68acd63d703d3569f282cd32a4160dcdd7bf76fa`, LF SHA-256
   `06cc45904ee427fa6b2d2812b6c54d2312d6b9d41e12cd4689d28b7def360d2e`,
   payload SHA-256
   `1c794190e4e83778de852d1f12df5a35fccbce414c27df67eeeb6f87ed7ee1d1`;

3. `genus2_sym12_marked_valuation_kernel.json`, commit
   `a0871416abb4ac58132b53dd4ae30faeed9719bd`, git blob
   `6e9fcc3d42f1a7acf74759dd408259fd507c79f0`, LF SHA-256
   `9e833cb7778c6613d0f4c7ef22a72319864c05ce41c50addc9dee778d5446076`.

Including the first two transitive packet manifests, the runtime reads exactly
nine files and 174,029 bytes. It processes eleven partitions, 35 partition rows,
19 removable corners, eleven endoscopic projection terms, 30 hook boxes,
70 free-module component operations, and three finite corroboration rows.
Those are also hard caps. Output is capped at 32,768 bytes and runtime at four
seconds. There are no network, database, field, polynomial, curve, or family
enumeration calls.

## 9. Literature/source grades

- Bergström, Faber, and van der Geer,
  [*Siegel Modular Forms of Genus 2 and Level 2: Cohomological Computations and
  Conjectures*](https://arxiv.org/abs/0803.0917): the form-attached rank-four
  inner channel, BFG Conjecture 8.1, and the explicitly expected nonregular
  Eisenstein continuation.
- Rösner, dissertation, pp. 95--99, Theorem 5.13, and Corollary 5.20:
  [arbitrary-weight holomorphic/stable and semisimplified inner/endoscopic
  theorems](https://sites.math.unt.edu/~schmidt/dimension_formulas/papers/2016_Dissertation_Roesner_final.pdf).
- Shmakov, dissertation, Theorem 4.6.4 and Theorems 4.6.6--4.6.8:
  [inner/endoscopic theorem and the one-Tate Eisenstein
  discrepancy](https://openscholar.uga.edu/nanna/record/1979/files/dissertation.pdf).
- Bergström--Cléry,
  [arXiv:2309.04388v2](https://arxiv.org/abs/2309.04388), Theorem 5.3 and
  Remark 5.4: exact Arthur decomposition and the boundary between it and the
  conditional `k=3` isotypical continuation.
- Cléry--van der Geer,
  [arXiv:2605.13300](https://arxiv.org/abs/2605.13300): covariant/valuation
  structure and `A_2[w]=A_2[2]/S5`; the project packet performs the corrected
  exact `(12,3)` valuation rank.
- [Official Siegel modular-form data query](https://smf.compositio.nl/api/Entries/2/2?j=12&k=3&l=0):
  frozen isotypical corroboration only; never queried by the producer.

No external novelty claim is made. No motivic isomorphism, compatible system,
RH/GRH implication, number-field transfer, or global Euler-product statement
is asserted.
