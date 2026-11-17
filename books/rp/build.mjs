// 『공화국의 탄생』 빌드: node build.mjs → dist/index.html
import fs from 'fs';
import {build} from './geo.mjs';
import * as D from './data.mjs';
import {EVENTS} from './events.mjs';
import {WHY} from './links.mjs';
import {BOOKS,BK} from './books.mjs';
import {TERMS,TCATS} from './terms.mjs';
import {PEOPLE as PEOPLE1,FACTS,PDENY as PDENY1} from './people.mjs';
const opt=async(f)=>fs.existsSync(f)?await import('./'+f):{};
const NP=6;
const mods=[];
for(let n=1;n<=NP;n++){
  const bodies={};for(const f of fs.readdirSync('.').filter(f=>new RegExp('^body_p'+n+'[a-z]?\\.mjs$').test(f)).sort())Object.assign(bodies,...Object.values(await import('./'+f)));
  mods.push({b:bodies,p:await opt('part'+n+'.mjs'),pp:await opt('people_p'+n+'.mjs'),n});}
const CONCL=(await opt('concl.mjs')).CONCL||null;
const LN=await opt('lineage.mjs');const LNB=Object.assign({},...(await Promise.all([1,2,3].map(n=>opt('lnb'+n+'.mjs')))).map(m=>Object.values(m)[0]||{}));

const BODY=Object.assign({},...mods.map(m=>m.b));
const PARTX=Object.fromEntries(mods.map(m=>['p'+m.n,m.p['P'+m.n]||null]));
const GROUP_CH=mods.map(m=>m.p['GROUP_CH'+m.n]||{});
const AXCH=Object.assign({},...mods.map(m=>m.p['AXCH'+m.n]||{}));
const PDENY=Object.assign({},PDENY1,...mods.map(m=>m.pp['PDENY'+m.n]||{}));
const ATS=mods.map(m=>m.pp['AT'+m.n]||{}),RELS=mods.map(m=>m.pp['REL'+m.n]||{});
const PEOPLE0=[...PEOPLE1,...mods.flatMap(m=>m.pp['PEOPLE'+m.n]||[])];
const PEOPLE=PEOPLE0.map(p=>{const at={...(p.at||{})};ATS.forEach(A=>Object.assign(at,A[p.id]||{}));
  const rel=[...(p.rel||[])];RELS.forEach(R=>(R[p.id]||[]).forEach(r=>{if(!rel.some(([x])=>x===r[0]))rel.push(r);}));
  const o={...p,at,rel};const keys=Object.keys(at).sort();o.at=Object.fromEntries(keys.map(k=>[k,at[k]]));return o;});
{const seen=new Set(),ns=new Set();for(const p of PEOPLE){if(seen.has(p.id)||ns.has(p.n))throw new Error('dup person '+p.id+p.n);seen.add(p.id);ns.add(p.n);}
 for(const A of [...ATS,...RELS])for(const k of Object.keys(A))if(!seen.has(k))throw new Error('AT/REL '+k);}
const PY={p1:[1640,1788],p2:[1789,1799],p3:[1791,1815],p4:[1815,1847],p5:[1846,1852],p6:[1852,1875]};

