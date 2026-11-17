import fs from 'fs';
const B={};for(const f of fs.readdirSync('.').filter(f=>/^body_p\d[a-z]?\.mjs$/.test(f)))Object.assign(B,...Object.values(await import('../'+f)));
const [a,b]=process.argv.slice(2).map(Number);
for(let i=a;i<=b;i++){const id='l'+String(i).padStart(2,'0');console.log(id,B[id]['안내'][0])}
