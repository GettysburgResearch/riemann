# Fixed actual-prime controls for second-order native face selection

Written before the first acquisition or kernel test. Use X=100000000 and
R=51/50. For i=0,...,5, the exact target is X*R^i. The only allowed
window is `[ceil(target-100), floor(target+100)]`. Search its odd integers
in increasing order and retain the first prime, using complete trial
division through its integer square root. There are at most101 odd
candidates per window; all candidates are below120000000, so every
trial divisor is below11000. No probabilistic primality test is used.

If a window is empty, preserve that failure and the successful windows.
Do not move the targets, widen the windows or select a different prime to
improve the eventual kernel conclusion. The acquisition job and the
later kernel certificate are separate, serialized jobs run by the
coordinating agent.

After acquisition, test two fixed panels: the first four primes and all
six primes. Use all2^r squarefree source factor allocations and the
original `2 ds` coefficient and `|kappahat|^2 dt/(2pi)` observation.
The candidate active supports are the central two coordinates. Solve
the restricted two-coordinate original Gram problem and test every
inactive KKT inequality. A failed face prediction is a valid retained
negative result; it must not be replaced by a different prime panel.

The exact kernel expressions use Q(sqrt2) and logarithms of rational
ratios, with an explicit256-bit input cap. This is a new bounded
certificate, not a modification of the previously frozen64-bit helper.
All pair frequencies, actual cardinality separation and the small-shift
formula domain are checked from the literal primes. No fitted quadratic
kernel, numerical quadrature or assumed exact arithmetic-log spacing is
permitted. The original full Gram KKT result decides the finite fixture;
the asymptotic theorem is proved separately with its cubic remainder.
