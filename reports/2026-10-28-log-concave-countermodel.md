# Symmetry and strict log concavity do not force critical-line zeros

**Status:** Proposed elementary counterexample, awaiting independent review.
**Scope:** Entire self-dual Laplace/Mellin transforms of positive kernels. This is not an L-function with an Euler product, and it gives no zero-free region for zeta or a Dirichlet L-function.
**Dependencies:** Gaussian integration, elementary properties of log-sum-exp and cosh.
**What was run:** Numerical evaluation below only illustrates an exact formula; no numerical zero finder or certification is used.
**Novelty:** Not established and the broad obstruction is already known. For example, [Pierson’s unreviewed preprint](https://doi.org/10.5281/zenodo.20465036) reports a numerical complex-zero counterexample for the cosine transform of exp(-t^3), and stresses additional decay conditions. The example here has an elementary closed-form zero formula and a strongly log-concave, real-analytic even kernel. A search of local Markdown for “log concav” and combined “Gaussian”/“cosh” found no matching discussion; this is not a comprehensive literature survey.
**Smallest remaining gap:** Independently check the derivation and compare against prior counterexamples in the literature; do not transfer it to arithmetic sources without proving the missing arithmetic properties.

For any k>0, define

    f(x) = exp(-k^2 x^2) (1 + cosh(k x)/5),
    F(s) = ∫_{-∞}^∞ f(x) exp((s-1/2)x) dx.

The integral converges locally uniformly for all complex s, hence F is entire. The real kernel f is positive, even, real analytic, and strictly log concave. To see the last point, write g(u)=1+(exp(u)+exp(-u))/10. The second derivative of log g(u) is the variance of a random variable supported on {-1,0,1} with weights proportional to (exp(-u)/10, 1, exp(u)/10). Thus 0 ≤ (log g)''(u) ≤ 1, and

    (log f)''(x) = k^2[-2 + (log g)''(kx)] ≤ -k^2 < 0.

The kernel is also Gaussian-decaying, and evenness gives the exact functional equation F(s)=F(1-s). The Gaussian integral yields, for z=s-1/2,

    F(s) = (sqrt(pi)/k) exp(z^2/(4k^2))
           [1 + exp(1/4) cosh(z/(2k))/5].

Set a=arcosh(5 exp(-1/4)) > 0. The zeros are exactly

    s = 1/2 ± 2ka + 2k(2n+1)π i,      n ∈ Z.

Indeed cosh w=-cosh a precisely when w=±a+(2n+1)πi. For any prescribed beta in (1/2,1), choose k=(beta-1/2)/(2a). Then every displayed zero has real part beta or 1-beta: in particular the transform has zeros on the prescribed line Re(s)=beta. Thus these qualitative assumptions alone cannot yield any fixed zero-free strip extending to the left of Re(s)=1. For a concrete choice k=1/20, note that 5 exp(-1/4)<5<cosh 5, so a<5 and 0<2ka=a/10<1/2. The zeros closest to the real axis have real parts approximately 0.29643255 and 0.70356745, and imaginary parts ±0.31415927.

Equivalently F(s)=∫_0^∞ f(log t) t^(s-1/2) dt/t is a Mellin transform of a positive kernel. This construction defeats any general argument deriving critical-line zeros solely from positivity, reflection symmetry, analyticity, rapid decay, and strict log concavity in the logarithmic variable. It does not rule out an argument using arithmetic inputs absent here, such as an Euler product, specific coefficient identities, or stronger kernel structure. Ordinary log concavity is not the stronger Pólya-frequency or total-positivity condition.

A relevant external example is [this unreviewed formalization README](https://github.com/gershonavi/xi-log-concavity/blob/main/README.md), which states the broad implication that concavity of log Φ, positivity, evenness and integrability force all zeros of the cosine transform to be real. The construction above refutes that implication as written; it does not adjudicate what Pólya actually proved, any stronger hypotheses in other sources, or the specific xi-kernel argument. The README labels its `polya_theorem` as an axiom, not a derivation.
