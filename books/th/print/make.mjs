// A4 인쇄본(줄글만): node print/make.mjs [책 HTML, 기본 dist/index.html]
// 책 폴더에서 실행한다. print/render.py가 이 도구를 부르고, 쪽수·조임 정보(print/state.json)를 넘긴다.
// 절 이름과 상자 이름은 그 책 HTML의 템플릿에서 읽는다. 그래서 화면판과 인쇄본의 이름이 같다(DEFECTS P-05·P-07).
// 덮어쓰기: print/meta.json(선택) — title, sub, eyebrow, span, endT, printFoot, introPrint(배열), engines, engn 등.
//   introPrint가 없으면 머리말에서 화면을 가리키는 문장(누르면·화면·메뉴·밑줄·서가에는 …)을 빼고 쓰고, 뺀 문장을 알린다.
import fs from 'fs';
const SRC = process.argv[2] || 'dist/index.html';
const s = fs.readFileSync(SRC, 'utf8');
const D = JSON.parse(s.match(/const DATA=(.*?);\n/s)[1]);
const OV = fs.existsSync('print/meta.json') ? JSON.parse(fs.readFileSync('print/meta.json', 'utf8')) : {};
const M = { ...(D.meta || {}), ...OV };
const ST = fs.existsSync('print/state.json') ? JSON.parse(fs.readFileSync('print/state.json', 'utf8')) : {};
const TOC = ST.toc || {}, TIGHT = ST.tight || {};
if (!M.title) { console.error('제목 없음: DATA.meta.title도 print/meta.json의 title도 없다'); process.exit(1); }

