// 서가 책(tq)용 보강 묶음: 슬롯마다 문단을 이어 붙인다
import {XA} from './extra_a.mjs';
import {XB} from './extra_b.mjs';
import {XC, XD} from './extra_c.mjs';
const EX = {};
for (const X of [XA, XB, XC, XD]) for (const [q, slots] of Object.entries(X)) {
  EX[q] ||= {};
  for (const [k, v] of Object.entries(slots)) EX[q][k] = [...(EX[q][k] || []), ...v];
}
export const EXTRA = EX;
