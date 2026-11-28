// 장마다 감지되었지만 at 설명이 없는 인물: node atcheck.mjs n2
import fs from 'fs';
const html=fs.readFileSync('dist/index.html','utf8');const D=JSON.parse(html.match(/const DATA=(.*?);\n/s)[1]);
const PE=Object.fromEntries(D.people.map(p=>[p.id,p]));const only=process.argv[2]||'';
for(const e of D.events){if(!e.id.startsWith(only)||!D.body[e.id])continue;
 const miss=e.pp.filter(x=>!(PE[x].at||{})[e.id]);if(miss.length)console.log(e.id,miss.map(x=>x+':'+PE[x].n).join(', '));}
