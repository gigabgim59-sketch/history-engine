// 보정 장 측정: node calc/measure.mjs  → 절별 문단 수·글자 수·비중, 문단당 글자 수, 수식·표 분량
import {B3A} from '../body_p3a.mjs';
import {plain,mathSpans,isTable} from '../checks/_text.mjs';
import {SLOTH} from '../data.mjs';
for(const [id,b] of Object.entries(B3A)){
  const rows=[];let tot=0,np=0,raw=0,nm=0,nt=0,mathRaw=0;
  for(const [k,arr] of Object.entries(b)){let c=0,n=0;for(const p of arr){const t=plain(p);c+=t.length;raw+=p.length;
      const ms=mathSpans(p);nm+=ms.length;mathRaw+=p.length-p.replace(/\$\$[\s\S]+?\$\$|(?<!\\)\$[^$\n]+?(?<!\\)\$/g,'').length;
      if(isTable(p))nt++;else if(!/^\$\$/.test(p.trim()))n++;}
    rows.push([SLOTH.is[k]||({안내:'먼저 알아 둘 것',갈림:'해석의 갈림',오해:'흔한 오해'})[k]||k,arr.length,n,c]);tot+=c;np+=n;}
  const proseChars=rows.reduce((a,r)=>a+r[3],0);
  console.log(`\n${id}: 셈한 분량 ${tot}자, 줄글 문단 ${np}개(표 ${nt}, 수식 문단·줄 안 수식 ${nm}), 수식 마크업 ${mathRaw}자(분량에서 뺌), 원문 길이 ${raw}자`);
  for(const [h,all,n,c] of rows)console.log(`  ${h.padEnd(12)} 항목 ${all} · ${c}자 · ${(c/tot*100).toFixed(1)}%`);
  const paras=Object.values(b).flat().filter(p=>!isTable(p)&&!/^\$\$/.test(p.trim())).map(p=>plain(p).length).sort((a,b)=>a-b);
  console.log(`  문단당 글자: 중앙 ${paras[Math.floor((paras.length-1)/2)]} · 평균 ${Math.round(paras.reduce((a,x)=>a+x,0)/paras.length)} · 최소 ${paras[0]} · 최대 ${paras.at(-1)}`);
}
