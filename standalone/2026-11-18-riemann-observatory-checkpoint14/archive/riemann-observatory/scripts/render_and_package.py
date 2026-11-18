#!/usr/bin/env python3
"""Render offline HTML/PDF original synthesis and distribute analysis, not source PDFs."""
import base64,hashlib,html,json,os,posixpath,re,shutil,zipfile
from argparse import ArgumentParser
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,KeepTogether,Image as RLImage
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
from distribution_policy import PRIVATE_PARTS, is_distributable
R=Path(__file__).resolve().parents[1]
parser=ArgumentParser(description=__doc__)
parser.add_argument('--output',type=Path,help='Write the ZIP and checksum here without updating delivery artifacts')
args=parser.parse_args()
metrics=json.loads((R/'quality/metrics.json').read_text())
cutoff=metrics.get('cutoff','2026-11-17')
coverage_line=(f"{metrics['selected_checkpoint_works']} selected source records · "
 f"{metrics['fulltexts_accessed_selected']} full texts accessed · "
 f"{metrics['whole_work_or_translation_read']} complete readings · "
 f"{metrics['scoped_level3_claim_groups']} independently reviewed scoped claim groups. "
 "The thousand-work mission remains unfinished. No RH resolution or publication novelty is claimed.")
sections=[('Start here','START_HERE.md'),('Executive checkpoint','executive_report.md'),('Coverage','quality/coverage_report.md'),('What we learned','final_synthesis/comprehensive_report.md'),('Strongest connections','connections/strongest_connections.md'),('25 research tasks','final_synthesis/top_25_research_opportunities.md'),('Limitations','quality/limitations.md')]

def rebase_href(href, source_path):
 parts=urlsplit(href)
 if parts.scheme or parts.netloc or not parts.path:return href
 if parts.path.startswith('/'):
  raise ValueError(f'Absolute local synthesis link in {source_path}: {href}')
 joined=posixpath.join(posixpath.dirname(source_path),parts.path)
 target=posixpath.normpath(joined)
 decoded_target=posixpath.normpath(unquote(joined))
 if decoded_target=='..' or decoded_target.startswith(('../','/')) or '\\' in decoded_target:
  raise ValueError(f'Local synthesis link leaves archive in {source_path}: {href}')
 relative=posixpath.relpath(target,'final_synthesis')
 if parts.path.endswith('/'):relative+='/'
 return urlunsplit(('', '', relative, parts.query, parts.fragment))

def inline(text, source_path):
 text=html.escape(text)
 text=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
 text=re.sub(r'`([^`]+)`',r'<code>\1</code>',text)
 def link(match):
  label, escaped_href=match.groups()
  href=html.escape(rebase_href(html.unescape(escaped_href),source_path),quote=True)
  return f'<a href="{href}">{label}</a>'
 text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,text)
 return text

