# The literal two-point result and its quantitative barriers

Status: source-faithful extraction; no independent upstream proof build and no new power-saving theorem.
Scope: OpenAI family 007, September 24, 2026, official commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.
What ran: full split-source download and inspection of the quantitative finite-law, analytic, trace and spectral transfers.
Smallest remaining gap: a growing-shift/progression adapter must bound the dependencies that the theorem treats as fixed; a polynomial saving requires a stronger analytic architecture as well.

The exact theorem is ordinary cancellation at every cutoff for fixed forms. It gives Liouville affine sums O_forms(X/(log X)^c), with one absolute c>0 and constants that need not be effective. The general corrected Elliott theorem assumes uniform nonpretentiousness against each fixed Dirichlet character and frequencies |t|<=N at prime cutoff N. It gives a limit, with no rate. The latter alone cannot supply a quantitative Möbius or character-twist estimate.

The following source locations are local full inputs to the PDF, not abbreviated summaries. Their immutable URLs and SHA-256 hashes are in `/workspace/.riemann-research/sources/chowla/manifest.json`.

| Source file | Exact relevant content |
| --- | --- |
| `build/introduction.tex`, Theorems `thm:q-affine`, `thm:elliott` | Fixed affine Liouville saving; general qualitative Elliott; explicit absence of growing-coefficient uniformity. |
| `quantitative/01-setup.tex`, `q:parameters`, `q:prime-masses` | L=(log X)^(1/A), J=floor(delta log L/(6W)), delta=1/200; disjoint centered prime supplies of reciprocal mass between W and 2W; primes dividing lh removed. |
| `quantitative/02-finite-law.tex`, `q:finite-law` | Integer/residue comparison uniform in every translated offset, error exp(-L^10), circuit depth<=20 and size<=exp(L^6), averaging interval>=exp(L^A/2). Modulus l is fixed. |
| `quantitative/03-analytic.tex`, `q:MRT-short`, `q:rough-shifts` | Short interval Fourier input; its rough-shift correlation bound hides concrete sqrt(h) and h factors. |
| `quantitative/04-paths-trace.tex`, `q:trace` and `q:mixed-difference` | Nonbacktracking weighted graph traces, singleton cancellation and residue-law transport. |
| `quantitative/05-rank-witness.tex`, `quantitative/06-forest.tex` | Independent congruences save reciprocal prime mass; a forest codes the complementary low-rank patterns independently of padding coefficients. |
| `quantitative/07-spectral.tex`, `q:prefix-error`, `q:finish` | Block-to-prefix comparison and final c=delta/(6WA). |

## 1. Concrete places where a shift grows

The finite-law comparison is **already uniform in offsets**. The origin residues at different sites share one coordinate per prime, rather than receiving independent copies. Thus merely replacing a fixed shift by a large offset does not by itself invalidate that comparison. The fixed modulus l enters in decoding error 2^(1-B)(l+sum p), B=ceil(L^15), and CRT product D<=l exp(tL). A growing l requires explicit bounds on log l, but no new equidistribution assertion in the offset is needed.

The analytic rough-shift argument has a real shift cost. It defines F_v with D terms and G_v with (2h+1)D terms. On the low-|B(theta)| region, Parseval gives

    integral |F_v G_v| <= sqrt(2h+1) D.

The resulting contribution is O(sqrt(2h+1)L^(-1.05)). On the complementary frequency set, absolute counting of G_v gives O((2h+1)L^(-1.55)). The short-interval MRT input used for F_v is absolute and its residue-class Fourier coefficients have total absolute value one, so this step does not add an l factor. Prefix translation errors are O(D/Y), also independent of h.

The final centering summation has O(L/eta) bins and 2^J extraction choices. Consequently its two explicit analytic costs have the schematic size

    2^J eta^(-1) [sqrt(2h+1)L^(-0.05)+(2h+1)L^(-0.55)].

This identifies an actual obstruction to h=X^rho in the published proof, even if every hidden fixed-h constant were made explicit. Logarithmically growing shifts may fit with a small enough exponent. That is a quantitative adapter task, rather than a literal corollary of the fixed-shift statement.

The graph block boundary has another explicit cost. In `q:prefix-error`, every displacement is at most R_L=h exp(100L+1), while block length M=ceil(exp(103L)). The prefix loss contains polynomial(L) R_L/M. This requires h to be well below exp(3L) if the present block choice is kept. It allows many logarithmic shifts but again does not permit h=X^rho.

Deleting primes dividing lh costs at most their reciprocal mass in the centered supplies and their contribution to the padding characteristic-function exponent. The source writes these as O_h,l(1), with a threshold depending on h,l. A growing-shift adapter must retain explicit sums over p|lh. These are not a failure of CRT or offset uniformity; they are losses from the arithmetic supplies and their product distributions.

## 2. Why a power of X cannot arise by retuning the existing constants

The graph saving is exp(-J), and J grows like log L. With L=(log X)^(1/A), this is a power of log X. The requirement to compare depth-20 residue circuits over intervals of length at least exp(L^A/2) forces L to be at most a fixed power of log X in this architecture. To get X^(-rho) from exp(-J), one would need J comparable to log X, hence L a positive power of X, violating that finite-law scale requirement.

There is also a prime-supply mass constraint: J supplies, each with reciprocal mass W, lie between exp(L^(1-delta)) and exp(L). Their total available logarithmic reciprocal mass is only of order log L. Replacing W by a smaller constant does not change that order. The final spectral transfer needs W large enough that exp(5) C_3/sqrt(W)<=exp(-1), so that constant cannot be freely driven to zero.

The MRT analytic input itself has only logarithmic savings,

    log log H/log H + (log Z)^(-1/700).

Choosing a different fixed A or W cannot turn those losses into a positive power. A polynomial bound must improve the analytic centering input, avoid paying the sqrt(h)/h costs for a useful large shift range, and replace or substantially sharpen the finite-law/graph scale comparison. These are exact structural changes needed by this proof, rather than a claim that no other correlation proof could work.

## 3. What can transfer without invented uniformity

For any fixed finite collection of shifts the source theorem gives a common eventual threshold by taking a maximum of their individual thresholds. A van der Corput argument can then derive qualitative cancellation of the corresponding one-point average. Allowing that finite collection to grow with X requires quantitative uniform constants. The source theorem's quantifier order does not provide them.

A quantitative one-point Liouville bound, if supplied by a justified growing-shift adapter, transfers to Möbius through the exact convolution

    mu(n)=sum_(d^2 m=n) mu(d) lambda(m).

This identity retains the square-divisor weights and can be summed with their convergent d^(-2) mass. It does not, by itself, improve a logarithmic rate into a power. Likewise a fixed-character multiplier can be handled only at the scope of its justified source rate.

No bound here asserts uniform cancellation for h=X^rho, polynomial Mertens cancellation, a zero-free line approaching 1/2, or RH.
