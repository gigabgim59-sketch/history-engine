// 장별 행적 자동 생성: 빌드본(dist)의 감지 결과에서, 장마다 그 인물이 처음 나오는 문장을 행적으로 뽑는다.
// 사용: node build.mjs && node tools/autoat.mjs → people_p1.mjs(AT1), tools/keep.json(쓰인 인물)
import fs from 'fs';
const html = fs.readFileSync('dist/index.html', 'utf8');
const D = JSON.parse(html.match(/const DATA=(.*?);\n/s)[1]);
const PE = Object.fromEntries(D.people.map(p => [p.id, p]));
const ORD = ['주체','원인','전개','배경','영향','안내','갈림','오해'];
const plain = s => String(s).replace(/\[\[[a-z0-9]+\]\]/g, '').replace(/<[^>]+>/g, '');
const sents = b => { const out = []; for (const k of ORD) for (const p of (b[k] || [])) { const t = plain(Array.isArray(p) ? p.join(' ') : p);
  if (t.startsWith('|')) { for (const row of t.split('\n').slice(2)) out.push(row.split('|').filter(Boolean).join(' — ')); }
  else t.split(/(?<=[다요]\.)\s+/).forEach(s => out.push(s.trim())); } return out.filter(Boolean); };
const AT = {}, keep = new Set();
for (const e of D.events) {
  const b = D.body[e.id]; if (!b) continue; const S = sents(b);
  for (const pid of e.pp || []) {
    const p = PE[pid]; const names = [p.n, ...(p.al || [])];
    const hit = S.filter(s => names.some(n => s.includes(n)));
    if (!hit.length) continue;
    let s = hit.find(s => s.length <= 120) || hit[0];
    if (s.length > 140) s = s.slice(0, 130).replace(/\s\S*$/, '') + '…';
    (AT[pid] ||= {})[e.id] = s.replace(/\|/g, ',');
    keep.add(pid);
  }
}
fs.writeFileSync('people_p1.mjs', `// 장별 행적: tools/autoat.mjs가 본문에서 그 인물이 처음 나오는 문장을 뽑았다. 손으로 고친 행적은 people_p2.mjs의 AT2에 둔다(뒤의 것이 앞의 것을 덮는다).\nexport const PEOPLE1 = [];\nexport const AT1 = ${JSON.stringify(AT, null, 0).replace(/\},"/g, '},\n"')};\nexport const REL1 = {};\nexport const PDENY1 = {};\n`);
fs.writeFileSync('tools/keep.json', JSON.stringify([...keep]));
console.log('인물', keep.size, '행적', Object.values(AT).reduce((a, x) => a + Object.keys(x).length, 0));
