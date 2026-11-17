import sys
from playwright.sync_api import sync_playwright
O=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch()
  for w in (390,1280):
    pg=b.new_page(viewport={'width':w,'height':900});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/brit/dist/index.html');pg.wait_for_timeout(500)
    for h in ['#/', '#/p/p1', '#/e/b01', '#/e/b02', '#/e/b08', '#/e/b10', '#/p/p2', '#/e/b14', '#/e/b16', '#/e/b21', '#/e/b23', '#/e/b30', '#/e/b31', '#/e/b35', '#/e/b38', '#/e/b40', '#/e/b45', '#/e/b47', '#/e/b50', '#/e/b51', '#/e/b54', '#/e/b59', '#/e/b60', '#/p/p6', '#/map', '#/map/b10', '#/lanes', '#/lanes/b30', '#/net/b30', '#/pp', '#/pp/clive', '#/id', '#/id/adm', '#/axis/fis', '#/t/rul', '#/rr/ind', '#/ln', '#/books', '#/terms', '#/end', '#/ul']:
      pg.evaluate("h=>{location.hash=h}",h);pg.wait_for_timeout(350)
      sw=pg.evaluate("document.documentElement.scrollWidth")
      if sw>w: errs.append(f'{h} overflow {sw}')
      pg.screenshot(path=f"{O}/{w}{h.replace('#','').replace('/','_')}.png")
    print(w,errs)
  b.close()
