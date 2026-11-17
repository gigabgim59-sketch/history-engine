// 문단 이동: node mvp.mjs c33 전개 -1 1   (끝 문단을 1번 자리로)
import fs from 'fs';
const [c,s,from,to]=process.argv.slice(2);
const MODS=[['body_p1.mjs','B1'],['body_p2.mjs','B2'],['body_p3.mjs','B3'],['body_p4.mjs','B4']];
for(const [f,v] of MODS){if(!fs.existsSync(f))continue;const m=await import('./'+f);if(!m[v][c])continue;const arr=m[v][c][s];const i=+from<0?arr.length+(+from):+from;const [p]=arr.splice(i,1);arr.splice(+to,0,p);
 const head=fs.readFileSync(f,'utf8').split('\n')[0];fs.writeFileSync(f,(head.startsWith('//')?head+'\n':'')+'export const '+v+' = '+JSON.stringify(m[v],null,1)+';\n');
 console.log(c,s,arr.map(p=>p.slice(0,18)).join(' | '));}
