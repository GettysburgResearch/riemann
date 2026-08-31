# Independent exact-SHA review: selected-point polynomial transport

Scientific source: `96543552b5bc5976d96c35123bfb82e609a27972`.
Immediate corrected-design parent:
`f8003a2569ba8cd9c62516d6f72aa8dfca9ce7b4`.
Original design: `689a93971cdd741a2b154f9506672667aa1a32dc`.
QT authoring base: `530732c5fd7f50364381f8af50e97ce809b674c5`.

Verdict: PASS, including mathematical review, independent primitive
reconstruction and the final release protocol. No scientific source file
was changed.

## 1. Analytic proof

The complete proof,557-line producer,263-line tests and source manifest
were read. The source equation is the exact f6(t)=0 at the inherited REAL
critical point, not a small computed derivative at its numerical center.

For g=f5, a=g(t), c=g''(t), the quadratic
P(w)=a+cw^2/2-i*lambda*cw factors as
(c/2)(w-iy)(w-i(lambda+d)). With 0<r<min(y,2d), the disk centered at iy
contains only the first simple model root and lies strictly above the real
axis. On its boundary the lower bound is |c|r(d-r/2).

Subtracting P from g(t+w)-i*lambda*g'(t+w) BEFORE interval evaluation
cancels the constant and linear f6 terms and the quadratic f7 term.
The remaining w^2 coefficient is -i*lambda*f8(t)/2. For n>=3 it is
[f^(n+5)(t)-i*lambda*f^(n+6)(t)]/n!. These shifts and factorials are
correct. Real projection of each complex coefficient enclosure is
legitimate at a real t; the original imaginary intervals are preserved
and checked to contain zero.

Cauchy's estimate on every radius-R disk around a possible TRUE critical t
bounds the two n>=N tails by

    M*(h/R)^N * [
      5!*binom(N+5,5)/(R^5*(1-h/R)^6)
      +lambda*6!*binom(N+6,6)/(R^6*(1-h/R)^7)
    ].

The binomial product inequality in JP3 proves the entire infinite tail.
It is not inferred from the130 finite test cases. With N32 only signed
coefficients through index37 enter; obtaining40 terms also checks the
unchanged full QT modulus panel8..39.

The64 equal CLOSED angle intervals cover [0,2pi] with all endpoints.
Their rectangular sine/cosine enclosures may extend beyond the circle;
the polynomial bound on those rectangles is conservative. The tail only
needs the true circle, whose points satisfy |w|<=y+r<=h<R. The proof
does not erroneously require every rectangular corner to satisfy |w|<=h.

All64 strict comparisons therefore give one companion zero counting
multiplicity, hence a simple zero. The separate full-parent-rectangle
containment test identifies it with the previously certified HA root.
Containment alone would not prove transport. Nonvanishing of C5/R0/C0
is inherited from the matched parent; it does not follow merely from
the quadratic Rouche lemma.

## 2. Independent primitive calculation

The review helper imports NO JP, QT, HA or OA producer code. It implements
the reflected completed formula at s=1/2-i*z, rather than the source's
s=1/2+i*z formula. At1024bits it performs the following independently:

- Recertifies the one simple real f6 zero by a fresh critical-point Rouche
  comparison on the entire tiny square around its original center.
- Evaluates all40 signed derivatives over the full real critical interval.
- Reconstructs the fixed calibration and uses y=lambda-d, not the author's
  cancellation-stable rationalization.
- Evaluates a NEW complete16x16 outer rectangle cover, with256 scalar
  reflected-Xi calls at1024bits, including the critical-center uncertainty.
- Evaluates the polynomial using ascending powers and direct summation,
  not complex Horner, on the same64 arcs.
- Independently checks the whole HA root rectangle against every allowed
  model center and the lower bound for its radius.

All64 independent arc comparisons pass. The largest independent upper
error/lower margin quotient is below0.780126; the independently rebuilt
tail/margin is below0.000000807. Both are conservative explanatory bounds
for this review's DIFFERENT enclosures, not replacements for the author's
exact endpoints. Full rectangle matching also passes with ratio below0.27.

The author's source result remains64/64 with worst ratio below4/5
(approximately0.7736072904), and full-parent displacement/radius below3/10.
Every author arc index, exact angle endpoint, error sum, strict comparison
and rational ratio was separately verified from the frozen fixture.

The independent report also authenticates all40 transitive Git-blob/LF
source versions, all five unchanged scientific files, all four artifact
seals, the payload, and the actual44-file native-runtime aggregate.
Commit objects and canonical relative POSIX paths are checked. Normal
and optimized independent reports agree exactly.

This is independent formula, region-bound and polynomial code, but the
SAME pinned FLINT special-function implementation. It is not a second
implementation of gamma/zeta or a formal verification of that library.

Independent report payload SHA256:

    68a049928fec718fe075766f49f3a9b79da145f144f0324eb5ec1bd567b37685

Independent40-source catalog SHA256:

    2fb6b01a73e2832188d03b7b751606d0b860af124f18013b65518672aa604f4f

## 3. Selection, source and acceptance scope

Index19 was deliberately selected AFTER the joint-M3 panel as its best
failing case. The original preregistration mistakenly expected signed
coefficients in QT, which stored only modulus bounds. The correction
was frozen before the new signed-jet experiment and preserves the point,
ratio1/2,512bits,N32,64arcs,R7/8 and fixed calibration. This is explicitly
not blinded prediction or an independently discovered new root.

The final pre-freeze byte repair removed an extra terminal LF from BOTH
saved JSON files. The manifest's canonical JSON did not change; its byte
hash did, and the fixture's artifact entry and payload were consequently
resealed. The final exact scientific state, not any intermediate output,
is the review target. No mathematical value was silently altered after
freezing.

The author checker freshly authenticates sources and reconstructs the
signed jet and all64 arcs. Type/JSON/bit/size guards use explicit exceptions.
It inherits the accepted QT critical/cover proof rather than claiming to
reexecute the entire26-node source panel or all its outer covers.

The reviewer ran32 tests normally in100.677s and optimized in100.521s.
Each includes two fully fresh resealed attacks. The additional review
harness rejects17 strict invalid inputs in EACH mode and two more fully
resealed attacks in EACH mode: relabeling the physical point and deleting
the Cauchy tail while consistently changing all error ratios. These
additional checks call the unpatched checker with full reconstruction;
no source, build result or arithmetic function is mocked.

Scientific fixture LF SHA256:

    aef1379325c101b31bdad40940066daa1fdae3a37496008a28fb22fe31cdc735

Scientific payload SHA256:

    933343e38b42cd9cafb98ee7b1824c4d0dad76af2f5271c3225dc7e4802438c9

No actionable mathematical defect was found. This certifies one
source-exact critical-point/companion-root correspondence. It does not
prove a continuous parameter homotopy, a new zero census, uniform
high-height transport, physical capture, innerness, RH or external novelty.
A nonreal derivative-companion zero is not an off-line classical Xi zero.

## 4. Final release protocol

Both fresh producer checks pass. All four normal/optimized fixture and
source-manifest emits agree exactly after LF normalization. Both independent
fixture checks also pass. Ruff, formatting, source immutability and the full
QT-base-to-source and source-to-review whitespace checks pass. The review
adds only its four identified files; the five scientific files are unchanged.
