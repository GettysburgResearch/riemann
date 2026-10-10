# Positive-density replicas: log-free spikes and a sharper tail criterion

**Status:** proved composition of PR 912's universal Mellin test and fixed-twist replication with PR 913's positive-density rough-base lemma. No new arithmetic higher-moment upper bound or zero-free line is proved. The last section is a finite-moment corollary consolidating PR 912 with the inherited second moment.

**Exact sources:** [PR 912, MELLIN_AND_SPIKES.md](https://github.com/GettysburgResearch/riemann/blob/6afd64e042ce7b59d550c3d76e9e2cca8b2c7379/standalone/2026-10-10-generalized-inverse-moments/MELLIN_AND_SPIKES.md), Sections 1–5; [PR 913, GENERAL_MOMENT_ATTACK.md](https://github.com/GettysburgResearch/riemann/blob/6498d6cc2eded03159c7332b25fd224ad07f89c1/standalone/2026-10-10-sextic-moment-descent/GENERAL_MOMENT_ATTACK.md), Section 6; and [PR 913, FOURTH_MOMENT_ATTACK.md](https://github.com/GettysburgResearch/riemann/blob/6498d6cc2eded03159c7332b25fd224ad07f89c1/standalone/2026-10-10-sextic-moment-descent/FOURTH_MOMENT_ATTACK.md), Proposition 2.1 and Section 8. The first two statements below need standard Hecke continuation, sextic reciprocity, and elementary ideal counting, but neither the imported quasi-Riemann theorem nor the imported second moment.

**Scope:** \(K=\mathbb Q(\sqrt{-3})\), a fixed finite-order Hecke character \(\nu\), the fixed excluded primes \(S\), and every fixed row exponent \(h>0\). Ideals prime to the fixed bad primes are represented by the fixed primary convention. Sixth powers do not depend on the unit representative. All zero extensions and moving coprimality masks are retained.

## 1. A positive proportion of sixth-power replicas is contractive

Use the literal family

\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad \chi_n(u)=(u/n)_6.
\tag{1.1}
\]

Fix a nonzero row \(v\), and put
\(\eta_v(n)=\nu(n)\chi_n(v)\). For a base ideal \(w\) prime to \(Sv\), complete multiplicativity and the original nonunit zeros give the finite identity

\[
A_{v w^6}(x;W)
=\sum_{\operatorname{rad}(r)\mid w}\eta_v(r)A_v(x/Nr;W).
\tag{1.2}
\]

Indeed, multiplication by \(w^6\) deletes precisely the coefficient primes dividing \(w\). Dividing the original inverse Euler product by its factors \(1-\eta_v(p)(Np)^{-s}\), for \(p\mid w\), gives (1.2). This also follows from finite coefficient convolution and requires no convergence of an infinite Dirichlet series. For each \(x\), only finitely many terms survive the lower support cutoff of \(W\).

Fix any \(\alpha>0\). For a fixed finite prime set \(Q\supseteq S\cup\{p:p\mid v\}\), let

\[
\mathcal V_Q(Y)=\{w:(w,Q)=1,\ Y/2<Nw\le Y\},\qquad
J_Q(Y)=|\mathcal V_Q(Y)|,
\]

\[
K_\alpha(w)
=\sum_{\substack{r\ne1\\\operatorname{rad}(r)\mid w}}(Nr)^{-\alpha}.
\tag{1.3}
\]

Elementary ideal counting and finite inclusion–exclusion give

\[
J_Q(Y)\sim \kappa_QY,\qquad \kappa_Q>0.
\tag{1.4}
\]

For each fixed \(r\) prime to \(Q\), the proportion of bases divisible by \(\operatorname{rad}(r)\) tends to \(1/N\operatorname{rad}(r)\). Uniformly for large \(Y\), this proportion is at most \(C_Q/N\operatorname{rad}(r)\): count multiples by the elementary bound \(O(Y/N\operatorname{rad}(r))\), and divide by (1.4). The positive dominating series converges, because

\[
\sum_{(r,Q)=1}\frac{(Nr)^{-\alpha}}{N\operatorname{rad}(r)}
=\prod_{p\notin Q}
\left(1+\frac1{Np((Np)^\alpha-1)}\right)<\infty.
\]

Dominated convergence therefore proves the exact limit

\[
\frac1{J_Q(Y)}\sum_{w\in\mathcal V_Q(Y)}K_\alpha(w)
\longrightarrow
\prod_{p\notin Q}
\left(1+\frac1{Np((Np)^\alpha-1)}\right)-1.
\tag{1.5}
\]

Enlarge the fixed set \(Q\) until the right side is less than \(1/8\). For all sufficiently large \(Y\), the mean in (1.5) is then at most \(1/4\). Markov's inequality gives

\[
\#\mathcal G_{\alpha,Q}(Y)\ge \frac12J_Q(Y),\qquad
\mathcal G_{\alpha,Q}(Y)
=\{w\in\mathcal V_Q(Y):K_\alpha(w)\le1/2\}.
\tag{1.6}
\]

