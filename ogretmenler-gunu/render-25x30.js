const { chromium } = require('playwright'); const fs=require('fs');
const check = process.argv[2]==='check';
(async () => {
  const b = await chromium.launch();
  let h=fs.readFileSync('tasarim-25x30.html','utf8'); if(!check) h=h.replace('<div id="guide"></div>','');
  fs.writeFileSync('tmp.html',h);
  const p = await b.newPage({ viewport:{width:945,height:1134}, deviceScaleFactor: check?1:3.125 });
  await p.goto('file://'+process.cwd()+'/tmp.html',{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready);
  const r = await p.evaluate(()=>['.stats','.card'].map(s=>{const b=document.querySelector(s).getBoundingClientRect();return s+':'+Math.round(b.top)+'-'+Math.round(b.bottom)}));
  console.log(r.join(' '));
  if(check){await p.screenshot({path:'/tmp/claude-0/check.png'});}
  else{await p.screenshot({path:'ogretmenler-gunu-25x30.png'});await p.pdf({path:'ogretmenler-gunu-25x30.pdf',width:'250mm',height:'300mm',printBackground:true,pageRanges:'1'});}
  fs.unlinkSync('tmp.html'); await b.close();
})();
