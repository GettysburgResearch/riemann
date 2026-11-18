# Independent source review: Knopp/Hamburger normalization and a later background attribution

Reviewer: equivalences. Date: 2026-11-17. Requested as an independent reconstruction; I did **not** read li_advocate's conclusions before deriving the variable/frequency correspondence and the converse-theorem implication below. No author's main theorem is characterized as false in this review.

## Source scope and evidence

Actual primary passages inspected, including page images to resolve OCR:

* Marvin I. Knopp, *Hamburger's Theorem on ζ(s) and the Abundance Principle for Dirichlet Series with Functional Equations*,2000, printed pp201–204 and211–212, plus contextual paragraphs/references. Private `sources/hamburger_round3/knopp2000.pdf`, extracted text and page images. **Partial reading**, not a whole16-page read or complete audit of its modular-integral construction.
* Takashi Nakamura, *Dirichlet series with periodic coefficients, Riemann's functional equation and real zeros of Dirichlet L-functions*, arXiv2008.02570**v4**,10September2021, actual p4 TheoremD,H1–H3,K and surrounding paragraph/Corollary2.2; definitions on pp1–3 and the corollary proof p7. **Targeted reading**, not a whole-paper audit.
* Jean-François Burnol, *Deux extensions de Théorèmes de Hamburger*, arXiv1106.4749**v2**,7January2012, actual pp2–3 Theorem1 and Corollary2. **Statement/hypothesis inspection**, not an audit of Burnol's distribution-theoretic proof.

Primary-source files are private. This review adds no selected work, no new whole-work reading, and no whole-paper L2 classification. At the time of the initial reconstruction, Knopp's original1994 paper had not been obtained. The addendum below supersedes that statement-access limitation: original pp361–363 were subsequently viewed directly from GDZ images, after the independent derivation was complete. The full1994proof remains unread.

## 1. What Knopp actually normalizes

The equations visibly printed on Knopp p201 are

\[
 R(u)=\pi^{-u}\Gamma(u)\varphi(u),\qquad
 R(u)=R(\tfrac12-u).
\]

I use \(u\) here to avoid hiding the change of variable under repeated use of \(s\). Knopp distinguishes:

* condition3(a): both \(\varphi(u)\) and **\(\varphi(u/2)\)** possess ordinary Dirichlet-series expansions. The displayed consequence is \(\varphi(u)=\sum b(n)n^{-2u}\). Together with finite-genus/pole hypotheses and the functional equation, the unique class is a multiple of \(\zeta(2u)\).
* condition3(b): only \(\varphi(u)\) must have an ordinary expansion, but its only allowed pole is the simple pole at \(u=1/2\).
* the abundance setup: relax both extra requirements, retaining finite-genus after clearing finitely many poles, the same completed functional equation, and an ordinary expansion of \(\varphi(u)\) in some right half-plane.

This is not an ambiguous use of “Dirichlet series”: p211 explicitly contrasts the **ordinary** series used there with Bochner's generalized Dirichlet series. Its Mellin-transform display is

\[
 \Phi(u)=\int_0^\infty\{F(iy)-a_0\}y^u\frac{dy}{y}
       =\pi^{-u}\Gamma(u)\sum_{n\ge1}a_n n^{-u}.
\]

The detailed abundance theorem on p212 retains \(R(u)=R(1/2-u)\). The parameter boundary and rational principal-part strip are written with non-strict inequalities in the page image, unlike a few OCR characters. That detail is not needed for the frequency comparison, but the scan should control any exact theorem transcription.

Knopp pp203–204 also explicitly explains that passing from the classical Hamburger functional equation to this form amounts to replacing the original variable by twice the new one. Thus the factor2 is part of the author's own explanation, not an inferred convention introduced by this review.

## 2. Independent variable and frequency calculation

To reach Nakamura's standard zeta completion, put

\[
 t=2u,\qquad F_\mathrm{std}(t)=\varphi(t/2),\qquad
 \Xi_{F_\mathrm{std}}(t)=\pi^{-t/2}\Gamma(t/2)F_\mathrm{std}(t).
\]

Then

\[
 \Xi_{F_\mathrm{std}}(t)=R(t/2),\qquad
 \Xi_{F_\mathrm{std}}(1-t)=R((1-t)/2)=R(t/2).
\]

So the standard functional equation is recovered **exactly**. But if the abundance condition gives

\[
 \varphi(u)=\sum_{n\ge1}b_n n^{-u},
\]

then

