# A follow-up: signed quantiles can replace small absolute values

**Status:** proposed further capture implication; independent review is recorded separately. The arithmetic quantile hypothesis remains open. This is a separate continuation; it changes no frozen claim or diagnostic in `EXACT_ZETA_BRIDGE_AND_SPARSE_CAPTURE.md`.

**Exact interfaces:** that companion's ordinary Möbius identity, positive principal-replica recurrence, fixed rough-base mean, and direct all-order derivative bound. All objects below remain Eisenstein-specific, with the same literal nonunit zeros, the trivial coefficient character, the finite bad-prime restoration, and the one fixed real universal test. The additional standard analytic input is Markov's polynomial inequality, stated explicitly below.

## 1. A weaker observation, at a slightly denser grid

Use the companion's notation

\[
B_1(D)=\sum_n\mu(n)W(n/D),\qquad
B_{w^6}(D)=\sum_{\operatorname{rad}r\mid w}B_1(D/Nr).
\tag{1.1}
\]

These quantities are real. Fix \(\alpha>0\), \(h>0\), and \(0<\gamma\le1/2\). Choose the fixed roughness set \(Q\) as in the companion, so for all large \(Y\), all but at most \(\gamma/4\) of the bases in

\[
\mathcal V_Q(Y)=\{w:(w,Q)=1,\ Y/2<Nw\le Y\},
\qquad J_Q(Y)=|\mathcal V_Q(Y)|
\]

satisfy \(K_\alpha(w)\le1/2\). Put \(Y_X=X^{h/6}\) at dyadic \(X\), keeping the same base set throughout \([X,2X]\).

Use the grid \(D_{X,i}=X\exp(i\Delta_X)\), \(\Delta_X=\log2/N_X\), with

\[
\boxed{\Delta_X(\log X)^2
\mathscr L(\lceil\log X\rceil)\longrightarrow0.}
\tag{1.2}
\]

### Theorem 1.1. Two signed quantiles suffice

Suppose a fixed \(C_0\ge0\) has the following property at every grid node in every sufficiently large dyadic interval:

\[
\#\{w\in\mathcal V_Q(Y_X): B_{w^6}(D_{X,i})\le C_0D_{X,i}^{\alpha}\}
\ge\gamma J_Q(Y_X),
\tag{1.3a}
\]

\[
\#\{w\in\mathcal V_Q(Y_X): B_{w^6}(D_{X,i})\ge-C_0D_{X,i}^{\alpha}\}
\ge\gamma J_Q(Y_X).
\tag{1.3b}
\]

Then the exact endpoint bound

\[
\boxed{B_1(D)\ll D^\alpha}
\tag{1.4}
\]

holds, and ordinary zeta is zero-free in \(\Re s>\alpha\). No positive exponent loss is needed.

The two sets in (1.3) may be disjoint and may change completely from node to node. In particular the hypothesis does not require even one replica with small absolute value. An abstract array split between arbitrarily large positive and negative values can satisfy both quantiles. The arithmetic recurrence prevents such an array from hiding a record value of this particular source.

For the original fixed test \(W_*\), with \(\mathscr L(j)=j\), one may take

\[
N_X=\left\lceil(\log X)^3\omega(X)\right\rceil,
\qquad \omega(X)\longrightarrow\infty.
\tag{1.5}
\]

This costs one extra logarithm relative to the companion's small-absolute-value criterion, while recovering the exact power endpoint. No claim that the original sparser grid suffices for (1.3) is made.

## 2. A one-sided interval estimate at an absolute record

We use the classical real-polynomial inequality: if \(P\) has degree at most \(d\) on an interval \(I\) of length \(\delta\), then

\[
\|P'\|_{L^\infty(I)}\le\frac{2d^2}{\delta}
\|P\|_{L^\infty(I)}.
\tag{2.1}
\]

This is Markov's inequality after an affine change from \([-1,1]\). It is applied to a Taylor polynomial, not to the arithmetic source as if that source were itself a polynomial.

### Lemma 2.1. Record bounds give a relative modulus on the preceding interval

Fix \(\beta>0\), and suppose \(D_*\in[X,2X]\) is an absolute record in the sense

\[
A=|B_1(D_*)|>0,
\qquad |B_1(y)|\le A(y/D_*)^\beta
\quad(0<y\le D_*).
\tag{2.2}
\]

Let \(w\) satisfy \(K_\beta(w)\le1/2\). Then

\[
|B_{w^6}(y)|\le\tfrac32A\quad(0<y\le D_*),
\qquad
|B_{w^6}(D_*)-B_1(D_*)|\le A/2.
\tag{2.3}
\]

For sufficiently large \(X\), put \(m=\lceil\log X\rceil\), and choose a fixed \(c>0\) sufficiently small, depending only on the derivative constants. Set

