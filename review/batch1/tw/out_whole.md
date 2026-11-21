# 『섬의 주인』 책 전체 검수 (머리말·부 머리·맺음·장 요약·서가·인쇄본)

## 0. 전제 점검

- 지시는 PLAN.md를 "평가어·시선·입장 기준" 문서라고 했지만, PLAN.md에는 평가어 목록도 '그 시대의 말' 목록도 없다(빌드 절차, 분량 기준, 표기 규칙, 최근 사실만 있음). SPEC.md는 자료에 없다. 그래서 범위 4)의 "평가어 목록이 서술자 문장에 쓰였는가"와 6)의 '그 시대의 말' 점검은 기준이 없어 적용하지 못했다. 이 책은 PLAN상 관점·여러 목소리 책이 아니어서 '매 장 바깥 점검'도 해당하지 않는다고 보았다. [추론, 중간]
- consistency.txt는 "연도 엇갈림 없음"이라고 하지만, 이 기계 검사는 기간·인원·주체가 엇갈리는 경우는 잡지 못한다. 아래 1~3번이 그런 엇갈림이다. 그러므로 "엇갈림 없음"을 통과로 보지 않았다.
- 같은 폴더의 STYLE.md에는 임칙서·홍수전 같은 아편전쟁·태평천국 인물이 적혀 있다. 다른 책(중국사)의 표기 파일로 보인다. 자료 목록에 없는 파일이라 지적에서는 뺐다. 다만 빌드에서 이 파일을 쓴다면 표기 규칙이 섞일 수 있다. [추측, 낮음]

## 1. 지적 표

