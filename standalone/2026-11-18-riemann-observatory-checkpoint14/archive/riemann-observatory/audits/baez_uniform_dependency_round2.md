# Closing the shrinking-epsilon Möbius dependency by the original Perron route

2026-11-17, equivalences agent. This note separates the actual Balazard–Saias source statement from a uniform reconstruction required in Báez-Duarte's quantitative proof. It does not replace that argument with the later Balazard–de Roton theorem. No novelty or RH advance is claimed. The new result is conditional on RH and explicitly sourced classical consequences of RH.

## Result of the investigation

The required uniform estimate can be reconstructed from the **same Perron contour method** as Balazard–Saias Lemma2, using the near-critical-line bounds in Titchmarsh§14.14 rather than recycling a fixed-distance O-constant. Specifically, under RH there exist fixed b,c,C_0>0 and N_0 such that, for every integer N>=N_0, every real t and

c/loglog N<=epsilon<=1/2,

one has

sum_(n<=N)mu(n)n^(-1/2-epsilon-it)
 =1/zeta(1/2+epsilon+it)
  +O(C_0 N^(-epsilon/3) exp(b L(t))),                    (U)

where L(t)=log(|t|+3)/loglog(|t|+3). The O-constant is independent of epsilon,N,t in this range. The proof and the dependence of c on a single classical inverse-zeta bound are given below. This closes the previously identified **constant-tracking** dependency at the level of ordinary mathematical reconstruction, conditional on the declared classical inputs. Independent reviewer confirmed the contour estimates and the need for the precise source-region bridge.

## Original paper: identity and actual access

PAPER-E007: Michel Balazard and Éric Saias, **Notes sur la fonction zeta de Riemann,1**, Advances in Mathematics139(2)(1998),310–321, DOI10.1006/aima.1998.1760, publisher PII S0001870898917601, article numberAI981760. Crossref metadata saved privately in sources/equivalence_round2/balazard_saias_notes1_crossref.json. The month1998-11 is verified; a precise publication day is not needed here. The source text is French despite Crossref's language field.

Direct publisher PDF/API attempts returned403. The complete reproduced primary article text, including page markers310–321, was read at https://www.academia.edu/114375539/Notes_sur_la_fonction%CE%B6de_Riemann_1. The tool response is preserved privately as balazard_saias_notes1_mirror_tool_response.json. The header, authors, page range, article number and mathematical statements match the canonical identity; this is a degraded text reproduction, not an independently authenticated publisher PDF. Formula extraction is partially garbled. Core equations below were reconstructed and cross-checked against Báez-Duarte and Burnol; exact typeset-source verification remains an access limitation.

This is not ESI623, **The Nyman–Beurling equivalent form for the Riemann hypothesis**, which was previously downloaded under an ambiguous filename in another track. The two works have separate identities and contents.

Whole-work read status: complete12-page reproduced primary text read; substantive reading Level1. Whole-paper Level2 is not claimed, since several peripheral equivalent criteria are only remarked on by the authors, source typesetting is unavailable, and not all cited analytic inputs were audited from their original proofs.

## Original theorem and six-lemma architecture

Let rho(y)={y}, S_n(t)=sum_(k<=n)mu(k)rho(1/(kt)), and c_n=sum_(k<=n)mu(k)/k. Define B_n(t)=S_n(t)-n c_n rho(1/(nt)); the tail coefficient cancels, so B_n belongs to the classical constrained Beurling space on(0,1).

The main theorem onp.313 states that, for each real p>=1, the following are equivalent:

- zeta has no zero in Re(s)>1/p;
- B_n→-1 in L^r(0,1) for every1<r<p;
- S_n is bounded in L^r(0,1) for every1<r<p.

For p=1 the r-ranges are empty and the zero-free statement holds. For p>2 the zero-free statement is false because there are critical-line zeros. The nonvacuous proof concerns1<p<=2.

Lemmas1–2,pp.315–316: a zero-free half-plane Re(s)>alpha, alpha>=1/2, supplies fixed-distance subpower bounds for zeta and its reciprocal, and the partial Möbius estimate

sum_(n<=x)mu(n)n^(-s)=1/zeta(s)+O_(alpha,delta,eta)(x^(-delta/3)(1+|Im s|)^eta)

