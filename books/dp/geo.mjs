// 지도 바탕: 세계, 자연 지구 투영(경도 10°를 가운데로). 오늘의 국경은 옅게(끄고 켤 수 있음)
import fs from 'fs';
import * as d3 from 'd3-geo';
import * as topo from 'topojson-client';
import * as simp from 'topojson-simplify';
export const W=1000;
export const BOX={lon0:-170,lon1:190,lat0:-44,lat1:72};
export function build(){
  const proj=d3.geoNaturalEarth1().rotate([-10,0]);
  proj.fitWidth(W,{type:'Sphere'});
  const band={type:'Feature',geometry:{type:'Polygon',coordinates:[[[-169.9,BOX.lat0],[-169.9,BOX.lat1],[0,BOX.lat1],[189.9,BOX.lat1],[189.9,BOX.lat0],[0,BOX.lat0],[-169.9,BOX.lat0]]]}};
  const pts=[[0,BOX.lat1],[0,BOX.lat0]].map(c=>proj(c));
  const y0=pts[0][1],y1=pts[1][1];
  const H=Math.round(y1-y0);
  proj.translate([proj.translate()[0],proj.translate()[1]-y0]).clipExtent([[0,0],[W,H]]);
  const path=d3.geoPath(proj).digits(1);
  let t=JSON.parse(fs.readFileSync('node_modules/world-atlas/land-110m.json'));
  const land=path(topo.feature(t,t.objects.land));
  let c=JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-110m.json'));
  const borders=path(topo.mesh(c,c.objects.countries,(a,b)=>a!==b));
  const grat=path(d3.geoGraticule().step([15,15])());
  const P=(lon,lat)=>proj([lon,lat]).map(v=>Math.round(v*10)/10);
  return {W,H,land,borders,prov:'',rivers:'',lakes:'',grat,P};
}
