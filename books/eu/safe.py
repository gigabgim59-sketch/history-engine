exec(open('/tmp/claude-0/-home-claude/4a153826-8782-5b1f-a4c8-74dc680cb13e/scratchpad/ext5.py').read().split("run('/home")[0])
_run=run
def srun(f,adds):
    s=open(f,encoding='utf-8').read()
    for ch,sec,_ in adds:
        i=s.index('\n'+ch+':{'); end=s.index('\n},',i)
        assert s.find('\n'+sec+':[',i,end)>0, (ch,sec,'missing')
    _run(f,adds)
