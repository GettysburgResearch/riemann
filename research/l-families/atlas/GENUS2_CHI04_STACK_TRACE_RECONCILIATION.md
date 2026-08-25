# Genus-two \(\chi_{(0,4)}\) marked-stack trace reconciliation

## Status

**PRIMARY-SOURCE RECONCILIATION COMPLETE.** The source-locked B4 packet proves,
for every odd prime power \(q\),

\[
 \left\langle\chi_{(0,4)}\right\rangle_q
   =-\frac{2q^2+1}{q^7},
 \qquad
 T_{0,4}(q)
   =\operatorname{Tr}\!\left(
      F_q,e_c(\mathcal M_2(w^1),V_{(4,4)})
    \right)
   =-(2q^2+1).
\]

The four primary sources audited here do **not** print or prove this all-field
marked-Weierstrass formula. They do, however, contain conjectural ambient
machinery whose correctly projected and boundary-subtracted prediction is
exactly \(-2\mathbb L^2-1\). Thus the new project proof is independent relative
to these sources, while the answer itself is structurally compatible with their
conjectures. No broader novelty claim is made.

This packet makes no finite-field sweep. Its replay uses exact polynomial,
finite-representation, and Laurent-character algebra only.

## 1. The five moduli problems must not be conflated

The notation is close enough to hide materially different fibres.

1. \(\mathcal M_2(w^1)\) parametrizes a smooth genus-two curve with one
   ordered Weierstrass point. Over \(\mathbf F_q\), the marked point must be
   rational. This is the target of the B4 theorem.
2. \(\mathcal M_{2,1}\) parametrizes a smooth genus-two curve with one
   arbitrary marked point. Its forgetful fibre over \(C\) is \(C(\mathbf F_q)\),
   not the rational ramification set of the hyperelliptic map.
3. \(\mathcal M_2\) is the unmarked smooth-curve stack.
4. \(\mathcal A_2(w^1)\) is the ambient stack of principally polarized
   abelian surfaces with one partial level-two label. It contains both the
   Jacobian locus \(\mathcal M_2(w^1)\) and a decomposable locus.
5. \(\mathcal A_2[2]\) carries a full level-two structure and an
   \(S_6\)-action. The quotient by the \(S_5\) fixing one label is
   \(\mathcal A_2(w^1)\). Forgetting the \(S_6\)-representation by taking its
   dimension is not the same operation as taking \(S_5\)-invariants.

Bergström--Faber--van der Geer define the last three level-two objects
explicitly in Section 2. Bergström's \(\mathcal H_{g,n}\), and the
\(\mathcal M_{2,n}\) used by Faber--van der Geer, have arbitrary marked curve
points instead.

## 2. What each primary source actually establishes

### Bergström 2006/2011

The Introduction and Section 7 state a weight-at-most-seven scope. Theorem
11.6 prints the unmarked local-system Euler characteristics only in weights
four and six:

\[
 (4,0),\ (3,1),\ (2,2),\qquad
 (6,0),\ (5,1),\ (4,2),\ (3,3).
\]

The pair \((4,4)\) has weight eight and is absent. Definition 12.1, Lemma
12.8, and Remark 12.9 introduce the ramification counts \(b_i,c_i,r_i\) and
show how bounded-weight information can be exchanged, but they do not
evaluate the missing weight-eight marked trace. Consequently this paper
neither prints \(e_c(\mathcal M_2,V_{(4,4)})\) nor the stronger marked class.

### Faber--van der Geer 2003

This paper treats level-one \(\mathcal A_2\), \(\mathcal M_2\), and
arbitrary-point \(\mathcal M_{2,n}\). It contains no \(w^1\) moduli problem.
Its Eisenstein theorem is stated for regular pairs \(l>m>0\). The authors say
that the displayed extension to nonregular pairs is expected, and explicitly
flag \(l=m>0\) with even \(m\) as an exceptional range with unexpected
\(L\)-function cancellations. The target \((l,m)=(4,4)\) lies exactly there.
The endoscopic contribution and resulting total formula are also labelled
conjectural. The finite-field counts are data for selected \(q\), not an
all-\(q\) theorem, and no \((4,4)\) row is printed.

The paper does print the level-one elliptic identities used in the exact
boundary calculation below:

\[
 e_c(\mathcal A_1,W_0)=\mathbb L,
 \qquad
 e_c(\mathcal A_1,W_r)=-S[r+2]-1
 \quad(r\ge2\text{ even}).
\]

### Bergström--Faber--van der Geer 2008

Section 2 defines \(\mathcal M_2(w^n)\), \(\mathcal A_2(w^n)\), and
\(\mathcal A_2[2]\), so this is the first audited source with the correct
marked-Weierstrass geometry. The logical strength of its subsequent results
must nevertheless be kept explicit:

