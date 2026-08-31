# Actual S3 arithmetic phase scout

Declared 2026-08-31 before the first atlas enumeration. This is discovery data,
not an analytic theorem or a new arbitrary Frobenius-polynomial family.

Source: the existing PR769 S3 cover x^3+A*x+B=u^2, with elliptic quotient
E:y^2=x^3+A*x+B and discriminant quotient
D:v^2=-4*A^3-27*(B-u^2)^2. Retain A!=0 and 4*A^3+27*B^2!=0.
The prior source and its finite cohomological ladder are frozen at
7b320b3a9a55a16e73d99dd9bbab5bf592d50c93; completion proof freeze
64075f1a3f81529f217dee1ae139656dfb9356f3.

Enumerate every A,B in each prime field p=5,7,11,13,17,19,23,29,31.
Use exact integer modular arithmetic and complete square-residue tables.
Count E with one infinity point and D with 1+chi(-27) infinity points.
Independently enumerate every cubic fibre over rational u. At good fibres,
retain root count and chi(u); at old ramification retain chi(u). Include
the unramified u=0 fibre in the genus-three cover point count, while retaining
its separate new quadratic-twist ramification label.

Predicted consistency, not an empirical law: if g counts all completely split
good rational fibres, r counts old rational ramification, and delta is one
for p=1 mod3, then #Z=6g+3r+2delta and a_D+2a_E=p+1-#Z.

Discovery targets: the actual values of t_Z=a_D+2a_E and t_Z/12; where this
candidate leading multiplier exponent is fractional, negative integral,
positive integral, or zero; which such cases have rational old ramification
or split infinity. Record representative examples without declaring any
first-radius theorem merely from traces. A subsequent proof must remove
finite arithmetic poles and distinguish multiplier zeros from singularities.

Do not count isomorphic curves as distinct moduli points. This is exhaustive
parameter enumeration within its declared finite panels, not an isomorphism
census. JavaScript discovery will be independently replayed in a source-bound
Python packet if it produces a useful theorem target.