\[
\delta=\frac{c}{\mathscr L(m)}<\frac{\log2}{2}.
\tag{2.4}
\]

For every \(0\le\eta\le\delta\),

\[
|B_{w^6}(D_*e^{-\eta})-B_{w^6}(D_*)|
\le C\frac{m^2\eta}{\delta}A+O(X^{-2})
+O\!\left(\frac{m^2\eta}{\delta}X^{-2}\right),
\tag{2.5}
\]

with constants uniform over the captured bases \(w\).

**Proof.** The positive recurrence (1.1) and the past record envelope give (2.3); no future record bound is used. On \([-\delta,0]\), set \(f(t)=B_{w^6}(D_*e^t)\). The companion derivative estimate, applied at scale \(X/2\) or \(X\) as necessary, gives

\[
\|f^{(m)}\|_\infty
\le C X\log(2X)B^{m+1}m!\mathscr L(m)^m.
\tag{2.6}
\]

This use remains valid if the past interval crosses the dyadic endpoint: the derivative estimate is uniform over all rows and does not require that a row lie in the height window of the smaller scale.

Let \(P\) be the degree-\((m-1)\) Taylor polynomial of \(f\) at \(-\delta\). The integral remainder gives

\[
\|f-P\|_\infty
\le C X\log(2X)B(Bc)^m=:E_X.
\tag{2.7}
\]

Choose \(Bc\le e^{-4}\). Since \(m\ge\log X\), \(E_X=O(X^{-2})\). By (2.3), \(\|P\|_\infty\le3A/2+E_X\). Equation (2.1) and the two endpoint approximation errors now give

\[
|f(-\eta)-f(0)|
\le 2E_X+\frac{2(m-1)^2\eta}{\delta}(3A/2+E_X),
\]

which is (2.5). \(\square\)

The endpoint factor \(m^2\) matters. Replacing it by an interior derivative estimate without a two-sided record envelope would silently strengthen the result.

## 3. Proof of the signed-quantile theorem

If \(|B_1(D)|D^{-\alpha}\) were unbounded, choose record scales \(D_j\to\infty\) with

\[
A_j=|B_1(D_j)|=F_jD_j^\alpha,
\qquad F_j\to\infty,
\]

and the past envelope (2.2) with \(\beta=\alpha>0\). Use the dyadic interval containing \(D_j\) and its common base set \(\mathcal V_Q(X^{h/6})\). At least \((1-\gamma/4)J_Q\) bases have \(K_\alpha\le1/2\). Their values at \(D_j\) have the sign of \(B_1(D_j)\) and absolute value at least \(A_j/2\).

Let \(D_{X,i}\) be the nearest grid point at or before \(D_j\). Thus \(D_{X,i}=D_je^{-\eta_j}\), \(0\le\eta_j<\Delta_X\), except that an exact grid point has \(\eta_j=0\). Condition (1.2) implies

\[
\frac{m^2\eta_j}{\delta}
\le c^{-1}m^2\Delta_X\mathscr L(m)\longrightarrow0.
\]

By Lemma 2.1, all of these contractive replicas still have the record's sign and absolute value at least \(A_j/4\) at this **same** grid node, for all sufficiently large records. Since \(A_j/D_{X,i}^\alpha\to\infty\), this exceeds the threshold in (1.3).

If the record is positive, at most \(\gamma J_Q/4\) bases can satisfy (1.3a), contradicting its required \(\gamma J_Q\). If it is negative, the same count contradicts (1.3b). Hence \(B_1(D)=O(D^\alpha)\) at the exact endpoint. The companion's nonvanishing Mellin detector gives the stated strict-half-plane zero exclusion.

The endpoint follows because the Taylor–Markov error is \(o(A_j)+O(X^{-2})\), relative to the record itself. Unlike the companion's direct Lagrange sampling bound, it does not multiply the observation threshold by \(X^{o(1)}\). The condition \(\alpha>0\) remains essential to the declared rough-base input.

## 4. Arithmetic and evidence boundary

This theorem provides a different sufficient observation condition; it proves no signed quantile estimate for the actual Möbius replicas. It does not control the full family of Hecke rows, and it does not improve an unconditional zero-free constant. For every fixed \(\alpha>1/2\), ordinary RH supplies even a uniform bound on all polynomially bounded principal replicas, as proved in the packet's converse note. Thus the cofinal signed-quantile assertions would again be equivalent to ordinary RH. No converse from the single fixed assertion of zero-freeness in \(\Re s>\alpha\) to the exact endpoint quantile is claimed.

No finite diagnostic is presented as a proof of Markov's inequality, the derivative bound, or the arithmetic quantile hypothesis. The new analytic step is the explicit Taylor–Markov relative modulus at a past absolute record. It has been written separately so that its hypotheses and the denser-grid cost can be challenged without altering the previously frozen sparse-capture theorem.
