# Two exact candidate extensions of ChainF50

**Status:** External exact-rational Bernstein certificates for source transitions and a conditional return calculation. These are not Lean-compiled source theorems or an established zero-free region. The candidate uses the pinned PR94 chain, the already proposed 1/250 floor-budget patch, source-specific physical/count transfer, and their imported dependencies. Do not treat the numerical work as an independent verification of those inputs or as a proof that the new modules have been implemented.

Starting from step 129 `G(96232839/10^8,3853/2000,1/10)`, consider

    step 130b: crossing=831/10000, A=401/1000, D=51/100,
               child G(962273544/10^9,24073/12500,1/10);
    step 131:  crossing=52/625, A=2/5, D=1/10,
               child G(962272712/10^9,192583/100000,1/10).

[check_step130b.py](check_step130b.py) and [check_step131.py](check_step131.py) hash-check the relevant pinned `HybridGates`, `HybridGatesMarked`, and `Gain` sources, and check the transcribed rational scalar gates. All one-variable cleared numerators and all six marked-HIGH cleared polynomials have positive exact Bernstein coefficients on their entire v,t,p boxes, without subdivision. The gates for selection, low identity and derivative are source algebraic identities with positive A, X and E. These external checks still require independent source-transcription review and Lean elaboration. An earlier alternative [check_step130.py](check_step130.py) also passes, but its child cannot be followed by the same floor-1/2 transition and its bottleneck count is worse than step 129.

At δ=223/500,p=1/2, the uncapped count branch of step 131 has exact value

    171739569504393/281831043125000 = 0.609370662649897…,

versus 0.609371056815… for step 129. The gain is about 3.94·10^−7 in this count exponent. The step-131 λ is below 2, so it is used **only as a count face**, not as a `PhysicalSchedule` face.

## Conditional scalar return at 0.87386926

[check_geometry131.py](check_geometry131.py) checks the rational parameter, schedule and relaxed 1/250-floor fields at

    θ=43693463/50000000=0.87386926,   h=80599/100000,
    physical cap=619/10000,           physical source=ChainF50 step 66.

Keep the old step-129 C/count windows and the step-64 capP count windows, and add a separate step-131 uncapped C window `δ∈[11/25,9/20]`, `p∈[49/100,1/2]`. The pinned implementation's concrete `physicalB`/`physicalLambda` constants currently also define capP; an amended implementation must **separate** step 66's physical face from step 64's capP count face. They cannot be silently replaced by one another.

[check_return131.py](check_return131.py) hash-checks pinned PR94 `Windows`, `Formulas`, `Constants` and `CountWindow`, tests all 15 transcribed admission guards on the full new window and the two changed earlier windows, and subdivides the full `(δ,p)∈[0,3/4]×[0,1/2]` box at each of the four d-edges using rational Bernstein coefficients. [return131-certificate.json](return131-certificate.json) records every leaf and its exact guard and row-margin minima. The first three edges use respectively 1, 2 and 2 leaves; the new top edge uses 85 leaves, including six using the added step-131 count face. The 1/250 floor reserve is a **different, previously proposed patch**, not part of the untouched PR94 statement.

The script imports the earlier 31 windows, the replacement weakC7 window, and the extra capC window. Its row-edge proof is a rational computation using the source transcriptions, not a Lean theorem. A Lean completion needs: (i) new Step_130 and Step_131 `HybridGatesM` modules proving the above exact polynomial bounds and invoking `density_step_marked` twice; (ii) an `AdmittedWindow` instance and the literal global-source restriction for the new C window; (iii) separate count capP and physical-source constants and their source supplies; (iv) the 1/250 floor-budget patch and new geometry; (v) regenerated finite row certificates, window cover and endpoint; and (vi) a fresh dependency-closure build. The existing pointwise min over count windows allows finite distinct count sources with one common mesh via source mesh monotonicity. None of those implementation steps is claimed complete here.

## A rigorous tail bound within this specific chain mechanism

The tiny remaining room has a structural explanation. Fix the floor qf=1/2, unchanged parent and child caps c₀=c=1/10, and the specific selection `u(v)=Av/(1+Dv)` and gates of `HybridGatesM`. For a parent `(B₀,L₀)`, write

    E₀=(2998/1000)L₀−6B₀,    Δ=L₀−L>0,
    s=(B₀−B)/Δ,              0≤s<1/10.

The gate q(0)>1/2 and `A>0` imply `E₀>0`. At `v=1/10−s`, the same gate and `principal_reference` imply

    Δ < E₀ [1−B₀+(L₀−2)/10] / [(1/10−s)(9/2+E₀)].                (1)

Indeed q>1/2 gives `u(v)>Δv/E₀`, while the principal gate gives `u(v)<[1−B+(L−2)/10]/(9/2)`; substitute `B=B₀−sΔ`, `L=L₀−Δ`. Each subsequent parent must retain E>0, and `E_child=E_parent−(2998/1000−6s)Δ`, which consumes at least `(2398/1000)Δ`.

For the step-131 parent above, `E₀=517/250000000=0.000002068`. At the fixed δ=223/500,p=1/2, put

    s*= (4243B₀−3662)/(4243L₀−3662)
       = 52615389627/563662086250 = 0.0933456248… .

All pre-final future transitions together satisfy `ΣΔ≤E₀/2.398=47/54500000`. If the last step has s<s*, (1), B≥22/23, and L<2 give `Δ≤E₀/[23·4.5·(0.1−s*)]`. If its s≥s*, it contributes no positive fixed-point count improvement; for an overall improving chain, the already accumulated positive amount limits its decrement. Splitting this latter case at `(s*+0.1)/2` gives an upper bound `2.4195·10^−5` for its decrement as well. Write `W=Σ(s*−s)Δ` over the future steps. The exact count formula at this point gives

    R(B₀,L₀)−R(B_f,L_f) = [129563/500] W / (4243 L_f−3662).       (2)

For an improving chain W>0. If the last s<s*, its positive contribution is at most `s*` times the favorable-last Δ bound above. If s≥s*, its contribution is nonpositive; the split bound still controls its possible effect on the denominator. Inserting the exact rational bounds gives a positive denominator and an improvement at most `2.0733·10^−8`, strictly below `3·10^−8`. Thus **any** further finite chain of this same form can improve the step-131 count exponent at this one point by less than 3·10^−8. This is not a bound on other density mechanisms, changed caps, count branches, source families, or the full endpoint. It explains why simply adding many more steps with the present q-floor and selection is unlikely to yield a substantial improvement.

**Independent scalar review:** A second researcher reran the geometry and 2D return checks, verified the transcribed branch formulas and all 15 guards, the old-capacity grouping, reserve, endpoint d, and the separation between the step-66 physical face and step-64 capP count face. They also checked the affine edge-to-interior argument in the pinned `Conductor.lean`; the minimum top-edge cleared row margin in this external certificate is approximately 1.157·10^−9. This does not compile the new steps, patch, source wiring or return in Lean. The separate source-transition transcription review and all imported-dependency qualifications remain necessary.