| 번호 | 위치 | 지적 | 근거 종류 | 확신도 | 강도 | 고칠 안 |
|---|---|---|---|---|---|---|
| 1 | 제2장 요약(index.md, part_01 요약 줄) | "아들 정경이 섬을 동녕이라 부르며 22년 동안 다스렸다"라고 했지만, 같은 장 본문은 "정씨의 대만은 3대 22년 만에 막을 내렸다"라고 하고 마지막에 항복한 사람을 정극상으로 적는다. 22년(1661–1683)은 정씨 3대 전체의 기간이다. 정경의 재위는 1662–1681년으로 약 19년이다. | 사실(본문 대조), 재위 연도는 기억 기반 | 높음 | 강 | "아들 정경과 손자 정극상이 섬을 동녕이라 부르며 다스렸고, 정씨의 통치는 22년 이어졌다"로 고친다 |
| 2 | 제7장 요약 | "총통 당경숭은 일본군이 상륙하자 열흘 만에 대륙으로 달아났다." 본문에 따르면 상륙은 5월 29일, 도주는 지룽이 함락된 이튿날 밤(6월 4일)이므로 약 6일 뒤다. 본문의 "열흘 남짓"은 대만민주국이 북부에서 사라지기까지의 기간을 가리킨다. 요약이 이 기간을 당경숭의 도주로 옮겨 썼다. | 사실(본문 대조) | 높음 | 약 | "일본군이 상륙한 지 일주일도 안 되어" 또는 "대만민주국 선포 열흘 남짓 만에"로 고친다 |
| 3 | 제9장 요약 | 시라이안 사건에서 "농민 수천 명이 체포되었다"라고 했지만, 본문은 "1천 명이 넘는 사람을 재판에 넘겨 860여 명에게 사형을 선고했다"라고만 적는다. 본문에는 체포 인원이 없고, 요약의 '수천'은 본문의 규모와 맞지 않는다. 기억으로는 체포된 사람이 1,900여 명이다. | 사실(본문 대조), 체포 인원은 기억 기반 | 중간 | 약 | 본문에 맞추어 "1천 명이 넘는 사람이 재판에 넘겨졌다"로 쓰거나, 출처를 달아 체포 인원을 본문과 요약에 함께 적는다 |
| 4 | 제11장 요약과 본문 19행 | "20만 명이 넘는 … 3만 명 가까이 돌아오지 못했다." 일본 후생노동성 집계는 207,183명이 복무했고 30,304명이 전사하거나 실종되었다는 것이다. '가까이'는 3만에 못 미친다는 뜻이 되므로 집계와 어긋난다. | 사실(웹) | 중간 | 약 | "3만 명 남짓"으로 바꾸고 집계 주체(일본 후생성)를 밝힌다 |
| 5 | 제13장 제목(index, part_02, PDF 차례·북마크) | "중앙정부의 천대"는 '遷臺'의 한자음을 그대로 적은 것으로 보인다. 그러나 한국어 독자는 '천대(賤待)'로 읽는다. 본문 어디에도 이 말의 풀이가 없다. | 사실(본문 대조: grep 결과 제목에만 나옴) | 높음 | 약 | "중앙정부의 대만 이전과 계엄, 백색 테러"로 바꾼다 |
| 6 | 머리말(화면판과 인쇄본 4쪽 모두) | "장마다 맨 앞의 ‘먼저 알아 둘 것’"이라고 약속했지만, 이 부분은 20장 가운데 10장(1·2·7·8·12·13·16·17·19·20장)에만 있다. | 사실(본문 대조) | 높음 | 약 | "주요 장의 맨 앞에는"으로 고치거나, 빠진 10장에 이 부분을 채운다 |
| 7 | 머리말 | "사건마다 배경과 원인과 주체와 전개를 같은 틀로 적고"라고 했지만, 5·9·14·18장에는 원인과 주체 절이 없고 15장에는 주체 절이 없다. | 사실(본문 대조) | 높음 | 약 | "대부분의 사건을"로 완화하거나 빠진 절을 채운다 |
| 8 | 머리말 "다섯 통치", 맺음 "다섯 번 바뀐 섬" | 1장 본문은 1626–1642년 북부를 스페인이 차지해 "남쪽의 네덜란드와 북쪽의 스페인이 나누어 차지한 섬"이었다고 적는다. 그런데 머리말과 맺음의 통치자 셈에는 스페인이 빠져 있다. 셈에서 뺄 수는 있지만, 뺀 기준을 밝히지 않아 본문과 어긋나 보인다. | 사실(본문 대조), 셈의 기준은 추론 | 중간 | 약 | "북부를 잠시 차지한 스페인을 빼면 다섯 통치"처럼 기준을 한 구절로 밝힌다 |
| 9 | 머리말의 지명 규칙과 1장 요약 '타이오안', 5장 요약 '다거우', 2부 머리 '멍자' | 머리말은 "지명은 오늘 쓰이는 이름을 중국어 발음으로" 적는다고 했다. 그러나 다거우(현 가오슝), 타이오안(현 안핑), 멍자(현 완화)처럼 당대 이름을 쓴 곳이 있다. 내용상 당대 이름이 맞는 자리이긴 하다. 문제는 규칙과 실제 쓰임이 어긋난다는 점이다. | 사실(본문 대조) | 높음 | 형식적 | 규칙에 "당대의 항구·지명은 옛 이름을 쓰고 처음에 오늘 이름을 밝힌다"는 예외를 덧붙이고, 처음 나오는 곳에 괄호로 오늘 이름을 적는다 |
| 10 | 1부 머리 '이 부에서 바뀐 것', 맺음 '첫째 겹' | "1684년부터 대만은 공식적으로 중국 왕조의 영토가 되었다", "대만이 처음 중국 왕조의 영토가 된 것은 1684년이었고"라고 썼다. 같은 글이 "정씨는 명의 제도를" 섬에 세웠다고 적고 있고, 정씨 정권의 성격(명 유신 정권인가, 독립 해상 왕국인가)이나 그 이전의 귀속은 해석과 정치적 주장이 갈리는 지점이다. 해석이 사실처럼 쓰였다. | 통설·추론 | 중간 | 약 | "1684년 청 제국의 부(府)로 편입되며 대만은 처음 대륙 왕조의 정식 행정 구역이 되었다"처럼 행정 편입이라는 사실로 좁혀 쓴다 |
| 11 | 맺음 '다섯째 겹'(화면판, 인쇄본 92쪽) | "황민화와 2·28의 상처를 지나(11장), (12장), 민주화 이후에야"에서 장 표시가 따로 떨어져 나열되어 문장이 깨졌다. | 사실(본문 대조) | 높음 | 형식적 | "황민화(11장)와 2·28(12장)의 상처를 지나"로 고친다 |
| 12 | 4부 머리 첫 문장 | "직선 대통령과 정권 교체"라고 썼다. 책의 다른 곳은 모두 '총통'을 쓴다. | 사실(본문 대조) | 높음 | 형식적 | "총통 직선과 정권 교체"로 고친다 |
| 13 | 서가 [wu], [dohae] | (1) [wu]의 "대만 고등학교 역사 교사의 강의"는 교보문고 서지에 부제로 나오지 않는다. 교보 기록은 '드디어 시리즈 2', 현대지성, 2024이다. 소개 문구를 부제처럼 쓴 것으로 보인다. (2) 다른 21권은 연도를 적었는데 이 두 권만 연도가 없다. 확인한 연도는 [wu] 2024(한국어판), [dohae] 2021(한국어판, 원서 2016)이다. | 사실(웹) | 중간 | 형식적 | 부제 자리를 비우고, 연도와 출판사(번역서이면 원서 연도도)를 다른 항목과 같은 형식으로 적는다 |
| 14 | 3부 머리 '본성인과 외성인', 'mig' | "외성인은 인구의 15% 안팎", "100만 명이 넘는 외성인이 600만의 본성인 사회에" 같은 인구 수치에 출처나 시점이 없다. 범위 d)의 출처 없는 수치다. 수치 자체는 통설의 범위 안에 있다(기억 기반). | 통설, 기억 기반 | 중간 | 형식적 | "1956년 인구 조사 기준" 같은 시점을 적거나, 출처를 장 본문 주석으로 돌린다 |
| 15 | 제6장 본문 269행 | "1874년의 출병은 일본 최초의 해외 출병"은 범위 c)의 최상급이다. 임진왜란 같은 전근대 출병이 있으므로 '메이지 정부(근대 일본) 최초'로 좁혀야 맞다. 장 본문 문장이라 본문 검수자와 겹칠 수 있다. | 통설, 기억 기반 | 중간 | 약 | "메이지 일본의 첫 해외 출병"으로 고친다 |
| 16 | 인쇄본 17쪽, 52쪽 | 거의 빈 쪽이다. 17쪽은 2장 끝 4줄, 52쪽은 3부 머리 끝 4줄뿐이다. 42·74·81·86쪽도 장 끝이 짧게 넘어간 쪽이다. 고아 제목은 찾지 못했다(쪽 끝 줄 검사). | 사실(PDF 텍스트 추출) | 높음 | 형식적 | 문단 간격이나 장 끝 단락을 조정해 앞쪽으로 당긴다 |

