import fs from 'fs';import {execSync} from 'child_process';
const t=execSync('node build.mjs 2>&1').toString();
const ev=(await import('./events.mjs')).EVENTS;let out=[];
for(const e of ev){const m=t.match(new RegExp(e.id+': (\\d+)'));if(!m)continue;const n=+m[1];const min=e.w==1?4500:2300;out.push(`${e.id}${n<min?'!':''}:${n}`)}console.log(out.join(' '));
