import sys
from playwright.sync_api import sync_playwright
O=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch()
  for w in (390,1280):
    pg=b.new_page(viewport={'width':w,'height':900});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/revol/dist/index.html');pg.wait_for_timeout(500)
    for h in ['#/', '#/p/p1', '#/e/v01', '#/e/v06', '#/e/v07', '#/e/v09', '#/e/v10', '#/p/p2', '#/e/v11', '#/e/v12', '#/e/v13', '#/e/v14', '#/e/v15', '#/e/v16', '#/e/v18', '#/e/v20', '#/e/v60', '#/p/p6', '#/map', '#/map/v07', '#/lanes', '#/lanes/v09', '#/net/v09', '#/pp', '#/pp/louis16', '#/id', '#/id/san', '#/axis/rig', '#/t/sov', '#/rr/par', '#/ln', '#/books', '#/terms', '#/end', '#/ul']:
      pg.evaluate("h=>{location.hash=h}",h);pg.wait_for_timeout(350)
      sw=pg.evaluate("document.documentElement.scrollWidth")
      if sw>w: errs.append(f'{h} overflow {sw}')
      pg.screenshot(path=f"{O}/{w}{h.replace('#','').replace('/','_')}.png")
    print(w,errs)
  b.close()
