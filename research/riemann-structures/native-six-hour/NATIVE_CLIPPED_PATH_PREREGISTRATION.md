# Preregistered original-source clipped-path self-consistency

The completed N=2,3 calibration found actual w-last winners. This
new campaign tests that source evidence; it does not modify the grid
executable or its heldout N=4 panel. The original source metric and
all63 ordered records remain those frozen by the grid source adapter.

The candidate path has w=0 during the planar graph
v=clip(lambda+mu u,0,1), with vertical endpoint completion, then
activates w at (u,v)=(1,1). The sixteen fixed starts are the Cartesian
product lambda in{-1/2,-1/8,1/8,1/2} and mu in{1/2,1,3/2,2}.
No starts are added after their outcomes are known.

A pure-Python floating Newton calculation is used ONLY to propose a
center. It has at most32 steps per start, each with at most16 fixed
halvings, within -2<lambda<2 and1/16<mu<4. Every start and refusal
is retained. Floating convergence does not certify any mathematical
claim and does not choose among grid paths.

For each proposed center the verifier uses the original coefficient
intervals and outward rational arithmetic on a2^-512 lattice. The
fixed root box has radius2^-30 in both coordinates. The box must
lie in one strict nonconstant clipping regime. A two-dimensional
Krawczyk inclusion uses an exactly inverted rational midpoint Jacobian
followed by declared2^-512 rational rounding of the preconditioner;
the chosen rational matrix must remain invertible. The binary center
and both box endpoints must lie exactly on the outward lattice, so
the increments[-2^-30,2^-30] cover the entire certified box. The
Krawczyk image must be strictly inside that box. The
same box must prove c=L2/2>0 and the full source support cone
f>=0 and d+min(e/2,e)>=0. Every sign failure is retained explicitly.

The original equations are L2 lambda+L0=L2 mu+L1=0, where
L=g+G(A,B,C/2,0,0,0). They use the exact source moments, including
both clipping breakpoints and endpoint segments. A strict root and
the full support certificate prove a global all-path source optimum
by NATIVE_SELF_CONSISTENT_PATH_OPTIMALITY.md. Otherwise the result
is only a candidate or actual-path upper bound, as appropriate.

Each successful center also defines a nearby rational actual path.
Its moments, all63 literal2ds integrals, all45 physical ratios and
original energy are independently replayed. Its energy is compared
with the root-box enclosure; a negative lower endpoint in that
enclosure difference is not called a negative excess. No external
solver, numerical integration or substituted quadratic is allowed.

Caps: sixteen starts,32 Newton steps,16 halvings per step, source
artifact8MiB, exact intermediate numerator/denominator32768bits,
serialized outward endpoints2048bits. A failed certificate is not
repaired by silently widening its parameter box or changing starts.
Any further campaign would require a separately recorded declaration.

This concerns the complete original H25 primitive path family. It
does not assert an all-height theorem or identify retained gamma.
