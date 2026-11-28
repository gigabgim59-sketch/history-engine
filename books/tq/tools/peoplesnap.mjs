// th의 인물 사전을 tq로 옮긴다: node tools/peoplesnap.mjs [사용 인물 목록 json]
// 장별 행적(at)은 비운다. 목록을 주면 그 인물만 남긴다. tq에만 있는 인물은 people_extra.mjs(PEOPLEX)에서 더한다.
import fs from 'fs';
const th = '../th/';
const {FACTS, PEOPLE: P0, PDENY: D0} = await import('../../th/people.mjs');
let all = [...P0], deny = {...D0};
for (let n = 1; n <= 6; n++) { const m = await import(`../../th/people_p${n}.mjs`); all.push(...(m['PEOPLE' + n] || [])); Object.assign(deny, m['PDENY' + n] || {}); }
if (fs.existsSync('people_extra.mjs')) { const x = await import('../people_extra.mjs'); all.push(...x.PEOPLEX); Object.assign(deny, x.PDENYX || {}); }
const keep = process.argv[2] ? new Set(JSON.parse(fs.readFileSync(process.argv[2], 'utf8'))) : null;
const out = all.filter(p => !keep || keep.has(p.id)).map(p => { const {at, rel, ...r} = p; return {...r, at: {}}; });
const names = new Set(out.flatMap(p => [p.n, ...(p.al || [])]));
const dn = Object.fromEntries(Object.entries(deny).filter(([k]) => names.has(k)));
fs.writeFileSync('people.mjs', `// th 인물 사전에서 옮겼다(tools/peoplesnap.mjs). 장별 행적은 people_p*.mjs의 AT에 있다.\nexport const FACTS = ${JSON.stringify(FACTS)};\nexport const PEOPLE = ${JSON.stringify(out, null, 0).replace(/\},\{/g, '},\n{')};\nexport const PDENY = ${JSON.stringify(dn)};\n`);
console.log('people', out.length);
