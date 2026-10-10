# Limits of interpolation, finite moment ladders, and long-row cofinality

**Status:** proved norm inequalities and fully quantified synthetic countermodels to deductions from those inequalities. These are not counterexamples to the arithmetic moment conjecture. The conditional application to an imported zero-free exponent does not independently validate that exponent.

**Scope:** \(h=1+\theta\), \(0<\theta\le1/10\), a fixed finite moment order \(K\), and all larger fixed orders \(k\ge K\). Constants may depend on these fixed parameters. The final long-row discussion separately allows varying fixed row exponents \(h_k>0\).

**Dependencies:** Hölder's elementary supremum interpolation, Markov's inequality, and the packet's already proved prime-replication extraction. The conditional arithmetic example also uses a uniform reciprocal bound with a fixed positive zero-free buffer, the polynomial conductor bound, and the imported second moment. No additional arithmetic cancellation theorem is asserted.

## 1. Interpolating a finite moment and a pointwise cap

Let \(D\ge2\), \(H=D^h\), and let \(U_D\) be a finite row set. For complex arrays \(a_D(u)\), define

\[
M_{2j}(D)=\sum_{u\in U_D}|a_D(u)|^{2j}.
\]

Fix \(K\ge1\) and \(B>1/2\). Suppose that, for every \(\epsilon>0\),

\[
M_{2K}(D)\ll_\epsilon H D^{K+\epsilon},
\qquad
\max_{u\in U_D}|a_D(u)|\ll_\epsilon D^{B+\epsilon}.
\tag{1.1}
\]

Then for every fixed \(k\ge K\) and every \(\epsilon>0\),

\[
\boxed{
M_{2k}(D)\ll_{k,\epsilon}
H D^{K+2(k-K)B+\epsilon}
=H D^{k+(2B-1)(k-K)+\epsilon}.}
\tag{1.2}
\]

**Proof.** Bound \(2k-2K\) powers of each entry by the supremum and sum the remaining \(2K\) powers. For a requested final loss choose the two input losses sufficiently small, depending on the fixed \(k\). If \(k=K\), use the moment hypothesis directly. This proves (1.2). \(\square\)

The excess exponent in (1.2) is

\[
e_k=(2B-1)(k-K).
\tag{1.3}
\]

Thus this deduction cannot meet \(e_k=o(k)\) while \(B>1/2\) stays fixed.

For the actual arithmetic family, feeding (1.2) into prime-replication extraction gives

\[
\begin{aligned}
\alpha_k
&=\frac12+\frac{5h}{12k}+\frac{(2B-1)(k-K)}{2k}\\
&=B+\frac Kk(B_K-B),
\qquad
B_K=\frac12+\frac{5h}{12K}.
\end{aligned}
\tag{1.4}
\]

This is a convex combination of \(B\) and \(B_K\). It cannot improve upon their minimum. A larger moment obtained only by this interpolation does not improve the best exponent already contained in its inputs.

## 2. Exact synthetic arrays show sharpness

The following arrays have an actual positive integer number of rows. They satisfy the entire finite ladder, so they also cover any smaller finite selection of moment inputs.

### Proposition 2.1. General construction with an explicit row-count condition

Fix \(h=1+\theta\), \(0<\theta\le1/10\), an integer \(K\ge1\), and \(B>1/2\) satisfying

\[
E:=h-K(2B-1)>0.
\tag{2.1}
\]

For each real \(D\ge2\), take

\[
U_D=\{1,\ldots,\lfloor D^h\rfloor\},
\qquad R_D=\lfloor D^E\rfloor,
\]

and define

\[
a_D(u)=
\begin{cases}
D^B,&1\le u\le R_D,\\
0,&R_D<u\le\lfloor D^h\rfloor.
\end{cases}
\tag{2.2}
\]

Then \(1\le R_D\le\lfloor D^h\rfloor\), and for every \(1\le j\le K\),

\[
M_{2j}(D)\le D^{h+j}.
\tag{2.3}
\]

For every fixed \(k\ge K\), once \(D\ge2^{1/E}\),

\[
\frac12D^{h+k+(2B-1)(k-K)}
\le M_{2k}(D)
\le D^{h+k+(2B-1)(k-K)}.
\tag{2.4}
\]

If also \(B\le B_K\), then for every fixed \(C>0\),

\[
R_D\ge C D^{h/6}/\log D
\tag{2.5}
\]

for all sufficiently large \(D\). Thus any prescribed subset of at most \(C D^{h/6}/\log D\) row labels can be assigned these large values by relabeling the array.

**Proof.** Since \(B>1/2\), (2.1) gives \(0<E<h\), proving the row-count assertions. For \(j\le K\),

\[
\begin{aligned}
M_{2j}(D)
&=R_DD^{2jB}
\le D^{h-K(2B-1)+2jB}\\
&=D^{h+j+(K-j)(1-2B)}
\le D^{h+j}.
\end{aligned}
\]

If \(D^E\ge2\), then \(D^E/2\le R_D\le D^E\). Multiplication by \(D^{2kB}\) gives (2.4). Finally \(B\le B_K\) is equivalent to \(E\ge h/6\), which proves (2.5), including equality of these exponents because of the logarithmic denominator. \(\square\)

These are arrays of numbers. No claim is made that they satisfy the prime-removal identities, character correlations, or any other additional arithmetic relation. The conclusion is that the norm bounds, a pointwise cap, and the number of principal replicas alone cannot give a smaller exponent.

### Corollary 2.2. A convenient endpoint model at every finite order

For every fixed \(K\ge1\), take