for alpha+delta<=Re(s)<=1. The constants depend on delta and eta. This statement alone does not authorize delta shrinking withx.

Lemma3,pp.316–317: the zero-free condition is equivalent to c_n=O_eta(n^(-1+1/p+eta)) for every eta>0. This follows from the corresponding Mertens-sum estimate by Abel summation and the prime number theorem c_infinity=0. The converse follows from M(n)=n c_n-sum_(k<n)c_k and convergence/analyticity of the Möbius Dirichlet series.

Lemma4,pp.317–318: for sigma>0,

integral_0^1|1+S_n(t)|²t^(2sigma-1)dt=(1/(2pi))integral_R|F_n(sigma+it)|²dt,

F_n(s)=c_n/(s-1)+(1-zeta(s)sum_(k<=n)mu(k)k^(-s))/s.

The apparent pole at1 cancels. The identity follows from the absolutely convergent Mellin integral on(0,1), then ordinary Fourier Plancherel aftert=exp(-u).

Lemma5,p.318–319: the weighted transform norm decays at a positive n-power on fixed sigma>=alpha+delta. Large imaginary parts are bounded using Lemmas1–3; small imaginary parts use maximum modulus on a rectangle, taking account of the removable pole at1.

Lemma6,p.319: B_n-S_n tends to0 in L^r whenever1<r<p under the zero-free hypothesis. Indeed its norm is at most C_r n^(1-1/r)|c_n|, which tends to0 after choosing eta<(1/r-1/p).

For the main forward implication choose sigma=(1/r+1/p)/2. Weighted L² convergence implies L^r convergence by Hölder because sigma<1/r. Lemma6 transfers S_n to B_n. The reverse implication uses the bounded L^r norm of S_n on(1/n,1), where S_n=c_n/t-1, to obtain |c_n|=O(n^(-1+1/r)); then let r approachp and apply Lemma3. The intermediate implication uses only the easy Beurling converse and Lemma6, not a new Hardy-space construction.

The authors' p.320 priority acknowledgement credits J.Lee's1996 paper with the central convergence result, explaining that their extra equivalent formulations/general p scope are refinements. A fair graph should retain this attribution rather than calling the entire program a new1998 discovery. Lee's original has not been read in this audit.

## Classical inverse-zeta input: exact source region

Downloaded primary monograph: E.C.Titchmarsh, revised by D.R.Heath-Brown, **The Theory of the Riemann Zeta-Function**,2nd edition1986, https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf. Private8.2MB copy and extracted text are in sources/equivalence_round2. Only the relevant chapter portions were inspected, not the entire book.

Book pp.354–355 (PDFpage182), Theorem14.14(B), Eqs14.14.2–14.14.5, were visually checked in the scanned page. Under RH they control log|zeta| near Re(s)=1/2 and log zeta beyond a distance of fixed positive constant divided byloglog|t|. **Eq14.14.4 itself is printed on the equality line** sigma=1/2+A/loglog t. It must not be quoted alone as a bound throughout a half-plane. Eqs14.14.2 and14.14.5 provide the adjacent uniform regions; a fixed-strip Phragmén–Lindelöf bridge handles the remaining right strip.

A consequence sufficient below is: for each fixed a>0 there are constants K_a,v_a such that

|log zeta(sigma+iv)|<=K_a log|v|/loglog|v|

when |v|>=v_a and1/2+a/loglog|v|<=sigma<=2. On the interval up to sigma=3/4 this follows by combining14.14.2–5. On3/4<=sigma<=2, the bound at3/4 is O(sqrt(log|v|)/loglog|v|), while log zeta is bounded on sigma=2 by its absolutely convergent Euler series. Apply the half-strip Phragmén–Lindelöf principle to

log zeta(s)/(Log(s+3))^(1/2)

above a fixed positive height. The branch of log zeta comes from the Euler series and continuation inside this zero-free, pole-free half-strip. Fixed-distance Borel–Carathéodory gives at most logarithmic growth inside. Multiplication by exp(eta s²), followed by eta↓0, justifies the maximum-principle passage at infinite height. Thus the whole fixed right strip has O(sqrt(log|v|)) growth for log zeta, more than sufficient for the displayed consequence. Negative heights follow by conjugation.

