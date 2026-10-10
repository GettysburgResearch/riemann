import OAI.NumberTheory.SiegelZeros.Main
#check @OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap
#check @OAI.SiegelZeros.WeightedTorusJets.dirichletRealZeroBound_proof
#print axioms OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap
#print axioms OAI.SiegelZeros.WeightedTorusJets.dirichletRealZeroBound_proof
open Lean in
#eval show CoreM Unit from do
  let env ← getEnv
  let mods := env.header.moduleNames
  let hasSeven := mods.any (fun m => m == `OAI.NumberTheory.DirichletL.Nonvanishing)
  let nDirichletL := (mods.filter (fun m => (`OAI.NumberTheory.DirichletL).isPrefixOf m)).size
  let nSiegel := (mods.filter (fun m => (`OAI.NumberTheory.SiegelZeros).isPrefixOf m)).size
  IO.println s!"imports OAI.NumberTheory.DirichletL.Nonvanishing: {hasSeven}; DirichletL modules loaded: {nDirichletL}; SiegelZeros modules loaded: {nSiegel}; total modules: {mods.size}"
