# Integrated packet: finite Robin foundations

**Packet status:** integrated, reviewed finite mathematics  
**Global status:** RH remains unsolved  
**Primary source A:** PR [#24](https://github.com/gfreund123/riemann/pull/24) at `ae477857d036fc182adb8db4e34e846fde7931b3`  
**Primary source B:** PR [#40](https://github.com/gfreund123/riemann/pull/40) at `36148418ee5c6ce1c294f66a0fc75a258810f796`  
**Review evidence:** `reports/gpt56-08/2026-08-01-pre-public-review-prs-4-43.md` at review-source commit `d1cf0320fb80dbe4d39e0e36d1c8af69bdcf3ff6`  
**Review verdicts:** #24 `VERIFIED`; #40 `VERIFIED`  
**Source-file status:** the frozen source files retain their original `PROPOSED` labels; the later exact-SHA review accepted the mathematics in the finite scope recorded here.

## Packet summary

This packet establishes three layers:

1. an independently reproduced finite Robin barrier through \(5582\);
2. a constructive complete reduction of every hypothetical Robin counterexample to a consecutive-prime, nonincreasing-exponent integer;
3. an exact shared-budget dynamic-program upper envelope for a bounded canonical tail.

The first two layers identify the correct infinite search domain. The third improves finite pruning. None proves Robin’s inequality for every integer.

---

## 1. Exact finite barrier

Write

\[
I(n)=\frac{\sigma(n)}n.
\]

The exact finite facts are:

1. the unique maximum of \(I(n)\) for \(1\le n\le5040\) is

   \[
   I(5040)=\frac{403}{105};
   \]

2. the unique maximum for \(5041\le n\le5582\) is

   \[
   I(5460)=\frac{224}{65};
   \]

3. independent integer/dyadic interval arithmetic proves

   \[
   e^\gamma\log\log5041-\frac{224}{65}>0,
   \]

   \[
   e^\gamma\log\log5582-\frac{403}{105}<0,
   \]

   \[
   e^\gamma\log\log5583-\frac{403}{105}>0.
   \]

Consequently:

- no Robin counterexample lies in \([5041,5582]\);
- \(5583\) is the first integer where the increasing threshold \(e^\gamma\log\log n\) exceeds \(403/105\).

### Finite arithmetic proof extract

For every \(n\le5582\), the source computation factors \(n\) by trial division and forms

\[
\sigma(n)
=
\prod_{p^a\parallel n}
\frac{p^{a+1}-1}{p-1}
\]

with exact integers. Two abundancy ratios are compared by integer cross multiplication, never by floating division.

The maxima are checked directly:

\[
5040=2^4\,3^2\,5\,7,
\qquad
\sigma(5040)=31\cdot13\cdot6\cdot8=19344,
\]

so

\[
\frac{19344}{5040}=\frac{403}{105};
\]

and

\[
5460=2^2\,3\,5\,7\,13,
\qquad
\sigma(5460)=7\cdot4\cdot6\cdot8\cdot14=18816,
\]

so

\[
\frac{18816}{5460}=\frac{224}{65}.
\]

A separately structured divisor-addition sieve agrees with every \(\sigma(n)\) through \(5582\) in the source test suite.

### Transcendental enclosure extract

The source uses:

- a positive atanh series with rational tail for logarithms;
- harmonic-number upper and lower bounds for Euler’s constant;
- a positive Taylor series with geometric tail for exponentials;
- integer endpoints over a common dyadic denominator.

No binary floating-point or `Decimal` transcendental operation is part of this finite certificate.

The integration pass reviewed the theorem and checker semantics but did not rerun the entire finite enumeration.

### Source files

- `claims/theorems/T-2001-independent-robin-finite-barrier.md`
- `claims/lemmas/L-2001-atanh-log-enclosure.md`
- `claims/lemmas/L-2002-euler-gamma-harmonic-enclosure.md`
- `claims/lemmas/L-2003-exp-taylor-enclosure.md`
- `experiments/X-2001-independent-robin-barrier/`

---

## 2. Canonical support and exponent dominance

### Lemma

Let

\[
n=\prod_{i=1}^k q_i^{a_i},
\qquad q_1<\cdots<q_k,
\]

and let

\[
b_1\ge b_2\ge\cdots\ge b_k
\]

be the same exponent multiset arranged in nonincreasing order. Let \(p_i\) be the \(i\)-th prime and define

\[
\mathcal H(n)=\prod_{i=1}^k p_i^{b_i}.
\]

Then

\[
\mathcal H(n)\le n,
\qquad
I(\mathcal H(n))\ge I(n).
\]

### Proof

It is enough first to remove one exponent inversion. Let \(p<q\) and \(0\le a<b\). Compare

\[
x=mp^a q^b,
\qquad
x'=mp^b q^a,
\]

with \(m\) coprime to \(pq\). Then

\[
\frac{x'}x
=
\left(\frac pq\right)^{b-a}<1.
\]

For \(r\ge0\), put

\[
F_r(t)=1+t+\cdots+t^r.
\]

The local abundancy factors are

\[
F_a(1/p)F_b(1/q)
\quad\text{and}\quad
F_b(1/p)F_a(1/q).
\]

For \(b>a\), the ratio

\[
G(t)=\frac{F_b(t)}{F_a(t)}
\]

is strictly increasing for \(t>0\). Indeed,

\[
G'(t)F_a(t)^2
=
F_b'(t)F_a(t)-F_b(t)F_a'(t)
=
\sum_{i=0}^b\sum_{j=0}^a(i-j)t^{i+j-1}.
\]

The terms with \(0\le i,j\le a\) cancel in pairs; the remaining terms have \(a+1\le i\le b\) and \(0\le j\le a\), hence \(i-j>0\). Since \(1/p>1/q\), moving the larger exponent to the smaller prime increases the local abundancy factor and decreases the integer.

Repeated inversion removal sorts the exponents. Replacing the sorted support \(q_i\) by the first \(k\) primes \(p_i\le q_i\) again decreases the integer, while

\[
I(r^{b_i})=1+r^{-1}+\cdots+r^{-b_i}
\]

decreases as the real variable \(r>1\) increases. Multiplication proves both inequalities.

### Source

- `claims/lemmas/L-2005-canonical-exponent-support-dominance.md`
- source blob `07418f6d67b5b5138b54720719d5a73a9dc4786a`

---

## 3. Complete canonical reduction for Robin search

Call

\[
h=\prod_{i=1}^k p_i^{b_i},
\qquad
b_1\ge\cdots\ge b_k\ge1,
\]

a Hardy–Ramanujan canonical integer.

### Theorem

The following are equivalent:

1. some \(n>5040\) satisfies

   \[
   I(n)\ge e^\gamma\log\log n;
   \]

2. some Hardy–Ramanujan canonical \(h>5040\) satisfies the same inequality.

Moreover, from any violating \(n\), the explicit transform \(h=\mathcal H(n)\) is itself a violation.

### Proof

The second statement trivially implies the first. Assume \(n\) violates Robin. The finite barrier gives \(n\ge5583\). Let \(h=\mathcal H(n)\). Then

\[
h\le n,\qquad I(h)\ge I(n).
\]

First \(h>5040\). Otherwise the finite maximum gives

\[
I(h)\le\frac{403}{105},
\]

whereas

\[
I(h)\ge I(n)
\ge e^\gamma\log\log n
\ge e^\gamma\log\log5583
>\frac{403}{105},
\]

a contradiction.

Since \(h\le n\) and \(\log\log x\) increases on this range,

\[
e^\gamma\log\log h
\le e^\gamma\log\log n.
\]

Therefore

\[
I(h)\ge I(n)
\ge e^\gamma\log\log n
\ge e^\gamma\log\log h.
\]

Thus \(h\) is a canonical Robin counterexample.

### Exact boundary

This reduces the complete search domain but does not make it finite. The canonical class contains every support size and unbounded exponent vectors.

The final statement “a Robin violation disproves RH” uses Robin’s classical equivalence theorem as an imported source-qualified result. The canonical reduction itself does not depend on that equivalence.

### Source

- `claims/theorems/T-2002-hardy-ramanujan-completeness.md`
- source blob `36ebbfc2fe6db478de50d6b4a3ec563b2b6dbff4`

---

## 4. Nested prefix-level encoding for bounded tails

Fix consecutive tail primes

\[
q_1<\cdots<q_n
\]

and a nonincreasing exponent vector

\[
A\ge b_1\ge\cdots\ge b_n\ge1.
\]

For each level \(r=2,\ldots,A\), define

\[
\ell_r=\#\{i:b_i\ge r\}.
\]

Then

\[
n\ge\ell_2\ge\ell_3\ge\cdots\ge\ell_A\ge0.
\]

Conversely, every such nested sequence determines exactly one canonical tail via

\[
b_i
=
1+\#\{r\in\{2,\ldots,A\}:i\le\ell_r\}.
\]

Thus bounded canonical tails are in bijection with nested prefix lengths.

Put

\[
R=\prod_{i=1}^nq_i,
\qquad
Q_\ell=\prod_{i=1}^{\ell}q_i,
\]

and

\[
g_{i,r}
=
\frac{I(q_i^r)}{I(q_i^{r-1})}
=
\frac{q_i^{r+1}-1}{q_i(q_i^r-1)},
\qquad
G_{r,\ell}=\prod_{i=1}^{\ell}g_{i,r}.
\]

Then the exact factorizations are

\[
N_{\rm tail}
=
R\prod_{r=2}^{A}Q_{\ell_r},
\]

and

\[
I(N_{\rm tail})
=
I(R)\prod_{r=2}^{A}G_{r,\ell_r}.
\]

### Proof extract

At level \(r\), canonical monotonicity forces the indices with \(b_i\ge r\) to be an initial prefix. Reordering the finite product by levels gives one mandatory \(R\), and each optional level contributes \(Q_{\ell_r}\). The prime-power abundancy ratios telescope level by level, yielding the second factorization.

### Source

- `claims/lemmas/L-3501-canonical-tail-level-encoding.md`
- source blob `e7a5759e4f963aaa1ac679fde10991ba73ec8140`

---

## 5. Exact powered shared-budget envelope

### Setup

Let a fixed canonical prefix have:

- integer value \(P\);
- exact abundancy \(I_P\);
- last exponent \(A\).

Let the remaining consecutive primes be \(q_1,\ldots,q_n\), with global integer bound \(B\). Put

\[
M=\left\lfloor\frac BP\right\rfloor,
\qquad
R=\prod_iq_i,
\qquad
M_0=\left\lfloor\frac MR\right\rfloor.
\]

Every completion has optional increment cost

\[
C(b)=\prod_iq_i^{b_i-1}\le M_0.
\]

Choose integers \(a\ge0\), \(d\ge1\). For every level and prefix length define the positive rational weight

\[
W_{r,\ell}
=
\frac{G_{r,\ell}^{\,d}}{Q_\ell^{\,a}}.
\]

Define the backward dynamic program

\[
V_{A+1}(m)=1,
\]

and

\[
V_r(m)
=
\max_{0\le\ell\le\min(m,n_r)}
W_{r,\ell}V_{r+1}(\ell).
\]

Let \(V=V_2(n)\) when \(A\ge2\), and \(V=1\) when \(A=1\).

### Theorem

Every bounded canonical completion satisfies

\[
I\!\left(P\prod_iq_i^{b_i}\right)^d
\le
\bigl(I_PI(R)\bigr)^d M_0^aV.
\]

Every object on the right is rational and is obtained by finite exact maximization. No logarithmic ordering, fractional power, or floating optimizer enters the proof object.

### Proof

By the nested-level encoding,

\[
C(b)=\prod_{r=2}^{A}Q_{\ell_r},
\qquad
J(b)=\prod_{r=2}^{A}G_{r,\ell_r}.
\]

Therefore

\[
\frac{J(b)^d}{C(b)^a}
=
\prod_{r=2}^{A}W_{r,\ell_r}.
\]

Backward induction on the level shows that every nested continuation from a previous prefix length \(m\) is bounded by \(V_r(m)\). Hence

\[
\frac{J(b)^d}{C(b)^a}\le V.
\]

Since \(C(b)\le M_0\),

\[
J(b)^d\le M_0^aV.
\]

Finally,

\[
I\!\left(P\prod_iq_i^{b_i}\right)
=
I_PI(R)J(b),
\]

which yields the stated inequality after raising to \(d\).

### Strict finite improvement control

The source includes a synthetic bounded subtree where the powered shared-budget envelope proves a ceiling below \(39/10\) while the product of separate exponent caps does not. This is an exact regression for the envelope, not a new Robin range.

### Source

- `claims/lemmas/L-3502-exact-powered-lagrange-tail-envelope.md`
- source blob `58b0a4b77df279228f554660139ae70cbaa78413`

---

## Dependencies and qualifications

### Native reviewed mathematics

The finite algebra in the statements and proofs above was independently reviewed at the exact source commits.

### Imported theorem

Robin’s global equivalence between RH and the strict inequality for every \(n>5040\) is not reproved here. It remains a named classical source interface.

### Computation status

- The finite \(n\le5582\) computation has exact integer/dyadic source artifacts.
- The review checked theorem and checker semantics without rerunning the full finite loop.
- The powered-envelope source artifact is a synthetic exact control.
- This packet does not import or claim the larger \(10^{54}\) or \(10^{100}\) traversal as an independently replayed result.

## Known exclusions and common misreadings

- Canonical does not mean colossally abundant.
- The transform proves existence of a canonical violator if any violator exists; it does not assert the original violator was canonical.
- A bounded-tail envelope is not a theorem about the unbounded canonical class.
- A stronger finite endpoint is not evidence that the infinite inequality holds.
- Search and verifier code sharing one transcendental kernel are not independent arithmetic backends.
- A certificate digest is provenance, not proof of an unavailable terminal stream.

## Why this packet matters

The arithmetic route now has a correct complete search domain and exact finite pruning language. This is a durable mathematical reduction independent of the success of any particular large scan.

## Exact next missing step

Prove an unbounded tail theorem, construct a complete infinite pruning argument, or find one exact violation. Extending the finite endpoint without crossing that quantifier is useful engineering but does not close the program.