\[
 F_\mathrm{std}(t)=\sum_{n\ge1}b_n n^{-t/2}
                 =\sum_{n\ge1}b_n(\sqrt n)^{-t}.
\]

The frequencies are \(\sqrt n\), not the positive integers. Conversely an ordinary standard-zeta series \(F_\mathrm{std}(t)=\sum a_m m^{-t}\) corresponds to \(\varphi(u)=\sum a_m m^{-2u}\), i.e. Knopp coefficients supported on square indices. The function \(\zeta(2u)\) is precisely the basic square-supported case.

**Why the support assertion cannot be evaded by a different expansion.** Ordinary convergence somewhere implies absolute convergence in a farther-right half-plane: convergence at a real \(u_0\) bounds \(b_n n^{-u_0}\), so \(|b_n|\ll n^{u_0}\) and the absolute series converges for \(\Re u>u_0+1\). Both the generalized expansion above and any putative ordinary expansion therefore converge absolutely on a common far-right half-plane. Their difference has the locally finite ordered frequency set \(\{\sqrt n\}\cup\mathbb N\). Uniqueness follows by taking the smallest frequency with a nonzero combined coefficient, multiplying by its \(t\)-power, and letting real \(t\to+\infty\); dominated convergence at one fixed convergence abscissa makes the remaining tail vanish. Every nonsquare coefficient must consequently vanish. Thus

\[
 F_\mathrm{std}\text{ has an ordinary expansion}
 \quad\Longleftrightarrow\quad b_n=0\text{ for every nonsquare }n.
\]

The regularity hypothesis after multiplication by a polynomial transfers under linear rescaling. The obstruction is the frequency class, not finite order/genus.

## 3. Exact later passage being compared

Nakamura v4p4, TheoremD, states the classical standard-variable completion:

\[
\begin{array}{ll}
\mathrm{H1}:&F(t)=\sum_{n\ge1}a(n)n^{-t},\ \text{absolutely convergent for }\Re t>1;\\
\mathrm{H2}:&P(t)F(t)\ \text{entire of finite order for a suitable nonzero polynomial }P;\\
\mathrm{H3}:&\Xi_F(1-t)=\Xi_F(t),\quad\Xi_F(t)=\pi^{-t/2}\Gamma(t/2)F(t).
\end{array}
\]

The paragraph immediately below says that Knopp[7,Theorem1] supplies infinitely many linearly independent solutions satisfying H2,H3 and

\[
\mathrm K:\qquad F(t)=\sum_{n\ge1}a(n)n^{-t}
\quad\text{absolutely convergent in some half-plane}.
\]

The actual p4 image confirms both \(n^{-t}\) and \(\Gamma(t/2)\); these are not lost OCR exponents. Nakamura's reference[7] is Knopp1994, *On Dirichlet series satisfying Riemann's functional equation*, Invent.Math117(1994),361–372. Knopp2000p212 explicitly identifies its own detailed Theorem1 as that result.

The literal conjunction H2+H3+ordinaryK is incompatible with the converse result inspected next. This is a background attribution/normalization problem; it is distinct from the explicit main constructions in the same paper.

## 4. Independent hypothesis match to Burnol: why a weaker abscissa alone does not create abundance

Burnol v2pp2–3 uses

\[
 \chi_B(t)=\frac{\pi^{-(1-t)/2}\Gamma((1-t)/2)}{\pi^{-t/2}\Gamma(t/2)},
 \qquad g(t)=\chi_B(t)f(1-t).
\]

Theorem1 assumes an ordinary series \(f(t)=\sum a_n n^{-t}\) converging sufficiently far right, and:

1. meromorphic continuation with finitely many poles;
2. on every finite-width vertical strip, for each \(\epsilon>0\),
   \(f(t)=O(\exp(\exp(\epsilon|t|)))\) as \(|\Im t|\to\infty\);
3. some \(N\in\mathbb N\), \(y>1/2\), with \(g(t)=O(|t|^N y^{-t})\) as \(\Re t\to+\infty\).

Corollary2 adds

4. for real \(\sigma\to+\infty\), \(g(\sigma)=c+O(\sigma^{-k})\) for every \(k\in\mathbb N\),

and concludes \(f(t)=c\zeta(t)\).

Now suppose the literal H2,H3,K hold.

