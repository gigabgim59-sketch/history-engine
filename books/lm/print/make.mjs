// A4 인쇄본: 줄글만. node print/make.mjs [toc.json]
import fs from 'fs';
const s=fs.readFileSync('dist/index.html','utf8');const D=JSON.parse(s.match(/const DATA=(.*?);\n/s)[1]);
const TOC=fs.existsSync('print/toc.json')?JSON.parse(fs.readFileSync('print/toc.json','utf8')):{};
const esc=x=>String(x).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const ref=x=>esc(x).replace(/(?:\[\[l(\d\d)\]\])+/g,m=>'<span class="xr">('+[...m.matchAll(/l(\d\d)/g)].map(r=>+r[1]).join('·')+'장)</span>');
const rich=x=>ref(String(x).replace(/<\/?b>/g,'\u0001')).replace(/\u0001([^\u0001]*)\u0001/g,'<b>$1</b>');
const SL={배경:'문제',원인:'정식화',주체:'현실로 간 관념',전개:'왜곡과 변형',영향:'남은 것'};
const SM={배경:'배경',원인:'세워지기까지',주체:'사람들',전개:'전개',영향:'남긴 것'};
const ORDER=['배경','원인','주체','전개','영향','갈림','오해'];
const lab=(e,k)=>k==='갈림'?'해석의 갈림':k==='오해'?'흔한 오해':(e.kd==='me'?SM:SL)[k];
const P=Object.fromEntries(D.parts.map(p=>[p.id,p]));
const mk=id=>`<span class="mk">§${id}§</span>`;
let front='',body='';
// 표제지
front+=`<section class="title"><div class="bar"></div><h1>${esc(D.meta.title)}</h1><p class="tsub">${esc(D.meta.sub)}</p><p class="tey">${esc(D.meta.eyebrow)}</p>
<div class="tfoot"><p>계몽주의 사상사 · 1680–오늘</p></div></section>`;
// 일러두기
front+=`<section class="colo"><p>이 책은 『계몽의 갈래』 HTML판의 줄글만 모은 인쇄본이다. 장마다 붙은 그 시대의 말과 작품, 인물 사전 187명, 용어 106개, 서가 155권, 지도와 연표, 사건 연결망, ‘사람들의 변화’ 표는 HTML판에서 볼 수 있다.</p><p>본문 속 (3장)과 같은 표시는 함께 읽을 장을 가리킨다.</p></section>`;
// 차례
let toc='<section class="toc"><h2 class="toch">차례</h2><table>';
toc+=`<tr class="tp"><td colspan="2">머리말</td><td>${TOC.intro||''}</td></tr>`;
for(const p of D.parts){toc+=`<tr class="tp"><td colspan="2">${esc(p.no)} ${esc(p.t)} <span class="ty">${esc(p.y)}</span></td><td>${TOC[p.id]||''}</td></tr>`;
 for(const e of D.events.filter(e=>e.p===p.id))toc+=`<tr><td class="tn">${e.no}</td><td>${esc(e.t)}</td><td>${TOC[e.id]||''}</td></tr>`;}
toc+=`<tr class="tp"><td colspan="2">맺음</td><td>${TOC.end||''}</td></tr></table></section>`;
front+=toc;
// 머리말
body+=`<section class="ch">${mk('intro')}<div class="open"><p class="kick">머리말</p><h2 class="ct">이 책을 읽기 전에</h2><div class="rule"></div></div>${D.meta.intro.map(x=>`<p>${rich(x)}</p>`).join('')}</section>`;
for(const p of D.parts){
 body+=`<section class="part">${mk(p.id)}<p class="pno">${esc(p.no)}</p><h2 class="pt">${esc(p.t)}</h2><p class="py">${esc(p.y)}</p><div class="rule"></div>`;
 for(const x of p.bgx) body+=x.startsWith('## ')?`<h3>${esc(x.slice(3))}</h3>`:`<p>${rich(x)}</p>`;
 const F=[['top','사상가'],['bot','권력'],['out','대중과 수용자'],['meet','세 힘이 만난 자리']];
 body+=`<h3>세 힘</h3>`+F.map(([k,l])=>`<p><b class="fl">${l}</b> ${rich(p.f[k])}</p>`).join('');
 body+=`<h3>이 부가 남긴 것</h3>`+p.sum.map(x=>`<p>${rich(x)}</p>`).join('')+`</section>`;
 for(const e of D.events.filter(e=>e.p===p.id)){
  const B=D.body[e.id];
  body+=`<section class="ch">${mk(e.id)}<div class="open"><p class="kick2">${esc(p.no)} ${esc(p.t)}</p><p class="kick">제${e.no}장${e.kd==='me'?' · 조직과 사건':''}</p><h2 class="ct">${esc(e.t)}</h2><p class="cy">${esc(e.y)}${e.pl?' · '+esc(Array.isArray(e.pl)?e.pl[0]:String(e.pl).split(',')[0]):''}</p><div class="rule"></div></div>`;
  body+=`<p class="lead">${ref(e.s)}</p>`;
  for(const k of ORDER){if(!B[k]||!B[k].length)continue;body+=`<h3>${lab(e,k)}</h3>`+B[k].map(x=>`<p>${ref(x)}</p>`).join('')}
  body+=`</section>`;}
}
body+=`<section class="ch">${mk('end')}<div class="open"><p class="kick">맺음</p><h2 class="ct">계몽의 갈래</h2><div class="rule"></div></div>`+D.concl.map(x=>x.startsWith('## ')?`<h3>${esc(x.slice(3))}</h3>`:`<p>${ref(x)}</p>`).join('')+`</section>`;
const css=fs.readFileSync('print/print.css','utf8');
const page=(cls,inner)=>`<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${css}</style></head><body class="${cls}">${inner}</body></html>`;
fs.writeFileSync('print/front.html',page('front',front));fs.writeFileSync('print/body.html',page('main',body));
console.log('ok');
