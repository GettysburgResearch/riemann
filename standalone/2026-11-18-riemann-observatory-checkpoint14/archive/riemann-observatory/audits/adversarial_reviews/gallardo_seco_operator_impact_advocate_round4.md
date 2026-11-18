# Independent operator classification and dependency impact for Gallardo–Gutiérrez–Seco2025

Reviewer: li_advocate. Date: 2026-11-17. The coefficient proof below was reconstructed before reading the other agents' operator-repair proofs. No outreach. No claim that the paper's principal RH/zero-free assertions are false.

## Actual primary source and exact restrictions

Canonical work: PAPER-E012, *Zero-Free Regions of the Riemann Zeta Function and Approximation in Weighted Dirichlet Spaces*, Eva A. Gallardo-Gutiérrez and Daniel Seco, Complex Analysis and Operator Theory19(2025), article38, DOI10.1007/s11785-025-01661-2. Actual publisher PDF inspected: `sources/logarithmic_riesz_round3/gallardo_seco2025.pdf`.

Visually checked publisher p3 (coefficient norm), p21 (Proposition5.1), p26 (Theorem5.5 and Lemma5.3), and read the proof text pp21–25 plus Theorem2.1's statement on p5. This is targeted technical reading, not a whole27-page journal audit. The arXiv2206.02654v6 p17 Proposition5.1 was also visually checked in its actual primary page image; its endpoint condition agrees with the publisher text. Theorem5.5's v6 text was compared to the publisher statement. No claim of a corrected later version is made.

The actual norm is

    ||f||_γ²=sum_{n≥0}(n+1)^γ |f_n|².

Proposition5.1 assumes α∈[−3,−2), a>0, and defines

    T_a f=f'−a f/(1−z): D_{α+2}→D_α.

It prints bounded bijectivity iff a≥−(α+1)/2. The auxiliary T_{a,h}=M_hT_a is asserted to have the same property when h is bounded holomorphic and bounded away from0 onD.

Publisher p26 **visibly includes** α=−3: Theorem5.5 assumes α∈[−3,−2] and a∈[1,(1−α)/2). This is not inferred from OCR punctuation.

## Correct classification

Put

    β=α+2,    t=−(α+1)/2=(1−β)/2,    δ=a−t.

For the source range, and in fact for every α<−1 and a>0:

| Parameter | Kernel | Range |
|---|---|---|
| a<t | span{(1−z)^{−a}} | allD_α; bounded right inverse exists |
| a=t | zero | dense, proper, nonclosed |
| a>t | zero | allD_α; bounded inverse exists |

The operator itself is bounded throughout. Thus the minimal correction to the bounded-bijection condition is **a>t**, not a≥t. A bounded invertible multiplier h transfers this entire classification to T_{a,h}.

## 1. Boundedness and the weighted Hardy estimates

For β<1, the derivative D:D_β→D_{β−2} is bounded directly from coefficients. Multiplication by1/(1−z) takes f_n to F_n=sum_{j≤n}f_j. Its boundedness follows from the weighted Hardy inequality

    sum_n(n+1)^{β−2}|F_n|²
       ≤C_β sum_n(n+1)^β|f_n|².

Here is a direct Schur-test proof of the form of Hardy inequality needed below. For r>0, the prefix matrix

    K_{nk}=n^{−r−1/2}k^{r−1/2}1_{k≤n}

is bounded onℓ²: use Schur weights w_n=n^{−1/2}; the row sum reduces to n^{−r−1/2}sum_{k≤n}k^{r−1}, and the column sum to k^{r−1/2}sum_{n≥k}n^{−r−1}. Both are bounded by a constant depending onr times w_n orw_k. The tail matrix

    L_{nk}=n^{r−1/2}k^{−r−1/2}1_{k≥n}

is bounded by the same argument with prefix/tail interchanged. Shifts by1 change constants only. Taking r=(1−β)/2 proves the multiplication estimate, hence boundedness of T_a for every a>0.

## 2. Exact coefficient recurrence

Define

    h_n=(a)_n/n!,
    H_n=(a+1)_n/n!=sum_{j=0}^n h_j,
    F_n=sum_{j=0}^n f_j,
    u_n=F_n/H_n.

