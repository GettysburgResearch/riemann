# SPL26 — separated-set pinching and an improved simple-zero proportion

Date: 2026-09-14.
Status: **Complete proposed component proofs and a proposed unconditional zeta corollary, pending independent mathematical review. Not an RH proof.**

Base: `GettysburgResearch/riemann@f99d9e3908dde4865377c75d9ca051c1f545bf4f`.

The new step is a global spectral-defect bound for the actual Montgomery–Taylor kernel. Close points are removed in disjoint pairs whose two-dimensional defects pay for their removal. The remaining, separated set has a Gram operator bounded strictly below the saturation threshold two. Thus the existing seven-point energy inequality transfers to the spectral defect without the 269/280-block loss.

The seven-point continuum inequality and the analytic prime-side trace estimates are **imported theorems**, not new computations here. Their exact identities and trust boundaries are recorded below and in DEPENDENCIES.md. The new majorant, matching argument, whole-matrix trace-norm adapter, and their composition are proved here. The executable checks only finite algebra and constants; it does not re-prove the analytic input or rerun the inherited seven-point search.

## 1. Statement and inherited inputs

Use Fourier transform

\[
\widehat f(x)=\int_{\mathbb R}f(t)e^{-2\pi ixt}\,dt.
\]

Define

\[
K(x)=\int_{-1/2}^{1/2}\cos(\sqrt2t)\cos(2\pi xt)\,dt,
\quad K_0=K(0)=\sqrt2\sin(1/\sqrt2),
\quad k(x)=K(x)/K_0,
\quad w(x)=k(x)^2.
\tag{1}
\]

The probability density

\[
q(t)=K_0^{-1}\cos(\sqrt2t)\mathbf1_{[-1/2,1/2]}(t)
\]

has Fourier transform k. For any ordered finite multiset X=(x_1,...,x_r), let

\[
G_X=(k(x_i-x_j))_{i,j\le r},\qquad D(X)=x_r-x_1.
\]

For empty and singleton sets define D=0. G_X is positive semidefinite and has diagonal one, with repetitions allowed. Define

\[
\Psi(t)=\begin{cases}(t-1)^2,&0\le t\le2,\\2t-3,&t\ge2,\end{cases}
\qquad \Delta(G)=\operatorname{tr}\Psi(G).
\tag{2}
\]

### Imported finite theorem P7

For every six nonnegative real gaps,

\[
\frac1{3000}\sum_{i=1}^6g_i+
\sum_{s=1}^6\frac2{7-s}\sum_{i=1}^{7-s}
 w(g_i+\cdots+g_{i+s-1})\ge\frac{19}{5000}.
\tag{P7}
\]

This is the ainta seven-point theorem [A], independently reconstructed in the repository's reviewer-A supplement [R, S01]. It is an inherited computer-assisted continuum inequality, not an empirical gap assertion. In particular it applies to subsets selected by the procedure below. No new seven-point search is claimed in this packet.

Set

\[
\alpha=19/5000,\qquad \beta=1/500,\qquad
H_{\rm MT}=\frac32-\frac1{\sqrt2}\cot(1/\sqrt2).
\]

### Theorem SPL1: full spectral defect, with no block-size loss

For every finite multiset X,

\[
\boxed{\Delta(G_X)+\frac{D(X)}{500}
\ge\frac{19}{5000}(r-6).}
\tag{3}
\]

More precisely, the greedy matching below produces b disjoint pairs at distances less than 2/3 and proves

\[
\Delta(G_X)+\beta D(X)
\ge\alpha(r-6)+\left(\frac{722}{9801}-2\alpha\right)b.
\tag{4}
\]

The coefficient of b is strictly positive. The theorem is not obtained by assuming G_X has spectrum below two for arbitrary X; densely clustered sets need not satisfy such a spectral bound.

### Theorem SPL2: proposed zeta consequence

Let N(T,2T) count nontrivial zeta zeros with T<Im(rho)<=2T, with multiplicity, and let S(T,2T) count simple critical-line zeros in that interval. Then, using the unconditional analytic estimates in [C, Theorem D and its proof],

