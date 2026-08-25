# The marked `chi_(0,3)` trace: exact theorem and literature reconciliation

**Status:** proved on this branch. The exact B3 character-sum theorem and the
marked-stack adapter give

\[
 \mathbb E[\chi_{0,3}(U_D)]=\frac{q^4-2q-1}{q^6},
 \qquad T_{0,3}(q)=q^4-2q-1
\]

for every odd prime power. The primary-source audit still finds no printed
all-\(q\) marked theorem in the cited papers; the internal proof and the
literature verdict are deliberately separate claims.

**Scope:** monic squarefree quintics, equivalently genus-two curves with one
marked rational Weierstrass point, over every finite field of odd
characteristic.  Nothing here concerns number-field \(L\)-functions, RH, or
GRH.

**Exact local dependencies:**

- `function_field/GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER.md`;
- `function_field/GENUS2_HIGH_WEIGHT_CHANNEL_PROBE.md`;
- `function_field/GENUS2_B3_PRIMITIVE_TRACE_AVERAGE.md`;
- their source-locked JSON payloads and focused producers.

**What was actually run:** a bounded exact-rational reconciliation, a
line-by-line independent audit of the B3 proof, the three frozen controls
\(q=3,5,7\), and a primary-source audit. The reconciliation replay enumerates
no finite field, polynomial family, curve, cohomology group, or modular form.

The exact mixed trace identity isolated by the literature bridge is now a
theorem as well:

\[
 \boxed{\mathcal M_{33}(q)=-q^4-q^2}
\]

It follows from the proved marked trace and the published unmarked trace via
the exact identity in Section 3.

## 1. The three moduli problems must not be conflated

Let \(\mathcal M_2\) be the stack of smooth genus-two curves.  There are two
different one-point covers in the cited literature:

1. \(\mathcal M_{2,1}\), where an arbitrary point of the curve is marked;
2. \(\mathcal M_2(w^1)\), where a Weierstrass point is marked.

Bergström's paper on pointed hyperelliptic curves primarily computes the first
kind.  Bergström--Faber--van der Geer define the second kind explicitly in
Section 2 of their level-two paper.  The quintic family in this repository is
the second kind:

\[
 \mathcal W_2^W(\mathbf F_q)
 \simeq
 \mathcal H_5(q)//\widetilde G(q),
 \qquad |\widetilde G(q)|=q(q-1).
\]

Consequently the stack adapter proves, for the weight-six character
\(\chi_{(0,3)}=V_{(3,3)}\),

\[
 \boxed{
 T_{0,3}(q)
 =\operatorname{Tr}\!\left(F_q,e_c(\mathcal M_2(w^1),V_{(3,3)})\right)
 ={q^3\over q(q-1)}
 \sum_{D\in\mathcal H_5(q)}\chi_{(0,3)}(U_D).
 }
\]

This closes the previously open factor-of-two and hyperelliptic-involution
convention.  It does not evaluate the trace.

## 2. What is already published

### The unmarked channel

For odd characteristic, Bergström's Section 11.1 connects the polynomial
finite-field counts to compactly supported local-system Frobenius traces.
Theorem 11.6 gives

\[
 e_c(\mathcal M_2,V_{(3,3)})=-\mathbb L-1.
\]

With the paper's geometric-Frobenius convention this imports the unmarked
trace

\[
 \boxed{
 \mathcal U_{33}(q)
 :=\sum_{[C]\in\mathcal M_2(\mathbf F_q)}
 {\operatorname{Tr}(F_q\mid V_{(3,3),C})\over|\operatorname{Aut}_q(C)|}
 =-q-1.
 }
\]

The December 2025 author erratum corrects Example 7.10 in that paper.  It does
not list Theorem 11.6 among the altered statements; any reconstruction of its
proof should nevertheless use the corrected Example 7.10 formula.

### The marked level-two paper

Bergström--Faber--van der Geer define \(\mathcal M_2(w^1)\), and Section 5
gives the exact finite-field point-count expression from which its traces can
be computed.  This is the right geometric setting.  It is not, however, a
printed all-\(q\) theorem for the trace above:

- their field set is explicitly bounded by \(q\le 37\);
- Section 5.3 says that the non-Eisenstein pieces are identified
  conjecturally;
