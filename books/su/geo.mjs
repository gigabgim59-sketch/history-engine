// 지도 바탕: 러시아 제국·소련, 정각 원뿔 투영(표준 위선 50°·68°, 중앙 경선 75°E)
import fs from 'fs';
import * as d3 from 'd3-geo';
import * as topo from 'topojson-client';
import * as simp from 'topojson-simplify';
export const W=1000;
export const BOX={lon0:10,lon1:156,lat0:34,lat1:74};
export function build(){
  const proj=d3.geoConicConformal().rotate([-75,0]).parallels([50,68]);
  // 경계 상자를 촘촘히 따라 찍어 휘어진 테두리 전체가 들어오게 맞춘다
  const ring=[];for(let x=BOX.lon0;x<=BOX.lon1;x+=2)ring.push([x,BOX.lat0]);for(let y=BOX.lat0;y<=BOX.lat1;y+=2)ring.push([BOX.lon1,y]);
  for(let x=BOX.lon1;x>=BOX.lon0;x-=2)ring.push([x,BOX.lat1]);for(let y=BOX.lat1;y>=BOX.lat0;y-=2)ring.push([BOX.lon0,y]);
  const box={type:'MultiPoint',coordinates:ring};
  // 위쪽(북극해)은 덜 보여 주도록 실제 사용 영역: 남쪽 가장자리와 북위 72° 선 안쪽
  proj.fitWidth(W,box);
  const [[,y0],[,y1]]=d3.geoPath(proj).bounds({type:'MultiPoint',coordinates:ring.filter(([,y])=>y<=72)});
  const H=Math.round(y1-y0)+10;
  proj.translate([proj.translate()[0],proj.translate()[1]-y0+5]).clipExtent([[-60,-60],[W+60,H+60]]);
  const path=d3.geoPath(proj).digits(1);
  let t=JSON.parse(fs.readFileSync('node_modules/world-atlas/land-50m.json'));
  t=simp.presimplify(t);t=simp.simplify(t,0.0008);
  const land=path(topo.feature(t,t.objects.land));
  let c=JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-50m.json'));
  c=simp.presimplify(c);c=simp.simplify(c,0.002);
  const borders=path(topo.mesh(c,c.objects.countries,(a,b)=>a!==b&&a.id!=null&&b.id!=null))||'';
  const inb=([x,y])=>x>BOX.lon0-2&&x<BOX.lon1+2&&y>BOX.lat0-2&&y<BOX.lat1+2;
  const lines=(feats,tol)=>{let out='';for(const f of feats){const g=f.geometry;const ls=g.type==='LineString'?[g.coordinates]:g.coordinates;for(const l of ls){let last=null;const pts=[];for(const c of l){const q=proj(c);if(!q)continue;if(last&&Math.hypot(q[0]-last[0],q[1]-last[1])<tol)continue;pts.push(q);last=q;}const e=proj(l.at(-1));if(e&&pts.length&&pts.at(-1)!==e)pts.push(e);if(pts.length<2)continue;out+='M'+pts.map(q=>q[0].toFixed(1)+','+q[1].toFixed(1)).join('L');}}return out;};
  // 강: 볼가·드네프르·돈·오비·예니세이·레나 등 큰 강만
  const rv=JSON.parse(fs.readFileSync('ref/ne/ne_10m_rivers_lake_centerlines.geojson'));
  const rf0=rv.features.filter(f=>f.properties.scalerank<=4&&f.properties.featurecla!=='Lake Centerline').filter(f=>{const g=f.geometry;const cs=g.type==='LineString'?g.coordinates:g.coordinates.flat();return cs.some(inb);});
  const rivers=lines(rf0,1.8);
  const lk=JSON.parse(fs.readFileSync('ref/ne/ne_50m_lakes.geojson'));
  const lakes=path({type:'FeatureCollection',features:lk.features.filter(f=>{const b=d3.geoBounds(f);return b[0][0]<BOX.lon1&&b[1][0]>BOX.lon0&&b[0][1]<BOX.lat1&&b[1][1]>BOX.lat0&&(f.properties.scalerank??9)<=3;})});
  const grat=path(d3.geoGraticule().step([10,10])());
  const P=(lon,lat)=>proj([lon,lat]).map(v=>Math.round(v*10)/10);
  return {W,H,land,borders,prov:'',rivers:rivers||'',lakes:lakes||'',grat,P};
}