All constants may depend on the fixed \(v,\alpha,Q\); none depends on the moving base \(w\).

For

\[
Y=(D^h/Nv)^{1/6},
\tag{1.7}
\]

the rows \(v w^6\), \(w\in\mathcal V_Q(Y)\), are distinct and have norm at most \(D^h\). Consequently there are at least \(c_{v,\alpha,h}D^{h/6}\) contractive replicas for all sufficiently large \(D\). No prime-ideal theorem is used. The argument works for every fixed \(h>0\), including \(h\ge6\).

## 2. A zero forces log-free moment spikes

Take PR 912's single fixed test \(W_*\in C_c^\infty((1,2))\), \(W_*\ge0\), with Mellin transform

\[
\widehat W_*(s)
=e^{s\log2/2}
\prod_{j\ge1}\frac{\sinh(a_js)}{a_js},
\qquad a_j=\frac{\log2}{8j^2}.
\tag{2.1}
\]

The source proves that this entire transform has no zero in \(\Re s>0\). If \(\psi_v\) is the primitive character inducing \(\eta_v\), the exact scale-Mellin identity is

\[
\int_0^\infty A_v(D;W_*)D^{-s}\frac{dD}{D}
=\widehat W_*(s)\frac{E_v(s)}{L_K(s,\psi_v)}
\quad(\Re s>1),
\tag{2.2}
\]

where the finite deleted Euler factor \(E_v\) is holomorphic and nonzero in \(\Re s>0\). Thus a bound \(A_v(D;W_*)=O(D^\alpha)\), with \(\alpha>0\), excludes every zero of this \(L\)-function in \(\Re s>\alpha\). The possible principal pole causes a zero of \(1/L\), not a pole of (2.2).

**Theorem 2.1.** Suppose \(L_K(s,\psi_v)\) has a zero with real part \(b>0\). For each fixed integer \(k\ge1\), every \(0<\beta<b\), and every fixed \(h>0\), there are scales \(D_j\to\infty\) such that

\[
\boxed{\displaystyle
\frac{\sum_{0<Nu\le D_j^h}|A_u(D_j;W_*)|^{2k}}
{D_j^{2k\beta+h/6}}\longrightarrow\infty.}
\tag{2.3}
\]

**Proof.** By (2.2), \(F(D)=|A_v(D;W_*)|/D^\beta\) is unbounded. The polynomial is continuous in \(D\) and vanishes below a positive fixed scale. Choose record scales \(D_j\) such that \(F(D_j)\to\infty\) and

\[
|A_v(x;W_*)|\le F(D_j)x^\beta
\quad(0<x\le D_j).
\]

Use (1.6) with \(\alpha=\beta\) and \(Y\) from (1.7). For each contractive base, (1.2) gives

\[
|A_{v w^6}(D_j;W_*)-A_v(D_j;W_*)|
\le |A_v(D_j;W_*)|K_\beta(w)
\le \tfrac12|A_v(D_j;W_*)|.
\]

At least \(cD_j^{h/6}\) distinct allowed rows therefore have absolute value at least \(\tfrac12|A_v(D_j;W_*)|\). Their contribution to the nonnegative moment is at least
\(c\,2^{-2k}D_j^{h/6}|A_v(D_j;W_*)|^{2k}\).
Dividing by the denominator in (2.3) gives a fixed positive multiple of \(F(D_j)^{2k}\to\infty\). \(\square\)

Relative to PR 912, the denominator in the forced spike is larger by \(\log D\), and the replica population has positive density among all allowed sixth-power bases. This is a logarithmic strengthening; it changes no extraction power.

## 3. A larger exceptional set is now permitted

**Theorem 3.1.** Fix \(\alpha>0\), \(C_0>0\), and \(h>0\). Suppose, at every sufficiently large \(D\),

\[
\boxed{\displaystyle
\#\{u:0<Nu\le D^h,\ |A_u(D;W_*)|>C_0D^\alpha\}
=o(D^{h/6}).}
\tag{3.1}
\]

Then for every fixed \(v\ne0\),
\(A_v(D;W_*)=O_{v,\alpha,C_0,h}(D^\alpha)\), and every fixed twist \(\psi_v\) is zero-free in \(\Re s>\alpha\).

**Proof.** Fix \(v\), and choose \(Q\) and its contractive bases as in Section 1. Their number is at least \(c_vD^{h/6}\), so (3.1) leaves a contractive base for which
\(|A_{vw^6}(D;W_*)|\le C_0D^\alpha\).
Rearrange (1.2). Under the inductive bound
\(|A_v(x;W_*)|\le Cx^\alpha\) at smaller scales, it gives

\[
|A_v(D;W_*)|
\le C_0D^\alpha+
C D^\alpha K_\alpha(w)
\le (C_0+C/2)D^\alpha.
\tag{3.2}
\]

Every nonunit ideal in the recurrence has norm at least two, so all smaller scale arguments are at most \(D/2\). Choose \(C\ge2C_0\), and enlarge it to handle the fixed starting interval. Dyadic induction closes (3.2). Equation (2.2) then gives zero exclusion. \(\square\)

