// 『제국의 길』 빌드: node build.mjs → dist/index.html
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
const PY={p1:[1853,1877],p2:[1877,1894],p3:[1894,1912],p4:[1912,1926],p5:[1927,1936],p6:[1937,1941]};

const META={...D.META,guide:fs.existsSync('dist/guide.html'),
 desc:'1853년 페리 내항에서 1941년 12월 개전 결정까지, 봉건 영주의 열도가 근대 국가가 되고 그 국가가 입헌 정치의 길을 버리고 총력전의 제국으로 나아간 88년을 60개의 분기점 사건으로 따라가는 근대 일본의 역사.',
 intro:[
 '이 책은 1853년 페리 함대의 내항에서 시작해 메이지 유신과 국가 건설, 청일·러일전쟁과 식민 제국의 형성, 다이쇼 데모크라시와 그 좌절, 1930년대의 위기와 군부의 대두를 거쳐 1941년 12월 미국·영국과의 개전 결정까지 근대 일본의 88년을 60개의 분기점 사건으로 따라갑니다.',
 '주인공은 일본이라는 국가와 그 안의 사람들입니다. 조선과 대만, 중국은 일본이 움직이고 바꾼 무대로서 충분히 다루되, 초점은 언제나 일본이 무엇을 왜 결정했고 그 결정이 안팎에 무엇을 남겼는가에 둡니다. 사실과 해석은 나누어 적고, 해석이 갈리는 곳은 장마다 「해석의 갈림」에, 널리 퍼진 잘못된 이해는 「흔한 오해」에 모았습니다.',
 '장마다 그 사건을 움직인 힘이 세 힘 가운데 무엇인지 표시하고, 사건이 근대 국가의 다섯 겹, 곧 <b>천황과 헌정</b>, <b>군대와 통수권</b>, <b>산업과 재정</b>, <b>사회</b>, <b>제국</b> 가운데 무엇을 바꾸었는지 기록합니다. 시대를 가로지르는 두 갈림길, 곧 입헌과 정당의 길과 천황제·군부의 길, 탈아와 아시아주의는 「줄기」에서 따라갈 수 있습니다.',
 '일본 사람과 땅의 이름은 일본어 원음으로(이토 히로부미, 사쓰마), 조선 사람은 우리 한자음으로, 중국 사람은 신해혁명 이전에 죽은 사람은 한자음(이홍장), 그 뒤까지 산 사람은 중국어 발음(위안스카이, 장제스)으로 적고, 사건의 이름은 한국에서 굳은 이름(메이지 유신, 을사늑약, 만주사변)을 씁니다. 1872년까지의 날짜는 음력을 쓰던 시대이므로 필요하면 양력을 함께 적습니다.'],
 engines:'근대 일본을 움직인 힘을 셋으로 나누어 봅니다. 번벌과 관료, 궁중과 군부가 위에서 설계하고 밀어붙인 <b>위로부터의 국가 건설</b>, 사족과 농민의 반란에서 민권운동과 정당, 노동·농민 운동과 도시 민중의 소요까지 국가를 밑에서 흔든 <b>아래로부터의 요구</b>, 그리고 열강의 함대와 조약, 청·조선·러시아, 세계대전과 공황처럼 위협이자 기회였던 <b>바깥의 압력과 기회</b>입니다. 세 힘이 어떻게 맞물렸는지가 각 시대의 얼굴을 정했습니다.'
};

const PORTS=[],LEASES=[];
const THREAD_EV={rk:['j07','j12','j13','j17','j19','j25','j31','j33','j35','j40','j44','j47','j49','j57'],
 gun:['j09','j11','j17','j18','j30','j42','j44','j45','j47','j48','j49','j50','j53','j57','j60'],
 dat:['j02','j03','j08','j15','j20','j23','j27','j32','j37','j44','j46','j58'],
 asi:['j10','j16','j22','j29','j32','j36','j45','j46','j51','j52','j54','j55','j59','j60']};

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
const seas=[['동해',134.5,40.2],['황해',123.3,35.6],['동중국해',125.5,29.2],['태평양',143.5,31.5],['남중국해',114.5,19.6],['태평양 건너',146.6,41.6]].map(([n,lo,la])=>({n,xy:P(lo,la)}));
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
