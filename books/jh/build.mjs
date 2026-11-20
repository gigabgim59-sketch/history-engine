// 소스가 사라진 책(DEFECTS je-02·jh-02)을 다시 빌드한다: book.json(출간본에서 되살린 DATA) + template.html(출간본의 템플릿).
// 본문을 고칠 때는 book.json의 body를, 화면을 고칠 때는 template.html을 고친다. 그다음 python3 font.py dist/index.html.
import fs from 'fs';
const D=JSON.parse(fs.readFileSync('book.json','utf8'));
const t=fs.readFileSync('template.html','utf8');
if(!t.includes('/*__DATA__*/'))throw new Error('template.html에 /*__DATA__*/ 자리가 없다');
fs.mkdirSync('dist',{recursive:true});
fs.writeFileSync('dist/index.html',t.replace('/*__DATA__*/',()=>'const DATA='+JSON.stringify(D)+';'));
console.log('ok', D.events.length+'장');
