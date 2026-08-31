# A bounded single top-class witness

This is a new contract, declared before its execution. The frozen central
20-test contract at `547d91b6c8f8432f0f594c634e8a58349c929288` remains
unchanged and uncompleted by this packet. Its authenticated source,
central-matrix and complete-old-column builders may be used; its full
kernel/build entrypoints may not. The accepted prefix and global promotion
proof are at `ed8c7251719a381abf6d55f57d768d69e76b776d`.

The aim is one actual degree-seven relation of weight (7,7,7), rather
than a measured 50-vector central kernel. Fresh construction retains all
592 original central D2 columns, their original row addresses, and every
matching old multiple of the accepted eleven degree-five and seventeen
degree-six D3 columns. The actual old list must have exactly 49 columns.

For each of the fixed primes 65521 and 1000003, in that order, select 49
old-coordinate rows. A nonzero determinant modulo the prime of the actual
49-by-49 minor proves those complete old columns independent over Q.
Require the sought vector to vanish on these 49 coordinates. This leaves
543 coordinates. Modular row selection and a square subsystem of size at
most 542 are discovery tools only. Stop selection after 542 independent
rows; no modular census of the remaining rows is claimed. Normalize the
one unselected coordinate to one and solve the square subsystem by a
fixed modular LU and at most sixteen Dixon lifts. Rational reconstruction
after each lift is a candidate generator, not a proof of rational rank or
uniqueness. A modular rank drop, reconstruction failure, failed exact
residual, or exhausted lift budget is retained explicitly. Try the second
prime after a failed first attempt; exhaustion is UNKNOWN, not a proof
that the class does not exist.

Acceptance has only exact conditions: the candidate is a nonzero primitive
integer vector, all 49 gauge coordinates are zero, every original D2 row
has exact zero residual, and the complete old-coordinate minor has the
certified nonzero modular determinant. A vector in the old span with all
gauge coordinates zero would have zero coefficients in that invertible
minor. The accepted nonzero vector therefore lies outside the complete old
span. This proves nonmembership over Q without rational elimination of
the old span or a full central kernel.

The frozen global theorem then applies: the independent Tor3 source has
exactly this one missing class, graded Nakayama completes D3, and Tor4=0
proves injectivity. Fresh polynomial composition, weight and grading
checks must still run for the actual added column. Global old/kernel
dimensions 775/776 are deductions after this theorem, not measured
matrices. The old 20/52/42/26 and full-composed contracts are not executed
or completed by this packet. Marked lifts are not claimed equivariant.

Resource limits remain 128 MiB for the root-owned worker and a 2 GiB free
RAM reserve. Mathematical limits are 592/49/543 source/gauge/reduced
coordinates, at most 4096 supported original rows, at most sixteen lifts
per fixed prime, and 4096 bits for stored exact inputs, reconstructed
fractions, accepted primitive coefficients and checked residuals. This is
not instrumentation of every transient arithmetic intermediate. Modular
matrices use standard-library unsigned integer arrays; no numerical
linear-algebra dependency, random prime, adaptive cap, or floating-point
candidate is permitted. Serialized proof data are capped at 64 MiB.

The artifact retains all original columns and old multiples, the old
minor, selected subsystem addresses, every attempted lift and failed
bounded residual, the successful integer witness and actual polynomial
map. SHA-pinned input authentication precedes helper compilation and
artifact parsing. Canonical typed JSON, body digests and all four owned
file identities are checked. --check regenerates the bounded discovery
and every exact acceptance condition. No execution has yet occurred.
