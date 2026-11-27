# 인물 파일 정오 2026-11-27 (본문 정오에 맞춘 인물 고리·설명). 책 폴더에서 실행
R=[
('people_p3.mjs',' jberger:{',' jberger:{st09:"조건부 오류율로 세 학파의 검정을 잇자고 했다(2003)",'),
('people_p3.mjs',' jeffreys:{',' jeffreys:{st09:"버거(2003)가 피셔·네이만과 함께 검정의 합의를 따진 세 사람의 하나",'),
('people_p3.mjs',' mayo:{',' mayo:{st21:"가능도비가 오류율을 보장하지 않는다고 비판했다(1996)",'),
('people_p4.mjs',' gelman:{',' gelman:{st13:"로베르 외(2009)의 토론에서 제프리스의 사전 규칙을 다시 읽었다",'),
('people_p5.mjs',' rubin:{',' rubin:{st14:"무작위 배정이 베이즈 분석에서도 쓸모 있다고 보았다(1978)",'),
('people_p3.mjs',"export const PDENY3 = {};","export const PDENY3 = {'프리드먼':[null,'^과 「위험']};"),
('people_p6.mjs',"2018년 동료 72명과","2018년 모두 72명의 저자와 함께"),
('people_p6.mjs',"st37:'동료 72명과 문턱을","st37:'모두 72명의 저자와 함께 문턱을"),
('people_p3.mjs','st40:"힉스 발표 뒤 5시그마가 무엇의 확률인지 물었다(2012)"','st40:"힉스 발표 뒤 그의 물음이 오헤이건의 질문으로 이어졌다(2012)"'),
]
for f,o,n in R:
    s=open(f,encoding='utf-8').read(); c=s.count(o)
    if c!=1: print('SKIP',c,f,o[:40]); continue
    open(f,'w',encoding='utf-8').write(s.replace(o,n)); print('ok',f,o[:30])