- Theorem 4.2 and Theorem 4.4 prove the Eisenstein formulas for regular
  \((l,m)\). For \(l=m\), the substituted dimension convention is explicitly
  conjectural.
- Corollary 4.5 gives the \(\mathcal A_2(w^1)\) Eisenstein formula only for
  regular pairs.
- Section 5 computes exact traces with a computer for odd \(q\le37\). This is
  a bounded data set, not an all-field formula.
- Section 9 reports numerical Euler-characteristic checks on the ambient
  \(\mathcal A_2(w^1)\). A numerical Euler characteristic is a specialization
  at \(\mathbb L=1\), not an all-\(q\) Frobenius trace.
- Section 10 says its example rows are conjectural and based on numerical
  evidence. Its \((4,4)\) row is for \(\mathcal A_2[2]\), not
  \(\mathcal M_2(w^1)\).

### Bergström's 2025 erratum

The erratum corrects the full-level example to

\[
 e_c(\mathcal A_2[2],V_{(4,4)})
 =15\mathbb L^6-45\mathbb L^5+30
  +15\Phi_{4,6}-5\Phi_{4,12}.
\]

The original sign of \(15\Phi_{4,6}\) was negative. The corrected row remains
an example from the conjectural section and remains an ambient
\(\mathcal A_2[2]\) statement. The erratum does not add an all-\(q\)
\(\mathcal M_2(w^1)\) theorem.

## 3. Exact \(S_5\)-projection of the BFG ambient prediction

This section is a reconciliation of BFG's stated conjectural formulas, not a
replacement proof for them.

By the symmetric-group branching rule, an irreducible \(S_6\)-representation
has an \(S_5\)-fixed vector precisely for the partitions \([6]\) and
\([5,1]\), once in each case. Applied to BFG's notation,

\[
 \dim A^{S_5}=0,\quad
 \dim B^{S_5}=0,\quad
 \dim C^{S_5}=2,
\]

and

