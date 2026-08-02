# Integrated packet: finite Robin foundations

**Packet status:** integrated reviewed finite mathematics  
**Scope:** finite arithmetic barrier, complete structural reduction of hypothetical violations, and exact bounded-tail algebra; no proof over the unbounded canonical class  
**Global status:** RH remains unsolved  
**Primary source A:** PR [#24](https://github.com/gfreund123/riemann/pull/24) at `ae477857d036fc182adb8db4e34e846fde7931b3`  
**Primary source B:** PR [#40](https://github.com/gfreund123/riemann/pull/40) at `36148418ee5c6ce1c294f66a0fc75a258810f796`  
**Review evidence:** `reports/gpt56-08/2026-08-01-pre-public-review-prs-4-43.md` at `d1cf0320fb80dbe4d39e0e36d1c8af69bdcf3ff6`  
**Review verdict:** #24 `VERIFIED`; #40 `VERIFIED`  
**Source-file status:** the frozen source files retain their original `PROPOSED` labels; the later exact-SHA review accepted the mathematics only in the scopes recorded here.  
**Replay in this integration:** none; theorem and checker semantics were reviewed, but the finite enumeration and production computations were not rerun.

## Imported global source interface

The RH interpretation uses the classical theorem:

> Guy Robin, “Grandes valeurs de la fonction somme des diviseurs et hypothèse de Riemann,” *Journal de Mathématiques Pures et Appliquées* (9) **63** (1984), 187–213.

The imported interface is:

\[
\mathrm{RH}
\quad\Longleftrightarrow\quad
\sigma(n)<e^\gamma n\log\log n
\quad\text{for every integer }n>5040.
\]

Equivalently,

\[
\frac{\sigma(n)}n<e^\gamma\log\log n
\qquad(n>5040).
\]

This packet **does not reproduce Robin’s proof**. The equivalence is used only to interpret:

- one exact violation as an RH disproof; or
- a proof over every \(n>5040\) as an RH proof.

The finite barrier, canonical transform, and bounded-tail envelope below are native reviewed mathematics and do not require Robin’s equivalence for their internal validity.

## Packet contents

1. exact finite barrier through \(5582\);
2. canonical prime-support and exponent-order dominance;
3. complete reduction of every hypothetical violation to a Hardy–Ramanujan canonical integer;
4. nested prefix-level encoding of bounded canonical tails;
5. exact powered shared-budget envelope.

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

- no Robin violation lies in \([5041,5582]\);
- \(5583\) is the first integer where the increasing threshold \(e^\gamma\log\log n\) exceeds \(403/105\).

### Exact arithmetic extract

For every \(n\le5582\), the source factors \(n\) by trial division and forms

\[
\sigma(n)
=
\prod_{p^a\parallel n}
\frac{p^{a+1}-1}{p-1}
\]

with exact integers. Ratios are compared by integer cross multiplication.

The maxima are:

\[
5040=2^4\,3^2\,5\,7,
\qquad
\sigma(5040)=31\cdot13\cdot6\cdot8=19344,
\]

hence

\[
\frac{19344}{5040}=\frac{403}{105},
\]

and

\[
5460=2^2\,3\,5\,7\,13,
\qquad
\sigma(5460)=7\cdot4\cdot6\cdot8\cdot14=18816,
\]

hence

\[
\frac{18816}{5460}=\frac{224}{65}.
\]

A separately structured divisor-addition sieve agrees with every \(\sigma(n)\) through \(5582\) in the source tests.

### Directed transcendental extract

The source encloses:

- logarithms by a positive atanh series with an explicit rational tail;
- Euler’s constant by harmonic-number upper and lower bounds;
- exponentials by a positive Taylor series with a geometric tail;
- every endpoint over one exact dyadic denominator.

No binary floating-point or `Decimal` transcendental is part of the finite certificate.

### Exact source

- `claims/theorems/T-2001-independent-robin-finite-barrier.md`
- `claims/lemmas/L-2001-atanh-log-enclosure.md`
- `claims/lemmas/L-2002-euler-gamma-harmonic-enclosure.md`
- `claims/lemmas/L-2003-exp-taylor-enclosure.md`
- `experiments/X-2001-independent-robin-barrier/`

---

## 2. Canonical support and exponent dominance

Let

\[
n=\prod_{i=1}^kq_i^{a_i},
\qquad q_1<\cdots<q_k,
\]

and let

\[
b_1\ge b_2\ge\cdots\ge b_k
\]

be the same exponent multiset in nonincreasing order. Let \(p_i\) be the \(i\)-th prime and define

\[
\mathcal H(n)=\prod_{i=1}^kp_i^{b_i}.
\]

Then

\[
\mathcal H(n)\le n,
\qquad
I(\mathcal H(n))\ge I(n).
\]

### Proof

It is enough to remove one exponent inversion. Let \(p<q\) and \(0\le a<b\). Compare

\[
x=mp^aq^b,
\qquad
x'=mp^bq^a,
\]

with \(m\) coprime to \(pq\). Then

\[
\frac{x'}x=\left(\frac pq\right)^{b-a}<1.
\]

For \(r\ge0\), set

\[
F_r(t)=1+t+\cdots+t^r.
\]

The relevant local factors are

\[
F_a(1/p)F_b(1/q)
\quad\text{and}\quad
F_b(1/p)F_a(1/q).
\]

For \(b>a\),

\[
G(t)=\frac{F_b(t)}{F_a(t)}
\]

is strictly increasing on \(t>0\), since

\[
G'(t)F_a(t)^2
=
\sum_{i=0}^b\sum_{j=0}^a(i-j)t^{i+j-1},
\]

and the terms with \(0\le i,j\le a\) cancel in pairs, leaving only positive terms with \(a+1\le i\le b\). Because \(1/p>1/q\), moving the larger exponent to the smaller prime decreases the integer and increases abundancy.

Repeating inversion removal sorts the exponents. Replacing the sorted support \(q_i\) by the first \(k\) primes \(p_i\le q_i\) again decreases the integer, while

\[
I(r^{b_i})=1+r^{-1}+\cdots+r^{-b_i}
\]

decreases as \(r>1\) increases. Multiplication proves the result.

### Exact source

- `claims/lemmas/L-2005-canonical-exponent-support-dominance.md`
- source blob `07418f6d67b5b5138b54720719d5a73a9dc4786a`

---

## 3. Complete canonical reduction

Call

\[
h=\prod_{i=1}^kp_i^{b_i},
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

The reverse implication is immediate. Assume \(n\) violates the inequality. The finite barrier gives \(n\ge5583\). Put \(h=\mathcal H(n)\). Then

\[
h\le n,\qquad I(h)\ge I(n).
\]

First \(h>5040\). Otherwise,

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

Since \(h\le n\) and \(\log\log x\) is increasing on this range,

\[
e^\gamma\log\log h
\le e^\gamma\log\log n.
\]

Therefore,

\[
I(h)\ge I(n)
\ge e^\gamma\log\log n
\ge e^\gamma\log\log h.
\]

Thus \(h\) is a canonical violation.

### Boundary

The reduction identifies a complete infinite search domain. It does not make that domain finite. Support size and exponents remain unbounded.

### Exact source

- `claims/theorems/T-2002-hardy-ramanujan-completeness.md`
- source blob `36ebbfc2fe6db478de50d6b4a3ec563b2b6dbff4`

---

## 4. Nested prefix-level encoding

Fix consecutive tail primes

\[
q_1<\cdots<q_n
\]

and a nonincreasing exponent vector

\[
A\ge b_1\ge\cdots\ge b_n\ge1.
\]

For \(r=2,\ldots,A\), define

\[
\ell_r=\#\{i:b_i\ge r\}.
\]

Then

\[
n\ge\ell_2\ge\ell_3\ge\cdots\ge\ell_A\ge0.
\]

Conversely, every such nested sequence determines exactly one canonical tail by

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

Then

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

The proof is finite reordering: at each level the active indices form an initial prefix, and the prime-power abundancy ratios telescope.

### Exact source

- `claims/lemmas/L-3501-canonical-tail-level-encoding.md`
- source blob `e7a5759e4f963aaa1ac679fde10991ba73ec8140`

---

## 5. Exact powered shared-budget envelope

Let a fixed canonical prefix have integer value \(P\), exact abundancy \(I_P\), and last exponent \(A\). Let the remaining consecutive primes be \(q_1,\ldots,q_n\), with global integer bound \(B\). Put

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

Choose integers \(a\ge0\), \(d\ge1\), and define

\[
W_{r,\ell}
=
\frac{G_{r,\ell}^{\,d}}{Q_\ell^{\,a}}.
\]

Set

\[
V_{A+1}(m)=1,
\]

and for \(r=A,A-1,\ldots,2\),

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
\bigl(I_PI(R)\bigr)^dM_0^aV.
\]

Every quantity on the right is rational and arises from finite exact maximization. No logarithmic ordering, fractional power, or floating optimizer enters the proof object.

### Proof

By the nested-level encoding,

\[
C(b)=\prod_{r=2}^{A}Q_{\ell_r},
\qquad
J(b)=\prod_{r=2}^{A}G_{r,\ell_r}.
\]

Therefore,

\[
\frac{J(b)^d}{C(b)^a}
=
\prod_{r=2}^{A}W_{r,\ell_r}.
\]

Backward induction shows every nested continuation is bounded by the corresponding \(V_r(m)\), so

\[
\frac{J(b)^d}{C(b)^a}\le V.
\]

Using \(C(b)\le M_0\),

\[
J(b)^d\le M_0^aV.
\]

Finally,

\[
I\!\left(P\prod_iq_i^{b_i}\right)
=
I_PI(R)J(b),
\]

which gives the theorem.

### Finite regression boundary

The source includes a synthetic bounded subtree where the joint envelope beats the product of separate exponent caps. This validates the finite algebra; it is not a larger verified Robin range.

### Exact source

- `claims/lemmas/L-3502-exact-powered-lagrange-tail-envelope.md`
- source blob `58b0a4b77df279228f554660139ae70cbaa78413`

---

## Computation and assurance status

- The \(n\le5582\) source uses exact integer/dyadic artifacts.
- The exact-SHA review checked theorem and checker semantics without rerunning the full finite loop.
- The powered-envelope retained artifact is a synthetic exact control.
- The larger \(10^{54}\) and \(10^{100}\) traversals are not integrated here as independently replayed results.
- A hash of an unavailable terminal stream is provenance, not proof of complete traversal.

## Common misreadings

- Canonical does not mean colossally abundant.
- The transform proves existence of a canonical violator if any violator exists; it does not assert the original \(n\) was canonical.
- A bounded-tail envelope is not a theorem about the unbounded class.
- A larger finite endpoint is not evidence that the global inequality holds.
- Search and verifier code sharing one arithmetic kernel are not independent backends.

## Why this packet matters

The arithmetic route has a complete structural search domain and exact finite pruning language independent of any one large scan.

## Exact next missing step

Prove an unbounded tail theorem, construct a complete infinite pruning argument, or find one exact violation. Extending only the finite endpoint does not cross the decisive quantifier.
