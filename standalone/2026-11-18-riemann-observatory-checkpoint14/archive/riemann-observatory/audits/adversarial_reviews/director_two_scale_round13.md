# Two-scale grid tightness: exact guarantee, classical lineage and formal scalar check

18 November 2026. The director read the complete standalone proof, independent reconstruction, and primary-source priority comparison. The result is a useful explicit consequence of classical modulus arguments and the classical random-triangle obstruction. No publication novelty or new general tightness mechanism is claimed. The selected 1974 Garsia–Rodemich paper is a targeted primary reproduction of GRR; Billingsley is a precisely identified 1968 first-edition excerpt, not a complete book reading.

## Statement with the quantifiers fixed

Fix finite p>1, a>1, b>1 and 0<C<infinity. For each row n, take an arbitrary finite deterministic grid from 0 to 1 and real random values X_n at its nodes. Initial values are tight. Suppose every pair of nodes at distance h>0 satisfies

```text
E|X_n(t)−X_n(s)|^p ≤ C min(h^a+epsilon_n, A_n h^b),
A_n≥1, 0<epsilon_n≤1, epsilon_n→0.
```

Let Z_n be polygonal interpolation, a'=min(a,p), b'=min(b,p),

```text
w_n=(epsilon_n/A_n)^(1/b),
lambda_n=epsilon_n/w_n=(A_n epsilon_n^(b−1))^(1/b).
```

For every 0<delta≤1 the uniform modulus obeys

```text
||omega(Z_n,delta)||_p
 ≤ C1 [delta^((a'−1)/p)
       +lambda_n^(1/p) min(1,(delta/w_n)^((b'−1)/p))],
```

with C1 depending only on the fixed exponents and C, uniformly over the permitted grids and laws. Consequently `A_n epsilon_n^(b−1)→0` guarantees tightness of each interpolant family whose own initial marginals are tight. Uniform tightness across a collection of families additionally requires uniform tightness of their initial marginals. This parameter condition is sharp **as a universal guarantee**: if it fails, there are grids and processes satisfying the same fixed C, with zero finite-dimensional limits, whose interpolants and step versions are not tight. It is not necessary for an individual process or a prescribed grid family; its upper estimates may have slack. The degenerate case C=0 is not part of the necessity assertion.

A standard right-continuous grid step process has the same continuous limit as its interpolant if the maximum mesh tends to zero or the maximum adjacent jump vanishes in probability. A different sufficient comparison is an exact representation X_n=Z_n composed with c_n, together with uniform c_n convergence to a continuous clock and the interpolants' uniform modulus, as in the prime-band application. Clock convergence alone does not compare arbitrary step paths to polygons: the fixed two-node grid with values 0,1 and identity clocks is a counterexample. Tightness supplies no finite-dimensional identification by itself. No minimum grid spacing is required.

## Independent proofs and fine-scale interpolation

The director checked the fractional-cell calculation that is easy to omit. A piece of length h inside a cell of length d multiplies its pth moment by (h/d)^p. The power cap p is therefore necessary. Depending on whether d lies above or below w_n, use the appropriate grid bound to get the continuous envelope

```text
E|Z_n(t)−Z_n(s)|^p
 ≤ C2 [h^a' + epsilon_n min(1,(h/w_n)^b')].
```

An arbitrary interval has two fractional cells and one full grid interval. The three-piece Lp inequality preserves this envelope. At dyadic level j, the pth moment of the largest adjacent increment is bounded by 2^j times the envelope at 2^−j. Continuous chaining and Minkowski sum two geometric series. The error series grows to the crossover w_n and decays beyond it, giving the displayed modulus. This proves the upper bound without assuming a minimum scale or silently absorbing an interval-independent error into h².

The independent GRR derivation gives the same estimate. On each row put H(h)=h^a'+epsilon min(1,(h/w)^b') and choose the admissible increasing gauge

```text
g(h)^p = h^(1+1/(p+1)) H(h)^(p/(p+1)).
```

Apply the original GRR inequality separately on blocks of length comparable to delta. With this exponent, H/g^p and the upper bound for h^(−2/p)g'(h) both equal a constant times `(H(h)/h)^(1/(p+1))/h`. The expected block energy and scale integral therefore reduce to `J(delta)=integral_0^delta (H(h)/h)^(1/(p+1))dh/h`; summing block pth moments gives modulus at most a constant times J(delta)^(1+1/p). Its two geometric integrals produce the same two-scale expression. An earlier internal draft had the wrong power of h in the gauge; independent algebraic review corrected it before canonical integration. The dyadic proof was unaffected. The source theorem is for continuous functions; the deterministic grid interpolation must precede that invocation.

