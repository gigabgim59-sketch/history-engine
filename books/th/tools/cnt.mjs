import fs from 'fs';
const B={};for(const f of fs.readdirSync('.').filter(f=>/^body_p\d[a-z]?\.mjs$/.test(f)))Object.assign(B,...Object.values(await import('../'+f)));
const T=Object.fromEntries(Object.entries(B).map(([k,v])=>[k,JSON.stringify(v)]));
for(const w of process.argv.slice(2)){const r=[];for(const [k,t] of Object.entries(T)){const n=t.split(w).length-1;if(n)r.push(k+'×'+n)}console.log(w,':',r.join(' ')||'—')}
