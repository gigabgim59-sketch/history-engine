// 인물 감지 점검: node ppcheck.mjs [r01..] — 장마다 감지된 인물과 짧은 이름의 앞뒤 문맥
import fs from 'fs';
const html=fs.readFileSync('dist/index.html','utf8');const D=JSON.parse(html.match(/const DATA=(.*?);\n/s)[1]);
const PE=Object.fromEntries(D.people.map(p=>[p.id,p]));const only=process.argv[2];
for(const e of D.events){if(only&&!e.id.startsWith(only))continue;if(!D.body[e.id])continue;
 console.log(e.id,e.pp.map(x=>PE[x].n).join(', '));}