For necessity choose a failing subsequence lambda_n≥c>0 and grid pitch d_n approximately w_n with d_n≥w_n. Put a fixed-height spike at one uniformly chosen interior node and zero at all other nodes; set all nonfailing rows to zero. A fixed pair's pth moment is at most a constant times v^p w_n≤(constant v^p/c)epsilon_n. At grid distances at least w_n both envelopes are at least epsilon_n. Choose v>0 small enough for the prescribed C. Fixed evaluations tend to zero while the sup norm stays v and an oscillation of size v occurs on a vanishing interval. This defeats C-tightness. It also defeats J1-tightness: a putative limit vanishes on a dense deterministic set of its a.s. continuity times and at the right endpoint, hence is zero, but the supremum norm is continuous under J1 time changes and stays v. Finite exceptional rows are harmless.

For b>p, imposing the fine power at **every continuous time** would instead force each row constant by subdivision and Minkowski. The sharp necessity theorem concerns grid assumptions and their interpolants, so it does not make that invalid continuous-time extrapolation.

## Direct exponents, arithmetic use and Lean boundary

For 1<q≤min(a,b), the best scalar envelope constant is comparable to

```text
1 + A_n^(q/b) epsilon_n^(1−q/b).
```

The crossover h=w_n proves necessity, and switching the two bounds there proves sufficiency. If A_n is uniformly bounded the direct grid exponent b is available even when b>a. If A_n is unbounded, exponents above a in that latter case fail at h=A_n^(−1/(b−a)); an exponent above b fails at arbitrarily small h. Tightness can hold without any fixed exponent q>1: take w_n=exp(−n²), epsilon_n=w_n/n, A_n=epsilon_n/w_n^b after discarding finitely many rows. Then lambda_n=1/n but every fixed higher-power envelope constant diverges.

For the arithmetic shrinking band, a=b=2, A=L², epsilon=L^−M. A fixed M>2 suffices for tightness; the maximal common grid exponent is 2M/(M+2). Arbitrarily large fixed log savings give every fixed exponent 2−eta. The earlier choice M≥6 and exponent 3/2 is a convenient instance, not the sharp saving threshold. The RH-dependent arithmetic bounds themselves were separately audited in Round 12.

The small scalar step has an actual Lean check. In `Observatory.twoScaleScalarBound`, assume real 0≤u≤1, 0<v≤1, C≥0, `X≤C(u^4+v^6)` and `X v²≤C u^4`. Then `X≤2 C u³`. Splitting at u=v² gives the fine or coarse case. With h=u² and L=1/v this is the M=6 minimum estimate after normalizing the bounded mass range. The exact source was compiled with Lean 4.33.0-rc2 and mathlib commit `51e6992efd06126df61a496bebf8f49482a4e129`. Its declaration uses only propext, Classical.choice and Quot.sound, with no sorryAx. The receipt pins source, command and output. This formalizes the scalar implication **given both bounds**; it does not formalize their number-theoretic hypotheses, probability, interpolation, or Brownian theorem. The upper assumption v≤1 is unused by the proof and may be dropped mathematically; the compiled recorded signature retains it.

## Primary antecedents and practical next step

Garsia–Rodemich, *Monotonicity of certain functionals under rearrangement* (1974), Theorem 1.2, pp. 69–70, explicitly restates GRR and supplies the upper modulus. Billingsley (1968), Theorem 8.2 p. 55 and Theorem 12.3 pp. 95–96, supplies tightness and common-clock comparisons. His §12 Problem 9 p. 103 contains the randomly placed shrinking triangle. The original 1970–71 GRR proof and Hahn–Klass theorem pages were not completely recovered; this archive does not claim to have read them. The first-edition Billingsley record has no assigned second-edition DOI. A targeted search did not establish priority for this exact two-parameter formulation.

The practical next use is to identify a fine estimate retaining local mass in another weighted arithmetic process, combine it with an available asymptotic remainder, and track the crossover. A new scalar inequality or Gaussian finite-dimensional calculation alone does not fill that arithmetic input.

[Standalone proof](uniform85_two_scale_tightness_lemma.md) · [Independent reconstruction](analytic86_two_scale_skeptic.md) · [Primary-source priority and GRR comparison](uniform89_tightness_priority.md) · [Actual Lean receipt](../../experiments/results/two_scale_scalar_lean_check.txt)
