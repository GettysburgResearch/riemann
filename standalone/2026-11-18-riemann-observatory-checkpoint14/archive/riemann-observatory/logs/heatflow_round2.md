# Heat-flow foundations campaign handoff

Date/cutoff2026-11-17. Task: actual original sources, exact heat/kernel assumptions and cutoff conventions, positive atomic control, and smooth approximations only with proofs.

## Primary reading and identity

**PAPER-D303:** deBruijn, *The roots of trigonometric integrals*, DukeMathJ17(3)(1950),**197–226**, DOI10.1215/S0012-7094-50-01720-0. Original TU Delft scan has30printed pages. The requested297–314 was corrected from originalpage numbering and Newman's reference. Repository1948 is not journalpublicationyear; originalreceived16July1948 is distinct. Targetedreading of introduction/Theorem1,§3Theorem10–14/corelimitproof,selected§7. WholepaperL0,completedsubstantive_reading=false; no full30-page/saddle-point audit.

**PAPER-D304:** Newman, *Fourier transforms with only real zeros*, ProcAMS61(2)(December1976),245–251, DOI10.1090/S0002-9939-1976-0434982-5; alternateJSTORDOI10.2307/2041319. Fullsevenprintedpages read, Gaussian-convolution/canonical-product/weak-limit architecture reconstructed. Classification/product/endpoint conditions imagechecked. L1complete; partialtechnical checks only, no wholepaperL2 or independent audit of every cited polynomial theorem. Copyright1977 is not publicationyear1977.

Private PDFs/source manifest under `sources/heatflow_round2`. The current download URLs and SHA256s are preserved. Do not distribute source PDFs/full text by default.

## Exact convention/hypothesis findings

- deBruijnTheorem10: integrable **function**, Hermitian symmetryf(u)=conjugatef(−u),decayO(e^{−|u|^β}),β>2. Not necessarilyreal/even separately; positivity/C∞not required.
- Theorem13,p205: **all** initialzeros in stripΔ; tilt e^{λ²u²/2} gives strip sqrt(max(Δ²−λ²,0)). Directheatτ=λ²/2 gives coefficient2. No silent “allbutfinitelymany” extension.
- NewmanTheorem1 usesreal/even function variant. Theorem2 instead concerns evennonnegativefinite **measures** and allGaussian dampingb>0; atoms permitted there.
- NewmanoriginalΞ_b(x)=∫e^{ixu−bu²}F(u)du has Ξ_0=ξ(1/2+ix). Theorem3 says **−1/8≤b0<∞**, realzeros iff **b≤b0**, including endpoint.
- Actualsourceformula comparison givesF_Newman(2u)=2Φ_RT(u),henceΞ_b(x)=8H_(−4b)(2x),andΛ_standard=−4b0. The factor4/sign are not inferred from memory.
- Purequartic kernels have threshold−∞; finiteGaussian measures may lack allpositiveheat tilts. Riemann-specific finite threshold requires more than genericpositivity.

## Auxiliary controls / proof status

1. Exactthree-atomρ_a=coshaδ0+(δ1+δ_-1)/2: heat e^τcoshw+cosha has onlyimaginaryzeros iffτ≥logcosha. Atoms notpassed off asdeBruijnfunctioninput.
2. Rigoroussource-class smoothing hε∝exp(−(u/ε)^4), f=ρ_a*hε. deBruijnTheorem1 proves hε'simaginary Laplacezeros; productgives initialexactstripa; Theorem13 and Rouché give **0<Λa,ε≤a²/2**. Locallyuniform convergence proves onlyliminfΛa,ε≥logcosha. No exact smoothed threshold/globalconvergence claim.
3. Consequently the coefficient2 cannot be universally increased toc>2 even for strictlypositiveevenC∞superGaussian densities. Chooseasmallwithlogcosha>a²/c andεsmall so anoff-axiszero persistsatτ=a²/c.
4. FiniteLi-typeprefixpositivity: at a0 everycoefficient isstrictpositive bycritical-line pairedzero products; finitecontinuity gives∀N∃asmall. Smoothing addsnonnegative critical-line contributions. These are model coefficients,notclassicalξ.
5. Exacta=1/100,first100 coefficients enclosedpositive at180digits by directedDecimalintervals with exact rational cosh/sinh tail bounds. Minimumlower>0.2449129068. Atomicthreshold has positive bracket near5e−5. Code/intervallogicawait independent adversarial review; generic analytic∃a proof does not dependon this calculation.

The director was sent every new control for independent scrutiny. At this handoff, no separate review is claimed complete for smoothing/sharpness/Li or intervalcode. Markedpending throughout. No sourceauthorerror alleged; no literature novelty claim.

## Files/counts

- `audits/heatflow_round2.md`: fullreport,exactsourceconditions,parameterderivation,atomic/smooth/controlproofs.
- `papers/PAPER-D303.md`,PAPER-D304.md,`papers/heatflow_round2_records.jsonl`:2 records,1 completedL1,1targetedL0.
- `theorems/heatflow_round2.jsonl`:10nodes; sourcepublishedresults clearlyseparate fromnewauxiliarycontrols/computationalenclosure underreview.
- `connections/heatflow_round2.jsonl`:3preciseconnections with compatibility and missingsteps.
- `experiments/code/heatflow_round2.py`:standardlibraryonly; exactFractionTaylorinputs,Decimaloutwardoperations.
- `experiments/results/heatflow_round2.json`:full100intervals,sourceinputbounds,tailcertificates and exactthresholdbracket.
- `scripts/heatflow_round2_records.py`:recordbuilder usingprivatesourcehashes.

## Continuation

1. Independentlyaudit quarticmollifierTheorem1hypotheses,Hadamardpairproduct/noexponentialfactor,finiteLiadditivity and allε/Nquantifiers.
2. Independentlyaudit Decimaldirectedoperations,rationalTaylorremainders,logseriesrecurrenceand Li conversion. Cross-checkwith Arb if available, withoutsubstitutingagreementfor interval-soundness proof.
3. Checkallconstantshistorical/modernbeforeusingheatnumerics. KeepΛ_modeldistinct fromΛ_Riemann.
4. Investigateactualglobalzeroestimates neededforlimsup thresholdconvergence; locallyuniformfunctionconvergencealone is insufficient.
5. Prior-literaturesearch for the exact sharpness/smoothing controlbeforepublicationnoveltyassessment. No classicalRHgain is asserted.
