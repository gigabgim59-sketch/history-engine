import sys
from playwright.sync_api import sync_playwright
O=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch()
  for w in (390,1280):
    pg=b.new_page(viewport={'width':w,'height':900});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/soviet/dist/index.html');pg.wait_for_timeout(500)
    for h in ['#/', '#/p/p1', '#/p/p7', '#/e/s01', '#/e/s02', '#/e/s08', '#/e/s12', '#/p/p2', '#/e/s16', '#/e/s19', '#/e/s24', '#/p/p3', '#/e/s25', '#/e/s32', '#/p/p4', '#/e/s39', '#/e/s44', '#/e/s48', '#/p/p5', '#/e/s51', '#/e/s56', '#/p/p6', '#/e/s61', '#/e/s68', '#/p/p7', '#/e/s81', '#/e/s84', '#/e/s85', '#/e/s91', '#/p/p8', '#/e/s95', '#/map', '#/map/s04', '#/lanes', '#/lanes/s10', '#/net/s07', '#/pp', '#/id', '#/id/wor', '#/axis/pow', '#/t/rev', '#/rr/sth', '#/ln', '#/ln/koryo', '#/books', '#/terms', '#/end', '#/ul']:
      pg.evaluate("h=>{location.hash=h}",h);pg.wait_for_timeout(350)
      sw=pg.evaluate("document.documentElement.scrollWidth")
      if sw>w: errs.append(f'{h} overflow {sw}')
      pg.screenshot(path=f"{O}/{w}{h.replace('#','').replace('/','_')}.png")
    print(w,errs)
  b.close()