An exact sufficient condition is that the exceptional count be smaller than
\(|\mathcal G_{\alpha,Q}((D^h/Nv)^{1/6})|\); condition (3.1) conveniently works for every fixed \(v\) without uniformity of the constants in \(v\). It improves PR 912's sufficient condition \(o(D^{h/6}/\log D)\). The new condition remains an unproved arithmetic input for any \(\alpha\) below the established cancellation range.

There is also an endpoint statement without an epsilon or logarithmic loss.

**Corollary 3.2.** If, for some fixed \(p\ge1\) and \(\alpha>0\),

\[
\sum_{0<Nu\le D^h}|A_u(D;W_*)|^p
\ll D^{p\alpha+h/6},
\tag{3.3}
\]

then \(A_v(D;W_*)\ll_v D^\alpha\) for every fixed \(v\).

**Proof.** Average the rearranged recurrence (1.2) over all \(\mathcal V_Q(Y)\), with \(Y\) from (1.7). Hölder's inequality and \(J_Q(Y)\asymp_v D^{h/6}\) bound the mean of \(|A_{vw^6}(D)|\) by \(C_vD^\alpha\). The average recurrence kernel is at most \(1/4\) by (1.5). Thus the same induction gives
\(|A_v(D)|\le(C_v+C/4)D^\alpha\), which closes for sufficiently large fixed \(C\). \(\square\)

If the right side of (3.3) has an arbitrary \(D^\epsilon\) loss, the conclusion is \(A_v(D)\ll_{v,\epsilon}D^{\alpha+\epsilon}\), with the usual rescaling of the requested loss. This corollary extends the earlier rough-base endpoint extraction from the untwisted row to every fixed sextic twist and the one universal test.

## 4. A finite-moment profile, conditional on the imported second moment

This is a consolidation of PR 912's moment-growth characterization and its interpolation argument, rather than a new high-moment arithmetic estimate.

For the fixed \(\nu\)-twist family, let

\[
B_\nu=\sup\{\Re\rho:\ L_K(\rho,\psi_v)=0,\
0<\Re\rho<1,\ v\ne0\},
\qquad \frac12\le B_\nu\le1,
\]

\[
M_{2k}(D;h)=\sum_{0<Nu\le D^h}|A_u(D;W_*)|^{2k},
\qquad
\Lambda_{2k}(h)=\limsup_{D\to\infty}
\frac{\log M_{2k}(D;h)}{\log D}.
\tag{4.1}
\]

The convention is \(\log0=-\infty\).

At this chosen fixed \(h\), assume the inherited all-row second-moment assertion

\[
M_2(D;h)\ll_\epsilon D^{h+1+\epsilon}
\quad\hbox{for every }\epsilon>0.
\tag{4.2}
\]

For the intended application, this is the imported second moment at \(h=1+\theta\); no assertion of its availability for arbitrary small \(h\) is made.

Use also PR 912's stated uniform reciprocal theorem, its polynomial conductor bound, and its deleted-Euler-factor bound. They imply

\[
\max_{0<Nu\le D^h}|A_u(D;W_*)|
\ll_\epsilon D^{B_\nu+\epsilon}
\tag{4.3}
\]

when \(B_\nu<1\); for \(B_\nu=1\), elementary coefficient counting gives the endpoint estimate. This is uniform over moving rows and masks, and does not follow merely from separate bounds with uncontrolled conductor constants.

**Corollary 4.1.** Under these explicitly stated inputs, every fixed integer \(k\ge1\) satisfies

\[
\boxed{\displaystyle
2kB_\nu+\frac h6
\le \Lambda_{2k}(h)
\le h+1+2(k-1)B_\nu.}
\tag{4.4}
\]

**Proof.** For every zero of every fixed twist, Theorem 2.1 gives
\(\Lambda_{2k}(h)\ge2k\beta+h/6\), for every positive \(\beta\) below its real part. Take the supremum over these real parts. For the upper bound, multiply (4.2) by the \((2k-2)\)-th power of (4.3), then let the freely chosen epsilon losses tend to zero. \(\square\)

Consequently

\[
\lim_{k\to\infty}\frac{\Lambda_{2k}(h)}{2k}=B_\nu.
\tag{4.5}
\]

PR 912 already proved this limit using the weaker upper bound \(2kB_\nu+h\). Equation (4.4) tightens its finite-\(k\) upper end by \(2B_\nu-1\) through the imported second moment. It does not improve the limiting characterization, and using its own upper bound for extraction cannot improve the known boundary \(B_\nu\).

In particular, a hypothetical estimate
\(M_{2k}(D;h)\ll_\epsilon D^{k+h+e_k+\epsilon}\)
still yields precisely

\[
\Re s>\frac12+\frac{5h}{12k}+\frac{e_k}{2k}.
\tag{4.6}
\]

An unbounded sequence of fixed orders with \(e_k/k\to0\) would imply GRH for this twist family, as already clarified by PR 912. Positive-density replication removes the logarithmic shortage of prime replicas; the number of actual sixth-power replicas remains \(O(D^{h/6})\), so this composition supplies no further power saving.
