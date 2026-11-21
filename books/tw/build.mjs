import fs from 'fs';
import {build} from './geo.mjs';
import * as D from './data.mjs';
import {EVENTS} from './events.mjs';
import {WHY} from './links.mjs';
import {BOOKS,BK} from './books.mjs';
import {TERMS,TCATS} from './terms.mjs';
import {CONCL} from './concl.mjs';
const mods=await Promise.all([1,2,3,4].map(async n=>{const f='./body_p'+n+'.mjs',g='./part'+n+'.mjs';
  return {b:fs.existsSync(f)?(await import(f))['B'+n]:{},p:fs.existsSync(g)?(await import(g)):{}};}));
const BODY=Object.assign({},...mods.map(m=>m.b));
const PARTX=Object.fromEntries(mods.map((m,i)=>['p'+(i+1),m.p['P'+(i+1)]||null]));
const AXCH=Object.assign({},...mods.map((m,i)=>m.p['AXCH'+(i+1)]||{}));
const PEOPLE=[],FACTS=[],PDENY={};
const PY={p1:[1624,1874],p2:[1871,1945],p3:[1945,1986],p4:[1987,2026]};

const META={...D.META,guide:false,
 desc:'1624년 네덜란드 상관에서 2026년까지, 다스리는 이가 다섯 번 바뀐 섬이 오늘의 민주 대만이 되기까지를 20개의 분기점 사건으로 따라가는 대만사.',
 intro:[
 '이 책은 1624년 네덜란드 동인도회사가 대만 남부에 상관을 세운 때부터 2026년까지, 대만의 400년을 20개의 분기점 사건으로 따라갑니다. 그 사이 섬은 북부를 잠시 차지한 스페인을 빼면 네덜란드, 정씨 왕국, 청, 일본, 중화민국의 다섯 통치를 차례로 겪었고, 20세기 말에야 섬사람들이 스스로 지도자를 뽑는 민주주의가 되었습니다.',
 '제목의 ‘섬의 주인’은 이 책이 따라가는 물음입니다. 누가 이 섬을 다스렸는가, 그리고 섬에 사는 사람들은 언제 어떻게 자기 운명의 주인이 되려 했는가. 원주민의 섬은 바다를 건넌 이민의 섬이 되었고, 식민지와 계엄을 지나 스스로를 대만 사람이라 부르는 사회가 되었습니다.',
 '그래서 사건마다 배경과 전개를, 큰 사건은 원인과 주체까지 같은 틀로 적고, 그 사건이 섬의 다섯 겹, 곧 <b>주권·통치</b>, <b>정치 체제</b>, <b>경제</b>, <b>사회·종족</b>, <b>정체성·언어</b> 가운데 무엇을 바꾸었는지 기록합니다. 주요 장의 맨 앞에 둔 ‘먼저 알아 둘 것’이 처음 접하는 독자를 위해 시대와 인물을 풀어 주고, 점선 밑줄이 그어진 말을 누르면 용어 풀이가 뜹니다. 장의 끝에는 해석이 갈리는 지점과 흔한 오해를 따로 적었습니다.',
 '최근의 일은 널리 인정되는 사실과 원인을 중심으로 적고, 아직 진행 중인 일은 그렇다고 밝힙니다. 사람 이름은 신해혁명(1911) 이전에 세상을 떠난 사람은 한자음(정성공, 유명전)으로, 그 이후의 사람은 중국어 발음(장제스, 리덩후이)으로, 일본 사람은 일본어 발음(고토 신페이)으로 적습니다. 지명은 오늘 쓰이는 이름을 중국어 발음으로 적습니다(타이난, 가오슝).'],
 engines:'400년의 변화를 움직인 큰 힘은 셋이었습니다. 바다 건너에서 와서 섬을 다스린 권력, 바다를 건너온 이주민과 원주민이 만나고 다투고 섞인 흐름, 그리고 섬사람이 자기 일을 스스로 정하려 한 요구입니다. 세 힘은 시대마다 서로 얽혔습니다. 이 책의 주제는 그 힘들이 지나간 자리에서 섬과 사람들이 무엇이 되었는가입니다.'
};

