import sys
from playwright.sync_api import sync_playwright
O=sys.argv[1]
with sync_playwright() as p:
  b=p.chromium.launch()
  for w in (390,1280):
    pg=b.new_page(viewport={'width':w,'height':900});errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/taiwan/dist/index.html');pg.wait_for_timeout(500)
    for h in ['#/', '#/p/p1', '#/p/p2', '#/p/p3', '#/p/p4', '#/end', '#/map', '#/map/t07', '#/net/t12', '#/books', '#/terms', '#/rr/nb', '#/e/t01', '#/e/t02', '#/e/t03', '#/e/t04', '#/e/t05', '#/e/t06', '#/e/t07', '#/e/t08', '#/e/t09', '#/e/t10', '#/e/t11', '#/e/t12', '#/e/t13', '#/e/t14', '#/e/t15', '#/e/t16', '#/e/t17', '#/e/t18', '#/e/t19', '#/e/t20']:
      pg.evaluate("h=>{location.hash=h}",h);pg.wait_for_timeout(350)
      sw=pg.evaluate("document.documentElement.scrollWidth")
      if sw>w: errs.append(f'{h} overflow {sw}')
      pg.screenshot(path=f"{O}/{w}{h.replace('#','').replace('/','_')}.png")
    print(w,errs)
  b.close()