## 2. 서지 확인 기록(지적 아님)

서가 23권 가운데 22권은 저자·제목·연도를 확인했다. [dohae]는 제목과 연도만 확인했다.

- [wu] 우이룽(吳宜蓉), 『드디어 만나는 대만사 수업』, 박소정 옮김, 현대지성, 2024. https://ebook-product.kyobobook.co.kr/dig/epd/ebook/E000009407986
- [dohae] 『도해 타이완사』 한국어판(2021, 원서 2016, 부제 문구 "선사시대부터 차이잉원 시대까지")는 확인했다. 저자 네 명의 이름은 확인하지 못했다. https://librairie.coreenne.fr/en/products/156364
- [rubin] Rubinstein ed., Taiwan: A New History (M.E. Sharpe, 1999; 증보판 2007, ISBN 9780765614957). https://libcat.library.tamu.edu/Record/in00002200829 , https://wholesale.awesomebooks.com/book/9780765614957/taiwan-a-new-history-east-gate-books
- [roy] Denny Roy, Taiwan: A Political History (Cornell UP, 2003). https://search.worldcat.org/title/50285149
- [manthorpe] Jonathan Manthorpe, Forbidden Nation: A History of Taiwan (Palgrave Macmillan, 2005; 2008 페이퍼백). https://search.worldcat.org/oclc/58720732 , https://us.macmillan.com/books/9780230614246
- [andrade] Tonio Andrade, How Taiwan Became Chinese (Columbia UP, 2008). https://search.worldcat.org/oclc/184821622
- [lost] Tonio Andrade, Lost Colony (Princeton UP, 2011). https://www.publishersweekly.com/978-0-691-14455-9
- [shepherd] John R. Shepherd, Statecraft and Political Economy on the Taiwan Frontier, 1600–1800 (Stanford UP, 1993). https://www.sup.org/books/asian-studies/statecraft-and-political-economy-taiwan-frontier-1600-1800
- [teng] Emma Jinhua Teng, Taiwan's Imagined Geography … 1683–1895 (Harvard University Asia Center, 2004). https://china.usc.edu/teng-taiwans-imagined-geography-chinese-colonial-travel-writing-and-pictures-1683-1895-2004
- [ching] Leo T. S. Ching, Becoming "Japanese" (UC Press, 2001). https://www.ucpress.edu/books/becoming-japanese/paper , https://ci.nii.ac.jp/ncid/BA52385069?l=en
- [tsurumi] E. Patricia Tsurumi, Japanese Colonial Education in Taiwan, 1895–1945 (Harvard UP, 1977). 서평 URL: https://cambridge.org/core/journals/journal-of-asian-studies/article/abs/japanese-colonial-education-in-taiwan-18951945-by-e-patricia-tsurumi-cambridge-harvard-university-press-harvard-east-asian-series-88-1977-xiii-334-pp-appendixes-bibliography-glossary-index-2000/0F57EBF3A48532EE88FD74A608E6DCBE
- [phillips] Steven E. Phillips, Between Assimilation and Independence … 1945–1950 (Stanford UP, 2003). https://www.cambridge.org/core/journals/china-quarterly/article/between-assimilation-and-independence-the-taiwanese-encounter-nationalist-china-19451950-by-steven-e-phillips-stanford-stanford-university-press-2003-272-pp-5500-isbn-0804744572/75332E81E73DBC8DCFDCF33CA3091A7B
- [tragic] Lai Tse-han, Ramon H. Myers, Wei Wou, A Tragic Beginning (Stanford UP, 1991). https://core-prod.cambridgecore.org/core/journals/china-quarterly/article/tragic-beginning-the-taiwan-uprising-of-february-28-1947-by-lai-tsehan-ramon-h-myers-and-wei-wou-stanford-stanford-university-press-1991-273-pp-3250-isbn-0-8047-18296/5DC2371417A8A91EED34E1640ADB778A
- [kerr] George H. Kerr, Formosa Betrayed (Houghton Mifflin, 1965). Kerr가 타이베이 주재 미국 부영사였다는 것도 확인했다. https://www.cambridge.org/core/journals/china-quarterly/article/formosa-betrayed-by-kerrgeorge-h-boston-houghton-mifflin-co-1965-514-pp-695/A0F3E392F083EAD52EE59A64236BB4D9 , https://en.wikipedia.org/wiki/George_H._Kerr
- [lin] Hsiao-ting Lin, Accidental State (Harvard UP, 2016). https://www.hoover.org/news/hoover-fellow-and-library-archives-curator-hsiao-ting-lin-publishes-new-view-modern-taiwan , https://taipeitimes.com/News/feat/archives/2016/12/24/2003661814
- [taylor] Jay Taylor, The Generalissimo's Son (2000). 서평으로 책이 있다는 것만 확인했다. https://newrepublic.com/article/85792/chiang-kai-shek-pakula-taylor (출판 연도 2000과 출판사 Harvard UP는 기억 기반)
- [gold] Thomas B. Gold, State and Society in the Taiwan Miracle (M.E. Sharpe, 1986). https://cambridge.org/core/journals/journal-of-asian-studies/article/state-and-society-in-the-taiwan-miracle-by-thomas-b-gold-armonk-n-y-m-e-sharpe-1986-xiv-162-pp-notes-bibliography-index-29-cloth-1395-paper/47B83438F60E53469A70CB938F68C5D8
- [rigger] Shelley Rigger, Why Taiwan Matters (2011; Updated Edition 2014). https://search.worldcat.org/oclc/868971064 , https://www.bookwire.com/book/Why-Taiwan-Matters-9781442204805-Rigger-Shelley-43983940
- [jacobs] J. Bruce Jacobs, Democratizing Taiwan (Brill, 2012). https://libcat.library.tamu.edu/Record/in00002740261/TOC (연도는 검색 결과 요약 수준으로 확인)
- [bush] Richard C. Bush, Difficult Choices (Brookings, 2021). https://www.brookings.edu/book/difficult-choices
- [ho] Ming-sho Ho, Challenging Beijing's Mandate of Heaven (Temple UP, 2019). https://cambridge.org/core/journals/china-quarterly/article/abs/challenging-beijings-mandate-of-heaven-taiwans-sunflower-movement-and-hong-kongs-umbrella-movement-mingsho-ho-philadelphia-rome-and-tokyo-temple-university-press-2019-xvi-269-pp-3995-isbn-9781439917077/24AE82BA2DFCE23D9F8CE3FBA970F3EC
- [slin] Syaru Shirley Lin, Taiwan's China Dilemma (Stanford UP, 2016). https://aparc.fsi.stanford.edu/node/12625
- [waka] 若林正丈, 『台湾の政治: 中華民国台湾化の戦後史』(東京大学出版会, 2008; 増補新装版 2021). https://www.tkfd.or.jp/research/political-review/a01068?id=444 , https://ndlsearch.ndl.go.jp/en/books/R100000002-I031391540

