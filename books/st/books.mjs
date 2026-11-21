// 서가: 원서만(SPEC). 모두 이번 세션에서 웹으로 서지(저자·연도·학술지·쪽)의 실재를 확인했다. 내용은 2차 자료로 확인한 범위만 본문에 썼다(UNVERIFIED)
export const BOOKS = [
 {id:'lindley57',lang:'en',t:'A statistical paradox',a:'D. V. Lindley',o:'Biometrika 44 (1957): 187–192',role:'린들리 역설의 원 논문.',warn:'—'},
 {id:'bartlett57',lang:'en',t:"A comment on D. V. Lindley's statistical paradox",a:'M. S. Bartlett',o:'Biometrika 44 (1957): 533–534',role:'사후 확률이 대립가설 사전의 폭에 달린다는 논평.',warn:'—'},
 {id:'bs87',lang:'en',t:'Testing a point null hypothesis: the irreconcilability of P values and evidence',a:'James O. Berger · Thomas Sellke',o:'JASA 82 (1987): 112–122',role:'사전 집합별 사후 확률의 하한.',warn:'—'},
 {id:'cb87',lang:'en',t:'Reconciling Bayesian and frequentist evidence in the one-sided testing problem',a:'George Casella · Roger L. Berger',o:'JASA 82 (1987): 106–111',role:'한쪽 검정에서의 화해.',warn:'—'},
 {id:'els63',lang:'en',t:'Bayesian statistical inference for psychological research',a:'Ward Edwards · Harold Lindman · Leonard J. Savage',o:'Psychological Review 70 (1963): 193–242',role:'멈추는 규칙의 무관함, p값과 증거의 하한.',warn:'—'},
 {id:'anscombe63',lang:'en',t:'Sequential medical trials',a:'F. J. Anscombe',o:'JASA 58 (1963): 365–383',role:'아미티지의 책에 대한 서평. 가능도 원리에 따른 해석.',warn:'—'},
 {id:'amr69',lang:'en',t:'Repeated significance tests on accumulating data',a:'P. Armitage · C. K. McPherson · B. C. Rowe',o:'JRSS A 132 (1969): 235–244',role:'반복 검정이 오류율을 부풀리는 정도.',warn:'—'},
 {id:'cornfield66',lang:'en',t:'Sequential trials, sequential analysis and the likelihood principle',a:'Jerome Cornfield',o:'The American Statistician 20 (1966): 18–23',role:'멈추는 규칙의 무관함을 따진 글.',warn:'—'},
 {id:'lp76',lang:'en',t:'Inference for a Bernoulli process (a Bayesian view)',a:'D. V. Lindley · L. D. Phillips',o:'The American Statistician 30 (1976): 112–119',role:'앞면 9·뒷면 3의 예.',warn:'—'},
 {id:'wl23',lang:'en',t:'History and nature of the Jeffreys–Lindley paradox',a:'Eric-Jan Wagenmakers · Alexander Ly',o:'Archive for History of Exact Sciences 77 (2023): 25–72',role:'역설의 역사와 해석.',warn:'—'},
 {id:'sbb01',lang:'en',t:'Calibration of p values for testing precise null hypotheses',a:'Thomas Sellke · M. J. Bayarri · James O. Berger',o:'The American Statistician 55 (2001): 62–71',role:'p값만으로 셈하는 베이즈 인자의 하한.',warn:'—'},
 {id:'kss96',lang:'en',t:'Reasoning to a foregone conclusion',a:'J. B. Kadane · M. J. Schervish · T. Seidenfeld',o:'JASA 91 (1996)',role:'정칙 사전에서 정해진 결론으로 가는 표집의 한계.',warn:'—'}
];
export const BK = {
 st18:[['els63','멈추는 규칙'],['anscombe63','서평 전체'],['amr69','반복 검정의 오류율'],['cornfield66','전체'],['lp76','이항·음이항의 예'],['kss96','전체']],
 st20:[['lindley57','전체'],['bartlett57','전체'],['bs87','하한의 표'],['cb87','한쪽 검정'],['els63','하한'],['wl23','역사와 해석'],['sbb01','보정식']]
};
