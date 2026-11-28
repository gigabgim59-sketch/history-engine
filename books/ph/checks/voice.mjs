// 목소리 검사: node checks/voice.mjs [dist/index.html]
// 1) 귀속 공식의 반복: META.formulas(기본 '이 서사에서','이 서사는')가 장당 META.formulaMax(기본 2)를 넘는 장 → 실패
// 2) 서술자 문장의 평가어: META.evalw 목록의 말이 따옴표·인용 밖에서, 귀속 표지 없이 쓰인 문장 → 보고(사람이 판단)
// 3) 학자 없는 갈림: 해석의 갈림 문단에 연도(4자리)도 인명 사전의 이름도 없는 경우 → 보고
// 4) 바깥 점검 비중: 갈림+오해가 본문에서 차지하는 비율 → 보고(관점 책은 SPEC 기준과 대조)
import {loadData,flat,NARR} from './_data.mjs';
const {D}=loadData(process.argv[2]||'dist/index.html');const M=D.meta||{};
const F=M.formulas||['이 서사에서','이 서사는'];const FMAX=M.formulaMax??2;const EV=M.evalw||[];
const CUE=/(라고|이라|라 불렀|이라 불렀|라 했|이라 했|로 보았|라 보았|에게는|에게 |의 눈에|의 말로|의 표현으로|라 부른|이라 부른|로 불렀)/;
const NAMES=(D.people||[]).flatMap(p=>[p.n,...(p.al||[])]).filter(n=>n&&n.length>=2);
const stripQ=s=>s.replace(/‘[^’]*’|“[^”]*”|「[^」]*」|『[^』]*』|"[^"]*"/g,'');
let fail=[],rep=[],tot=0,out=0;const fcount={};
for(const e of D.events){const b=D.body[e.id];if(!b)continue;
  for(const k of NARR){for(const p of (b[k]||[])){if(typeof p!=='string')continue;tot+=p.length;if(k==='갈림'||k==='오해')out+=p.length;
    for(const f of F){const n=p.split(f).length-1;if(n)fcount[e.id]=(fcount[e.id]||0)+n;}
    for(const s of p.split(/(?<=[다요]\.)\s+/)){const bare=stripQ(s);
      for(const w of EV)if(bare.includes(w)&&!CUE.test(s))rep.push(`${e.id} ${k}: 평가어 '${w}' — ${s.slice(0,70)}…`);}
    if(k==='갈림'&&!/\d{4}/.test(p)&&!NAMES.some(n=>p.includes(n)))rep.push(`${e.id} 갈림: 연도·학자 이름 없음 — ${p.slice(0,60)}…`);}}
  for(const [k,v] of Object.entries(b))if(!['말','작품','사관',...NARR].includes(k))rep.push(`${e.id}: 알 수 없는 절 '${k}'`);}
for(const [id,n] of Object.entries(fcount))if(n>FMAX)fail.push(`${id}: 공식 ${n}회(기준 ${FMAX})`);
const total=Object.values(fcount).reduce((a,b)=>a+b,0);
console.log(`공식(${F.join('·')}) 전체 ${total}회, 장당 기준 초과 ${fail.length}장`);
console.log(`바깥 점검(갈림+오해) 비중 ${(100*out/Math.max(1,tot)).toFixed(1)}%`+(M.outerMin?` (SPEC 기준 ${M.outerMin}%)`:''));
if(M.outerMin&&100*out/tot<M.outerMin)fail.push(`바깥 점검 비중이 기준 미만`);
if(rep.length)console.log('확인할 것('+rep.length+'):\n'+rep.slice(0,80).join('\n')+(rep.length>80?`\n… 외 ${rep.length-80}건`:''));
if(fail.length)console.log('실패:\n'+fail.slice(0,40).join('\n')+(fail.length>40?`\n… 외 ${fail.length-40}건`:''));
process.exit(fail.length?1:0);