def blocks(text):
 out=[];buf=[];code=False
 def flush():
  if buf:out.append(('p',' '.join(buf)));buf.clear()
 for line in text.splitlines():
  if line.startswith('```'):
   flush();code=not code;continue
  if code:out.append(('code',line));continue
  im=re.match(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$',line)
  if im:flush();out.append(('image',(im[1],im[2])));continue
  if not line.strip():flush();continue
  if re.match(r'^#+\s',line):
   flush();m=re.match(r'^(#+)\s+(.*)',line);out.append(('h'+str(min(len(m[1]),4)),m[2]));continue
  if line.startswith('|'):
   flush()
   if not re.match(r'^\|[- :|]+\|$',line):out.append(('row',[x.strip() for x in line.strip('|').split('|')]))
   continue
  if re.match(r'^[-*] ',line):flush();out.append(('li',line[2:]));continue
  if re.match(r'^\d+\.\s+',line):flush();out.append(('num',line));continue
  buf.append(line)
 flush();return out
parts=[]
for i,(label,path) in enumerate(sections):
 parts.append(f'<section id="s{i}"><p class="eyebrow">{html.escape(label)}</p>')
 bs=blocks((R/path).read_text());table=False
 for kind,text in bs:
  if kind!='row' and table:parts.append('</tbody></table>');table=False
  if kind=='row':
   if not table:parts.append('<table><tbody>');table=True
   parts.append('<tr>'+''.join('<td>'+inline(x,path)+'</td>' for x in text)+'</tr>')
  elif kind=='image':
   alt,src=text;asset=(R/Path(path).parent/src).resolve()
   assert asset.is_relative_to(R) and asset.is_file(),'Invalid local synthesis image'
   mime='image/png' if asset.suffix.lower()=='.png' else 'image/svg+xml'
   data=base64.b64encode(asset.read_bytes()).decode()
   parts.append('<figure><img style="width:100%;height:auto" alt="'+html.escape(alt,quote=True)+'" src="data:'+mime+';base64,'+data+'"><figcaption>'+inline(alt,path)+'</figcaption></figure>')
  elif kind.startswith('h'):parts.append(f'<{kind}>{inline(text,path)}</{kind}>')
  elif kind=='li':parts.append('<p class="bullet">• '+inline(text,path)+'</p>')
  elif kind=='num':parts.append('<p class="bullet">'+inline(text,path)+'</p>')
  elif kind=='code':parts.append('<pre>'+html.escape(text)+'</pre>')
  else:parts.append('<p>'+inline(text,path)+'</p>')
 if table:parts.append('</tbody></table>')
 parts.append('</section>')
css='''*{box-sizing:border-box}body{margin:0;background:#f5f3ec;color:#182435;font:17px/1.7 Georgia,serif}header{background:#12263b;color:#faf7ed;padding:64px max(6vw,24px)}header h1{font-size:clamp(32px,5vw,62px);line-height:1.12;max-width:1000px;margin:12px 0}header p{max-width:850px;color:#d4dce5}.badge{font:12px/1.5 system-ui;letter-spacing:.18em;text-transform:uppercase;color:#d7b771}nav{display:flex;gap:16px;flex-wrap:wrap;font:14px system-ui}nav a{color:#f0d494}main{max-width:1000px;margin:auto;padding:16px 28px 80px}section{padding:42px 0;border-bottom:1px solid #c8c9c9}.eyebrow{font:12px system-ui;letter-spacing:.18em;text-transform:uppercase;color:#8b6332}h1,h2,h3,h4{font-family:system-ui;line-height:1.35}h1{font-size:30px}h2{font-size:24px;margin-top:36px}h3{font-size:20px}a{color:#1c5278}table{font:14px/1.6 system-ui;border-collapse:collapse;width:100%;margin:20px 0}td{padding:10px 12px;border-bottom:1px solid #ccd1d4;vertical-align:top}tr:first-child{background:#e6e9e8;font-weight:600}code,pre{font:14px/1.6 monospace;overflow-wrap:anywhere}pre{white-space:pre-wrap;background:#e6e9e8;padding:6px 12px}.bullet{padding-left:10px}footer{font:13px system-ui;padding:30px;text-align:center}@media print{body{background:white}header{padding:20px}section{break-before:auto}nav{display:none}}'''
ht='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Riemann Observatory · Research checkpoint</title><style>'+css+'</style><header><div class="badge">Research checkpoint · '+html.escape(cutoff)+'</div><h1>The Riemann Observatory</h1><p>'+html.escape(coverage_line)+'</p><nav>'+''.join(f'<a href="#s{i}">{html.escape(x[0])}</a>' for i,x in enumerate(sections))+'</nav></header><main>'+''.join(parts)+'</main><footer>Offline synthesis. Exact provenance, source links, code and continuation instructions are in the accompanying archive.</footer></html>'
(R/'final_synthesis/synthesis.html').write_text(ht)
# Unicode PDF, all original analysis; typesetting is not mathematical certification.
pdfmetrics.registerFont(TTFont('DV','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DV-Bold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('DV',normal='DV',bold='DV-Bold',italic='DV',boldItalic='DV-Bold')
styles=getSampleStyleSheet()
for n in ['Normal','BodyText','Heading1','Heading2','Heading3','Heading4']:
 styles[n].fontName='DV';styles[n].fontSize=9.4;styles[n].leading=14
styles['Heading1'].fontName='DV-Bold';styles['Heading1'].fontSize=20;styles['Heading1'].leading=26
styles['Heading2'].fontName='DV-Bold';styles['Heading2'].fontSize=13;styles['Heading2'].leading=18
styles['Heading3'].fontName='DV-Bold';styles['Heading3'].fontSize=11
styles['Normal'].spaceAfter=8
small=ParagraphStyle('Cell',fontName='DV',fontSize=8,leading=11)
story=[]
for i,(label,path) in enumerate(sections):
 if i:story.append(PageBreak())
 pending=[]
 def flush_table():
  if pending:
   width=490/max(len(x) for x in pending)
   tab=Table([[Paragraph(inline(c,path),small) for c in row] for row in pending],colWidths=[width]*max(len(x) for x in pending),repeatRows=1,hAlign='LEFT')
   tab.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e7ecef')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,-1),.25,colors.HexColor('#ccd2d5')),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
   story.append(tab);story.append(Spacer(1,12));pending.clear()
 for kind,text in blocks((R/path).read_text()):
  if kind=='row':pending.append(text);continue
  flush_table()
  if kind=='image':
   alt,src=text;asset=(R/Path(path).parent/src).resolve()
   assert asset.is_relative_to(R) and asset.is_file(),'Invalid local synthesis image'
   pic=RLImage(str(asset));pic.drawHeight=pic.imageHeight*490/pic.imageWidth;pic.drawWidth=490
   story.append(pic);story.append(Paragraph(inline(alt,path),small));story.append(Spacer(1,12));continue
  if kind.startswith('h'):story.append(Paragraph(inline(text,path),styles['Heading'+kind[1:]]));continue
  if kind=='li':text='• '+text
  # reportlab does not support HTML code tags.
  t=inline(text,path).replace('<code>','').replace('</code>','')
  story.append(Paragraph(t,styles['Normal']))
 flush_table()
def page(canvas,doc):
 canvas.setFont('DV',8);canvas.setFillColor(colors.HexColor('#526477'))
 canvas.drawString(42,23,'Riemann Observatory · incomplete research checkpoint · '+cutoff)
 canvas.drawRightString(552,23,str(doc.page))
doc=SimpleDocTemplate(str(R/'final_synthesis/synthesis.pdf'),pagesize=(595.27,841.89),rightMargin=45,leftMargin=45,topMargin=40,bottomMargin=42,title='Riemann Observatory — Research checkpoint',author='Riemann Observatory research program')
doc.build(story,onFirstPage=page,onLaterPages=page)
# Include originals, logs and reproducible results; omit private source copies and bulky raw API payloads.
files=[]
for current,dirs,names in os.walk(R):
 dirs[:]=[d for d in dirs if d not in PRIVATE_PARTS]
 for name in names:
  p=Path(current)/name
  if not p.is_file() or not is_distributable(p.relative_to(R)):continue
  if str(p.relative_to(R))=='quality/distribution_manifest.json':continue
  files.append(p)
files.sort()
payloads={str(p.relative_to(R)):p.read_bytes() for p in files}
# Active contributors can add tracks during a snapshot. Never distribute a
# half-written JSONL line even when its exact byte hash would be valid.
for name,data in payloads.items():
 if name.endswith('.jsonl'):
  for line in data.decode('utf-8').splitlines():
   if line.strip():json.loads(line)
manifest=[{'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()} for name,data in payloads.items()]
manifest_bytes=(json.dumps({'included_files':len(files)+1,'excluded':['sources/ and raw source staging directories','corpus/raw_discovery/ raw API responses','bytecode, build caches and unapproved source PDFs'],'scope':'File-byte checkpoint during active research; manifest hashes describe the exact bytes in this ZIP. Original PDF allowlist: scripts/distribution_policy.py.','files':manifest},indent=2)+'\n').encode()
(R/'quality/distribution_manifest.json').write_bytes(manifest_bytes)
payloads['quality/distribution_manifest.json']=manifest_bytes
output=args.output if args.output is not None else R.parent/'riemann-observatory.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for name,data in payloads.items():z.writestr('riemann-observatory/'+name,data)
with zipfile.ZipFile(output) as z:
 assert z.testzip() is None
 assert not any('/sources/' in n or '/raw_discovery/' in n for n in z.namelist())
 assert all(is_distributable(n.removeprefix('riemann-observatory/')) for n in z.namelist())
 for row in manifest:assert hashlib.sha256(z.read('riemann-observatory/'+row['path'])).hexdigest()==row['sha256']
checksum=hashlib.sha256(output.read_bytes()).hexdigest()
output.with_suffix('.zip.sha256').write_text(checksum+'  '+output.name+'\n')
if args.output is None:
 Path('/workspace/artifacts').mkdir(exist_ok=True)
 for p in [output,output.with_suffix('.zip.sha256'),R/'final_synthesis/synthesis.html',R/'final_synthesis/synthesis.pdf']:shutil.copy2(p,Path('/workspace/artifacts')/p.name)
print(json.dumps({'zip':str(output),'bytes':output.stat().st_size,'included_files':len(files),'sha256':checksum,'html':str(R/'final_synthesis/synthesis.html'),'pdf':str(R/'final_synthesis/synthesis.pdf')},indent=2))
