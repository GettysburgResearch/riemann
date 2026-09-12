# Exploratory attempts retained with their limitations

The main theorem contribution was reached after testing a different proposed construction. These explorations are not premises of `PROOF.md` and are not part of the exact checker's accepting arithmetic.

## Moment-ratio scouting

`moment_scout.py` computed normalized even theta moments through degree 40 at 70-digit mpmath precision. It used eight terms of the positive-half-line theta series and integrated only to t=4. It did **not** attach rigorous bounds to either omitted tail. The first ratio `2(2n-1)mu_(2n-2)/mu_(2n)` was approximately 43.2806880748; the twentieth approximately 82.5415833856. Inspected finite alternating differences had the displayed positive signs.

These finite observations do not prove that a continuous interpolation is a Bernstein/Pick function, that any such class applies to theta, or that its entire function has the Lee-Yang property. The primary KPS literature was explored for those distinctions, not imported as a theorem closing this gap.

## Gaussian-polynomial interpolation

The next scout interpolated a degree-N polynomial through `C^n n! mu_(2n)/(2n)!` at n=0,...,N and searched one scale C. A numerical root/gap penalty sought negative real roots with a proposed sufficient gap pattern. For N=1 and N=2 the sampled fit had zero floating penalty. For N=3,...,12 the scan and local optimizer did not find a zero-penalty fit.

This is **not** a proof that the cone is empty or that Gaussian-polynomial or interacting-spin approximation is impossible. The algorithm searched a restricted one-parameter family, used ordinary `numpy.roots` after coefficient conversion to machine precision, and produced visibly ill-conditioned large roots in several cases. No interval root isolation or global parameter cover was attempted. The all-order positivity/convergence bridge for this alternative was not established, so the manuscript does not present it as a successful construction.

## Historical file handling

The archive's separate `exploration/` directory retains the original five files byte-for-byte: two scripts, two logs, and the moment JSON. Those rough original scripts contain their original `/mnt/data/attack` paths; they are historical execution records rather than the portable verification interface. The portable `check.py` and `diagnostic.py` in the research packet are the supported replay commands.

No favorable finite scout is used as evidence of RH. No failed floating fit is elevated to a theorem.
