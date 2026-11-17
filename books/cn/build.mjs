import fs from 'fs';
import {build} from './geo.mjs';
import * as D from './data.mjs';
import {EVENTS} from './events.mjs';
import {WHY} from './links.mjs';
import {BODY1} from './body_p1.mjs';
import {P1,GROUP_CH1,AXCH1} from './part1.mjs';
import {BOOKS,BK} from './books.mjs';
import {TERMS,TCATS} from './terms.mjs';
import {PEOPLE as PEOPLE1,FACTS,PDENY as PDENY1} from './people.mjs';
import {PEOPLE2,AT2,REL2,PDENY2} from './people_p2.mjs';
import {B2A} from './body_p2a.mjs';
import {B2B} from './body_p2b.mjs';
import {P2,GROUP_CH2,AXCH2} from './part2.mjs';
import {PEOPLE3,AT3,REL3,PDENY3} from './people_p3.mjs';
import {B3A} from './body_p3a.mjs';
import {B3B} from './body_p3b.mjs';
import {P3,GROUP_CH3,AXCH3} from './part3.mjs';
import {PEOPLE4,AT4,REL4,PDENY4} from './people_p4.mjs';
import {B4A} from './body_p4a.mjs';
import {B4B} from './body_p4b.mjs';
import {P4,GROUP_CH4,AXCH4} from './part4.mjs';
import {PEOPLE5,AT5,REL5,PDENY5} from './people_p5.mjs';
import {B5A} from './body_p5a.mjs';
import {B5B} from './body_p5b.mjs';
import {P5,GROUP_CH5,AXCH5} from './part5.mjs';
import {PEOPLE6,AT6,REL6,PDENY6} from './people_p6.mjs';
import {B6A} from './body_p6a.mjs';
import {B6B} from './body_p6b.mjs';
import {P6,GROUP_CH6,AXCH6} from './part6.mjs';
import {CONCL} from './concl.mjs';
import {LCATS,LINEAGE} from './lineage.mjs';
import {LNB1} from './lnb1.mjs';
import {LNB2} from './lnb2.mjs';
import {LNB3} from './lnb3.mjs';

const BODY={...BODY1,...B2A,...B2B,...B3A,...B3B,...B4A,...B4B,...B5A,...B5B,...B6A,...B6B};
const PARTX={p1:P1,p2:P2,p3:P3,p4:P4,p5:P5,p6:P6};
const GROUP_CH=[GROUP_CH1,GROUP_CH2,GROUP_CH3,GROUP_CH4,GROUP_CH5,GROUP_CH6];
const AXCH={...AXCH1,...AXCH2,...AXCH3,...AXCH4,...AXCH5,...AXCH6};
// 인물: 부마다 새 인물과 기존 인물의 행적을 합친다
const PDENY={...PDENY1,...PDENY2,...PDENY3,...PDENY4,...PDENY5,...PDENY6};
const ATS=[AT2,AT3,AT4,AT5,AT6],RELS=[REL2,REL3,REL4,REL5,REL6];
const PEOPLE0=[...PEOPLE1,...PEOPLE2,...PEOPLE3,...PEOPLE4,...PEOPLE5,...PEOPLE6];
const PEOPLE=PEOPLE0.map(p=>{const at={...(p.at||{})};ATS.forEach(A=>Object.assign(at,A[p.id]||{}));
  const rel=[...(p.rel||[])];RELS.forEach(R=>(R[p.id]||[]).forEach(r=>{if(!rel.some(([x])=>x===r[0]))rel.push(r);}));
  const o={...p,at,rel};const keys=Object.keys(at).sort();o.at=Object.fromEntries(keys.map(k=>[k,at[k]]));return o;});
{const seen=new Set(),ns=new Set();for(const p of PEOPLE){if(seen.has(p.id)||ns.has(p.n))throw new Error('dup person '+p.id+p.n);seen.add(p.id);ns.add(p.n);}
 for(const A of [...ATS,...RELS])for(const k of Object.keys(A))if(!seen.has(k))throw new Error('AT/REL '+k);}
