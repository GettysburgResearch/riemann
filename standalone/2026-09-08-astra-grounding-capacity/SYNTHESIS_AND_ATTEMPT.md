# Post-integration synthesis and the attempted full proof

Status: research synthesis, not an independent acceptance report and NOT a
completed RH proof. No original source, prior review, or accepted status changes.
The latest main snapshot read was f99d9e3908dde4865377c75d9ca051c1f545bf4f.
The scientific integration referred to in the repository's new audit is #800;
main's later documentation changes do not independently approve live research.

## 1. What was actually compared

This is a targeted comparison, not a complete census or an audit of all packets.
Exact path and SHA references are in SOURCES.json.

| Source | Depth of this pass | Surviving contribution used for orientation | Missing conclusion |
|---|---|---|---|
| #803, 31a35a90 | RC proof Sections 1-6 read; PR metadata read; no author code run | Physical residual norms admit uniform rational tail capture BEFORE optimization. The period mean is a Jordan-totient quadratic. | No subpower bound for the resulting growing-prefix minima. A period mean is not the physical norm. |
| #819, c4fb0136 | Intrinsic-entropy proof Sections 0-5 read; no numerical replay | The actual source-domain defect is the classical BSY logarithmic defect; target choice can strongly attenuate it. | A small upper certificate and fast convergence to a floor do not identify that floor as zero. |
| #812, 2d683186 | Metadata-level orientation only | Reports a fixed-controller obstruction and source-qualified quasipolynomial Gram conditioning. | Not independently re-proved here; conditioning is not a target error estimate. |
| #823, effa0565 | Earlier contextual summary only, not fresh proof review | Reports small positive late-tail modifications preserving finite data but adding inner factors. | It changes the infinite arithmetic source, so is not an actual-zeta counterexample. |
| #818, bd7bc8ee | Our existing square-grid proof and inherited taper statements reread; no parent producer run | Unconditional local detail is summable. The bounded source adapter keeps the original metric. | Cumulative square-cell levels are not controlled. RH-to-Cramer remains conditional. |
| #825, e4a486d3 | Full graph proof read; native identities rederived in new product cases | All divisor-closed supports have a quantified anchored and centered bound O(log log P). | No full Weil/prime-discrepancy source is identified with that graph. |
| #826, 3a82b80d | Proof of graph paths and Section 3 spectra read; Section 3 reconstructed here | Product reservoirs have exact spectra and an absolute mean-zero gap. | This is not a tensor theorem for n<=N, and does not price arbitrary source couplings. |

The new #827 review census was inspected at metadata level only. Its twelve
paper-reviewed packets do not make all forty-two identified packets accepted.
This pass is not a replacement for that independent review process.

## 2. The route tested