\[
B=B_K=\frac12+\frac{5h}{12K},
\qquad E=h/6,
\qquad R_D=\lfloor D^{h/6}\rfloor.
\tag{2.6}
\]

In the stated domain \(h\le11/10\), one has \(1/2<B_K<1\). Proposition 2.1 gives all diagonal upper moments through \(2K\), the pointwise cap \(D^{B_K}\), and

\[
M_{2k}(D)\asymp
H D^{k+\frac{5h}{6K}(k-K)}
\quad(k\ge K).
\tag{2.7}
\]

There are more large entries than the prime-replica count, up to any fixed prime-count constant, for sufficiently large \(D\). The excess in (2.7) has positive limiting slope \(5h/(6K)\).

If there is an additional prescribed cap \(B_{\rm cap}>1/2\), take instead

\[
B=\min(B_{\rm cap},B_K).
\tag{2.8}
\]

Then \(E\ge h/6>0\), all the same finite moment bounds hold, and the excess slope \(2B-1\) is still positive. This explicitly handles a stronger pointwise input without violating it.

For example, with \(B_{\rm cap}=7/8\), the \(K=1\) construction uses \(B=7/8\) and \(R_D=\lfloor D^{h-3/4}\rfloor\), rather than the larger endpoint \(B_1\). For \(K\ge2\), \(B_K<7/8\) throughout \(h\le11/10\), so the endpoint model itself respects that cap.

## 3. Conditional application of the imported pointwise exponent

Suppose the exact arithmetic family has the imported second moment

\[
M_2(D)\ll_\epsilon HD^{1+\epsilon},
\tag{3.1}
\]

and suppose a uniform zero-free half-plane with boundary \(B<1\) is available for all relevant primitive twists. The standard reciprocal lemma with a fixed positive buffer, together with polynomial conductor growth and deleted-Euler-factor control, then gives

\[
|A_u(D;W)|\ll_{\delta}D^{B+\delta}
\quad(0<Nu\le D^h)
\tag{3.2}
\]

for every \(\delta>0\), with constants uniform in the moving row. This pointwise statement must include its conductor uniformity; bounds with uncontrolled individual-character constants are insufficient.

Taking \(K=1\) in Proposition 1 yields

\[
M_{2k}(D)\ll_\epsilon
H D^{1+2B(k-1)+\epsilon}.
\tag{3.3}
\]

If the imported value \(B=7/8\) is assumed, this gives

\[
M_4(D)\ll_\epsilon HD^{11/4+\epsilon},
\qquad
e_k=\frac34(k-1).
\tag{3.4}
\]

This is weaker than the requested \(M_4\ll HD^{2+\epsilon}\). Its extracted boundary is

\[
\alpha_k
=\frac78+\frac1k\left(\frac1{24}+\frac{5\theta}{12}\right)
>\frac78.
\tag{3.5}
\]

Thus the interpolation does not bootstrap the imported boundary downward. No independent validation of the claimed imported value \(7/8\) is contained in this example.

## 4. The tail target needs new information as well

A diagonal \(2K\)-th moment gives, by Markov,

\[
\#\{u:|a_D(u)|>D^\alpha\}
\ll_\epsilon D^{h+K-2K\alpha+\epsilon}.
\tag{4.1}
\]

To infer the sufficient prime-replica tail bound

\[
\#\{u:|a_D(u)|>D^\alpha\}
=o(D^{h/6}/\log D)
\tag{4.2}
\]

by a strict power saving in (4.1), one needs

\[
\alpha>\frac12+\frac{5h}{12K}=B_K.
\tag{4.3}
\]

At equality, additional logarithmic information would be required. For every \(\alpha<B_K\), the endpoint array in Corollary 2.2 has \(R_D\asymp D^{h/6}\) entries above any fixed multiple of \(D^\alpha\) at sufficiently large \(D\), so it violates (4.2) while satisfying every moment through \(2K\). If a stronger cap \(B_{\rm cap}\) is imposed, the same statement holds for \(\alpha<\min(B_{\rm cap},B_K)\), using (2.8).

This pinpoints the arithmetic content that a new tail theorem must add beyond the moment bounds already known.

## 5. Why long-row diagonal moments do not give cofinal descent

Suppose a \(2k\)-th moment theorem, perhaps only along a sequence of fixed orders \(k\to\infty\), has the form

\[
M_{2k}(D,D^{h_k})\ll_\epsilon
D^{k+h_k+e_k+\epsilon},
\qquad h_k>0,\quad e_k\ge0.
\tag{5.1}
\]

The prime-replication formula gives boundary

\[
\frac12+\frac{5h_k}{12k}+\frac{e_k}{2k}.
\tag{5.2}
\]

The prime argument remains valid at any fixed positive row exponent: primes have norm comparable to \(D^{h_k/6}\); all lower-scale terms decrease, and for sufficiently large exponents the unwanted terms simply vanish by the fixed support.

To make the displayed gap tend to zero by this deduction, both \(h_k/k\to0\) and \(e_k/k\to0\) are necessary and sufficient. In particular, if \(\liminf h_k/k=c>0\), the gap remains at least \(5c/12\), irrespective of having exact diagonal size \(e_k=0\).

The packet's unconditional theorem first guaranteeing diagonal size at \(H\ge D^{2k}\) therefore supplies no cofinal approach to \(1/2\). More generally, collapsing \(k\) factors of length \(D\) into one coefficient sequence of length \(D^k\), followed by a theorem requiring a comparable row range, keeps \(h_k\) proportional to \(k\). It does not meet the short-row requirement.

These propositions rule out specific shortcuts from existing norm information. They do not rule out the desired arithmetic moment theorem, a new short-row tail estimate, or an amplification using additional character correlations.
