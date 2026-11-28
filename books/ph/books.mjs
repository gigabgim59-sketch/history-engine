// 서가: 원서만(SPEC, LIBRARY §3.9). lang: 'src' 원전, 'en'·'de'·'fr' 연구서의 언어.
// 2026-11-28 보정 장 셋의 서지. 웹(출판사·도서관 목록·SEP 서지)으로 실재를 확인한 것과 기억에 기댄 것을 UNVERIFIED '서지'에 나누어 적었다. warn이 '—'가 아니면 판·출판사 대조가 남았다.
export const BOOKS = [
 {id:'scotus_ord',lang:'src',t:'Ordinatio, liber primus, distinctio secunda',a:'Ioannes Duns Scotus',o:'Opera omnia, vol. 2 (Civitas Vaticana: Typis Polyglottis Vaticanis, 1950)',role:'무한한 존재의 증명(제1부 제1–2문).',warn:'바티칸 판 권수 대조 전'},
 {id:'ockham_quodl',lang:'src',t:'Quodlibeta septem',a:'Guillelmus de Ockham',o:'Opera theologica IX, ed. J. C. Wey (St. Bonaventure, NY: Franciscan Institute, 1980)',role:'첫 임의 토론 제1문: 신이 하나뿐이라는 것은 자연 이성으로 증명되는가.',warn:'편자·연도 대조 전'},
 {id:'derijk1994',lang:'src',t:'Nicholas of Autrecourt: His Correspondence with Master Giles and Bernard of Arezzo',a:'L. M. de Rijk (ed.)',o:'Leiden: Brill, 1994 (Studien und Texte zur Geistesgeschichte des Mittelalters 42)',role:'편지의 비판 교감본과 영역, 아비뇽 재판 기록과 단죄 명제.',warn:'—'},
 {id:'weinberg1948',lang:'en',t:'Nicolaus of Autrecourt: A Study in 14th Century Thought',a:'Julius R. Weinberg',o:'Princeton: Princeton University Press, 1948',role:'니콜라우스의 인과 비판을 흄의 선구로 읽은 표준 연구.',warn:'—'},
 {id:'adams1987',lang:'en',t:'William Ockham',a:'Marilyn McCord Adams',o:'Notre Dame, IN: University of Notre Dame Press, 1987 (2 vols.)',role:'오컴의 형이상학·인식론·신학의 종합 연구.',warn:'—'},
 {id:'gilson1938',lang:'en',t:'Reason and Revelation in the Middle Ages',a:'Étienne Gilson',o:'New York: Charles Scribner’s Sons, 1938',role:'버지니아 대학 리처즈 강연. 오컴 이후 중세적 종합이 풀렸다는 해석.',warn:'—'},
 {id:'kant_aa',lang:'src',t:'Kant’s gesammelte Schriften',a:'Immanuel Kant',o:'hg. von der Königlich Preußischen Akademie der Wissenschaften (Berlin: Reimer, später de Gruyter, 1900–)',role:'『유일하게 가능한 증명 근거』(AA 2), 『순수이성비판』(AA 3–4), 「방향」(AA 8), 『실천이성비판』(AA 5), 『종교』(AA 6).',warn:'—'},
 {id:'wood1970',lang:'en',t:'Kant’s Moral Religion',a:'Allen W. Wood',o:'Ithaca: Cornell University Press, 1970',role:'요청이 비판 철학과 모순 없이 서는 진지한 믿음이라는 해석.',warn:'—'},
 {id:'vaihinger1911',lang:'de',t:'Die Philosophie des Als Ob',a:'Hans Vaihinger',o:'Berlin: Reuther & Reichard, 1911',role:'칸트의 요청을 실천의 허구로 읽은 해석.',warn:'판·출판사 대조 전'},
 {id:'jacobi1785',lang:'src',t:'Ueber die Lehre des Spinoza in Briefen an den Herrn Moses Mendelssohn',a:'Friedrich Heinrich Jacobi',o:'Breslau, 1785; erweiterte Ausgabe 1789',role:'레싱과의 대화와 멘델스존과의 편지, 증명하는 이성은 숙명론에 이른다는 논지.',warn:'출판사 대조 전'},
 {id:'mendelssohn1785',lang:'src',t:'Morgenstunden oder Vorlesungen über das Daseyn Gottes',a:'Moses Mendelssohn',o:'Berlin, 1785',role:'신의 존재에 관한 강의와 레싱의 ‘정화된 범신론’.',warn:'출판사 대조 전'},
 {id:'mendelssohn1786',lang:'src',t:'Moses Mendelssohn an die Freunde Lessings. Ein Anhang zu Herrn Jacobi Briefwechsel über die Lehre des Spinoza',a:'Moses Mendelssohn',o:'Berlin: Voß, 1786',role:'죽은 직후 나온 야코비에 대한 항의.',warn:'—'},
 {id:'herder1787',lang:'src',t:'Gott. Einige Gespräche',a:'Johann Gottfried Herder',o:'Gotha: Ettinger, 1787; 2. Aufl. 1800',role:'스피노자의 신을 근원적 힘으로 다시 읽은 대화편.',warn:'—'},
 {id:'beiser1987',lang:'en',t:'The Fate of Reason: German Philosophy from Kant to Fichte',a:'Frederick C. Beiser',o:'Cambridge, MA: Harvard University Press, 1987',role:'범신론 논쟁을 이성의 권위의 위기로 읽은 연구.',warn:'—'},
 {id:'allison1966',lang:'en',t:'Lessing and the Enlightenment: His Philosophy of Religion and Its Relation to Eighteenth-Century Thought',a:'Henry E. Allison',o:'Ann Arbor: University of Michigan Press, 1966',role:'레싱의 종교 철학과 스피노자주의 문제.',warn:'—'},
 {id:'altmann1973',lang:'en',t:'Moses Mendelssohn: A Biographical Study',a:'Alexander Altmann',o:'University, AL: University of Alabama Press; Philadelphia: Jewish Publication Society; London: Routledge & Kegan Paul, 1973',role:'멘델스존의 생애와 범신론 논쟁.',warn:'공동 출판사 표기 대조 전'}
];
export const BK = {
 ph14:[['scotus_ord','제1권 제2구분'],['ockham_quodl','첫 임의 토론 제1문'],['derijk1994','편지와 재판 기록'],['weinberg1948','전체'],['adams1987','신의 존재 장'],['gilson1938','갈림']],
 ph26:[['kant_aa','AA 2·3·5·6·8'],['wood1970','전체'],['vaihinger1911','갈림'],['jacobi1785','1787년 부록은 별도'],['beiser1987','칸트와 범신론 논쟁']],
 ph28:[['jacobi1785','전체'],['mendelssohn1785','전체'],['mendelssohn1786','전체'],['herder1787','전체'],['kant_aa','AA 8 「방향」'],['beiser1987','제2–4장'],['allison1966','갈림'],['altmann1973','갈림']]
};
