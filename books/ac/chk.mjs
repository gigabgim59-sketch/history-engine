// 분량 하한 검사: node chk.mjs  (! = 하한 미달)
// 하한은 data.mjs의 META.len {1:{min,target,draft},2:{…},3:{…}}에서 읽는다. 없으면 역사서 기본값.
import {execSync} from 'child_process';
const D=await import('./data.mjs');
const DEF={1:{min:4500},2:{min:2300},3:{min:1350}};
const LEN=(D.META&&D.META.len)||DEF;
const t=execSync('node build.mjs 2>&1').toString();
const ev=(await import('./events.mjs')).EVENTS;const out=[];let miss=0;
for(const e of ev){const m=t.match(new RegExp('[\'"]?'+e.id+'[\'"]?: (\\d+)'));if(!m)continue;const n=+m[1];
  const min=((e.kd&&LEN[e.kd])||LEN[e.w]||DEF[e.w]||{}).min||0; /* 장 종류(kd) 이름의 분량을 먼저 본다(checks/lengths.mjs와 같게, DEFECTS E-22) */if(n<min)miss++;out.push(`${e.id}${n<min?'!':''}:${n}`);}
console.log(out.join(' '));console.log(miss?`하한 미달 ${miss}장`:'하한 미달 없음');