- Section 9 reports a numerical Euler-characteristic check for the ambient
  \(\mathcal A_2(w^1)\), not an all-field trace theorem for
  \(\mathcal M_2(w^1)\);
- the example table is for \(\mathcal A_2[2]\), not
  \(\mathcal M_2(w^1)\), and the 2025 author erratum changes the
  \(V_{(3,3)}\) row by an additional constant term \(-15\).

Thus the level-two paper strongly corroborates the route, but its printed
tables do not certify \(T_{0,3}(q)=q^4-2q-1\) for every odd prime power.

## 3. Exact reduction to one mixed ramification trace

For a genus-two curve \(C\), let

\[
 R_1(C)=\#\{\text{rational Weierstrass points of }C\}.
\]

In Bergström's Appendix, \(r_1(C)\) counts the rational base points of the
hyperelliptic map whose fibres are unramified.  Definition 12.1 therefore gives
the exact identity

\[
 R_1(C)=|\mathbf P^1(\mathbf F_q)|-r_1(C)=q+1-r_1(C).
\]

Define the mixed trace isolated by the original reconciliation:

\[
 \mathcal M_{33}(q)
 :=\sum_{[C]\in\mathcal M_2(\mathbf F_q)}
 {r_1(C)\operatorname{Tr}(F_q\mid V_{(3,3),C})
  \over|\operatorname{Aut}_q(C)|}.
\]

Taking the groupoid cardinality of the forgetful fibre
\(\mathcal M_2(w^1)\to\mathcal M_2\) gives

\[
 \begin{aligned}
 T_{0,3}(q)
 &=\sum_{[C]}{R_1(C)\operatorname{Tr}(F_q\mid V_{(3,3),C})
                  \over|\operatorname{Aut}_q(C)|}\\
 &=(q+1)\mathcal U_{33}(q)-\mathcal M_{33}(q)\\
 &=-(q+1)^2-\mathcal M_{33}(q).
 \end{aligned}
\]

It follows, by exact polynomial arithmetic, that

\[
 \boxed{
 T_{0,3}(q)=q^4-2q-1
 \quad\Longleftrightarrow\quad
 \mathcal M_{33}(q)=-q^4-q^2.
 }
\]

This reduction was narrower than the earlier `B3-PRIMITIVE-TRACE-AVERAGE`
handoff: the entire channel became one named mixed ramification trace with a
two-term target. The B3 theorem now closes both formulations.

## 4. Branch-local proof and independent audit

`GENUS2_B3_PRIMITIVE_TRACE_AVERAGE.md` proves, for every odd prime power,

\[
 \sum_{D\in\mathcal H_5(q)}b_D^3
 =q(q-1)(4q^6-9q^5+7q^4+8q^3-12q^2-9q-1).
\]

Combining this with the exact Weyl-character identity

\[
 \chi_{0,3}
 =\frac{b_D^3}{q^3}-\frac{b_D^2}{q^2}
  -\frac{2a_D^2b_D}{q^2}-\frac{b_D}{q}
  +\frac{3a_D^2}{q}
\]

and the four established lower moments gives

\[
 \mathbb E[\chi_{0,3}(U_D)]=\frac{q^4-2q-1}{q^6}.
\]

The proof evaluates finite sign inventories for all seven primitive conductor
types, retains every even-exponent deletion Euler factor, applies polynomial
Möbius inversion, and sums an exhaustive 23-signature partition of the
\(q^6\) ordered quadratic triples.

The independent audit reconstructed the \(Sp(4)\) Weyl character; derived the
three sign inventories and all seven \(p_1,p_2\) aggregates separately; checked
all 23 signature weights and every \(C_1,C_3,C_5,S_5\) polynomial; and matched
the symbolic factorization and exhaustive \(q=3,5,7\) controls. A direct
\(\mathbf F_7\) reconstruction of all 13,573 distinct degree-six products also
matched every row and the total \(14,205,744\). No proof defect was found.

The source-locked B3 certificate has payload SHA-256
`e8001e46712db6d991286f5ea02eca62d0a58a43b20eaad146d30ca539e952dd`.

## 5. Why Bergström's Appendix does not supply this proof

