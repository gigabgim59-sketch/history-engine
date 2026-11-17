import sys
from playwright.sync_api import sync_playwright
O=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch()
  for w in (390,1280):
    pg=b.new_page(viewport={'width':w,'height':900});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/dipl/dist/index.html');pg.wait_for_timeout(500)
    for h in ['#/', '#/p/p1', '#/e/d01', '#/e/d02', '#/e/d08', '#/e/d09', '#/p/p2', '#/e/d16', '#/e/d17', '#/e/d22', '#/e/d30', '#/e/d31', '#/e/d36', '#/e/d38', '#/e/d44', '#/e/d45', '#/e/d50', '#/e/d51', '#/e/d54', '#/e/d58', '#/e/d60', '#/p/p6', '#/map', '#/map/d08', '#/lanes', '#/lanes/d09', '#/net/d09', '#/pp', '#/pp/kennan', '#/id', '#/id/dec', '#/axis/ord', '#/t/con', '#/rr/eas', '#/ln', '#/books', '#/terms', '#/end', '#/ul']:
      pg.evaluate("h=>{location.hash=h}",h);pg.wait_for_timeout(350)
      sw=pg.evaluate("document.documentElement.scrollWidth")
      if sw>w: errs.append(f'{h} overflow {sw}')
      pg.screenshot(path=f"{O}/{w}{h.replace('#','').replace('/','_')}.png")
    print(w,errs)
  b.close()
