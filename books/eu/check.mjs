// 유기성 점검: 장마다 앞 장 참조·뒤 장 참조, 분량, 부별 합계
import fs from 'fs';
const h=fs.readFileSync('dist/eurasia.html','utf8');const D=JSON.parse(h.match(/const DATA=(.*?);\n/s)[1]);
const E=Object.fromEntries(D.events.map(e=>[e.id,e]));const T={1:5000,2:2500,3:1500};
for(const p of D.parts){let sum=0;const rows=[];
 for(const e of D.events.filter(x=>x.p===p.id)){const b=D.body[e.id];if(!b){rows.push(`${e.no} ${e.id} 미집필`);continue;}
  const txt=Object.values(b).flat().join('');sum+=txt.length;const refs=[...new Set((txt.match(/\[\[(\w+)\]\]/g)||[]).map(x=>x.slice(2,-2)))];
  const back=refs.filter(r=>E[r].no<e.no).length,fwd=refs.filter(r=>E[r].no>e.no).length;
  const warn=[back?'':'앞참조없음',fwd?'':'뒤참조없음',txt.length<T[e.w]*0.8?'분량부족':''].filter(Boolean).join(',');
  if(warn)rows.push(`${e.no} ${e.id} ${txt.length}자 ${warn}`);}
 console.log(p.no,'합계',sum,rows.length?'\n  '+rows.join('\n  '):'');}
