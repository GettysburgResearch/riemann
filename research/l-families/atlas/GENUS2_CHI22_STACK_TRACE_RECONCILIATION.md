# The marked `chi_(2,2)` trace: exact theorem and literature reconciliation

**Status:** proved on this branch. The exact M22 character-sum theorem and the
marked-stack adapter give

\[
 \mathbb E[\chi_{2,2}(U_D)]
   =\frac{2q^3-q^2-2q-2}{q^6},
 \qquad
 T_{2,2}(q)=2q^3-q^2-2q-2
\]

for every odd prime power. The primary-source audit finds a printed theorem
for the corresponding **unmarked** local system, but no printed all-\(q\)
marked-Weierstrass theorem or mixed ramification identity in the sources
audited here. The branch proof and the literature verdict are separate claims.

**Scope:** monic squarefree quintics, equivalently genus-two curves with one
marked rational Weierstrass point, over every finite field of odd
characteristic. Nothing here concerns number-field \(L\)-functions, RH, or
GRH.

**Exact local dependencies:**

- `function_field/GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER.md`;
- `function_field/GENUS2_B3_PRIMITIVE_TRACE_AVERAGE.md`;
- `function_field/GENUS2_M22_TRIANGULAR_TRACE_AVERAGE.md`;
- their source-locked JSON payloads and focused producers.

**What was actually run:** a bounded exact-integer reconciliation of the three
packets, the polynomial forgetful-fibre identities, and a primary-source
audit. The replay enumerates no finite field, polynomial family, curve,
cohomology group, or modular form.

## 1. Character notation and the three moduli problems

The project character is written in fundamental-weight coordinates. The
marked-stack adapter proves the exact conversion

\[
 \chi_{(2,2)}
 \quad\longleftrightarrow\quad
 (4,2)\text{ in the }e\text{-basis}
 \quad\longleftrightarrow\quad
 V_{(4,2)}
\]

in the notation of the audited papers. Its local-system weight is
\(4+2=6\), and the central character is even.

Three different stacks must not be conflated:

1. \(\mathcal M_2\): a genus-two curve with no marked point;
2. \(\mathcal M_{2,1}\): a genus-two curve with one arbitrary marked point;
3. \(\mathcal M_2(w^1)\): a genus-two curve with one marked Weierstrass
   point.

Bergström's pointed-hyperelliptic paper computes the first two kinds of
information. Bergström--Faber--van der Geer explicitly define the third kind
in Section 2. The monic squarefree quintic family in this repository models
the third stack:

\[
 \mathcal M_2(w^1)(\mathbf F_q)
 \simeq \mathcal H_5(q)//\widetilde G(q),
 \qquad |\widetilde G(q)|=q(q-1).
\]

Consequently the adapter proves

\[
 \boxed{
 T_{2,2}(q)
 =\operatorname{Tr}\!\left(
   F_q,e_c(\mathcal M_2(w^1),V_{(4,2)})
  \right)
 ={q^3\over q(q-1)}
 \sum_{D\in\mathcal H_5(q)}\chi_{(2,2)}(U_D).
 }
\]

This fixes the stack measure, Tate normalization, and hyperelliptic
involution. It does not by itself evaluate the trace.

## 2. What is already published

### 2.1 The unmarked channel

Bergström uses geometric Frobenius in Section 2. Section 11.1 explains the
polynomial finite-field trace bridge, and Theorem 11.6 prints

\[
 e_c(\mathcal M_2,V_{(4,2)})=\mathbb L^3.
\]

The paper identifies \(\mathbb L=\mathbf Q_\ell(-1)\), whose geometric
Frobenius trace is \(q\). Thus, for every odd prime power in the paper's
finite-field calculation,

\[
 \boxed{
 \mathcal U_{42}(q)
 :=\sum_{[C]\in\mathcal M_2(\mathbf F_q)}
 {\operatorname{Tr}(F_q\mid V_{(4,2),C})
  \over |\operatorname{Aut}_q(C)|}
 =q^3.
 }
\]

The December 2025 author erratum corrects Example 7.10 of that paper. It
does not list Theorem 11.6 among the altered statements.

### 2.2 The arbitrary-point channel is not the marked-Weierstrass channel