책 안 사실 대조에 쓴 웹 자료:
- 대만 정체성 조사(4부 머리 '정체성의 변화'): 1992년 '대만인' 17.6%, '둘 다' 46.4%, '중국인' 25.5%. 최근 조사는 '대만인' 61.7%, '중국인' 2.4%. 본문의 "20%에 못 미쳤다", "60%를 넘었고", "몇 퍼센트로 줄었다"와 맞는다. https://www.taipeitimes.com/News/front/archives/2024/02/24/2003813999
- 대만인 일본군 복무 207,183명, 전사·실종 30,304명(지적 4). https://en.wikipedia.org/wiki/Taiwanese_Imperial_Japan_Serviceman

## 3. 확인 못함

- [dohae] 저자 궈팅위·왕핀한·쉬야링·좡젠화의 이름과 한국어판 출판사. 제목과 2021년 한국어판이 있다는 것은 확인했다.
- [wu]의 "대만 고등학교 역사 교사의 강의"가 표지 문구로라도 쓰였는지.
- 시라이안 사건의 체포 인원(기억으로는 1,900여 명, 지적 3).
- 3부 머리의 외성인 비율 15%와 이주 인원 100만 명 이상, 1부 끝의 "19세기에 200만 명", 2부 머리의 "300만에서 600만 가까이". 모두 기억과 어긋나지 않아 지적으로 세지 않았다(14번은 출처 표기만 지적했다).
- 4부 머리의 "TSMC는 세계 최첨단 칩의 대부분"(통설과 어긋나지 않음), 맺음의 "가장 부유하고 가장 자유로운 시기"(평가 표현, 형식적).

