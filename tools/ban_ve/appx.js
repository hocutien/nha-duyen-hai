const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const f of ['dien','nuoc','mang']){await p.goto('file://'+process.argv[2]+'/'+f+'.html');await p.waitForTimeout(500);
await p.pdf({path:process.argv[3]+'/'+f+'.pdf',format:'A3',landscape:true,printBackground:true,margin:{top:'12mm',bottom:'12mm',left:'15mm',right:'12mm'}});}
await b.close();})();