\[
\boxed{
\liminf_{T\to\infty}\frac{S(T,2T)}{N(T,2T)}
\ge c_{\rm SPL}:=\frac{H_{\rm MT}-1/500}{1-19/5000}
=\frac{5000H_{\rm MT}-10}{4981}.
}
\tag{5}
\]

The constant is enclosed by exact rational series in the checker:

\[
0.673058325315610967410539842203
<c_{\rm SPL}<
0.673058325315610967410539842204.
\]

The same lower limit holds for the corresponding counts in (0,T]. If N_d denotes distinct zeros, the same argument also proves

\[
\liminf_{T\to\infty}N_d(T,2T)/N(T,2T)\ge(1+c_{\rm SPL})/2.
\tag{6}
\]

These are ordinary unconditional mathematical statements with explicitly imported, unconditional analytic and computer-assisted inputs. They are **not yet independently reviewed new theorems**. No current-world-record or external-priority claim is made. In particular, [A] already contains the earlier 67.3 percent lift; neither that result nor its stability inequality is claimed as new here.

## 2. A rationally certified bandlimited majorant

### Lemma SPL3

The function

\[
B(t)=\frac54\left(\frac{\sin(2\pi t/3)}{2\pi t/3}\right)^2
\tag{7}
\]

(with its continuous value at zero) satisfies

\[
B(t)\ge q(t)\quad(t\in\mathbb R),\qquad
\widehat B(x)=\frac{15}{8}(1-3|x|/2)_+.
\tag{8}
\]

**Proof.** Outside [-1/2,1/2], q=0 and B>=0. Inside, put v=t^2 in [0,1/4]. The alternating sine estimate gives K_0>=11/12. Use pi^2<10, sin(u)/u>=1-u^2/6 for |u|<=pi/3, and cos(sqrt(2)t)<=1-v+v^2/6. The lower bound for sinc is positive on this interval, so squaring is legitimate. Hence

\[
B(t)-q(t)\ge
\frac54(1-20v/27)^2-\frac{12}{11}(1-v+v^2/6)
=\frac7{44}-\frac{226}{297}v+\frac{4042}{8019}v^2=:R(v).
\]

The derivative R' is increasing and R'(1/4)=-4081/8019<0. Thus

\[
R(v)\ge R(1/4)=\boxed{23/64152}>0.
\tag{9}
\]

The stated elementary trigonometric estimates follow from alternating series on the indicated compact intervals. The checker also encloses pi from Machin's identity to verify 9<pi^2<10. No numerically sampled function inequality is used.

For the Fourier identity, the inverse transform of (3/2)1_{[-1/3,1/3]} is sinc(2pi t/3). The transform of its square is the convolution of those rectangles, namely (3/2)(1-3|x|/2)_+. Multiplication by 5/4 gives (8). This identity is continuous at the two endpoints and the right side is zero there. In particular integral B=15/8. □

### Corollary SPL4: separated Gram matrices never reach saturation

If distinct points of X are at least 2/3 apart, then

\[
\boxed{0\preceq G_X\preceq(15/8)I,\qquad
\Delta(G_X)=2\sum_{i<j}w(x_j-x_i).}
\tag{10}
\]

**Proof.** For any complex vector a,

\[
a^*G_Xa=\int q(t)\left|\sum_j a_je^{2\pi ix_jt}\right|^2dt
\le\int B(t)\left|\sum_j a_je^{2\pi ix_jt}\right|^2dt
=\frac{15}{8}\sum_j|a_j|^2.
\]

Every off-diagonal term in the final integral is zero by (8), including pairs exactly 2/3 apart. Since every eigenvalue belongs to [0,15/8], Psi equals (t-1)^2 throughout the spectrum. The diagonal of G_X is one, so its squared Frobenius distance from I is precisely its off-diagonal squared energy. □

This is an upper Gram bound, not a lower frame bound. Bandlimited majorants and Fourier support are classical mechanisms; the explicit source-specific majorant and constants are what are needed here.

## 3. Close pairs pay their entire deletion cost

### Lemma SPL5

For 0<=x<=2/3,

