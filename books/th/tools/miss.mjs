// node tools/miss.mjs 1 20 : 장마다 at 없는 인물과 첫 문맥
import fs from 'fs';
const html=fs.readFileSync('dist/index.html','utf8');const D=JSON.parse(html.match(/const DATA=(.*?);\n/s)[1]);
const PE=Object.fromEntries(D.people.map(p=>[p.id,p]));const [a,b]=process.argv.slice(2).map(Number);
const B={};for(const f of fs.readdirSync('.').filter(f=>/^body_p\d[a-z]?\.mjs$/.test(f)))Object.assign(B,...Object.values(await import('../'+f)));
for(const e of D.events){const n=+e.id.slice(1);if(n<a||n>b)continue;const s=JSON.stringify(B[e.id]).replace(/\[\[l\d\d\]\]/g,'');
 for(const x of e.pp.filter(x=>!(PE[x].at||{})[e.id])){const p=PE[x];let i=-1,nm='';for(const w of [p.n,...(p.al||[])]){const j=s.indexOf(w);if(j>=0&&(i<0||j<i)){i=j;nm=w}}
  console.log(e.id,x,i<0?'?':s.slice(Math.max(0,i-25),i+55).replace(/\s+/g,' '))}}