The equation T_af=g has coefficients

    g_n=(n+1)F_{n+1}−(n+1+a)F_n.

Thus, with d_n=g_n/[(n+1)H_{n+1}],

    u_{n+1}−u_n=d_n,
    u_n=c+sum_{k=0}^{n−1}d_k.

For n≥1,

    f_n=h_n u_n+g_{n−1}/(n+a),                        (R)

and f0=c. The second term of(R) is always bounded from D_α toD_β. For fixeda>0,

    h_n asymp n^{a−1},    H_n asymp n^a.

If b_k=(k+1)^{α/2}g_k, then d_k is comparable to b_k(k+1)^{−δ−1/2}, while the squared domain weight of h_nu_n is comparable to(n+1)^{2δ−1}|u_n|².

If δ<0, set c=0 and use the prefix Hardy estimate with r=−δ to obtain a bounded right inverse. If δ>0, the series sum d_k converges by Cauchy–Schwarz; set c=−sum d_k, so u_n=−sum_{k≥n}d_k. The tail Hardy estimate with r=δ gives a bounded inverse. All small-index terms are controlled by fixed constants; no limiting uniformity in δ→0 is claimed.

Every homogeneous analytic solution is c(1−z)^{−a}. It belongs toD_β iff

    sum n^{β+2a−2}<∞,

equivalently a<t. This proves the stated kernel classification and completes the off-critical surjectivity/bijectivity proof.

## 3. Critical approximate-null polynomials and explicit missing range data

At a=t, h=(1−z)^{−a} has divergent domain norm at the harmonic-series boundary. Let

    P_N(z)=sum_{n=0}^N h_n z^n.

The exact coefficient recurrence gives

    T_aP_N=−aH_N z^N/(1−z).

At the critical relation α+2a=−1,

    ||P_N||_β² asymp logN,
    ||T_aP_N||_α²=a²H_N²sum_{n≥N}(n+1)^α=O(1).

Therefore P_N/||P_N|| is an explicit unit sequence whose images tend to0. Since the critical kernel is zero, T_a is not bounded below, hence its range is not closed. Its range contains every polynomial: for polynomialg, choose c=−sum d_k (a finite sum), making u_n=0 eventually and f a polynomial whose coefficients sum to0. The range is consequently dense. It cannot be onto, since a bounded injective onto map between these Hilbert spaces would have a bounded inverse.

There is also an explicit g outside the critical range. Put

    d_n=1/[(n+2)log(n+2)],
    g_n=(n+1)H_{n+1}d_n.

At criticality its codomain norm is comparable to sum_{n≥2}1/[n(logn)²], hence finite. Every analytic solution has

    f_n/h_n=c+sum_{k<n}d_k+n d_{n−1}/a.

The real part tends to+∞ regardless of the constantc, while(n+1)^βh_n² is comparable to1/n. Thus no such solution belongs toD_β. The series for g is analytic onD since its coefficients have only polynomial growth. This proves proper range without relying solely on the inverse-mapping theorem.

### Exact source endpoint α=−3,a=1

Here β=−1 and P_N=1+z+...+z^N. Then

    ||P_N||_{−1}²=H_{N+1},
    T_1P_N=−(N+1)z^N/(1−z),
    ||T_1P_N||_{−3}²
       =(N+1)²sum_{m≥N+1}m^{−3}
       ≤1/2+1/(N+1).

This is a direct counterexample to a bounded inverse at a parameter pair actually included in the printed proposition. It is not a counterexample to an RH assertion.

## 4. Exact dependency impact on Theorem5.5

For Theorem5.5's parameter range, t∈[1/2,1] and a≥1. Thus its use of the critical equality a=t can occur **only at α=−3,a=1**. For every α>−3 in its range, every a≥1 is strictly above t and the corrected T_a is a bounded bijection. At α=−3,a>1 it is also strictly above t. The endpoint error therefore does not by itself invalidate every parameter case of Theorem5.5.

