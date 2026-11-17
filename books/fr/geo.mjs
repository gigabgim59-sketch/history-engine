// 지도 바탕: 혁명기 프랑스, 등장방형 투영(표준 위선 46.5°). 도 경계는 오늘의 데파르트망(1790년 83개 도가 바탕)
import fs from 'fs';
import * as d3 from 'd3-geo';
import * as topo from 'topojson-client';
import * as simp from 'topojson-simplify';
export const W=1000;
export const BOX={lon0:-6,lon1:11,lat0:41,lat1:51.8};
const K=Math.cos(46.5*Math.PI/180);
export function build(){
  const raw=(l,p)=>[l*K,p];raw.invert=(x,y)=>[x/K,y];
  const proj=d3.geoProjection(raw).rotate([-2.5,0]);
  const box={type:'Feature',geometry:{type:'Polygon',coordinates:[[[BOX.lon0,BOX.lat0],[BOX.lon0,BOX.lat1],[BOX.lon1,BOX.lat1],[BOX.lon1,BOX.lat0],[BOX.lon0,BOX.lat0]]]}};
  proj.fitWidth(W,box);
  const [[,y0],[,y1]]=d3.geoPath(proj).bounds(box);
  const H=Math.round(y1-y0);
  proj.translate([proj.translate()[0],proj.translate()[1]-y0]).clipExtent([[-60,-60],[W+60,H+60]]);
  const path=d3.geoPath(proj).digits(1);
  let t=JSON.parse(fs.readFileSync('node_modules/world-atlas/land-50m.json'));
  t=simp.presimplify(t);t=simp.simplify(t,0.0004);
  const land=path(topo.feature(t,t.objects.land));
  let c=JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-50m.json'));
  c=simp.presimplify(c);c=simp.simplify(c,0.001);
  const borders=''; // 오늘의 국경은 그리지 않는다
  const inb=([x,y])=>x>BOX.lon0-2&&x<BOX.lon1+2&&y>BOX.lat0-2&&y<BOX.lat1+2;
  // 성 경계: Natural Earth 1급 행정 경계 가운데 중국
  const a1=JSON.parse(fs.readFileSync('ref/ne/adm1_lines.geojson'));
  const lines=(feats,tol)=>{let out='';for(const f of feats){const g=f.geometry;const ls=g.type==='LineString'?[g.coordinates]:g.coordinates;for(const l of ls){let last=null,seg='';const pts=[];for(const c of l){const q=proj(c);if(!q)continue;if(last&&Math.hypot(q[0]-last[0],q[1]-last[1])<tol)continue;pts.push(q);last=q;}const e=proj(l.at(-1));if(e&&pts.length&&pts.at(-1)!==e)pts.push(e);if(pts.length<2)continue;out+='M'+pts.map(q=>q[0].toFixed(1)+','+q[1].toFixed(1)).join('L');}}return out;};
  const prov=lines(a1.features.filter(f=>f.properties.ADM0_NAME==='France'),1.0);
  // 강: Natural Earth 10m 강 중심선, 규모가 큰 것만
  const rv=JSON.parse(fs.readFileSync('ref/ne/ne_10m_rivers_lake_centerlines.geojson'));
  const thin=co=>co.filter((p,i)=>i%3===0||i===co.length-1);
  const rf0=rv.features.filter(f=>f.properties.scalerank<=5&&f.properties.featurecla!=='Lake Centerline').filter(f=>{const g=f.geometry;const cs=g.type==='LineString'?g.coordinates:g.coordinates.flat();return cs.some(inb);});
  const rivers=lines(rf0.filter(f=>f.properties.scalerank<=5&&f.properties.featurecla!=='Lake Centerline'),1.4);
  const lk=JSON.parse(fs.readFileSync('ref/ne/ne_50m_lakes.geojson'));
  const lakes=path({type:'FeatureCollection',features:lk.features.filter(f=>{const b=d3.geoBounds(f);return b[0][0]<BOX.lon1&&b[1][0]>BOX.lon0&&b[0][1]<BOX.lat1&&b[1][1]>BOX.lat0;})});
  const grat=path(d3.geoGraticule().step([5,5])());
  const P=(lon,lat)=>proj([lon,lat]).map(v=>Math.round(v*10)/10);
  return {W,H,land,borders,prov:prov||'',rivers:rivers||'',lakes:lakes||'',grat,P};
}
