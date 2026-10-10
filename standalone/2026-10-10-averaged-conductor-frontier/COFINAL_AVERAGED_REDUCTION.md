# Averaged signed remainders with sublinear moment losses

**Status:** a proved conditional implication combining the exact double residual reduction in PR #918 with the scale-averaged extraction in PR #917. No bound for the new signed remainder is proved here. In particular, no new full fourth moment, zero-free half-plane, cofinal hierarchy or RH conclusion is asserted.

**Sources:** PR #918 at `cfa102748b26f840ccc4b963a660711424db0ec3`, `standalone/2026-10-10-sextic-joint-core/DOUBLE_RESIDUAL_REDUCTION.md`, Proposition 2.1 and its proof; PR #917 at `6b4723042b3d250024eef45cb1924f88f28e902c`, `standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/SCALE_AVERAGED_CRITERION.md`, Theorems 3.1 and 4.1. The one-sided incidence bound retains the native second-moment input recorded in PR #915. The extraction itself is elementary once its arithmetic averaged-moment hypothesis is supplied.

## 1. Exact signed inequality before taking a positive part

Fix an integer \(k\ge2\), a finite-order character \(\nu\), the fixed excluded-prime set \(S\), and the nonnegative smooth test \(W_*\) from the source extraction theorem, whose Mellin transform is nonzero on \(\Re s>0\). Fix \(h=1+\theta\), with \(\theta>0\) in the permitted native second-moment range, and put

\[
H=D^h,\qquad
M_{2k}(D,H)=\sum_{0<Nu\le H}|A_u(D;W_*)|^{2k}.
\]

Let \(\Phi\) be the fixed nonnegative smooth row majorant used in PR #918. For the one-sided shared-incidence lengths, put \(Q=\prod_iX_i/\max_iX_i\). Split \(A^k=G_{Q_0}+R_{Q_0}\) into complete blocks with \(Q\le Q_0\) and \(Q>Q_0\), respectively.

Retain exactly PR #918's real signed remainder
\(\mathcal T_{k,Q_0}^{\Phi}(D,H)\). Its two side tuples have \(Q>Q_0\); their full Hermitian tuple has \(g_1\ne1\) and \(Ng_1\sqrt{Ng_2}>H\), with all definitions, coefficients and literal zeros unchanged.

For \(1/2<b\le1\), assume precisely the one-sided inputs of that source. At \(b=1\), the pointwise part is elementary counting, so the only nonclassical input here is the inherited native second moment. For \(b<1\), the additional pointwise bound must be uniform in rows and smaller scales.

The proof of the source proposition gives the slightly more informative unsimplified inequalities

\[
\begin{split}
M_{2k}(D,H)
&\le C_\epsilon HD^{k+\epsilon}
 (1+Q_0^{2b-1})+2\mathcal T_{k,Q_0}^{\Phi}(D,H),\\
\mathcal T_{k,Q_0}^{\Phi}(D,H)
&\ge-C_\epsilon HD^{k+\epsilon}.
\end{split}
\tag{1.1}
\]

Indeed, the full smooth residual square is \(\mathcal T+E\), where \(|E|\le C_\epsilon HD^{k+\epsilon}\). It is nonnegative. Insert this identity into the sharp-row inequality \(\|G+R\|_2^2\le2\|G\|_2^2+2\|R\|_2^2\), and bound the controlled error above. This proves the first line without replacing \(\mathcal T\) by its positive part; nonnegativity proves the second. Both constants are uniform in the cutoff.

## 2. A one-sided scale average is sufficient

Fix \(q,e\ge0\), and set \(Q_0(D)=D^q\). Suppose, for every \(\epsilon>0\), uniformly for every \(X\ge2\), that

\[
\int_X^{2X}\mathcal T_{k,D^q}^{\Phi}(D,D^h)\frac{dD}{D}
\le C_\epsilon X^{h+k+e+\epsilon}.
\tag{2.1}
\]

This is an upper bound for a signed integral. It is not a hypothesis on the integral of an absolute value, on an isolated sharp signed sector, or on each individual scale.

Define

\[
\lambda=\max\{e,(2b-1)q\}.
\tag{2.2}
\]

**Theorem 2.1.** Under the stated inputs and (2.1),

\[
\int_X^{2X}M_{2k}(D,D^h)\frac{dD}{D}
\ll_\epsilon X^{h+k+\lambda+\epsilon}.
\tag{2.3}
\]

Consequently every fixed primitive row twist covered by the source extraction is zero-free in

