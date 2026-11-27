// node tools/autoat.mjs /tmp/miss.txt > sp/atZ.txt : 본문에서 그 인물이 처음 나오는 문장을 장별 설명으로 뽑는다
import fs from 'fs';
const B={};for(const f of fs.readdirSync('.').filter(f=>/^body_p\d[a-z]?\.mjs$/.test(f)))Object.assign(B,...Object.values(await import('../'+f)));
const R={};for(const r of fs.readFileSync('sp/p1rows.txt','utf8').split('\n')){if(!r.trim()||r[0]==='#')continue;const x=r.split('|');R[x[0]]=[x[1],...(x[2]?x[2].split(','):[])];}
const ORD=['주체','원인','전개','배경','영향','안내','사관','오해','갈림'];
const sents=c=>{const out=[];for(const k of ORD){const v=c[k];if(!v)continue;for(const p of v){const t=Array.isArray(p)?p[1]:p;String(t).replace(/\[\[k\d+\]\]/g,'').split(/(?<=[다요]\.)\s+/).forEach(s=>out.push(s.trim()));}}return out.filter(Boolean);};
const lines=fs.readFileSync(process.argv[2],'utf8').trim().split('\n');const out=[];
for(const l of lines){const c=l.slice(0,l.indexOf(' ')),rest=l.slice(l.indexOf(' ')+1);const ids=rest.split(', ').map(x=>x.split(':')[0]);const S=sents(B[c]);const parts=[c];
 for(const id of ids){const names=R[id];const hit=S.filter(s=>names.some(n=>s.includes(n)));if(!hit.length){console.error('nohit',c,id);continue;}
  let s=hit.find(s=>s.length<=120)||hit.sort((a,b)=>a.length-b.length)[0];s=s.replace(/[|;]/g,',');parts.push(id+':'+s);}
 out.push(parts.join('|'));}
console.log(out.join('\n'));
