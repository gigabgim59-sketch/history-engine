// 단독 자료 빌드: src 폴더에서 node build.mjs → ../쟁점별 신학 정리.html (글꼴은 따로 font.py로 심는다). 서가 책 tq의 원고이기도 하다(tools/gen.mjs).
import fs from 'fs';
import {META, PARTS, TRAD, AXES} from './meta.mjs';
import {IA} from './issues_a.mjs'; import {IB} from './issues_b.mjs'; import {IC} from './issues_c.mjs';
import {ID} from './issues_d.mjs'; import {IE} from './issues_e.mjs';
import {COMPARE, AXTAB, TIMELINE, TH} from './appendix.mjs';

const IS = [...IA, ...IB, ...IC, ...ID, ...IE];
const TN = Object.fromEntries(TRAD);
// ── 검사
const err = [];
const ids = new Set();
for (const q of IS) {
  if (ids.has(q.id)) err.push('중복 ' + q.id); ids.add(q.id);
  if (!PARTS.some(p => p.id === q.p)) err.push(q.id + ' 부 없음 ' + q.p);
  for (const k of ['t','q','key','lead','pos','txt','arg','doc','crit','mis']) if (!q[k] || (Array.isArray(q[k]) && !q[k].length)) err.push(q.id + ' 칸 비었음 ' + k);
  for (const a of q.ax || []) if (!AXES[a]) err.push(q.id + ' 축 ' + a);
  for (const c of q.ch || []) if (!TH[c]) err.push(q.id + ' 장 ' + c);
  q.pos.forEach((r, i) => { if (r.length !== 5) err.push(q.id + ' 입장 칸 수 ' + i); for (const t of r[4]) if (!TN[t]) err.push(q.id + ' 꼬리표 ' + t); });
  q.txt.forEach((r, i) => { if (r.length !== 3 || !Array.isArray(r[2])) err.push(q.id + ' 본문 칸 ' + i); });
  q.arg.forEach((r, i) => { if (r.length !== 3) err.push(q.id + ' 논거 칸 ' + i); });
  q.crit.forEach((r, i) => { if (r.length !== 3) err.push(q.id + ' 비판 칸 ' + i); });
  q.doc.forEach((r, i) => { if (r.length !== 2) err.push(q.id + ' 문서 칸 ' + i); });
}
COMPARE.rows.forEach(r => { if (r.length !== COMPARE.cols.length + 2) err.push('비교표 칸 수 ' + r[0] + ' ' + r.length); if (!ids.has(r.at(-1))) err.push('비교표 쟁점 ' + r.at(-1)); });
for (const r of [...AXTAB, ...TIMELINE]) for (const x of String(r.at(-1)).split(' ')) if (!ids.has(x)) err.push('참조 ' + x);
const evalw = ['이단적','비성경적','성경적이다','참된 교회','거짓 교사','광신','미신'];
const narr = q => [q.key, ...q.lead, ...q.mis].join(' ');
for (const q of IS) for (const w of evalw) if (narr(q).includes(w)) err.push(q.id + ' 서술자 문장의 평가어 ' + w);
if (err.length) { console.error(err.join('\n')); process.exit(1); }

// ── 쓰기
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const qref = s => esc(s).replace(/\bq(\d\d)\b/g, (m) => { const q = IS.find(x => x.id === m); return q ? `<a href="#${m}" class="qr">${q.t}</a>` : m; });
const tags = t => t.map(x => `<span class="tg tg-${x}">${esc(TN[x])}</span>`).join('');
const partOf = id => PARTS.find(p => p.id === id);
let qn = 0;
const num = Object.fromEntries(IS.map(q => [q.id, ++qn]));

