/- Generated candidate edges; uncompiled and dependent on the retuned overlay. -/
import Submissions.arvi_density.Return.Formulas
set_option autoImplicit false
set_option linter.unnecessarySeqFocus false
set_option maxHeartbeats 1000000
namespace QRH.ArviDensity.Return
noncomputable section
def edge131_0_000_coefficients : Fin 3 → Fin 4 → ℝ := ![![(10027158667685362505583271/530720442628535418750000:ℝ), (26819834309673981836374243/530720442628535418750000:ℝ), (23558192616291876155998673/530720442628535418750000:ℝ), (6765516974303256825207701/530720442628535418750000:ℝ)], ![(2477422719427156649435129/132680110657133854687500:ℝ), (4534684643254804405872907/106144088525707083750000:ℝ), (1043016787099706173529302/33170027664283463671875:ℝ), (3924536255029903344844813/530720442628535418750000:ℝ)], ![(401082796107481153431449/106144088525707083750000:ℝ), (72528740901011864953163/10614408852570708375000:ℝ), (1010194056086186416085527/265360221314267709375000:ℝ), (318625506059732576670149/530720442628535418750000:ℝ)]]
theorem edge131_0_000_identity (δ p : ℝ) : rowMargin .oldSmall .old δ p =
 Record12518109.Bernstein.bsum 2 3 (318625506059732576670149/7548024072939170400000000:ℝ) edge131_0_000_coefficients (0:ℝ) (3/4:ℝ) (0:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_0_000_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_0_000_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (0:ℝ) (3/4:ℝ))
 (hp : p ∈ Set.Icc (0:ℝ) (1/2:ℝ)) : 0 < rowMargin .oldSmall .old δ p := by
 rw [edge131_0_000_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_0_000_coefficients]
def edge131_1_000_coefficients : Fin 3 → Fin 4 → ℝ := ![![(3733307362107680742812549/1061440885257070837500000:ℝ), (7315943309748937138350311/1061440885257070837500000:ℝ), (1614170112156292423946191/353813628419023612500000:ℝ), (371834867917905108766937/353813628419023612500000:ℝ)], ![(4016760159384663278940497/530720442628535418750000:ℝ), (9342493599926582261957/849152708205656670000:ℝ), (448307616236850233170667/106144088525707083750000:ℝ), (130500170466989431070707/530720442628535418750000:ℝ)], ![(1709195299537985833013689/212288177051414167500000:ℝ), (2790206852028364150911331/212288177051414167500000:ℝ), (7076762051757725820519887/1061440885257070837500000:ℝ), (1094225149010212031031677/1061440885257070837500000:ℝ)]]
theorem edge131_1_000_identity (δ p : ℝ) : rowMargin .oldSwitch .old δ p =
 Record12518109.Bernstein.bsum 2 3 (130500170466989431070707/60384192583513363200000000:ℝ) edge131_1_000_coefficients (3/8:ℝ) (3/4:ℝ) (0:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_1_000_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_1_000_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3/8:ℝ) (3/4:ℝ))
 (hp : p ∈ Set.Icc (0:ℝ) (1/2:ℝ)) : 0 < rowMargin .oldSwitch .old δ p := by
 rw [edge131_1_000_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_1_000_coefficients]
def edge131_1_001_coefficients : Fin 3 → Fin 4 → ℝ := ![![(6919663091938636072941601/1061440885257070837500000:ℝ), (18381066849391024810220243/1061440885257070837500000:ℝ), (16003144422966141401615683/1061440885257070837500000:ℝ), (504637851723750296037449/117937876139674537500000:ℝ)], ![(2957352348187335259069549/530720442628535418750000:ℝ), (7315321469613671520132341/530720442628535418750000:ℝ), (1193195188364682906995731/106144088525707083750000:ℝ), (1608006820397078273915863/530720442628535418750000:ℝ)], ![(3240805145464317795197497/1061440885257070837500000:ℝ), (1167687331963769659101031/212288177051414167500000:ℝ), (373889298504309825443713/117937876139674537500000:ℝ), (623002387110352378685759/1061440885257070837500000:ℝ)]]
theorem edge131_1_001_identity (δ p : ℝ) : rowMargin .oldSwitch .old δ p =
 Record12518109.Bernstein.bsum 2 3 (623002387110352378685759/60384192583513363200000000:ℝ) edge131_1_001_coefficients (0:ℝ) (3/8:ℝ) (0:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_1_001_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_1_001_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (0:ℝ) (3/8:ℝ))
 (hp : p ∈ Set.Icc (0:ℝ) (1/2:ℝ)) : 0 < rowMargin .oldSwitch .old δ p := by
 rw [edge131_1_001_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_1_001_coefficients]
def edge131_2_000_coefficients : Fin 3 → Fin 4 → ℝ := ![![(197329958223621923/56781393862500000:ℝ), (390505881365430797/56781393862500000:ℝ), (261591478058777521/56781393862500000:ℝ), (60939881316968647/56781393862500000:ℝ)], ![(212493162455870519/28390696931250000:ℝ), (502543452806339/45425115090000:ℝ), (25182172461797069/5678139386250000:ℝ), (9363019560893989/28390696931250000:ℝ)], ![(90956388427623823/11356278772500000:ℝ), (149903277477299077/11356278772500000:ℝ), (385252723038199249/56781393862500000:ℝ), (60615583389822979/56781393862500000:ℝ)]]
theorem edge131_2_000_identity (δ p : ℝ) : rowMargin .newSwitch .old δ p =
 Record12518109.Bernstein.bsum 2 3 (9363019560893989/3230230406400000000:ℝ) edge131_2_000_coefficients (3/8:ℝ) (3/4:ℝ) (0:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_2_000_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_2_000_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3/8:ℝ) (3/4:ℝ))
 (hp : p ∈ Set.Icc (0:ℝ) (1/2:ℝ)) : 0 < rowMargin .newSwitch .old δ p := by
 rw [edge131_2_000_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_2_000_coefficients]
def edge131_2_001_coefficients : Fin 3 → Fin 4 → ℝ := ![![(184170347165543701/28390696931250000:ℝ), (488907994099129543/28390696931250000:ℝ), (425304946701627983/28390696931250000:ℝ), (120567299768042141/28390696931250000:ℝ)], ![(78189161556667999/14195348465625000:ℝ), (97389203023196933/7097674232812500:ℝ), (31990680117445771/2839069693125000:ℝ), (10841039024375747/3548837116406250:ℝ)], ![(85770763672792297/28390696931250000:ℝ), (31314058873131881/5678139386250000:ℝ), (92113092712332767/28390696931250000:ℝ), (17575725219465659/28390696931250000:ℝ)]]
theorem edge131_2_001_identity (δ p : ℝ) : rowMargin .newSwitch .old δ p =
 Record12518109.Bernstein.bsum 2 3 (17575725219465659/1615115203200000000:ℝ) edge131_2_001_coefficients (0:ℝ) (3/8:ℝ) (0:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_2_001_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_2_001_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (0:ℝ) (3/8:ℝ))
 (hp : p ∈ Set.Icc (0:ℝ) (1/2:ℝ)) : 0 < rowMargin .newSwitch .old δ p := by
 rw [edge131_2_001_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_2_001_coefficients]
