# A complete native primitive preimage of the canonical zero chart

This packet closes one finite composition diagram. It reconstructs every one
of the 24 canonical Boolean histories from the literal half-geodesic source,
including every factor allocation, derivative site, the measure `2 ds`, both
owner orders and the separate Beta measure. The reconstructed completed
coefficient is zero. The held-out dense tuple reconstructs its positive
coefficient `1/9` through the same map.

This is a source-defined preimage of the canonical coefficient, not an
identification with the complete retained-carrier/renewal member of T-106140.
Product collapse precedes owner extraction and completion. It does not
preserve the primitive ratio observation or its diagonal.

## 1. The ordered diagram and its physical weights

Use the exact labelled sources of L-102707 and L-106132/133, authenticated in
the replay. All labels in the two fixtures are distinct physical primes
apart from explicitly shared bilateral cores; neither fixture uses a 67
alias. Put

\[
 \Lambda_s=\prod_p\{s\sqrt{1-x_p}+(1-s)\sqrt{1-x_p^2}\},
 \qquad {cal V}=\int_0^1(\partial_s\Lambda_s)\otimes\Lambda_s\,2ds.
 \tag{1}
\]

At a squarefree raw support R of size r>0, an allocation L subset R and
derivative site j in L have stripped integrand

\[
 (-1/2)^r s^{r-1}.
 \tag{2}
\]

There are r*2^(r-1) such site records. Their complete sum under `2 ds` is
`(-1)^r`. Equivalently, squarefree product collapse of (1) is `mu-epsilon`.
The left-root-free factor allocation is retained with coefficient zero.
This calculation is finite and uses the actual measure once.

Fix distinct owners p,q and a disjoint squarefree core C. For each ordered
Boolean partition C=A disjoint-union B disjoint-union D, use the raw support

\[
 R_D=\{p,q\}\cup D,\qquad K_D=pqD.
 \tag{3}
\]

Here products and supports share notation only in formulas specifying a
physical integer. Extract the owner coefficient **after** product collapse.
The two owners kill the epsilon coefficient and contribute sign +1, so this
coefficient is exactly mu(D). Multiply it by a_U(A)a_U(B), sum the Boolean
partitions, and obtain

\[
 b_U(C)=(a_U\star a_U\star\mu)(C)
       =(a_U\star h)\star(a_U\star h)(C),\quad h(S)=(-1/2)^{|S|}.
 \tag{4}
\]

Owner extraction means a coefficient map on the labelled source. It is not
an ordinary derivative on a quotient that kills square monomials.

For k=|C|+2, the two owner orders each carry the exact independent base
measure `(1-theta)dtheta`, while `theta^(k-2)` remains in the integrand:

\[
 (1-\theta)\theta^{k-2}d\theta,
 \qquad \int_0^1(1-\theta)\theta^{k-2}d\theta=1/[k(k-1)].
 \tag{5}
\]

Their sum is the source's canonical share 1/binom(k,2). Neither theta nor
its measure is the homotopy parameter s. Completion then sends the raw
physical product K_D to N=pq C^2. Its amplitude multiplier is

\[
 \sqrt{K_D/N}=\sqrt D/C.
 \tag{6}
\]

Thus the literal nested history has final physical coefficient

\[
 \frac{a_U(A)a_U(B)\mu(D)}{\binom{k}{2}\sqrt N}.
 \tag{7}
\]

Formula (6) is independent of the inner factor allocation, but is not
independent of the Boolean history. It is part of this declared map, not
a claim of norm preservation. The diagram is

```
all native half-geodesic factors and sites, with 2 ds
  -> product collapse at pqD -> owner coefficient extraction
  -> a_U(A)a_U(B) and complete Boolean partition sum
  -> both owner orders and (1-theta) theta^(k-2) dtheta
  -> completed physical index pq C^2 -> original Mellin observation.
```

The alternative route in (4), directly expanding the authenticated Boolean
half-source square, gives the same coefficient and is an independent replay
check. Its intermediate atoms and diagonal need not agree.

## 2. Actual endpoint colours give another finite preimage

