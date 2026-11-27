// 본문 글의 수식·표 마크업(DEFECTS E-16). build·검사 도구가 함께 쓴다. 템플릿과 print/make.mjs에도 같은 규칙이 있다.
//   줄 안 수식: $…$     문단 수식: 문단 전체가 $$…$$     글자 그대로의 달러: \$
//   표: 문단이 '|'로 시작한다. 줄마다 한 행, 칸은 '|'로 가른다. 둘째 줄이 |---|---|이면 첫 줄은 머리 행.
const MRE=/\$\$([\s\S]+?)\$\$|(?<!\\)\$([^$\n]+?)(?<!\\)\$/g;
export function mathSpans(s){const out=[];if(typeof s!=='string'||!s.includes('$'))return out;
  for(const m of s.matchAll(MRE))out.push(m[1]!==undefined?['d',m[1].trim()]:['i',m[2].trim()]);return out;}
export const isTable=s=>typeof s==='string'&&s.startsWith('|');
export const tableRows=s=>s.split('\n').filter(l=>l.trim()).map(l=>l.trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim()));
export const isSep=r=>r.every(c=>/^:?-{3,}:?$/.test(c));
// 분량 셈에 쓰는 글: 수식 마크업을 지우고, 표는 칸 글자만 남긴다
export function plain(s){if(typeof s!=='string')return '';let t=s.replace(MRE,'').replace(/\\\$/g,'$');
  if(isTable(s))t=tableRows(t).filter(r=>!isSep(r)).map(r=>r.join('')).join('');return t;}