const META={...D.META,guide:fs.existsSync('dist/guide.html'),
 desc:'계몽사상에서 1875년 제3공화정까지, 왕이 없는 나라라는 생각이 원리가 되고 조직을 얻고 혁명 속에서 헌법이 되어 유럽 곳곳에 퍼져 나간 길을 60개의 분기점 사건으로 따라가는 공화주의의 역사.',
 intro:[
 '이 책은 17세기 잉글랜드 공화국과 18세기 계몽사상에서 시작해 프랑스 혁명을 한가운데 두고, 1848년의 ‘민족의 봄’을 거쳐 1875년 프랑스 제3공화정의 성립까지 유럽 공화주의의 역사를 60개의 분기점 사건으로 따라갑니다. 그 사이 유럽은 공화국을 세웠다 잃기를 거듭했고, 마침내 공화정이 오래가는 체제가 되는 데 이르렀습니다.',
 '제목의 ‘공화국’은 왕이 아니라 시민이 주인인 나라, 법 아래에서 공공의 일을 함께 다스리는 나라를 뜻합니다. 그 생각은 로마와 피렌체의 기억에서 나와 계몽사상가들의 손에서 다듬어졌고, 클럽과 신문과 비밀결사로 조직되었으며, 재정 파탄과 기근과 전쟁의 위기 속에서 터져 나와 헌법이 되었습니다. 그리고 군대와 망명자와 모방을 타고 유럽 곳곳에 퍼지거나, 왕과 교회와 외국의 간섭에 되돌려졌습니다.',
 '그래서 장마다 그 사건이 이 ‘구체화의 다섯 고리’ 가운데 어디에 있는지 표시하고, 사건이 공화정의 다섯 겹, 곧 <b>주권</b>, <b>시민권</b>, <b>헌정 구조</b>, <b>자유와 권리</b>, <b>민족과 교회</b> 가운데 무엇을 바꾸었는지 기록합니다. 장마다 맨 앞의 ‘먼저 알아 둘 것’이 처음 접하는 독자를 위해 시대와 인물을 풀어 주고, 점선 밑줄이 그어진 말을 누르면 용어 풀이가 뜹니다. 장의 끝에는 해석이 갈리는 지점과 흔한 오해를 따로 적었습니다.',
 '사람 이름과 땅이름은 원어 발음을 국립국어원 외래어 표기법에 따라 적고, 나폴레옹·빈처럼 관용이 굳은 이름은 관용을 따릅니다. 이름을 누르면 원어 표기와 생몰년을 볼 수 있습니다. 프랑스 혁명의 날짜는 공화력 대신 오늘의 달력으로 적고, 테르미도르·브뤼메르처럼 사건의 이름이 된 달 이름만 그대로 씁니다.'],
 engines:'공화정은 한 번에 만들어지지 않았습니다. 이 책은 공화정이 생겨나고 퍼져 나간 과정을 다섯 고리로 나누어 봅니다. 원리와 개념과 상징의 <b>생각</b>, 그것을 함께 움직이는 조직으로 바꾸는 <b>결사</b>, 낡은 질서를 무너뜨리는 <b>위기</b>, 터져 나온 요구가 형태를 얻는 <b>제도</b>, 그리고 다른 나라로 퍼지거나 되돌려지는 <b>전파와 반동</b>입니다. 사건마다 이 고리들이 서로 다른 순서와 무게로 맞물렸고, 그 맞물림의 차이가 나라마다 공화정의 운명을 갈랐습니다.'
};

const PORTS=[],LEASES=[];
const THREAD_EV={sov:['r01','r02','r05','r09','r11','r14','r17','r22','r29','r41','r49','r52','r57','r60'],
 vote:['r08','r09','r15','r16','r18','r22','r29','r37','r39','r42','r50','r52','r55','r56','r60'],
 exp:['r07','r08','r23','r24','r25','r26','r27','r28','r31','r32','r35','r36','r37','r40','r44','r48','r49','r54','r56'],
 ord:['r10','r19','r20','r22','r29','r34','r35','r43','r46','r47','r50','r52','r58','r59']};

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
const ids=new Set(EVENTS.map(e=>e.id)),err=[];const EG=new Set(D.ENGINES.map(x=>x[0]));
EVENTS.forEach(e=>{e.nx.forEach(x=>{if(!ids.has(x))err.push('nx '+e.id+x);if(!WHY[e.id+'>'+x])err.push('why '+e.id+'>'+x);});(e.g||[]).forEach(x=>{if(!EG.has(x))err.push('g '+e.id+x);});});
Object.keys(WHY).forEach(k=>{const [a,b]=k.split('>');if(!EVENTS.find(e=>e.id===a)?.nx.includes(b))err.push('why extra '+k);});
Object.entries(BK).forEach(([e,l])=>l.forEach(([b])=>{if(!BOOKS.find(x=>x.id===b))err.push('book '+e+b);}));
Object.entries(BODY).forEach(([k,v])=>{if(!ids.has(k))err.push('body '+k);JSON.stringify(v).replace(/\[\[(\w+)\]\]/g,(m,x)=>{if(!ids.has(x))err.push('ref '+k+x);});});
for(const p of Object.values(PARTX))if(p)JSON.stringify(p).replace(/\[\[(\w+)\]\]/g,(m,x)=>{if(!ids.has(x))err.push('partref '+x);});
for(const k of Object.keys(AXCH))if(!ids.has(k))err.push('axch '+k);
for(const m of GROUP_CH)for(const [gid,l] of Object.entries(m)){if(!D.GROUPS.find(x=>x.id===gid))err.push('group '+gid);l.forEach(([c,a])=>{if(!ids.has(c))err.push('gch '+c);if(!D.AXES.find(x=>x.id===a))err.push('gax '+a);});}
if(CONCL)JSON.stringify(CONCL).replace(/\[\[(\w+)\]\]/g,(m,x)=>{if(!ids.has(x))err.push('conclref '+x);});
if(err.length){console.error(err);process.exit(1);}

