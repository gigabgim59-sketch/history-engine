import fs from 'fs';
import {build} from './geo.mjs';
import * as D0 from './data.mjs';
import * as A from './data_add.mjs';
import * as A2 from './data_add2.mjs';
import {RH} from './rh.mjs';
import * as A3 from './data_add3.mjs';
import * as A4 from './data_add4.mjs';
import * as A5 from './data_add5.mjs';
import {FORCES} from './data_parts.mjs';
import {PBG,PSUM,CONCL} from './data_pbg.mjs';
import {BODY as B0} from './body.mjs';
import {BODY_P1} from './body_p1.mjs';
import {BODY_P1B} from './body_p1b.mjs';
import {BODY_P1C} from './body_p1c.mjs';
import {BODY_P1D} from './body_p1d.mjs';
import {BODY_P1E} from './body_p1e.mjs';
import {BODY_P2} from './body_p2.mjs';
import {BODY_P2B} from './body_p2b.mjs';
import {BODY_P2C} from './body_p2c.mjs';
import {BODY_P2D} from './body_p2d.mjs';
import {BODY_P2E} from './body_p2e.mjs';
import {BODY_P2F} from './body_p2f.mjs';
import {BODY_P2G} from './body_p2g.mjs';
import {BODY_P2H} from './body_p2h.mjs';
import {BODY_P2I} from './body_p2i.mjs';
import {BODY_P3} from './body_p3.mjs';
import {BODY_P3B} from './body_p3b.mjs';
import {BODY_P3C} from './body_p3c.mjs';
import {BODY_P3D} from './body_p3d.mjs';
import {BODY_P3E} from './body_p3e.mjs';
import {BODY_P3F} from './body_p3f.mjs';
import {BODY_P3G} from './body_p3g.mjs';
import {BODY_P3H} from './body_p3h.mjs';
import {BODY_P3I} from './body_p3i.mjs';
import {BODY_P5X} from './body_p5x.mjs';
import {BODY_P4} from './body_p4.mjs';
import {BODY_P4B} from './body_p4b.mjs';
import {BODY_P4C} from './body_p4c.mjs';
import {BODY_P4D} from './body_p4d.mjs';
import {BODY_P4E} from './body_p4e.mjs';
import {BODY_P4F} from './body_p4f.mjs';
import {BODY_P5A} from './body_p5a.mjs';
import {BODY_P5B} from './body_p5b.mjs';
import {BODY_P5C} from './body_p5c.mjs';
import {BODY_P5D} from './body_p5d.mjs';
import {BODY_P5E} from './body_p5e.mjs';
import {TERMS5} from './data_terms5.mjs';
import {TERMS6} from './data_terms6.mjs';
import {LINEAGE,LCATS} from './data_lineage.mjs';
import * as LBX from './data_lnb.mjs';
import {GUIDE_P1} from './guide_p1.mjs';
import {GUIDE_P2} from './guide_p2.mjs';
import {GUIDE_P3} from './guide_p3.mjs';
import {GUIDE_P4} from './guide_p4.mjs';
import {GUIDE_P5} from './guide_p5.mjs';
import {BODY_P5F} from './body_p5f.mjs';
const BODY={...B0,...BODY_P5F,...BODY_P5E,...BODY_P5D,...BODY_P5C,...BODY_P5B,...BODY_P5A,...BODY_P4F,...BODY_P4E,...BODY_P4D,...BODY_P4C,...BODY_P4B,...BODY_P4,...BODY_P5X,...BODY_P3,...BODY_P3I,...BODY_P3H,...BODY_P3G,...BODY_P3F,...BODY_P3E,...BODY_P3D,...BODY_P3C,...BODY_P3B,...BODY_P2,...BODY_P2I,...BODY_P2H,...BODY_P2G,...BODY_P2F,...BODY_P2E,...BODY_P2B,...BODY_P2C,...BODY_P2D,...BODY_P1,...BODY_P1B,...BODY_P1C,...BODY_P1D,...BODY_P1E};
const PO={p1:0,p2:1,p3:2,p4:3,p5:4};
const ALL=[...D0.EVENTS,...A.EVENTS_ADD,...A2.EVENTS_ADD2,...A3.EVENTS_ADD3,...A4.EVENTS_ADD4,...A5.EVENTS_ADD5].sort((a,b)=>PO[a.p]-PO[b.p]||a.yr-b.yr);
ALL.forEach(e=>{if(A2.NX_ADD[e.id])e.nx=[...e.nx,...A2.NX_ADD[e.id]];if(A5.NX_ADD5[e.id])e.nx=[...e.nx,...A5.NX_ADD5[e.id]];if(A4.NX_ADD4[e.id])e.nx=[...e.nx,...A4.NX_ADD4[e.id]];if(A4.BK_KSY[e.id])e.bk=[...(e.bk||[]),...A4.BK_KSY[e.id]];if(A3.BK_ADD[e.id])e.bk=[...(e.bk||[]),...A3.BK_ADD[e.id]];});
const GR=[...D0.GROUPS.slice(0,2),A2.GROUP_PARSI,D0.GROUPS[2],A.GROUP_ADD,...D0.GROUPS.slice(3),A3.GROUP_SAR].map(g=>({...g,ch:[...g.ch,...(A2.GROUP_CH_ADD[g.id]||[]),...(A5.GROUP_CH_ADD5[g.id]||[])]}));
const T1=[...A.TIER1,...A2.TIER1_ADD,...A3.TIER1_ADD3,...A4.TIER1_ADD4,'x06'],T3=[...A.TIER3,...A2.TIER3_ADD,...A3.TIER3_ADD3].filter(x=>!T1.includes(x));
const D={...D0,TERMS:(()=>{const CAT={울루스:'개념·제도',카간:'개념·제도',칸:'개념·제도',칼리프:'개념·제도',술탄:'개념·제도',샤:'개념·제도',움마:'종교·사상',굴람:'개념·제도',맘룩:'민족·집단',수니파:'종교·사상',시아파:'종교·사상',수피즘:'종교·사상',바르나:'개념·제도',자티:'개념·제도',박띠:'종교·사상',베다:'문헌',아베스타:'문헌',디아스포라:'개념·제도',랍비:'종교·사상',야를릭:'개념·제도',쥐즈:'민족·집단',투르크화:'개념·제도',텡그리:'종교·사상',오구즈:'민족·집단',킵착:'민족·집단',카를룩:'민족·집단',사르트:'민족·집단',마와라안나흐르:'땅이름',투르키스탄:'땅이름',정교:'종교·사상','제3의 로마':'종교·사상',탄지마트:'개념·제도','민족 경계 획정':'개념·제도',니스바:'언어·문자',인도유럽어족:'언어·문자',얌나야:'민족·집단',미탄니:'왕조·국가',후르리어:'언어·문자',마리야누:'민족·집단',데바:'종교·사상',다에바:'종교·사상',아수라:'종교·사상',아샤:'종교·사상',리타:'종교·사상',소마:'종교·사상',하오마:'종교·사상',쿠트:'종교·사상',딤미:'개념·제도',마왈리:'민족·집단',슈우비야:'개념·제도','투르크-페르시아':'개념·제도',투란:'땅이름','달라이 라마':'종교·사상',겔룩파:'종교·사상','칭기즈 혈통':'개념·제도','합동 교회':'종교·사상',바랴기:'민족·집단',유라시아주의:'종교·사상',힌두트바:'종교·사상',드라비다어족:'언어·문자',아리야바르타:'땅이름'};const base=[...D0.TERMS,...A4.TERMS_ADD4].map(([t,d])=>[t,d,CAT[t]||'개념·제도']);const have=new Set(base.map(x=>x[0]));const t5=TERMS5.filter(x=>!have.has(x[0]));t5.forEach(x=>have.add(x[0]));return [...base,...t5,...TERMS6.filter(x=>!have.has(x[0]))];})(),EVENTS:ALL,GROUPS:GR,BOOKS:[...D0.BOOKS,A4.BOOK_KSY,...A3.BOOKS_ADD3]};

