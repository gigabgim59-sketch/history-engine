import sys
from playwright.sync_api import sync_playwright
O=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch()
  for w in (390,1280):
    pg=b.new_page(viewport={'width':w,'height':900});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/napol/dist/index.html');pg.wait_for_timeout(500)
    for h in ['#/', '#/p/p1', '#/e/n01', '#/e/n23', '#/e/n41', '#/e/n55', '#/e/n60', '#/p/p6', '#/map', '#/map/n42', '#/lanes', '#/lanes/n23', '#/net/n47', '#/pp', '#/id', '#/axis/war', '#/t/war', '#/rr/eas', '#/ln', '#/books', '#/terms', '#/end', '#/ul']:
      pg.evaluate("h=>{location.hash=h}",h);pg.wait_for_timeout(350)
      sw=pg.evaluate("document.documentElement.scrollWidth")
      if sw>w: errs.append(f'{h} overflow {sw}')
      pg.screenshot(path=f"{O}/{w}{h.replace('#','').replace('/','_')}.png")
    print(w,errs)
  b.close()