\[
k(x)\ge19/99,
\qquad
\Delta\begin{pmatrix}1&k(x)\\k(x)&1\end{pmatrix}
=2k(x)^2\ge722/9801>19/2500.
\tag{11}
\]

**Proof.** The global inequality cos u>=1-u^2/2 gives

\[
k(x)\ge1-2\pi^2x^2\int t^2q(t)dt
\ge1-\frac{\pi^2x^2}{6K_0}
\ge1-\frac{10(4/9)}{6(11/12)}=19/99.
\]

Here integral t^2 cos(sqrt(2)t)dt<=1/12. Also |k(x)|<=1 because q is a probability density. The two eigenvalues 1+-k are therefore in [0,2], and direct substitution into Psi proves the claim. □

The numerical room is large: the certified pair price is greater than 0.073, while removing two points requires only 2alpha=0.0076. No lower bound for the number of close pairs among zeta zeros is assumed.

### Lemma SPL6: summing the inherited seven-point inequality

For any q ordered points Y,

\[
E(Y)+\beta D(Y)\ge\alpha(q-6),\qquad
E(Y)=2\sum_{i<j}w(y_j-y_i).
\tag{12}
\]

For q>=7, sum (P7) over every consecutive window of seven points. A pair separated by s indices appears in at most 7-s windows; its aggregate coefficient is at most two. Each gap appears in at most six windows, giving aggregate coefficient at most 6/3000=beta. All unused pair terms are nonnegative. For q<=6, the right side is nonpositive and the result is immediate. □

### Proof of Theorem SPL1

Scan the ordered points from left to right. If the next two points are less than 2/3 apart, put them in a pair and remove both. Otherwise retain the first point and advance by one. Retain an unpaired final point. This partitions the points into b disjoint pairs and a surviving set Y of q=r-2b points. Two consecutive survivors are at least 2/3 apart: when the earlier one was retained, every remaining point was at least that far to its right.

Pinch G_X into the principal block G_Y and the b pair blocks. Since Psi is convex and trace Psi is unitarily invariant, averaging blockwise diagonal unitary conjugations proves

\[
\Delta(G_X)\ge\Delta(G_Y)+\sum_{\rm pairs}\Delta(G_{\rm pair}).
\tag{13}
\]

This step drops cross-block entries by a **proved convex trace inequality**, not by pretending they have favorable entrywise signs. Apply (10), (11), and (12):

\[
\Delta(G_X)+\beta D(X)
\ge\alpha(q-6)+b(722/9801)
=\alpha(r-6)+(722/9801-2\alpha)b,
\]

since D(Y)<=D(X). The empty-survivor case uses E(Y)=D(Y)=0 and the same inequality (12). This proves (4), hence (3). □

### Abstract form of the argument

For another normalized positive-definite kernel, the same conclusion holds whenever: a separated set has Gram spectrum in [0,2]; every deleted close pair costs at least 2alpha in Delta; and every finite set satisfies E+beta span>=alpha(count-q_0). The conclusion is Delta+beta span>=alpha(count-q_0). This is an energy-to-spectral-defect transfer, not a zeta theorem without the analytic inputs below.

## 4. Two matrix facts, including the inherited stability inequality

For PSD matrices of one fixed size,

\[
|\Delta(A)-\Delta(B)|\le2\|A-B\|_1.
\tag{14}
\]

Indeed Psi is 2-Lipschitz on [0,infinity), and the sum of absolute differences of the ordered Hermitian eigenvalues is bounded by the trace norm of A-B. Equivalently, use the spectral trace subgradient of Psi, whose operator norm is at most two, along the segment joining A and B. The same trace functional is convex, which justifies (13). These are finite-dimensional spectral facts, not a claim that Psi is operator convex.

### Lemma SPL7: stability-enhanced rank–trace bound (inherited, rederived)

Let V be d-by-r with column norms at most one, P=VV*, M=V*V, and Q Hermitian with n_+(Q)<=b. Then

\[
\boxed{\|P+Q\|_F^2\ge4\operatorname{tr}(P+Q)-3r-4b+\Delta(M).}
\tag{15}
\]

This is the lemma in [A, Section 2], not a new lemma claimed here.

