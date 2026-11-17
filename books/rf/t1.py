import sys
from playwright.sync_api import sync_playwright
O=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch()
  for w in (390,1280):
    pg=b.new_page(viewport={'width':w,'height':900});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/reform/dist/index.html');pg.wait_for_timeout(500)
    for h in ['#/', '#/p/p1', '#/e/f01', '#/e/f04', '#/e/f05', '#/e/f08', '#/e/f10', '#/e/f11', '#/e/f60', '#/p/p6', '#/map', '#/map/f01', '#/lanes', '#/lanes/f10', '#/net/f10', '#/pp', '#/pp/luther', '#/id', '#/id/min', '#/axis/fai', '#/t/aut', '#/rr/med', '#/ln', '#/books', '#/terms', '#/end', '#/ul']:
      pg.evaluate("h=>{location.hash=h}",h);pg.wait_for_timeout(350)
      sw=pg.evaluate("document.documentElement.scrollWidth")
      if sw>w: errs.append(f'{h} overflow {sw}')
      pg.screenshot(path=f"{O}/{w}{h.replace('#','').replace('/','_')}.png")
    print(w,errs)
  b.close()