This uses the classical conditional theorem as an accepted external input. Its full chain back through the original Littlewood estimates is not re-audited here; no additional zero-spacing, simplicity or derivative-moment assumption is introduced.

## Finite-height inverse lemma, including low heights

**LemmaF.** Under RH, there exist K,V_0>0 such that for V>=V_0,

sup_(|v|<=V, 1/2+1/loglog V<=sigma<=2)|1/zeta(sigma+iv)|
 <=exp(K log V/loglog V).                                (F)

The apparent difficulty is that the near-line estimate is indexed by the actual heightv, while the left boundary in(F) is indexed byV. It is not enough to insertV forv without justification.

Put delta=1/loglog V and split at U=exp(sqrt(log V)). For U<=|v|<=V,

loglog|v|>=1/2 loglog V, hence delta>=1/(2loglog|v|).

Apply the preceding classical consequence with a=1/2. The function log x/loglog x is increasing for sufficiently largex, so its bound is at most K_1 log V/loglog V.

For |v|<U, set H(s)=(s-1)zeta(s), with the pole at1 removed. RH makes H analytic and nonzero in Re(s)>1/2, so it has a holomorphic logarithm there, fixed by the positive value at2. On disks centered at2+iv with outer radius3/2-delta/2 and inner radius3/2-delta, classical polynomial growth of H gives

Re log H<=C log(|v|+3), and |log H(2+iv)|<=C log(|v|+3).

The second bound follows directly from Log(1+iv)+log zeta(2+iv), whose Euler-series part is uniformly bounded. Borel–Carathéodory yields

|log H(sigma+iv)|<=C delta^(-1)log(|v|+3)

uniformly on1/2+delta<=sigma<=2. Consequently log|1/zeta| is bounded above by the same expression with another constant; the extra polynomial |s-1| factor is absorbed. At the pole s=1,1/zeta is zero and the upper bound holds by continuity.

For |v|<U the resulting upper bound is O(loglog V sqrt(log V)), which is o(log V/loglog V). Combine both ranges and enlarge K,V_0. This proves(F) with constants independent of delta,V,v,sigma. This low-height patch prevents a hidden loss near fixed low-lying zeros as the horizontal distance shrinks.

## Perron rectangle and every error term

Let N be a sufficiently large integer, epsilon in the range specified below, s=1/2+epsilon+it, and sigma=Re(s). Take truncation height H_N=N^4. The initial Perron abscissa is

kappa=1-sigma+1/log N,

so Re(s+w)=1+1/log N on the original vertical line. Shift that line to Re(w)=-epsilon/2; the shifted s+w line has real part1/2+epsilon/2. Under RH the inverse zeta factor has no pole anywhere in this rectangle; its zero at the zeta pole is harmless. The sole kernel residue atw=0 is1/zeta(s).

The standard truncated Perron formula for coefficients bounded by1, as used on Balazard–Saias p.315, has an error bounded by

C[N^(1-sigma)log N/H_N
  +N^(-sigma)(1+N log H_N/H_N)].

Even allowing an extra harmless logarithm leaves the bounds below unchanged. At integerN, the difference between a half-weighted Perron endpoint and the requested full coefficient is at most(1/2)N^(-sigma), already absorbed. Thus there is no endpoint exception in(U).

Set V=|t|+H_N+3. If epsilon>=c/loglog N with c>=2, then

epsilon/2>=1/loglog V.

For largeN the entire rectangle has1/2+1/loglog V<=Re(s+w)<=2 and |Im(s+w)|<=V. LemmaF therefore bounds the reciprocal throughout the rectangle by Z=exp(K log V/loglog V).

For x>=16, the function phi(x)=log x/loglog x is increasing and phi(2x)<=2phi(x). Therefore

phi(V)<=2phi(N^4)+2phi(|t|+3)
       <=8 log N/loglog N+2L(t).

The small values3<=|t|+3<16 cause no problem, since the other argument N^4 is already in the increasing range. Put A=8K and b=2K. Uniformly on the rectangle,

Z<=exp(A log N/loglog N+bL(t)).

**Shifted vertical edge:** the factor N^w has modulus N^(-epsilon/2). Also integral_(-H_N)^(H_N)|-epsilon/2+iv|^(-1)dv is O(log N), because epsilon>=c/loglog N. Thus this edge is

