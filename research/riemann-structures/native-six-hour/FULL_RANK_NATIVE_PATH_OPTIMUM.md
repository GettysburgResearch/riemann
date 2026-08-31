# The original native optimum at the first full source horizon

The held-out horizon450 computation certifies a global minimum over all
continuous coordinatewise monotone paths from000 to111 in the literal
three-prime source, with all source indices supported on2,3,5 and ordered
products nm<=450. It retains the original2ds current, physical1/sqrt(nm)
coefficient, every equal-ratio alias, and the original measure
|kappa_hat(t)|^2dt/(2pi). This is not a complete retained-gamma decoder or
an assertion about all horizons.

The source-only filtration at2952d7c0 proves that450 is the first horizon
containing all20 curvature directions of this fixed-prime source. The
earlier physical rank atlas separately measured rank20 there. Thus the
new certificate tests the full source variation space at a horizon chosen
by the source theorem, rather than selecting a convenient planar model.

## Exact acquisition and result

Calibration is frozen at530ab2d0ee328c4902b102a693941ab49c860949 and the
unchanged held-out run at a4f6ea24a703d183e569d4257ed8d7e867089b86.
Their complete source pins are in native_full_rank_path_certificate.py.
The parent executed the calibration in2.36seconds and the held-out run
in16.84seconds, with reported peak memory below37MiB. The held-out
artifact has proof-object hash
6387035d7036030a10dc8dff819bf36e381e56e2b25686fbe08f51dc38702de0.
The acquisition code required a closing-bracket repair during formatting
before any scientific run; both frozen phases use the same repaired bytes.

The held-out source contains614 ordered records and265 physical ratios.
All35245 upper-triangular kernel pairs were streamed, including the
24182 zero entries;11063 entries are nonzero. Each off-diagonal entry
updates both response coordinates, while a diagonal entry occurs once.
Four response vectors give the planar3-by-3 Gram form and all20-by-4
couplings with the complete source variation space. A separate full
kernel stream computes the energy of one actual rational path, selected
by the first certified root, and agrees exactly with its planar formula.
No full265-by-265 matrix is retained in memory.

All16 preregistered starts produced certified roots and passed the full
eight-quadratic source cone. Approximate values, only for reading the
exact rational enclosures, are

    lambda = -0.12650381198,
    mu     =  1.1600902574,
    minimum energy = 178.6045826115.

Both endpoint clips are active. The optimal oriented path first follows
w=0 and v=clip(lambda+mu*u,0,1), then activates w at u=v=1. Its energy is
the minimum of the complete original observation, not merely the minimum
within that two-parameter family.

## Why the finite calculation certifies every admissible path

The exact20-moment source decoder and the eight-quadratic theorem are
frozen at69b5322b. If F_* is the certified field, its derivative in each
of the20 source directions is computed from the original kernel. After
subtracting an exact endpoint potential, the part involving w has form

    w(P1 du + Q1 dv) + w^2(P2 du + Q2 dv).

Nonnegativity of P1,P1+P2,Q1,Q1+Q2 on the unit square is exactly checked
through eight univariate quadratic minima. Removing w until the endpoint
therefore does not increase the linear supporting functional. On w=0
the remaining support problem is a strictly convex quadratic in v,
whose minimizer is the displayed clipped affine graph. The interval
Krawczyk calculation certifies its self-consistency with the original
physical gradient, including the C/2 normalization.

Let c>0 be the certified planar quadratic coefficient and let delta>0
be any lower bound for the eight lower-envelope minima. The exact
quadratic energy identity gives, for every admissible path,

    E(path)-E_* >= 2c integral |v-clip(lambda+mu*u,0,1)|^2 du
                  +2delta(D+F)+||F_path-F_*||_nu^2,

where D=integral w du and F=integral w dv. Thus equality forces w last
and the continuous clipped graph, with the forced endpoint segments.
The oriented path image is unique, allowing pauses and nondecreasing
reparametrization. Arbitrary strictly increasing parametrizations are
not asserted unique.

The endpoint clips differ from the H25 case, but no monotonicity or
persistence of the optimizer in the horizon is inferred. In particular,
the separate infinite-horizon completion theorem does not make this
finite optimizer an infinite-horizon optimizer.

## Final verification contract

The final producer re-executes both complete frozen acquisition phases,
including the full H450 kernel streams and every declared start. It
independently enumerates the supported indices and all ordered records,
reconstructs all physical1/d sums, and integrates every actual source
record on the nonlinear power path(u,v,w)=(t,t^2,t^3). It also reuses the
authenticated universal64-monomial/27-power-path integral control.

A separate exact original-kernel two-ratio control checks the diagonal,
both off-diagonal responses, and the physical square-root denominator.
Mod65521 elimination confirms the already measured physical direction
ranks6 and20; rank20 is exact because there are only20 columns. The
tests reject incomplete record lists, altered equal-ratio weights,
false root or cone claims, changed witness selection, typed numeric
aliases, unsupported source indices, and altered source scope.

The final producer and tests are pending their serialized parent run.
The discovery timings and successful outcomes above report the two
already completed frozen acquisitions, not future validation.
