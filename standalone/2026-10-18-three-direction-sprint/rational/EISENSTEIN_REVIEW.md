# Independent component review of the complete cube-filter moment

Reviewer: rational rough-core subagent, 2026-10-18. Independent agent
review, not an external or human referee report. No scientific status is
integrated by this receipt.

Reviewed `../eisenstein/HYBRID_MOMENT.md`, Sections 1--4, SHA-256:
`c7001217a76c47a115ecfcd6121ee644dd58ce74c56e3e480b63fe912f3cc82a`.
I also read the complete relevant arithmetic filter in CUBE_TILT.md and
the author's pinned `_source-04-reflection.tex` local/frozen expansion,
profile, quadratic-sieve, tail and moment proof.

Result: no blocking analytic gap found at the explicitly pinned reflection
interface and native row scope. The final exponent `(11M-1)/7` is weaker
than the original `2M-1` for `1<M<2`; the text correctly does not claim
a new zero-free region.

Independent reconstruction:

1. Every unrestricted filter ideal has unique decomposition `n=a^2 b`
   with b squarefree, allowing a and b to share primes. Setting
   `e=gcd(b,c)`, the squarefree core is `l=b1 c1`, and the row mask
   `(ae,d)=1` remains. For fixed a,e, the number of pairs is at most
   `NC/((Na)^2(Ne)^2)`. Divisor Cauchy therefore gives complete column
   mass `1/[N(Na)^2(Ne)^2]` up to an epsilon divisor factor. The sieve
   outputs `D/[N(Na)^2(Ne)^2]+C/[(Na)^4(Ne)^4]`. Minkowski over a,e
   costs harmonic sums in the first root and convergent sums in the
   second. No shared-prime or higher-power population has disappeared.
2. Fourier separation uses two actual Euler derivatives on a fixed log
   interval. Its phases separate n,c,d and preserve the true quadratic
   kernel. Arbitrary frozen row masks and common row multipliers contract
   the relevant sieve norm. This is not a sieve for a synthetic column
   subsequently identified with the arithmetic filter.
3. For frozen h,f,a_f,k, the exact effective column scale is
   `C_eff=D^2(Nf)^2 N^3/[Z Na_f(Nk)^3]`. Multiplying its square root by
   the native weight `beta(a_f)/Nk` gives
   `sqrt(D^2(Nf)^2 N^3/Z) beta(a_f)/[sqrt(Na_f)(Nk)^(5/2)]`.
   The full k sum converges, and the frozen-exponent sum is `E_f(1/2)`.
   The other root uses `E_f(0)` and retained harmonic/logarithmic sums.
   The common cutoff `R0=Z^delta(D^2P/Z)N^3` is independent of the
   individual filter n. Its discarded tail retains the same native
   beta majorants, and the filter's absolute mass on a dyad is O(1).
   Thus no uncharged polynomial N is hidden in the frozen tail sum.
4. In the original primal expansion, freezing c,k leaves their whole
   character as a common row multiplier. The Gaussian coefficient sum
   is `O((Z/N^3)^(1/2+epsilon))`, and is flat at input below one. This
   gives the displayed second estimate without imposing n,c or n,k
   coprimality. The infinite n tail is then paid using uniform small-input
   Gaussian flatness, before restricting to polynomially many dyads.
5. The two balances are `min(LN^3,DZ/N^4)` and
   `min(LN^3,Z/N^3)`, `L=D^2P/Z`. Their exponents produce
   `D^(11/7)P^(4/7)Z^(-1/7)` and `D sqrt(P)`. Multiplying the powerful
   row count and using `PD<<Z^M` gives exactly `(11M-1)/7`. The excess
   over the native bound is `(6-3M)/7`, positive in the relevant range.

Two clarity requests were incorporated before the reviewed snapshot:
the profile uses its actual positive exponent alpha rather than silently
mixing the original source with a stronger numerical exponent, and the
row sum explicitly retains the native compact shape and finite unit
classes/modulo-Gamma convention. It is not an infinite unrestricted
generator sum over an ideal-norm annulus.

This review is analytic. It neither supplies a finite check of the
imported quadratic large sieve nor validates the open improved CT moment.
