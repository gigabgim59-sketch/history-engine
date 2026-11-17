import json,re,subprocess,pdfplumber
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter,PdfReader
def pdf(src,out,nofoot=False):
  with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page()
    h=open(src).read()
    if nofoot:h=h.replace('</style>','@page{@bottom-center{content:none}}</style>')
    open(src,'w').write(h)
    pg.goto('file:///home/claude/enl/'+src);pg.wait_for_timeout(500)
    pg.pdf(path=out,prefer_css_page_size=True,print_background=True);b.close()
def toc():
  T={}
  with pdfplumber.open('print/body.pdf') as d:
    for i,pg in enumerate(d.pages):
      for m in re.findall(r'§(\w+)§',pg.extract_text() or ''):T.setdefault(m,i+1)
  return T
subprocess.run(['node','print/make.mjs'],check=True)
pdf('print/body.html','print/body.pdf')
T=toc();json.dump(T,open('print/toc.json','w'))
subprocess.run(['node','print/make.mjs'],check=True)
pdf('print/front.html','print/front.pdf',True)
w=PdfWriter()
for f in ['print/front.pdf','print/body.pdf']:
  for pg in PdfReader(f).pages:w.add_page(pg)
w.write('print/enl_a4.pdf')
print('front',len(PdfReader('print/front.pdf').pages),'body',len(PdfReader('print/body.pdf').pages),'toc',len(T))
