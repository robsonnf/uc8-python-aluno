/* Servir somente uma distribuição gerada, nunca a autoria. Sem dependências. */
import {createServer} from 'node:http';
import {readFile,stat,realpath} from 'node:fs/promises';
import {dirname,resolve,extname,sep} from 'node:path';
import {fileURLToPath} from 'node:url';
import {existsSync} from 'node:fs';
const base=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const professor=process.argv.includes('--professor');
const candidate=existsSync(resolve(base,'index.html'))?base:resolve(base,'saida',professor?'professor':'aluno');
if(!existsSync(resolve(candidate,'index.html')))throw Error('Gere primeiro: python scripts/build.py');
const root=await realpath(candidate),host=process.argv.includes('--rede')?'0.0.0.0':'127.0.0.1';
const mime={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.mjs':'text/javascript; charset=utf-8','.json':'application/json; charset=utf-8','.csv':'text/csv; charset=utf-8','.md':'text/plain; charset=utf-8','.txt':'text/plain; charset=utf-8'};
const inside=p=>p===root||p.startsWith(root+sep);
const server=createServer(async(req,res)=>{
 try{
  if(!['GET','HEAD'].includes(req.method)){res.writeHead(405).end();return;}
  const url=new URL(req.url,'http://localhost');let pathname=decodeURIComponent(url.pathname);
  if(pathname.split(/[\\/]/).some(p=>p.startsWith('.'))||pathname.includes('\\')||pathname.includes(':')){res.writeHead(403).end('Acesso negado');return;}
  if(pathname==='/'||pathname==='/lessons'||pathname==='/lessons/')pathname='/index.html';
  const target=resolve(root,pathname.replace(/^\/+/,''));
  if(!inside(target)){res.writeHead(403).end('Acesso negado');return;}
  const canonical=await realpath(target).catch(()=>null);
  if(!canonical||!inside(canonical)||!(await stat(canonical)).isFile()){res.writeHead(404).end('Não encontrado');return;}
  res.writeHead(200,{'content-type':mime[extname(canonical)]||'text/plain; charset=utf-8','cache-control':'no-store','x-content-type-options':'nosniff'});
  if(req.method==='HEAD')res.end();else res.end(await readFile(canonical));
 }catch{res.writeHead(400).end('Requisição inválida');}
});
let port=Number(process.env.PORTA??4321),attempt=0;
if(!Number.isInteger(port)||port<0||port>65535)throw Error('PORTA inválida');
server.on('error',error=>{if(error.code==='EADDRINUSE'&&process.env.PORTA==null&&attempt++<20)server.listen(++port,host);else throw error;});
server.on('listening',()=>{console.log('\nMaterial servido: http://localhost:'+server.address().port+'/');console.log('Distribuição: '+root);console.log(host==='127.0.0.1'?'Acesso somente neste computador.':'Acesso na rede habilitado explicitamente; compartilhe apenas o aluno.');console.log('Ctrl+C para parar.');});
server.listen(port,host);
