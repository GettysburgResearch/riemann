# Independent review: conditional Xi zero-feature form domain

Verdict: **PASS** for the conditional analytic theorem and exact controls at
release commit `b7112aa9c8c96aae60e8d0a8ad9fe3b36ffc88ea`.

Review date: 2026-09-01. The preregistered proof at
`ca0dae696803b729f8ba618451208a533ba14224` is unchanged in the release.
`XI_ZERO_FEATURE_FORM_DOMAIN_OBSTRUCTION.md` has Git blob
`eb9d5b9b48e791396f173043209f766042e7912b` and normalized-LF SHA256
`477b930eb18fa114aa13a09c559029b7dc7f6c818c0c74a0fadb0516a61e05c0`.
The load-bearing source-polarization theorem is frozen at
`e5e43625b157ecc5f602532e16a1197679594824`. No scientific source was
edited and no push was made.

## Accepted conditional theorem

Assume RH only where the proof says so. On the dense exponential core
`D` in `H=L2(0,infinity)`, the feature map

    (Vg)_(gamma,0)=sqrt(2m_gamma) integral g(t)cos(gamma t)dt,
    (Vg)_(gamma,1)=sqrt(2m_gamma) integral g(t)sin(gamma t)dt

is well defined into the direct sum over distinct positive ordinates and is
the minimal Kolmogorov factor of the safe kernel. It satisfies

    2 Re <g,T_0 g> = ||Vg||^2  on D,

but `D(V*)={0}`. Therefore `V` and the positive quadratic form are not
closable. This is a form-domain obstruction, not evidence against RH and
not an operator identity `T_0+T_0*=V*V`.

## Normalization and minimality

The RH product gives

    F(z)=sum_gamma m_gamma[(z-i gamma)^(-1)+(z+i gamma)^(-1)].

Laplace integration supplies the two features
`x/(x^2+gamma^2)` and `gamma/(x^2+gamma^2)`. Their Gram product is exactly

    2m_gamma (xy+gamma^2)
      /((x^2+gamma^2)(y^2+gamma^2)),

which equals the corresponding term of `(F(x)+F(y))/(x+y)`. Thus both the
factor two and the multiplicity aggregation are correct. Square summability
follows from `sum m_gamma/gamma^2<infinity`.

If a vector `(a_gamma,b_gamma)` is orthogonal to every kernel feature, the
function

    R(z)=sum sqrt(2m_gamma)(a_gamma z+b_gamma gamma)/(z^2+gamma^2)

converges locally normally away from the discrete boundary poles. The
identity theorem makes it zero in the right half-plane. Its residues at
`+i gamma` and `-i gamma` are nonzero scalar multiples of
`a_gamma-i b_gamma` and `a_gamma+i b_gamma`; both vanish, so each coordinate
pair is zero. This proves minimality without duplicating a repeated ordinate.

## The adjoint-domain obstruction

For `a in D(V*)`, adjointness and the conjugate-linear-first convention give

    <Ve_x,a> = <e_x,u> = (Lu)(x)

for some `u in H`. The right side is a right-half-plane H2 function, and the
identity theorem identifies it with the same meromorphic `R` in the open
half-plane.

The boundary-pole step is valid. After subtracting the term
`c/(z-i gamma)`, local normal convergence makes the remainder bounded by
some fixed `M` in a disk around that isolated ordinate. On the interval
`|t-gamma|<=sigma`, for sufficiently small `sigma` the pole dominates the
remainder, so

    integral |R(sigma+it)|^2 dt >= constant*|c|^2/sigma.

This contradicts the uniform H2 norm unless `c=0`. Repeating at both
`+i gamma` and `-i gamma` yields the two independent equations above and
hence `a_gamma=b_gamma=0` for every ordinate. Therefore `D(V*)={0}`.

The core `D` is dense in the nonzero Hilbert space `H`. The standard
dense-domain criterion says that `V` is closable exactly when `D(V*)` is
dense in its target; it is not. Equivalently, the form `q(g)=||Vg||^2`
fails the form-closability sequence criterion. If a closed form factor
existed, its restriction to `D` and projection to the minimal feature span
would give a closable minimal factor, contradicting the result.

## Every minimal factor

The conclusion is not tied to the displayed cosine/sine coordinates.
For any two minimal factors of the same kernel, the map sending one finite
linear combination of kernel vectors to the other preserves Gram products.
It therefore extends uniquely to a unitary `U`, and on the common H-domain
`D` the second factor is `UV`. Consequently

    D((UV)*) = U D(V*) = {0},

up to the equivalent placement of `U*` dictated by the chosen direction.
Every minimal Hilbert-space factor has the same nonclosability. A nonminimal
extension cannot repair it either, since orthogonal projection back to its
minimal closed span would preserve closability.

There is no conflict with the source theorem's conditional closability of
`T_0`: a closed accretive operator need not have a closable real-part form
without a sectorial hypothesis. No such hypothesis is asserted here.

## Exact finite replay and boundary

At exact release bytes, all 24 tests pass normally and under `python -O`;
both checks pass, and normal/optimized fixture and source-manifest emissions
are LF-exact. The producer, test, fixture and source-manifest blobs are
`8408d2ac7ad2d875d23f8a8948a120c348577597`,
`fa61ed99591735e44f4ed30101b982bbcc719342`,
`ac4de16dd7d4647e2bc6cc5d5613df452c0e4304`, and
`c98064ca57cbeb6ad2cd0940c74391e4ff4004e0`.

The finite controls authenticate the rational Gram, residue, rank,
minimality and release contracts only. They do not prove RH, the infinite
H2 boundary argument, source-kernel positivity, or an order-five theorem.
