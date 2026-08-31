# Why the three alternating grid winners do not solve every finer grid

This is a proof-only consequence of calibration
`fd24a4acb3b9a041bce4fb8701d2a887e77d2def` and heldout artifact
`885fff1b92897d604dbec971a2945c76191c7dfd`. It changes neither frozen
executable nor source metric and requires no new computation.

For the actual word `(23)^N5^N`, the k-th u step occurs at v=k/N,
for k=0,...,N-1. Integrating the six source coordinates gives

    A=(N-1)/(2N),
    B=(N-1)(4N+1)/(12N^2),
    C/2=(N-1)(2N-1)/(12N^2), D=E=F=0.                  (1)

The complete original field is affine in these coordinates. Hence
these particular fields converge in the original Mellin norm to
the synchronized graph v=u followed by w. Their energies converge
to about158.333344517, certified in the synchronized-face packet.

The exhaustive heldout N=4 winner has strictly smaller original
energy, about157.49597972322044. On every grid with N divisible by4,
repeat each of its twelve steps N/4 times. This is the same oriented
continuous path with a finer subdivision, so all63 source records,
all45 physical ratios and its energy are exactly unchanged.

Therefore for all sufficiently large multiples of4, the alternating
word `(23)^N5^N` has energy greater than an available actual path.
It cannot minimize on those grids. The alternating pattern's success
at N=2,3,4 thus has a proved limit; it is not evidence of an all-N
formula for the minimizer. This conclusion predates and does not
depend on solving the subsequent continuous clipped-path problem.

The statement has only the fixed H25 primitive source scope.
