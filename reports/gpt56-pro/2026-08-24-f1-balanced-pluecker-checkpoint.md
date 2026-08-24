# F1 balanced Plücker checkpoint

The radial-owner repair at T-105440 made the full source coefficient-exact but
left two apparent endpoint objects: shared-owner stars and four-label
rectangles.

The current PR #719 source package changes that disposition.

1. Any common owner can be extracted from both physical products with exact
   Gram weight `1/ell`. The owner disappears and cannot recur. This includes a
   shared second owner, which is not covered by the literal shared-greatest
   display in L-102837.
2. The remaining clean sector has four distinct owner primes and unique
   semiprime squareclasses.
3. Its Plücker rectangle is exactly a tensor of two nontrivial augmentation
   local systems. No zero frequency remains.
4. Fixed owner moduli, owner/core overlaps and Type-I square lattices are
   already paid.
5. The only direct theorem is the coherent signed balanced packet
   `F1BPT105450=BQSP102870`.

RH remains unproved.
