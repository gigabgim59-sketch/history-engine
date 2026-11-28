// 책 안 일관성 검사: node checks/consistency.mjs [dist/index.html]
// 같은 대상(저작 『』「」, '연도+이름+헌법·조약…')이 장마다 다른 연도(3년 이내 차이)로 쓰였거나,
// 장 요약(s)의 연도가 그 장 본문에 없는 경우를 보고한다. 판단은 사람(또는 검수자)이 한다.
import {loadData,flat} from './_data.mjs';
const {D}=loadData(process.argv[2]||'dist/index.html');
const seen={};const add=(key,y,where)=>{(seen[key]=seen[key]||[]).push([+y,where]);};
const KIND='헌법|조약|선언|협정|회의|칙령|법|강화|협약|공의회|헌장|선거';
for(const e of D.events){const b=D.body[e.id];if(!b)continue;const t=flat(b)+' '+(e.s||'');
  for(const m of t.matchAll(/(\d{3,4})년[^.。]{0,25}?([『「][^』」]{2,30}[』」])/g))add(m[2],m[1],e.id);
  for(const m of t.matchAll(/([『「][^』」]{2,30}[』」])\s*\((\d{3,4})/g))add(m[1],m[2],e.id);
  for(const m of t.matchAll(new RegExp('(\\d{3,4})년(?:의)? ((?:[가-힣]{2,8} ){0,1}[가-힣]{2,8} ?(?:'+KIND+'))(?![가-힣])','g')))add(m[2].replace(/\s+/g,' '),m[1],e.id);}
const rep=[];
for(const [k,l] of Object.entries(seen)){const ys=[...new Set(l.map(x=>x[0]))];if(ys.length<2)continue;
  const lo=Math.min(...ys),hi=Math.max(...ys);if(hi-lo>3)continue;
  rep.push(`${k}: `+ys.map(y=>`${y}(${[...new Set(l.filter(x=>x[0]===y).map(x=>x[1]))].join(',')})`).join(' / '));}
const sum=[];
for(const e of D.events){const b=D.body[e.id];if(!b||!e.s)continue;const t=flat(b);
  for(const y of new Set((e.s.match(/\d{4}/g)||[])))if(!t.includes(y))sum.push(`${e.id}: 요약의 ${y}가 본문에 없음`);}
console.log(rep.length?`연도가 엇갈리는 대상 ${rep.length}건:\n`+rep.join('\n'):'연도 엇갈림 없음');
if(sum.length)console.log(`요약↔본문 ${sum.length}건:\n`+sum.join('\n'));
