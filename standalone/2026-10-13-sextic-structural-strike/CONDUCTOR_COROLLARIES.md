# Global conductor consequence and the remaining five-label limit

**Status:** two deductions from the frozen conjugate-pair theorem, and one exact limit of the displayed bounds. No new native moment or zeta zero-free statement.

**Load-bearing new source:** [CONJUGATE_PAIR_CONDUCTOR_SIEVE.md](CONJUGATE_PAIR_CONDUCTOR_SIEVE.md), SHA256
`220d767a03ed6c61b8e5a3ea34b48a0a2adae92607047fbfa0bb96e5be876ef2`,
Theorems 3.1 and 4.1. The latter's general-order extension is equation (4.6).

**Other sources:** de Faveri, arXiv:2610.04045v1, Theorem 1.1, equations (1.4)–(1.5), and Section 9; PR #929 at `97bf40329489992e9384c34d7595af6d01a40774`, `CUBIC_CONDUCTOR_AVERAGE.md`, Theorem 2.1. The external analytic theorems are retained as inputs.

## 1. Conductor-size mean for the entire conjugate local type

Fix \(n\geq3\), a number field containing \(\mu_n\), the standard family and all bad-prime/ray data. Let \(\psi\) range over a fixed finite family of finite-order Hecke characters with bounded conductor. For \(X\geq1\),
\[
\boxed{
\sum_{\substack{a,b\in I(S)\\ab\ {\rm squarefree}\\N(ab)\leq X}}
\left|L\!\left(\tfrac12+it,(\psi\chi_{a b^{n-1}})^{\rm prim}\right)\right|^2
\ll_{\epsilon}X^{1+\epsilon}(2+|t|)^{C_\epsilon}.
}
\tag{1.1}
\]
If a fixed good prime occurs in \(\operatorname{cond}\psi\), first include that prime in the fixed bad set or retain the finite local partition there. This is a fixed operation, not an enlargement by a moving conductor.

**Proof.** On every nonempty dyad \(Na\asymp A,\ Nb\asymp B\), the general-order mean ratio in (4.6) of the companion proof is bounded, because \(R\) is fixed and \(M=\min(A,B)\geq1,\ M\leq N_0=\max(A,B)\). In the final term the two length powers have sum \(3/n-1\leq0\), and the power of \(N_0\) is nonpositive. Hence that dyad has mean \(O((AB)^{1+\eta}(2+|t|)^C)\).

Retain only dyads meeting \(AB\ll X\), and drop the remaining conductor cutoff by positivity. Their sums satisfy
\[
\sum_{\substack{A=2^j,\ B=2^\ell\\AB\ll X}}AB
\ll X\log(2X).
\]
Choose \(\eta\) smaller than \(\epsilon\). The finite ray partitions and the bounded number of exceptional bounded-conductor characters do not change the conclusion. \(\square\)

The conductor outside the fixed bad set is exactly \(ab\). Thus (1.1) is a bound ordered by conductor, even though the defining ideal \(a b^{n-1}\) can have much larger norm.

### Corollary 1.2. The fully sextic local type

Take \(n=6\) over the Eisenstein field. Among characters in the standard sixth-order family, (1.1) includes every character whose component at each ramified good prime has exact order six. Allowing a fixed finite family of bad-prime twists covers any prescribed bounded local data at \(S\).

At a good prime the tame residue-character group is cyclic, and there are precisely \(\varphi(6)=2\) characters of exact order six relative to a fixed primitive generator: its first and fifth powers. Partition the ramified primes according to those two signs to obtain the unique good conductor labels \(a,b\). Any discrepancy confined to the fixed bad primes is one of finitely many fixed Hecke characters. This proves the asserted coverage.

The corresponding statement holds for the exact-order-three and exact-order-four local types, since their primitive local powers are also precisely \(1\) and \(n-1\). For \(n=3\), all nontrivial local components have order three, so the conductor family is complete. For \(n=4\), local components of order two remain outside this corollary. For \(n=6\), local components of order two or three remain outside it.

The distinction matters in the native moment problem: a tuple with mutually disjoint singleton primes produces the fully sextic local type. Consequently the new theorem gives a sharp absolute central-\(L\) mean for the character family attached to the leading primitive core. Turning that family mean into the desired moment still requires signed singleton cancellation, as the companion theorem's term \(D^k(HL)^{1/2}\) shows.

No claim of external novelty or priority is made for the conductor theorem; the proof is presented as a source-qualified deduction.

## 2. The complete five-label family: valid bounds in three directions

An arbitrary good sixth-order conductor pattern has the form
\[
u=q_1q_2^2q_3^3q_4^4q_5^5,\qquad
q_1q_2q_3q_4q_5\ {\rm squarefree}.
\tag{2.1}
\]
Let \(Nq_i\asymp Q_i\), put \(P=\prod_{i=1}^5Q_i\), and let
\(\mathcal M(\mathbf Q)\) be the central \(L^2\)-mean over this physical box, with fixed finite bad-prime twists.

