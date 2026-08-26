# Genus-two Sym12 conditional endoscopic closure

Status: **EXACT CONDITIONAL REDUCTION; NOT AN ALL-`q` THEOREM**
Scope: formal trace-channel algebra for the ambient stack
`A_2(w^1)`, with three separately graded imported premises
Exact repository sources: committed Sym12 inventory and committed finite scout
Runtime: finite branching and integer algebra only; no web, database, field,
polynomial, curve, or modular-form-space query
Smallest remaining gap: resolve the nonregular one-Tate Eisenstein discrepancy
and establish the stable `S5`-invariant vanishing without the same conjectural
continuation

The replay is `genus2_sym12_conditional_endoscopic_closure.py`; its canonical,
self-hashed output is `genus2_sym12_conditional_endoscopic_closure.json`.

## 1. Master defect identity and conditional closure

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

The desired closure uses two additional statements:

1. the nonregular compact-support Eisenstein formula continues with the BFG
   convention, so `epsilon_Eis=0`;
2. the stable/general Siegel cusp channel has no `S5` invariant, so `G=0`.

Under exactly those two unresolved premises, (1) becomes

\[
\boxed{\widehat H_{12}=-\mathbb L f_-.}
\tag{2}
\]

For `q=p^r`, the first term in (1) means

\[
 -p^r(\alpha_{-,p}^r+\beta_{-,p}^r),
\]

with the other two channels evaluated by their `F_p^r` traces. It does not
mean `-p^r` times a naive composite-index Fourier coefficient. Equation (1)
is an exact source-relative reduction; equation (2) is not yet an
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

Rösner and Shmakov do not evaluate the stable/general term at this weight;
Shmakov leaves `S_gen,Gamma(2)[12,3]` present. Bergström--Cléry, Theorem 5.3,
proves its isotypical formula for `k>=4`. Their Remark 5.4 extends the formula
to `k=3,j>0` only **assuming** the BFG nonregular Eisenstein conjecture.

The official data query with `j=12,k=3,l=0` returns only

```text
[3,1^3], [2^3], [2^2,1^2], [2,1^4], [1^6].
```

None is `[6]` or `[5,1]`, so their implemented decomposition has zero `S5`
invariant. The producer freezes those five rows, recomputes their Specht
dimensions as `10+5+9+5+1=30`, and projects their invariant multiplicities to
zero.

That is conditional formula/database evidence, not an unconditional theorem.
The theorem-level total dimension `30` alone does not imply the invariant
vanishing. Some sources print the weight as `S_(3,12)(Gamma[2])`; this packet
uses the project/API convention `(j,k)=(12,3)`.

Cléry--van der Geer, arXiv:2605.13300, unconditionally gives the structural
covariant/valuation description of level-2 forms and explicitly identifies
`A_2[w]=A_2[2]/S5`. It does not print or compute the `(j,k)=(12,3)`
`S5`-isotypical dimension; its dimension discussion refers back to the 2025
Bergström--Cléry work. It therefore confirms the quotient normalization but
does not upgrade the vanishing.

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

Before specializing either open channel, the cohomological target is

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

This proves (1). After imposing both `epsilon_Eis=0` and `G=0`,

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

Only after separately imposing `G=0` does this become
`Hhat_12=L-L*f_-`. The producer verifies the master, BFG-closed, and both
Shmakov-branch subtractions coefficientwise.

## 7. Finite corroboration only

The committed finite scout gives

| `p` | `Hhat_12(p)` | `a_p(f_-)` | BFG-required `-p a_p(f_-)` | `2-4L`-required `p-p a_p(f_-)` |
|---:|---:|---:|---:|---:|
| 3 | -3,708 | 1,236 | -3,708 | -3,705 |
| 5 | 287,250 | -57,450 | 287,250 | 287,255 |
| 7 | -449,624 | 64,232 | -449,624 | -449,617 |

These exact rows corroborate (2) after taking Frobenius traces. With `G=0`,
the `2-4L` branch misses them by exactly `+p` in every row. Without that
vanishing, the Shmakov branch instead forces `Tr(F_p,G)=p` for
`p=3,5,7`; the rows do not contradict Shmakov alone. They are not a premise
of the formal reduction, do not decide either open channel, and cannot prove
any fourth `q` or prime-power row.

## 8. Locked repository inputs and runtime caps

The producer content-locks the canonical JSON and transitively verifies the
note/producer/test manifests of:

1. `genus2_sym12_arithmetic_inventory.json`, commit
   `70dd4a130e702a2d6df4b0fb96a0182a560009a4`, git blob
   `b48963d7b9bc6459046024507a2f2cb8ccbbcd40`, LF SHA-256
   `e966b54fe909570eaac7d9253f635c8067c5f874ed47c9daf485c8fd88bfbd85`,
   payload SHA-256
   `557ab6465a16bb6080caa2a249c3d0935f8d36fb49bdf54898a0fe72b372496f`;

2. `genus2_sym12_finite_cusp_trace_scout.json`, commit
   `0e89f3ae989c0ef81f9f0fcfd359116d57f83f32`, git blob
   `4741ef79f8dd84634680df612cdd8b1d93d3e8bf`, LF SHA-256
   `8827b08f86fa0bd3a77698f250f9d40aea193a39b5c80e180f9a1f3acbac6ff9`,
   payload SHA-256
   `3572d443f7f5371771a0123b1ebcb1c08e010f02a65c3413d935216b1fcd3168`.

Including both transitive packet manifests, the runtime reads exactly eight
files and 150,269 bytes. It processes eleven partitions, 35 partition rows,
19 removable corners, eleven endoscopic projection terms, 30 hook boxes,
70 free-module component operations, and three finite corroboration rows.
Those are also hard caps. Output is capped at 32,768 bytes and runtime at four
seconds. There are no network, database, field, polynomial, curve, or family
enumeration calls.

## 9. Literature/source grades

- Bergström, Faber, and van der Geer,
  [*Siegel Modular Forms of Genus 2 and Level 2: Cohomological Computations and
  Conjectures*](https://arxiv.org/abs/0803.0917): BFG Conjecture 8.1 and the
  explicitly expected nonregular Eisenstein continuation.
- Rösner, dissertation, Theorem 5.13, pp. 97--98:
  [semisimplified inner/endoscopic theorem](https://sites.math.unt.edu/~schmidt/dimension_formulas/papers/2016_Dissertation_Roesner_final.pdf).
- Shmakov, dissertation, Theorem 4.6.4 and Theorems 4.6.6--4.6.8:
  [inner/endoscopic theorem and the one-Tate Eisenstein
  discrepancy](https://openscholar.uga.edu/nanna/record/1979/files/dissertation.pdf).
- Bergström--Cléry,
  [arXiv:2309.04388v2](https://arxiv.org/abs/2309.04388), Theorem 5.3 and
  Remark 5.4: regular isotypical formula and conditional `k=3` continuation.
- Cléry--van der Geer,
  [arXiv:2605.13300](https://arxiv.org/abs/2605.13300): unconditional
  covariant/valuation structure and `A_2[w]=A_2[2]/S5`, but no computed
  `(12,3)` `S5`-isotypical dimension.
- [Official Siegel modular-form data query](https://smf.compositio.nl/api/Entries/2/2?j=12&k=3&l=0):
  frozen isotypical corroboration only; never queried by the producer.

No external novelty claim is made. No motivic isomorphism, compatible system,
RH/GRH implication, number-field transfer, or global Euler-product statement
is asserted.
