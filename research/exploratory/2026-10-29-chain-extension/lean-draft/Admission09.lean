/- Generated candidate; uncompiled; requires the count-source overlay. -/
import Submissions.arvi_density.Return.Formulas
set_option autoImplicit false
set_option linter.unnecessarySeqFocus false
namespace QRH.ArviDensity.Return
noncomputable section
def admission09_00_coefficients : Fin 1 → Fin 2 → ℝ := ![![(364596/26971:ℝ), (281625/26971:ℝ)]]
theorem admission09_00_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 0 =
 Record12518109.Bernstein.bsum 0 1 (11265/15412:ℝ) admission09_00_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_00_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_00_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 0 := by
 rw [admission09_00_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_00_coefficients]
def admission09_01_coefficients : Fin 1 → Fin 2 → ℝ := ![![(241300/26971:ℝ), (185300/26971:ℝ)]]
theorem admission09_01_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 1 =
 Record12518109.Bernstein.bsum 0 1 (1853/3853:ℝ) admission09_01_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_01_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_01_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 1 := by
 rw [admission09_01_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_01_coefficients]
def admission09_02_coefficients : Fin 1 → Fin 2 → ℝ := ![![(1543604449/337137500:ℝ), (96592161/26971000:ℝ)]]
theorem admission09_02_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 2 =
 Record12518109.Bernstein.bsum 0 1 (96592161/385300000:ℝ) admission09_02_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_02_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_02_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 2 := by
 rw [admission09_02_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_02_coefficients]
def admission09_03_coefficients : Fin 2 → Fin 3 → ℝ := ![![(178831524100/37570603:ℝ), (309078674600/37570603:ℝ), (131492142500/37570603:ℝ)], ![(170810650000/37570603:ℝ), (293458587500/37570603:ℝ), (123970937500/37570603:ℝ)]]
theorem admission09_03_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 3 =
 Record12518109.Bernstein.bsum 1 2 (396707/986368:ℝ) admission09_03_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_03_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_03_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 3 := by
 rw [admission09_03_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_03_coefficients]
def admission09_04_coefficients : Fin 2 → Fin 3 → ℝ := ![![(76571190538317/117408134375:ℝ), (196218299668/187853015:ℝ), (76694175834/187853015:ℝ)], ![(5399830855137/7514120600:ℝ), (218123754207/187853015:ℝ), (172610191707/375706030:ℝ)]]
theorem admission09_04_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 4 =
 Record12518109.Bernstein.bsum 1 2 (38347087917/770600000000:ℝ) admission09_04_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_04_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_04_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 4 := by
 rw [admission09_04_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_04_coefficients]
def admission09_05_coefficients : Fin 2 → Fin 3 → ℝ := ![![(132176930639241/234816268750:ℝ), (997932121321/939265075:ℝ), (184821432459/375706030:ℝ)], ![(3329503832253/7514120600:ℝ), (126530936715/150282412:ℝ), (29360820225/75141206:ℝ)]]
theorem admission09_05_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 5 =
 Record12518109.Bernstein.bsum 1 2 (1174432809/24659200000:ℝ) admission09_05_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_05_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_05_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 5 := by
 rw [admission09_05_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_05_coefficients]
def admission09_06_coefficients : Fin 2 → Fin 4 → ℝ := ![![(288649641834038572/18094941669875:ℝ), (26130139517419427564/669512841785375:ℝ), (836575799513511016/26780513671415:ℝ), (43507741283758200/5356102734283:ℝ)], ![(1260467043600111097/74985438279962:ℝ), (3093262811836090697/74985438279962:ℝ), (1243297990313351150/37492719139981:ℝ), (325363317333361350/37492719139981:ℝ)]]
theorem admission09_06_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 6 =
 Record12518109.Bernstein.bsum 1 3 (1522770944931537/21971501320000000:ℝ) admission09_06_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_06_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_06_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 6 := by
 rw [admission09_06_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_06_coefficients]
def admission09_07_coefficients : Fin 2 → Fin 3 → ℝ := ![![(3967000041093714371/1809494166987500:ℝ), (127577126183936887/36189883339750:ℝ), (802953151211859/579038133436:ℝ)], ![(57811618718861969/28951906671800:ℝ), (921594562944359/289519066718:ℝ), (716339539996125/579038133436:ℝ)]]
theorem admission09_07_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 7 =
 Record12518109.Bernstein.bsum 1 2 (5730716319969/38004759040000:ℝ) admission09_07_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_07_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_07_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 7 := by
 rw [admission09_07_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_07_coefficients]
def admission09_08_coefficients : Fin 2 → Fin 4 → ℝ := ![![(12507343125645404641049/50665836675650000000:ℝ), (19874129066024452303369/50665836675650000000:ℝ), (163111980363576277759/1013316733513000000:ℝ), (46616597862484107/8106533868104000:ℝ)], ![(3274882882270895844149/3242613547241600000:ℝ), (7884641999403633786169/3242613547241600000:ℝ), (32014649274098722219/16213067736208000:ℝ), (17593384903033805697/32426135472416000:ℝ)]]
theorem admission09_08_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 8 =
 Record12518109.Bernstein.bsum 1 3 (46616597862484107/950118976000000000000:ℝ) admission09_08_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_08_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_08_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 8 := by
 rw [admission09_08_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_08_coefficients]
