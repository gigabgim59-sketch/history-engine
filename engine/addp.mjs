// 본문 보강 도구: node addp.mjs spec.json
// spec: [{c:'c05', s:'전개', t:'새 문단', at:2}]   at을 빼면 끝에 붙인다
//       [{c:'c05', s:'전개', after:'문장.', add:' 덧붙일 문장'}]   문단 안 특정 문장 뒤에 덧붙인다
//       말·작품은 t에 배열을 준다: {c, s:'말', t:['낱말','풀이']}
// 고친 결함(DEFECTS E-01): 절 이름을 정규화하고 허용 목록으로 검사한다. 쓴 뒤 다시 읽어
// 겹친 키·빈 절·허용되지 않은 키(예: 다른 문자로 쓴 '작品')를 찾아 멈춘다.
import fs from 'fs';
const ORDER=['안내','배경','원인','주체','전개','영향','사관','갈림','오해','말','작품'];
const ALLOWED=new Set(ORDER);
const files=fs.readdirSync('.').filter(f=>/^body_p\d+[a-z]?\.mjs$/.test(f)).sort();
const spec=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const loaded={};
for(const f of files){const src=fs.readFileSync(f,'utf8');const m=src.match(/export const (\w+)\s*=/);if(!m)continue;
  const mod=await import('./'+f+'?'+Date.now());loaded[f]={v:m[1],obj:mod[m[1]],head:src.split('\n')[0]};}
const where=c=>Object.keys(loaded).find(f=>loaded[f].obj[c]);
const reorder=ch=>{const o={};for(const k of ORDER)if(ch[k])o[k]=ch[k];for(const k of Object.keys(ch))if(!(k in o))o[k]=ch[k];for(const k of Object.keys(ch))delete ch[k];Object.assign(ch,o);};
const touched=new Set();
for(const x0 of spec){const x={...x0,s:String(x0.s||'').normalize('NFC').trim()};
 if(!ALLOWED.has(x.s))throw new Error(`허용되지 않은 절 이름 '${x0.s}' (${x.c}). 허용: ${ORDER.join(', ')}`);
 const f=where(x.c);if(!f)throw new Error('없는 장 '+x.c);const ch=loaded[f].obj[x.c];
 if(x.after){const arr=ch[x.s]||[];const hits=arr.filter(p=>typeof p==='string'&&p.includes(x.after));
   if(hits.length!==1)throw new Error(`기준 문장이 ${hits.length}곳: ${x.c} ${x.s} ${x.after}`);
   const i=arr.indexOf(hits[0]);const k=hits[0].indexOf(x.after)+x.after.length;arr[i]=hits[0].slice(0,k)+x.add+hits[0].slice(k);}
 else{const isPair=x.s==='말'||x.s==='작품'||x.s==='사관';
   if(isPair?!Array.isArray(x.t):typeof x.t!=='string')throw new Error(`t의 형식이 맞지 않음: ${x.c} ${x.s}`);
   if(!isPair&&(!x.t.trim()||ALLOWED.has(x.t.trim())))throw new Error(`빈 문단이거나 절 이름만 있는 문단: ${x.c} ${x.s}`);
   if(!ch[x.s])ch[x.s]=[];const arr=ch[x.s];const at=x.at===undefined?arr.length:x.at;arr.splice(at,0,x.t);}
 reorder(ch);touched.add(f);}
for(const f of touched){const {v,obj,head}=loaded[f];fs.writeFileSync(f,(head.startsWith('//')?head+'\n':'')+'export const '+v+' = '+JSON.stringify(obj,null,1)+';\n');}
// 다시 읽어 검사
const bad=[];
for(const f of touched){const src=fs.readFileSync(f,'utf8');
  // 같은 장 안에서 같은 키가 두 번 나오는지(문자열 수준)
  for(const blk of src.split(/\n \"[^"]+\": \{\n/).slice(1)){const keys=[...blk.matchAll(/^  "([^"]+)": \[/gm)].map(m=>m[1]);
    const dup=keys.filter((k,i)=>keys.indexOf(k)!==i);if(dup.length)bad.push(f+' 겹친 키 '+dup.join(','));}
  const mod=await import('./'+f+'?'+Date.now()+'r');const obj=mod[loaded[f].v];
  for(const [c,ch] of Object.entries(obj))for(const [k,arr] of Object.entries(ch)){
    if(!ALLOWED.has(k))bad.push(`${c}: 허용되지 않은 키 '${k}'`);
    if(!Array.isArray(arr)||!arr.length)bad.push(`${c}: 빈 절 '${k}'`);}}
if(bad.length){console.error('검사 실패:\n'+bad.join('\n'));process.exit(1);}
const W={};(await import('./events.mjs')).EVENTS.forEach(e=>W[e.id]=e.w);
for(const c of new Set(spec.map(x=>x.c))){const f=where(c);const SL=v=>typeof v==='string'?v.length:Array.isArray(v)?v.reduce((s,x)=>s+SL(x),0):0;console.log(c,'w'+W[c],SL(Object.values(loaded[f].obj[c])));}