const PY={p1:[1840,1864],p2:[1861,1901],p3:[1901,1927],p4:[1927,1949],p5:[1949,1976],p6:[1976,2026]};

const META={...D.META,guide:true,
 desc:'1840년 아편전쟁에서 2026년까지, 청 제국이 오늘의 중국이 되는 길을 60개의 분기점 사건으로 따라가며 주권·정치 체제·경제·사회·이념의 다섯 겹이 어떻게 바뀌었는지 읽는 중국 근현대사.',
 intro:[
 '이 책은 1840년 아편전쟁에서 2026년까지, 청 제국이 오늘의 중국이 되기까지의 길을 60개의 분기점 사건으로 따라갑니다. 그 길에서 중국은 황제를 잃고 공화국을 세웠으며, 군벌과 내전과 외국의 침략을 지나 공산당의 국가가 되었고, 다시 시장경제로 세계 2위의 경제 대국이 되었습니다.',
 '제목의 ‘천하’는 청 황제가 다스린다고 여긴 문명 세계를, ‘국가’는 국경과 조약과 국민으로 이루어진 근대의 나라를 가리킵니다. 1840년의 청은 천하의 중심을 자처한 다민족 제국이었고, 오늘의 중국은 그 제국의 영토 대부분을 이어받은 국민국가입니다. 이 책은 그 사이에서 무엇이 버려지고 무엇이 이어졌는지를 묻습니다.',
 '그래서 사건마다 배경과 원인과 주체와 전개를 같은 틀로 적고, 그 사건이 국가의 다섯 겹, 곧 <b>주권·영토</b>, <b>정치 체제</b>, <b>경제</b>, <b>사회</b>, <b>이념</b> 가운데 무엇을 바꾸었는지 기록합니다. 장마다 맨 앞의 ‘먼저 알아 둘 것’이 처음 접하는 독자를 위해 시대와 인물을 풀어 주고, 점선 밑줄이 그어진 말을 누르면 용어 풀이가 뜹니다. 장의 끝에는 학자들의 해석이 갈리는 지점과 흔한 오해를 따로 적었습니다.',
 '최근의 일은 널리 인정되는 사실과 원인을 중심으로 적고, 아직 진행 중인 일은 그렇다고 밝힙니다. 사람 이름은 신해혁명 이전에 세상을 떠난 사람은 한자음(임칙서, 증국번)으로, 그 이후의 사람은 중국어 발음(쑨원, 마오쩌둥)으로 적습니다. 지명은 오늘 쓰이는 이름을 중국어 발음으로 적습니다.'],
 engines:'186년의 변화를 움직인 큰 힘은 셋이었습니다. 바깥에서 밀려온 열강과 세계 시장과 전쟁, 아래에서 체제를 갈아엎으려 한 혁명, 그리고 위에서 나라를 다시 짜려 한 국가 건설입니다. 세 힘은 시대마다 서로 부딪치고 얽혔습니다. 이 책의 주제는 세 힘 자체가 아니라, 그 힘들이 지나간 자리에서 국가와 사람들이 무엇이 되었는가입니다.'
};

