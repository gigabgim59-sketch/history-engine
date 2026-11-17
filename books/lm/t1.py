import sys
from playwright.sync_api import sync_playwright
O=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch()
  for w in (390,1280):
    pg=b.new_page(viewport={'width':w,'height':900});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/enl/dist/index.html');pg.wait_for_timeout(500)
    for h in ['#/', '#/p/p1', '#/e/l01', '#/e/l06', '#/e/l09', '#/e/l12', '#/p/p2', '#/e/l14', '#/e/l20', '#/e/l22', '#/p/p3', '#/e/l26', '#/e/l29', '#/e/l33', '#/e/l34', '#/e/l35', '#/p/p4', '#/e/l36', '#/e/l40', '#/e/l42', '#/e/l46', '#/p/p5', '#/e/l48', '#/e/l51', '#/e/l54', '#/e/l59', '#/e/l60', '#/e/l64', '#/p/p6', '#/e/l66', '#/e/l68', '#/e/l70', '#/map', '#/map/l40', '#/lanes', '#/lanes/l59', '#/net/l59', '#/pp', '#/pp/voltaire', '#/pp/marx', '#/id', '#/id/rev', '#/axis/pol', '#/t/lib', '#/rr/fra', '#/ln', '#/books', '#/terms', '#/end', '#/ul']:
      pg.evaluate("h=>{location.hash=h}",h);pg.wait_for_timeout(350)
      sw=pg.evaluate("document.documentElement.scrollWidth")
      if sw>w: errs.append(f'{h} overflow {sw}')
      pg.screenshot(path=f"{O}/{w}{h.replace('#','').replace('/','_')}.png")
    print(w,errs)
  b.close()
