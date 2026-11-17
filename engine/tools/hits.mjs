import fs from 'fs';
const B={};const F={};for(const f of fs.readdirSync('.').filter(f=>/^body_p\d[a-z]?\.mjs$/.test(f))){const m=await import('../'+f);for(const o of Object.values(m))for(const k of Object.keys(o)){B[k]=o[k];F[k]=f}}
const re=/세 갈래|갈래|자유주의·실증주의·사회주의|자유주의와 실증주의, 사회주의/;
for(const id of Object.keys(B).sort()){for(const [k,v] of Object.entries(B[id])){if(['말','작품'].includes(k))continue;v.forEach((p,i)=>{if(re.test(p))console.log(`## ${id} ${k}${i} [${F[id]}]\n${p}\n`)})}}
