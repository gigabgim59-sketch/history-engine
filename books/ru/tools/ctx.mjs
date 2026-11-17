// node tools/ctx.mjs u03 비어드
import fs from 'fs';
const [c,w]=process.argv.slice(2);
const files=fs.readdirSync('.').filter(f=>/^body_p\d[a-z]?\.mjs$/.test(f));
for(const f of files){const m=await import('../'+f);const o=Object.values(m)[0][c];if(!o)continue;const s=JSON.stringify(o);let i=-1;while((i=s.indexOf(w,i+1))>=0)console.log(f,JSON.stringify(s.slice(Math.max(0,i-30),i+w.length+12)));}
const ev=(await import('../events.mjs')).EVENTS.find(e=>e.id===c);const t=ev.s+ev.q;let i=-1;while((i=t.indexOf(w,i+1))>=0)console.log('events',JSON.stringify(t.slice(Math.max(0,i-30),i+w.length+12)));
