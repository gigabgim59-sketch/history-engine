import asyncio, json, base64, io
from playwright.async_api import async_playwright
from PIL import Image
U='file:///home/claude/japan/dist/index.html'
O='/tmp/claude-0/-home-claude/4a153826-8782-5b1f-a4c8-74dc680cb13e/scratchpad/guide_jp/'
out={}
def enc(name,png,cssw,maxw):
    im=Image.open(io.BytesIO(png)).convert('RGB')
    # target pixel width = 2x display width
    tw=min(im.width,maxw*2)
    if im.width>tw: im=im.resize((tw,round(im.height*tw/im.width)),Image.LANCZOS)
    dw=min(cssw,maxw); dh=round(im.height*dw/im.width)
    b=io.BytesIO();im.save(b,'WEBP',quality=74,method=6)
    out[name]=('data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode(),dw,dh)
    im.save(O+name+'.png')
    print(name,(dw,dh),len(b.getvalue())//1024,'KB')
async def box(pg,js,pad=12):
    r=await pg.evaluate(js)
    return {'x':max(0,r[0]-pad),'y':max(0,r[1]-pad),'width':r[2]+2*pad,'height':r[3]+2*pad}
UNION="""(sels=>{let x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;for(const s of sels){const e=typeof s==='string'?document.querySelector(s):s;if(!e)continue;const r=e.getBoundingClientRect();x0=Math.min(x0,r.left);y0=Math.min(y0,r.top+scrollY);x1=Math.max(x1,r.right);y1=Math.max(y1,r.bottom+scrollY);}return [x0,y0,x1-x0,y1-y0]})"""
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    ctx=await b.new_context(viewport={'width':1100,'height':900},device_scale_factor=2)
    pg=await ctx.new_page()
    async def go(h,t=600):
      await pg.goto(U+h);await pg.wait_for_timeout(t)
    async def shot(name,clip,maxw=720,hidebar=True,fp=True):
      await pg.evaluate("(h)=>{let st=document.getElementById('capst');if(!st){st=document.createElement('style');st.id='capst';document.head.appendChild(st);}st.textContent=h?'body>header.bar,.fabs,.toast{visibility:hidden!important}':'.fabs,.toast{visibility:hidden!important}'}",hidebar)
      if not fp:
        sy=await pg.evaluate('scrollY');clip=dict(clip);clip['y']=max(0,clip['y']-sy)
      png=await pg.screenshot(clip=clip,full_page=fp);enc(name,png,round(clip['width']),maxw)
    # chapter head → 핵심
    await go('#/e/j45')
    await shot('chapter',await box(pg,UNION+"(['.chead','.q','section.keys'])",16))
    # term popup
    await pg.evaluate("window.scrollTo(0,0)")
    t=await pg.evaluate("(()=>{const t=[...document.querySelectorAll('.guide .term, .rh .term')][2];t.scrollIntoView({block:'center'});t.click();return 1})()");await pg.wait_for_timeout(400)
    await shot('term',await box(pg,"(()=>{const p=document.querySelector('#pop').getBoundingClientRect();const c=document.querySelector('article.col').getBoundingClientRect();const y0=Math.min(p.top,innerHeight/2)-110,y1=p.bottom+20;return [Math.min(c.left,p.left)-4,y0+scrollY,Math.max(c.right,p.right)-Math.min(c.left,p.left)+8,y1-y0]})()",8),720,True,False)
    await pg.click('body',position={'x':5,'y':880});await pg.wait_for_timeout(200)
    # 고리
    await pg.evaluate("[...document.querySelectorAll('h2')].find(h=>h.textContent==='고리').scrollIntoView({block:'center'})");await pg.wait_for_timeout(300)
    await shot('links',await box(pg,UNION+"([[...document.querySelectorAll('h2')].find(h=>h.textContent==='고리').closest('section')])",16))
    # secbar open
    await pg.evaluate("window.scrollTo(0,2400)");await pg.wait_for_timeout(400)
    await pg.click('.sb-cur');await pg.wait_for_timeout(300)
    await shot('secbar',await box(pg,"(()=>{const c=document.querySelector('article.col').getBoundingClientRect();const m=document.querySelector('.secmenu').getBoundingClientRect();const s=document.querySelector('.secbar').getBoundingClientRect();return [c.left,s.top+scrollY,c.width,m.bottom-s.top+40]})()",0),720,True,False)
    # map
    await go('#/map/j45',800)
    await shot('map',await box(pg,UNION+"(['.seg','.mapwrap'])",12),1000)
    # lanes with region
    await go('#/lanes');await pg.click('[data-only="tok"]');await pg.wait_for_timeout(300)
    await shot('lanes',await box(pg,"(()=>{const c=document.querySelector('.ctrl').getBoundingClientRect();const s=document.querySelector('#lsc').getBoundingClientRect();return [s.left,c.top+scrollY,s.width,s.bottom-c.top]})()",12),1000)
    # trail
    await go('#/rr/tok')
    await shot('trail',await box(pg,UNION+"(['main .col .eyebrow','main .col .meter',document.querySelectorAll('main .part')[0]])",16))
    # net
    await go('#/net/j45');await pg.hover('.edg.core',force=True);await pg.wait_for_timeout(300)
    await shot('net',await box(pg,UNION+"(['.netbar','#edinfo','#nsc'])",12),1000)
    # id
    await go('#/id/wor')
    await shot('id',await box(pg,UNION+"(['main .col .eyebrow','.gstrip'])",16))
    # search
    await go('#/');await pg.evaluate("(document.getElementById('capst')||{}).textContent=''");await pg.fill('#q','만주사변');await pg.wait_for_timeout(500);await pg.evaluate("document.querySelector('.tabs').style.visibility='hidden';document.querySelector('.brand').style.visibility='hidden'")
    await shot('search',await box(pg,"(()=>{const r=document.querySelector('#results').getBoundingClientRect();const q=document.querySelector('.sbox').getBoundingClientRect();return [r.left-8,q.top-8,Math.max(r.right,q.right)-r.left+16,r.bottom-q.top+14]})()",0),720,False)
    # 요소별 변천
    await pg.fill('#q','');await pg.evaluate("document.getElementById('results').hidden=true")
    await go('#/ln',700);await pg.evaluate("document.getElementById('results').hidden=true")
    await shot('lnlist',await box(pg,UNION+"(['.lncats',document.querySelectorAll('.lncards .card')[0],document.querySelectorAll('.lncards .card')[1]])",14))
    await go('#/ln/tokyo',700);await pg.evaluate("document.getElementById('results').hidden=true")
    await shot('lineage',await box(pg,UNION+"(['main .col .eyebrow','main .col .q','main .col section.keys',document.querySelectorAll('main .slot')[0]])",14))
    await pg.evaluate("document.getElementById('lnglance').scrollIntoView()");await pg.wait_for_timeout(300)
    await shot('lnglance',await box(pg,UNION+"(['#lnglance','.lnglance',document.querySelectorAll('.lnsteps li')[0]])",14))
    # 밑줄: 하나 긋고, 다른 곳을 골라 단추가 뜬 모습
    await go('#/e/j35',700)
    await pg.evaluate("(sel=>{const p=[...document.querySelectorAll(sel)].find(x=>x.textContent.length>140);const w=document.createTreeWalker(p,NodeFilter.SHOW_TEXT);let t,b=null;while((t=w.nextNode()))if(!b||t.length>b.length)b=t;const r=document.createRange();r.setStart(b,ARGA);r.setEnd(b,Math.min(b.length,ARGB));const s=getSelection();s.removeAllRanges();s.addRange(r);p.scrollIntoView({block:'center'});return 1})".replace('ARGA','4').replace('ARGB','46')+"('main article .slot p')");await pg.wait_for_timeout(400)
    await pg.click('.ub-add');await pg.wait_for_timeout(300)
    await pg.evaluate("(()=>{const mp=document.querySelector('mark.ul').closest('p');const ps=[...document.querySelectorAll('main article p')].filter(x=>x.textContent.length>100);const p=ps[ps.indexOf(mp)+1];const w=document.createTreeWalker(p,NodeFilter.SHOW_TEXT);let t,b=null;while((t=w.nextNode()))if(!b||t.length>b.length)b=t;const r=document.createRange();r.setStart(b,20);r.setEnd(b,Math.min(b.length,52));const s=getSelection();s.removeAllRanges();s.addRange(r);return 1})()");await pg.wait_for_timeout(500)
    await shot('ul',await box(pg,"(()=>{const m=document.querySelector('mark.ul').getBoundingClientRect();const r=getSelection().getRangeAt(0).getBoundingClientRect();const b=document.querySelector('.ulbar').getBoundingClientRect();const c=document.querySelector('article.col').getBoundingClientRect();const y0=Math.min(m.top,r.top,b.top)-20,y1=Math.max(m.bottom,r.bottom,b.bottom)+20;return [c.left,y0+scrollY,c.width,y1-y0]})()",8),720,False,False)
    await pg.evaluate("getSelection().removeAllRanges()")
    await go('#/ul',500)
    await shot('ullist',await box(pg,UNION+"(['main .col .eyebrow','.ulgrp'])",14))
    await go('#/pp',700)
    await shot('pplist',await box(pg,"(()=>{const a=document.querySelector('main h1').getBoundingClientRect();const b=document.querySelector('#plife').getBoundingClientRect();return [b.left,a.top+scrollY,b.width,Math.min(b.bottom,a.top+760)-a.top]})()",14),1000)
    await go('#/pp/ito',700)
    await shot('person',await box(pg,UNION+"(['main .col .chead','main .col section.keys'])",16))
    await go('#/p/p3',700)
    await shot('part',await box(pg,UNION+"(['main .col .chead','main .col .keys','.f3'])",16))
    # mobile
    m=await b.new_context(viewport={'width':390,'height':780},device_scale_factor=2,has_touch=True)
    mp=await m.new_page()
    await mp.goto(U+'#/e/j17');await mp.wait_for_timeout(400);await mp.click('.tb-mark');await mp.evaluate("window.scrollTo(0,1500)");await mp.wait_for_timeout(900)
    await mp.goto(U+'#/e/j35');await mp.wait_for_timeout(500)
    await mp.evaluate("(()=>{const ps=[...document.querySelectorAll('main p')].filter(x=>x.textContent.length>140);const p=ps[2];const w=document.createTreeWalker(p,NodeFilter.SHOW_TEXT);let t,b=null;while((t=w.nextNode()))if(!b||t.length>b.length)b=t;const r=document.createRange();r.setStart(b,2);r.setEnd(b,Math.min(b.length,34));const s=getSelection();s.removeAllRanges();s.addRange(r);const y=p.getBoundingClientRect().top+scrollY-260;window.scrollTo(0,y);return 1})()");await mp.wait_for_timeout(900)
    png=await mp.screenshot();enc('m_ul',png,390,300)
    await mp.click('.ub-add');await mp.wait_for_timeout(300)
    await mp.goto(U+'#/');await mp.wait_for_timeout(2600)
    png=await mp.screenshot();enc('m_home',png,390,300)
    await mp.goto(U+'#/e/j45');await mp.wait_for_timeout(400);await mp.evaluate("window.scrollTo(0,1800)");await mp.wait_for_timeout(300);await mp.evaluate("window.scrollBy(0,-120)");await mp.wait_for_timeout(500)
    png=await mp.screenshot();enc('m_read',png,390,300)
    await b.close()
  json.dump(out,open(O+'imgs.json','w'))
asyncio.run(main())
