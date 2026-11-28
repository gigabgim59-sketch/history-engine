// 용어(terms.mjs)·서지(books.mjs)·맺음(concl.mjs) 생성: node tools/extras.mjs
// 용어: 장마다의 '말'을 모은다. 서지: th의 원서 서가에서 관련 장의 책을 가져온다. 맺음: 아래 문단과 쟁점×전통 표.
import fs from 'fs';
import path from 'path';
import {pathToFileURL} from 'url';
const SRC = path.resolve('src');
const imp = f => import(pathToFileURL(path.join(SRC, f)).href);
const {EVENTS} = await import('../events.mjs');
const B = {};
for (const f of fs.readdirSync('.').filter(f => /^body_p\d[a-z]?\.mjs$/.test(f)).sort()) Object.assign(B, ...Object.values(await import('../' + f)));
// 용어
const CAT = {p1:'신론',p2:'계시와 성경',p3:'인간과 죄',p4:'그리스도와 구원',p5:'그리스도와 구원',p6:'교회와 성례',p7:'종말과 창조',p8:'교파와 전통'};
const seen = new Set(), TERMS = [];
for (const e of EVENTS) for (const [t, d] of (B[e.id]?.말 || [])) { if (seen.has(t)) continue; seen.add(t); TERMS.push([t, d, CAT[e.p]]); }
fs.writeFileSync('terms.mjs', `// 용어: tools/extras.mjs가 장마다의 '말'에서 모은다\nexport const TCATS=${JSON.stringify([...new Set(Object.values(CAT))])};\nexport const TERMS=${JSON.stringify(TERMS, null, 0).replace(/\],\[/g, '],\n[')};\n`);
// 서지
const TB = await import('../../th/books.mjs');
const issues = [...(await imp('issues_a.mjs')).IA, ...(await imp('issues_b.mjs')).IB, ...(await imp('issues_c.mjs')).IC, ...(await imp('issues_d.mjs')).ID, ...(await imp('issues_e.mjs')).IE];
const CFTH = {tq27:['th17','th16','th09'],tq28:['th15','th23','th36'],tq29:['th20','th19','th21'],tq30:['th24','th27','th21'],tq31:['th18','th54'],tq32:['th32','th31'],tq33:['th58'],tq34:['th22']};
const chmap = Object.fromEntries(issues.map(q => ['tq' + q.id.slice(1), q.ch || []]));
Object.assign(chmap, CFTH);
const BK = {}, used = new Set();
for (const [tq, ths] of Object.entries(chmap)) {
  const rows = [];
  for (const th of ths) for (const r of (TB.BK[th] || [])) if (!rows.some(x => x[0] === r[0])) rows.push([r[0], `『같은 성경, 다른 답』 ${+th.slice(2)}장 서가에서 — ${r[1]}`]);
  if (rows.length) { BK[tq] = rows.slice(0, 5); rows.slice(0, 5).forEach(r => used.add(r[0])); }
}
const BOOKS = TB.BOOKS.filter(b => used.has(b.id));
fs.writeFileSync('books.mjs', `// 서지: tools/extras.mjs가 th의 원서 서가에서 관련 장의 책을 가져온다(원서만, th와 같은 확인 상태)\nexport const BOOKS=${JSON.stringify(BOOKS, null, 0).replace(/\},\{/g, '},\n{')};\nexport const BK=${JSON.stringify(BK, null, 1)};\n`);
// 맺음
const {COMPARE} = await imp('appendix.mjs');
const cell = s => String(s).replace(/\|/g, '/');
const qn = q => 'tq' + q.slice(1);
const table = '|쟁점|' + COMPARE.cols.join('|') + '|\n|' + ['---', ...COMPARE.cols.map(() => '---')].join('|') + '|\n' + COMPARE.rows.map(r => `|${r[0]}(${qn(r.at(-1))})|` + r.slice(1, -1).map(cell).join('|') + '|').join('\n');
const CONCL = [
 '## 처음의 물음',
 '이 책은 두 가지를 물었다. 기독교 신학의 주요 쟁점마다 전통들은 어떤 답을 내고 어떤 성경 본문과 논거에 기대는가. 그리고 각 교파의 답들은 그 교파의 근본 명제에서 어떻게 일관되게 이어지는가. 제1~7부의 스물여섯 쟁점 장이 첫 물음에, 제8부의 여덟 교파 장이 둘째 물음에 답했다. 여기서는 그 답을 판정하지 않고, 쟁점과 교파를 한 표로 겹쳐 놓고 갈림의 축으로 다시 정리한다.',
 '## 같은 본문, 다른 독해',
 '쟁점 장마다 둔 ‘같은 본문, 다른 독해’는 한 가지를 거듭 보여 주었다. 다툼은 대개 성경을 받느냐 받지 않느냐가 아니라 같은 구절을 어떤 틀로 읽느냐에서 생겼다. 롬 5:12의 한 전치사구[[tq09]], 롬 3:28의 ‘믿음으로’[[tq14]], 마 26:26의 ‘이다’[[tq20]], 계 20장의 천년[[tq23]], 마 25:46의 ‘영원한’[[tq24]]이 그 예다. 그 틀은 각 전통의 근본 명제였다. 그래서 쟁점 장의 독해 차이는 교파 장의 근본 명제로 되돌아가 읽을 때 일관된 모양을 얻는다.',
 '## 쟁점과 전통의 표',
 '아래 표는 열여섯 쟁점에서 여덟 전통이 공식 문서나 대표 신학자의 글로 낸 답을 줄여 적은 것이다. 넓은 전통(성공회·감리교·오순절·침례교)의 다양성은 크게 줄였다. 표의 각 줄은 괄호 안의 쟁점 장에, 각 열은 제8부의 교파 장에 자세한 서술이 있다.',
 table,
 '## 여덟 축으로 본 갈림',
 '<b>계시와 이성, 역사와 초월.</b> 하나님은 어떻게 알려지고 성경은 어떤 권위를 가지는가[[tq04]][[tq05]][[tq06]]. 가톨릭과 정교회는 교회의 전승 안에서, 개신교는 교회 위의 성경에서 출발한다. 같은 개신교 안에서 무오의 범위[[tq05]]와 창조의 해석[[tq26]]이 다시 갈렸다.',
 '<b>초월과 내재.</b> 하나님은 세계와 어떻게 관계하시는가[[tq02]][[tq03]]. 이 축은 성찬에서 그리스도가 어떻게 계시는가[[tq20]]와 그리스도의 두 본성[[tq11]]에까지 이어진다.',
 '<b>주권과 자유, 은총과 응답.</b> 구원의 결정적 원인은 어디에 있는가[[tq08]][[tq09]][[tq13]][[tq15]]. 개혁주의의 주권, 루터교의 오직 은혜, 가톨릭과 정교회의 협력, 웨슬리의 선행은총은 이 축 위의 서로 다른 자리다[[tq29]][[tq30]][[tq28]][[tq27]][[tq32]].',
 '<b>법정과 변화.</b> 구원은 신분의 변화인가 존재의 변화인가[[tq14]][[tq25]]. 전가와 신화와 성화가 이 축 위에 놓이고, 칭의 공동선언(1999)은 이 축의 오랜 대립을 다시 다루었다.',
 '<b>정의와 사랑, 보편과 특수.</b> 하나님의 보편적 구원 의지와 그리스도의 유일성, 심판의 정의는 어떻게 함께 서는가[[tq12]][[tq16]][[tq24]]. 이 축에서는 교파 사이보다 교파 안의 목소리가 더 크게 갈렸다.',
 '## 일관성은 어디에 있었나',
 '여덟 교파 장은 일관성이 전통마다 다른 자리에 있음을 보여 주었다. 정교회와 가톨릭은 구원론·성례론·교회론이 하나의 원리(신화, 은총과 본성)로 이어진다. 루터교와 개혁주의는 구원론(칭의, 주권)에서 출발해 성례와 교회로 넓어진다. 성공회는 예배와 질서에서, 침례교·자유교회는 교회론에서, 감리교와 오순절은 성화와 성령의 체험에서 일관성을 찾는다. 그래서 어떤 쟁점에서는 한 교파 안의 답이 하나로 모이고, 어떤 쟁점에서는 넓게 흩어진다.',
 '그 일관성은 그 전통의 강점이면서 비판이 들어오는 자리였다. 한 명제가 한 영역에서 낳은 결론을 다른 전통이 받을 수 없을 때 쟁점이 생겼고, 같은 전통 안에서 그 결론을 끝까지 밀 것인가를 두고 다시 갈림이 생겼다. 교파 장마다 끝에 둔 ‘주요 난제와 비판’은 그 자리를 기록한 것이다.',
 '## 남은 물음',
 '어느 답이 성경에 맞는지는 이 책의 물음이 아니었다. 이 책은 답들을 나란히 놓고 그 답들이 어디서 나왔는지를 보이려 했다. 시대 순의 갈림은 짝을 이루는 『같은 성경, 다른 답』에 있다. 읽는 이가 각 전통의 글로 돌아가 판단할 몫은 그대로 남는다.'
];
fs.writeFileSync('concl.mjs', `// 맺음: tools/extras.mjs가 만든다(쟁점×전통 표는 원고 부록의 비교표)\nexport const CONCL = ${JSON.stringify(CONCL, null, 1)};\n`);
console.log('terms', TERMS.length, 'books', BOOKS.length, 'bk', Object.keys(BK).length);
