// 학파 배분(SPEC '보정 뒤 결정' 3): 문단마다 주된 목소리 하나 — 문단에서 가장 먼저 나오는 학파 표지(사람 이름 등)의 학파.
// 표지가 없는 문단(서술자의 정의·계산)은 세지 않는다. 한 학파가 셈한 문단의 3분의 2를 넘으면 STATUS에 이유를 적는다.
// 표지 목록은 calc/voices.json(장을 쓸 때 사람을 더한다). 사용: node calc/schools.mjs [장 id …]
import fs from 'fs';
import {isTable} from '../checks/_text.mjs';
const V=JSON.parse(fs.readFileSync(new URL('./voices.json',import.meta.url)));
const BODY={};for(const f of fs.readdirSync('.').filter(f=>/^body_p\d+[a-z]?\.mjs$/.test(f)))Object.assign(BODY,...Object.values(await import('../'+f)));
const want=process.argv.slice(2);const over=[];
for(const [id,b] of Object.entries(BODY).sort()){if(want.length&&!want.includes(id))continue;
  const ps=Object.values(b).flat().filter(p=>typeof p==='string'&&!isTable(p)&&!/^\$\$/.test(p.trim())&&!p.startsWith('## '));const c={};let n=0;
  for(const p of ps){let best=null,bi=1e9;for(const [k,ws] of Object.entries(V))for(const w of ws){const i=p.indexOf(w);if(i>=0&&i<bi){bi=i;best=k;}}
    if(best){c[best]=(c[best]||0)+1;n++;}}
  const top=Object.entries(c).sort((a,b)=>b[1]-a[1])[0];if(top&&top[1]/n>2/3)over.push(id);
  console.log(id,`문단 ${ps.length}, 목소리 있는 문단 ${n}:`,Object.entries(c).sort((a,b)=>b[1]-a[1]).map(([k,x])=>`${k} ${x}(${Math.round(x/n*100)}%)`).join(' / '));}
console.log(over.length?'3분의 2 초과: '+over.join(', '):'3분의 2 초과 없음');
