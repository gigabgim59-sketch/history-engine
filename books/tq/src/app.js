(function(){
var store={get:function(k){try{return localStorage.getItem(k)}catch(e){return null}},set:function(k,v){try{localStorage.setItem(k,v)}catch(e){}}};
var root=document.documentElement,t=store.get('tq-theme');if(t)root.setAttribute('data-theme',t);
document.getElementById('theme').onclick=function(){
 var dark=root.getAttribute('data-theme')?root.getAttribute('data-theme')==='dark':matchMedia('(prefers-color-scheme: dark)').matches;
 var n=dark?'light':'dark';root.setAttribute('data-theme',n);store.set('tq-theme',n);};
var body=document.body;
document.getElementById('menu').onclick=function(e){e.stopPropagation();body.classList.toggle('menu');};
document.addEventListener('click',function(e){if(body.classList.contains('menu')&&!e.target.closest('.toc'))body.classList.remove('menu');});
document.querySelectorAll('.toc a').forEach(function(a){a.addEventListener('click',function(){body.classList.remove('menu');});});
// 찾기: 쟁점 본문 전체에서 낱말을 찾아 맞는 쟁점만 남긴다
var qs=[].slice.call(document.querySelectorAll('section.issue[data-text]')),hit=document.getElementById('hit'),inp=document.getElementById('q'),tm;
function norm(s){return s.toLowerCase().replace(/\s+/g,'')}
var idx=qs.map(function(s){return norm(s.getAttribute('data-text'))});
function find(){var v=norm(inp.value);var n=0;
 qs.forEach(function(s,i){var on=!v||idx[i].indexOf(v)>=0;s.classList.toggle('off',!on);if(on)n++;
  var li=document.querySelector('.toc li[data-q="'+s.id+'"]');if(li)li.classList.toggle('off',!on);});
 document.querySelectorAll('.part').forEach(function(p){if(p.id==='apx')return;var any=false,el=p.nextElementSibling;
  while(el&&!el.classList.contains('part')){if(el.classList.contains('issue')&&!el.classList.contains('off'))any=true;el=el.nextElementSibling;}
  p.style.display=(!v||any)?'':'none';});
 hit.textContent=v?('‘'+inp.value+'’: 쟁점 '+n+'개'):'';}
inp.addEventListener('input',function(){clearTimeout(tm);tm=setTimeout(find,150);});
// 전통 강조
var sel=document.getElementById('tr');
sel.addEventListener('change',function(){var v=sel.value;
 document.querySelectorAll('table.pos tbody tr').forEach(function(tr){var tg=(tr.getAttribute('data-tags')||'').split(' ');
  tr.classList.toggle('hl',!!v&&tg.indexOf(v)>=0);tr.classList.toggle('dim',!!v&&tg.indexOf(v)<0);});
 store.set('tq-trad',v);});
var sv=store.get('tq-trad');if(sv){sel.value=sv;sel.dispatchEvent(new Event('change'));}
})();
