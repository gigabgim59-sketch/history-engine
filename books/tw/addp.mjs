// 본문 보강 도구: node addp.mjs spec.json
// spec: [{c:'c05', s:'전개', t:'새 문단', at:2}]  at 생략 시 끝에 추가
//       [{c:'c05', s:'전개', after:'문장.', add:' 덧붙일 문장'}]  문단 안 특정 문장 뒤에 덧붙임
import fs from 'fs';
const MODS=[['body_p1.mjs','B1'],['body_p2.mjs','B2'],['body_p3.mjs','B3'],['body_p4.mjs','B4']];
const ORDER=['안내','배경','원인','주체','전개','영향','갈림','오해'];
const spec=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const loaded={};
for(const [f,v] of MODS){if(!fs.existsSync(f))continue;const m=await import('./'+f+'?'+Date.now());loaded[f]={v,obj:m[v],head:fs.readFileSync(f,'utf8').split('\n')[0]};}
const where=c=>Object.keys(loaded).find(f=>loaded[f].obj[c]);
const touched=new Set();
for(const x of spec){const f=where(x.c);if(!f)throw new Error('no chapter '+x.c);const ch=loaded[f].obj[x.c];
 if(x.after){const arr=ch[x.s];const i=arr.findIndex(p=>p.includes(x.after));if(i<0||arr.filter(p=>p.includes(x.after)).length>1)throw new Error('anchor '+x.c+x.s+x.after);
   const p=arr[i];const k=p.indexOf(x.after)+x.after.length;arr[i]=p.slice(0,k)+x.add+p.slice(k);}
 else{if(!ch[x.s]){ch[x.s]=[];const o={};for(const k of ORDER)if(ch[k])o[k]=ch[k];for(const k of Object.keys(ch))if(!(k in o))o[k]=ch[k];for(const k of Object.keys(ch))delete ch[k];Object.assign(ch,o);}
   const arr=ch[x.s];const at=x.at===undefined?arr.length:x.at;arr.splice(at,0,x.t);}
 touched.add(f);const o={};for(const k of ORDER)if(ch[k])o[k]=ch[k];for(const k of Object.keys(ch))if(!(k in o))o[k]=ch[k];for(const k of Object.keys(ch))delete ch[k];Object.assign(ch,o);}
for(const f of touched){const {v,obj,head}=loaded[f];fs.writeFileSync(f,(head.startsWith('//')?head+'\n':'')+'export const '+v+' = '+JSON.stringify(obj,null,1)+';\n');}
const W={};const ev=(await import('./events.mjs')).EVENTS;ev.forEach(e=>W[e.id]=e.w);
for(const x of new Set(spec.map(x=>x.c))){const f=where(x);console.log(x,'w'+W[x],Object.values(loaded[f].obj[x]).flat().join('').length);}
