// Exhaustive six-dimensional proof from directed point and cell enclosures.
// Floating point: IEC559 binary64, round-to-nearest, no contraction/fast-math.
#include <array>
#include <vector>
#include <cmath>
#include <cfenv>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <limits>
#include <cstdint>
#include <algorithm>
#include <stdexcept>
#ifdef __FAST_MATH__
#error "Fast math is not allowed in the accepting calculation."
#endif
struct Box {std::array<int,6> lo,hi;};
double down(double x){return std::nextafter(x,-INFINITY);}
double up(double x){return std::nextafter(x,INFINITY);}
struct I{double l,h;I(double x=0):l(x),h(x){} I(double a,double b):l(a),h(b){}};
I operator+(I a,I b){return I(down(a.l+b.l),up(a.h+b.h));}
I operator-(I a,I b){return I(down(a.l-b.h),up(a.h-b.l));}
I operator*(I a,I b){double v[4]={a.l*b.l,a.l*b.h,a.h*b.l,a.h*b.h};return I(down(*std::min_element(v,v+4)),up(*std::max_element(v,v+4)));}
I operator/(I a,I b){if(b.l<=0&&b.h>=0)throw std::runtime_error("interval zero divisor");return a*I(down(1/b.h),up(1/b.l));}
I square(I a){if(a.l>=0)return I(std::max(0.,down(a.l*a.l)),up(a.h*a.h));if(a.h<=0)return I(std::max(0.,down(a.h*a.h)),up(a.l*a.l));return I(0,up(std::max(a.l*a.l,a.h*a.h)));}
I rat(int64_t n,int64_t d){double x=double(n)/double(d);return I(down(x),up(x));}
struct RangeMin{std::vector<int>lg;std::vector<std::vector<double>>sp;int len;double outside;
 RangeMin(std::vector<double>v,double o):len(v.size()),outside(o){lg.assign(len+1,0);for(int i=2;i<=len;i++)lg[i]=lg[i/2]+1;sp.resize(lg[len]+1);sp[0]=std::move(v);for(int k=1;k<=lg[len];k++){int n=len-(1<<k)+1;sp[k].resize(n);for(int i=0;i<n;i++)sp[k][i]=std::min(sp[k-1][i],sp[k-1][i+(1<<(k-1))]);}}
 double query(int a,int b)const{if(a<0||b>=len||b<a)return outside;int k=lg[b-a+1];return std::min(sp[k][a],sp[k][b-(1<<k)+1]);}
};
double readnum(std::istream&f){std::string s;if(!(f>>s))throw std::runtime_error("truncated table");size_t p=0;double x=std::stod(s,&p);if(p!=s.size()||std::isnan(x))throw std::runtime_error("bad table number");return x;}
bool screen(double a[6][6]){double l[6][6]={},d[6]={};for(int k=0;k<6;k++){double p=a[k][k];for(int j=0;j<k;j++)p-=l[k][j]*l[k][j]*d[j];if(!(p>1e-13))return false;d[k]=p;for(int i=k+1;i<6;i++){double u=a[i][k];for(int j=0;j<k;j++)u-=l[i][j]*l[k][j]*d[j];l[i][k]=u/p;}}return true;}
uint64_t hash_state=1469598103934665603ULL;
void hash_u(uint64_t x){for(int i=0;i<8;i++){hash_state^=uint8_t(x);hash_state*=1099511628211ULL;x>>=8;}}
int integer_arg(const char* s){std::string t(s);if(t.empty()||t.find_first_not_of("0123456789")!=std::string::npos)throw std::runtime_error("bad integer argument");size_t p=0;int n=std::stoi(t,&p);if(p!=t.size())throw std::runtime_error("bad integer argument");return n;}
int main(int argc,char**argv){try{
 if(argc!=4&&argc!=5)throw std::runtime_error("usage: search_cert table target_num target_den [pressure_denominator]");
 int pressure_den=argc==5?integer_arg(argv[4]):3000; if(pressure_den<1000||pressure_den>10000)throw std::runtime_error("bad pressure denominator");
 if(!std::numeric_limits<double>::is_iec559||std::numeric_limits<double>::digits!=53||std::fegetround()!=FE_TONEAREST)throw std::runtime_error("unsupported floating environment");
 std::ifstream f(argv[1]);std::string magic;int grid,len,precision;f>>magic>>grid>>len>>precision;
 if(!f||magic!="MPFR_KERNEL_V1"||grid!=4000||len!=48016||(precision!=160&&precision!=256))throw std::runtime_error("unexpected table metadata");
 std::vector<std::array<I,2>> pt(2*len+1);
 for(auto &row:pt){double l=readnum(f),h=readnum(f),d=readnum(f),e=readnum(f);if(!(l<=h&&d<=e&&l>=0&&h<1.00001&&std::isfinite(d)&&std::isfinite(e)))throw std::runtime_error("bad point");row={I(l,h),I(d,e)};}
 std::vector<double>v(len),v2(len);
 for(int i=0;i<len;i++){v[i]=readnum(f);v2[i]=readnum(f);if(!(v[i]>=0&&v[i]<=1)||!((i<3800&&v2[i]==-INFINITY)||(i>=3800&&std::isfinite(v2[i]))))throw std::runtime_error("bad cell");}
 std::string extra;if(f>>extra)throw std::runtime_error("extra table bytes");
 int tn=integer_arg(argv[2]),td=integer_arg(argv[3]);if(tn<=0||tn>10000000||td<=0||td>1000000000)throw std::runtime_error("bad target");
 I targetI=rat(tn,td);double target=targetI.h;int cutoff=(int)((int64_t(tn)*pressure_den*grid+td-1)/td);
 if(cutoff+6>len||cutoff<1)throw std::runtime_error("table too short");
 RangeMin rm(v,0.0),rm2(v2,-INFINITY);I cc[7];for(int r=1;r<=6;r++)cc[r]=rat(2,7-r);
 std::vector<std::pair<int,int>>cmp;
 for(int i=0;i<cutoff;i++){double d=(rat(i,int64_t(grid)*pressure_den)+cc[1]*I(v[i])).l;if(d<target){if(cmp.empty()||cmp.back().second<i-1)cmp.push_back({i,i});else cmp.back().second=i;}}
 if(cmp.size()>10)throw std::runtime_error("too many initial components");
 std::cerr<<"components "<<cmp.size()<<":";for(auto p:cmp)std::cerr<<" ["<<p.first<<","<<p.second<<"]";std::cerr<<"\n";
 uint64_t htests=0,hpd=0;
 auto convex=[&](const Box&b,const int*lp,const int*hp)->double{
  double mat[6][6]={};std::array<std::array<I,6>,6>A{};
  for(int r=1;r<=6;r++)for(int j=0;j<=6-r;j++){
   double d2=rm2.query(lp[j+r]-lp[j],hp[j+r]-hp[j]+r-1);if(!std::isfinite(d2))return -INFINITY;
   double c=(cc[r]*I(d2)).l; // EXACT chosen binary rational coefficient <= actual one
   for(int ii=j;ii<j+r;ii++)for(int jj=j;jj<j+r;jj++){mat[ii][jj]+=c;A[ii][jj]=A[ii][jj]+I(c);}
  }
  if(!screen(mat))return -INFINITY;htests++;
  I L[6][6],D[6];
  for(int k=0;k<6;k++){
   I p=A[k][k];for(int j=0;j<k;j++)p=p-square(L[k][j])*D[j];if(!(p.l>0))return -INFINITY;D[k]=p;
   for(int i=k+1;i<6;i++){I a=A[i][k];for(int j=0;j<k;j++)a=a-L[i][j]*L[k][j]*D[j];L[i][k]=a/D[k];}
  }hpd++;
  int mp[7]={0};for(int j=0;j<6;j++)mp[j+1]=mp[j]+b.lo[j]+b.hi[j]+1;
  I value=rat(mp[6],int64_t(2)*grid*pressure_den),gradient[6];for(auto &g:gradient)g=rat(1,pressure_den);
  for(int r=1;r<=6;r++)for(int j=0;j<=6-r;j++){
   int index=mp[j+r]-mp[j];if(index<0||index>2*len)return -INFINITY;
   value=value+cc[r]*pt[index][0];I gd=cc[r]*pt[index][1];for(int i=j;i<j+r;i++)gradient[i]=gradient[i]+gd;
  }
  I t[6],quadratic;
  for(int i=0;i<6;i++){t[i]=gradient[i];for(int j=0;j<i;j++)t[i]=t[i]-L[i][j]*t[j];quadratic=quadratic+square(t[i])/D[i];}
  double lower=(value-I(.5)*quadratic).l;
  // Also use the convex tangent on the actual box.
  I tangent=value;for(int i=0;i<6;i++){double ab=std::max(std::abs(gradient[i].l),std::abs(gradient[i].h));tangent=tangent-I(ab)*rat(b.hi[i]-b.lo[i]+1,2*grid);}
  return std::max(lower,tangent.l);
 };
 std::vector<Box>stack;Box root;auto fill=[&](auto&&self,int j)->void{if(j==6){stack.push_back(root);return;}for(auto p:cmp){root.lo[j]=p.first;root.hi[j]=p.second;self(self,j+1);}};fill(fill,0);
 uint64_t initial=stack.size(),nodes=0,splits=0,leaves=0,pressure=0,interval=0,convex_leaves=0;size_t maxstack=stack.size();double minmargin=INFINITY;
 while(!stack.empty()){
  Box b=stack.back();stack.pop_back();nodes++;int lp[7]={0},hp[7]={0};for(int j=0;j<6;j++){lp[j+1]=lp[j]+b.lo[j];hp[j+1]=hp[j]+b.hi[j];hash_u(b.lo[j]);hash_u(b.hi[j]);}
  if(lp[6]>=cutoff){pressure++;leaves++;hash_u(1);continue;}
  double low=rat(lp[6],int64_t(grid)*pressure_den).l;
  for(int r=1;r<=6;r++)for(int j=0;j<=6-r;j++)low=down(low+(cc[r]*I(rm.query(lp[j+r]-lp[j],hp[j+r]-hp[j]+r-1))).l);
  if(low>=target){interval++;leaves++;hash_u(2);minmargin=std::min(minmargin,down(low-target));continue;}
  double cl=convex(b,lp,hp);if(cl>=target){convex_leaves++;leaves++;hash_u(3);minmargin=std::min(minmargin,down(cl-target));continue;}
  int jmax=0;for(int j=1;j<6;j++)if(b.hi[j]-b.lo[j]>b.hi[jmax]-b.lo[jmax])jmax=j;
  if(b.hi[jmax]==b.lo[jmax]){std::cerr<<"UNRESOLVED nodes="<<nodes<<" interval="<<std::setprecision(17)<<low<<" convex="<<cl<<" box=";for(int j=0;j<6;j++)std::cerr<<b.lo[j]<<",";std::cerr<<"\n";return 1;}
  hash_u(4);int mid=(b.lo[jmax]+b.hi[jmax])/2;Box b2=b;b.hi[jmax]=mid;b2.lo[jmax]=mid+1;stack.push_back(b);stack.push_back(b2);splits++;maxstack=std::max(maxstack,stack.size());
  if(nodes%1000000==0)std::cerr<<"nodes "<<nodes<<" stack "<<stack.size()<<" convex "<<convex_leaves<<"\n";
 }
 if(nodes!=initial+2*splits||leaves!=initial+splits||leaves!=pressure+interval+convex_leaves)throw std::runtime_error("coverage inconsistency");
 std::cout<<"{\"verified\":true,\"target_numerator\":"<<tn<<",\"target_denominator\":"<<td<<",\"pressure_denominator\":"<<pressure_den<<",\"grid\":"<<grid<<",\"cutoff_cells\":"<<cutoff<<",\"initial_boxes\":"<<initial<<",\"nodes\":"<<nodes<<",\"splits\":"<<splits<<",\"leaves\":"<<leaves<<",\"pressure_leaves\":"<<pressure<<",\"interval_leaves\":"<<interval<<",\"convex_leaves\":"<<convex_leaves<<",\"interval_ldl_tests\":"<<htests<<",\"interval_ldl_positive\":"<<hpd<<",\"max_stack\":"<<maxstack<<",\"traversal_fnv64\":\""<<std::hex<<hash_state<<std::dec<<"\",\"minimum_comparison_margin\":\""<<std::hexfloat<<minmargin<<"\"}\n";
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 2;}}
