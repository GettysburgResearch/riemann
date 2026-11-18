# Primary ancestry of the near-line reciprocal estimate

Agent `/root/corpus`,2026-11-17. This audits a critical input to the growing logarithmic Riesz construction. It separates actual source reading, a new local reconstruction of a standard consequence, and remaining source access limits. No RH proof or literature novelty is claimed.

## 1. Exact citation chain, traced before searching

The existing private Titchmarsh–Heath-Brown1986 scan is `sources/equivalence_round2/titchmarsh1986.pdf`. Actual printed354–355, §14.14(A/B), equations14.14.1–5, were visually read here. The book is already a corpus work: this adds **no new book/work or whole-book reading count**.

§14.14 derives its estimates from Theorem14.13. The actual §14.13 introduction/footnote and the book's original-paper bibliography identify, among its cited antecedents:

- J.E.Littlewood(4), *On the zeros of the Riemann zeta-function*, Proceedings of the Cambridge Philosophical Society22(1924),295–318, DOI10.1017/S0305004100014225.
- E.C.Titchmarsh(3), *A consequence of the Riemann hypothesis*, Journal of the London Mathematical Society2(1927),247–254, DOI10.1112/jlms/s1-2.4.247.

The footnote also cites Landau(11) and Cramér(1); these are antecedents in a chain, not a claim that a single original paper contains every later displayed formula. The1927 paper must not be confused with Titchmarsh1928 *On the remainder in the formula for N(T)*, separately numbered(2). The1924 paper must not be confused with Littlewood's1925 *On the Riemann zeta-function* or1928 *On the function1/ζ(1+ti)*. Titles/years were taken from actual book references, then checked against publisher metadata; they were not guessed from memory.

## 2. Actual original-source access and limits

The1924 publisher identifies volume22,issue3,20September1924,295–318; its2008date is online republication. Its PDF endpoint returns HTTP200 **HTML with an access wall**, not a PDF. A fully reproduced primary article text is accessible through the web tool at https://studylib.net/doc/7952840/on-the-zeros-of-the-riemann-zeta-function . The text carries original page markers, author, receipt16June1924, theorem/lemma numbering and proof prose. The actual reproduced text was read at §1–2 and targeted §§14–23, with earlier Lemmas1–3/Theorems1–3 also inspected. Many mathematical displays disappear or degrade in its OCR, including portions of the sup-function definitions and theorem displays. **No whole24-page Level1 or typeset-original technical audit is claimed.** The preserved tool response and failed PDF/image attempts are private in `sources/littlewood_dependency_corpus_round4/`.

The1927 Wiley PDF returns403; the Oxford publisher metadata establishes title, author, date1October1927 and receipt20November1926, but no substantive1927paper reading has occurred. Internet Archive public-volume searches found earlier Cambridge volumes, not a usable1924volume22. No access restriction was bypassed.

Thus the historical source chain is substantially identified and its mathematical architecture partly read, but **the full original Littlewood/Titchmarsh proof ancestry is not yet source-audited end to end**. The exact legible1986source theorem remains the accepted external input. Do not promote a missing display from OCR into a verified original formula.

## 3. Original branch and constant conventions actually read

Littlewood1924§1,295 defines f(s)=log ζ(s) first by its Euler logarithmic Dirichlet series for σ>1, then by horizontal continuation from2+it when t is not a zero ordinate. At zero ordinates it uses the symmetric limit in t. Zero counts at a horizontal boundary receive half-weight; the condition Re ρ>σ in N(σ,T) remains strict. Under RH, for σ>1/2,t>4, the horizontal path is zero-free and the resulting f is the analytic branch continued from the Euler half-plane. It is **not an arbitrary principal-value logarithm chosen separately at each point**.

The paper explicitly says its unsuffixed A,a denote positive absolute constants that may vary, suffixed constants keep their value, and O constants are absolute unless stated otherwise. An O assertion includes both its multiplier and threshold. These conventions do not make an arbitrary newly introduced parameter a uniform automatically. In fixed-a consequences below K_a and the threshold are allowed to depend on a.

The reproduced primary proof §§14–23 has the following architecture: RH permits repeated horizontal-integral representations of S_n; monotone maxima P,Q compare boundary argument and near-line analytic logarithm; Lindelöf's rotation of domains, Hadamard three circles and Borel–Carathéodory compare these maxima; interpolation/one-sided counting monotonicity bootstraps them to the logT/loglogT scale. Theorem11 gives the familiar S and iterated-integral bounds; §23/Theorem12 derives a near-line logζ estimate and the critical-line upper bound for ζ. This architecture is read from the actual reproduced proof. Exact individual displayed sup domains and all constants remain a source-type-setting limitation.

## 4. What the legible1986theorem says

Under RH, §14.14(A),14.14.1 gives

