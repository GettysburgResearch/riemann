// Ordinary long-double reconnaissance, not a directed or global certificate.
// Literal beta(n)=mu(n)-1_{67|n}mu(n/67); H_1(x)=4sqrt(x)A(x)-3B(x).
#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>
struct Kahan {
  long double value=0, error=0;
  void add(long double x) { const auto y=x-error; const auto t=value+y;
    error=(t-value)-y; value=t; }
};
int main(int argc,char** argv) {
  const uint64_t requested=argc>1?std::strtoull(argv[1],nullptr,10):100000000;
  if(requested<2 || requested>1000000000ULL) return 2;
  const uint32_t limit=static_cast<uint32_t>(requested);
  const auto begin=std::chrono::steady_clock::now();
  std::vector<int8_t> mu(limit+1); std::vector<uint8_t> composite(limit+1);
  std::vector<uint32_t> primes; mu[1]=1;
  for(uint32_t i=2;i<=limit;++i) {
    if(!composite[i]) { primes.push_back(i); mu[i]=-1; }
    for(const auto p:primes) {
      const uint64_t product=uint64_t(i)*p; if(product>limit) break;
      composite[product]=1;
      if(i%p==0) { mu[product]=0; break; }
      mu[product]=-mu[i];
    }
  }
  Kahan A,B,mass; long double minimum=std::numeric_limits<long double>::infinity();
  long double min_x=0; uint64_t negative_intervals=0; bool first=true;
  std::cout<<std::setprecision(21);
  std::cout<<"{\n\"arithmetic\":\"ORDINARY_LONG_DOUBLE_KAHAN_RECONNAISSANCE\",\n"
    <<"\"source\":\"mu(n)-1_{67|n}mu(n/67)\",\n\"limit\":"<<limit<<",\n\"blocks\":[\n";
  uint64_t next_report=10;
  for(uint32_t n=1;n<limit;++n) {
    const int beta=int(mu[n])-(n%67==0?int(mu[n/67]):0);
    const long double root=std::sqrt((long double)n), next_root=std::sqrt((long double)n+1);
    A.add((long double)beta/n); B.add(beta/root);
    const auto a=4*A.value,b=3*B.value;
    const auto left=a*root-b, right=a*next_root-b;
    if(left<minimum) {minimum=left; min_x=n;}
    if(right<minimum) {minimum=right; min_x=(long double)n+1;}
    if(std::min(left,right)<0) {
      ++negative_intervals; long double low=n,high=(long double)n+1;
      if(left*right<0 && a!=0) {
        const long double crossing=(b/a)*(b/a);
        if(a>0) high=std::clamp(crossing,low,high); else low=std::clamp(crossing,low,high);
      }
      const auto length=high-low;
      const auto integral=b*std::log1p(length/low)-2*a*length/(std::sqrt(high)+std::sqrt(low));
      mass.add(integral);
    }
    if(uint64_t(n)+1==next_report || n+1==limit) {
      if(!first) std::cout<<",\n"; first=false;
      std::cout<<"{\"endpoint\":"<<n+1<<",\"H_left\":"<<right<<",\"prefix_A\":"<<A.value
        <<",\"prefix_B\":"<<B.value<<",\"minimum\":"<<minimum<<",\"minimum_endpoint\":"<<min_x
        <<",\"negative_intervals\":"<<negative_intervals<<",\"negative_mass\":"<<mass.value<<"}";
      next_report*=10;
    }
  }
  const auto seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-begin).count();
  std::cout<<"\n],\n\"elapsed_seconds\":"<<seconds<<",\n\"prime_count\":"<<primes.size()
    <<",\n\"directed_certification\":false,\n\"rh_proved\":false\n}\n";
}
