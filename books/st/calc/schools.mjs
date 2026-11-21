// 학파 배분(SPEC '배분 점검'): 장마다 학파별로 이름이 나오는 문단 수. 한 문단에 여러 학파가 나오면 각각 센다.
// 분류는 이 장에서 그 사람이 낸 답의 자리다(인물 사전의 고정 진영과 같지 않을 수 있다).
import {B3A} from '../body_p3a.mjs';
import {isTable} from '../checks/_text.mjs';
const S={
 '베이즈(객관·주관)':['제프리스','린들리','에드워즈','새비지','콘필드','제임스 버거','버거·셀크','셀크','바야리','라우더','바허마커르스','로베르','스프렝어','케데인'],
 '가능도주의':['앤스컴','가능도 원리'],
 '피셔':['피셔'],
 '네이만–피어슨·오류 통계':['아미티지','네이만','스파노스','오류율'],
 '학파 밖·응답자':['바틀릿','카셀라','로저 버거','샌번','시먼스']
};
for(const [id,b] of Object.entries(B3A)){const ps=Object.values(b).flat().filter(p=>!isTable(p)&&!/^\$\$/.test(p.trim()));const c={};let any=0;
  for(const p of ps){let hit=false;for(const [k,ws] of Object.entries(S))if(ws.some(w=>p.includes(w))){c[k]=(c[k]||0)+1;hit=true;}if(hit)any++;}
  console.log(id,`문단 ${ps.length}, 학파 언급 문단 ${any}`,Object.entries(c).map(([k,n])=>`${k} ${n}(${(n/any*100).toFixed(0)}%)`).join(' / '));}
