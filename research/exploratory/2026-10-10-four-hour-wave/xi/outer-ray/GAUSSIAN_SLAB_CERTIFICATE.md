# Directed whole-parameter Gaussian transport for a larger native slab

Status: proposed certificate; directed native replay passed, independent
certificate review pending. The result covers the actual
`Xi(z)=xi(1/2+i*z)`, derivative order `r=0`, `lambda=10`, and the closed
finite rectangle `|T|<=13`, `0<=y<=1/2`, `z=T-i*y`.

The source, normalization, complete count and historical FLINT import have
exactly the qualified scope in
[NATIVE_SLAB_CERTIFICATE.md](NATIVE_SLAB_CERTIFICATE.md). The new checker
[check_gaussian_slab.py](check_gaussian_slab.py) independently replays all
8,049 directed native Hardy-Z sign brackets, the complete-count library
output, the nonzero census endpoint and the directed `xi(1/2)>1/4` seed.
No candidate zero-search result alone supplies completeness.

It then uses the complete-tail algebra in
[GAUSSIAN_TAIL_TRANSPORT.md](GAUSSIAN_TAIL_TRANSPORT.md). The exact unknown
tail coefficient is `a_1=sum m/rho^2`. Conjugate blocks in the classical
strip prove `0<=a_1<=S`, where

\[
S=\frac{2(\log8192+1)}{8192}-\frac{8049}{8192^2}.
\tag{GS1}
\]

All 32 subintervals `[j*S/32,(j+1)*S/32]` are enclosed by directed balls.
For every domain box and every parameter bin the checker computes the
full finite-census logarithmic derivatives, adds the exact Gaussian terms
`-2az` and `-2a`, guards the companion derivative denominator, and proves
`Re W_a>0`. Its extracted family margins take the minimum real lower bound
and maximum modulus upper bound over every parameter bin. This protects the
whole allowed interval, including the actual unknown coefficient.

The compact positive-T half starts with 104 by 8 boxes of widths `1/8` and
`1/16`, which exactly cover `[0,13]` by `[0,1/2]`. A coarse box whose
interval enclosure cannot prove the strict predicate is replaced by all
four exact dyadic children. The recursive function returns only after
every child is covered; its maximum allowed depth is eight and exhaustion
fails the entire checker. Every accepted leaf encloses all 32 parameter
bins. The exact leaf-count identity `leaves=832+3*splits` also guards the
finite tree. The full negative-T half follows
from the exact identity

\[
W(-\overline z)=\overline{W(z)}.
\tag{GS2}
\]

Indeed an even entire function with real Taylor coefficients satisfies
`F(-conjugate z)=conjugate F(z)` and
`F'(-conjugate z)=-conjugate F'(z)`. For its order-zero companion
`E=F-i lambda F'`, this gives
`E(-conjugate z)=conjugate E(z)` and
`E'(-conjugate z)=-conjugate E'(z)`, proving (GS2). This applies both to
every even Gaussian base and to the actual Xi.

The disk radius `B=105/8` contains the entire rectangle since
`13^2+(1/2)^2 < (105/8)^2`. The checker applies the complete residual
budgets (G6), not a truncated tail or an assumed real tail. With each full
family modulus upper bound `M` and angular lower bound `tau`, it requires
the exact strict predicate (G14). It also extracts the directed actual
sector lower bound

\[
\operatorname{Re}W_{\Xi}
\ge a-M\frac{\alpha+\beta}{1-\beta}>0,
\tag{GS3}
\]

where `a>0` is the family real lower bound. All finite and parameter
arithmetic is Arb/acb at 128 bits; the receipt stores exact rational lower
bounds and hashes the direct source list in the checker and backend binaries. Ordinary
decimal displays are approximate summaries of those rational bounds.

The accepted receipt is
[gaussian_slab_certificate.json](gaussian_slab_certificate.json). All
8,049 native sign brackets passed. The 832 coarse boxes required 551
complete four-child subdivisions, giving 2,485 accepted leaves at maximum
depth three. All 79,520 accepted domain/parameter boxes passed, with exact
receipt bounds implying `Re W_Xi > 1/100000` on the entire closed rectangle.
The checker also visited rejected coarse enclosures; these are refined
coverage nodes, never accepted sectors. The source hashes bind the
proof adapter, candidate input, full-tail theorem and checker.

The outcome is a finite actual-source companion certificate with
an imported historical complete-count contract. It neither proves the
classical product/count theorem by finite arithmetic nor verifies FLINT's
historical Gram/Rosser table independently. It supplies no uniform control
at unbounded `|T|`, no new complete zero census above 8192, and no RH proof.
