# Primary-source record for the integrated zeta argument bound

Read independently on 2026-10-10. These are imported unconditional analytic
theorems, not rederived in this research wave. The displayed absolute-value
bars were checked in rendered PDF pages because text extraction omits them.

## The 2011 paper

Timothy Trudgian, *Improvements to Turing's Method*, Mathematics of
Computation 80 (2011), 2259–2279. Author preprint
[arXiv:0903.1885v3](https://arxiv.org/abs/0903.1885v3), version date
2010-08-05; the arXiv primary metadata supplies the journal citation.

PDF: https://arxiv.org/pdf/0903.1885v3.
Local source: `/workspace/.riemann-research/sources/trudgian-turing-0903.1885v3.pdf`.
SHA256: e8d021a3c083d0f07427760661478e47390d446d06714257dee702246facc878.
Extracted text has the same stem with `.txt`, SHA256
c68fd1c01587cb3dcd44552a94b39ebced45158ac270383701ad53e7049522e5.

PDF page 2, equation (1.1), defines S(T)=arg zeta(1/2+iT)/pi away
from zero ordinates. The argument is continued along the polygon
2 -> 2+iT -> 1/2+iT, starting with arg zeta(2)=0. The theorem is about
this continued argument, rather than the principal argument at its end.
Any convention for values at the discrete zero ordinates gives the same
integral. The conventional mean of the two limiting values can be used.

PDF page 3, **Theorem 2.2**, states exactly:

    | integral_(t1)^(t2) S(t) dt | <= 2.067 + 0.059 log(t2),
    for every t2 > t1 > 168*pi.                            (T1)

The first paragraph on PDF page 4 explicitly says the constants are valid
for all such t1,t2. The later reference to 2*pi*10^12 describes the scale
at which the constants were optimized; it is not a theorem hypothesis.
No RH or verified-zero-census hypothesis is imposed. Logarithms are natural.
Footnote 3, PDF page 4, discusses the possibility of lowering the starting
height but does not change the safe stated 168*pi threshold used here.

Two printed introduction conventions must not be imported as count facts:
the displayed value at a zero omits the usual factor 1/2, and the prose
describes N(T) using both signs while equation (1.2) uses the usual
positive-ordinate normalization. Neither changes the literal argument
function away from its isolated discontinuities or bound (T1). The
successor paper below defines N(T) explicitly with 0<Im(rho)<T.

## The successor

T. S. Trudgian, *Improvements to Turing's Method II*,
[arXiv:1406.3416v2](https://arxiv.org/abs/1406.3416v2), version date
2014-10-17. The PDF cover's typesetting date is different from the pinned
arXiv version date; the citation here uses the arXiv identifier/version.

PDF: https://arxiv.org/pdf/1406.3416v2.
Local source: `/workspace/.riemann-research/sources/trudgian-turing2-1406.3416v2.pdf`.
SHA256: 00529b8cf9572bc24bbff72106bb7f0c7e620ce39ab300e519dde35226b2263d.
Extracted text has the same stem with `.txt`.

**Theorem 1**, PDF pages 1–2, states:

    | integral_(t1)^(t2) S(t) dt |
       <= 1.698 + 0.183 log log(t2) + 0.049 log(t2),
    for every t2 > t1 > 10^5.                             (T2)

Theorem 2, PDF page 5, gives the parameterized constants and permits
t2>=t1>=10^5. PDF page 6, Table 1 and its immediately preceding paragraph,
say all displayed triples are valid for t1>=10^5, with the row heights
describing near-optimal choices rather than applicability thresholds.
For example the T=10^6 row gives a=1.520, b=0.197, c=0.058. The main
explicit theorem (T2) or original (T1) are simpler imports when no
table-parameter revalidation is desired.

## Scope for the height adapter

These bounds control the integral of the complete continued zeta argument
on every interval above the stated threshold. They do not bound S(T)
pointwise and do not certify an individual critical-line zero or a
complete finite census. Any endpoint-selection or weighted integration
argument must be proved separately using this exact normalization and
its own smooth gamma/count correction. The primary PDFs are sufficient
to import (T1)/(T2); the earlier research's finite-count boundary remains
a separate input.
