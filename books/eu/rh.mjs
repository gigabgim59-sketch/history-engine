// 지역 통사 합치기: 본문 + 보강 문단을 원래 문단 번호 뒤에 끼워 넣는다(뒤에서부터)
import {NE} from './rh_ne.mjs';
import {IR} from './rh_ir.mjs';
import {IR_X} from './rh_ir_x.mjs';
import {IN} from './rh_in.mjs';
import {IN_X, IR_X2} from './rh_x2.mjs';
import {ST_A} from './rh_st.mjs';
import {ST_B} from './rh_st2.mjs';
import {RU} from './rh_ru.mjs';
import {RU_X,NE_X,IR_X3,IN_X2,ST_X} from './rh_x3.mjs';
import {RU_X2,NE_X2,IR_X4,IN_X3,ST_X2} from './rh_x4.mjs';
import {NE_X3,IR_X5,IN_X4,ST_X3,RU_X3} from './rh_x5.mjs';
import {IN_X5,ST_X4,RU_X4,FIN,FIN2,FIN3,FIN4} from './rh_x6.mjs';
import {FIN5} from './rh_x7.mjs';
function merge(base, ...lists){
  const out = Object.fromEntries(Object.entries(base).map(([k,v])=>[k,[...v]]));
  const all = lists.flat().map((x,i)=>({p:x[0],at:x[1],items:x[2],i}));
  all.sort((a,b)=>a.p.localeCompare(b.p)||b.at-a.at||b.i-a.i);
  all.forEach(x=>out[x.p].splice(x.at+1,0,...x.items));
  return out;
}
const F=r=>[...FIN,...FIN2,...FIN3,...FIN4,...FIN5].filter(x=>x[0]===r).map(x=>x[1]);
export const RH = {
  ne: merge(NE, NE_X, NE_X2, NE_X3, F('ne')),
  ir: merge(IR, IR_X, IR_X2, IR_X3, IR_X4, IR_X5, F('ir')),
  in: merge(IN, IN_X, IN_X2, IN_X3, IN_X4, IN_X5, F('in')),
  st: merge({...ST_A, ...ST_B}, ST_X, ST_X2, ST_X3, ST_X4, F('st')),
  ru: merge(RU, RU_X, RU_X2, RU_X3, RU_X4, F('ru')),
};
