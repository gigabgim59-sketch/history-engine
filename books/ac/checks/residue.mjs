// 화면 잔재 검사: node checks/residue.mjs [dist/index.html]
// 메뉴에 보이는 모든 화면(과 첫 화면)을 열어 다음을 찾는다. 하나라도 있으면 실패.
//  1) residue_words.txt의 문구(그 책 DATA에 없는 경우)  2) 수 낱말과 자료 수의 불일치(네 줄기인데 줄기가 다섯 등)
//  3) 자료 없는 화면으로 가는 메뉴  4) 스크립트 오류
import fs from 'fs';import path from 'path';import {fileURLToPath,pathToFileURL} from 'url';
import {loadData} from './_data.mjs';
import {createRequire} from 'module';const require=createRequire(import.meta.url);
const {chromium}=require('playwright');
const here=path.dirname(fileURLToPath(import.meta.url));
const file=path.resolve(process.argv[2]||'dist/index.html');const {D}=loadData(file);
const DATAJSON=JSON.stringify(D);
const words=fs.readFileSync(path.join(here,'residue_words.txt'),'utf8').split('\n').filter(l=>l&&!l.startsWith('#')).map(l=>l.split('\t'));
const NUM={한:1,두:2,세:3,네:4,다섯:5,여섯:6,일곱:7,여덟:8,아홉:9,열:10,열한:11,열두:12};
const COUNT={줄기:(D.threads||[]).length,무대:(D.regions||[]).length,집단:(D.groups||[]).length,힘:(D.engines||[]).length,부:(D.parts||[]).length,축:(D.axes||[]).length,겹:(D.axes||[]).length};
const HAS={pp:(D.people||[]).length,id:(D.groups||[]).length,ln:(D.lineage||[]).length,t:(D.threads||[]).length,econ:D.econ?1:0,air:D.econ?1:0};
const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1280,height:900}});const errs=[];pg.on('pageerror',e=>errs.push('스크립트 오류: '+e.message));
await pg.goto(pathToFileURL(file).href);await pg.waitForTimeout(600);
const tabs=await pg.evaluate(()=>[...document.querySelectorAll('#tabs a[data-v]')].filter(a=>!a.hidden&&a.offsetParent!==null||!a.hidden).map(a=>[a.dataset.v,a.getAttribute('href')]));
const out=[];
for(const [v] of tabs)if(v in HAS&&!HAS[v])out.push(`메뉴 '${v}'가 보이지만 자료가 없음`);
const screens=[['home','#/'],...tabs.filter(([v])=>v!=='home'),
 ...((D.regions||[]).length?[['rr','#/rr/'+D.regions[0].id]]:[]),...((D.groups||[]).length?[['idg','#/id/'+D.groups[0].id]]:[])];
for(const [v,h] of screens){await pg.evaluate(x=>{location.hash=x},h);await pg.waitForTimeout(350);
  const t=await pg.evaluate(()=>document.querySelector('main')?document.querySelector('main').innerText:document.body.innerText);
  for(const [w,why,home] of words){if(home&&home===(D.meta&&D.meta.title))continue;if(t.includes(w)&&!DATAJSON.includes(w))out.push(`${h}: '${w}' (${why})`);}
  for(const m of t.matchAll(/(?<![가-힣])(한|두|세|네|다섯|여섯|일곱|여덟|아홉|열|열한|열두) (줄기|무대|집단|힘|부|축|겹)(?![가-힣])/g)){
    const n=NUM[m[1]],k=m[2],have=COUNT[k];
    if(have&&n!==have&&!DATAJSON.includes(m[0]))out.push(`${h}: '${m[0]}'인데 자료의 ${k}는 ${have}개`);}
}
// 장·부·맺음 화면: 금지 문구만 본다(본문의 수 낱말은 정당한 쓰임이 많다)
const pages=[...(D.parts||[]).map(p=>'#/p/'+p.id),...(D.events||[]).map(e=>'#/e/'+e.id),'#/end'];
for(const h of pages){await pg.evaluate(x=>{location.hash=x},h);await pg.waitForTimeout(120);
  const t=await pg.evaluate(()=>document.querySelector('main')?document.querySelector('main').innerText:'');
  for(const [w,why,home] of words){if(home&&home===(D.meta&&D.meta.title))continue;if(t.includes(w)&&!DATAJSON.includes(w))out.push(`${h}: '${w}' (${why})`);}
  // 템플릿이 만든 제목·설명(h2·라벨·주석)의 수 낱말
  const th=await pg.evaluate(()=>[...document.querySelectorAll('main h2, main .lbl, main .note, main .eyebrow')].map(x=>x.innerText).join('\n'));
  for(const m of th.matchAll(/(?<![가-힣])(한|두|세|네|다섯|여섯|일곱|여덟|아홉|열|열한|열두) (줄기|무대|집단|힘|부|축|겹)(?![가-힣])/g)){
    const n=NUM[m[1]],k=m[2],have=COUNT[k];
    if(have&&n!==have&&!DATAJSON.includes(m[0]))out.push(`${h}: '${m[0]}'인데 자료의 ${k}는 ${have}개`);}}
await b.close();
const all=[...new Set([...out,...errs])];
console.log(all.length?all.join('\n'):'잔재 없음');process.exit(all.length?1:0);