// 개항장: [이름, 경도, 위도, 개항 연도, 근거]
const PORTS=[
 ['광저우',113.26,23.13,1842,'난징조약'],['샤먼',118.08,24.48,1842,'난징조약'],['푸저우',119.30,26.08,1842,'난징조약'],['닝보',121.55,29.87,1842,'난징조약'],['상하이',121.47,31.23,1843,'난징조약'],
 ['잉커우(뉴좡)',122.23,40.67,1858,'톈진조약'],['옌타이(덩저우)',121.39,37.54,1858,'톈진조약'],['타이난',120.20,23.00,1858,'톈진조약'],['단수이',121.44,25.17,1858,'톈진조약'],['산터우',116.68,23.35,1858,'톈진조약'],['하이커우(충저우)',110.35,20.03,1858,'톈진조약'],
 ['한커우',114.27,30.58,1858,'톈진조약'],['주장',115.99,29.71,1858,'톈진조약'],['전장',119.45,32.20,1858,'톈진조약'],['톈진',117.20,39.13,1860,'베이징조약'],
 ['이창',111.29,30.69,1876,'즈푸조약'],['우후',118.38,31.33,1876,'즈푸조약'],['원저우',120.67,28.00,1876,'즈푸조약'],['베이하이',109.12,21.48,1876,'즈푸조약'],
 ['충칭',106.55,29.56,1891,'즈푸조약 추가 조항'],['사스',112.24,30.32,1895,'시모노세키조약'],['쑤저우',120.62,31.30,1895,'시모노세키조약'],['항저우',120.16,30.27,1895,'시모노세키조약']
];
// 조차지·할양지: [이름, 경도, 위도, 시작, 끝, 누가]
const LEASES=[
 ['홍콩섬',114.17,22.28,1842,1997,'영국'],['주룽',114.18,22.32,1860,1997,'영국'],['마카오',113.54,22.19,1887,1999,'포르투갈'],
 ['대만',121.0,23.7,1895,1945,'일본'],['자오저우만',120.30,36.07,1898,1914,'독일'],['뤼순·다롄',121.60,38.95,1898,1945,'러시아→일본'],
 ['웨이하이웨이',122.12,37.50,1898,1930,'영국'],['신계',114.10,22.45,1898,1997,'영국'],['광저우만',110.40,21.20,1898,1945,'프랑스']
];
const THREAD_EV={sov:['c01','c02','c05','c06','c14','c15','c17','c20','c24','c26','c30','c38','c50','c56'],
 rev:['c03','c04','c21','c22','c27','c28','c29','c31','c33','c37','c40','c41','c49','c54'],
 mod:['c07','c08','c09','c16','c19','c30','c45','c47','c52','c53','c55','c57','c58'],
 fr:['c06','c10','c11','c13','c23','c39','c42','c44','c48','c59','c60']};

