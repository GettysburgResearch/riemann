# Independent review of the complete heat derivative cone

Verdict: ACCEPT at the inherited actual-source census/count scope. The
claim covers every real u>=1 and integer0<=r<=u*5419²/32. It leaves the
universal complete-monotonicity premise, all-window positivity and RH open.

Frozen owner proof `../xi/FINITE_CENSUS_HEAT_DERIVATIVE_CONE.md` SHA256
`d0679c63b57ffe755ad22853bc5d2d98c007d00d4a1c4941e2383a91e184fcc7`;
checker `../xi/check_heat_derivative_cone.py` SHA256
`784238e5caa98ec855a134fd5a077c949b8154c2844a63486c7323d23c556fd8`.
Both were read in full. I also read the complete prior
COARSE_ZERO_COUNT.md theta/Jensen proof and checked its rotation/count
normalization against the present positive-half-plane representatives.

The real head is complete by the frozen native count-free census through
5419. The selected actual interval in(14,15) gives a strictly positive
head lower bound14^(2r)exp(-225u) for every integer r>=0. The complete
classical strip pays |rho|^(2r)<= (gamma²+1/4)^r and the heat modulus
exp[-u Re(rho²)]<=exp(u/4)exp(-u gamma²). Conjugate occurrences and their
multiplicities are retained in the actual ordinate count.

I checked the entire tail argument. The inequalities
(gamma²+A²)/(R²+A²)<=gamma²/R² and2log(gamma/R)<=gamma²/R²-1 give the
stated exp(-r) and v=u-r/R². Stieltjes integration over gamma>R gives
the negative CLOSED-head endpoint-N(R)exp(-vR²); its omission is safe.
The actual full countN(t)<tlogt<=t² pays the infinite endpoint and the
Gaussian integral, yielding(R²+1/v)exp(-vR²). The factors exp(-r) and
exp(r) cancel exactly, so no r-dependent factor is lost in HD5.

For the cone, v>=31u/32 and u>=1 imply R²+1/v<R²+2. The two rational
exponential bounds in HD6 give the strict log comparison. Substituting
r<=uR²/32 and18<=18u produces precisely
-u[5R²/8-973/4], with positive coefficient146825859/8. This dominates
every unknown complex block and proves the positive total derivative;
if the tail vanishes, the same conclusion follows directly. No assumed
real tail or finite sampling of the time variable is used.

Normal and optimized independent checker replays both exited successfully;
their JSON outputs are byte identical, SHA256
`1708abc0dd320a35d8f753aa20b1330d5fda60c364a6ad678acf3122226a3bcd`.
They are saved as heat_cone_independent.normal.json and
heat_cone_independent.optimized.json in this operator directory. The
checker authenticates the frozen prior census, its exact source hashes
(including selected candidate intervals), and the literal rational guards.
It records the additional analytic count/heat imports; it does not rerun
the old native root calculation or infinitely many derivatives.

At u=1, the exact floor5419²/32 is917673. Every fixed derivative order
is eventually covered, but arbitrarily high orders at one fixed time
remain outside the cone. Eventual positivity therefore supplies no
universal complete-monotonicity or cofinal zero-location conclusion.