O(N^(-epsilon/2)log N exp(A log N/loglog N+bL(t))).

**Two horizontal edges:** their lengths are bounded, |w|>=H_N, and N^Re(w)<=e N^(1-sigma)<=e N^(1/2). Their total is

O(N^(-7/2)exp(A log N/loglog N+bL(t))).

**Perron truncation and endpoint:** since sigma>=1/2 and H_N=N^4, these are O(N^(-1/2)) after enlarging the absolute constant. All estimates are uniform for0<epsilon<=1/2; constants depend only on the fixed classical input, not on a fixed-epsilon limiting argument.

## Absorbing the shrinking-distance loss

For sufficiently largeN,

log N<=exp(log N/loglog N).

Thus the vertical error is at most a fixed constant times

N^(-epsilon/2) exp((A+1)log N/loglog N+bL(t)).

Choose

c=max(2,6(A+1))=6(8K+1).

Whenever epsilon>=c/loglog N,

(A+1)/loglog N<=epsilon/6,

and the vertical bound becomes O(N^(-epsilon/3)exp(bL(t))). For N sufficiently large depending on A,c, the horizontal term is smaller than this, because A/loglog N<=1 and epsilon/3<=1/6. The Perron error O(N^(-1/2)) is smaller as well. This proves(U).

The admissible range is nonempty only once loglog N>=2c; the assertion is asymptotic and no effective numerical threshold is claimed. The constants are tracked symbolically through K, not estimated numerically. Most importantly, the exponent margin is explicit: the N^(-epsilon/2) contour gain pays both the inverse-zeta growth loss and its logarithmic integration factor, leaving N^(-epsilon/3).

## Consequence for Báez-Duarte Proposition3.1

On Re(s)=1/2, multiply(U) by zeta(s). RH supplies |zeta(s)|<=C exp(K_0 L(t)); the critical-line estimate is Titchmarsh14.14.1. Therefore

I_(N,epsilon)=integral_R|zeta(s)|²|M_N(s+epsilon)-1/zeta(s+epsilon)|² dt/|s|²
 <=C N^(-2epsilon/3) integral_R exp(B L(t))dt/(1/4+t²).

The remaining integral is finite for every fixed B: L(t)=o(log|t|). Its constant is independent of epsilon,N. The separately reconstructed ratio estimate gives J_epsilon=O(epsilon^(2/3)). Consequently

||f_(epsilon,N)+chi||²_H<=C[N^(-2epsilon/3)+epsilon^(2/3)].

Choose epsilon=c/loglog N. Then the first term is negligible compared with the second, and

||f_(epsilon,N)+chi||_H=O((loglog N)^(-1/3)).

This uses the original shifted Möbius coefficients mu(n)n^(-epsilon), with no substitution by a later optimized-distance theorem or a fixed logarithmic Selberg array. It supplies the missing constant-tracking bridge identified in the preceding audit.

## Audit classification and remaining limitations

- Original Balazard–Saias Lemma2: fixed-distance statement verified in actual reproduced primary text and its Perron mechanism reconstructed. Its printed O_(alpha,delta,eta) does not itself claim shrinking-distance uniformity.
- Uniform extension(U): conditional mathematical reconstruction succeeds using independently sourced near-line RH bounds. No extra arithmetic hypothesis beyond RH has been found necessary.
- Báez-Duarte's quantitative proposition: all central analytic transitions now have explicit reconstructions, including the formerly unresolved uniform input. Main-paper promotion should wait for the parent's independent adjudication of this extension and the separate J_epsilon reconstruction; the earlier checkpoint's conservative status remains historically accurate.
- Source access remains imperfect: no publisher-quality BS PDF, no published2003 Báez-Duarte comparison. Full primary text was read through a degraded mirror. The classical Littlewood/Titchmarsh input is sourced and inspected, but its entire historical proof chain is not re-audited.
- No numerical verification is substituted for the asymptotic proof; enormous unspecified thresholds and unevaluated constants make this a proof dependency audit, not a practical approximation algorithm.

Continuation: independently check the finite-height lemma and endpoint-sensitive Perron formula; obtain the exact PDF when available; inspect any author errata; if explicit usable constants are desired, replace the symbolic K by a proved explicit conditional reciprocal-zeta bound and propagate the resulting huge N_0 honestly.
