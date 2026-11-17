import fs from 'fs';
const B={};for(const f of fs.readdirSync('.').filter(f=>/^body_p\d[a-z]?\.mjs$/.test(f)))Object.assign(B,...Object.values(await import('../'+f)));
const au=new Map();
for(const [id,c] of Object.entries(B)){for(const w of c['작품']||[]){const who=(w[1].split('·')[1]||'').trim();for(const n of who.split(/와 |과 |, | 엮음| 옮김/).map(s=>s.trim()).filter(Boolean)){if(!au.has(n))au.set(n,new Set());au.get(n).add(id)}}}
console.log([...au].map(([n,s])=>n+'('+[...s].join(',')+')').join(' | '));
