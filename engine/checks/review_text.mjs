// 독립 검수용 본문 뽑기: node checks/review_text.mjs <책 HTML> <출력 폴더> [장 수/묶음, 기본 9]
// 출간본 DATA에서 장마다 부·제목·연도·요약·절(화면판 절 이름)·그 시대의 말·작품을 텍스트로 뽑는다.
// 묶음 파일 part_01.md …, 머리말·맺음·서가 목록(front.md), 장 요약과 연도 문장 목록(index.md)을 만든다.
import fs from 'fs';
import path from 'path';
import { loadData } from './_data.mjs';
const [file, out, per0] = process.argv.slice(2);
const per = +(per0 || 9);
const { D, html } = loadData(file);
fs.mkdirSync(out, { recursive: true });
const M = D.meta || {};
let SLOTH = D.sloth || null;
if (!SLOTH) { const m = html.match(/const SLOTH=(\{.*?\});/s); SLOTH = m && !/DATA/.test(m[1]) ? Function('return ' + m[1])() : {}; }
const grab = (re, d) => { const m = html.match(re); return m ? m[1] : d; };
const LAB = {
  안내: grab(/class="keys guide"><p class="lbl">([^<$]+)<\/p>/, '먼저 알아 둘 것'),
  영향: grab(/<section class="slot"><h2>(영향[^<$]*)<\/h2>/, '영향'),
  사관: M.hvl || grab(/class="box hvb"><p class="lbl">([^<$]+)<\/p>/, '관점들의 풀이'),
  갈림: M.debl || grab(/class="box deb"><p class="lbl">([^<$]+)<\/p>/, '해석의 갈림'),
  오해: '흔한 오해', 말: '그 시대의 말', 작품: '이 장의 작품',
};
const E = Object.fromEntries(D.events.map(e => [e.id, e]));
const P = Object.fromEntries(D.parts.map(p => [p.id, p]));
const ref = t => String(t).replace(/\[\[(\w+)\]\]/g, (m, id) => E[id] ? `(${E[id].no}장)` : '');
const ORDER = ['안내', '배경', '원인', '주체', '전개', '영향', '사관', '갈림', '오해', '말', '작품'];
const chap = e => {
  const B = D.body[e.id] || {}; const p = P[e.p];
  let s = `\n## 제${e.no}장 ${e.t} (${e.id})\n- 부: ${p.no} ${p.t} · 연도: ${e.y}${e.kd ? ' · 종류: ' + e.kd : ''}\n- 요약: ${ref(e.s || '')}\n`;
  for (const k of ORDER) {
    const v = B[k]; if (!v || !v.length) continue;
    const lab = LAB[k] || (SLOTH[e.kd] || {})[k] || k;
    s += `\n### ${lab}\n`;
    if (k === '사관') s += v.map(([a, t]) => `- **${a}**: ${ref(t)}`).join('\n') + '\n';
    else if (k === '말') s += v.map(([w, x]) => `- ${w}: ${ref(x)}`).join('\n') + '\n';
    else if (k === '작품') s += v.map(([w, y, x]) => `- ${w} (${y}): ${ref(x)}`).join('\n') + '\n';
    else s += v.map(x => x.startsWith('## ') ? `#### ${x.slice(3)}` : ref(x)).join('\n\n') + '\n';
  }
  return s;
};
const ev = D.events; const files = [];
for (let i = 0; i < ev.length; i += per) {
  const grp = ev.slice(i, i + per); const n = String(files.length + 1).padStart(2, '0');
  const f = path.join(out, `part_${n}.md`);
  fs.writeFileSync(f, `# 『${M.title || ''}』 검수 본문 ${n}: 제${grp[0].no}장~제${grp[grp.length - 1].no}장\n` + grp.map(chap).join(''));
  files.push([f, grp[0].no, grp[grp.length - 1].no]);
}
let front = `# 『${M.title || ''}』 머리말·부 머리·맺음·서가\n\n## 머리말\n` + (M.intro || []).map(x => ref(x.replace(/<\/?b>/g, '**'))).join('\n\n') + '\n';
for (const p of D.parts) {
  front += `\n## ${p.no} ${p.t} (${p.y})\n` + (p.lead ? ref(p.lead) + '\n\n' : '') + (p.bgx || []).map(ref).join('\n\n') + '\n';
  if (p.f) front += '\n' + Object.entries(p.f).map(([k, v]) => `- ${k}: ${ref(v)}`).join('\n') + '\n';
  if (p.sum) front += '\n' + p.sum.map(ref).join('\n\n') + '\n';
}
front += `\n## 맺음 ${M.endT || ''}\n` + (D.concl || []).map(x => ref(x)).join('\n\n') + '\n';
front += `\n## 서가(${(D.books || []).length}권)\n` + (D.books || []).map(b => `- [${b.id}] ${b.a || ''} · ${b.t || ''} · ${b.o || b.y || ''}${b.role ? ' — ' + b.role : ''}`).join('\n') + '\n';
fs.writeFileSync(path.join(out, 'front.md'), front);
let idx = `# 『${M.title || ''}』 장 요약과 연도 문장\n\n` + ev.map(e => `- 제${e.no}장 ${e.t} (${e.y}): ${ref(e.s || '')}`).join('\n') + '\n';
fs.writeFileSync(path.join(out, 'index.md'), idx);
console.log(files.map(([f, a, b]) => `${path.basename(f)}: ${a}~${b}장 ${fs.statSync(f).size}B`).join('\n'));
