# Gonek's 1984 mean-value theorem: whole-source adjudication

18 November 2026. The director read all nineteen journal pages, pp.123–141, including the references and receipt dates, both independent whole-work reconstructions, and the third review of the local findings. The controlling displays on pp.123,125,126,129 and 140 were checked in rendered source images. The main theorem and all three corollaries survive reconstruction, with three local display repairs and an explicit bulk-interval justification for the gap application. The corrections do not change the derivative prefix used by this archive.

Source: S. M. Gonek, *Mean values of the Riemann zeta-function and its derivatives*, Inventiones Mathematicae 75(1) (1984), 123–141, DOI 10.1007/BF01403094. Exact nineteen-page journal scan SHA-256 `dfdd2444a2f62f1947c897e87101080225714dbf1f21db8ca19096d2a6e80fc3`. The currently faculty-linked Rochester PDF is byte-identical. Springer confirms the publication metadata but its separately requested PDF returned a subscription page. A bounded author/publisher/Crossref search found no separately indexed correction; that is not an exhaustive correction history. [Author-hosted journal scan](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf) · [Version check](release123_gonek_version_history.md).

## Exact theorem and useful consequence

Let mu,nu be fixed nonnegative integers, L_T=log(T/(2pi))/(2pi), and alpha real with |alpha|≤L_T/2. Count all nontrivial zeros rho=beta+i gamma with multiplicity. The unconditional theorem (4) is

```text
sum_(1≤gamma≤T) zeta^(mu)(rho+i alpha/L_T)
                    zeta^(nu)(1−rho−i alpha/L_T)
 = (−1)^(mu+nu) T/(2pi) (log T)^(mu+nu+2)
   [1/(mu+nu+1)−H(mu,nu,2pi alpha)−H(nu,mu,−2pi alpha)]
   +O_(mu,nu)(T(log T)^(mu+nu+1)),
```

uniformly throughout that real alpha interval. The entire kernel has the exact representations

```text
H(mu,nu,c)=mu! sum_(j≥0) (ic)^j/[(j+mu+1)!(j+mu+nu+2)]
 =integral_0^1 integral_0^1 x^(mu+nu+1)(1−y)^mu exp(icxy) dy dx.
```

The beta integral checks the series term by term. The integral bounds the kernel and all fixed real-argument derivatives uniformly, even when alpha grows like log T. It is safer than taking absolute values of the large-argument Taylor series. Under RH, 1−rho is conjugate to rho and the shifted second derivative factor becomes the complex conjugate of the corresponding critical-line derivative.

For mu=nu=1 and alpha=0 the bracket is 1/3−2/(2!·4)=1/12, so RH gives

```text
A(T)=sum_(0<gamma≤T)|zeta'(rho)|²
    =T(log T)^4/(24pi)+O(T(log T)^3).
```

No simplicity is assumed. Multiple zeros are counted with multiplicity and have zero unshifted first-derivative weight. For all fixed mu≥1 the diagonal coefficient is mu²/[(2mu+1)(mu+1)²], giving the source's average comparison factor (mu/(mu+1))² after zero counting.

The statement does not provide growing-order uniformity or two independently varied complex shifts. A separate single microscopic complex continuation in the skeptical reconstruction can recover the derivative prefix by Cauchy extraction; that is not silently promoted to the source's printed theorem.

## Proof architecture and the audited analytic interfaces

The proof integrates xi_*'/xi_* times the two zeta derivatives around the rectangle with real sides 1−a,a, 1<a<2, lower height one and a good upper height. The shifted poles are outside for the stated real displacement delta=alpha/L_T, |delta|≤1/2. Each residue is the zero multiplicity times the displayed test.

Local zero counting gives a good height within a bounded distance at separation at least c/log T from ordinates. The standard local logarithmic derivative and fixed-order convexity estimates control the upper and lower edges. The reflected left edge is the **complex conjugate** of the right edge with mu and nu exchanged; the bar is visible in (23) and (37). Losing it reverses the kernel's second argument incorrectly. The argument is unconditional at this point.

Lemmas 1–5 evaluate the right-edge gamma saddle. The phase has its saddle at r=2pi n; endpoint neighborhoods of width sqrt(T) are controlled by the second-derivative estimate, including a saddle just outside the interval. Away from them integration by parts supplies reciprocal distance. With b_n≪_epsilon n^epsilon and fixed a>1, harmonic summation near the cutoff and absolute summation farther away give the source error O(T^(a−1/2)log^m T). Absolute convergence justifies interchanging series and integral. A saddle exactly at an endpoint is absorbed by that error. The phase e(−n) is one, and all leading normalization constants cancel.

Lemmas 6–10 supply differentiated gamma asymptotics, the two-divisor beta coefficient, and convolution with the von Mangoldt function. The ordinary effective PNT, followed by Abel summation against u^(i delta−1) log^m(x/u), gives a uniform error for |delta|≤1/2. The beta integral controls the shifted main kernel before it is expanded. Log weighting is ordinary partial summation; the zero-weight case is already the original summatory formula. Lemma 10 follows by integrating the finite binomial sum against the beta weight.

On the right line, xi_*'/xi_* splits into zeta'/zeta, half the logarithm and i pi/4, plus a smaller error. The first gives the negative H term, the second gives half the rational diagonal, and the third is lower by one logarithm. The fixed differentiations and finite binomial identity close the coefficient. Set a=5/4 to absorb the remaining power errors. Restore arbitrary T by keeping the physical displacement delta fixed, putting alpha'=delta L_(T') at a nearby good T', and using the bounded real derivative of H. Local zero counting and convexity bound the added endpoints, including T itself at a zero.

