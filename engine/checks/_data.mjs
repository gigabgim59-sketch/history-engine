// 출간본(dist/index.html 또는 서가에서 꺼낸 책 HTML)에서 DATA를 꺼낸다. 검사 도구들이 함께 쓴다.
import fs from 'fs';
export function loadData(path){
  const h=fs.readFileSync(path,'utf8');const i=h.indexOf('const DATA=');if(i<0)throw new Error('DATA 없음: '+path);
  let d=0,j=i+11,q=null,esc=false;
  for(;j<h.length;j++){const c=h[j];if(q){if(esc){esc=false;continue;}if(c==='\\'){esc=true;continue;}if(c===q)q=null;continue;}
    if(c==='"'||c==="'"||c==='`'){q=c;continue;}if(c==='{')d++;else if(c==='}'){d--;if(!d){j++;break;}}}
  const txt=h.slice(i+11,j);let D;try{D=JSON.parse(txt);}catch(e){D=(0,eval)('('+txt+')');}
  return {D,html:h};
}
export const flat=v=>typeof v==='string'?v:Array.isArray(v)?v.map(flat).join(''):v&&typeof v==='object'?Object.values(v).map(flat).join(''):'';
export const NARR=['안내','배경','원인','주체','전개','영향','갈림','오해'];