// 개항장: [이름, 경도, 위도, 개항 연도, 근거]
const PORTS=[['단수이',121.44,25.17,1860,'톈진조약'],['안핑',120.16,23.0,1865,'톈진조약'],['지룽',121.74,25.13,1863,'단수이의 보조항'],['다거우',120.27,22.62,1864,'안핑의 보조항']];
const LEASES=[];
// 인물 등장 찾기: 본문과 같은 규칙(짧은 이름은 앞뒤가 한글 낱말이면 제외, 조사만 허용)
const HG=/[가-힣]/,PTC=/^(?:으로서|으로써|으로|로서|로써|에서|에게서|에게|한테|까지|부터|처럼|보다|마다|조차|이나|이라는|이라|라는|이었다|이었|이며|이고|이자|이다|였다|였|에는|은|는|이|가|을|를|의|에|와|과|로|도|만|들|께|라|란|인)+(?![가-힣])/;
const NAMES=[['\u0000none','']];PEOPLE.forEach(p=>[p.n,...(p.al||[])].forEach(n=>NAMES.push([n,p.id])));NAMES.sort((a,b)=>b[0].length-a[0].length);
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
const groups=[];
const parts=D.PARTS.map(p=>({...p,y0:PY[p.id][0],y1:PY[p.id][1],...(PARTX[p.id]||{})}));
const regions=D.REGIONS.map(r=>({...r,xy:P(r.lon,r.lat)}));
const seas=[['대만 해협',119.75,23.35],['바시 해협',120.9,21.85],['동중국해',122.2,26.05],['태평양',122.35,22.9]].map(([n,lo,la])=>({n,xy:P(lo,la)}));
{const errs=[];JSON.stringify(CONCL).replace(/\[\[(\w+)\]\]/g,(m,x)=>{if(!ids.has(x))errs.push('conclref '+x);});
 for(const k of Object.keys(AXCH))if(!ids.has(k))errs.push('axch '+k);
 for(const p of Object.values(PARTX))if(p)JSON.stringify(p).replace(/\[\[(\w+)\]\]/g,(m,x)=>{if(!ids.has(x))errs.push('partref '+x);});
 if(errs.length){console.error(errs);process.exit(1);}}
const lineage=[],LCATS=[];
const DATA={meta:META,why:WHY,concl:CONCL,body:BODY,W:g.W,H:g.H,land:g.land,grat:g.grat,borders:g.borders,prov:g.prov,rivers:g.rivers,lakes:g.lakes||'',
 regions,seas,people,facts:FACTS,pdeny:PDENY,axes:D.AXES,engines:D.ENGINES,parts,events,groups,books:BOOKS,terms:TERMS,tcats:TCATS,lineage,lcats:LCATS,
 threads:[],
 ports:PORTS.map(([n,lo,la,y,d])=>({n,y,d,xy:P(lo,la)})),leases:LEASES.map(([n,lo,la,y,until,who])=>({n,y,until,who,xy:P(lo,la)}))};

let html=fs.readFileSync('template.html','utf8');
html=html.replace('/*__DATA__*/',()=>'const DATA='+JSON.stringify(DATA)+';').replaceAll('__TITLE__',META.title).replaceAll('__SUB__',META.sub).replaceAll('__DESC__',META.desc);
fs.mkdirSync('dist',{recursive:true});
fs.writeFileSync('dist/index.html',html);
const strip=s=>String(s).replace(/\s/g,'');
const bc=Object.fromEntries(Object.entries(BODY).map(([k,v])=>[k,Object.values(v).flat().join('').length]));
console.log('ok',(html.length/1024).toFixed(0)+'KB','H='+g.H,bc);
