// 쟁점 원고(outputs/쟁점별 신학 정리/src)를 엔진 본문(body_p1~p7.mjs)과 장 목록 조각으로 바꾼다.
// 사용: 책 폴더에서 node tools/gen.mjs
// 보강 문단은 src/extra.mjs(EXTRA: {qNN:{슬롯:[문단], 말:[[낱말,풀이]]}})에서 덧붙인다.
import fs from 'fs';
import path from 'path';
import {pathToFileURL} from 'url';
const SRC = path.resolve('src');
const imp = f => import(pathToFileURL(path.join(SRC, f)).href);
const {IA} = await imp('issues_a.mjs'), {IB} = await imp('issues_b.mjs'), {IC} = await imp('issues_c.mjs'), {ID} = await imp('issues_d.mjs'), {IE} = await imp('issues_e.mjs');
const {TH} = await imp('appendix.mjs');
const EXTRA = fs.existsSync(path.join(SRC, 'extra.mjs')) ? (await imp('extra.mjs')).EXTRA : {};
const IS = [...IA, ...IB, ...IC, ...ID, ...IE];
const TN = {orth:'정교회',cath:'가톨릭',luth:'루터교',ref:'개혁주의',ang:'성공회',arm:'아르미니우스주의·웨슬리주의',pent:'오순절·은사주의',free:'재세례파·침례교·자유교회',mod:'근현대 신학',phil:'철학'};
const cell = s => String(s).replace(/\|/g, '/').replace(/\n/g, ' ');
const tbl = (head, rows) => '|' + head.join('|') + '|\n|' + head.map(() => '---').join('|') + '|\n' + rows.map(r => '|' + r.map(cell).join('|') + '|').join('\n');
const id = q => 'tq' + q.id.slice(1);
const thref = q => (q.ch || []).length ? `시대 순으로는 『같은 성경, 다른 답』의 ${q.ch.map(c => `${+c.slice(2)}장 「${TH[c].replace(/^◆ /, '◆')}」`).join(', ')}에서 다룬다.` : '';
const body = {};
for (const q of IS) {
  const x = EXTRA[q.id] || {};
  const b = {
    안내: [q.key + (q.q ? ' 이 장의 물음은 이렇다. ' + q.q : ''), ...(x.안내 || []), thref(q)].filter(Boolean),
    배경: [...q.lead, ...(x.배경 || [])],
    원인: [...(x.원인앞 || []), tbl(['입장', '핵심 주장', '대표', '원전'], q.pos.map(r => [r[0] + (r[4].length ? ` (${r[4].map(t => TN[t]).join('·')})` : ''), r[1], r[2], r[3]])), ...(x.원인 || [])],
    주체: q.txt.flatMap(([ref, gist, rd]) => [`${ref}: ${gist}`, tbl(['읽는 쪽', '독해'], rd)]).concat(x.주체 || []),
    전개: [tbl(['논거', '주장', '반론'], q.arg), ...(x.전개 || [])],
    영향: [...q.doc.map(([t, d]) => `${t}: ${d}`), ...(x.영향 || [])],
    갈림: [...q.crit.map(([t, w, c]) => `${t}에 대해 ${w}: ${c}`), ...(x.갈림 || [])],
    오해: [...q.mis, ...(x.오해 || [])],
    말: x.말 || []
  };
  body[id(q)] = b;
}
const parts = ['p1','p2','p3','p4','p5','p6','p7'];
for (const [i, p] of parts.entries()) {
  const ids = IS.filter(q => q.p === p).map(id);
  const obj = Object.fromEntries(ids.map(k => [k, body[k]]));
  fs.writeFileSync(`body_p${i + 1}.mjs`, `// 제${i + 1}부 본문: tools/gen.mjs가 쟁점 원고에서 만든다. 손으로 고치지 말고 원고(src)를 고친다.\nexport const B${i + 1} = ${JSON.stringify(obj, null, 1)};\n`);
}
// 줄기용: 쟁점마다 등장하는 전통
const tr = {};
for (const q of IS) for (const r of q.pos) for (const t of r[4]) if (TN[t] && !['mod', 'phil'].includes(t)) (tr[t] ||= new Set()).add(id(q));
fs.writeFileSync('tools/threads.json', JSON.stringify(Object.fromEntries(Object.entries(tr).map(([k, v]) => [k, [...v].sort()])), null, 1));
fs.writeFileSync('tools/issues.json', JSON.stringify(IS.map(q => ({id: id(q), p: q.p, t: q.t, q: q.q, key: q.key, ax: q.ax})), null, 1));
console.log('body', Object.keys(body).length);