At each prime, the L-102904 probability experiment chooses `E tensor C` or
`C tensor E` with equal probability, E=1-x and C=1-x^2. On a squarefree raw
support R, each of its 2^r colour assignments has precisely one nonzero
allocation, placing the prime in its E slot. That allocation contributes
`(-1)^r`. After product collapse the probability mean is therefore mu(R),
and its probability diagonal is 1. The counting diagonal of already weighted
colour atoms would instead be 2^(-r); it is a different resolution.

Owner extraction, (4)--(6), give the same canonical coefficient. This is an
authenticated colour measure, not a declaration that an empty colour or
renewal label makes every later carrier coefficient equal to one. The
colour preimage and the geodesic preimage have different ratio fields.

## 3. The full 24-history zero chart

Use the predecessor's actual U=64 chart

```
p,q = 2,3;       C = {71,73,79};  N = 6*(71*73*79)^2
r,s = 5,7;       D = {401,421};   M = 35*(401*421)^2.
```

For these rough cores, a_U(empty)=0 and a_U(nonempty)=-1. The left core
has 12 nonzero histories: six have empty D and sign +1; six have a singleton
D and sign -1. The right core has two histories, both with empty remainder
and sign +1. Hence all 24 bilateral histories are retained, twelve of each
sign, each of modulus 1/(60 sqrt(NM)). Their sum is zero.

The replay opens every inner primitive cone rather than substituting its
endpoint sum. On the left this is 96 nonzero derivative-site records before
the two owner orders; on the right it is eight. Including both owner orders
on each side gives 3072 bilateral nested site records: 768 positive records
of coefficient 1/3840, and 2304 negative records of coefficient -1/11520,
before the common 1/sqrt(NM). Their exact sum is zero.

Every branch is observed only after completion, so its final Mellin phase is
the same physical N/M. The zero is therefore exact for the original
`|kappahat(t)|^2 dt/(2pi)` observation as well as coefficientwise. This does
not say that the primitive ratio field at the different raw indices K_D
was zero. In particular it does not identify this preimage with the earlier
3888-factor primitive at the already completed product NM.

Three legitimate diagonal resolutions, stated after transporting to the
same completed physical output, are

\[
 D_{\rm continuous}=\frac{29}{25200NM},\qquad
 D_{\rm integrated\ site}=\frac1{14400NM},\qquad
 D_{\rm history}=\frac1{150NM}.
 \tag{8}
\]

The first integrates the squared branch integrand with the product of the
two `2 ds` measures and two base measures `(1-theta)dtheta`. In particular,
the depth factor becomes `theta^(2|C|)` when the integrand is squared; it
is not absorbed into an unchanged measure. The second integrates those
parameters before squaring each site branch. The third combines all inner
sites and owner orders into the 24 original histories before squaring.
The completely recombined coefficient diagonal is zero. Multiplying (8)
by Gamma(0) gives the corresponding same-frequency observed diagonals;
none is asserted to be the full T-106140 paid diagonal.

## 4. Held-out positive tuple and exact scope

Use the previously frozen dense fixture's first actual pair, with cutoff
U=2^20, owners (1049639,1050713) and (1051747,1052797), common prime
1053821, and reduced core primes 1054903 and 1055917. Each two-prime core
has two +1 histories and share 1/6. The same construction gives four
bilateral histories of coefficient 1/36, sum 1/9, and 256 nested site
records each of coefficient 1/2304. Its three stripped diagonals are
1/2025, 1/20736 and 1/324, in the order of (8).

This checks a zero and a positive source with the same fixed maps, measures
and normalization; no coefficient was chosen to force either answer.
The exact half-source identity, primitive reconstruction and completion are
now bound on these tuples. The identification of the complete carrier,
marked, renewal and region-dependent weights with this composite map remains
open. An arbitrary pre-collapse ratio mask does not commute with this
diagram; no new full native moment estimate follows.

## 5. Replay and provenance

The producer authenticates the frozen geodesic executable and its exact Git
source blobs before execution, then separately authenticates L-106132,
L-106133, L-102904 and the predecessor/held-out fixture. All arithmetic is
rational, all allocations and derivative sites are retained, and the
fixture comparison uses canonical typed JSON. The maximum raw inner support
has three labels; the large physical output integers do not require a
large arithmetic sweep. Validation is performed by the coordinating agent;
this note does not claim a run before that happens.
