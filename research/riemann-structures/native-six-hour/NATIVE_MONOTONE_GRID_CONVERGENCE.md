# Complete native grid paths and constructive convergence

Keep the original H25 source, all63 ordered factors, physical weights
and original Mellin measure. The six source coordinates are
x=(A,B,C/2,D,E,F); the complete field is

    F_path=F_ref+sum_i x_i V_i.                          (1)

The fixed reference and six variation vectors are the authenticated
ones in NATIVE_AFFINE_PHYSICAL_FLOOR.md. All grid paths below are
actual continuous piecewise linear monotone paths in the activation
cube, not arbitrary event-order probability vectors.

## 1. The complete finite search is exact integer arithmetic

For a grid of mesh1/N enumerate every word having N occurrences of
each of2,3,5. At the corresponding current state(k,l,m), the u-step
integrals give the numerator increments

    (2Nl,l(2k+1),l^2,2Nm,m(2k+1),0)

over the common denominator2N^3. A v-step adds2Nm only to F, and a
w-step changes none of these six coordinates. The full source
reference in(1) already retains the fixed endpoint contribution.

If L is the integer numerator vector and d=2N^3, the original energy
is

    I(L)=c+2g.L/d+L^t G L/d^2.                           (2)

Quantize every original coefficient interval outward to denominator
2^512. Since each L_i and L_iL_j is nonnegative, the lower and upper
scores multiplied by2^512 d^2 are exact integer expressions. This
uses the actual source metric and includes every cross term. A
floating-point ranking is unnecessary.

The complete path count is(3N)!/(N!)^3. Paths with identical source
coordinates have identical full observed fields by(1), but their
word multiplicities remain recorded. Surviving overlapping score
intervals are checked with the exact original energy expressions;
only exact equality or strict interval separation supports an exact
minimum/tie assertion. A representative of every surviving class is
independently integrated through all63 original factors.

## 2. Every monotone source path has a nearby grid path

Let delta=1/N. For each coordinate of a continuous monotone path,
order its crossings of k/N. At a crossing pause the original path
while the grid path takes that coordinate step; between crossings
pause the grid path while the original path moves. Resolve simultaneous
crossings in a fixed coordinate order. At all times each coordinate
differs by at most delta. The resulting grid word has exactly N steps
per coordinate and is one of the exhaustively enumerated paths.

Pauses do not change Stieltjes source integrals. Both reparameterized
paths have coordinate variation1 and the same endpoints. Integration
by parts therefore gives

    |Delta x| <= delta (2,3/2,3/2,2,3/2,2).              (3)

For example A=integral v du gives two terms bounded by delta each.
Write B=(1/2)integral v d(u^2): the integrand difference costs
delta/2 and the integrator difference costs delta. For C/2 write
(1/2)integral v^2 du, with the two bounds delta and delta/2.
The D,E,F bounds follow in the same way. These are comparisons of
actual source integrals, not just distances between coefficient lists.

Let

    C_src=2||V_A||+(3/2)||V_B||+(3/2)||V_C||
                       +2||V_D||+(3/2)||V_E||+2||V_F||,
    M=||F_ref||+||V_A||+(1/2)||V_B||+(1/2)||V_C||
                       +||V_D||+(1/2)||V_E||+||V_F||.     (4)

All norms here are in the original L2(nu); V_C is the vector paired
with C/2. The coordinate bounds0<=x<=(1,1/2,1/2,1,1/2,1) show
||F_path||<=M for every path. Equation(3) gives

    ||F_path-F_grid|| <= C_src/N,
    |I_path-I_grid| <= 2M C_src/N.                       (5)

If m_N is the complete grid minimum and m is the all-path infimum,

    m_N-2M C_src/N <= m <= m_N.                           (6)

In particular these actual source minima converge to the full
infimum. This is a convergence theorem, not a claim that a small grid
already achieves it. The constant may be loose; the independently
certified source-halfspace lower bounds remain useful alongside(6).
Nonnested grids need not have monotonically decreasing minima.

## 3. Attainment and the precise source class

For the continuous monotone bounded-variation/Stieltjes class, the
all-path infimum is attained. Remove common pauses and parameterize
by s=u+v+w in[0,3]. Every coordinate is then1-Lipschitz, monotone,
and their sum is s. This family is compact in the uniform topology.
The same integration-by-parts estimates used in(3) make all six
moments and the original observed energy continuous on it. A
minimizing subsequence therefore has an admissible limiting minimizer.

The grid paths are piecewise linear and their minima also converge
to the infimum if one initially restricts to piecewise smooth paths.
Attainment within that smaller regularity class is not asserted.
Neither statement extends the H25 source chart to larger horizons;
source closure must be checked separately.

## 4. Scope of the registered campaign

The calibration grids are N=2 and3, followed by a frozen-executable
heldout grid N=4. The finite counts are90,1680,34650. All use the
original metric and exact integer scores, with whole-source replay
of every surviving minimizer class. The computation supplies actual
upper bounds and reproducible finite minimizers. It does not identify
the complete gamma source or turn an affine/convex-hull relaxation
into an attainable all-path minimizer.