function issueHtml(q) {
  const n = num[q.id];
  return `<section class="issue" id="${q.id}" data-text="${esc([q.t, q.q, q.key, ...q.lead, ...q.pos.flat(2), ...q.txt.flat(3), ...q.arg.flat(), ...q.doc.flat(), ...q.crit.flat(), ...q.mis].join(' '))}">
<header class="ih"><div class="eyebrow">${partOf(q.p).n}. ${esc(partOf(q.p).t)} · 쟁점 ${n}</div><h2>${esc(q.t)}</h2>
<p class="qq">${esc(q.q)}</p>
<div class="meta">${(q.ax || []).map(a => `<span class="ax">${esc(AXES[a])}</span>`).join('')}</div></header>
<div class="keybox"><b>핵심</b> ${esc(q.key)}</div>
<h3>물음이 생긴 자리</h3>${q.lead.map(p => `<p>${esc(p)}</p>`).join('')}
<h3>입장들</h3>
<div class="tw"><table class="pos"><thead><tr><th>입장</th><th>핵심 주장</th><th>대표</th><th>원전</th></tr></thead><tbody>
${q.pos.map(r => `<tr data-tags="${r[4].join(' ')}"><td><b>${esc(r[0])}</b><div class="tgs">${tags(r[4])}</div></td><td>${esc(r[1])}</td><td>${esc(r[2])}</td><td class="src">${esc(r[3])}</td></tr>`).join('')}
</tbody></table></div>
<h3>같은 본문, 다른 독해</h3>
${q.txt.map(r => `<div class="txt"><div class="ref">${esc(r[0])}</div><div class="gist">${esc(r[1])}</div><dl>${r[2].map(([w, d]) => `<dt>${esc(w)}</dt><dd>${esc(d)}</dd>`).join('')}</dl></div>`).join('')}
<h3>논거와 반론</h3>
<div class="tw"><table class="arg"><thead><tr><th>논거</th><th>주장</th><th>반론</th></tr></thead><tbody>
${q.arg.map(r => `<tr><td><b>${esc(r[0])}</b></td><td>${esc(r[1])}</td><td>${esc(r[2])}</td></tr>`).join('')}
</tbody></table></div>
<h3>교회 문서</h3><ul class="docs">${q.doc.map(([t, d]) => `<li><b>${esc(t)}</b> ${esc(d)}</li>`).join('')}</ul>
<h3>이름 붙은 비판</h3><ul class="crit">${q.crit.map(([t, w, c]) => `<li><span class="ct">${esc(t)}</span>에 대해 <b>${esc(w)}</b>: ${esc(c)}</li>`).join('')}</ul>
<h3>흔한 오해</h3><ul class="mis">${q.mis.map(m => `<li>${esc(m)}</li>`).join('')}</ul>
${q.ch && q.ch.length ? `<div class="chs"><b>역사 속에서</b> 『같은 성경, 다른 답』 ${q.ch.map(c => `<span>${+c.slice(2)}장 ${esc(TH[c])}</span>`).join('')}</div>` : ''}
<p class="top"><a href="#toc">차례로</a></p>
</section>`;
}

const toc = PARTS.map(p => `<li class="tp"><a href="#${p.id}">${p.n}. ${esc(p.t)}</a><ol>${IS.filter(q => q.p === p.id).map(q => `<li data-q="${q.id}"><a href="#${q.id}"><span class="n">${num[q.id]}</span>${esc(q.t)}</a></li>`).join('')}</ol></li>`).join('')
  + `<li class="tp"><a href="#apx">부록</a><ol><li><a href="#cmp">교파 종합 비교</a></li><li><a href="#axt">대립 축과 쟁점</a></li><li><a href="#tl">문서 연표</a></li></ol></li>`;

const body = PARTS.map(p => `<div class="part" id="${p.id}"><div class="pn">${p.n}</div><h1>${esc(p.t)}</h1><p>${esc(p.d)}</p></div>` + IS.filter(q => q.p === p.id).map(issueHtml).join('\n')).join('\n');

