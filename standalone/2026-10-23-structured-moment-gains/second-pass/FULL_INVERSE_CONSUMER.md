# Consumer for a genuinely improved full inverse moment

Status: proved implication; the stronger input below is not claimed proved here.

Scope: the Eisenstein field \(F=E=\mathbb Q(\omega)\), with primary ideal
generators and its finite unit sectors as in the pinned OpenAI source
below. Use its full sextic row family, natural zeros, and coefficient
characters. An unrestricted element-by-norm sum over a field with
infinitely many units is not intended. No truncated core or diagonal-only
estimate meets the hypothesis.

Exact primary source for this field and its row convention:
[OpenAI, pinned paper.tex](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
labels `eq:raw-moment`, `lem:inverse-amplification`,
`eq:inverse-scale-supremum`, and `eq:sixth-power-column-identity`.
The elementary amplification identity is also (10.16) in
[Liu, arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1#S10.SS4),
in that paper's stated cyclotomic setting. Liu's field hypothesis is not
silently identified with the Eisenstein field here. The proof below uses
the displayed stronger full-moment estimate as a hypothesis.

## 1. Input and conclusion

Write

\[
 M_k^W(D)=D^{-1/2}\sum_n\mu_F(n)\nu(n)\chi_n(k)W(Nn/D).
\]

Here ideals and finite unit classes have the source normalization, \(\nu\)
is a fixed finite-order coefficient character with conductor supported in the
fixed set \(S\), and the characters have their natural zero extensions.

For \(\alpha>0\), assume **the full moment**

\[
 \sum_{0<Nk\le H}|M_k^W(D)|^2
 \ll_{c,\epsilon,W,F,S,\nu}H(HD)^\epsilon,
 \qquad H\ge\max(2,D^{\alpha+c}),                 \tag{1}
\]

for every \(c,\epsilon>0\) and every smooth annular test \(W\), uniformly
on bounded families measured by fixed finite smooth seminorms. In
particular this includes the scale derivatives below and the families
\(W_s(y)=W(y)y^{-s}\) for \(s\) in any fixed compact subset of
\(\mathbb C\). This latter uniformity is needed for the holomorphic
reciprocal deduction, not just the scale supremum. Every row is retained,
including sixth powers and powerful ideals. Natural-zero punctures remain
present.

Then, for every \(\epsilon>0\),

\[
 \sum_n\mu_F(n)\nu(n)W(Nn/D)
 \ll D^{\frac12+\frac{5\alpha}{12}+\epsilon}.  \tag{2}
\]

Consequently the corresponding Hecke function has no zeros in

\[
 \Re s>\frac12+\frac{5\alpha}{12}.              \tag{3}
\]

This implication is useful only when the right-hand side is below an
already available boundary. Principal poles at \(s=1\) are allowed.

For sixth-power-free rows \(u\), uniformly on any fixed bounded range of
\(r\ge0\), (1) also gives

\[
 \sum_{U\le Nu\le2U}^{(6)}|M_u^W(U^r)|^2
 \ll U^{e_\alpha(r)+\epsilon},\qquad
 e_\alpha(r)=\max\left(1,\frac{1+5\alpha r}{6}\right). \tag{4}
\]

## 2. Proof with the punctures retained

Put \(T_0=(\sup\operatorname{supp}W)^{-1}\). The sum is zero below \(T_0\),
and differentiation in \(\log T\) replaces \(W\) by

\[
 W^{[1]}(y)=-\tfrac12W(y)-yW'(y).
\]

Sobolev on unit logarithmic intervals, followed by (1), gives

\[
 \sum_{Nk\le H}\sup_{T_0\le T\le D}|M_k^W(T)|^2
 \ll H(HD)^\epsilon                              \tag{5}
\]

when \(H\ge (eD)^{\alpha+c}\); reducing the fixed positive gap absorbs
the harmless factor \(e\). Bounded columns are handled directly.

For each exterior ideal \(a\), the pinned source's
`eq:sixth-power-column-identity` is the exact identity

\[
 M_u^W(D)=\sum_{d\mid\operatorname{rad}a}
 \mu_F(d)\nu(d)\chi_d(u)(Nd)^{-1/2}
 M_{ua^6}^W(D/Nd).                              \tag{6}
\]

At a prime dividing \(u\), the terms involving that prime have the same
zero extension on both sides. At a prime dividing \(a\), multiplication by
the missing Euler factor restores the original inverse Euler factor.
Thus (6) does not replace a punctured character by its primitive character.
Its absolute divisor mass is

\[
 \prod_{p\mid a}(1+(Np)^{-1/2})\ll_\epsilon (Na)^\epsilon. \tag{7}
\]

For \(u=1\), average (6) over \(\gg H^{1/6}\) ideals \(a\) with
\(Na\le H^{1/6}\). Equations (5)–(7) imply

\[
 |M_1^W(D)|^2\ll H^{5/6}(HD)^\epsilon.
\]

Choose \(H=D^{\alpha+c}\), then let the positive gaps and losses be as
small as the requested \(\epsilon\). This proves (2). A smooth dyadic
partition shows that the inverse Dirichlet series extends holomorphically
to (3). Its identity with \(1/L_F^S(s,\nu)\) in \(\Re s>1\), followed by
the identity theorem, proves zero-freeness. Deleted finite Euler factors
have no zeros in this half-plane.

For (4), choose \(H\asymp\max(U,D^{\alpha+c})\), with a sufficiently large
fixed constant. Average (6) over
\(\gg(H/U)^{1/6}\) possible \(a\). The map \((u,a)\mapsto ua^6\) is
injective when \(u\) is sixth-power-free, with the fixed finite unit
conventions retained. Thus

\[
 (H/U)^{1/6}\sum_u|M_u^W(D)|^2
 \ll H(HD)^\epsilon.
\]

The resulting \(U^{1/6}H^{5/6}\), with \(D=U^r\), is precisely (4).

## 3. Quantitative targets and the iteration qualification

If (1) were proved with \(\alpha=B_{\rm flat}\), the conclusion would be

\[
 B_{\rm new}=\tfrac12+\tfrac5{12}B_{\rm flat}
 =0.864536102933318\ldots .                       \tag{8}
\]

If it were proved with \(\alpha=4/5\), the conclusion would be \(B=5/6\).
These are implications from a full estimate, not claims obtained from the
short-core estimate or from canceling one reflected diagonal.

Suppose more strongly that a common all-character zero-free bound \(\beta\)
implies (1) with \(\alpha=\beta\), for **each fixed finite-order \(\nu\)**.
Then (3) improves that same common family bound by

\[
 \beta\longmapsto\tfrac12+\tfrac5{12}\beta.
\]

Iteration from \(B_{\rm flat}\) tends to the fixed point \(6/7\). For any
\(\sigma>6/7\), finitely many iterations suffice to put the common bound
below \(\sigma\), so the open half-plane \(\Re s>6/7\) follows under this
full bridge hypothesis. A theorem restricted to \(\nu=1\) does not justify
this iteration: its improved principal bound cannot replace the common
Hecke-family bound used in a subsequent reciprocal completion argument.

For the Riemann zeta function alone, a one-step principal result over
\(E\) suffices, since
\(\zeta_E(s)=\zeta(s)L(s,\chi_{-3})\). A zero of \(\zeta\) in the open
positive half-plane cannot be canceled by a pole of the nonprincipal
Dirichlet factor, which is entire.

## 4. Where this meets the current scalar comparison

The presently active formal detected class has approximately

\[
 \delta=0.4693448587,\quad t=1.1639535765,\quad
 r=0.7456999427,\quad m=0.4182536338.
\]

These numbers describe the existing optimizer; they do not prove a new
estimate. Formula (4) changes its long inverse input directly. For
\(\alpha<22/25\), however, the direct boundary (3) is already below
\(13/15\), the minimum of the existing low-side envelope
\(\max(11/12-\ell/4,\,2/3+\ell)\). A new full raw inverse theorem in that
range therefore has a simpler consumer than re-optimizing the old theta
comparison.