def edge131_3_000_coefficients : Fin 3 → Fin 4 → ℝ := ![![(7175062025231208860303999473/188556287915250000000000000:ℝ), (315077874220405450179719703007/5091019773711750000000000000:ℝ), (13229659387382293975645155893/509101977371175000000000000:ℝ), (2473570839338537869713670847/2545509886855875000000000000:ℝ)], ![(53394169047517503744408291551/424251647809312500000000000:ℝ), (58909342327605506763932865331/254550988685587500000000000:ℝ), (163431348812676797749290858547/1272754943427937500000000000:ℝ), (5013661842642614623835281309/254550988685587500000000000:ℝ)], ![(91980486601539590319410568691/848503295618625000000000000:ℝ), (564378275109790977151329360347/2545509886855875000000000000:ℝ), (373230367620034827514429715683/2545509886855875000000000000:ℝ), (79461772176211018596432061409/2545509886855875000000000000:ℝ)]]
theorem edge131_3_000_identity (δ p : ℝ) : rowMargin .newTop .old δ p =
 Record12518109.Bernstein.bsum 2 3 (2473570839338537869713670847/4633959331805184000000000000000:ℝ) edge131_3_000_coefficients (9/16:ℝ) (3/4:ℝ) (1/4:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_000_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_000_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (9/16:ℝ) (3/4:ℝ))
 (hp : p ∈ Set.Icc (1/4:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .old δ p := by
 rw [edge131_3_000_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_000_coefficients]
def edge131_3_001_coefficients : Fin 3 → Fin 4 → ℝ := ![![(204955022887609704693470765196157/106062911952328125000000000:ℝ), (1360730957485146362726878060143637/318188735856984375000000000:ℝ), (1395653371053214934254598593067/497169899776538085937500:ℝ), (287617683183234835769192425247/621462374720672607421875:ℝ)], ![(16636637490060423873903848668397/3314465998510253906250000:ℝ), (118538025072335086847530048854349/9943397995530761718750000:ℝ), (5524293663353007893562178461086/621462374720672607421875:ℝ), (1234669545152207979065606554498/621462374720672607421875:ℝ)], ![(144543884326690749865215547403/46034249979309082031250:ℝ), (9696995033666704920251765983867/1242924749441345214843750:ℝ), (775238622075324672175595483207/124292474944134521484375:ℝ), (978850586558096553524207048417/621462374720672607421875:ℝ)]]
theorem edge131_3_001_identity (δ p : ℝ) : rowMargin .newTop .old δ p =
 Record12518109.Bernstein.bsum 2 3 (287617683183234835769192425247/1186293588942127104000000000000000:ℝ) edge131_3_001_coefficients (141/256:ℝ) (9/16:ℝ) (31/64:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_001_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_001_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (141/256:ℝ) (9/16:ℝ))
 (hp : p ∈ Set.Icc (31/64:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .old δ p := by
 rw [edge131_3_001_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_001_coefficients]
def edge131_3_002_coefficients : Fin 3 → Fin 3 → ℝ := ![![(283793748538696407288961717/6052050000000000000000:ℝ), (74008628428179462715501/1108163452148437500:ℝ), (730401452439202836567041/35461230468750000000:ℝ)], ![(692729167654808650086864541/6052050000000000000000:ℝ), (3072015690652185125897111/17730615234375000000:ℝ), (133495931525573634236521/2216326904296875000:ℝ)], ![(885269298344573963976583/12911040000000000000:ℝ), (7691029024276670408257693/70922460937500000000:ℝ), (2879883562241680654193359/70922460937500000000:ℝ)]]
theorem edge131_3_002_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (730401452439202836567041/1057672396800000000000000000:ℝ) edge131_3_002_coefficients (69/128:ℝ) (141/256:ℝ) (31/64:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_002_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_002_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (69/128:ℝ) (141/256:ℝ))
 (hp : p ∈ Set.Icc (31/64:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_002_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_002_coefficients]
def edge131_3_003_coefficients : Fin 3 → Fin 4 → ℝ := ![![(67559802989916743637108239866189/127275494342793750000000000:ℝ), (770551004435978189064621059090987/636377471713968750000000000:ℝ), (535689424685507455911429517171957/636377471713968750000000000:ℝ), (20578672940780888575715331169883/127275494342793750000000000:ℝ)], ![(103924385368316861421325751530213/63637747171396875000000000:ℝ), (1300731104221158199487543990735531/318188735856984375000000000:ℝ), (1050906861464130551945953904856571/318188735856984375000000000:ℝ), (53950339496172157898307281854421/63637747171396875000000000:ℝ)], ![(29449989646878202050009572339489/25455098868558750000000000:ℝ), (1934178236388592464861087031703723/636377471713968750000000000:ℝ), (1668256907661932184647893360055083/636377471713968750000000000:ℝ), (94056085284809381322504307367717/127275494342793750000000000:ℝ)]]
theorem edge131_3_003_identity (δ p : ℝ) : rowMargin .newTop .old δ p =
 Record12518109.Bernstein.bsum 2 3 (20578672940780888575715331169883/60738231753836907724800000000000000:ℝ) edge131_3_003_coefficients (69/128:ℝ) (9/16:ℝ) (15/32:ℝ) (31/64:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_003_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_003_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (69/128:ℝ) (9/16:ℝ))
 (hp : p ∈ Set.Icc (15/32:ℝ) (31/64:ℝ)) : 0 < rowMargin .newTop .old δ p := by
 rw [edge131_3_003_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_003_coefficients]
def edge131_3_004_coefficients : Fin 3 → Fin 4 → ℝ := ![![(26574413800899887555655557/364352322656250000000:ℝ), (16026767759488459181759369/101208978515625000000:ℝ), (1967105368870421128297187/18976683471679687500:ℝ), (51505553380120701852748/2846502520751953125:ℝ)], ![(12973136463899453008202261/72870464531250000000:ℝ), (122766695750868474864892111/303626935546875000000:ℝ), (5441383031185363307026831/18976683471679687500:ℝ), (171154608744459630785984/2846502520751953125:ℝ)], ![(159594783723012675898566173/1457409290625000000000:ℝ), (314248001734970049858285043/1214507742187500000000:ℝ), (14831581701043536350376443/75906733886718750000:ℝ), (130915054023383377296346/2846502520751953125:ℝ)]]
theorem edge131_3_004_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (12876388345030175463187/42450122342400000000000000:ℝ) edge131_3_004_coefficients (33/64:ℝ) (69/128:ℝ) (15/32:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_004_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_004_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (33/64:ℝ) (69/128:ℝ))
 (hp : p ∈ Set.Icc (15/32:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_004_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_004_coefficients]
def edge131_3_005_coefficients : Fin 3 → Fin 4 → ℝ := ![![(32029016027156280107395178453783/1272754943427937500000000000:ℝ), (65676626823246282828404748581629/1272754943427937500000000000:ℝ), (37163129661859814670202652348351/1272754943427937500000000000:ℝ), (233023871474702371759303606367/84850329561862500000000000:ℝ)], ![(54099700705016306973098838797711/636377471713968750000000000:ℝ), (128035221304582643036160584774413/636377471713968750000000000:ℝ), (95830123446462613713012083297717/636377471713968750000000000:ℝ), (1458173950254955985914008321401/42425164780931250000000000:ℝ)], ![(85458867046806803299236660922607/1272754943427937500000000000:ℝ), (217658419517333322811501359993421/1272754943427937500000000000:ℝ), (181174631526271134531188192746349/1272754943427937500000000000:ℝ), (3263405736341378853777429578369/84850329561862500000000000:ℝ)]]
theorem edge131_3_005_identity (δ p : ℝ) : rowMargin .newTop .old δ p =
 Record12518109.Bernstein.bsum 2 3 (233023871474702371759303606367/1265379828204935577600000000000000:ℝ) edge131_3_005_coefficients (33/64:ℝ) (9/16:ℝ) (7/16:ℝ) (15/32:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_005_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_005_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (33/64:ℝ) (9/16:ℝ))
 (hp : p ∈ Set.Icc (7/16:ℝ) (15/32:ℝ)) : 0 < rowMargin .newTop .old δ p := by
 rw [edge131_3_005_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_005_coefficients]
def edge131_3_006_coefficients : Fin 3 → Fin 4 → ℝ := ![![(26075350903278094479817/9108808066406250000:ℝ), (25292742585649123380143/4858030968750000000:ℝ), (7405214399478195549907/3036269355468750000:ℝ), (73675608924892143731/1138601008300781250:ℝ)], ![(647087580856719128306609/91088080664062500000:ℝ), (1643316936267580093522877/121450774218750000000:ℝ), (108242760812816863368481/15181346777343750000:ℝ), (1810847253876987820408/2846502520751953125:ℝ)], ![(2210635257804631406356097/455440403320312500000:ℝ), (1625065468015909471272293/161934365625000000000:ℝ), (1908164881730507413312387/303626935546875000000:ℝ), (12139632255781254025877/11386010083007812500:ℝ)]]
theorem edge131_3_006_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (73675608924892143731/2122506117120000000000000:ℝ) edge131_3_006_coefficients (15/32:ℝ) (33/64:ℝ) (7/16:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_006_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_006_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (15/32:ℝ) (33/64:ℝ))
 (hp : p ∈ Set.Icc (7/16:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_006_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_006_coefficients]
def edge131_3_007_coefficients : Fin 3 → Fin 4 → ℝ := ![![(26712778687685682232573181119/20364079094847000000000000:ℝ), (251431090269041792168528806793/101820395474235000000000000:ℝ), (119039791098638145441983618251/101820395474235000000000000:ℝ), (839358009359039266014467053/101820395474235000000000000:ℝ)], ![(1165149396526545115189198548751/254550988685587500000000000:ℝ), (511178641942151148818512331801/50910197737117500000000000:ℝ), (1716495096131239111387010409593/254550988685587500000000000:ℝ), (323751865395034131461809799339/254550988685587500000000000:ℝ)], ![(10949022735903059391457243490939/2545509886855875000000000000:ℝ), (26854109172874944567254849862353/2545509886855875000000000000:ℝ), (21455738061982833980004908133721/2545509886855875000000000000:ℝ), (5538655119698982698076276762307/2545509886855875000000000000:ℝ)]]
theorem edge131_3_007_identity (δ p : ℝ) : rowMargin .newTop .old δ p =
 Record12518109.Bernstein.bsum 2 3 (839358009359039266014467053/47451743557685084160000000000000:ℝ) edge131_3_007_coefficients (15/32:ℝ) (9/16:ℝ) (3/8:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_007_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_007_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (15/32:ℝ) (9/16:ℝ))
 (hp : p ∈ Set.Icc (3/8:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .old δ p := by
 rw [edge131_3_007_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_007_coefficients]
def edge131_3_008_coefficients : Fin 3 → Fin 4 → ℝ := ![![(4216337192104571434174964099/7287046453125000000000:ℝ), (693589637126350498244444051/607253871093750000000:ℝ), (11030347540378711514782747/18976683471679687500:ℝ), (49037494699578212379416/2846502520751953125:ℝ)], ![(115596384215175872041352693/91088080664062500000:ℝ), (6508548425606031736365491/2530224462890625000:ℝ), (1333176215035763636041828/948834173583984375:ℝ), (57418225684618437799568/569300504150390625:ℝ)], ![(16484646443634861260035807/22772020166015625000:ℝ), (2900899902515975741570423/1897668347167968750:ℝ), (873446385242194235528024/948834173583984375:ℝ), (328181622995869563523304/2846502520751953125:ℝ)]]
theorem edge131_3_008_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (6129686837447276547427/679201957478400000000000000:ℝ) edge131_3_008_coefficients (117/256:ℝ) (15/32:ℝ) (31/64:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_008_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_008_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (117/256:ℝ) (15/32:ℝ))
 (hp : p ∈ Set.Icc (31/64:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_008_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_008_coefficients]
def edge131_3_009_coefficients : Fin 3 → Fin 4 → ℝ := ![![(62118085644637703552281613551/7287046453125000000000:ℝ), (5146329458383988389207603771/303626935546875000000:ℝ), (40674482242072727171448803/4744170867919921875:ℝ), (417582675284439029848768/2846502520751953125:ℝ)], ![(32692838385603399249944704397/1821761613281250000000:ℝ), (916959541326760813345655899/25302244628906250000:ℝ), (90838647025109713809791524/4744170867919921875:ℝ), (2417375746594160897043584/2846502520751953125:ℝ)], ![(17637637258822443668903400679/1821761613281250000000:ℝ), (1523045248726483192416769619/75906733886718750000:ℝ), (53802475512991421880946988/4744170867919921875:ℝ), (2720816985488566562433856/2846502520751953125:ℝ)]]
theorem edge131_3_009_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (6524729301319359841387/2716807829913600000000000000:ℝ) edge131_3_009_coefficients (231/512:ℝ) (117/256:ℝ) (63/128:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_009_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_009_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (231/512:ℝ) (117/256:ℝ))
 (hp : p ∈ Set.Icc (63/128:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_009_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_009_coefficients]
def edge131_3_010_coefficients : Fin 3 → Fin 4 → ℝ := ![![(952247216419780967436591611183/7287046453125000000000:ℝ), (7915335081754005052606718263/30362693554687500000:ℝ), (622834112488022422366348012/4744170867919921875:ℝ), (3589058097615165037348352/2846502520751953125:ℝ)], ![(489749046476733962874067045147/1821761613281250000000:ℝ), (456412114406161161691364011/843408154296875000:ℝ), (1326926658737980964211293552/4744170867919921875:ℝ), (20957099904773340348408832/2846502520751953125:ℝ)], ![(255430105025756903452422134903/1821761613281250000000:ℝ), (435089325676791732536685811/1518134677734375000:ℝ), (733066267453353176720143408/4744170867919921875:ℝ), (925449324823557314918912/113860100830078125:ℝ)]]
theorem edge131_3_010_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (7009879096904619213571/10867231319654400000000000000:ℝ) edge131_3_010_coefficients (459/1024:ℝ) (231/512:ℝ) (127/256:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_010_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_010_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (459/1024:ℝ) (231/512:ℝ))
 (hp : p ∈ Set.Icc (127/256:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_010_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_010_coefficients]
def edge131_3_011_coefficients : Fin 3 → Fin 4 → ℝ := ![![(72164782776039327148332414133/569102512280273437500:ℝ), (214914057493525827488298251627/853653768420410156250:ℝ), (266762790780171708979949046016/2134134421051025390625:ℝ), (80545170332326217139900416/2134134421051025390625:ℝ)], ![(2924725482772941712420163028347/11382050245605468750000:ℝ), (8723538009989691287809969266629/17073075368408203125000:ℝ), (543888348083534380525444688576/2134134421051025390625:ℝ), (1801852423376376157039089664/2134134421051025390625:ℝ)], ![(1605127783051975308750598757599/12140853595312500000000:ℝ), (14495914250053424036608161300419/54633841178906250000000:ℝ), (290155097400451771315293088516/2134134421051025390625:ℝ), (6044579326291988297478563456/2134134421051025390625:ℝ)]]
theorem edge131_3_011_identity (δ p : ℝ) : rowMargin .newTop .C131 δ p =
 Record12518109.Bernstein.bsum 2 3 (19664348225665580356421/1018448615964672000000000000000:ℝ) edge131_3_011_coefficients (57/128:ℝ) (459/1024:ℝ) (127/256:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_011_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_011_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (57/128:ℝ) (459/1024:ℝ))
 (hp : p ∈ Set.Icc (127/256:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C131 δ p := by
 rw [edge131_3_011_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_011_coefficients]
def edge131_3_012_coefficients : Fin 3 → Fin 4 → ℝ := ![![(44144432073082580628796355257/910880806640625000000:ℝ), (34086219154974390411012152321/303626935546875000000:ℝ), (24173531157897093266952918341/303626935546875000000:ℝ), (14404764104658978172798912567/910880806640625000000:ℝ)], ![(45514742062137794348287751821/455440403320312500000:ℝ), (35253101478333137639315931259/151813467773437500000:ℝ), (12569735946589790980105856357/75906733886718750000:ℝ), (30344456449044734915789138747/910880806640625000000:ℝ)], ![(6097791648588361161986943383/113860100830078125000:ℝ), (5107814426656532143544687383/40483591406250000000:ℝ), (497518586946664431403736867/5397812187500000000:ℝ), (142488989370958783693933779647/7287046453125000000000:ℝ)]]
theorem edge131_3_012_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (14404764104658978172798912567/445121794853044224000000000000000:ℝ) edge131_3_012_coefficients (57/128:ℝ) (231/512:ℝ) (63/128:ℝ) (127/256:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_012_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_012_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (57/128:ℝ) (231/512:ℝ))
 (hp : p ∈ Set.Icc (63/128:ℝ) (127/256:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_012_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_012_coefficients]
def edge131_3_013_coefficients : Fin 3 → Fin 4 → ℝ := ![![(18276601293484865156552081/5829637162500000000:ℝ), (1752238736135677814170858037/242901548437500000000:ℝ), (6173877990635894979545754973/1214507742187500000000:ℝ), (3659324761108847425099704239/3643523226562500000000:ℝ)], ![(12078095247023265416448797513/1821761613281250000000:ℝ), (1034409435695429660895265557/67472652343750000000:ℝ), (735352146749770183890268103/67472652343750000000:ℝ), (200095112918632542748627669/91088080664062500000:ℝ)], ![(13708167953033119206365371997/3643523226562500000000:ℝ), (10824210665834780323970996207/1214507742187500000000:ℝ), (2004939489724670990922055931/303626935546875000000:ℝ), (10586240648786789797807203721/7287046453125000000000:ℝ)]]
theorem edge131_3_013_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (3659324761108847425099704239/55640224356630528000000000000000:ℝ) edge131_3_013_coefficients (57/128:ℝ) (117/256:ℝ) (31/64:ℝ) (63/128:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_013_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_013_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (57/128:ℝ) (117/256:ℝ))
 (hp : p ∈ Set.Icc (31/64:ℝ) (63/128:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_013_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_013_coefficients]
def edge131_3_014_coefficients : Fin 3 → Fin 4 → ℝ := ![![(3052052765160741613082696101/14574092906250000000000:ℝ), (2310661818324460115583040013/4858030968750000000000:ℝ), (1608058067533468422244237289/4858030968750000000000:ℝ), (942637535596055509246547179/14574092906250000000000:ℝ)], ![(3383619204322780172120363221/7287046453125000000000:ℝ), (2583723163534318720048828981/2429015484375000000000:ℝ), (1825227026189648003845497541/2429015484375000000000:ℝ), (1106442395244861682647483901/7287046453125000000000:ℝ)], ![(4229562415374672007729484821/14574092906250000000000:ℝ), (373556867134980725786401069/539781218750000000000:ℝ), (846213793990778577068497607/1619343656250000000000:ℝ), (1757673888600982404204834421/14574092906250000000000:ℝ)]]
theorem edge131_3_014_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (942637535596055509246547179/6955028044578816000000000000000:ℝ) edge131_3_014_coefficients (57/128:ℝ) (15/32:ℝ) (15/32:ℝ) (31/64:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_014_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_014_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (57/128:ℝ) (15/32:ℝ))
 (hp : p ∈ Set.Icc (15/32:ℝ) (31/64:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_014_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_014_coefficients]
def edge131_3_015_coefficients : Fin 3 → Fin 4 → ℝ := ![![(2235023171214409032076037368742713/4370707294312500000000:ℝ), (279165370562421541588682156898283/273169205894531250000:ℝ), (43601851662011352440263002495232/85365376842041015625:ℝ), (15431241872301100742782124032/85365376842041015625:ℝ)], ![(875086249110959571206102930344189/853653768420410156250:ℝ), (34995197308917477617276629972856/17073075368408203125:ℝ), (437950211401687997047622084952064/426826884210205078125:ℝ), (613018596279277305479974813696/426826884210205078125:ℝ)], ![(1098613054819394207746939827183056/2134134421051025390625:ℝ), (2200068398887802483454126100027136/2134134421051025390625:ℝ), (1106349133690815105769389077856256/2134134421051025390625:ℝ), (4892827236091803447910960562176/2134134421051025390625:ℝ)]]
theorem edge131_3_015_identity (δ p : ℝ) : rowMargin .newTop .C131 δ p =
 Record12518109.Bernstein.bsum 2 3 (470924129403720115441349/166862621239651860480000000000000:ℝ) edge131_3_015_coefficients (3645/8192:ℝ) (57/128:ℝ) (1023/2048:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_015_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_015_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3645/8192:ℝ) (57/128:ℝ))
 (hp : p ∈ Set.Icc (1023/2048:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C131 δ p := by
 rw [edge131_3_015_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_015_coefficients]
def edge131_3_016_coefficients : Fin 3 → Fin 4 → ℝ := ![![(6606395252737702912069785495949999/809390239687500000000:ℝ), (55719871074988740492816729832796939/3414615073681640625000:ℝ), (17408567836718959117348272008848384/2134134421051025390625:ℝ), (2850807601602006428462114668544/2134134421051025390625:ℝ)], ![(743720592090777200064257140885154821/45528200982421875000000:ℝ), (139396164198624443747306199739948157/4268268842102050781250:ℝ), (34843168892910306977421719772409856/2134134421051025390625:ℝ), (6981864583658205675806281695232/2134134421051025390625:ℝ)], ![(372488958669619627598638291954782103/45528200982421875000000:ℝ), (69852635255535969216681591664651711/4268268842102050781250:ℝ), (17487740712740018919493830300602368/2134134421051025390625:ℝ), (21839179394079754759989283782656/2134134421051025390625:ℝ)]]
theorem edge131_3_016_identity (δ p : ℝ) : rowMargin .newTop .C131 δ p =
 Record12518109.Bernstein.bsum 2 3 (10874967962654138292168101/16686262123965186048000000000000000:ℝ) edge131_3_016_coefficients (7287/16384:ℝ) (3645/8192:ℝ) (2047/4096:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_016_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_016_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (7287/16384:ℝ) (3645/8192:ℝ))
 (hp : p ∈ Set.Icc (2047/4096:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C131 δ p := by
 rw [edge131_3_016_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_016_coefficients]
def edge131_3_017_coefficients : Fin 3 → Fin 4 → ℝ := ![![(10319264843076226066134994010716639/1264672249511718750000:ℝ), (34830791303650732737690582213638654/2134134421051025390625:ℝ), (697465378433223283146305613217792/85365376842041015625:ℝ), (19598742978284917326945692155904/2134134421051025390625:ℝ)], ![(74273199576859746654151267092874849/4552820098242187500000:ℝ), (13920703192446062129523409558111097/426826884210205078125:ℝ), (34793022828036210781199691341520896/2134134421051025390625:ℝ), (5061490512976916447483203158016/2134134421051025390625:ℝ)], ![(1486466243852766177995837887039056847/182112803929687500000000:ℝ), (278607036871226427620996941478133559/17073075368408203125000:ℝ), (17409528023754299761962433548116992/2134134421051025390625:ℝ), (634173989343110926636525551616/426826884210205078125:ℝ)]]
theorem edge131_3_017_identity (δ p : ℝ) : rowMargin .newTop .C131 δ p =
 Record12518109.Bernstein.bsum 2 3 (2413506752479990218869783/4171565530991296512000000000000000:ℝ) edge131_3_017_coefficients (1821/4096:ℝ) (7287/16384:ℝ) (2047/4096:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_017_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_017_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (1821/4096:ℝ) (7287/16384:ℝ))
 (hp : p ∈ Set.Icc (2047/4096:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C131 δ p := by
 rw [edge131_3_017_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_017_coefficients]
def edge131_3_018_coefficients : Fin 3 → Fin 4 → ℝ := ![![(21964444631145684088631103797300657/7287046453125000000000:ℝ), (5666527744606383312257613500594923/809671828125000000000:ℝ), (4013123942433661609746574302461123/809671828125000000000:ℝ), (7083807137442754922624463702962957/7287046453125000000000:ℝ)], ![(4395089302232804376944388725435533/728704645312500000000:ℝ), (3400851419621968705089516390100853/242901548437500000000:ℝ), (2407544535228556479882828377178857/242901548437500000000:ℝ), (283033598736696501723189349754759/145740929062500000000:ℝ)], ![(176376293857943213431876930619581/58296371625000000000:ℝ), (682780075256529770930822785243157/97160619375000000000:ℝ), (483865081081281289378009673970503/97160619375000000000:ℝ), (8910511111943282379736711766299/9108808066406250000:ℝ)]]
theorem edge131_3_018_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (283033598736696501723189349754759/149358089971144224072007680000000000000:ℝ) edge131_3_018_coefficients (1821/4096:ℝ) (3645/8192:ℝ) (1023/2048:ℝ) (2047/4096:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_018_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_018_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (1821/4096:ℝ) (3645/8192:ℝ))
 (hp : p ∈ Set.Icc (1023/2048:ℝ) (2047/4096:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_018_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_018_coefficients]
def edge131_3_019_coefficients : Fin 3 → Fin 4 → ℝ := ![![(22182568383314326253082522723061/116592743250000000000:ℝ), (47775260906001612639707020495981/107956243750000000000:ℝ), (509372189467387846241082195033679/1619343656250000000000:ℝ), (907508893736346769740963673161551/14574092906250000000000:ℝ)], ![(2778949797827430565217010349754033/7287046453125000000000:ℝ), (2154428483775560991464108047106993/2429015484375000000000:ℝ), (1531073807336366815088626159125041/2429015484375000000000:ℝ), (908884128738638994252318651896177/7287046453125000000000:ℝ)], ![(560050356265928218240730142284221/2914818581250000000000:ℝ), (434826947835319939488993283914173/971606193750000000000:ℝ), (1549186842559623010508757270016177/4858030968750000000000:ℝ), (925406449006066718306631848229041/14574092906250000000000:ℝ)]]
theorem edge131_3_019_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (907508893736346769740963673161551/233372015579912850112512000000000000000:ℝ) edge131_3_019_coefficients (1821/4096:ℝ) (57/128:ℝ) (511/1024:ℝ) (1023/2048:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_019_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_019_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (1821/4096:ℝ) (57/128:ℝ))
 (hp : p ∈ Set.Icc (511/1024:ℝ) (1023/2048:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_019_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_019_coefficients]
def edge131_3_020_coefficients : Fin 3 → Fin 4 → ℝ := ![![(1455185415424799499272195913098623/45528200982421875000000:ℝ), (1092720888413698438478909254060447/17073075368408203125000:ℝ), (68799372279051302872593324318976/2134134421051025390625:ℝ), (420838559066538328909470937088/2134134421051025390625:ℝ)], ![(107521876026512702038256021927933/1686229666015625000000:ℝ), (434895818014193631289025505836227/3414615073681640625000:ℝ), (135882945294824265334458225099008/2134134421051025390625:ℝ), (30990912111161142261000003584/426826884210205078125:ℝ)], ![(5815313417301967297310610255438047/182112803929687500000000:ℝ), (4353656183197148499826208594996479/68292301473632812500000:ℝ), (13582919367174818236334617960256/426826884210205078125:ℝ), (10805414177135437280609030144/2134134421051025390625:ℝ)]]
theorem edge131_3_020_identity (δ p : ℝ) : rowMargin .newTop .C131 δ p =
 Record12518109.Bernstein.bsum 2 3 (2638040570589706367336189/1042891382747824128000000000000000:ℝ) edge131_3_020_coefficients (909/2048:ℝ) (1821/4096:ℝ) (511/1024:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_020_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_020_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (909/2048:ℝ) (1821/4096:ℝ))
 (hp : p ∈ Set.Icc (511/1024:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C131 δ p := by
 rw [edge131_3_020_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_020_coefficients]
def edge131_3_021_coefficients : Fin 3 → Fin 4 → ℝ := ![![(2726173863418879812894836392063/227720201660156250000:ℝ), (3386234309558428528520713873909/121450774218750000000:ℝ), (24142229300214978300111820496131/1214507742187500000000:ℝ), (28916676896603833158315117444887/7287046453125000000000:ℝ)], ![(10906473676883971005589027699357/455440403320312500000:ℝ), (939439500128194177778561378589/16868163085937500000:ℝ), (2004185889278762312486918917651/50604489257812500000:ℝ), (3579254597716373836886068028563/455440403320312500000:ℝ)], ![(11027202070639421479663840485997/910880806640625000000:ℝ), (8563138812093025114811690020589/303626935546875000000:ℝ), (1221647033336440329678248491273/60725387109375000000:ℝ), (146498618830875348160855277653/36435232265625000000:ℝ)]]
theorem edge131_3_021_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (3579254597716373836886068028563/455804717929517285376000000000000000:ℝ) edge131_3_021_coefficients (909/2048:ℝ) (57/128:ℝ) (255/512:ℝ) (511/1024:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_021_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_021_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (909/2048:ℝ) (57/128:ℝ))
 (hp : p ∈ Set.Icc (255/512:ℝ) (511/1024:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_021_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_021_coefficients]
def edge131_3_022_coefficients : Fin 3 → Fin 4 → ℝ := ![![(274817189927168774475094233423473/136584602947265625000000:ℝ), (5530052583216926248533427475591/1365846029472656250000:ℝ), (4430998702492913608896548086336/2134134421051025390625:ℝ), (84250773516495343614476359168/2134134421051025390625:ℝ)], ![(545202301579862099573934862738201/136584602947265625000000:ℝ), (272488735048342329851340070588039/34146150736816406250000:ℝ), (8568288126087109650183122779712/2134134421051025390625:ℝ), (56409034012444239350561364992/2134134421051025390625:ℝ)], ![(1090455808032335671664652697033217/546338411789062500000000:ℝ), (108724168420203807359346579882067/27316920589453125000000:ℝ), (4241286848861527700656716967696/2134134421051025390625:ℝ), (6744437081932402596719999488/2134134421051025390625:ℝ)]]
theorem edge131_3_022_identity (δ p : ℝ) : rowMargin .newTop .C131 δ p =
 Record12518109.Bernstein.bsum 2 3 (13172728675649223821718749/260722845686956032000000000000000:ℝ) edge131_3_022_coefficients (453/1024:ℝ) (909/2048:ℝ) (255/512:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_022_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_022_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (453/1024:ℝ) (909/2048:ℝ))
 (hp : p ∈ Set.Icc (255/512:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C131 δ p := by
 rw [edge131_3_022_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_022_coefficients]
def edge131_3_023_coefficients : Fin 3 → Fin 4 → ℝ := ![![(1375728756680434802359653871459/1821761613281250000000:ℝ), (89117570848983050104503377131/50604489257812500000:ℝ), (170079199785918472827500335857/134945304687500000000:ℝ), (14833687670199082232622077039/58296371625000000000:ℝ)], ![(1370344707284317799982690948853/910880806640625000000:ℝ), (1060919787427403707500372965149/303626935546875000000:ℝ), (753777882890659254801483856753/303626935546875000000:ℝ), (89781249255280589802501768383/182176161328125000000:ℝ)], ![(1394903559119946257105751966661/1821761613281250000000:ℝ), (1082303013416326574092823781893/607253871093750000000:ℝ), (772005202814133803878379248421/607253871093750000000:ℝ), (92799459099166851654372088049/364352322656250000000:ℝ)]]
theorem edge131_3_023_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (89781249255280589802501768383/5697558974118966067200000000000000:ℝ) edge131_3_023_coefficients (453/1024:ℝ) (57/128:ℝ) (127/256:ℝ) (255/512:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_023_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_023_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (453/1024:ℝ) (57/128:ℝ))
 (hp : p ∈ Set.Icc (127/256:ℝ) (255/512:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_023_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_023_coefficients]
def edge131_3_024_coefficients : Fin 3 → Fin 4 → ℝ := ![![(46461303576608920645057821883/364352322656250000000:ℝ), (1965792435267694673109521263/7590673388671875000:ℝ), (130207061489234650711354736/948834173583984375:ℝ), (16408429872544447423310336/2846502520751953125:ℝ)], ![(18231251924364943639253260123/72870464531250000000:ℝ), (1267399381437260150486988121/2530224462890625000:ℝ), (241897344286782963468191536/948834173583984375:ℝ), (2397339114809471949771776/569300504150390625:ℝ)], ![(908870571520188680774181544847/7287046453125000000000:ℝ), (7531908312844380995857102487/30362693554687500000:ℝ), (587425135191136198659381868/4744170867919921875:ℝ), (1346457014933669887460864/2846502520751953125:ℝ)]]
theorem edge131_3_024_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (2629798857292323998947/10867231319654400000000000000:ℝ) edge131_3_024_coefficients (225/512:ℝ) (453/1024:ℝ) (127/256:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_024_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_024_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (225/512:ℝ) (453/1024:ℝ))
 (hp : p ∈ Set.Icc (127/256:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_024_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_024_coefficients]
def edge131_3_025_coefficients : Fin 3 → Fin 4 → ℝ := ![![(34947860233934183248382231369/728704645312500000000:ℝ), (27219848773136557444734294419/242901548437500000000:ℝ), (306317370431895176699660621/3795336694335937500:ℝ), (24199998802956776742251077813/1457409290625000000000:ℝ)], ![(34526283315167249241482229677/364352322656250000000:ℝ), (8880818371079290086734987143/40483591406250000000:ℝ), (2097006442893004374777062433/13494530468750000000:ℝ), (11216825635781826824200867331/364352322656250000000:ℝ)], ![(178112656532057101085376734641/3643523226562500000000:ℝ), (137879804859624340214239922897/1214507742187500000000:ℝ), (98229052871315151638002986977/1214507742187500000000:ℝ), (59153984658362691261386963881/3643523226562500000000:ℝ)]]
theorem edge131_3_025_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (11216825635781826824200867331/356097435882435379200000000000000:ℝ) edge131_3_025_coefficients (225/512:ℝ) (57/128:ℝ) (63/128:ℝ) (127/256:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_025_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_025_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (225/512:ℝ) (57/128:ℝ))
 (hp : p ∈ Set.Icc (63/128:ℝ) (127/256:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_025_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_025_coefficients]
def edge131_3_026_coefficients : Fin 3 → Fin 4 → ℝ := ![![(14986721324019276035916107071/1821761613281250000000:ℝ), (1293394589724320483887166731/75906733886718750000:ℝ), (45651044027107833188545292/4744170867919921875:ℝ), (2300329282485786221829952/2846502520751953125:ℝ)], ![(5752263301010455540692302749/364352322656250000000:ℝ), (160800609212249474341152139/5060448925781250000:ℝ), (3158476248618132575534356/189766834716796875:ℝ), (1856725475923787109571712/2846502520751953125:ℝ)], ![(455965294893167103186384203/58296371625000000000:ℝ), (37675633209651823389178183/2429015484375000000:ℝ), (295593383346399331539343/37953366943359375:ℝ), (11096804304673823319232/113860100830078125:ℝ)]]
theorem edge131_3_026_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (173387567260528489363/108672313196544000000000000:ℝ) edge131_3_026_coefficients (111/256:ℝ) (225/512:ℝ) (63/128:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_026_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_026_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (111/256:ℝ) (225/512:ℝ))
 (hp : p ∈ Set.Icc (63/128:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_026_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_026_coefficients]
def edge131_3_027_coefficients : Fin 3 → Fin 4 → ℝ := ![![(22517157894568244293773618031/7287046453125000000000:ℝ), (1955896544921060117798893659/269890609375000000000:ℝ), (4275920924721625984505344319/809671828125000000000:ℝ), (4094099083970082894348629867/3643523226562500000000:ℝ)], ![(4375578047385887097671091323/728704645312500000000:ℝ), (3353596475491925163435045971/242901548437500000000:ℝ), (11801750818311520038031043179/1214507742187500000000:ℝ), (6976072024953891420326559337/3643523226562500000000:ℝ)], ![(23188329114119884875562950391/7287046453125000000000:ℝ), (17864964858620581571581429511/2429015484375000000000:ℝ), (12690333478535593388964359087/2429015484375000000000:ℝ), (7661227019481498280072257619/7287046453125000000000:ℝ)]]
theorem edge131_3_027_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (6976072024953891420326559337/111280448713261056000000000000000:ℝ) edge131_3_027_coefficients (111/256:ℝ) (57/128:ℝ) (31/64:ℝ) (63/128:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_027_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_027_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (111/256:ℝ) (57/128:ℝ))
 (hp : p ∈ Set.Icc (31/64:ℝ) (63/128:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_027_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_027_coefficients]
def edge131_3_028_coefficients : Fin 3 → Fin 4 → ℝ := ![![(249192124724970072968927459/455440403320312500000:ℝ), (44563309389309402798501731/37953366943359375000:ℝ), (3479705397663891447528628/4744170867919921875:ℝ), (60380228311639158447112/569300504150390625:ℝ)], ![(915863055385253198186840567/910880806640625000000:ℝ), (17249199244924399956601607/8434081542968750000:ℝ), (5356491683556260061115022/4744170867919921875:ℝ), (252050486506193827280848/2846502520751953125:ℝ)], ![(3583543764336161692070092091/7287046453125000000000:ℝ), (588755379191621470918549579/607253871093750000000:ℝ), (9342896088076797958852243/18976683471679687500:ℝ), (40277334220353621950168/2846502520751953125:ℝ)]]
theorem edge131_3_028_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (5034666777544202743771/679201957478400000000000000:ℝ) edge131_3_028_coefficients (27/64:ℝ) (111/256:ℝ) (31/64:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_028_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_028_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (27/64:ℝ) (111/256:ℝ))
 (hp : p ∈ Set.Icc (31/64:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_028_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_028_coefficients]
def edge131_3_029_coefficients : Fin 3 → Fin 4 → ℝ := ![![(1492599544275460429139642351/7287046453125000000000:ℝ), (235166885319979520091492211/485803096875000000000:ℝ), (875933988586010245750460087/2429015484375000000000:ℝ), (592178439915080398650777947/7287046453125000000000:ℝ)], ![(1401194377911553070372748671/3643523226562500000000:ℝ), (353250483823167432969619901/404835914062500000000:ℝ), (245465256450281987890574233/404835914062500000000:ℝ), (430367552885826211273039409/3643523226562500000000:ℝ)], ![(1566977597492572349891582231/7287046453125000000000:ℝ), (1196282124074431601141754187/2429015484375000000000:ℝ), (33799209947157430178894113/97160619375000000000:ℝ), (51226998271022929797350777/728704645312500000000:ℝ)]]
theorem edge131_3_029_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (430367552885826211273039409/3477514022289408000000000000000:ℝ) edge131_3_029_coefficients (27/64:ℝ) (57/128:ℝ) (15/32:ℝ) (31/64:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_029_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_029_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (27/64:ℝ) (57/128:ℝ))
 (hp : p ∈ Set.Icc (15/32:ℝ) (31/64:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_029_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_029_coefficients]
def edge131_3_030_coefficients : Fin 3 → Fin 4 → ℝ := ![![(98800434358993033428480571/7287046453125000000000:ℝ), (74606497009171996550083783/2429015484375000000000:ℝ), (52700592196739885510549911/2429015484375000000000:ℝ), (1645138617100860435895679/364352322656250000000:ℝ)], ![(20655741484098193449517439/728704645312500000000:ℝ), (15073753493695902577094551/242901548437500000000:ℝ), (10014499078961333687066503/242901548437500000000:ℝ), (1087597977770919951799309/145740929062500000000:ℝ)], ![(5738579500546451345394931/291481858125000000000:ℝ), (294956932785252341492653/6477374625000000000:ℝ), (215297683702372772725037/6477374625000000000:ℝ), (2145026991585784746310711/291481858125000000000:ℝ)]]
theorem edge131_3_030_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (1087597977770919951799309/4346892527861760000000000000:ℝ) edge131_3_030_coefficients (27/64:ℝ) (15/32:ℝ) (7/16:ℝ) (15/32:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_030_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_030_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (27/64:ℝ) (15/32:ℝ))
 (hp : p ∈ Set.Icc (7/16:ℝ) (15/32:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_030_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_030_coefficients]
def edge131_3_031_coefficients : Fin 3 → Fin 4 → ℝ := ![![(10857699629598759834125317/291481858125000000000:ℝ), (101696288258364756073979293/1214507742187500000000:ℝ), (4456914353092833582173963/75906733886718750000:ℝ), (34565040583983015417904/2846502520751953125:ℝ)], ![(22781750565320440077449281/364352322656250000000:ℝ), (12895140916974118835410367/101208978515625000000:ℝ), (1398655118207434902724771/18976683471679687500:ℝ), (24573760445535581777696/2846502520751953125:ℝ)], ![(2164063715857617939135061/72870464531250000000:ℝ), (17145142835472890396957597/303626935546875000000:ℝ), (518556471517079462570747/18976683471679687500:ℝ), (1300327452442567049152/2846502520751953125:ℝ)]]
theorem edge131_3_031_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (20317616444415110143/2653132646400000000000000:ℝ) edge131_3_031_coefficients (51/128:ℝ) (27/64:ℝ) (15/32:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_031_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_031_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (51/128:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (15/32:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_031_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_031_coefficients]
def edge131_3_032_coefficients : Fin 3 → Fin 3 → ℝ := ![![(1260800375798961417995689/567379687500000000000:ℝ), (307444389059012021008729/94563281250000000000:ℝ), (631126124244819986597387/567379687500000000000:ℝ)], ![(8389574805882144221133557/2269518750000000000000:ℝ), (9022862956400373383617/1891265625000000000:ℝ), (14187392740393944314147/11347593750000000000:ℝ)], ![(124831743708468087017133227/72624600000000000000000:ℝ), (188609573969415945118417/94563281250000000000:ℝ), (209205629464194210061301/567379687500000000000:ℝ)]]
theorem edge131_3_032_identity (δ p : ℝ) : rowMargin .newTop .capC δ p =
 Record12518109.Bernstein.bsum 2 2 (209205629464194210061301/1057672396800000000000000000:ℝ) edge131_3_032_coefficients (3/8:ℝ) (51/128:ℝ) (15/32:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_032_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_032_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3/8:ℝ) (51/128:ℝ))
 (hp : p ∈ Set.Icc (15/32:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .capC δ p := by
 rw [edge131_3_032_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_032_coefficients]
def edge131_3_033_coefficients : Fin 3 → Fin 4 → ℝ := ![![(195765646482035469111644267/3643523226562500000000:ℝ), (51380358256362366386070947/404835914062500000000:ℝ), (12941868794969670468026043/134945304687500000000:ℝ), (32980744817242916943858887/1457409290625000000000:ℝ)], ![(182365069274488570366936163/1821761613281250000000:ℝ), (137639209754790660819410239/607253871093750000000:ℝ), (97177276824482482195111363/607253871093750000000:ℝ), (1515984237493124870508179/45544040332031250000:ℝ)], ![(186850512836903258837392787/3643523226562500000000:ℝ), (138408688654173221513299211/1214507742187500000000:ℝ), (94556416916993026758756467/1214507742187500000000:ℝ), (10986760493200738277966761/728704645312500000000:ℝ)]]
theorem edge131_3_033_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (10986760493200738277966761/43468925278617600000000000000:ℝ) edge131_3_033_coefficients (51/128:ℝ) (27/64:ℝ) (7/16:ℝ) (15/32:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_033_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_033_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (51/128:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (7/16:ℝ) (15/32:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_033_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_033_coefficients]
def edge131_3_034_coefficients : Fin 3 → Fin 3 → ℝ := ![![(410105286298474251928414421/145249200000000000000000:ℝ), (311359078474695785749802197/72624600000000000000000:ℝ), (1664529430129502925019331/1075920000000000000000:ℝ)], ![(373655590502835799924563797/72624600000000000000000:ℝ), (265640395676518833057814549/36312300000000000000000:ℝ), (151478196134379899508433/64555200000000000000:ℝ)], ![(374748556439481402379695149/145249200000000000000000:ℝ), (256421398888309674088301953/72624600000000000000000:ℝ), (3369112539552998797888439/3227760000000000000000:ℝ)]]
theorem edge131_3_034_identity (δ p : ℝ) : rowMargin .newTop .capC δ p =
 Record12518109.Bernstein.bsum 2 2 (3369112539552998797888439/6016980746240000000000000000:ℝ) edge131_3_034_coefficients (3/8:ℝ) (51/128:ℝ) (7/16:ℝ) (15/32:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_034_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_034_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3/8:ℝ) (51/128:ℝ))
 (hp : p ∈ Set.Icc (7/16:ℝ) (15/32:ℝ)) : 0 < rowMargin .newTop .capC δ p := by
 rw [edge131_3_034_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_034_coefficients]
def edge131_3_035_coefficients : Fin 3 → Fin 4 → ℝ := ![![(7407962096458196255755949/1821761613281250000000:ℝ), (5278845982827277093149077/607253871093750000000:ℝ), (13922883325159386233565653/2429015484375000000000:ℝ), (984299873463015876745807/910880806640625000000:ℝ)], ![(1046471301784603421346427/113860100830078125000:ℝ), (185124898715362506862493/9488341735839843750:ℝ), (7705834054197116165941697/607253871093750000000:ℝ), (263568222512230273167337/113860100830078125000:ℝ)], ![(5349552549609534501944743/910880806640625000000:ℝ), (1307372256174558113373581/101208978515625000000:ℝ), (1805942921819631015295637/202417957031250000000:ℝ), (1682175704004707286220693/910880806640625000000:ℝ)]]
theorem edge131_3_035_identity (δ p : ℝ) : rowMargin .newTop .C δ p =
 Record12518109.Bernstein.bsum 2 3 (984299873463015876745807/1698004893696000000000000000:ℝ) edge131_3_035_coefficients (27/64:ℝ) (15/32:ℝ) (3/8:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_035_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_035_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (27/64:ℝ) (15/32:ℝ))
 (hp : p ∈ Set.Icc (3/8:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .C δ p := by
 rw [edge131_3_035_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_035_coefficients]
def edge131_3_036_coefficients : Fin 3 → Fin 3 → ℝ := ![![(1792352630262417611602951/116199360000000000000:ℝ), (14800922757927098209003/968328000000000000:ℝ), (22571835701760060083507/72624600000000000000:ℝ)], ![(62095381075674531702663779/1815615000000000000000:ℝ), (5452484735615262249273989/151301250000000000000:ℝ), (2504027173423762892586509/907807500000000000000:ℝ)], ![(180514728907245765992353127/9078075000000000000000:ℝ), (34709957277882539753785339/1513012500000000000000:ℝ), (32024743299179649231842809/9078075000000000000000:ℝ)]]
theorem edge131_3_036_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (22571835701760060083507/2166113068646400000000000000:ℝ) edge131_3_036_coefficients (105/256:ℝ) (27/64:ℝ) (27/64:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_036_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_036_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (105/256:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (27/64:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_036_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_036_coefficients]
def edge131_3_037_coefficients : Fin 3 → Fin 4 → ℝ := ![![(2304088904021968854838143388727/7287046453125000000000:ℝ), (34585479629116734188801082851/37953366943359375000:ℝ), (8296547346616133199281705369/9488341735839843750:ℝ), (3975419141628703393593319696/14232512603759765625:ℝ)], ![(227257454227272730649121986573/364352322656250000000:ℝ), (1135546914893946071605540531/632556115722656250:ℝ), (544012807227791302767097346/316278057861328125:ℝ), (1561594626203300551226393728/2846502520751953125:ℝ)], ![(22596125606638512120012622367/72870464531250000000:ℝ), (338359758081058855271365147/379533669433593750:ℝ), (32382753166902374106732442/37953366943359375:ℝ), (154733041237108901478759136/569300504150390625:ℝ)]]
theorem edge131_3_037_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (4835407538659653171211223/8693785055723520000000000000:ℝ) edge131_3_037_coefficients (207/512:ℝ) (105/256:ℝ) (111/256:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_037_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_037_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (207/512:ℝ) (105/256:ℝ))
 (hp : p ∈ Set.Icc (111/256:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_037_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_037_coefficients]
def edge131_3_038_coefficients : Fin 3 → Fin 3 → ℝ := ![![(393075384231302373829441493/1161993600000000000000:ℝ), (32269312223650609734679276229/72624600000000000000000:ℝ), (348000511601410303969169779/3227760000000000000000:ℝ)], ![(10591176035577344672652805829/14524920000000000000000:ℝ), (7149257411481004315604490781/7262460000000000000000:ℝ), (417677349390379363843966241/1613880000000000000000:ℝ)], ![(11864147582898306773682939989/29049840000000000000000:ℝ), (8351672196619103742744260389/14524920000000000000000:ℝ), (181168653584217875350436407/1075920000000000000000:ℝ)]]
theorem edge131_3_038_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (348000511601410303969169779/6161388284149760000000000000000:ℝ) edge131_3_038_coefficients (207/512:ℝ) (105/256:ℝ) (55/128:ℝ) (111/256:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_038_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_038_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (207/512:ℝ) (105/256:ℝ))
 (hp : p ∈ Set.Icc (55/128:ℝ) (111/256:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_038_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_038_coefficients]
def edge131_3_039_coefficients : Fin 3 → Fin 4 → ℝ := ![![(147390885707585394130820309807/455440403320312500000:ℝ), (19713273385830761257321454/21085203857421875:ℝ), (284467204460722243371991664/316278057861328125:ℝ), (4100509780059040170766149256/14232512603759765625:ℝ)], ![(577046857357939825972308884987/910880806640625000000:ℝ), (8669044842152790700734646147/4744170867919921875:ℝ), (8325809474114416000432609252/4744170867919921875:ℝ), (7986610324797329961616968848/14232512603759765625:ℝ)], ![(2276673067682517755542312016951/7287046453125000000000:ℝ), (34157107186312810762303717667/37953366943359375000:ℝ), (8189454235915152342657364073/9488341735839843750:ℝ), (3921872586278212965281149048/14232512603759765625:ℝ)]]
theorem edge131_3_039_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (490234073284776620660143631/869378505572352000000000000000:ℝ) edge131_3_039_coefficients (51/128:ℝ) (207/512:ℝ) (111/256:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_039_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_039_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (51/128:ℝ) (207/512:ℝ))
 (hp : p ∈ Set.Icc (111/256:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_039_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_039_coefficients]
def edge131_3_040_coefficients : Fin 3 → Fin 3 → ℝ := ![![(22953476056850033985981437/72624600000000000000:ℝ), (1857656527698881998889508461/4539037500000000000000:ℝ), (2127774726382596147643379/22415000000000000000:ℝ)], ![(589812608438038884199748603/907807500000000000000:ℝ), (479130940390631852081556917/567379687500000000000:ℝ), (7998115620368942570072413/40347000000000000000:ℝ)], ![(1275161645600425934264093269/3631230000000000000000:ℝ), (8535338754688712594140705091/18156150000000000000000:ℝ), (194800731301863381338846491/1613880000000000000000:ℝ)]]
theorem edge131_3_040_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (19149972537443365328790411/385086767759360000000000000000:ℝ) edge131_3_040_coefficients (51/128:ℝ) (207/512:ℝ) (55/128:ℝ) (111/256:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_040_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_040_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (51/128:ℝ) (207/512:ℝ))
 (hp : p ∈ Set.Icc (55/128:ℝ) (111/256:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_040_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_040_coefficients]
def edge131_3_041_coefficients : Fin 3 → Fin 3 → ℝ := ![![(1493514854212214650627808377/36312300000000000000000:ℝ), (108014516512787426187165733/2017350000000000000000:ℝ), (93273331782280142201081203/7262460000000000000000:ℝ)], ![(63033733804847286802497373/726246000000000000000:ℝ), (4591472077232674157219411/40347000000000000000:ℝ), (50630592645337079738093771/1815615000000000000000:ℝ)], ![(363843560064028284733059347/7262460000000000000000:ℝ), (2322281499682215924539009/33622500000000000000:ℝ), (282083092288908450266758469/14524920000000000000000:ℝ)]]
theorem edge131_3_041_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (93273331782280142201081203/866445227458560000000000000000:ℝ) edge131_3_041_coefficients (51/128:ℝ) (105/256:ℝ) (27/64:ℝ) (55/128:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_041_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_041_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (51/128:ℝ) (105/256:ℝ))
 (hp : p ∈ Set.Icc (27/64:ℝ) (55/128:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_041_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_041_coefficients]
def edge131_3_042_coefficients : Fin 3 → Fin 3 → ℝ := ![![(781989610631021425411699777/145249200000000000000000:ℝ), (505677291939015827675810189/72624600000000000000000:ℝ), (81661729713483973401383933/48416400000000000000000:ℝ)], ![(173328588446345267495864933/14524920000000000000000:ℝ), (568219459540202257137873233/36312300000000000000000:ℝ), (95383144864978559973821591/24208200000000000000000:ℝ)], ![(1116557415084717054460926697/145249200000000000000000:ℝ), (793899072633803760731002649/72624600000000000000000:ℝ), (162786548113137057935671403/48416400000000000000000:ℝ)]]
theorem edge131_3_042_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (81661729713483973401383933/361018844774400000000000000000:ℝ) edge131_3_042_coefficients (51/128:ℝ) (27/64:ℝ) (13/32:ℝ) (27/64:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_042_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_042_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (51/128:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (13/32:ℝ) (27/64:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_042_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_042_coefficients]
def edge131_3_043_coefficients : Fin 3 → Fin 4 → ℝ := ![![(8730894905362734646936937411898191/7287046453125000000000:ℝ), (33763632138520709609732389100627/9488341735839843750:ℝ), (16711608800166607471850953621768/4744170867919921875:ℝ), (16541906025401473700305056799744/14232512603759765625:ℝ)], ![(271944609487322439227586133420513/113860100830078125000:ℝ), (33650856236626815563485808509984/4744170867919921875:ℝ), (33309650262795558204288804691456/4744170867919921875:ℝ), (32969455701001613039766382641152/14232512603759765625:ℝ)], ![(16942843868919645293663150477278/14232512603759765625:ℝ), (223617793309223823630991081984/63255611572265625:ℝ), (1844481481332770105106013560832/527130096435546875:ℝ), (16429839086258694422624866926592/14232512603759765625:ℝ)]]
theorem edge131_3_043_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (31337431118504895062684759/54336156598272000000000000000:ℝ) edge131_3_043_coefficients (1629/4096:ℝ) (51/128:ℝ) (447/1024:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_043_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_043_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (1629/4096:ℝ) (51/128:ℝ))
 (hp : p ∈ Set.Icc (447/1024:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_043_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_043_coefficients]
def edge131_3_044_coefficients : Fin 3 → Fin 4 → ℝ := ![![(275217842675390705371351929364793863/7287046453125000000000:ℝ), (534817849201189729739569897850699/4744170867919921875:ℝ), (532104880801614900300387045109024/4744170867919921875:ℝ), (529395938668652480405686803636224/14232512603759765625:ℝ)], ![(137372450832088371747100087372325069/1821761613281250000000:ℝ), (1067781960774433925839870528169188/4744170867919921875:ℝ), (354116573954773863141760308543616/1581390289306640625:ℝ), (1056925545169946729707257254576128/14232512603759765625:ℝ)], ![(68570338298443691277841637225469007/1821761613281250000000:ℝ), (532982446533675879148102230778316/4744170867919921875:ℝ), (106052633236560966062322625754752/948834173583984375:ℝ), (527547921786562689966878779621376/14232512603759765625:ℝ)]]
theorem edge131_3_044_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (32198969835605632932548753639/55640224356630528000000000000000:ℝ) edge131_3_044_coefficients (3255/8192:ℝ) (1629/4096:ℝ) (895/2048:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_044_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_044_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3255/8192:ℝ) (1629/4096:ℝ))
 (hp : p ∈ Set.Icc (895/2048:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_044_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_044_coefficients]
def edge131_3_045_coefficients : Fin 3 → Fin 4 → ℝ := ![![(8740395244039883800416386787917050847/7287046453125000000000:ℝ), (17027727323735412999497902598304262/4744170867919921875:ℝ), (16984402378282439309921239641688192/4744170867919921875:ℝ), (16941109604243321948949377604714496/14232512603759765625:ℝ)], ![(174654287161234357503242411873545651/72870464531250000000:ℝ), (6805080169686951925254424739283224/948834173583984375:ℝ), (6787740131614362885357876505928192/948834173583984375:ℝ), (6770412969848923429917592061476864/2846502520751953125:ℝ)], ![(17450217103868230370094068832242131/14574092906250000000:ℝ), (75545867225205064173099190886232/21085203857421875:ℝ), (75353088184048184196783347536384/21085203857421875:ℝ), (676444070691337709038441973284864/569300504150390625:ℝ)]]
theorem edge131_3_045_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (5160858693628980324084792887/8902435897060884480000000000000:ℝ) edge131_3_045_coefficients (6507/16384:ℝ) (3255/8192:ℝ) (1791/4096:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_045_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_045_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (6507/16384:ℝ) (3255/8192:ℝ))
 (hp : p ∈ Set.Icc (1791/4096:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_045_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_045_coefficients]
def edge131_3_046_coefficients : Fin 3 → Fin 4 → ℝ := ![![(55725736240092093908663859175899782819/1457409290625000000000:ℝ), (108700769199808294598338214272185052/948834173583984375:ℝ), (542811306326549295515950064575939072/4744170867919921875:ℝ), (542119023870557842974119282457706496/14232512603759765625:ℝ)], ![(139252438734482603321070743987957838503/1821761613281250000000:ℝ), (1086523681591038567985572326698181296/4744170867919921875:ℝ), (361712733439996317559714793469384704/1581390289306640625:ℝ), (1083753233636728897570106380411469824/14232512603759765625:ℝ)], ![(13919083706723610627373234859977806227/364352322656250000000:ℝ), (21720840323399633639140192941186992/189766834716796875:ℝ), (542328066329054112574116623580956672/4744170867919921875:ℝ), (541635381944428234798566830989377536/14232512603759765625:ℝ)]]
theorem edge131_3_046_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (516543752617290720747534590711/890243589706088448000000000000000:ℝ) edge131_3_046_coefficients (13011/32768:ℝ) (6507/16384:ℝ) (3583/8192:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_046_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_046_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (13011/32768:ℝ) (6507/16384:ℝ))
 (hp : p ∈ Set.Icc (3583/8192:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_046_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_046_coefficients]
def edge131_3_047_coefficients : Fin 3 → Fin 3 → ℝ := ![![(738487002363987155987478592043449/94563281250000000000:ℝ), (4319578220109031131715026020672/277040863037109375:ℝ), (4312087516983624400130589880981/554081726074218750:ℝ)], ![(787705798245761120016746023659593/50433750000000000000:ℝ), (69112008975619725864849610437797/2216326904296875000:ℝ), (862401459231328116493976471921/55408172607421875:ℝ)], ![(189046520707771582767090247599643577/24208200000000000000000:ℝ), (1105774665863014054714691431690667/70922460937500000000:ℝ), (4311936460995089835822789583723/554081726074218750:ℝ)]]
theorem edge131_3_047_identity (δ p : ℝ) : rowMargin .newTop .capC δ p =
 Record12518109.Bernstein.bsum 2 2 (4311936460995089835822789583723/4436199564587827200000000000000000:ℝ) edge131_3_047_coefficients (813/2048:ℝ) (13011/32768:ℝ) (3583/8192:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_047_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_047_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (813/2048:ℝ) (13011/32768:ℝ))
 (hp : p ∈ Set.Icc (3583/8192:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .capC δ p := by
 rw [edge131_3_047_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_047_coefficients]
def edge131_3_048_coefficients : Fin 3 → Fin 4 → ℝ := ![![(139580516654772144171277355243454102749/3643523226562500000000:ℝ), (27880605774553570262516106256720411571/242901548437500000000:ℝ), (8701600436248413335924797604865833813/75906733886718750000:ℝ), (278096501910997991378020056013001501041/7287046453125000000000:ℝ)], ![(27903753849508912765737301124560350277/364352322656250000000:ℝ), (46447076653182004445316935147119183423/202417957031250000000:ℝ), (139163756580581030857338610225299764591/607253871093750000000:ℝ), (17373293636218920529802640506838641497/227720201660156250000:ℝ)], ![(139457322159719236426652376068883605009/3643523226562500000000:ℝ), (27855946265084083533852938161640291077/242901548437500000000:ℝ), (139102206419983318174317842442710669213/1214507742187500000000:ℝ), (138924747422504867191082728666529355743/3643523226562500000000:ℝ)]]
theorem edge131_3_048_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (138924747422504867191082728666529355743/238972943953830758515212288000000000000000:ℝ) edge131_3_048_coefficients (13011/32768:ℝ) (6507/16384:ℝ) (1791/4096:ℝ) (3583/8192:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_048_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_048_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (13011/32768:ℝ) (6507/16384:ℝ))
 (hp : p ∈ Set.Icc (1791/4096:ℝ) (3583/8192:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_048_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_048_coefficients]
def edge131_3_049_coefficients : Fin 3 → Fin 3 → ℝ := ![![(1136280534539678559825380632141481173/145249200000000000000000:ℝ), (8402334311275113724895736200838851/537960000000000000000:ℝ), (1132350609323317938256461050897547989/145249200000000000000000:ℝ)], ![(1136262192005289752528351801422894933/72624600000000000000000:ℝ), (126032901953719122637580718249508013/4034700000000000000000:ℝ), (226466184633225935896761641517724849/14524920000000000000000:ℝ)], ![(1136246310934942914880413124340766253/145249200000000000000000:ℝ), (126031062704640696426325875407032249/8069400000000000000000:ℝ), (1132313697938863163262235419116671787/145249200000000000000000:ℝ)]]
theorem edge131_3_049_identity (δ p : ℝ) : rowMargin .newTop .capC δ p =
 Record12518109.Bernstein.bsum 2 2 (1132313697938863163262235419116671787/1162923098659311373516800000000000000000:ℝ) edge131_3_049_coefficients (813/2048:ℝ) (13011/32768:ℝ) (1791/4096:ℝ) (3583/8192:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_049_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_049_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (813/2048:ℝ) (13011/32768:ℝ))
 (hp : p ∈ Set.Icc (1791/4096:ℝ) (3583/8192:ℝ)) : 0 < rowMargin .newTop .capC δ p := by
 rw [edge131_3_049_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_049_coefficients]
def edge131_3_050_coefficients : Fin 3 → Fin 4 → ℝ := ![![(877372904045726940195445900596992177/728704645312500000000:ℝ), (4375748605643761025348014373924012983/1214507742187500000000:ℝ), (21823204686961849726030897166162291/6072538710937500000:ℝ), (8707083020497387545738898208879647697/7287046453125000000000:ℝ)], ![(35064347375805400575861943607314661/14574092906250000000:ℝ), (874384210837356588192642105812970593/121450774218750000000:ℝ), (290720462512721367710702964734487841/40483591406250000000:ℝ), (43497010672596108102423160073199397/18217616132812500000:ℝ)], ![(175170395755438535078621156558127313/145740929062500000000:ℝ), (174725242512436434680319671225251801/48580309687500000000:ℝ), (174280419519642214453511069262216029/48580309687500000000:ℝ), (173835926567832378607390916741673247/145740929062500000000:ℝ)]]
theorem edge131_3_050_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (173835926567832378607390916741673247/298716179942288448144015360000000000000:ℝ) edge131_3_050_coefficients (6507/16384:ℝ) (3255/8192:ℝ) (895/2048:ℝ) (1791/4096:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_050_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_050_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (6507/16384:ℝ) (3255/8192:ℝ))
 (hp : p ∈ Set.Icc (895/2048:ℝ) (1791/4096:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_050_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_050_coefficients]
def edge131_3_051_coefficients : Fin 3 → Fin 4 → ℝ := ![![(279693780641408875122476369807700597253/7287046453125000000000:ℝ), (46556423579794866730599744605361465317/404835914062500000000:ℝ), (1549907967424102804579881727801433589/13494530468750000000:ℝ), (34828557321541239888373132885569244529/910880806640625000000:ℝ)], ![(139785297490931986885908093282035738789/1821761613281250000000:ℝ), (69803813181984024105248293624949722211/303626935546875000000:ℝ), (34857505291733982425909345525767206967/151813467773437500000:ℝ), (2175820029358396550170338780025384793/28465025207519531250:ℝ)], ![(69862002550748368309541110570604455177/1821761613281250000000:ℝ), (34886570597142852146520939946065535769/303626935546875000000:ℝ), (13936862562541087056625523762838863/121450774218750000:ℝ), (17398879348889006476108444045963310047/455440403320312500000:ℝ)]]
theorem edge131_3_051_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (17398879348889006476108444045963310047/29871617994228844814401536000000000000000:ℝ) edge131_3_051_coefficients (13011/32768:ℝ) (6507/16384:ℝ) (3581/8192:ℝ) (1791/4096:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_051_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_051_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (13011/32768:ℝ) (6507/16384:ℝ))
 (hp : p ∈ Set.Icc (3581/8192:ℝ) (1791/4096:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_051_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_051_coefficients]
def edge131_3_052_coefficients : Fin 3 → Fin 3 → ℝ := ![![(284561478223857722576299294599611477/36312300000000000000000:ℝ), (284069907639794222745187006139417557/18156150000000000000000:ℝ), (18905237134027311400271529658823899/2420820000000000000000:ℝ)], ![(284557228588840099708805175921467069/18156150000000000000000:ℝ), (284065489982266881377347071497042629/9078075000000000000000:ℝ), (3780986285024166255730876496036159/242082000000000000000:ℝ)], ![(569107188906764937813533774607264301/72624600000000000000000:ℝ), (142030843878759960764350564675774379/9078075000000000000000:ℝ), (18904666740615050651188737862145317/2420820000000000000000:ℝ)]]
theorem edge131_3_052_identity (δ p : ℝ) : rowMargin .newTop .capC δ p =
 Record12518109.Bernstein.bsum 2 2 (18904666740615050651188737862145317/19382051644321856225280000000000000000:ℝ) edge131_3_052_coefficients (813/2048:ℝ) (13011/32768:ℝ) (3581/8192:ℝ) (1791/4096:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_052_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_052_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (813/2048:ℝ) (13011/32768:ℝ))
 (hp : p ∈ Set.Icc (3581/8192:ℝ) (1791/4096:ℝ)) : 0 < rowMargin .newTop .capC δ p := by
 rw [edge131_3_052_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_052_coefficients]
def edge131_3_053_coefficients : Fin 3 → Fin 4 → ℝ := ![![(28022692332135702140570188104307116511/728704645312500000000:ℝ), (139935710238256259484837825466441418723/1214507742187500000000:ℝ), (139758024746831932525569801604864986313/1214507742187500000000:ℝ), (11166432413240967612490468041367926691/291481858125000000000:ℝ)], ![(28010404705465034633424195113505940543/364352322656250000000:ℝ), (139874220519599342000176071844862790347/607253871093750000000:ℝ), (15521831495855953684023584991935646463/67472652343750000000:ℝ), (697594061678698222404003794476422619/9108808066406250000:ℝ)], ![(27998177191055563820641838146879930111/728704645312500000000:ℝ), (139813031321919840293141748669424484123/1214507742187500000000:ℝ), (139635242659229722246973348111404462643/1214507742187500000000:ℝ), (27891503989260878842794977350891539073/728704645312500000000:ℝ)]]
theorem edge131_3_053_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (27891503989260878842794977350891539073/47794588790766151703042457600000000000000:ℝ) edge131_3_053_coefficients (13011/32768:ℝ) (6507/16384:ℝ) (895/2048:ℝ) (3581/8192:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_053_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_053_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (13011/32768:ℝ) (6507/16384:ℝ))
 (hp : p ∈ Set.Icc (895/2048:ℝ) (3581/8192:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_053_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_053_coefficients]
def edge131_3_054_coefficients : Fin 3 → Fin 3 → ℝ := ![![(14076693465411620531311317977155949/1793200000000000000000:ℝ), (1138245008543371471351774693496316797/72624600000000000000000:ℝ), (1136278726207117472027325539655541117/145249200000000000000000:ℝ)], ![(380065505508035983914906993619577983/24208200000000000000000:ℝ), (227645736418667970776636296528132249/7262460000000000000000:ℝ), (227252345533409396111469812988592697/14524920000000000000000:ℝ)], ![(380061108294130126280834920073049503/48416400000000000000000:ℝ), (1138214817908666646861458942279957381/72624600000000000000000:ℝ), (1136247191125216457349195910471623811/145249200000000000000000:ℝ)]]
theorem edge131_3_054_identity (δ p : ℝ) : rowMargin .newTop .capC δ p =
 Record12518109.Bernstein.bsum 2 2 (1136247191125216457349195910471623811/1162923098659311373516800000000000000000:ℝ) edge131_3_054_coefficients (813/2048:ℝ) (13011/32768:ℝ) (895/2048:ℝ) (3581/8192:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_054_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_054_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (813/2048:ℝ) (13011/32768:ℝ))
 (hp : p ∈ Set.Icc (895/2048:ℝ) (3581/8192:ℝ)) : 0 < rowMargin .newTop .capC δ p := by
 rw [edge131_3_054_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_054_coefficients]
def edge131_3_055_coefficients : Fin 3 → Fin 4 → ℝ := ![![(27730894051569951328181303476896553/728704645312500000000:ℝ), (27591370588842575000840442688889843/242901548437500000000:ℝ), (3431506724253061689898522052027051/30362693554687500000:ℝ), (54625886811172674289437924499385621/1457409290625000000000:ℝ)], ![(27684085441491719240153047315108357/364352322656250000000:ℝ), (9181466633380854229516096274232779/40483591406250000000:ℝ), (27404921275057106804923118741012239/121450774218750000000:ℝ), (13632824652232470478501893393839219/182176161328125000000:ℝ)], ![(27638217598662252693506357487201517/728704645312500000000:ℝ), (137491847370099799572768221018906153/1214507742187500000000:ℝ), (136793642571390073087371224388694253/1214507742187500000000:ℝ), (27219294457424743118720424203401027/728704645312500000000:ℝ)]]
theorem edge131_3_055_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (27219294457424743118720424203401027/46674403115982570022502400000000000000:ℝ) edge131_3_055_coefficients (3255/8192:ℝ) (1629/4096:ℝ) (447/1024:ℝ) (895/2048:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_055_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_055_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3255/8192:ℝ) (1629/4096:ℝ))
 (hp : p ∈ Set.Icc (447/1024:ℝ) (895/2048:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_055_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_055_coefficients]
def edge131_3_056_coefficients : Fin 3 → Fin 4 → ℝ := ![![(8807112286728788492237826068081561621/7287046453125000000000:ℝ), (4392423730886787691832661951770573983/1214507742187500000000:ℝ), (2190649784984215710358033317170116481/607253871093750000000:ℝ), (218509182769177887254342575263964253/182176161328125000000:ℝ)], ![(879950883920848122426798015922943117/364352322656250000000:ℝ), (48762394933347912042758846230106227/6747265234375000000:ℝ), (218874246245974512355594868752906823/30362693554687500000:ℝ), (5457953196413247645115456191510821/2277202016601562500:ℝ)], ![(87919805925244447171596788342696393/72870464531250000000:ℝ), (43848449474461884452775472671372761/12145077421875000000:ℝ), (10934269650289847327581720123923487/3036269355468750000:ℝ), (4362579029040886421075150916247507/3643523226562500000:ℝ)]]
theorem edge131_3_056_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (4362579029040886421075150916247507/7467904498557211203600384000000000000:ℝ) edge131_3_056_coefficients (6507/16384:ℝ) (3255/8192:ℝ) (1789/4096:ℝ) (895/2048:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_056_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_056_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (6507/16384:ℝ) (3255/8192:ℝ))
 (hp : p ∈ Set.Icc (1789/4096:ℝ) (895/2048:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_056_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_056_coefficients]
def edge131_3_057_coefficients : Fin 3 → Fin 4 → ℝ := ![![(280760461474691518714848851394214984819/7287046453125000000000:ℝ), (70101173716017112476502554917635332023/607253871093750000000:ℝ), (17503066259826756184530862948332346099/151813467773437500000:ℝ), (874042366601198739113961178322278781/22772020166015625000:ℝ)], ![(140318947419404423346710621081153545163/1821761613281250000000:ℝ), (11678417707426682948281227319009790837/50604489257812500000:ℝ), (8747696470660268243090545456264102343/37953366943359375000:ℝ), (218414594566935094878912224339935508/2846502520751953125:ℝ)], ![(70128982391885848065610295883050748931/1821761613281250000000:ℝ), (17509997273521865630328245547666768847/151813467773437500000:ℝ), (4371939299504658920895608775293869981/37953366943359375000:ℝ), (436638134221222208308100121076339603/11386010083007812500:ℝ)]]
theorem edge131_3_057_identity (δ p : ℝ) : rowMargin .newTop .weakC7 δ p =
 Record12518109.Bernstein.bsum 2 3 (436638134221222208308100121076339603/746790449855721120360038400000000000000:ℝ) edge131_3_057_coefficients (13011/32768:ℝ) (6507/16384:ℝ) (3579/8192:ℝ) (895/2048:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_057_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_057_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (13011/32768:ℝ) (6507/16384:ℝ))
 (hp : p ∈ Set.Icc (3579/8192:ℝ) (895/2048:ℝ)) : 0 < rowMargin .newTop .weakC7 δ p := by
 rw [edge131_3_057_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_057_coefficients]
def edge131_3_058_coefficients : Fin 3 → Fin 3 → ℝ := ![![(71386206746775604876152460337189941/9078075000000000000000:ℝ), (23754401374473418624458424873524679/1513012500000000000000:ℝ), (14228051297746928778619529140948369/1815615000000000000000:ℝ)], ![(71385312406970775703553289558843247/4539037500000000000000:ℝ), (23754089251589356017908459462563423/756506250000000000000:ℝ), (2845571124113802477495166389962429/181561500000000000000:ℝ)], ![(571076576070762212263362378677312987/72624600000000000000000:ℝ), (47507656874063631253204006386857387/3026025000000000000000:ℝ), (14227690725047542726198129191817327/1815615000000000000000:ℝ)]]
theorem edge131_3_058_identity (δ p : ℝ) : rowMargin .newTop .capC δ p =
 Record12518109.Bernstein.bsum 2 2 (14227690725047542726198129191817327/14536538733241392168960000000000000000:ℝ) edge131_3_058_coefficients (813/2048:ℝ) (13011/32768:ℝ) (3579/8192:ℝ) (895/2048:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_058_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_058_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (813/2048:ℝ) (13011/32768:ℝ))
 (hp : p ∈ Set.Icc (3579/8192:ℝ) (895/2048:ℝ)) : 0 < rowMargin .newTop .capC δ p := by
 rw [edge131_3_058_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_058_coefficients]
def edge131_3_059_coefficients : Fin 3 → Fin 3 → ℝ := ![![(1560475705640586441448283914396121/145249200000000000000000:ℝ), (1050391185434649055613523044644057/72624600000000000000000:ℝ), (20020781008456552899271291907483/5379600000000000000000:ℝ)], ![(1542148005296249556311584221512729/72624600000000000000000:ℝ), (1031726789753977378516041342183097/36312300000000000000000:ℝ), (57951121089840128896331199191521/8069400000000000000000:ℝ)], ![(1526394040371398856958743894623633/145249200000000000000000:ℝ), (1015635865713373985596583813353117/72624600000000000000000:ℝ), (56125811142406703541468500588207/16138800000000000000000:ℝ)]]
theorem edge131_3_059_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (56125811142406703541468500588207/32303419407203093708800000000000000000:ℝ) edge131_3_059_coefficients (813/2048:ℝ) (6507/16384:ℝ) (1789/4096:ℝ) (3579/8192:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_059_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_059_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (813/2048:ℝ) (6507/16384:ℝ))
 (hp : p ∈ Set.Icc (1789/4096:ℝ) (3579/8192:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_059_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_059_coefficients]
def edge131_3_060_coefficients : Fin 3 → Fin 3 → ℝ := ![![(194104231352064710169482823066977/145249200000000000000000:ℝ), (43426686942139574104915679231819/24208200000000000000000:ℝ), (66519495800676549085401928976449/145249200000000000000000:ℝ)], ![(7679266531032413837209847115017/2904984000000000000000:ℝ), (1707643628232804128838067713059/484164000000000000000:ℝ), (2569141330305377537732578694641/2904984000000000000000:ℝ)], ![(1524022342928479897521603093013/1161993600000000000000:ℝ), (337360131074886384692921485183/193665600000000000000:ℝ), (2503240182778554969887673890167/5809968000000000000000:ℝ)]]
theorem edge131_3_060_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (2503240182778554969887673890167/726826936662069608448000000000000000:ℝ) edge131_3_060_coefficients (813/2048:ℝ) (3255/8192:ℝ) (447/1024:ℝ) (1789/4096:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_060_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_060_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (813/2048:ℝ) (3255/8192:ℝ))
 (hp : p ∈ Set.Icc (447/1024:ℝ) (1789/4096:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_060_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_060_coefficients]
def edge131_3_061_coefficients : Fin 3 → Fin 3 → ℝ := ![![(314550198396924783950658073709/18156150000000000000000:ℝ), (75758678948409564864405032623/3631230000000000000000:ℝ), (17264030483499091235261800201/4841640000000000000000:ℝ)], ![(155860983732938592972753698071/4539037500000000000000:ℝ), (92954515145044992615061574867/2269518750000000000000:ℝ), (10099078923197881162912113019/1513012500000000000000:ℝ)], ![(156965436850715538735456895759/9078075000000000000000:ℝ), (93727186894414117041900136271/4539037500000000000000:ℝ), (10246286797469254130857025317/3026025000000000000000:ℝ)]]
theorem edge131_3_061_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (10099078923197881162912113019/1478733188195942400000000000000000:ℝ) edge131_3_061_coefficients (813/2048:ℝ) (51/128:ℝ) (223/512:ℝ) (447/1024:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_061_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_061_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (813/2048:ℝ) (51/128:ℝ))
 (hp : p ∈ Set.Icc (223/512:ℝ) (447/1024:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_061_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_061_coefficients]
def edge131_3_062_coefficients : Fin 3 → Fin 3 → ℝ := ![![(759153809580053078418468975433/6052050000000000000000:ℝ), (69305087817032805525346361807/283689843750000000000:ℝ), (16863210100795724463299629933/141844921875000000000:ℝ)], ![(56204231238081777319693163603/224150000000000000000:ℝ), (138515343078628264569086160139/283689843750000000000:ℝ), (16848810633676164845890664353/70922460937500000000:ℝ)], ![(3035049124644675670156147476473/24208200000000000000000:ℝ), (276991452437241551457979247963/1134759375000000000000:ℝ), (16843796831989676242096444267/141844921875000000000:ℝ)]]
theorem edge131_3_062_identity (δ p : ℝ) : rowMargin .newTop .capC δ p =
 Record12518109.Bernstein.bsum 2 2 (16843796831989676242096444267/17328904549171200000000000000000:ℝ) edge131_3_062_coefficients (405/1024:ℝ) (813/2048:ℝ) (223/512:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_062_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_062_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (405/1024:ℝ) (813/2048:ℝ))
 (hp : p ∈ Set.Icc (223/512:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .capC δ p := by
 rw [edge131_3_062_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_062_coefficients]
def edge131_3_063_coefficients : Fin 3 → Fin 3 → ℝ := ![![(4363221957227930635192200791/1815615000000000000000:ℝ), (3737183451718071009487661203/1210410000000000000000:ℝ), (10039225179002673288510117023/14524920000000000000000:ℝ)], ![(8595486511316962577768191747/1815615000000000000000:ℝ), (1813968817761243361608736613/302602500000000000000:ℝ), (2313172092309441133734835493/1815615000000000000000:ℝ)], ![(8717212089257937295648441243/3631230000000000000000:ℝ), (9217178743355599177579722253/3026025000000000000000:ℝ), (11841973740991442109349976887/18156150000000000000000:ℝ)]]
theorem edge131_3_063_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (2313172092309441133734835493/110904989114695680000000000000000:ℝ) edge131_3_063_coefficients (405/1024:ℝ) (51/128:ℝ) (111/256:ℝ) (223/512:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_063_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_063_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (405/1024:ℝ) (51/128:ℝ))
 (hp : p ∈ Set.Icc (111/256:ℝ) (223/512:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_063_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_063_coefficients]
def edge131_3_064_coefficients : Fin 3 → Fin 3 → ℝ := ![![(30037728028923432088152703559/3631230000000000000000:ℝ), (991918605220796432655205813/63042187500000000000:ℝ), (4237160999150805719198220349/567379687500000000000:ℝ)], ![(11985555616740542108981838047/726246000000000000000:ℝ), (395516544817715737661273527/12608437500000000000:ℝ), (844115120031590979375798413/56737968750000000000:ℝ)], ![(23960429180787034789226421427/2904984000000000000000:ℝ), (158041130429490259455750739/10086750000000000000:ℝ), (168535034663927003526980371/22695187500000000000:ℝ)]]
theorem edge131_3_064_identity (δ p : ℝ) : rowMargin .newTop .capC δ p =
 Record12518109.Bernstein.bsum 2 2 (168535034663927003526980371/173289045491712000000000000000:ℝ) edge131_3_064_coefficients (201/512:ℝ) (405/1024:ℝ) (111/256:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_064_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_064_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (201/512:ℝ) (405/1024:ℝ))
 (hp : p ∈ Set.Icc (111/256:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .capC δ p := by
 rw [edge131_3_064_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_064_coefficients]
def edge131_3_065_coefficients : Fin 3 → Fin 3 → ℝ := ![![(2309927676174865155459814877/7262460000000000000000:ℝ), (3834770749541747620914176857/9078075000000000000000:ℝ), (57043956308150543546636363/537960000000000000000:ℝ)], ![(89866418994418924005292967/145249200000000000000:ℝ), (7271235661554055556486312951/9078075000000000000000:ℝ), (74909257122815479122380401/403470000000000000000:ℝ)], ![(2310563302927625238333174887/7262460000000000000000:ℝ), (7506704597008637194233189779/18156150000000000000000:ℝ), (78290523176731443507942887/806940000000000000000:ℝ)]]
theorem edge131_3_065_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (74909257122815479122380401/1540347071037440000000000000000:ℝ) edge131_3_065_coefficients (201/512:ℝ) (51/128:ℝ) (55/128:ℝ) (111/256:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_065_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_065_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (201/512:ℝ) (51/128:ℝ))
 (hp : p ∈ Set.Icc (55/128:ℝ) (111/256:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_065_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_065_coefficients]
def edge131_3_066_coefficients : Fin 3 → Fin 3 → ℝ := ![![(3050826992855413940266236463057/24208200000000000000000:ℝ), (278795794058984251465460460947/1134759375000000000000:ℝ), (8488400496451217958818558939/70922460937500000000:ℝ)], ![(253701506136287458495525522387/1008675000000000000000:ℝ), (69538708693882603163296792523/141844921875000000000:ℝ), (2116780566185457907422989477/8865307617187500000:ℝ)], ![(189976033979221318558096111457/1513012500000000000000:ℝ), (17354019180183518070245870867/70922460937500000000:ℝ), (1056317108218622600921591203/8865307617187500000:ℝ)]]
theorem edge131_3_066_identity (δ p : ℝ) : rowMargin .newTop .capC δ p =
 Record12518109.Bernstein.bsum 2 2 (1056317108218622600921591203/1083056534323200000000000000000:ℝ) edge131_3_066_coefficients (801/2048:ℝ) (201/512:ℝ) (223/512:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_066_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_066_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (801/2048:ℝ) (201/512:ℝ))
 (hp : p ∈ Set.Icc (223/512:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .capC δ p := by
 rw [edge131_3_066_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_066_coefficients]
def edge131_3_067_coefficients : Fin 3 → Fin 3 → ℝ := ![![(44090880194822815358208612701/6052050000000000000000:ℝ), (2279421515135413530737980763/283689843750000000000:ℝ), (110099456670539747899150081/141844921875000000000:ℝ)], ![(16702554852460624621352243671/1210410000000000000000:ℝ), (4101162980356224466952393281/283689843750000000000:ℝ), (16129725925907780508569/22695187500000000:ℝ)], ![(53122207330707242501465371199/8069400000000000000000:ℝ), (7444118485656458183563151207/1134759375000000000000:ℝ), (517281394045908095822263/141844921875000000000:ℝ)]]
theorem edge131_3_067_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (517281394045908095822263/17328904549171200000000000000000:ℝ) edge131_3_067_coefficients (399/1024:ℝ) (801/2048:ℝ) (223/512:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_067_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_067_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (399/1024:ℝ) (801/2048:ℝ))
 (hp : p ∈ Set.Icc (223/512:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_067_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_067_coefficients]
def edge131_3_068_coefficients : Fin 3 → Fin 3 → ℝ := ![![(98401257185040716619821107783/36312300000000000000000:ℝ), (17837105234416035457050193/4728164062500000000:ℝ), (77657816100179939219135028553/72624600000000000000000:ℝ)], ![(92038023532054261483729822813/18156150000000000000000:ℝ), (20603468838921231612827270633/3026025000000000000000:ℝ), (15912714429538104097541751853/9078075000000000000000:ℝ)], ![(88201619689866540452603131153/36312300000000000000000:ℝ), (19216341367866624011053312487/6052050000000000000000:ℝ), (27340518251363191545878029607/36312300000000000000000:ℝ)]]
theorem edge131_3_068_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (27340518251363191545878029607/1109049891146956800000000000000000:ℝ) edge131_3_068_coefficients (399/1024:ℝ) (201/512:ℝ) (111/256:ℝ) (223/512:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_068_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_068_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (399/1024:ℝ) (201/512:ℝ))
 (hp : p ∈ Set.Icc (111/256:ℝ) (223/512:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_068_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_068_coefficients]
def edge131_3_069_coefficients : Fin 3 → Fin 3 → ℝ := ![![(4295479279222150360968974551/4539037500000000000000:ℝ), (102756376570097505411611917/94563281250000000000:ℝ), (83327106437813168625659593/567379687500000000000:ℝ)], ![(16070659183915452788743913419/9078075000000000000000:ℝ), (180712018652010921201702767/94563281250000000000:ℝ), (43674123834112173904307521/283689843750000000000:ℝ)], ![(61101019909168583586930011191/72624600000000000000000:ℝ), (649880142172613398378784261/756506250000000000000:ℝ), (13827092258073206999371543/567379687500000000000:ℝ)]]
theorem edge131_3_069_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (13827092258073206999371543/4332226137292800000000000000000:ℝ) edge131_3_069_coefficients (99/256:ℝ) (399/1024:ℝ) (111/256:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_069_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_069_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (99/256:ℝ) (399/1024:ℝ))
 (hp : p ∈ Set.Icc (111/256:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_069_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_069_coefficients]
def edge131_3_070_coefficients : Fin 3 → Fin 3 → ℝ := ![![(10062708240631387787016216197/29049840000000000000000:ℝ), (35440610827958653484623738409/72624600000000000000000:ℝ), (154118525152890160265936519/1075920000000000000000:ℝ)], ![(9300959317847642791592887733/14524920000000000000000:ℝ), (31312288385904809450899904993/36312300000000000000000:ℝ), (72715418505544786734993293/322776000000000000000:ℝ)], ![(361915620503602982811316997/1161993600000000000000:ℝ), (29719065035787050709531741941/72624600000000000000000:ℝ), (320950383170082588884669891/3227760000000000000000:ℝ)]]
theorem edge131_3_070_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (320950383170082588884669891/6161388284149760000000000000000:ℝ) edge131_3_070_coefficients (99/256:ℝ) (201/512:ℝ) (55/128:ℝ) (111/256:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_070_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_070_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (99/256:ℝ) (201/512:ℝ))
 (hp : p ∈ Set.Icc (55/128:ℝ) (111/256:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_070_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_070_coefficients]
def edge131_3_071_coefficients : Fin 3 → Fin 3 → ℝ := ![![(3019746940910512778229117581/72624600000000000000000:ℝ), (686799579033548162452884797/12104100000000000000000:ℝ), (14135507358134395583813381/907807500000000000000:ℝ)], ![(2862311994148464348761896553/36312300000000000000000:ℝ), (620766475749204686121587711/6052050000000000000000:ℝ), (178558810056166267127056067/7262460000000000000000:ℝ)], ![(3026968975966399387631148449/72624600000000000000000:ℝ), (661400188257381252581504963/12104100000000000000000:ℝ), (38906903414590860335453749/2904984000000000000000:ℝ)]]
theorem edge131_3_071_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (178558810056166267127056067/1732890454917120000000000000000:ℝ) edge131_3_071_coefficients (99/256:ℝ) (51/128:ℝ) (27/64:ℝ) (55/128:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_071_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_071_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (99/256:ℝ) (51/128:ℝ))
 (hp : p ∈ Set.Icc (27/64:ℝ) (55/128:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_071_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_071_coefficients]
def edge131_3_072_coefficients : Fin 3 → Fin 3 → ℝ := ![![(27827178841247112909439261/1815615000000000000000:ℝ), (5608597285289339170729951/302602500000000000000:ℝ), (32668511038758974415374353/9078075000000000000000:ℝ)], ![(124150679351797067740830869/4539037500000000000000:ℝ), (22244313102288891510614603/756506250000000000000:ℝ), (12949314360171697918620241/4539037500000000000000:ℝ)], ![(190769339624772886911968339/14524920000000000000000:ℝ), (1580575320729767630415367/121041000000000000000:ℝ), (3036068709246449238282223/9078075000000000000000:ℝ)]]
theorem edge131_3_072_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (3036068709246449238282223/270764133580800000000000000000:ℝ) edge131_3_072_coefficients (3/8:ℝ) (99/256:ℝ) (27/64:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_072_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_072_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3/8:ℝ) (99/256:ℝ))
 (hp : p ∈ Set.Icc (27/64:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_072_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_072_coefficients]
def edge131_3_073_coefficients : Fin 3 → Fin 3 → ℝ := ![![(49907888213071205378067727/9078075000000000000000:ℝ), (7053906561953749034267587/907807500000000000000:ℝ), (286903987707265012330349/121041000000000000000:ℝ)], ![(44869900109847399575170711/4539037500000000000000:ℝ), (28982327941566954879525227/2269518750000000000000:ℝ), (4675063883608542507197819/1513012500000000000000:ℝ)], ![(100321466669782913158794533/18156150000000000000000:ℝ), (131564853666564426883616669/18156150000000000000000:ℝ), (44261218644615633343801381/24208200000000000000000:ℝ)]]
theorem edge131_3_073_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (4675063883608542507197819/22563677798400000000000000000:ℝ) edge131_3_073_coefficients (3/8:ℝ) (51/128:ℝ) (13/32:ℝ) (27/64:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_073_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_073_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3/8:ℝ) (51/128:ℝ))
 (hp : p ∈ Set.Icc (13/32:ℝ) (27/64:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_073_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_073_coefficients]
def edge131_3_074_coefficients : Fin 3 → Fin 3 → ℝ := ![![(12388054541837053365039863/18156150000000000000000:ℝ), (2761718285074047611091133/3026025000000000000000:ℝ), (4625566004396527781590951/18156150000000000000000:ℝ)], ![(12421588486969612780776983/9078075000000000000000:ℝ), (2550088737301727875668997/1513012500000000000000:ℝ), (3366068978590576330866697/9078075000000000000000:ℝ)], ![(17889021885900868800449843/18156150000000000000000:ℝ), (1026043268142839708186191/756506250000000000000:ℝ), (5816786093534845026963383/14524920000000000000000:ℝ)]]
theorem edge131_3_074_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (3366068978590576330866697/8461379174400000000000000000:ℝ) edge131_3_074_coefficients (3/8:ℝ) (27/64:ℝ) (3/8:ℝ) (13/32:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_074_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_074_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3/8:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (3/8:ℝ) (13/32:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_074_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_074_coefficients]
def edge131_3_075_coefficients : Fin 3 → Fin 4 → ℝ := ![![(189802824308667092841615053911/2545509886855875000000000000:ℝ), (362819813757240193672312852661/2545509886855875000000000000:ℝ), (195027450409823198842162577353/2545509886855875000000000000:ℝ), (6892505308862399110079926201/848503295618625000000000000:ℝ)], ![(276837919843036080947494510831/1272754943427937500000000000:ℝ), (102021679878867674468581540897/254550988685587500000000000:ℝ), (246573884284489888387330438543/1272754943427937500000000000:ℝ), (3767995727064415323359914963/424251647809312500000000000:ℝ)], ![(783391278258485613900461564971/2545509886855875000000000000:ℝ), (1817969535128811906691576186301/2545509886855875000000000000:ℝ), (684543052479453464381701893959/1272754943427937500000000000:ℝ), (27625726813382425786627743049/212125823904656250000000000:ℝ)]]
theorem edge131_3_075_identity (δ p : ℝ) : rowMargin .newTop .old δ p =
 Record12518109.Bernstein.bsum 2 3 (3767995727064415323359914963/12357224884813824000000000000000:ℝ) edge131_3_075_coefficients (3/8:ℝ) (9/16:ℝ) (1/4:ℝ) (3/8:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_075_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_075_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3/8:ℝ) (9/16:ℝ))
 (hp : p ∈ Set.Icc (1/4:ℝ) (3/8:ℝ)) : 0 < rowMargin .newTop .old δ p := by
 rw [edge131_3_075_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_075_coefficients]
def edge131_3_076_coefficients : Fin 3 → Fin 4 → ℝ := ![![(3397897338225659523251200763/407281581896940000000000000:ℝ), (160400004649401400964649946193/10182039547423500000000000000:ℝ), (89354691946539084740325852043/10182039547423500000000000000:ℝ), (502767028724650847029236997/407281581896940000000000000:ℝ)], ![(7320882082419133005364526843/203640790948470000000000000:ℝ), (357567576469764224212719586121/5091019773711750000000000000:ℝ), (211539364080320218643257204201/5091019773711750000000000000:ℝ), (6865589920341703640440157831/1018203954742350000000000000:ℝ)], ![(24276877447314686487477852923/407281581896940000000000000:ℝ), (1396727970199962970489840984937/10182039547423500000000000000:ℝ), (1060983669081588448680009113857/10182039547423500000000000000:ℝ), (53169170985168207530442890399/2036407909484700000000000000:ℝ)]]
theorem edge131_3_076_identity (δ p : ℝ) : rowMargin .newTop .old δ p =
 Record12518109.Bernstein.bsum 2 3 (502767028724650847029236997/185358373272207360000000000000:ℝ) edge131_3_076_coefficients (3/8:ℝ) (3/4:ℝ) (0:ℝ) (1/4:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_076_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_076_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3/8:ℝ) (3/4:ℝ))
 (hp : p ∈ Set.Icc (0:ℝ) (1/4:ℝ)) : 0 < rowMargin .newTop .old δ p := by
 rw [edge131_3_076_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_076_coefficients]
def edge131_3_077_coefficients : Fin 3 → Fin 3 → ℝ := ![![(7813774127242660484504297/24208200000000000000000:ℝ), (301971675199959176644643/567379687500000000000:ℝ), (256222445818957567138693/1134759375000000000000:ℝ)], ![(45751065772125198321943/100867500000000000000:ℝ), (22377673953703573917487/35461230468750000000:ℝ), (15203882630069528997137/70922460937500000000:ℝ)], ![(73918112972592021591973/378253125000000000000:ℝ), (3916327979370856449949/17730615234375000000:ℝ), (1641272956462918352849/35461230468750000000:ℝ)]]
theorem edge131_3_077_identity (δ p : ℝ) : rowMargin .newTop .capC δ p =
 Record12518109.Bernstein.bsum 2 2 (1641272956462918352849/4131532800000000000000000:ℝ) edge131_3_077_coefficients (21/64:ℝ) (3/8:ℝ) (7/16:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_077_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_077_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (21/64:ℝ) (3/8:ℝ))
 (hp : p ∈ Set.Icc (7/16:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .capC δ p := by
 rw [edge131_3_077_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_077_coefficients]
def edge131_3_078_coefficients : Fin 3 → Fin 3 → ℝ := ![![(479339437982063304549761/1210410000000000000000:ℝ), (810766573080965984178487/1134759375000000000000:ℝ), (758291861279423944818887/2269518750000000000000:ℝ)], ![(2748252611073060149079217/6052050000000000000000:ℝ), (81418175214328310419151/113475937500000000000:ℝ), (67774923945155966559511/226951875000000000000:ℝ)], ![(337838539547553237932333/2689800000000000000000:ℝ), (148589153537599003305661/1134759375000000000000:ℝ), (57090694775595784293761/2269518750000000000000:ℝ)]]
theorem edge131_3_078_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (57090694775595784293761/264418099200000000000000000:ℝ) edge131_3_078_coefficients (9/32:ℝ) (21/64:ℝ) (7/16:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_078_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_078_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (9/32:ℝ) (21/64:ℝ))
 (hp : p ∈ Set.Icc (7/16:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_078_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_078_coefficients]
def edge131_3_079_coefficients : Fin 3 → Fin 3 → ℝ := ![![(2299856343533099606507041/18156150000000000000000:ℝ), (50687068508507971304123/224150000000000000000:ℝ), (7507346113295069656449407/72624600000000000000000:ℝ)], ![(472786611612497691245123/4539037500000000000000:ℝ), (208269586635594174139/1576054687500000000:ℝ), (342980201763087741798557/9078075000000000000000:ℝ)], ![(474882483183282654728693/9078075000000000000000:ℝ), (24272361418872305165921/504337500000000000000:ℝ), (17433876830080773268387/9078075000000000000000:ℝ)]]
theorem edge131_3_079_identity (δ p : ℝ) : rowMargin .newTop .capP δ p =
 Record12518109.Bernstein.bsum 2 2 (17433876830080773268387/264418099200000000000000000:ℝ) edge131_3_079_coefficients (9/32:ℝ) (3/8:ℝ) (3/8:ℝ) (7/16:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_079_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_079_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (9/32:ℝ) (3/8:ℝ))
 (hp : p ∈ Set.Icc (3/8:ℝ) (7/16:ℝ)) : 0 < rowMargin .newTop .capP δ p := by
 rw [edge131_3_079_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_079_coefficients]
def edge131_3_080_coefficients : Fin 3 → Fin 4 → ℝ := ![![(345466596393033588835959985439/636377471713968750000000000:ℝ), (980507929945355340565666767491/636377471713968750000000000:ℝ), (467319517299021755053852412843/318188735856984375000000000:ℝ), (149632232393528016603845896817/318188735856984375000000000:ℝ)], ![(351981400715883411482146731751/636377471713968750000000000:ℝ), (189344892078938349055686345443/127275494342793750000000000:ℝ), (43312500579696964703680125583/31818873585698437500000000:ℝ), (67626810784783446191599691549/159094367928492187500000000:ℝ)], ![(355637480616189105414360190661/2545509886855875000000000000:ℝ), (771369914946334156997833583189/2545509886855875000000000000:ℝ), (69761558847429358271675110763/318188735856984375000000000:ℝ), (17420113765162286007146405447/318188735856984375000000000:ℝ)]]
theorem edge131_3_080_identity (δ p : ℝ) : rowMargin .newTop .old δ p =
 Record12518109.Bernstein.bsum 2 3 (17420113765162286007146405447/18535837327220736000000000000000:ℝ) edge131_3_080_coefficients (3/16:ℝ) (9/32:ℝ) (3/8:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_080_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_080_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3/16:ℝ) (9/32:ℝ))
 (hp : p ∈ Set.Icc (3/8:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .old δ p := by
 rw [edge131_3_080_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_080_coefficients]
def edge131_3_081_coefficients : Fin 3 → Fin 4 → ℝ := ![![(215282065874156342898431860217/1272754943427937500000000000:ℝ), (607377449731164132484478364217/1272754943427937500000000000:ℝ), (1148840076342149243542492292587/2545509886855875000000000000:ℝ), (121438690789822646400031011529/848503295618625000000000000:ℝ)], ![(246434583923620927275516533/3197876742281250000000000:ℝ), (100735467501025543980738975133/636377471713968750000000000:ℝ), (16177590427133197782094333199/159094367928492187500000000:ℝ), (422738004988069550171996591/21212582390465625000000000:ℝ)], ![(92558029967985058580767518527/1272754943427937500000000000:ℝ), (34875952063914926663207280209/254550988685587500000000000:ℝ), (90483578645866135900961263391/1272754943427937500000000000:ℝ), (2665125258981703608359960291/424251647809312500000000000:ℝ)]]
theorem edge131_3_081_identity (δ p : ℝ) : rowMargin .newTop .old δ p =
 Record12518109.Bernstein.bsum 2 3 (2665125258981703608359960291/6178612442406912000000000000000:ℝ) edge131_3_081_coefficients (3/16:ℝ) (3/8:ℝ) (1/4:ℝ) (3/8:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_081_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_081_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3/16:ℝ) (3/8:ℝ))
 (hp : p ∈ Set.Icc (1/4:ℝ) (3/8:ℝ)) : 0 < rowMargin .newTop .old δ p := by
 rw [edge131_3_081_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_081_coefficients]
def edge131_3_082_coefficients : Fin 3 → Fin 4 → ℝ := ![![(56832797279917344298563960739/848503295618625000000000000:ℝ), (475682473147208334257796926651/2545509886855875000000000000:ℝ), (439869770775160569828518206651/2545509886855875000000000000:ℝ), (134685689467704268466413162217/2545509886855875000000000000:ℝ)], ![(8499801451253113355239435003/141417215936437500000000000:ℝ), (214218880843217239182019726181/1272754943427937500000000000:ℝ), (199604921856147792017361951571/1272754943427937500000000000:ℝ), (61884254074208573032497140417/1272754943427937500000000000:ℝ)], ![(23291878095292717069669264993/1697006591237250000000000000:ℝ), (171158154966329557416206168503/5091019773711750000000000000:ℝ), (14371207973745543220055894909/509101977371175000000000000:ℝ), (20881543269836287826374037783/2545509886855875000000000000:ℝ)]]
theorem edge131_3_082_identity (δ p : ℝ) : rowMargin .newTop .old δ p =
 Record12518109.Bernstein.bsum 2 3 (20881543269836287826374037783/4633959331805184000000000000000:ℝ) edge131_3_082_coefficients (0:ℝ) (3/16:ℝ) (1/4:ℝ) (1/2:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_082_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_082_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (0:ℝ) (3/16:ℝ))
 (hp : p ∈ Set.Icc (1/4:ℝ) (1/2:ℝ)) : 0 < rowMargin .newTop .old δ p := by
 rw [edge131_3_082_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_082_coefficients]
def edge131_3_083_coefficients : Fin 3 → Fin 4 → ℝ := ![![(29507529880436285114025733253/1018203954742350000000000000:ℝ), (380099437438383487487391288319/5091019773711750000000000000:ℝ), (20663001055290488767587754679/318188735856984375000000000:ℝ), (9737975633111430802352895281/509101977371175000000000000:ℝ)], ![(16539927049648452524592363653/509101977371175000000000000:ℝ), (156270598303828349220935048803/2545509886855875000000000000:ℝ), (89162872584685406117425148273/2545509886855875000000000000:ℝ), (2851792898887283767645383547/509101977371175000000000000:ℝ)], ![(36154850770615819935158994053/1018203954742350000000000000:ℝ), (353438170124191172469004688731/5091019773711750000000000000:ℝ), (211347544718466540020356500431/5091019773711750000000000000:ℝ), (7203547675605733172939356393/1018203954742350000000000000:ℝ)]]
theorem edge131_3_083_identity (δ p : ℝ) : rowMargin .newTop .old δ p =
 Record12518109.Bernstein.bsum 2 3 (2851792898887283767645383547/1853583732722073600000000000000:ℝ) edge131_3_083_coefficients (3/16:ℝ) (3/8:ℝ) (0:ℝ) (1/4:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_083_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_083_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (3/16:ℝ) (3/8:ℝ))
 (hp : p ∈ Set.Icc (0:ℝ) (1/4:ℝ)) : 0 < rowMargin .newTop .old δ p := by
 rw [edge131_3_083_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_083_coefficients]
def edge131_3_084_coefficients : Fin 3 → Fin 4 → ℝ := ![![(159426365820198722748724537891/2036407909484700000000000000:ℝ), (449628935562957956702750637673/2036407909484700000000000000:ℝ), (420978773665319745159327661673/2036407909484700000000000000:ℝ), (130776203922560511205301561891/2036407909484700000000000000:ℝ)], ![(68326107055112657569857798691/1018203954742350000000000000:ℝ), (191698835527168716790357790089/1018203954742350000000000000:ℝ), (178948789371837360266971979537/1018203954742350000000000000:ℝ), (55576060899781301046471988139/1018203954742350000000000000:ℝ)], ![(42390901393536992390991059491/2036407909484700000000000000:ℝ), (510836499366733307418876471413/10182039547423500000000000000:ℝ), (411853658259261973006902044503/10182039547423500000000000000:ℝ), (22327744165110145372351174109/2036407909484700000000000000:ℝ)]]
theorem edge131_3_084_identity (δ p : ℝ) : rowMargin .newTop .old δ p =
 Record12518109.Bernstein.bsum 2 3 (22327744165110145372351174109/3707167465444147200000000000000:ℝ) edge131_3_084_coefficients (0:ℝ) (3/16:ℝ) (0:ℝ) (1/4:ℝ) δ p := by
 norm_num [rowMargin,Ebase,edgeD,edgeC,oldCapacity,newCapacity,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,edge131_3_084_coefficients,Fin.sum_univ_succ] <;> ring
theorem edge131_3_084_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (0:ℝ) (3/16:ℝ))
 (hp : p ∈ Set.Icc (0:ℝ) (1/4:ℝ)) : 0 < rowMargin .newTop .old δ p := by
 rw [edge131_3_084_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [edge131_3_084_coefficients]
end
end QRH.ArviDensity.Return
