import sys
from playwright.sync_api import sync_playwright
O=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch()
  for w in (390,1280):
    pg=b.new_page(viewport={'width':w,'height':900});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/china/dist/index.html');pg.wait_for_timeout(500)
    for h in ['#/','#/p/p1','#/p/p2','#/p/p3','#/p/p4','#/p/p5','#/p/p6','#/ln','#/ln/mao','#/ln/tw','#/end','#/e/c52','#/e/c54','#/e/c58','#/e/c60','#/pp/xi','#/pp/trump','#/id/hk','#/e/c43','#/e/c47','#/e/c49','#/pp/khrushchev','#/pp/wuhan','#/id/tib','#/e/c30','#/e/c35','#/e/c40','#/pp/chenyi','#/pp/chenyitw','#/id/tw','#/e/c19','#/e/c22','#/e/c29','#/pp/zaifeng','#/pp/stalin','#/id/wor','#/e/c09','#/e/c14','#/e/c16','#/e/c17','#/e/c18','#/pp/lihongzhang','#/map/c15','#/e/c01','#/e/c03','#/e/c30','#/map','#/map/c05','#/lanes','#/lanes/c03','#/net/c01','#/pp','#/pp/zengguofan','#/id','#/id/peas','#/axis/sov','#/t/sov','#/rr/hn','#/ln','#/books','#/terms','#/end','#/ul']:
      pg.evaluate("h=>{location.hash=h}",h);pg.wait_for_timeout(350)
      sw=pg.evaluate("document.documentElement.scrollWidth")
      if sw>w: errs.append(f'{h} overflow {sw}')
      pg.screenshot(path=f"{O}/{w}{h.replace('#','').replace('/','_')}.png")
    print(w,errs)
  b.close()