const g = build();
const P = (lon, lat) => g.proj([lon, lat]).map(v => Math.round(v * 10) / 10);

// 같은 자리에 놓이는 사건은 작은 원 위로 흩어 놓는다
const groups = {};
const events = D.EVENTS.map(e => {
  const [x, y] = P(e.pl[1], e.pl[2]);
  const k = Math.round(x / 6) + ':' + Math.round(y / 6);
  (groups[k] = groups[k] || []).push(e.id);
  return {...e, mx:x, my:y};
});
Object.values(groups).forEach(ids => {
  if (ids.length < 2) return;
  ids.forEach((id, i) => {
    const e = events.find(v => v.id === id), a = (i / ids.length) * Math.PI * 2 - Math.PI / 2;
    e.mx = Math.round((e.mx + Math.cos(a) * 11) * 10) / 10;
    e.my = Math.round((e.my + Math.sin(a) * 11) * 10) / 10;
  });
});
events.forEach((e, i) => { e.no = i + 1; e.w = T1.includes(e.id) ? 1 : T3.includes(e.id) ? 3 : 2; });

const regions = D.REGIONS.map(r => ({...r, xy: P(r.lon, r.lat)}));
const seas = [['지중해', 18, 34.2], ['흑해', 34.5, 43.4], ['카스피해', 50.6, 42.2], ['페르시아만', 51.5, 27.0],
  ['홍해', 38.3, 20.5], ['아라비아해', 63, 16], ['벵골만', 89, 16]]
  .map(([n, lon, lat]) => ({n, xy: P(lon, lat)}));