## 4. 검토하지 않음

- 범위 4)의 평가어 점검과 6)의 '그 시대의 말' 점검: PLAN.md에 기준 목록이 없어 하지 못했다(0절).
- 범위 6)의 [[id]] 교차 참조: 자료(front.md, index.md, part_*.md)에 [[...]] 표기가 없다. 그래서 맺음의 "(n장)" 표시 9곳이 맞는 장을 가리키는지만 대조했고, 문제를 찾지 못했다. HTML판의 링크 대상은 자료에 없어 보지 못했다.
- 화면판(HTML)과 인쇄본의 전체 대조: 인쇄본 2쪽은 용어·서가·지도·연표·연결망이 HTML판에만 있다고 밝히고, 인쇄본 머리말에서는 '점선 밑줄' 문장이 빠져 있다. 인쇄본이 화면판에 없는 것을 말하는 곳은 찾지 못했다. HTML 파일 자체는 자료에 없어 보지 못했다.
- 인쇄본 형식: 북마크(머리말·4부·20장·맺음, 계층 정상), 글꼴(Noto Serif CJK KR 두 종, CID TrueType, 모두 서브셋 내장), 표지(1쪽, 텍스트 보임, 숨은 표지 없음), 쪽 끝 고아 제목(쪽 끝 줄을 텍스트로 검사해 발견 없음)을 보았다. 쪽 이미지를 렌더링해 눈으로 보는 검사는 하지 않았다. 텍스트 추출로 잡히지 않는 시각적 문제(그림 잘림, 여백)는 검토하지 않음으로 둔다.
- 장 요약 20개와 본문의 대조: 연도·기간·인원 같은 핵심 수치만 대조했다(1~4번). 요약 문장 전체의 뉘앙스 대조는 하지 않았다.
- 장 본문의 문장 단위 사실 확인: 맡은 범위가 아니다. 15번은 범위 c) 순서를 따르다 눈에 띈 것이다.
- PLAN.md '최근 사실'(2025–2026) 항목과 20장 요약: 20장 요약에는 수치가 거의 없어 대조할 것이 없었다. 20장 본문의 최근 수치는 본문 검수 범위다.