\[
\boxed{\displaystyle
\Re s>\frac12+\frac{5h}{12k}
 +\frac{\max\{e,(2b-1)q\}}{2k}.}
\tag{2.4}
\]

**Proof.** Integrate the first line of (1.1). On \([X,2X]\), the integral of the controlled term is bounded by
\(C_\epsilon X^{h+k+(2b-1)q+\epsilon}\), since all exponents are fixed. Equation (2.1) controls the remaining signed integral. The sum of the two bounds is (2.3), after adjusting constants. Apply PR #917, Theorem 4.1, with moment excess \(\lambda\). That theorem proves the extraction by exact sixth-power replicas, an invertible causal average of Euler-removal operators, and the nonvanishing Mellin test; it does not require a pointwise moment estimate. This gives (2.4). \(\square\)

The lower bound in (1.1) also shows that replacing (2.1) by an upper bound for the integral of the positive part changes the premise by at most a controlled \(X^{h+k+\epsilon}\) error. The signed formulation is valid directly and avoids imposing a stronger unneeded absolute-value premise.

If \(Q_0(D)\) is any chosen measurable growing subpower cutoff, the same argument applies with incidence excess zero: for every \(\eta>0\), \(Q_0(D)\le D^\eta\) eventually. Reallocate the arbitrary small-power losses in (1.1), and absorb the bounded initial range of scales into the constant. The conclusion is then (2.4) with the maximum replaced by \(e\).

## 3. A cofinal criterion allows polynomial cutoffs

Now take an unbounded sequence of fixed orders \(k\), keeping the desired primitive row twist, its finite-order \(\nu\), and its row \(r\) fixed along the sequence. At each order suppose the native second-moment input and (2.1) hold, with parameters \(h_k,b_k,q_k,e_k\). Require that every \(h_k\) lie in the allowed native range, that \(1/2<b_k\le1\), and that

\[
h_k=o(k),\qquad q_k=o(k),\qquad e_k=o(k).
\tag{3.1}
\]

A single fixed admissible \(h>1\) is sufficient for the first condition. Since \(2b_k-1\le1\),

\[
0\le\max\{e_k,(2b_k-1)q_k\}\le\max\{e_k,q_k\}=o(k).
\]

Equation (2.4) therefore approaches \(1/2\). For each fixed primitive row twist, no zero can lie strictly to the right of that line if all these arithmetic hypotheses hold. When the hypotheses also cover the contragredient characters, the functional equation gives the critical-line conclusion for that family. Requiring the hypotheses for every fixed finite-order \(\nu\) supplies this coverage and gives the corresponding finite-order Hecke-family conclusion. The principal member is self-dual and includes ordinary zeta through the factorization of the Dedekind zeta function of \(K\).

This criterion permits, for example, \(q_k=\sqrt{k}\) and \(e_k=\sqrt{k}\), with \(b_k=1\) and fixed \(h\). Each fixed-order cutoff \(Q_0=D^{\sqrt{k}}\) is polynomial in \(D\); the conditional boundary in (2.4) still tends to \(1/2\). For sufficiently large \(k\), this removes a larger one-sided portion than a subpower cutoff while remaining below the generic maximum scale \(Q\asymp D^{k-1}\). No averaged bound (2.1) for this example is asserted.

Constants may depend arbitrarily on each fixed order and its fixed data. If a proof route uses an enlarged finite \(S=S_k\), fixed before varying scales, the deleted Euler factors remain nonzero in \(\Re s>0\); the extraction still concerns the same primitive functions. This allows qualitative cofinal deductions, but gives no quantitative height-dependent shrinking band or usable uniformity as \(k\) grows.

## 4. What still has to be proved

The theorem is a composition of two proved reductions around an open arithmetic estimate. It does not prove (2.1), even at one new order. At the fourth moment, reaching the limiting \(17/24\) boundary through this route requires zero moment excess and arbitrarily small fixed \(h-1>0\). The separate small-gcd criterion in this packet gives a more useful fourth-order residual than the subpower-incidence periphery.

For the cofinal hierarchy, exact diagonal-size estimates at every order are more than necessary: signed dyadic averages with losses sublinear in the order suffice. Obtaining those averages still requires cancellation of the actual Möbius/sextic coefficients. In the cofinal regime, at all sufficiently large orders, completely disjoint long tuples remain within the unresolved sector; their large number has not been turned into a bound by the new quantifiers. At an arbitrary fixed order a cutoff beyond all supported \(Q\) can make the remainder empty, but the displayed controlled moment loss is then large.