**Proof.** Write Q=Q_+-Q_- with Q_+Q_-=0. Nonnegative tr(PQ_+) gives

\[
\|P+Q\|_F^2\ge\|P-Q_-\|_F^2+\|Q_+\|_F^2,
\quad \|Q_+\|_F^2\ge4\operatorname{tr}Q_+-4b.
\]

Pad matrices and eigenvalue lists with zeros if necessary. Von Neumann's trace inequality pairs the decreasing eigenvalues p_i of P and n_i of Q_- to bound tr(PQ_-) above. For p>=0,

\[
\min_{n\ge0}\{(p-n)^2+4n\}=2p-1+\Psi(p).
\]

Summing the r terms of M and dropping nonnegative additional terms proves

\[
\|P-Q_-\|_F^2\ge2\operatorname{tr}P-r+\Delta(M)-4\operatorname{tr}Q_-.
\]

Combine these inequalities and use tr P<=r. This proves (15), including dependent columns and r>d. □

## 5. A whole-matrix adapter for the actual zeta vectors

Pointwise or fixed-separation entry convergence would not justify replacing a growing Gram matrix by G_X. The following trace-norm estimate closes that issue without returning to bounded blocks.

Let L>=8, h=2pi/L, tau_j=T+jh, d=floor(LT/(2pi)). Choose the fixed smooth monotone ramp rho from [C], zero for arguments<=0 and one for arguments>=1, and put

\[
\phi_L(u)=\sqrt{\cos(\sqrt2u/L)}\,\rho(L/2-|u|)
\quad (|u|\le L/2),
\]

extended by zero. Write a_L=L^{-1}integral phi_L^2. In this paragraph only, use the angular-frequency transform

\[
\widetilde\phi(\xi)=\int\phi(u)e^{-i\xi u}du.
\]

For real ordinates gamma_i with normalized coordinates x_i=(gamma_i-T)/h, define

\[
V_{ji}=\frac{\widetilde\phi_L(\gamma_i-\tau_j)}{\sqrt{a_L}\,L},
\quad 0\le j<d,
\quad M=V^*V.
\tag{16}
\]

Retain only coordinates in

\[
L^2\le x_i\le d-1-L^2.
\tag{17}
\]

No spacing assumption is made on them.

### Lemma SPL8: uniform trace-norm replacement at growing dimension

For r retained points,

\[
\boxed{\|M-G_X\|_1\le r\left(\frac4{K_0L}+\frac4{L^2}\right).}
\tag{18}
\]

**Proof.** Put q_L(t)=phi_L(Lt)^2/a_L. The raw missing density has nonnegative mass e_L=K_0-a_L<=2/L, from the two taper collars. Therefore

\[
a_L\ge2/3,\qquad
\|q_L-q\|_1\le2e_L/K_0\le4/(K_0L).
\tag{19}
\]

Parseval on [-L/2,L/2], with its complete orthonormal Fourier basis shifted by T, gives the exact infinite-grid Gram

