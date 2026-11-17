import sys
from playwright.sync_api import sync_playwright
O=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch()
  for w in (390,1280):
    pg=b.new_page(viewport={'width':w,'height':900});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/japan/dist/index.html');pg.wait_for_timeout(500)
    for h in ['#/', '#/p/p1', '#/p/p2', '#/p/p5', '#/e/j01', '#/e/j05', '#/e/j09', '#/e/j11', '#/map', '#/map/j05', '#/lanes', '#/lanes/j05', '#/net/j05', '#/pp', '#/id', '#/id/pea', '#/axis/emp', '#/t/rk', '#/rr/tok', '#/ln', '#/books', '#/terms', '#/end', '#/ul']:
      pg.evaluate("h=>{location.hash=h}",h);pg.wait_for_timeout(350)
      sw=pg.evaluate("document.documentElement.scrollWidth")
      if sw>w: errs.append(f'{h} overflow {sw}')
      pg.screenshot(path=f"{O}/{w}{h.replace('#','').replace('/','_')}.png")
    print(w,errs)
  b.close()