// ── 그 책 템플릿에서 이름 읽기 ──
const grab = (re, def) => { const m = s.match(re); return m ? m[1] : def; };
let SLOTH = D.sloth || null;
if (!SLOTH) { const m = s.match(/const SLOTH=(\{.*?\});/s); SLOTH = m && !/DATA/.test(m[1]) ? Function('return ' + m[1])() : {}; }
let ENG = OV.engines || D.engines || null;
if (!ENG) { const m = s.match(/\$\{(\[\[.*?\]\])\.map\(\(\[k,n\]\)/s); ENG = m ? Function('return ' + m[1])() : []; }
const L = {
  guide: grab(/class="keys guide"><p class="lbl">([^<$]+)<\/p>/, '먼저 알아 둘 것'),
  eff: grab(/<section class="slot"><h2>(영향[^<$]*)<\/h2>/, null) || grab(/\|\|'(영향[^']*)'\)\}<\/h2>/, '영향'),
  hv: M.hvl || grab(/class="box hvb"><p class="lbl">([^<$]+)<\/p>/, '관점들의 풀이'),
  deb: M.debl || grab(/class="box deb"><p class="lbl">([^<$]+)<\/p>/, '해석의 갈림'),
  myth: grab(/class="box myth"><p class="lbl">([^<$]+)<\/p>/, '흔한 오해'),
  sum: grab(/p\.sum\?`<section class="slot"><h2>([^<$]+)<\/h2>/, '이 부에서 바뀐 것'),
  eng: M.engn ? '이 시대의 ' + M.engn : grab(/<h2 class="sh">(이 시대의 [^<$]+)<\/h2><div class="f3">/, '이 시대의 힘'),
  meet: grab(/<p class="lbl">([^<$]+)<\/p><p>\$\{linky\(p\.f\.meet\)\}/, '고리들이 맞물리는 곳'),
  lead: grab(/<p class="lbl">([^<$]+)<\/p><p>\$\{linky\(p\.lead\)\}/, '이 시대의 큰 그림'),
};
const NUMW = ['영', '한', '두', '세', '네', '다섯', '여섯', '일곱', '여덟', '아홉', '열', '열한', '열두', '열세', '열네', '열다섯'];
const kn = n => NUMW[n] || String(n);
const josa = (w, a, b) => { const c = [...w].reverse().find(ch => /[가-힣]/.test(ch)); return c && (c.charCodeAt(0) - 0xac00) % 28 ? a : b; };

// ── 글 다듬기 ──
const E = Object.fromEntries(D.events.map(e => [e.id, e]));
const esc = x => String(x).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const ref = t => t.replace(/(?:\[\[(\w+)\]\])+/g, m => {
  const ids = [...m.matchAll(/\[\[(\w+)\]\]/g)].map(r => r[1]).filter(x => E[x]);
  return ids.length ? `<span class="xr">(${ids.map(x => `<a href="#c-${x}">${E[x].no}</a>`).join('·')}장)</span>` : '';
});
// 수식·표(DEFECTS E-16): 빌드가 만든 MathML(D.math)을 넣는다. 규칙은 checks/_text.mjs와 같다
const MATH = D.math || {};
const MRE = /\$\$([\s\S]+?)\$\$|(?<!\\)\$([^$\n]+?)(?<!\\)\$/g;
const mathHtml = (d, t) => MATH[d + ':' + t.trim()] || esc(t);
const rich0 = x => ref(esc(x).replace(/&lt;(\/?)(b|i|em|strong)&gt;/g, '<$1$2>'));
const rich = x => { const ms = []; x = String(x); if (x.includes('$')) x = x.replace(MRE, (m, a, b) => { ms.push(a !== undefined ? ['d', a] : ['i', b]); return '\u0003' + (ms.length - 1) + '\u0004'; }).replace(/\\\$/g, '$');
  const h = rich0(x); return ms.length ? h.replace(/\u0003(\d+)\u0004/g, (m, i) => mathHtml(...ms[+i])) : h; };
const tRows = x => x.split('\n').filter(l => l.trim()).map(l => l.trim().replace(/^\||\|$/g, '').split('|').map(c => c.trim()));
const tSep = r => r.every(c => /^:?-{3,}:?$/.test(c));
const tbl = x => { const rows = tRows(x), hd = rows.length > 1 && tSep(rows[1]), bd = hd ? rows.slice(2) : rows;
  return `<table class="mt">${hd ? `<thead><tr>${rows[0].map(c => `<th>${rich(c)}</th>`).join('')}</tr></thead>` : ''}<tbody>${bd.map(r => `<tr>${r.map(c => `<td>${rich(c)}</td>`).join('')}</tr>`).join('')}</tbody></table>`; };
const paras = (a, cls = '') => (a || []).map(x => x.startsWith('## ') ? `<p class="h4">${esc(x.slice(3))}</p>`
  : /^\$\$[\s\S]+\$\$$/.test(x.trim()) ? `<div class="mblk">${mathHtml('d', x.trim().slice(2, -2))}</div>`
  : x.startsWith('|') ? tbl(x) : `<p${cls ? ` class="${cls}"` : ''}>${rich(x)}</p>`).join('');
const KIND = Object.fromEntries((D.kinds || []).map(k => [k[0], k[1]]));
const KD0 = D.kinds && D.kinds[0] ? D.kinds[0][0] : null;
const tight = id => TIGHT[id] ? ` tg${TIGHT[id]}` : '';

// ── 머리말: 화면을 가리키는 문장 ──
const UI = /누르면|눌러|화면|메뉴|밑줄|클릭|탭에서|맨 위 띠|아래의 ‘다음’|서가에는|서가에서|서가의|점선|이어 읽기|지도에서|연결망에서|연표에서/;
const dropped = [];
let intro = M.introPrint;
if (!intro) {
  // introReplace: [[원문 일부, 인쇄본 문구], …] — 화면을 가리키는 구절만 바꿔 쓸 때
  const rep = p => (M.introReplace || []).reduce((t, [a, b]) => t.split(a).join(b), p);
  intro = (M.intro || []).map(rep).map(p => {
    const ss = p.split(/(?<=[.?!])\s+/);
    const keep = ss.filter(x => { if (UI.test(x)) { dropped.push(x); return false; } return true; });
    return keep.join(' ');
  }).filter(x => x.trim());
}

// ── 앞붙이 ──
const seq = []; // [id, 북마크 이름, 단계]
let front = '', body = '';
front += `<section class="title"><div class="bar"></div><p class="t1">${esc(M.title)}</p><p class="tsub">${esc(M.sub || '')}</p>${M.eyebrow ? `<p class="tey">${esc(M.eyebrow)}</p>` : ''}
<div class="tfoot"><p>${esc(M.printFoot || M.span || '')}</p></div></section>`;
const hasW = Object.values(D.body).some(b => b['말'] && b['말'].length), hasK = Object.values(D.body).some(b => b['작품'] && b['작품'].length);
const only = [];
if (hasW || hasK) only.push('장마다 붙은 ' + (hasW && hasK ? '그 시대의 말과 작품' : hasW ? '그 시대의 말' : '작품 목록'));
if ((D.people || []).length) only.push(`인물 사전 ${D.people.length}명`);
if ((D.terms || []).length) only.push(`용어 ${D.terms.length}개`);
if ((D.books || []).length) only.push(`서가 ${D.books.length}권`);
const mapOK = !M.nomap && D.land, lanesOK = !M.nolanes && (D.regions || []).length;
if (mapOK || lanesOK) only.push(mapOK && lanesOK ? '지도와 연표' : mapOK ? '지도' : '연표');
only.push(D.linkk ? '연결망' : '사건 연결망');
if (D.econ) only.push('경제 지표');
if ((D.groups || []).length) only.push('‘사람들의 변화’ 표');
const last = only[only.length - 1];
front += `<section class="colo"><p>이 책은 『${esc(M.title)}』 HTML판의 줄글만 모은 인쇄본이다. ${esc(only.join(', '))}${josa(last, '은', '는')} HTML판에서 볼 수 있다.</p><p>본문 속 (3장)과 같은 표시는 함께 읽을 장을 가리킨다. 차례와 장 표시를 누르면 그 쪽으로 간다.</p></section>`;
let toc = '<section class="toc"><p class="toch">차례</p><table>';
const row = (id, a, b, cls = '') => `<tr${cls ? ` class="${cls}"` : ''}>${a}<td><a href="#c-${id}">${b}</a></td><td><a href="#c-${id}">${TOC[id] || ''}</a></td></tr>`;
toc += row('intro', '', '머리말', 'tp').replace('<td><a', '<td colspan="2"><a');
for (const p of D.parts) {
  toc += row(p.id, '', `${esc(p.no)} ${esc(p.t)} <span class="ty">${esc(p.y)}</span>`, 'tp').replace('<td><a', '<td colspan="2"><a');
  for (const e of D.events.filter(e => e.p === p.id)) toc += row(e.id, `<td class="tn">${e.no}</td>`, esc(e.t));
}
toc += row('end', '', '맺음', 'tp').replace('<td><a', '<td colspan="2"><a') + '</table></section>';
front += toc;

// ── 본문 ──
seq.push(['intro', '머리말', 0]);
body += `<section class="ch${tight('intro')}" id="c-intro"><div class="open"><h1 class="ct"><span class="kick">머리말</span><span class="tt">이 책을 읽기 전에</span></h1><div class="rule"></div></div>${paras(intro)}</section>`;
for (const p of D.parts) {
  seq.push([p.id, `${p.no} ${p.t}`, 0]);
  body += `<section class="part${tight(p.id)}" id="c-${p.id}"><h1 class="ph"><span class="pno">${esc(p.no)}</span><span class="pt">${esc(p.t)}</span></h1><p class="py">${esc(p.y)}</p><div class="rule"></div>`;
  if (p.lead) body += `<p class="h3">${esc(L.lead)}</p><p>${rich(p.lead)}</p>`;
  if (p.bgx && p.bgx.length) body += paras(p.bgx);
  if (p.f && ENG.length) {
    body += `<p class="h3">${esc(L.eng)}</p>` + ENG.map(([k, n]) => p.f[k] ? `<p class="fh">${esc(n)}</p><p>${rich(p.f[k])}</p>` : '').join('');
    if (p.f.meet) body += `<p class="fh">${esc(L.meet)}</p><p>${rich(p.f.meet)}</p>`;
  }
  if (p.bg && (D.regions || []).length) {
    body += `<p class="h3">이 시대의 ${kn(D.regions.length)} 무대</p>` + D.regions.map(r => p.bg[r.id] ? `<p class="fh">${esc(r.n)}</p><p>${rich(p.bg[r.id])}</p>` : '').join('');
    if (p.bg.pe) body += `<p class="fh">${esc(M.pen || '세계')}</p><p>${rich(p.bg.pe)}</p>`;
  }
  if (p.sum && p.sum.length) body += `<p class="h3">${esc(L.sum)}</p>` + paras(p.sum);
  body += '</section>';
  for (const e of D.events.filter(e => e.p === p.id)) {
    const B = D.body[e.id] || {};
    seq.push([e.id, `${e.no}. ${e.t}`, 1]);
    const kd = e.kd && KD0 && e.kd !== KD0 && KIND[e.kd] ? ' · ' + KIND[e.kd] : '';
    const pl = !M.nomap && e.pl && (Array.isArray(e.pl) ? e.pl[0] : String(e.pl).split(',')[0]);
    body += `<section class="ch${tight(e.id)}" id="c-${e.id}"><div class="open"><p class="kick2">${esc(p.no)} ${esc(p.t)}</p><h2 class="ct"><span class="kick">제${e.no}장${esc(kd)}</span><span class="tt">${esc(e.t)}</span></h2><p class="cy">${esc(e.y)}${pl ? ' · ' + esc(pl) : ''}</p><div class="rule"></div></div>`;
    body += `<p class="lead">${rich(e.s)}</p>`;
    const sec = (lab, a) => a && a.length ? `<p class="h3">${esc(lab)}</p>` + paras(a) : '';
    body += sec(L.guide, B['안내']);
    for (const h of ['배경', '원인', '주체', '전개']) body += sec((SLOTH[e.kd] || {})[h] || h, B[h]);
    body += sec((SLOTH[e.kd] || {})['영향'] || L.eff, B['영향']);
    if (B['사관'] && B['사관'].length) body += `<p class="h3">${esc(L.hv)}</p>` + B['사관'].map(([a, t]) => `<p class="fh">${esc(a)}</p><p>${rich(t)}</p>`).join('');
    body += sec(L.deb, B['갈림']);
    body += sec(L.myth, B['오해']);
    body += '</section>';
  }
}
seq.push(['end', '맺음', 0]);
body += `<section class="ch${tight('end')}" id="c-end"><div class="open"><h1 class="ct"><span class="kick">맺음</span><span class="tt">${esc(M.endT || M.title)}</span></h1><div class="rule"></div></div>${paras(D.concl)}</section>`;

const css = fs.readFileSync(new URL('./print.css', import.meta.url), 'utf8');
const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>${esc(M.title)}</title><style>/*__FONTS__*/\n${css}</style></head><body><div class="front">${front}</div><div class="main">${body}</div></body></html>`;
fs.mkdirSync('print', { recursive: true });
fs.writeFileSync('print/book.html', html);
fs.writeFileSync('print/seq.json', JSON.stringify({ title: M.title, sub: M.sub || '', pfx: M.pfx || null, seq }));
if (dropped.length && !M.introPrint) console.error('머리말에서 뺀 문장(화면을 가리킴) ' + dropped.length + '개:\n  ' + dropped.join('\n  ') + '\n  → 어색하면 print/meta.json에 introPrint를 쓴다');
console.log('ok', seq.length, '구획');
