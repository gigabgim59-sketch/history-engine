import sys, asyncio
from playwright.async_api import async_playwright
OUT='/tmp/claude-0/-home-claude/4a153826-8782-5b1f-a4c8-74dc680cb13e/scratchpad/shots/'
routes=sys.argv[1:]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for dark in (False,):
            pg=await b.new_page(viewport={'width':1280,'height':900},color_scheme='dark' if dark else 'light')
            errs=[]
            pg.on('pageerror',lambda e: errs.append(str(e)))
            pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
            await pg.goto('file:///home/claude/eurasia/dist/eurasia.html')
            for r in routes:
                name,_,w=r.partition('@')
                if w: await pg.set_viewport_size({'width':int(w),'height':900})
                await pg.evaluate(f"location.hash='{name}'")
                await pg.wait_for_timeout(250)
                fn=OUT+(name.replace('#/','').replace('/','_') or 'home')+(('_'+w) if w else '')+('_d' if dark else '')+'.png'
                await pg.screenshot(path=fn,full_page=False)
                print(fn)
            print('errors',errs)
        await b.close()
asyncio.run(main())
