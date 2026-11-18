// Independent inspection harness, not a search replay. The included author source is unchanged.
#define main author_reference_main
#include "verify.cpp"
#undef main
#include <iostream>
#include <fstream>
int main(int argc, char** argv) {
  if (argc != 3) return 2;
  std::ifstream pf(argv[1]); auto p=certificate::readParameters(pf); if(!p) return 3;
  auto c=certificate::makeCertificate(*p); if(!c) return 4;
  certificate::Potentials pot(*c);
  std::ifstream tf(argv[2],std::ios::binary);
  auto table=certificate::KernelTable::read(tf,p->gridLength,p->scale); if(!table) return 5;
  int n; std::cin>>n;
  for(int i=0;i<n;++i){
    std::size_t gap,type,base; certificate::Grid lo,hi,pos,first,last;
    std::cin>>gap>>type>>base>>lo>>hi>>pos>>first>>last;
    auto a=pot.affineBound(gap,type,lo,hi);
    std::cout<<pot.value(gap,type,pos)<<' '<<pot.minimum(gap,type,lo,hi)<<' '
      <<pot.minimumOfDifference(gap,type,base,lo,hi)<<' '<<a.slope<<' '<<a.offset<<' '
      <<table->minimum(first,last)<<'\n';
  }
}