// 중국 역사 지도(사용자 자료)의 장성·실크로드 선: 그 지도의 등장방형 좌표를 경위도로 되돌려 이 지도에 다시 투영
const inv=(x,y)=>[x/800*62+73.5, 53.8-y/560*36.3];
const reproj=d=>'M'+d.replace(/^M\s*/,'').split(/\s*L\s*/).map(p=>{const [x,y]=p.trim().split(',').map(Number);return P(...inv(x,y)).join(',');}).join('L');
const WALL=reproj("M 596.8,212.9 L 561.3,205.2 L 522.6,197.5 L 483.9,200.6 L 432.3,212.9 L 380.6,228.3 L 341.9,220.6 L 320.0,216.0");
const SILK=reproj("M 456.8,300.8 L 391.0,274.6 L 320.0,216.0 L 273.5,212.9 L 200.0,168.2 L 135.5,174.3 L 32.3,220.6");
const GATES=[['산해관',119.75,40.01],['가욕관',98.29,39.8],['장안',108.94,34.27]].map(([n,lo,la])=>({n,xy:P(lo,la)}));
const GUIDE={...GUIDE_P1,...GUIDE_P2,...GUIDE_P3,...GUIDE_P4,...GUIDE_P5};for(const [k,v] of Object.entries(GUIDE)){if(BODY[k])BODY[k]={안내:v,...BODY[k]};}
import {WHY} from './data_links.mjs';
const DATA = {why:WHY,concl:CONCL,body:BODY,wall:WALL,silk:SILK,gates:GATES,W: 1000, H: g.H, land: g.land, grat: g.grat, borders: g.borders, regions, seas,
  axes: D.AXES, parts: D.PARTS.map(p=>({...p,f:FORCES[p.id],bgx:PBG[p.id],sum:PSUM[p.id]})), events, groups: D.GROUPS, books: D.BOOKS, terms: D.TERMS, lineage: LINEAGE.map(l=>({...l,b:LBX.LB[l.id]||null})), lcats: LCATS, status: D.STATUS, rh: RH, threads: [...A2.THREADS, A3.THREAD_STEPPE].map(t=>({...t,ev:[...t.ev,...({steppe:['x05','x02','x04'],mono:['x03','x06'],khan:['x05','x02','x04'],nation:['x06']}[t.id]||[])].sort((a,b)=>ALL.findIndex(e=>e.id===a)-ALL.findIndex(e=>e.id===b))}))};

let html = fs.readFileSync('template.html', 'utf8');
html = html.replace('/*__DATA__*/', () => 'const DATA=' + JSON.stringify(DATA) + ';');
fs.mkdirSync('dist', {recursive: true});
fs.writeFileSync('dist/eurasia.html', html);
fs.rmSync('dist/eurasia.html.bak',{force:true});
console.log('ok', (html.length / 1024).toFixed(0) + 'KB', 'H=' + g.H);