Let c=a−1≥0, u=(1−z)^{−c}, and h=(1−z)^c. Lemma5.3 gives the exact formulas

    T_{a,h}(u)=−f0,
    T_{a,h}(u h_k)=Ψ(r_k),    f0=1/(1−z).

The map T_{a,h} is bounded throughout the theorem's range, since T_a is bounded and h is bounded. Consequently the displayed approximation condition in Theorem5.5 **always implies** approximation of f0 byΨ(r_k) inD_α. Theorem2.1 then supplies the zero-free implication for α>−3; at α=−3 the claimed zero-free half-plane is Re(s)>1, already true independently by the Euler product. Neither the endpoint correction nor this review challenges that forward implication.

For the reverse direction, two distinctions matter:

1. At α=−3,a=1, T_1 has no bounded inverse, so reverse closure transport cannot be justified by a Hilbert-space isomorphism. The endpoint approximation might still be true, but needs an independent argument.
2. If a>1, the h used in Lemma5.3 vanishes as z→1 and is **not bounded away from0**. Thus Proposition5.1's assertion about invertible multipliers does not directly apply to this h. This is a dependency question, not a proof that Theorem5.5 is false.

Indeed, for a>t, T_a is an isomorphism but T_{a,h}=M_hT_a is not an onto isomorphism of the full unweighted spaces. In the theorem's range0<c<t, multiplication M_h:D_α→D_α has dense proper range: it contains polynomials because(1−z)^{−c}∈D_α, but is not onto. For example choose b=t+1−c/2; then g=(1−z)^{−b} belongs toD_α, while g/h has exponent b+c>t+1 and does not. A bounded inverse for this full composition is therefore unavailable.

There is a precise, legitimate alternative topology. Define

    D_{α,h}={g:g/h∈D_α},    ||g||_{α,h}=||g/h||_α.

For a>t the same composition T_{a,h} **is** an isomorphism from D_β ontoD_{α,h}. Hence Lemma5.3 exactly identifies the theorem's domain closure condition with

    f0 ∈ closure_{D_{α,h}} span{Ψ(r_k)}.

This is generally stronger than closure in ordinaryD_α. To establish the reverse implication using this route, one needs the additional statement that the stipulated zero-free region gives this weighted-subspace closure, or another direct approximation argument for this special family. It is not enough merely to rename h as an invertible H∞ multiplier.

Theorem2.1 as printed is an approximation⇒zero-free theorem, not an explicit converse. An external generalized Nyman–Beurling theorem or special-core argument could supply missing reverse-direction information; this review has not ruled that out. In particular, a direct compositional inverse on the weighted range is valid, but it does not by itself identify the two closure topologies.

## Source-proof localization and classification

The source pp22–25 asserts simultaneous Riesz-basis properties of its chosen domain polynomials and their images, then surjectivity for all a>0; the critical approximate-null sequence proves that this combined isomorphism conclusion fails at equality. This review does not attribute the problem to a particular asymptotic coefficient without independently checking that local calculation. The exact verified issue is the **included critical bounded-bijection endpoint** in Proposition5.1, present in both inspected versions.

For Theorem5.5: forward approximation⇒zero-free survives this operator repair. Reverse-direction dependency questions at the included critical pair and for noninvertible h require further expert/source analysis or a separate constructive proof. No conclusion of theorem falsity is made. Earlier Theorems2.1 and3.1 do not depend on the later Proposition5.1.

No novelty is claimed for the weighted-Hardy classification; its value here is a complete replacement statement with explicit counterexamples and a narrowly traced dependency boundary.

## Reproducibility and source-version evidence

Exact standard-library code/results: `experiments/code/gallardo_critical_operator_advocate_round4.py` and `experiments/results/gallardo_critical_operator_advocate_round4.json`. The code checks16 rational coefficient identities for truncated homogeneous solutions and4 directed rational endpoint norm bounds. The general classification is the analytic coefficient/Hardy proof above, not inferred from those finite checks.

The publisher p26 and preprintv6 p21 theorem ranges were independently viewed in actual page images. Both includeα=−3. Source provenance and hashes for this targeted review are in `sources/logarithmic_riesz_round3/gallardo_advocate_source_manifest_round4.json`. No new whole-paper reading count is claimed.
