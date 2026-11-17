// 『제국의 경영』 빌드: node build.mjs → dist/index.html
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
const PY=Object.fromEntries(D.PARTS.map(p=>[p.id,[p.y0,p.y1]]));
const META={...D.META,guide:fs.existsSync('dist/guide.html')};
const ECON=(await opt('econ.mjs')).ECON||null;

const PORTS=[],LEASES=[];
const THREAD_EV=D.THREAD_EV;

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
EVENTS.forEach(e=>{if(!e.kd)e.kd='ev';});
if(D.KINDS)EVENTS.forEach(e=>{if(!D.KINDS.find(k=>k[0]===e.kd))err.push('kd '+e.id);});
if(err.length){console.error(err);process.exit(1);}

const YC={};EVENTS.forEach(e=>{(YC[e.yr]=YC[e.yr]||[]).push(e.id);});
const YF=id=>{const e=EVENTS.find(x=>x.id===id),L=YC[e.yr];return L.length>1?e.yr+L.indexOf(id)/L.length*0.9:e.yr;};
const events=EVENTS.map((e,i)=>{const [x,y]=P(e.pl[1],e.pl[2]);const txt=[e.s,e.q,...(BODY[e.id]?Object.values(BODY[e.id]).flat():[])].join('\n');
  const pp=mentions(txt);PEOPLE.forEach(p=>{if(p.at&&p.at[e.id]&&!pp.includes(p.id))pp.push(p.id);});
  return {...e,yr:YF(e.id),no:i+1,mx:x,my:y,bk:BK[e.id]||[],axc:AXCH[e.id]||[],pp};});
const people=PEOPLE.map(p=>({...p,ch:events.filter(e=>e.pp.includes(p.id)).map(e=>e.id)}));
for(const p of PEOPLE)for(const c of Object.keys(p.at||{}))if(!ids.has(c))err.push('people at '+p.id+c);
for(const p of PEOPLE)if(!FACTS.find(f=>f[0]===p.f))err.push('faction '+p.id+p.f);
for(const p of PEOPLE)for(const [r] of (p.rel||[]))if(!PEOPLE.find(q=>q.id===r))err.push('rel '+p.id+r);
if(err.length){console.error(err);process.exit(1);}
const groups=D.GROUPS.map(gr=>({...gr,ch:GROUP_CH.flatMap(m=>m[gr.id]||[])}));
const parts=D.PARTS.map(p=>({...p,y0:PY[p.id][0],y1:PY[p.id][1],...(PARTX[p.id]||{})}));
const regions=D.REGIONS.map(r=>({...r,xy:P(r.lon,r.lat)}));
const seas=[['대서양',-38,28],['태평양',-150,15],['인도양',78,-18],['태평양',165,22]].map(([n,lo,la])=>({n,xy:P(lo,la)}));
const lineage=(LN.LINEAGE||[]).map(l=>({...l,b:LNB[l.id]||null}));
const DATA={meta:META,why:WHY,concl:CONCL,body:BODY,W:g.W,H:g.H,land:g.land,grat:g.grat,borders:g.borders,prov:g.prov,rivers:g.rivers,lakes:g.lakes,
 regions,seas,people,facts:FACTS,pdeny:PDENY,axes:D.AXES,engines:D.ENGINES,parts,events,groups,books:BOOKS,terms:TERMS,tcats:TCATS,lineage,lcats:LN.LCATS||[],
 threads:D.THREADS.map(t=>({...t,ev:THREAD_EV[t.id]||[]})),ports:[],leases:[],kinds:D.KINDS||null,econ:ECON};

let html=fs.readFileSync('template.html','utf8');
html=html.replace('/*__DATA__*/',()=>'const DATA='+JSON.stringify(DATA)+';').replaceAll('__TITLE__',META.title).replaceAll('__SUB__',META.sub).replaceAll('__DESC__',META.desc);
fs.mkdirSync('dist',{recursive:true});
fs.writeFileSync('dist/index.html',html);
const bc=Object.fromEntries(Object.entries(BODY).map(([k,v])=>[k,Object.values(v).flat().join('').length]));
console.log('ok',(html.length/1024).toFixed(0)+'KB','H='+g.H,'people',PEOPLE.length,bc);
