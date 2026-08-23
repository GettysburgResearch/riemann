import RiemannFormal.Statement.RH

namespace RiemannFormal

inductive FormalStatus where
  | unstated
  | stated
  | proved
  | provedConditional
  | upstreamProved
  | blockedLibrary
  | blockedMathematics
  | refutedFormalized
  | superseded
  deriving DecidableEq, Repr

def scientificReleaseCommit : String :=
  "852d8aa05c701ea7818ce8a50543e68987fef5cc"

def scientificReleaseTree : String :=
  "35bd1a022c6b264f5af8f6f23d7926979fb9682d"

def researchCensusTerminalPR : Nat := 707

def canonicalSemanticClaimCount : Nat := 139

end RiemannFormal