\[
(M_\infty)_{ij}=\sum_{j'\in\mathbb Z}V_{j'i}^*V_{j'j}
=\int q_L(t)e^{2\pi i(x_i-x_j)t}dt.
\]

In particular the full diagonal is one, and the finite columns in (16) have norm at most one. For z(t)=(e^{2pi ix_it})_i, the rank-one matrix z(t)z(t)* has trace norm r. Integrating the signed density difference proves

\[
\|M_\infty-G_X\|_1\le r\|q_L-q\|_1.
\tag{20}
\]

This is the essential r-scale estimate; summing absolute entrywise errors would incorrectly cost r^2.

The variation of sqrt(cos(sqrt(2)u/L)) on its support is at most two, and the taper has variation two. Thus integral |phi_L'|<=4, with zero endpoint values. Integration by parts gives |tilde phi_L(xi)|<=4/|xi| for xi!=0. The squared normalized term at index j is consequently at most

\[
\frac4{\pi^2a_L}|x_i-j|^{-2}\le\frac23|x_i-j|^{-2}.
\]

For (17), the sum over j<0 and j>=d is bounded by 4/L^2, even with this coarse coefficient. The omitted full-grid Gram is PSD. Its trace norm is its trace, so

\[
\|M_\infty-M\|_1\le4r/L^2.
\tag{21}
\]

Equations (19)–(21) and the triangle inequality prove (18). □

Combining (14), (18), and (3) gives the explicit actual-Gram inequality

\[
\Delta(M)\ge\alpha(r-6)-\beta D(X)
-\frac{8r}{K_0L}-\frac{8r}{L^2}.
\tag{22}
\]

The diagonal of M was not set equal to one. Every lost grid term is paid, and all separations are allowed. This is a new adapter proved here; it does not require uniform entrywise convergence across a growing separation range.

## 6. The complete zeta composition

This section separates inherited arithmetic from the new finite geometry.

### Imported analytic input [C]

For the above optimized taper with L=log(T/(2pi)), let I=(T,2T], D_0=sqrt(T), I'=(T-D_0,2T+D_0]. The finite normalized real symmetric Weil matrix \widehat A_T of the zeros in I' and the complete prime-side matrix \widehat G_T have the following properties, proved in [C, Sections 4–7.1]:

1. The simple on-line contribution is P_1=VV*, with columns as in (16), initially for every simple on-line zero in I'. Each column has norm<=1 by the complete-grid Parseval identity.
2. If s_1 counts these simple zeros, s_2 counts distinct multiple on-line zeros, and p counts unordered reflected off-line pairs, then Q'=\widehat A_T-P_1 satisfies n_+(Q')<=s_2+p. This follows from one positive rank-one contribution per distinct multiple on-line zero and one positive direction per hyperbolic off-line pair; no termwise positivity of complex pair energies is assumed.
3. N(I')>=s_1+2s_2+2p, with all multiplicities retained.
4. The analytic estimates are

\[
\operatorname{tr}\widehat G_T=N(I)(1+o(1)),\qquad
\|\widehat G_T\|_F^2=(2-H_{\rm MT}+o(1))N(I).
\tag{23}
\]

The complete outside-zero tail satisfies \|\widehat G_T-\widehat A_T\|_1=O(T^{-1/2}) for this taper, by the same proof as [C, Proposition 4.2] with its bounded second-derivative norm. It follows that

\[
4\operatorname{tr}\widehat A_T-\|\widehat A_T\|_F^2
=(2+H_{\rm MT}+o(1))N(I).
\tag{24}
\]

Only o(N) precision is needed in (24). Equivalently the tail error in the squared norm is bounded by 2||Ghat||_F||Ehat||_1+||Ehat||_1^2. The original proof's explicit prime-side estimates, not a new assumed bound for off-line terms, supply (23).

These are unconditional analytic inputs. They are not internally proved by this packet's finite checker. This pass read the relevant primary PDF sections and inspected the printed pages for the normalization, tail, rank decomposition and Theorem D. It did not independently redo the whole original paper or its formalization.

### Proof of (5)

Apply the inherited stability lemma (15) to P_1+Q'. With M_all the full simple-zero Gram,

\[
\|\widehat A_T\|_F^2
\ge4\operatorname{tr}\widehat A_T-3s_1-4s_2-4p+\Delta(M_{\rm all}).
\]

The multiplicity inequality implies

\[
s_1\ge4\operatorname{tr}\widehat A_T-\|\widehat A_T\|_F^2
-2N(I')+\Delta(M_{\rm all}).
\tag{25}
\]

Pinching to the retained simple-zero block M preserves the lower bound Delta(M_all)>=Delta(M). Removing I'\I costs O(sqrt(T)log T)=o(N(I)) zeros. Removing the strips in (17) costs O(L^2)=o(N(I)), by the classical unit-interval zero count. Thus, writing S=S(T,2T) and N=N(T,2T), the retained count r satisfies r=S-o(N). Its normalized span is at most d, and Riemann–von Mangoldt gives d=N+o(N).

Equations (24), (25) give

\[
S\ge H_{\rm MT}N+\Delta(M)-o(N).
\tag{26}
\]

Insert (22). Since r=O(N), L tends to infinity, and D(X)<=N+o(N),

\[
S\ge H_{\rm MT}N+\alpha S-\beta N-o(N).
\]

Hence

\[
(1-\alpha)S\ge(H_{\rm MT}-\beta)N-o(N),
\]

proving (5). There is no remaining unbounded source inequality assumed between (26) and (5). □

### Distinct zeros and the global count

For distinct zeros, use

\[
3s_1+4s_2+4p
=2(s_1+s_2+p)+(s_1+2s_2+2p)
\le2N_d(I')+N(I').
\]

The same stability bound and tail removals yield

\[
N_d(I)\ge\tfrac12[(1+H_{\rm MT})N+\Delta(M)]-o(N).
\]

Insert Delta(M)>=alpha S-beta N-o(N) and (5). Since
H_MT+alpha c_SPL-beta=c_SPL, this proves (6). This is NOT inferred from the generally false elementary inequality N_d>=(N+S)/2; high multiplicities would invalidate that naive argument.

To pass from dyadic intervals to (0,T], fix any epsilon>0. The proved dyadic inequality with constant c_SPL-epsilon holds for every sufficiently large lower endpoint. Sum over T/2^{j+1}<Im rho<=T/2^j until that endpoint becomes bounded. The remaining bounded range contributes o(N(0,T)). This proves the full-height lower limit. The distinct count is treated identically. □

## 7. Numerical comparison and scope

The exact old constants retained in [R, S02] are

\[
c_{269}=\frac{1345000H_{\rm MT}-2680}{1340003},
\]

\[
c_{280}=\frac{H_{\rm MT}-279/140000}{1-c_*/280},\quad
c_*=2\sqrt{726237/700000}-1+2603/700000.
\]

The checker encloses all three and proves

\[
c_{\rm SPL}-c_{280}>0.00004867.
\]

In percentage units this is over 0.004867 percentage points, a modest but strict improvement. The new constant is about 67.30583253156 percent; it is not 73 percent, not 100 percent, and not a resolution of RH. The distinct-zero corollary is about 83.65291626578 percent.

The scalar Montgomery–Taylor extremal barrier is not contradicted. The arithmetic second-moment constant has not changed. The improvement uses information discarded by the scalar reduction: spectral stability of the actual simple-zero Gram, combined with deterministic point-configuration geometry.

No novelty claim is made for Parseval, bandlimited majorants, pinching, trace-norm spectral continuity, stability inequalities, or the seven-point certificate. No claim is made that this is the best possible use of P7, or that the new leading constant is a verified world record. Independent review should check the new composition at its frozen bytes and then compare against all external work.

## References

[A] `ainta/zeta-simple-zeros@040c5e899e658aed7b56a2a87f501798fe10761d`, paper/riemann.tex, blob `fed199bb7e641c718ac1f33d5e885c0b412d5080`, *More than 67.3% of the zeros of the Riemann zeta function are simple and lie on the critical line*. Sections 2–5 supply the stability inequality, P7 and the prior block lift.
https://github.com/ainta/zeta-simple-zeros/blob/040c5e899e658aed7b56a2a87f501798fe10761d/paper/riemann.tex

[R] `GettysburgResearch/riemann@f99d9e3908dde4865377c75d9ca051c1f545bf4f`, reviews/A/supplement/REPORT.md, blob `e1359f93c399c783e01c86d614fa02e86666671a`, Sections S01–S02. Independent inherited P7 computation; repaired finite-grid and 269/280-block boundaries.
https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/reviews/A/supplement/REPORT.md

[C] Claude, *More than two thirds of the zeros of the Riemann zeta function lie on the critical line*, August 10, 2026, 35-page public manuscript. Inherited analytic input: Lemma 2.2, Propositions 4.1–4.4, trace/second-moment calculations in Section 5 and their optimized extension in Section 7.1, Theorem D. Read through the publisher's primary PDF; the current arXiv successor is Alpöge–Furman, arXiv:2608.13637, which is not silently substituted for this frozen analytic input.
https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf

[L] Y. Lamzouri, arXiv:2609.02882, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*. Context only: this packet does not claim to have verified all of that paper or to use its formalization as a premise.
https://arxiv.org/abs/2609.02882