* H2 gives finitely many poles and finite-order growth after clearing them. In a fixed vertical strip at large height, the polynomial denominator is bounded below by a polynomial in height; finite-order growth \(\exp(C|t|^d)\) is smaller than \(\exp(\exp(\epsilon|t|))\) for every positive \(\epsilon\). Thus1,2 hold.
* H3 gives \(g=f\) identically as meromorphic functions; no conjugation is introduced.
* Choose a real \(\sigma_a\) of absolute convergence. Uniformly for \(\sigma\ge\sigma_a\) and all imaginary parts,
  \[
   |f(\sigma+i\tau)-a_1|
   \le\sum_{n\ge2}|a_n|n^{-\sigma_a}2^{-(\sigma-\sigma_a)}
   =C\,2^{-(\sigma-\sigma_a)}.
  \]
  Hence \(g=f\) is bounded in a right half-plane, verifying3 with \(y=1\) and, if the convention excludes0 from \(\mathbb N\), \(N=1\).
* Along the real axis the same exponential bound is \(O_k(\sigma^{-k})\) for every fixed \(k\), verifying4 with \(c=a_1\).

Burnol Corollary2 therefore gives

\[
 \boxed{\mathrm{H2+H3+ordinaryK}\ \Longrightarrow\ F(t)=a_1\zeta(t).}
\]

The class is at most one dimensional, not infinitely dimensional. This implication is a direct, exact hypothesis match to an established primary theorem; it does not require estimating the original convergence abscissa by1. It also remains true if K initially means ordinary convergence without the word “absolute”, because one can move the convergence line to the right as above. This does not assert that Hamburger1921 himself proved this weaker-abscissa extension under every modern formulation; the proof invoked here is Burnol's stated extension.

## 5. Alternative interpretations tested

1. **Implicit rescaling of all notation.** The word “Riemann's functional equation” sometimes covers Knopp's \(u\)-normalization. Reading the abundance sentence in that convention is mathematically sound, but then its displayed H3 must become \(\pi^{-u}\Gamma(u)\) with reflection \(1/2-u\). Retaining Nakamura's explicitly defined H3 while rescaling only the prose does not work.
2. **Generalized series intended in K.** With \((\sqrt n)^{-t}\), or more generally positive frequencies, the abundance attribution is consistent with Knopp. Replacing the printed \(n^{-t}\) by those generalized frequencies repairs this background comparison. The printed n=1,2,… expansion is otherwise unambiguous and uses the same convention as H1.
3. **A special square-supported infinite family.** This cannot rescue the literal sentence: square support makes both \(\varphi(u/2)\) ordinary and its transformed standard function ordinary. It restores precisely the restrictive Hamburger class; Burnol gives only scalar zeta multiples.
4. **Weak convergence or large abscissa.** Moving the abscissa changes neither the integer frequency set nor the exponential approach to \(a_1\) on the far right. It cannot rescue the literal H2,H3,K conjunction.
5. **Finite genus versus finite order.** A finite-genus entire function is of finite order in the standard factorization setting used by Knopp; even accepting only Nakamura's explicit finite-order H2 already yields the contradiction above. This distinction does not supply the missing infinite-dimensional class.
6. **Completed versus uncompleted pole conditions.** Gamma introduces additional completed-function poles, but H2 is imposed on the uncompleted function and Knopp likewise imposes finite-genus after clearing its finitely many poles. This is compatible under rescaling; it is not the missing frequency hypothesis. Removing finite-pole regularity altogether would be a genuine different way to evade Burnol, relevant to the explicit g below.

Thus there is a clear normalization/frequency repair, but no literal interpretation preserving all three displayed standard-variable assumptions and the claimed infinite-dimensional conclusion. The1994 original and any later revised journal wording should still be compared before a final public history-of-corrections statement.

## 6. Why this does not refute Nakamura's explicit constructions

For a nontrivial primitive even character \(\chi\pmod q\), \(q>1\), Nakamura defines

\[
 f_\chi(t)=q^tL(t,\chi)+G(\chi)L(t,\overline\chi).
\]

This is finite order (indeed entire for nonprincipal primitive characters), and satisfies the standard functional equation. But its series has frequencies \(n/q\) and \(n\), not only integers. The leading frequency \(1/q<1\) has coefficient1 and cannot cancel against the second series. Equivalently \(f_\chi(\sigma)\sim q^\sigma\) as real \(\sigma\to+\infty\), whereas any ordinary series convergent in some right half-plane tends to its coefficient at1. So this explicit f violates not just H1's specific abscissa requirement but **ordinaryK itself**. That is a frequency-class escape from the converse theorem, not a counterexample to it.

Corollary2.2 instead sets