def admission09_09_coefficients : Fin 2 → Fin 4 → ℝ := ![![(61288507044748451399/10133167335130000:ℝ), (799841220907871054417/50665836675650000:ℝ), (27446325392291300749/2026633467026000:ℝ), (61762008513734379/16213067736208:ℝ)], ![(816651930438314267/162130677362080:ℝ), (10577045339097782723/810653386810400:ℝ), (179561191978060973/16213067736208:ℝ), (49769412018541125/16213067736208:ℝ)]]
theorem admission09_09_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 9 =
 Record12518109.Bernstein.bsum 1 3 (398155296148329/15201903616000000:ℝ) admission09_09_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_09_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_09_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 9 := by
 rw [admission09_09_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_09_coefficients]
def admission09_10_coefficients : Fin 3 → Fin 4 → ℝ := ![![(304179599483768707/6541981247375:ℝ), (2243126028882657371/19625943742125:ℝ), (14291305895918935/157007549937:ℝ), (1217196737218015/52335849979:ℝ)], ![(4565591478967238/52335849979:ℝ), (33437425367394214/157007549937:ℝ), (26365777982848750/157007549937:ℝ), (2211905236438750/52335849979:ℝ)], ![(4199813710896375/104671699958:ℝ), (10155961645896375/104671699958:ℝ), (3948371210390625/52335849979:ℝ), (972172595390625/52335849979:ℝ)]]
theorem admission09_10_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 10 =
 Record12518109.Bernstein.bsum 2 3 (12443809221/3156377600000:ℝ) admission09_10_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_10_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_10_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 10 := by
 rw [admission09_10_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_10_coefficients]
def admission09_11_coefficients : Fin 2 → Fin 3 → ℝ := ![![(3691118570767152879/1809494166987500:ℝ), (118079225202376243/36189883339750:ℝ), (3692561956922659/2895190667180:ℝ)], ![(53525391975817551/28951906671800:ℝ), (424102407209218/144759533359:ℝ), (654480768181225/579038133436:ℝ)]]
theorem admission09_11_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 11 =
 Record12518109.Bernstein.bsum 1 2 (26179230727249/190023795200000:ℝ) admission09_11_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_11_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_11_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 11 := by
 rw [admission09_11_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_11_coefficients]
def admission09_12_coefficients : Fin 1 → Fin 1 → ℝ := ![![(74999/20000000:ℝ)]]
theorem admission09_12_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 12 =
 Record12518109.Bernstein.bsum 0 0 (74999/20000000:ℝ) admission09_12_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_12_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_12_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 12 := by
 rw [admission09_12_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_12_coefficients]
def admission09_13_coefficients : Fin 1 → Fin 1 → ℝ := ![![(755659947/40000000000:ℝ)]]
theorem admission09_13_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 13 =
 Record12518109.Bernstein.bsum 0 0 (755659947/40000000000:ℝ) admission09_13_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_13_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_13_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 13 := by
 rw [admission09_13_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_13_coefficients]
def admission09_14_coefficients : Fin 1 → Fin 1 → ℝ := ![![(1/2:ℝ)]]
theorem admission09_14_identity (δ p : ℝ) : admissionGuard .weakC7 δ p 14 =
 Record12518109.Bernstein.bsum 0 0 (1/2:ℝ) admission09_14_coefficients (397/1000:ℝ) (27/64:ℝ) (43/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission09_14_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission09_14_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .weakC7 δ p 14 := by
 rw [admission09_14_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission09_14_coefficients]
theorem admission09_all {δ p : ℝ} (hδ : δ ∈ Set.Icc (397/1000:ℝ) (27/64:ℝ))
 (hp : p ∈ Set.Icc (43/100:ℝ) (1/2:ℝ)) (j : Fin 15) : 0 < admissionGuard .weakC7 δ p j := by
 fin_cases j
 · exact admission09_00_pos hδ hp
 · exact admission09_01_pos hδ hp
 · exact admission09_02_pos hδ hp
 · exact admission09_03_pos hδ hp
 · exact admission09_04_pos hδ hp
 · exact admission09_05_pos hδ hp
 · exact admission09_06_pos hδ hp
 · exact admission09_07_pos hδ hp
 · exact admission09_08_pos hδ hp
 · exact admission09_09_pos hδ hp
 · exact admission09_10_pos hδ hp
 · exact admission09_11_pos hδ hp
 · exact admission09_12_pos hδ hp
 · exact admission09_13_pos hδ hp
 · exact admission09_14_pos hδ hp
end
end QRH.ArviDensity.Return