const YC={};EVENTS.forEach(e=>{(YC[e.yr]=YC[e.yr]||[]).push(e.id);});
const YF=id=>{const e=EVENTS.find(x=>x.id===id),L=YC[e.yr];return L.length>1?e.yr+L.indexOf(id)/L.length*0.9:e.yr;};
const events=EVENTS.map((e,i)=>{const [x,y]=P(e.pl[1],e.pl[2]);const txt=[e.s,e.q,...(BODY[e.id]?Object.values(BODY[e.id]).flat():[])].join('\n');
  const pp=mentions(txt);PEOPLE.forEach(p=>{if(p.at&&p.at[e.id]&&!pp.includes(p.id))pp.push(p.id);});
  return {...e,yr:YF(e.id),no:i+1,mx:x,my:y,bk:BK[e.id]||[],axc:AXCH[e.id]||[],pp};});
const people=PEOPLE.map(p=>({...p,ch:events.filter(e=>e.pp.includes(p.id)).map(e=>e.id)}));
for(const p of PEOPLE)for(const c of Object.keys(p.at||{}))if(!ids.has(c))err.push('people at '+p.id+c);
for(const p of PEOPLE)for(const [r] of (p.rel||[]))if(!PEOPLE.find(q=>q.id===r))err.push('rel '+p.id+r);
if(err.length){console.error(err);process.exit(1);}
const groups=D.GROUPS.map(gr=>({...gr,ch:GROUP_CH.flatMap(m=>m[gr.id]||[])}));
const parts=D.PARTS.map(p=>({...p,y0:PY[p.id][0],y1:PY[p.id][1],...(PARTX[p.id]||{})}));
const regions=D.REGIONS.map(r=>({...r,xy:P(r.lon,r.lat)}));
const seas=[['대서양',-9.5,47.5],['북해',3.2,56.2],['지중해',5.5,38.6],['발트해',18.6,56.6],['아드리아해',15.3,43.3],['대서양 건너',-11.6,43.3]].map(([n,lo,la])=>({n,xy:P(lo,la)}));
const lineage=(LN.LINEAGE||[]).map(l=>({...l,b:LNB[l.id]||null}));
const DATA={meta:META,why:WHY,concl:CONCL,body:BODY,W:g.W,H:g.H,land:g.land,grat:g.grat,borders:g.borders,prov:g.prov,rivers:g.rivers,lakes:g.lakes,
 regions,seas,people,facts:FACTS,pdeny:PDENY,axes:D.AXES,engines:D.ENGINES,parts,events,groups,books:BOOKS,terms:TERMS,tcats:TCATS,lineage,lcats:LN.LCATS||[],
 threads:D.THREADS.map(t=>({...t,ev:THREAD_EV[t.id]||[]})),ports:[],leases:[]};

let html=fs.readFileSync('template.html','utf8');
html=html.replace('/*__DATA__*/',()=>'const DATA='+JSON.stringify(DATA)+';').replaceAll('__TITLE__',META.title).replaceAll('__SUB__',META.sub).replaceAll('__DESC__',META.desc);
fs.mkdirSync('dist',{recursive:true});
fs.writeFileSync('dist/index.html',html);
const bc=Object.fromEntries(Object.entries(BODY).map(([k,v])=>[k,Object.values(v).flat().join('').length]));
console.log('ok',(html.length/1024).toFixed(0)+'KB','H='+g.H,'people',PEOPLE.length,bc);
