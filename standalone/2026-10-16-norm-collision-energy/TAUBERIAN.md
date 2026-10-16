# A positive Laplace Tauberian lemma, with proof

Status: classical method reconstructed here; not a new Tauberian theorem.
It is used only for the sharp asymptotic, not for the unconditional upper
bounds in Theorems A and B.

Let mu be a positive, locally finite measure on [0,infinity). Suppose its
Laplace transform L(t) is finite for every t>0 and

    L(t) ~ C t^(-r) as t downarrow 0,  C>0, r>0.

Then mu([0,X]) ~ C X^r/Gamma(r+1).

Proof. Define nu_X(A)=mu(XA)/(C X^r). Its Laplace transform at lambda>0
tends to lambda^(-r). Weight nu_X by exp(-x), then push forward by y=exp(-x)
to the compact interval [0,1]. Call the finite measure sigma_X. Its j-th
moment, j>=0, is

    integral y^j d sigma_X = L((j+1)/X)/(C X^r)
                             -> (j+1)^(-r).

The candidate limiting measure sigma is obtained in exactly the same way
from nu(dx)=x^(r-1)dx/Gamma(r); the elementary gamma integral gives these
moments and total mass one. Convergence on polynomials and uniform
polynomial approximation on [0,1], with bounded total masses, imply weak
convergence sigma_X -> sigma. This also proves uniqueness without a
signed-measure Tauberian assumption.

The bounded function y^(-1)1_[exp(-1),1](y) has only one relevant jump,
at exp(-1), and sigma has no atom there. Approximate it from above and below
by continuous functions whose discrepancy is supported in a shrinking
interval around exp(-1). Weak convergence, then the absence of that atom,
gives convergence of its integrals. These integrals are exactly

    nu_X([0,1]) = mu([0,X])/(C X^r).

The limit is integral_0^1 x^(r-1)dx/Gamma(r)=1/Gamma(r+1). QED.

For the Gaussian smoothing in THEOREMS.md, the elementary Rankin bound
mu([0,X])<=exp(1)L(1/(1+X)) supplies O((1+X)^r). Hence replacing the sharp
cutoff X by X-beta-G and taking expectation over one fixed standard normal
G preserves the leading coefficient by dominated convergence. Negative
cutoffs mean zero. This argument includes the atom at log(1)=0.

Credit: Hardy--Littlewood/Karamata positive Tauberian theory. A modern
primary discussion is Herdegen--Liang--Shelley, arXiv:2205.13075, on the
continuity theorem for Laplace transforms. Only its abstract was accessible
in this pass; its generalized signed-measure theorem is not imported.