Accepted external inputs are the functional equation, Stirling and its fixed derivatives, classical convexity, local zero count and logarithmic derivative, effective ordinary PNT, and the stated oscillatory integral estimates. Their uses and upstream references are identified; this adjudication is not a new audit of every source in the bibliography. The source offers effective constants in principle, not a practical numerical onset or explicit derivative-tail remainder.

## Three version-specific display repairs

**1. Introductory equation (2), p.123.** It omits (−1)^(mu+nu) from the continuous mixed derivative asymptotic. The derivative notation is explicitly differentiation in the complex argument. At mu=1,nu=0 the differentiated functional equation gives, on the critical line,

```text
2 Re[zeta'(s)zeta(1−s)]=(chi'/chi)(s)|zeta(s)|²,
(chi'/chi)(1/2+it)=−log(t/(2pi))+O(1/t).
```

Hardy–Littlewood's second moment and partial summation give leading real part −T log²T/2, opposite to the printed positive term. The imaginary integral is a boundary derivative of |zeta|² and lower order by convexity. This is a witnessed false introductory display in the pinned Gonek printing. It is not a claim about Ingham's original notation or proof. The source's main formula (4) already has the correct sign.

**2. Lemma 1's auxiliary phase, p.129.** After extracting e^(−ir), the source prints f(x)=(1+x)log(1+x)−(1+x), then asserts f(0)=0 with a double zero. The literal f(0) is −1. The correct inner phase is F(x)=f(x)+1=(1+x)log(1+x)−x. In fact t log(t/(er))=−r+rF(x) for t=r(1+x). The signed analytic square root of 2F(x) gives the stated stationary-phase lemma and error. It is the auxiliary definition, not the lemma's conclusion, that needs repair. Restricting later applications to integer saddles cannot justify the lemma's intermediate identity for arbitrary real r.

**3. Gap normalization, p.140.** The source's p.125 definition is limsup(gamma_n−gamma_(n−1))log gamma_n/(2pi). Page 140 instead prints the reciprocal factor 2pi/log gamma_n. These cannot define the same quantity: the zero-count estimate gives bounded gaps at large heights and hence the latter limsup is zero, while the properly normalized limsup is at least one by the mean zero density. Restore the p.125 normalization for the proof. The p.125 corollary itself prints the valid weak bound lambda≥1.9.

These are independent local mathematical witnesses, not evidence that the main theorem or a whole research strategy fails. The duplicated section number and other typography are not elevated to additional mathematical findings.

## Repair of the gap application and exact numerical certification

The shrinking arcs in §6 do not cover the entire fixed interval [1,T] by the stated eventual gap bound: their initial fixed-height gaps do not shrink. This observation identifies an insufficient covering justification, not a counterexample to the aggregate inequality. Work instead on [epsilon T,(1−epsilon)T]. If lambda<beta'<beta, the zero count supplies flanking ordinates at comparable heights, and eventually every relevant gap is smaller than beta/L_T. Nonnegative arc mass therefore dominates the continuous second-moment mass on this bulk interval.

Integrating Corollary 2 gives F(beta)T log T+O_beta(T), with

```text
F(beta)=integral_(−beta/2)^(beta/2) [1−(sin(pi x)/(pi x))²] dx.
```

First let T increase, then epsilon decrease to zero, obtaining F(beta)≥1 for every beta>lambda. Continuity and F(1.9)<1 prove the printed lambda≥1.9, and indeed a strict improvement over 1.9. No strict inequality is inferred merely by comparing leading asymptotic coefficients.

The director independently certified

```text
0.99726619997764485330428683895726174554962281741506
 < F(1.9) <
0.99726619997764485330428683895726174554962281741507.
```

The reproducible calculation uses exact rational Machin bounds for pi, forty-one series terms and a rigorous alternating tail. It assumes no RH. RH is required separately for the gap implication. [Code](../../experiments/code/director_gonek_gap_round15.py) · [PASS receipt](../../experiments/results/director_gonek_gap_round15.json).

## Strict-tail consequence and remaining work

Under RH, ordinary Stieltjes partial summation for the strict positive tail gives

```text
sum_(gamma>Y)|zeta'(rho)|²/(gamma²+1/4)
 =−A(Y)/(Y²+1/4)+integral_Y^infinity 2t A(t)/(t²+1/4)² dt
 =(log Y)^4/(24pi Y)+O((log Y)^3/Y).
```

The leading boundary term subtracts one copy and the integral supplies two. Conjugate ordinates double the two-sided tail. This version includes exact ordinate cutoffs and is the denominator input used elsewhere in the archive. It gives no growing polynomial twist or inverse-derivative moment bound. The local corrections and bulk covering repair leave this consequence unchanged.

The next useful task is a complete explicit budget for the PNT convolution, saddle summation and good-height endpoint constants. A new 2026 PNT input may quantify one convolution step, but has not yet been independently integrated into this whole-source adjudication. It must not be advertised as an effective final derivative-tail constant.

[Independent whole advocate](geometry88_gonek_whole_advocate.md) · [Independent whole skeptic](prime88_gonek_whole_skeptic.md) · [Third local-witness adjudication](weighted89_gonek_local_adjudication_input.md) · [Bounded version comparison](release123_gonek_version_history.md).