const apx = `<div class="part" id="apx"><div class="pn">부록</div><h1>한눈에 보기</h1></div>
<section class="issue" id="cmp"><h2>교파 종합 비교</h2><p class="note">${esc(COMPARE.note)}</p>
<div class="tw"><table class="cmp"><thead><tr><th>쟁점</th>${COMPARE.cols.map(c => `<th>${esc(c)}</th>`).join('')}</tr></thead><tbody>
${COMPARE.rows.map(r => `<tr><th><a href="#${r.at(-1)}">${esc(r[0])}</a></th>${r.slice(1, -1).map(c => `<td>${esc(c)}</td>`).join('')}</tr>`).join('')}
</tbody></table></div></section>
<section class="issue" id="axt"><h2>대립 축과 쟁점</h2><p class="note">스물여섯 쟁점은 몇 개의 근본 물음으로 모인다. 같은 전통이 축마다 서는 자리가 다르므로, 교파의 맞섬은 한 줄 위의 대립으로 정리되지 않는다.</p>
<div class="tw"><table class="arg"><thead><tr><th>축</th><th>근본 물음</th><th>관련 쟁점</th></tr></thead><tbody>
${AXTAB.map(r => `<tr><td><b>${esc(r[0])}</b></td><td>${esc(r[1])}</td><td>${qref(r[2]).split(' ').join(' · ')}</td></tr>`).join('')}
</tbody></table></div>
<p>어느 축에서 무엇을 사람의 근본 문제로 보는가가 신학 전체의 모양을 정한다는 지적이 여러 신학자에게서 나왔다. 죄책을 중심에 두면 칭의가, 죽음과 썩음을 중심에 두면 신화와 치유가, 소외를 중심에 두면 화해와 새 존재가, 억압을 중심에 두면 해방이 신학의 중심에 선다. 이 자료는 그 가운데 어느 것이 옳은지 판정하지 않는다.</p></section>
<section class="issue" id="tl"><h2>문서 연표</h2><p class="note">이 자료에서 근거로 든 공의회·신앙고백·교회 문서를 연대순으로 놓았다.</p>
<div class="tw"><table class="arg tl"><thead><tr><th>연도</th><th>문서</th><th>내용</th><th>쟁점</th></tr></thead><tbody>
${TIMELINE.map(r => `<tr><td class="yr">${r[0]}</td><td><b>${esc(r[1])}</b></td><td>${esc(r[2])}</td><td>${qref(r[3]).split(' ').join(' · ')}</td></tr>`).join('')}
</tbody></table></div></section>`;

const tradOpts = TRAD.map(([k, v]) => `<option value="${k}">${esc(v)}</option>`).join('');
const css = fs.readFileSync(new URL('./style.css', import.meta.url), 'utf8');
const js = fs.readFileSync(new URL('./app.js', import.meta.url), 'utf8');
const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${esc(META.title)}</title><meta name="description" content="${esc(META.sub)}">
<!--__FONTS__--><style>${css}</style></head><body>
<header class="bar"><button id="menu" aria-label="차례 열기">☰</button><a class="brand" href="#top">${esc(META.title)}</a>
<input id="q" type="search" placeholder="낱말로 쟁점 찾기 (예: 칼케돈, 롬 9, 연옥)" aria-label="쟁점 찾기">
<select id="tr" aria-label="전통으로 입장 거르기"><option value="">전통 강조 없음</option>${tradOpts}</select>
<button id="theme" aria-label="밤 모드 바꾸기">◐</button></header>
<nav id="toc" class="toc"><div class="tocin"><p class="th">차례</p><ol>${toc}</ol><p class="hit" id="hit"></p></div></nav>
<main id="top"><div class="cover"><div class="eyebrow">기독교 신학 · 주제별 정리</div><h1 class="title">${esc(META.title)}</h1><p class="sub">${esc(META.sub)}</p>
${META.intro.map(p => `<p>${esc(p)}</p>`).join('')}
<p class="caveat">${esc(META.caveat)}</p>
<div class="legend"><b>읽는 법</b> 쟁점마다 ① 핵심 ② 물음이 생긴 자리 ③ 입장들(표) ④ 같은 본문, 다른 독해 ⑤ 논거와 반론 ⑥ 교회 문서 ⑦ 이름 붙은 비판 ⑧ 흔한 오해 ⑨ 『같은 성경, 다른 답』의 관련 장 순서입니다. 위쪽의 전통 상자에서 전통을 고르면 그 꼬리표가 붙은 입장이 강조됩니다.</div></div>
${body}
${apx}
<footer class="foot">${esc(META.title)} · 쟁점 ${IS.length}개 · ${new Date().toISOString().slice(0, 10)} 판</footer></main>
<script>${js}</script></body></html>`;
const out = new URL('../쟁점별 신학 정리.html', import.meta.url);
fs.writeFileSync(out, html);
const plain = html.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>/g, '').replace(/data-text="[^"]*"/g, '').replace(/<[^>]+>/g, '');
console.log('ok', IS.length, '쟁점', Math.round(html.length / 1024) + 'KB', '본문 글자', plain.replace(/\s+/g, '').length);