The forgetful fibre of \(\mathcal M_{2,1}\to\mathcal M_2\) has
\(\#C(\mathbf F_q)=q+1-a_1(C)\) rational objects. Therefore its pulled-back
\(V_{(4,2)}\) trace is

\[
 \mathcal A_{42}(q)
 =(q+1)\mathcal U_{42}(q)
 -\sum_{[C]}{a_1(C)\operatorname{Tr}(F_q\mid V_{(4,2),C})
             \over|\operatorname{Aut}_q(C)|}.
\]

The cross term has odd central weight. The central hyperelliptic
\(\mu_2\)-inertia therefore acts nontrivially on the tensor local system, so
its stack cohomology vanishes; equivalently, the weighted quadratic-twist
descent cancels. Hence

\[
 \boxed{\mathcal A_{42}(q)=q^4+q^3.}
\]

This exact consequence is useful as a firewall: it is not the desired
marked-Weierstrass trace.

### 2.3 What the level-two paper does and does not print

Bergström--Faber--van der Geer define \(\mathcal M_2(w^1)\), and Section 5
gives the exact finite point-count machinery for its level-two setting. This
is the right geometry, but it does not print the all-field theorem above:

- the computation is explicitly for odd \(q\le 37\);
- the later non-Eisenstein and endoscopic identifications are conjectural;
- Section 9 checks numerical Euler characteristics of the ambient
  \(\mathcal A_2(w^1)\), not all-field Frobenius traces on
  \(\mathcal M_2(w^1)\);
- the example row for \(V_{(4,2)}\) is for the ambient full-level stack
  \(\mathcal A_2[2]\), not \(\mathcal M_2(w^1)\).

The 2025 erratum prints the corrected ambient row

\[
 e_c(\mathcal A_2[2],V_{(4,2)})
 =-45\mathbb L^3+45-S[\Gamma_2[2],(2,5)].
\]

It remains an ambient, conjectural-table statement and does not import the
marked curve-stack polynomial.

## 3. Exact reduction to one mixed ramification trace

For a genus-two curve \(C\), let \(R_1(C)\) be the number of rational
Weierstrass points. Bergström's Definition 12.1 lets \(r_1(C)\) count the
rational base points of the hyperelliptic map with unramified fibre. Hence

\[
 R_1(C)=|\mathbf P^1(\mathbf F_q)|-r_1(C)=q+1-r_1(C).
\]

Define

\[
 \mathcal M_{42}(q)
 :=\sum_{[C]\in\mathcal M_2(\mathbf F_q)}
 {r_1(C)\operatorname{Tr}(F_q\mid V_{(4,2),C})
  \over|\operatorname{Aut}_q(C)|}.
\]

Groupoid cardinality of the forgetful fibre
\(\mathcal M_2(w^1)\to\mathcal M_2\) gives

\[
 \begin{aligned}
 T_{2,2}(q)
 &=(q+1)\mathcal U_{42}(q)-\mathcal M_{42}(q)\\
 &=q^3(q+1)-\mathcal M_{42}(q).
 \end{aligned}
\]

Therefore

\[
 \boxed{
 T_{2,2}(q)=2q^3-q^2-2q-2
 \quad\Longleftrightarrow\quad
 \mathcal M_{42}(q)=q^4-q^3+q^2+2q+2.
 }
\]

This is the narrowest missing literature-side identity. It has mixed weight
\(6+1=7\), so it lies exactly in the \(a_\lambda r_\xi\) language of Remark
12.9.

## 4. What the branch proves

`GENUS2_M22_TRIANGULAR_TRACE_AVERAGE.md` first proves, for every odd prime
power, the exact moment

\[
 \sum_{D\in\mathcal H_5(q)}a_D^2b_D^2
 =q(q-1)(q+1)
  (5q^5-19q^4+29q^3-5q^2-21q-3).
\]

Its pointwise triangular identity gives

\[
 R_{22}=\chi_{0,3}+\chi_{2,2}
 =\frac{a_D^2b_D^2}{q^3}
  -\frac{3a_D^2b_D}{q^2}
  -\frac{a_D^4}{q^2}
  +\frac{5a_D^2}{q}-1.
\]

After the lower moments are substituted, the independently proved B3 packet
supplies
\(\mathbb E[\chi_{0,3}]=(q^4-2q-1)/q^6\). Exact subtraction yields

\[
 \mathbb E[\chi_{2,2}]
 =\frac{2q^3-q^2-2q-2}{q^6}.
\]

The marked-stack adapter then proves the displayed \(T_{2,2}\) theorem, and
the published unmarked theorem proves the displayed \(\mathcal M_{42}\)
identity as an exact consequence. No interpolation is used.

## 5. Why the Appendix is a reduction, not a published proof

Lemma 12.8 says that knowing **all** \(u_g\)'s of degree at most \(N\) is
equivalent to knowing all \(b_\mu c_\nu\) averages of weight at most \(N\).
Remark 12.9 adds the equivalent mixed coordinates \(a_\lambda r_\xi\).
Thus \(\mathcal M_{42}\) is in the published coordinate language.

The quantifier "all" is load-bearing. Section 7.3 explicitly says that the
paper cannot compute every degree-six \(u_g\); it computes the general cases
needed for the ordinary \(a_\lambda\) moments. The printed arbitrary-point
results likewise do not select a ramification point. Therefore the Appendix
does not evaluate \(\mathcal M_{42}\) or \(T_{2,2}\).

A direct source-locked alternative proof could decompose
\(r_1\operatorname{Tr}V_{(4,2)}\) into the Appendix's \(u_g\) coordinates,
isolate every degree-six or degree-seven term not already computed (including
the genuinely new degree-seven general terms), provide the genus-zero and
genus-one base cases, and apply Theorem 4.12. That route is precise but is not
executed here. The branch instead closes the trace through the M22/B3
signature algebra.

## 6. Exact specializations and claim boundary

The reconciliation polynomial gives the following exact checks:

| \(q\) | \(\mathcal U_{42}\) | \(\mathcal A_{42}\) | \(T_{2,2}\) | \(\mathcal M_{42}\) |
|---:|---:|---:|---:|---:|
| 3 | 27 | 108 | 37 | 71 |
| 5 | 125 | 750 | 213 | 537 |
| 7 | 343 | 2744 | 621 | 2123 |

These are specializations and regression checks, not inputs to the all-field
proof.

The strongest justified verdict is:

> Bergström's Theorem 11.6 publishes the unmarked trace
> \(\mathcal U_{42}=q^3\). The marked trace is proved on this branch by exact
> M22/B3 character-sum algebra plus the marked-stack normalization. Relative
> to the audited sources, it is not a table import; it is exactly equivalent
> to the branch consequence
> \(\mathcal M_{42}=q^4-q^3+q^2+2q+2\).

No novelty claim is made. A publication-level novelty assessment would need
an expert review of later level-two and hyperelliptic-local-system literature.

## 7. Primary-source ledger

1. Jonas Bergström, *Equivariant counts of points of the moduli spaces of
   pointed hyperelliptic curves*,
   [arXiv:math/0611813](https://arxiv.org/abs/math/0611813), especially
   Section 2 (PDF pp. 3--4), Section 7.3 (p. 17), Section 11.1 (p. 26),
   Theorem 11.6 and Definition 12.1 (p. 29), Lemma 12.8 (pp. 30--31), and
   Remark 12.9 (p. 31). Audited arXiv v2 PDF SHA-256:
   `12457527533aa0898375b5085c29cd0dec88e77ef4612a8810baac01ba92d5cd`.
2. Jonas Bergström, Carel Faber, Gerard van der Geer, *Siegel modular forms
   of genus 2 and level 2: cohomological computations and conjectures*,
   [arXiv:0803.0917](https://arxiv.org/abs/0803.0917), especially Sections
   2--3 (PDF pp. 2--3), Section 5 (pp. 6--8), and Sections 9--10 (p. 12).
   Audited arXiv v2 PDF SHA-256:
   `f6294c69e2cafe16b4b0dc1ba1692a46813ba6e467e546aa548442d1a4f2a19e`.
3. Jonas Bergström, author erratum dated 2 December 2025,
   [official PDF](https://www.su.se/download/18.1f09f4df19a7bbe0dfd6a83e/1764771423396/Erratum.pdf).
   Audited PDF SHA-256:
   `b064eef272d63a2a9b604647d25a346b825f48cba430399c14b144d477af16a3`.

The hashes identify the exact documents inspected. They are provenance
records, not a network replay performed by the local checker.

## Replay

From the repository root:

```text
python research/l-families/atlas/function_field/genus2_chi22_stack_trace_reconciliation.py --check
python -O research/l-families/atlas/function_field/genus2_chi22_stack_trace_reconciliation.py --check
python -m unittest tests.test_genus2_chi22_stack_trace_reconciliation -v
python -O -m unittest tests.test_genus2_chi22_stack_trace_reconciliation -v
```
