# A measured simple-zero improvement, not another RH completion claim

**PROPOSED finite theorems and an input-qualified zeta corollary. Independent
mathematical review required. RH is not proved. No world-record claim.**

This packet responds to the criticism that repeated RH-equivalent reductions
have not supplied the missing arithmetic bound. It leaves the native-energy
programme's status unchanged and instead improves a concrete output of the
existing seven-point/simple-zero method.

Read [PROOF.md](PROOF.md), especially Sections2--6. The source and acceptance
boundaries are in [SOURCES.md](SOURCES.md) and [VALIDATION.md](VALIDATION.md).

## What changes

For a PSD trace-m Gram G, write Delta=tr Psi(G) and E=tr(G-I)^2, where
Psi(t)=(t-1)^2 up to2 and2t-3 thereafter. The existing sharp envelope at q<2
has value c_m(q). Under E+z>=q, the prior deduction kept the unit span charge,

    Delta+z >= c_m(q).

The new valid deduction rescales BOTH costs:

    Delta+(c_m(q)/q)z >= c_m(q).

A separate explicit bound pays finite diagonal defects and overlap errors.
Offset averaging now favors m=322, not280. With the SAME inherited seven-point
inequality and the SAME named analytic simple-zero interface, it gives

    liminf N_0^s(T,2T)/N(T,2T)
          >=0.673012903898232480616262080101...

The preceding 280-point consequence was

    0.673009652279136912013711991616... .

The gain is 0.0003251619095568602550088485... PERCENTAGE POINTS.
It is small. It is nevertheless an actual improvement in a numerical
consequence rather than a reformulation leaving an RH-strength hypothesis.
The seven-point input is not newly computed, and neither the existing269
nor280 deduction is attributed to this pass.

## What is complete, and what remains external

SSL26-1 is the all-matrix secant theorem, including arbitrarily large input
energy via radial contraction. SSL26-2 pays trace and overlap defects.
SSL26-3 is the finite all-configuration offset theorem. SSL26-4 is the
input-qualified simple-zero application. Its only inherited substantive
inputs are P7 and the explicitly listed Gabor/trace/tail interface (A1)--(A3).
There is no new unproved arithmetic bound hidden behind this corollary.

SSL26-5 solves the restricted affine optimization over EVERY fixed m>=7 and
fixed finite convex mixtures of block sizes. m=322 is optimal when one uses only
trace, the inherited scalar pressure, and affine span charges. A finite
rational comparison covers7<=m<2000; a proved analytic upper bound covers
all m>=2000. For q_m>=2 the computation uses a feasible matrix as an UPPER
bound on a possible deduction, never as an unproved lower spectral envelope.

This ceiling is NOT an optimum over actual kernel configurations, new local
inequalities, adaptive partitions, new windows, or all simple-zero methods.
It gives a clear stop to more block-size tuning without new information.

## How this changes the next research task

The trace-only extremizer is an equicorrelation matrix: one large eigenvalue
and m-1 equal deviations in the other direction. It has not been shown to
be a realizable kernel Gram at the endpoint span used in the relaxation.
To improve further, prove a quantitative incompatibility between that
extremizer and actual Montgomery--Taylor point configurations, or strengthen
the local geometric input with a fully checked continuum inequality. Merely
optimizing this affine formula again cannot improve the certified maximum.
This proposed direction is not claimed solved in the present packet.

## Reproduce

Python3.10+ and the standard library suffice, from this directory:

```bash
python -S -B verify.py --check result.json --self-test
python -S -O -B verify.py --check result.json --self-test
```

`--write NEW_PATH` is a producer option that refuses to overwrite a file;
it is not an acceptance mode. `--check` reconstructs and compares the entire
typed receipt without rewriting it. The script uses exact integers/Fractions,
alternating rational series and outward integer-square-root intervals.
It does not require a numerical eigenvalue or zeta oracle.

The finite controls include2,179 rational spectra;8,716 secant predicates;
124 trace-defect cases;325 complete offset counts; and1,993 block-size
comparisons. A single implementation and normal/optimized agreement do not
constitute an independent proof review. Ten resealed mutations and one
duplicate-key input are refused in each self-test.

## Review priorities

Check the direction of the secant inequality, the radial treatment of E>=2,
the trace-defect correction, and the uniform compact-separation transfer.
Then inspect the restricted optimization proof and its q>=2 witness boundary.
Finally independently replay the short rational certificate and verify the
published-source hypotheses before promoting a zeta-proportion claim.
Do not reclassify previous source theorems or mark RH solved.

This is an addition-only packet against main
`f99d9e3908dde4865377c75d9ca051c1f545bf4f`. It is separate from #848's
resonance/prime-dephasing research. Publication status belongs to the external
delivery receipt; the author does not invent a remote branch or commit.