\[
 |\zeta(1/2+it)|\le C\exp(C\log t/\log\log t).
\]

The proof on354 obtains the upper bound on log|ζ| uniformly for σ>1/2, then passes to σ=1/2 by continuity. Theorem14.14(B),14.14.2 gives a lower bound of the form

\[
 \log|\zeta(\sigma+it)|
 \ge- C\frac{\log t}{\log\log t}
 \log\!\frac2{(\sigma-1/2)\log\log t}
\]

in its stated sufficiently near-line range, together with the corresponding upper bound Clogt/loglogt. Equation14.14.3 controls the continued argument by O(logt/loglogt). Equation14.14.4 is explicitly on an equality line σ=1/2+A/loglogt; it is not by itself a half-plane theorem. Equation14.14.5 extends into an adjacent region by Phragmén–Lindelöf. The printed A is part of an unspecified-constant convention, not a licence to send A→0 inside an untracked O constant.

The lower-bound mechanism is particularly transparent from the actual proof: with δ=σ−1/2 and ξ=1/loglogt, the troublesome integral is

\[
 \int_0^\xi\frac{dx}{\sqrt{\delta^2+x^2}}
 =\operatorname{arsinh}(\xi/\delta).
\]

At δ=a/loglogt it equals arsinh(1/a), finite for each fixed a>0, rather than a t-dependent loss. This directly diagnoses the parameter dependence; it does not claim uniformity as a→0. The argument estimate uses the Poisson kernel δ/(δ²+x²), whose integral is at mostπ/2 uniformly in δ>0.

## 5. A separate tracked Borel–Carathéodory bridge for every fixed a

This elementary reconstruction avoids reading an unspecified A as an arbitrary parameter. Suppose the accepted RH theorem supplies (i) Re f(s)≤C L(t) uniformly for σ>1/2 at large t, and (ii) |f(1/2+A_0/ loglogt+it)|≤C_0 L(t) on one fixed equality curve A_0>0, where L(t)=logt/loglogt and f is the branch above. Both are explicit consequences of the legible §14.14 proof/statements. Then for every fixed a>0, after increasing the height threshold,

\[
 |f(\sigma+it)|\le K_aL(t),\qquad
 \sigma\ge1/2+a/\log\log t,\quad\sigma\le2. \tag{L1}
\]

For0<a<A_0 write μ=1/loglogt and center a disk at s_0=1/2+A_0μ+it. Take outer radius R=(A_0−a/2)μ and inner radius r=(A_0−a)μ. The outer closed disk remains strictly in σ>1/2, so f is analytic there; it never touches a possible critical-line zero. Heights within the disk have L comparable to L(t), uniformly at large t. Borel–Carathéodory gives

\[
 \max_{|s-s_0|\le r}|f(s)|
 \le\frac{2r}{R-r}\max_{|s-s_0|\le R}\Re f(s)
 +\frac{R+r}{R-r}|f(s_0)|
 \ll (1+A_0/a)L(t).
\]

This covers1/2+aμ≤σ≤1/2+A_0μ. For a≥A_0 the region is a subset of the already controlled right region. That right region can be taken from14.14.5 plus the existing fixed-strip bridge. Alternatively, apply the maximum principle to f(s)/[Log(s+3)/LogLog(s+3)] in the curved region between the A_0equality curve and σ=2 above a fixed large height. The denominator is analytic and nonzero there. RH and an ordinary Borel–Carathéodory disk bound give only polylogarithmic growth, sufficient after multiplication by exp(εs²), which decays on the upper truncation. The left, right and bottom boundaries are bounded; first let upper height→∞ and then ε↓0. This supplies the entire right region. Small changes in the curve's height parameter are absorbed in its fixed constants.

Taking real parts in(L1) yields both upper and reciprocal bounds exp(K_aL(t)); the latter follows from |1/ζ|=exp(−Re f). This is a standard local reconstruction, **not a newly sourced statement attributed verbatim to the1924paper**. Independent review is requested. The existing actual-height-to-finite-height argument and low-height Borel–Carathéodory patch remain separately documented in `audits/baez_uniform_dependency_round2.md`; they are not silently replaced by t→V.

## 6. Remaining precise source task

Obtain a legible scan of Littlewood1924printed308–317, especially the four sup-function definitions311 and Theorem12 at317, and the1927Titchmarsh247–254fullpaper. Compare original μ(t) versus μ(T) in each maximum before inferring a finite-height theorem directly from the old notation. Reconstruct the rotation/three-circle bootstrap with all thresholds if the whole historical proof chain is to be marked independently audited. Until then the existing growing-Riesz theorem remains conditional on the explicit classical1986theorem, whose relevant statements/proof passage have been read; ancestry access remains a disclosed limit rather than a hidden extra hypothesis.