The strongest apparent composition was:

  full arithmetic norm capture (#803)
  + inverse control of multiplicative relations (#825/#826)
  + explicit source-domain defect (#819)
  -> small full residual -> RH.

I tried to make the middle implication a source-level estimate, rather than
concluding it from positive finite matrices. Three obligations remain distinct.

1. The form E(p)=integral |1-sum a_n floor(x/n)|^2 dx/x^2 is not the graph
   energy sum log(p)/(jp^k)|f(jp^k)-f(j)|^2. A usable application must specify
   f as a function of the SAME a_n, and prove the necessary norm comparison.
2. Even the exact period mean in RC1 is
   |1+sum a_n/2|^2+(1/12)sum J_2(d)|sum_{d|n}a_n/n|^2. Its divisor transform,
   J_2 weight, physical initial segment, and coherent term cannot be discarded
   or replaced by the harmonic graph metric merely because both involve divisors.
3. Eliminating the graph's mean-zero sector leaves the retained mean and all
   its couplings. The parent Schur lower estimate requires a sign for that
   complete retained expression. It does not manufacture one.

No norm-preserving equality or upper comparison discharging (1)-(3) was
constructed in this pass. Thus this composition is not an unconditional proof.

## 3. A concrete calculation, not another unproved RH criterion

The new proof tests the frequently implicit step of fixing the graph value at
1 to control the mean channel. On the SQUAREFREE primorial supports the exact
mean-zero gap is (3/2)log 2. Nonetheless the optimal anchored inverse is

  C_sf(P)=(1/zeta(2))log log P+O(1),

and on unbounded-exponent finite-prime reservoirs it is

  C_geo(P)=log log P+O(1).

The root contrast has an explicit Green vector and a finite subset formula;
its squared functional norm G_P differs from C_P by O(1/log log P). These are
unconditional theorems, with sharp leading coefficients. They show that the
log-log cost in the anchored part of #825 is intrinsic, not just its path proof.
They do not show that centered gaps on arbitrary nonproduct ideals are sharp.

The same calculation gives a COMPLETE specified block test:

  c|a|^2+2Re(conj(a)tau[f(1)-mean f])+E(f) >=0 for all a,f
  iff c>=|tau|^2 G_P.

A constant gap alone misses this growing susceptibility. The exact inverse
makes that root-shaped coupling auditable, rather than leaving an unknown
inverse or using a diagonal-only test. This does not assert that actual xi's
coupling is root-shaped; that source identification is a separate requirement.

## 4. What I tried next and why it did not finish RH

One might subtract the explicit logarithmic growth from the retained channel.
But subtracting a scalar from a positive form need not preserve its sign.
Here the finite identity above gives explicit negative tests whenever the
retained reserve is below |tau|^2 G_P. The correct arithmetic reserve would
have to be derived from the FULL gamma/prime/continuum source. No such reserve
is proved to dominate that exact cost.

Likewise, the return product in the new proof factors as zeta(1+t)H(t) for
real t>0. Its 1/t singularity explains the log-log growth. It uses the pole
at s=1, where the Euler expansion is already valid. Analytic or spectral
positivity of this return kernel does not place the nontrivial zeros of zeta.
It is not a Hilbert--Polya operator with the desired zero spectrum.

The residue-minimum route and the prime-energy route still offer clear tests
for progress: prove an unconditional small upper bound for the ACTUAL affine
minimum, or for the ACTUAL cumulative discrepancy. A new source-preserving
inequality from the graph into either of those objects would be valuable.
Neither the old gap nor its now-exact grounding cost is that inequality.

## 5. A precise full ending, conditional on the unproved part

For comparison, the intrinsic-source route from #819 has a simple logical
endpoint. The actual disk source A(w)=w*zeta(1/(1-w)) has A(0)=1 and factors
A=B O. Its unit-target distance is

  delta=1-exp(-2J),
  J=(1/(2pi))integral_R log|zeta(1/2+it)|/(t^2+1/4)dt.

J is the sum of strictly positive Blaschke contributions of right-of-line zeros.
Thus J<=0, or equivalently a construction of unit-target trial errors tending
unconditionally to zero, would give J=0, source completeness and RH by reflection.
This is the credited classical BSY/Hardy mechanism, not a new result here.

The graph results supply neither J<=0 nor that trial sequence. The finite
physical minima in #803 supply authenticated upper numbers for fixed classes,
not the needed unbounded limit. The main missing mathematical assertion is
explicit and is NOT being delegated to reviewers as a routine final step.

## 6. Handoff

Review the new native form normalization, the root spectral weights, the
Dirichlet secular equation, and the two elementary Euler-product asymptotics.
Then use the exact root-cost test only after proving a corresponding source
adapter. The new numerical controls are finite-prime capacity enclosures, not
values of J, zeta zeros, growing physical residual minima, or a new prime-error
exponent. No paper or numerical acceptance is claimed for any earlier packet.

Classical background consulted: Aldous--Fill, Reversible Markov Chains and
Random Walks on Graphs, Chapter 3 (spectral representation and hitting times);
Alouges--Darses--Hillion, arXiv:2006.02953 (approximation versus coefficient
control). The new proofs reconstruct the formulas they need. An exhaustive
novelty search was not performed.
