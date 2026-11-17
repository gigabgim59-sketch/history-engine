// 지도 바탕: 세계, 자연 지구 투영(경도 10°를 가운데로). 오늘의 국경은 옅게(끄고 켤 수 있음)
import fs from 'fs';
import * as d3 from 'd3-geo';
import * as topo from 'topojson-client';
import * as simp from 'topojson-simplify';
export const W=1000;
export const BOX={lon0:-170,lon1:190,lat0:-44,lat1:72};
export function build(){
  // 동아시아: 원뿔 등적 투영, 경도 125°를 가운데로
  const proj=d3.geoConicEqualArea().parallels([30,45]).rotate([-123,0]);
  const area={type:'Feature',geometry:{type:'MultiPoint',coordinates:[[104,24],[104,50],[146,24],[146,50],[125,52],[125,23]]}};
  const H=620;
  proj.fitExtent([[10,10],[W-10,H-10]],area).clipExtent([[0,0],[W,H]]);
  const path=d3.geoPath(proj).digits(1);
  let t=JSON.parse(fs.readFileSync('node_modules/world-atlas/land-50m.json'));
  const land=path(topo.feature(t,t.objects.land));
  let c=JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-50m.json'));
  const borders=path(topo.mesh(c,c.objects.countries,(a,b)=>a!==b));
  const grat=path(d3.geoGraticule().step([15,15])());
  const P=(lon,lat)=>proj([lon,lat]).map(v=>Math.round(v*10)/10);
  return {W,H,land,borders,prov:'',rivers:'',lakes:'',grat,P};
}
