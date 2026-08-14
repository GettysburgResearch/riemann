#include <bits/stdc++.h>
using namespace std; vector<int> basep={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
int main(){int JMAX=5000,RMAX=100000;int XMAX=JMAX*RMAX; // cannot arrays huge
 // Instead sample ratios and compute harmonic prefixes per max N? use ratio formula scaled j, N up to 2e6 cap
 int NMAX=3000000; vector<long double> inv(NMAX+3),lg(NMAX+3),prefI(NMAX+3),prefL(NMAX+3);
 for(int m=1;m<=NMAX+2;m++){inv[m]=1/sqrtl((long double)m);lg[m]=logl((long double)m);prefI[m]=prefI[m-1]+inv[m];prefL[m]=prefL[m-1]+inv[m]*lg[m];}
 vector<int> testp={67,71,83,127,251,509,1009,5003};
 mt19937_64 gen(1234567);long double mn=1e100;tuple<int,int,int> arg;long long neg=0;
 for(int it=0;it<1000000;it++){
  int p=testp[gen()%testp.size()]; int j=2+gen()%2000; int ratio=1+gen()%1500; int N=min(NMAX-2,j*ratio+(int)(gen()%j)); if(N<=j)N=j+1;
  vector<int> ps=basep;ps.push_back(p);sort(ps.begin(),ps.end());vector<pair<int,int>> ds={{1,1}};int maxd=N/j;
  for(int q:ps){int z=ds.size();for(int i=0;i<z;i++)if(1LL*ds[i].first*q<=maxd)ds.push_back({ds[i].first*q,-ds[i].second});}sort(ds.begin(),ds.end());
  long double A=(long double)(j+1)/(j-1),B=-(long double)(j+1)*(j-2)/(j*(j-1)),C=2.0L/(j*(j-1)),D=0,logN=lg[N];
  for(auto [d,mu]:ds){int M=N/d;long double logY=logN-lg[d],qv=A*inv[j]*(logY-lg[j]);if(M>=j+1)qv+=B*inv[j+1]*(logY-lg[j+1]);if(M>=j+2)qv+=C*(logY*(prefI[M]-prefI[j+1])-(prefL[M]-prefL[j+1]));D+=mu*inv[d]*qv;}
  if(D<mn){mn=D;arg={p,j,N};}if(D<-1e-12){neg++;cerr<<"NEG "<<p<<" "<<j<<" "<<N<<" "<<(double)D<<"\n";break;}
 }
 auto [p,j,N]=arg;cout<<setprecision(20)<<"neg="<<neg<<" min="<<mn<<" p="<<p<<" j="<<j<<" N="<<N<<" ratio="<<(long double)N/j<<"\n";
}
