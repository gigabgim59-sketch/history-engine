// 분량 검사: node checks/lengths.mjs [dist/index.html]
// 1) 등급별 하한(META.len 또는 기본값) 2) 장 머리 표시(WL)가 실제 중앙값(100자 반올림)과 같은가. 다르면 실패.
import {loadData,flat} from './_data.mjs';
const path=process.argv[2]||'dist/index.html';const {D,html}=loadData(path);
const DEF={1:{min:4500},2:{min:2300},3:{min:1350}};const LEN=(D.meta&&D.meta.len)||DEF;
const by={},under=[];
for(const e of D.events){const b=D.body[e.id];if(!b)continue;const n=flat(b).length;(by[e.w]=by[e.w]||[]).push(n);
  const min=(LEN[e.w]||DEF[e.w]||{}).min||0;if(n<min)under.push(`${e.id}(w${e.w}) ${n}<${min}`);}
const med=a=>{const b=[...a].sort((x,y)=>x-y);return b[Math.floor((b.length-1)/2)];};
let WL=D.meta&&D.meta.wl;
if(!WL){const m=html.match(/WL=(?:\(DATA\.meta&&DATA\.meta\.wl\)\|\|)?(\{1:'[^']*',2:'[^']*',3:'[^']*'\})/);WL=m?(0,eval)('('+m[1]+')'):{};}
const num=s=>{const m=String(s||'').match(/([\d,]+)\s*자|(\d+)천\s*자/);return m?(m[1]?+m[1].replace(/,/g,''):+m[2]*1000):null;};
const bad=[];
for(const [w,a] of Object.entries(by)){const want=Math.round(med(a)/100)*100,shown=num(WL[w]);
  console.log(`w${w}: ${a.length}장 최소 ${Math.min(...a)} / 중앙 ${med(a)} / 최대 ${Math.max(...a)} · 표시 ${WL[w]||'(없음)'} · 계산 약 ${want.toLocaleString('en-US')}자`);
  if(shown!==want)bad.push(`w${w} 표시 ${WL[w]} ≠ 계산 약 ${want.toLocaleString('en-US')}자`);}
if(under.length)console.log('하한 미달:',under.join(', '));
if(bad.length)console.log('표시 불일치:',bad.join(' / '));
process.exit(under.length||bad.length?1:0);
