#include <algorithm>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

struct Scanner {
  uint32_t limit;
  uint32_t cache_limit;
  std::vector<int8_t> mu;
  std::vector<uint32_t> lp;
  std::vector<uint32_t> primes;
  std::vector<double> s0_cache, slog_cache;
  long double s0 = 0.0L, slog = 0.0L, annular = 0.0L;

  explicit Scanner(uint32_t n): limit(n), cache_limit(n/67 + 8), mu(n+1), lp(n+1),
      s0_cache(cache_limit+1), slog_cache(cache_limit+1) {}

  void build_mu(){
    mu[1]=1;
    for(uint32_t i=2;i<=limit;i++){
      if(lp[i]==0){ lp[i]=i; primes.push_back(i); mu[i]=-1; }
      for(uint32_t p:primes){
        uint64_t v=(uint64_t)i*p; if(v>limit) break;
        lp[(uint32_t)v]=p;
        if(p==lp[i]){ mu[(uint32_t)v]=0; break; }
        mu[(uint32_t)v]=(int8_t)-mu[i];
      }
    }
    std::vector<uint32_t>().swap(lp);
    std::vector<uint32_t>().swap(primes);
  }

  int coeff(uint32_t n) const {
    int a=(n==1?6:0)-6*(int)mu[n];
    if((n&1u)==0) a+=9*(int)mu[n/2];
    if((n&3u)==0) a-=3*(int)mu[n/4];
    return a;
  }

  long double A_from_cache(long double x) const {
    if(x<=1.0L) return 0.0L;
    uint32_t hi=(uint32_t)std::floor(x);
    uint32_t lo=(uint32_t)std::floor(x/4.0L);
    if(hi>cache_limit) throw std::runtime_error("cache range exceeded");
    long double s0h=s0_cache[hi], s0l=s0_cache[lo];
    long double slh=slog_cache[hi], sll=slog_cache[lo];
    return std::log(4.0L)*s0l + std::log(x)*(s0h-s0l) - (slh-sll);
  }

  long double U67_cached(long double x) const {
    if(x<=1.0L) return 0.0L;
    return A_from_cache(x)/std::sqrt(x);
  }

  long double U71_from_cache(long double x) const {
    long double sum=0.0L, fac=1.0L;
    while(x>1.0L){ sum += fac*U67_cached(x); x/=67.0L; fac/=67.0L; }
    return sum;
  }

  int run(const std::string& out){
    build_mu();
    long double max_q=-std::numeric_limits<long double>::infinity();
    uint32_t argmax=0; long double best_child_u=0,best_parent_u=0;
    long double best_child_f=0,best_parent_f=0;
    uint64_t nonpositive_den=0;
    // annular at X=1 equals zero. Update coefficients and then advance annular X -> X+1.
    for(uint32_t y=1;y<=limit;y++){
      int a=coeff(y);
      long double w=(long double)a/std::sqrt((long double)y);
      s0 += w; slog += w*std::log((long double)y);
      if(y<=cache_limit){ s0_cache[y]=(double)s0; slog_cache[y]=(double)slog; }

      if(y>=67){
        long double u67_parent=annular/std::sqrt((long double)y);
        long double parent=u67_parent + U71_from_cache((long double)y/67.0L)/67.0L;
        long double child=U71_from_cache((long double)y/67.0L);
        if(parent<=0){ ++nonpositive_den; }
        else {
          long double q=child/parent;
          if(q>max_q){
            max_q=q; argmax=y; best_child_u=child; best_parent_u=parent;
            best_child_f=child*std::sqrt((long double)y/67.0L);
            best_parent_f=parent*std::sqrt((long double)y);
          }
        }
      }
      // derivative d/dlog X on cell (y,y+1) is current scalar prefix s0.
      annular += s0*std::log1p(1.0L/(long double)y);
    }
    std::ofstream f(out);
    f<<std::setprecision(18);
    f<<"{\n";
    f<<"  \"limit\": "<<limit<<",\n";
    f<<"  \"max_q67\": "<<(double)max_q<<",\n";
    f<<"  \"argmax_y\": "<<argmax<<",\n";
    f<<"  \"child_U71\": "<<(double)best_child_u<<",\n";
    f<<"  \"parent_U71\": "<<(double)best_parent_u<<",\n";
    f<<"  \"child_F71\": "<<(double)best_child_f<<",\n";
    f<<"  \"parent_F71\": "<<(double)best_parent_f<<",\n";
    f<<"  \"nonpositive_denominators\": "<<nonpositive_den<<",\n";
    f<<"  \"rh_established\": false,\n";
    f<<"  \"status\": \"FLOATING_RECONNAISSANCE_NONPROBATIVE\"\n";
    f<<"}\n";
    std::cout<<std::setprecision(18)<<"max_q67="<<(double)max_q<<" argmax="<<argmax
             <<" child_F71="<<(double)best_child_f<<" parent_F71="<<(double)best_parent_f
             <<" nonpositive_den="<<nonpositive_den<<"\n";
    return 0;
  }
};
int main(int argc,char**argv){
  uint32_t limit=100000000; std::string out="p67_ratio_scan.json";
  if(argc>1) limit=(uint32_t)std::stoul(argv[1]); if(argc>2) out=argv[2];
  try { Scanner s(limit); return s.run(out); } catch(const std::exception& e){ std::cerr<<e.what()<<"\n"; return 2; }
}