The new sextic pair bound applies jointly to \(q_1,q_5\), with moving background
\[
R_6=Q_2Q_3Q_4,\quad
M_6=\min(Q_1,Q_5),\quad N_6=\max(Q_1,Q_5).
\]
After counting the background labels it gives
\[
\mathcal M(\mathbf Q)\ll P^{1+\epsilon}
\left[
1+R_6^{1/6}M_6^{-2/3}
+R_6^{1/2}(M_6/N_6)^{1/3}
+R_6^{1/4}M_6^{-5/12}N_6^{-1/12}
\right].
\tag{2.2}
\]
The old cubic pair bound applies jointly to \(q_2,q_4\), with
\[
R_3=Q_1Q_3Q_5,\quad
M_3=\min(Q_2,Q_4),\quad N_3=\max(Q_2,Q_4),
\]
and gives
\[
\mathcal M(\mathbf Q)\ll P^{1+\epsilon}
\left[
1+R_3^{1/2}(M_3/N_3)^{1/6}
+R_3^{1/3}M_3^{-1/3}
\right].
\tag{2.3}
\]
The quadratic single-label sieve applies to \(q_3\), with
\(R_2=Q_1Q_2Q_4Q_5\), and gives
\[
\mathcal M(\mathbf Q)\ll P^{1+\epsilon}
\left[1+(R_2/Q_3)^{1/2}\right].
\tag{2.4}
\]
Here (2.4) is the standard quadratic large sieve plus the same uniform approximate-functional-equation and squarefree-index adapter. The powers of the original sixth-order family of exponents \(2\) and \(3\) form the required cubic and quadratic families after fixing the finite ray data.

One can also retain every single-label sixth-order or cubic estimate. These are legitimate bounds for the same positive mean, so their minimum can be taken. This gives useful anisotropic improvements, but the universal exponent in the next section does not improve.

## 3. An exact obstruction to improving the universal weighted exponent by these means

The Section 9 comparison in the primary source requires
\[
\mathcal M(\mathbf Q)
\ll Q_1^{1+\epsilon}(Q_2Q_3Q_4Q_5)^{\alpha+\epsilon}
\tag{3.1}
\]
uniformly in the five sizes. Its stated exponent for order six is
\(\alpha=11/8\).

Set
\[
Q_1=Q_2=Q_3=Q_4=Q_5=X.
\tag{3.2}
\]
Then \(P=X^5\). Every single-label branch has the approximate-functional-equation ratio
\[
P^{1/2}/Q_j=X^{3/2}.
\]
The sixth-order pair bound (2.2) has ratios
\[
1,\quad X^{-1/6},\quad X^{3/2},\quad X^{1/4}.
\tag{3.3}
\]
The cubic pair bound (2.3) has ratios
\[
1,\quad X^{3/2},\quad X^{2/3}.
\tag{3.4}
\]
The quadratic bound has \(1+X^{3/2}\). Therefore the best of the complete displayed upper bounds still has size
\[
X^{5+3/2}=X^{13/2}.
\tag{3.5}
\]
But (3.1) has size \(X^{1+4\alpha}\). Consequently no universal value \(\alpha<11/8\) can be certified just by minimizing or geometrically interpolating this finite list of bounds.

This is an exact statement about their right-hand sides. It is not an arithmetic lower bound for \(\mathcal M\), and does not preclude a better joint estimate that uses three or more conductor labels simultaneously.

For completeness the matching upper exponent \(11/8\) is already supplied by the older single-label calculation. Write \(R=Q_2Q_3Q_4Q_5\) and select the largest \(Q_j\). Then \(Q_j\geq Q_1\) and \(Q_j\geq R^{1/4}\). The source bound
\[
\mathcal M(\mathbf Q)\ll P^{1+\epsilon}
\left[1+P^{1/2}/Q_j+(P/Q_j)^{1/3}\right]
\]
is at most
\[
P^{1+\epsilon}\left[1+R^{3/8}+R^{1/3}\right]
\ll Q_1^{1+\epsilon}R^{11/8+\epsilon}.
\]
Thus the exact optimum of the displayed bound family for this uniform objective is \(11/8\); no linear-programming computation is needed to prove that conclusion.

A floating-point search over all orientations and all active monomials located (3.2), but it is only exploratory evidence. Equations (3.2)–(3.5) and the preceding elementary upper bound supply the actual proof.

## 4. What this says about another attempted extension

Summing the five labels independently after applying a two-label theorem fixes three others as a background conductor. In the balanced box, that background has norm \(X^3\), and both pair methods pay its square root in the second mean. This exactly reinstates the old \(X^{3/2}\) loss.

Reflecting both negative-sign labels independently does not by itself resolve that issue. It replaces them by dual lengths of order \(P/Q_j\) and introduces correspondingly larger positive row volumes. A proof would need to exploit the joint signed kernel before those new volume terms are bounded separately. The present conjugate-pair theorem does not provide such an estimate.

The broader conclusion is therefore precise: the fully sextic local-type conductor mean is at conductor size; mixing independent order-six, order-three and order-two local components still has a balanced background obstruction for the currently combined inequalities.

