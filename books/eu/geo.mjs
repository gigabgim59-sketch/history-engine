import fs from 'fs';
import * as d3 from 'd3-geo';
import * as topo from 'topojson-client';
import * as simp from 'topojson-simplify';
export const W=1000;
export function build(){
  let t=JSON.parse(fs.readFileSync('node_modules/world-atlas/land-50m.json'));
  t=simp.presimplify(t); t=simp.simplify(t,0.0006);
  const land=topo.feature(t,t.objects.land);
  const box={type:'Feature',geometry:{type:'MultiPoint',coordinates:[[-8,30],[22,62],[140,60],[132,28],[72,5],[40,10],[-6,36],[100,6]]}};
  const proj=d3.geoConicConformal().parallels([28,55]).rotate([-68,0]);
  proj.fitWidth(W,box);
  const [[x0,y0],[x1,y1]]=d3.geoPath(proj).bounds(box);
  const H=Math.round(y1-y0+20);
  proj.translate([proj.translate()[0],proj.translate()[1]-y0+10]).clipExtent([[0,0],[W,H]]);
  const path=d3.geoPath(proj).digits(1);
  const grat=d3.geoGraticule().step([20,10])();
  // 현재 국경(희미하게): 내부 경계만, 승인 여부가 엇갈리는 분리 지역의 선은 빼고, 크림은 국제적으로 인정된 경계로 둔다
  let c=JSON.parse(fs.readFileSync('node_modules/world-atlas/countries-50m.json'));
  c=simp.presimplify(c); c=simp.simplify(c,0.002);
  const m=topo.mesh(c,c.objects.countries,(a,b)=>a!==b&&a.id!=null&&b.id!=null);
  const inBox=([x,y])=>x>32.3&&x<36.2&&y>45.6&&y<46.5;
  m.coordinates=m.coordinates.filter(l=>!l.every(inBox));
  return {H,land:path(land),grat:path(grat),borders:path(m),proj};
}