\[
 \dim (A')^{S_5}=0,\quad
 \dim (B')^{S_5}=1,\quad
 \dim (C')^{S_5}=1.
\]

The elementary modular-form dimensions needed at \((l,m)=(4,4)\) are

\[
 \dim S_{12}(\Gamma_0(2))=2,
 \qquad
 S_{12}(\Gamma_0(2))^{\mathrm{new}}=0,
 \qquad
 \dim S_{12}(\mathrm{SL}_2(\mathbf Z))=1,
\]

and \(S_4(\Gamma_0(2))=S_6(\Gamma_0(2))=0\). One direct check is that
\(M_{2k}(\Gamma_0(2))\) has dimension \(\lfloor k/2\rfloor+1\); at weight
twelve its two cusp forms are the two degeneracy images of the level-one
form.

With BFG's nonregular convention, the \(S_5\)-invariant Eisenstein prediction
is

\[
 e_{\mathrm{Eis}}(\mathcal A_2(w^1),V_{(4,4)})
 =1-2\mathbb L^5.
\]

Conjecture 8.3 contributes the \([6]\)-channel

\[
 \mathbb L^5(\mathbb L+1)=\mathbb L^6+\mathbb L^5.
\]

Conjecture 7.6 supplies no \(S_5\)-invariant cuspidal channel here: the only
possible \([5,1]\)-term uses
\(S_{12}(\Gamma_0(2))^{\mathrm{new}}=0\), while \([3^2]\) and \([1^6]\)
have no \(S_5\)-fixed vectors. Hence the ambient prediction is

\[
 e_c(\mathcal A_2(w^1),V_{(4,4)})
 \stackrel{\mathrm{BFG\ conj.}}{=}
 \mathbb L^6-\mathbb L^5+1.
\]

As a consistency check, forgetting the full \(S_6\)-action reconstructs the
erratum's corrected row. The \(+15\Phi_{4,6}\) term belongs to BFG's
representation \(A\), whose \(S_5\)-invariant multiplicity is zero. Thus the
erratum is essential for the full-level ledger but its changed sign does not
alter the one-label quotient.

## 4. Exact decomposable boundary

On the decomposable locus, a marked one of the six nonzero two-torsion points
distinguishes one elliptic component. Therefore

\[
 \mathcal A_{1,1}(w^1)\cong Y_0(2)\times\mathcal A_1.
\]

The restriction of the weight-eight local system is

\[
 V_{(4,4)}\big|_{\mathrm{SL}_2\times\mathrm{SL}_2}
 =\bigoplus_{r=0}^{4}
   (W_r\boxtimes W_r)\otimes\mathbb L^{4-r}.
\]

The producer verifies the equivalent Weyl-character identity exactly in a
two-variable Laurent ring:

\[
 \chi_{(0,4)}(x,y)=\sum_{r=0}^{4}\chi_r(x)\chi_r(y),
\]

where \(\chi_{(0,4)}\) is the fundamental-weight notation for the character
of \(V_{(4,4)}\).

The summand dimensions \(1,4,9,16,25\) total \(55\), the dimension of
\(V_{(4,4)}\), and the Tate twists make every summand have weight eight.

For \(Y_0(2)\), which has genus zero and two cusps,

\[
 e_c(Y_0(2),W_0)=\mathbb L-1,
 \qquad
 e_c(Y_0(2),W_2)=e_c(Y_0(2),W_4)=-2.
\]

The odd \(r\) terms vanish on the unmarked \(\mathcal A_1\) factor. The three
even contributions are therefore

\[
 \begin{array}{c|c}
 r&\text{contribution}\\ \hline
 0&\mathbb L^4(\mathbb L-1)\mathbb L
      =\mathbb L^6-\mathbb L^5,\\
 2&\mathbb L^2(-2)(-1)=2\mathbb L^2,\\
 4&(-2)(-1)=2.
 \end{array}
\]

Thus the boundary identity is exact:

\[
 e_c(\mathcal A_{1,1}(w^1),V_{(4,4)})
 =\mathbb L^6-\mathbb L^5+2\mathbb L^2+2.
\]

## 5. Reconciliation with the project theorem

Subtracting the exact boundary from the conjectural ambient prediction gives

\[
 \begin{aligned}
 e_c(\mathcal M_2(w^1),V_{(4,4)})
 &\stackrel{\mathrm{BFG\ conj.}}{=}
 (\mathbb L^6-\mathbb L^5+1)
 -(\mathbb L^6-\mathbb L^5+2\mathbb L^2+2)\\
 &=-2\mathbb L^2-1.
 \end{aligned}
\]

Its geometric-Frobenius trace is \(-(2q^2+1)\), exactly the theorem proved
independently in the source-locked B4 packet. The scientifically accurate
summary is therefore:

The B4 theorem establishes this all-field trace identity. It does not, by
itself, prove equality with \(-2\mathbb L^2-1\) in a motivic Grothendieck
group.

> The all-odd-prime-power marked trace is not printed or proved in the four
> audited primary sources. It is, however, the exact curve-open consequence
> of BFG's conjectural ambient level-two formalism after the correct
> \(S_5\)-projection and an exact decomposable-boundary subtraction.

This is a relative source statement, not a global novelty assessment. Later
literature has not been exhaustively audited here.

## 6. Primary-source ledger

1. Jonas Bergström, *Equivariant counts of points of the moduli spaces of
   pointed hyperelliptic curves*,
   [arXiv:math/0611813](https://arxiv.org/abs/math/0611813), especially the
   Introduction, Sections 2 and 7, Theorem 11.6, Definition 12.1, Lemma 12.8,
   and Remark 12.9. Audited arXiv v2 PDF SHA-256:
   `12457527533aa0898375b5085c29cd0dec88e77ef4612a8810baac01ba92d5cd`.
2. Carel Faber and Gerard van der Geer, *Sur la cohomologie des systèmes
   locaux sur les espaces des modules des courbes de genre 2 et des surfaces
   abéliennes*,
   [arXiv:math/0305094](https://arxiv.org/abs/math/0305094), especially
   Sections 1, 2, 4, 5, and 8. Audited arXiv v1 PDF SHA-256:
   `986f0f98303db367099ffa676fff0cbb19857e9ebd830082a4213c04cb053021`.
3. Jonas Bergström, Carel Faber, and Gerard van der Geer, *Siegel modular
   forms of genus 2 and level 2: cohomological computations and conjectures*,
   [arXiv:0803.0917](https://arxiv.org/abs/0803.0917), especially Sections
   2, 4, 5, and 9--10 and Conjectures 7.6 and 8.3. Audited arXiv v2 PDF
   SHA-256:
   `f6294c69e2cafe16b4b0dc1ba1692a46813ba6e467e546aa548442d1a4f2a19e`.
4. Jonas Bergström, author erratum dated 2 December 2025,
   [official PDF](https://www.su.se/download/18.1f09f4df19a7bbe0dfd6a83e/1764771423396/Erratum.pdf),
   p. 1. Audited PDF SHA-256:
   `b064eef272d63a2a9b604647d25a346b825f48cba430399c14b144d477af16a3`.

The hashes identify the exact documents inspected. They are provenance
records; the local checker performs no network replay.

## Replay

From the repository root:

```text
python research/l-families/atlas/function_field/genus2_chi04_stack_trace_reconciliation.py --check
python -O research/l-families/atlas/function_field/genus2_chi04_stack_trace_reconciliation.py --check
python -m unittest tests.test_genus2_chi04_stack_trace_reconciliation -v
python -O -m unittest tests.test_genus2_chi04_stack_trace_reconciliation -v
```
