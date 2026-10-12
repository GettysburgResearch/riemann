# Independent full HC1–HC28 audit

Date: 2026-10-10. Read-only checkout/Git. Verdict: scoped PASS; no
mathematical gap found in the width 8174 harmonic continuation.

Claim audited: actual Xi(z)=xi(1/2+i z), derivative order zero,
every real lambda in [1,10], the entire closed lower column
z=T-i y, |T|<=8174, y>=0. Both companion and companion derivative are
nonzero and Re(i E/E')>0. The imported finite complete census through 8192
and its historical FLINT complete-count qualification remain explicit.
The claim is not cofinal in T and gives no RH conclusion.

## Complete polynomial count HC3–HC9 (lines 58–139)

Every finite product is built from entire opposite/conjugate blocks of
the actual complete product. Real pairs give positive coefficients after
z=-it. Every nonreal block is outside real part 8192, while its imaginary
part is at most 1/2, so Re(rho^-2)>0; quartets and multiplicities preserve
nonnegative coefficients. Nested blocks have constant coefficient one,
which makes all coefficients nondecreasing. Complete local convergence
then proves f_n(t)<=f(t), f_n'(t)<=f'(t), and the displayed polynomial
maximum-modulus derivative bounds. Initial approximants can be taken to
contain the entire finite census, or the finite initial tail discarded.

The theta-source inequality u sinh(tu)<=cosh((t+1)u) is valid for every
t,u>=0. It bounds f'(t) by f(t+1), without a synthetic substitute source.
Consequently every lambda in [1,10] has the same 11f(L+1) majorant.
Jensen uses E_n(0)=F(0)>1/4 and the correct completed-xi exponent at
s=2t+3/2, giving log88+(t+7/4)log(2t+3/2). The rational coefficient
201215/163840<4/3 and log2>2/3 give the complete polynomial companion
count N_(n,lambda)(t)<2t log t for t>=1024. This counts all companion
zeros with analytic multiplicity, including arbitrarily high upper zeros;
it does not assume a companion zero strip or authenticate a limiting list.

## Complete negative harmonic bound HC10–HC15 (lines143–218)

For C=8191.5 and V=8191, complete localization makes E zero-free in a
neighborhood of the closed rectangle [-V,V] by [0,1/2]. The real-axis
argument supplies its boundary nonvanishing. For each fixed lambda,
q=E'/E and its imaginary part are therefore harmonic there. The outer
theorem and continuity give the nonnegative top value.

The polynomial companions are zero-free in the lower central region
|Re z|<C, and all their zeros have imaginary part>=-1/2. Thus every
lower zero lies in[-1/2,0) with |Re zeta|>=C. Upper/real companion zeros
give nonnegative imaginary logarithmic-derivative contributions. A lower
zero contributes at least -A/(x-alpha)^2, exactly HC12.

The complete Jensen count, not a selected lower packet, bounds the near
negative contribution. Its near radius is strictly below 16383, count
below 458752, and separation>=C-V=A gives negative budget 917504.
For the far part, |x-alpha|>|alpha|/2 and |zeta|^2<=2alpha^2 imply the
8A inverse-square majorant. Partial summation with the complete count
retains every omitted companion zero and bounds that sum by
4(log(2V)+1)/(2V)<60/16382<1. The far negative budget is below 4.
The uniform total -917508>-2^20 survives local quotient convergence and
continuity to every boundary. No unspecified zeros are discarded.

## Whole-bottom positive floor HC16–HC20 (lines220–283)

The complete product gives D=-(F'/F)'>0 throughout the real interval
away from roots: tail conjugate pairs have real distance>1>A, so their
individual contributions are positive. Cauchy–Schwarz over all 16098
finite real census factors gives q_P^2<=16098D. The complete actual
tail sum is below 28/R, so the paired derivative bound is below 2^18.
Together they give q^2<32196D+2^37.

The first native pair is below 15, hence D>=2/(V+15)^2>2^-27 uniformly.
The companion identity Im(E'/E)=lambda D/(1+lambda^2 q^2) gives the
strict floor 2^-72 for all lambda in [1,10], with every denominator
coefficient accounted for. At a simple real root, direct substitution
gives imaginary part 1/lambda, so the floor extends across every root.
This uses the full finite census and complete paired infinite tail,
not a root midpoint or zero-tail assumption.

## Harmonic measure and the closed attachment HC21–HC28 (lines285–392)

The side harmonic measure series has the correct odd sine coefficients
4/(n pi) and cosh ratio for both vertical sides. Its maximum-principle
bounds 0<=h_s<=1 and the inequalities |sin(n theta)|<=n sin theta,
cosh(nkx)/cosh(nkV)<=2exp(-nk(V-|x|)) give HC23.

The comparison u-bp+(M+b)h_s has nonnegative boundary lower limits
on all four sides. At bottom corners, continuity gives u>b and p<=1;
at top corners, p tends to zero and u has a nonnegative continuous value.
The nonnegative bounded harmonic measure therefore introduces no corner
singularity obstruction. The bounded-domain maximum principle proves
HC24 with the displayed multiplier M+b.

At L=8174.25, separation V-L=67/4. The exponential denominator is
greater than 1/2 because 2pi(V-L)>100. Using 3<pi<4 gives
p>sin(theta)/4 and h_s<6exp(-2pi(V-L))sin(theta). Thus the positive term
exceeds 2^-74 sin(theta), while the negative term is below
2^24 exp(-2pi(V-L))sin(theta). Their ratio exceeds
2^-98 exp(100)>4, exactly HC27. This proves strict positivity at every
interior depth, uniformly for the displayed lambda interval.

The larger L leaves a neighborhood around the claimed endpoints 8174.
At y=A, E is nonzero across the line; u is harmonic and nonnegative in
that neighborhood, with strict positive values on both sides. The strong
minimum principle makes its value on the line strict. Bottom values were
already strict, and the full region y>A is supplied by the outer theorem.
Finally u>0 implies E'/E!=0 and Re(i E/E')=u/|E'/E|^2>0. The companion
is separately zero-free by complete localization. No circular denominator
or assumed sector is used in this last step.

## Exact checks, independent controls and freeze

The checker passed normal and optimized modes with 33 guards. Both outputs
are byte-identical to the retained receipt:
2980c9201a8de1b1f4b471ae8142a880df1758e657f3ba927a35d359ac696291.
Outputs: /tmp/review-harmonic-constants-{normal,optimized}.json.
Every direct-source hash in the retained prior native receipt and current
harmonic receipt matches its displayed file. The finite primitive values
and historical complete-count proof are imported, not rerun by this
constants checker; its scope flags state that qualification correctly.

The independent /tmp/review_harmonic_oracle.py reconstructs both boundary
companion identities symbolically, verifies the separated harmonic modes
and side Fourier coefficients, derives a separate exact reciprocal
bottom floor from D0=2/(V+15)^2, and directly encloses the exponential
side suppression with directed pi/exp arithmetic. These are consistency
controls accompanying the full analytic review above.

The independent oracle passed normal and optimized modes with identical
output, SHA256
70358a8a6d73a8585902884eee8467a98b0bfc15750613c03ecd12c17a3f41f4.
Its separate exact bottom floor is 1/462746208614099378418, which
exceeds 2^-72. Outputs: /tmp/review-harmonic-oracle.json and the two
normal/optimized oracle logs.

Frozen proof:
188dc63c7039b4162d43a91864b48266256a3bf8120a29c0f9086c066f2a2241.
Frozen checker:
1c2602b51ed11ce362219d6f06af2519692b92630d18c445b9975ddb42e4003a.
Frozen exact receipt:
2980c9201a8de1b1f4b471ae8142a880df1758e657f3ba927a35d359ac696291.
