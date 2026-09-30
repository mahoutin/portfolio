from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json,re
root=Path(__file__).resolve().parents[1]
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='img' and a.get('src'):assert a.get('alt'),'Image missing alternative text'
  for name in ['src','href']:
   if a.get(name):self.refs.append(a[name])
pages=['index.html','nomi/index.html','aie-insured-portal/index.html','coverage-collective/index.html','resume/index.html']
for name in pages:
 page=root/name;p=Parser();p.feed(page.read_text());assert p.h1==1
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme:continue
  target=root/u.path.lstrip('/') if u.path else page
  if target.is_dir():target/='index.html'
  assert target.is_file(),(name,ref)
  if u.fragment:
   q=Parser();q.feed(target.read_text());assert u.fragment in q.ids,(name,ref)
 assert 'chatgpt.site' not in page.read_text()
 assert '<meta name="robots" content="noindex,nofollow">' not in page.read_text()
fonts=(root/'fonts.css').read_text()
for path in re.findall(r'url\(([^)]+)\)',fonts):assert(root/path.lstrip('/')).is_file()
assert(root/'assets/fonts/OFL.txt').is_file()
assert(root/'assets/alexander-hounsou-resume.pdf').read_bytes().startswith(b'%PDF-')
css=(root/'studio.css').read_text();assert '@media(max-width:650px)' in css and '@media(max-width:1000px)' in css
assert 'prefers-reduced-motion' in (root/'style.css').read_text()
config=json.loads((root/'vercel.json').read_text())
assert config['git']['deploymentEnabled']['studio-redesign'] is False
for rewrite in config['rewrites']:assert(root/rewrite['destination'].lstrip('/')).is_file()
assert not(root/'.openai').exists()
print('PASS: five pages; local links, anchors, assets, fonts/license, PDF signature, responsive CSS and route/deployment configuration')