Lemma 12.8 identifies the information in **all** \(u_g\)'s of degree at most
\(N\) with all \(b_\mu c_\nu\) averages of weight at most \(N\).  Remark 12.9
adds the equivalent mixed coordinates \(a_\lambda r_\xi\).  Our
\(\mathcal M_{33}\) lies in this language.

The quantifier "all" is load-bearing.  Section 7.3 states explicitly that the
paper cannot compute every degree-six \(u_g\); it computes only the general
cases needed for the ordinary \(a_\lambda\) moments.  Therefore the Appendix
is a coordinate equivalence, not an evaluation of the mixed marked channel.
The published results for arbitrary pointed curves must not be promoted to a
result for a marked ramification point.

Two exact routes were identified:

1. Decompose \(r_1\operatorname{Tr}V_{(3,3)}\) into the Appendix's \(u_g\)
   coordinates, identify the non-general degree-six terms, supply their
   genus-zero and genus-one base cases, and apply Theorem 4.12. This remains an
   unexecuted independent alternative.
2. Evaluate the \((p_1,p_2)\) and deletion-character averages across the
   frozen 23 B3 signatures. This route is complete and independently audited.

The completed second route proves the scalar identity without broad
finite-field enumeration. The Appendix route could still provide a useful
cohomological cross-check.

## 6. Finite controls and claim boundary

The locked \(q=3,5,7\) rows give

| \(q\) | \(T_{0,3}(q)\) | implied \(\mathcal M_{33}(q)\) |
|---:|---:|---:|
| 3 | 74 | -90 |
| 5 | 614 | -650 |
| 7 | 2386 | -2450 |

These agree with \(-q^4-q^2\). They are exact regression checks, not inputs to
the all-field proof.

The strongest justified verdict is therefore:

> The marked trace is proved on this branch by exact character-sum algebra and
> the marked-stack normalization. It is not a theorem imported from the cited
> tables. The literature bridge independently turns it into the exact mixed
> ramification trace \(\mathcal M_{33}(q)=-q^4-q^2\).

No novelty claim is made.  A publication-level novelty assessment would need
an expert review of later level-two and hyperelliptic-local-system literature.

## 7. Primary-source ledger

1. Jonas Bergström, *Equivariant counts of points of the moduli spaces of
   pointed hyperelliptic curves*,
   [arXiv:math/0611813](https://arxiv.org/abs/math/0611813), especially
   Section 7.3, Section 11.1, Theorem 11.6, Definition 12.1, Lemma 12.8,
   and Remark 12.9.  Audited arXiv v2 PDF SHA-256:
   `12457527533aa0898375b5085c29cd0dec88e77ef4612a8810baac01ba92d5cd`.
2. Jonas Bergström, Carel Faber, Gerard van der Geer, *Siegel modular forms
   of genus 2 and level 2: cohomological computations and conjectures*,
   [arXiv:0803.0917](https://arxiv.org/abs/0803.0917), especially Sections
   2, 5.1, 5.3, and 9.  Audited PDF SHA-256:
   `f6294c69e2cafe16b4b0dc1ba1692a46813ba6e467e546aa548442d1a4f2a19e`.
3. Jonas Bergström, author erratum dated 2 December 2025,
   [official PDF](https://www.su.se/download/18.1f09f4df19a7bbe0dfd6a83e/1764771423396/Erratum.pdf).
   Audited PDF SHA-256:
   `b064eef272d63a2a9b604647d25a346b825f48cba430399c14b144d477af16a3`.

The hashes identify the exact documents inspected.  They are provenance
records, not a network replay performed by the local checker.

## Replay

From the repository root:

```text
python research/l-families/atlas/function_field/genus2_chi03_stack_trace_reconciliation.py --check research/l-families/atlas/function_field/genus2_chi03_stack_trace_reconciliation.json
python -O research/l-families/atlas/function_field/genus2_chi03_stack_trace_reconciliation.py --check research/l-families/atlas/function_field/genus2_chi03_stack_trace_reconciliation.json
python -m unittest tests.test_genus2_chi03_stack_trace_reconciliation -v
python -O -m unittest tests.test_genus2_chi03_stack_trace_reconciliation -v
```