\[
 H(t,q)=(q^t+q^{1-t})^{-1},\qquad g_\chi=Hf_\chi.
\]

Here \(H(1-t,q)=H(t,q)\), so standard H3 is retained. Also

\[
 q^tH(t,q)=\frac1{1+q^{1-2t}}
 =\sum_{k\ge0}(-q)^k(q^{2k})^{-t},\quad\Re t>1/2.
\]

Multiplying this absolutely convergent geometric series by the ordinary series for \(q^{-t}f_\chi\), absolutely convergent for \(\Re t>1\), proves the ordinary H1 claim. The declared regularity condition is now

\[
 \mathrm D:\quad D(t)g_\chi(t)\text{ entire of finite order for a Dirichlet polynomial }D,
 \qquad D(t)=1+q^{1-2t}.
\]

This is **not** H2. A nonconstant Dirichlet polynomial has infinitely many complex zeros and can clear infinitely many poles; a polynomial in t has only finitely many zeros. No inference \(D\Rightarrow H2\) is valid. The source expressly states D, not H2, for g.

A concrete check makes the escape visible without any unproved zero assertion. Take the primitive even quadratic character mod5, for which \(G(\chi)=\sqrt5\). Then

\[
 g(t)=\frac{1+\sqrt5\,5^{-t}}{1+5\,25^{-t}}L(t,\chi).
\]

Its ordinary-series coefficients at1 and2 are1 and−1. Hence it cannot equal \(c\zeta(t)\). If only finitely many poles of this g survived, clearing those poles would produce an entire finite-order function, putting g under H2,H3,K and contradicting the verified implication above. The finite-order assertion after finite-pole clearing can be checked directly: outside fixed small disks about the regularly spaced zeros of \(1+5e^{-2t\log5}\), its reciprocal has at most exponential growth in a finite strip and is bounded appropriately in either far half-plane; inside canceled-zero disks the maximum principle transfers the boundary bound. Thus infinitely many poles must remain for this concrete example. This derived observation does not locate which denominator zeros cancel and is not attributed as a new result.

The explicit constructions therefore evade different hypotheses exactly as needed. The normalization problem in the background Knopp attribution does not, by itself, produce a counterexample to Theorem2.1 or Corollary2.2.

## Outcome, classification and limits

* Independently checked: Knopp-to-standard rescaling; square-frequency restriction; all BurnolCorollary2 hypotheses for literal H2,H3,K; distinction between f's generalized frequencies and g's Dirichlet-polynomial pole clearing.
* Source comparison finding: **a later background attribution requires a normalization/frequency correction**. The exact literal conjunction as printed conflicts with the inspected converse theorem. Treat this as a narrowly scoped source-interpretation/attribution issue for parent/expert adjudication, not an assertion that the author's main explicit theorem is false.
* Not checked here: Knopp1994 original proof, Knopp2000 full modular-integral construction, Burnol distribution-theoretic proof, complete Nakamura main theorem, journal-version correction history.
* No RH claim, no novelty claim, no numerical agreement offered as proof, and no new whole-work read count.


## Addendum: original1994 statement now directly inspected

After completing and saving the independent reconstruction above, li_advocate located the original1994scan through EuDML→GDZ. I directly viewed the shared images `knopp1994_pdf367.jpg`, `knopp1994_pdf368.jpg`, `knopp1994_pdf369.jpg`, corresponding to printed pp361–363, in `sources/hamburger_round3/`. This adds three targeted original-source pages, **not** a whole12-page reading or proof audit.

Original p361 visibly defines R(s)=π^(−s)Γ(s)φ(s) and reflects1/2−s. Original p362 condition3(a) explicitly distinguishes ordinary φ(s/2), displaying φ(s)=Σb(n)n^(−2s), from condition3(b)'s ordinary φ(s)=Σa(n)n^(−s). The new relaxed condition3 retains only ordinary φ(s) in some right half-plane. Original Theorem1 on that same page uses R(s)=π^(−s)Γ(s)φ(s), preserving those conditions; its finite-codimension rational-principal-part abundance statement has σ0≥1/4 and the closed strip1/2−σ0≤Re(s)≤σ0. Original p363 continues the weight-k generalization and correspondence.

Thus the1994 original statement agrees with the2000author chapter on the exact normalization. The possibility that the2000restatement alone introduced a factor2 has now been checked and excluded at the statement level. Remaining limitations are the original construction proof and Nakamura's later journal/revision wording; no correction-history conclusion is asserted.