// 인물 등장 찾기: 본문과 같은 규칙(짧은 이름은 앞뒤가 한글 낱말이면 제외, 조사만 허용)
const HG=/[가-힣]/,PTC=/^(?:으로서|으로써|으로|로서|로써|에서|에게서|에게|한테|까지|부터|처럼|보다|마다|조차|이나|이라는|이라|라는|이었다|이었|이며|이고|이자|이다|였다|였|에는|은|는|이|가|을|를|의|에|와|과|로|도|만|들|께|라|란|인)+(?![가-힣])/;
const NAMES=[];PEOPLE.forEach(p=>[p.n,...(p.al||[])].forEach(n=>NAMES.push([n,p.id])));NAMES.sort((a,b)=>b[0].length-a[0].length);
const PRE=new RegExp('('+NAMES.map(x=>x[0].replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('|')+')','g');
const PID=Object.fromEntries(NAMES);
const PD=Object.fromEntries(Object.entries(PDENY).map(([k,[l,r]])=>[k,[l&&new RegExp(l),r&&new RegExp(r)]]));
function mentions(text){const out=[];text.replace(PRE,(m,_g,off,str)=>{const pv=str[off-1]||'',nx=str.slice(off+m.length);
  if(m.length<=3){if(pv&&HG.test(pv))return m;if(nx&&HG.test(nx[0])&&!PTC.test(nx))return m;}
  const dn=PD[m];if(dn){const L=str.slice(Math.max(0,off-16),off);if((dn[0]&&dn[0].test(L))||(dn[1]&&dn[1].test(nx)))return m;}
  if(!out.includes(PID[m]))out.push(PID[m]);return m;});return out;}
const g=build();
const P=g.P;
// 점검
const ids=new Set(EVENTS.map(e=>e.id)),err=[];
EVENTS.forEach(e=>{e.nx.forEach(x=>{if(!ids.has(x))err.push('nx '+e.id+x);if(!WHY[e.id+'>'+x])err.push('why '+e.id+'>'+x);});});
Object.keys(WHY).forEach(k=>{const [a,b]=k.split('>');if(!EVENTS.find(e=>e.id===a)?.nx.includes(b))err.push('why extra '+k);});
Object.entries(BK).forEach(([e,l])=>l.forEach(([b])=>{if(!BOOKS.find(x=>x.id===b))err.push('book '+e+b);}));
Object.entries(BODY).forEach(([k,v])=>{if(!ids.has(k))err.push('body '+k);JSON.stringify(v).replace(/\[\[(\w+)\]\]/g,(m,x)=>{if(!ids.has(x))err.push('ref '+k+x);});});
if(err.length){console.error(err);process.exit(1);}

const groups0={};
const events=EVENTS.map((e,i)=>{const [x,y]=P(e.pl[1],e.pl[2]);const txt=[e.s,e.q,...(BODY[e.id]?Object.values(BODY[e.id]).flat():[])].join('\n');
  const pp=mentions(txt);PEOPLE.forEach(p=>{if(p.at&&p.at[e.id]&&!pp.includes(p.id))pp.push(p.id);});
  return {...e,no:i+1,mx:x,my:y,bk:BK[e.id]||[],axc:AXCH[e.id]||[],pp};});
const people=PEOPLE.map(p=>({...p,ch:events.filter(e=>e.pp.includes(p.id)).map(e=>e.id)}));
for(const p of PEOPLE)for(const c of Object.keys(p.at||{}))if(!ids.has(c))err.push('people at '+p.id+c);
for(const p of PEOPLE)for(const [r] of (p.rel||[]))if(!PEOPLE.find(q=>q.id===r))err.push('rel '+p.id+r);
if(err.length){console.error(err);process.exit(1);}
const groups=D.GROUPS.map(gr=>({...gr,ch:GROUP_CH.flatMap(m=>m[gr.id]||[])}));
const parts=D.PARTS.map(p=>({...p,y0:PY[p.id][0],y1:PY[p.id][1],...(PARTX[p.id]||{})}));
const regions=D.REGIONS.map(r=>({...r,xy:P(r.lon,r.lat)}));
const seas=[['황해',123.6,35.3],['동중국해',125.5,29.0],['남중국해',114.5,17.5],['동해',134.5,40.5]].map(([n,lo,la])=>({n,xy:P(lo,la)}));
const LNB={...LNB1,...LNB2,...LNB3};
const lineage=LINEAGE.map(l=>({...l,b:LNB[l.id]||null}));
{const errs=[];for(const l of lineage){if(!l.b)errs.push('no body '+l.id);for(const [c] of l.st)if(!ids.has(c))errs.push('ln '+l.id+c);
  JSON.stringify(l.b||'').replace(/\[\[(\w+)\]\]/g,(m,x)=>{if(!ids.has(x))errs.push('lnref '+l.id+x);});}
 JSON.stringify(CONCL).replace(/\[\[(\w+)\]\]/g,(m,x)=>{if(!ids.has(x))errs.push('conclref '+x);});
 if(errs.length){console.error(errs);process.exit(1);}}
const DATA={meta:META,why:WHY,concl:CONCL,body:BODY,W:g.W,H:g.H,land:g.land,grat:g.grat,borders:g.borders,prov:g.prov,rivers:g.rivers,lakes:g.lakes,
 regions,seas,people,facts:FACTS,pdeny:PDENY,axes:D.AXES,engines:D.ENGINES,parts,events,groups,books:BOOKS,terms:TERMS,tcats:TCATS,lineage,lcats:LCATS,
 threads:D.THREADS.map(t=>({...t,ev:THREAD_EV[t.id]})),
 ports:PORTS.map(([n,lo,la,y,d])=>({n,y,d,xy:P(lo,la)})),leases:LEASES.map(([n,lo,la,y,until,who])=>({n,y,until,who,xy:P(lo,la)}))};

let html=fs.readFileSync('template.html','utf8');
html=html.replace('/*__DATA__*/',()=>'const DATA='+JSON.stringify(DATA)+';').replaceAll('__TITLE__',META.title).replaceAll('__SUB__',META.sub).replaceAll('__DESC__',META.desc);
fs.mkdirSync('dist',{recursive:true});
fs.writeFileSync('dist/index.html',html);
const strip=s=>String(s).replace(/\s/g,'');
const bc=Object.fromEntries(Object.entries(BODY).map(([k,v])=>[k,Object.values(v).flat().join('').length]));
console.log('ok',(html.length/1024).toFixed(0)+'KB','H='+g.H,bc);
