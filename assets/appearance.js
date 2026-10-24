/* Só a preferência visual é guardada; tentativas e formulários continuam sem autosave. */
(()=>{
'use strict';
const root=document.documentElement,key='uc8-theme';
const valid=value=>value==='light'||value==='dark';
let saved=null;try{saved=localStorage.getItem(key);}catch{}
// O link explícito prevalece sobre a escolha salva e a preferência do sistema.
const requested=new URL(location.href).searchParams.get('theme');
let theme=valid(requested)?requested:valid(saved)?saved:matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
root.dataset.theme=theme;
function links(){
 // Só links HTML relativos recebem o tema; downloads, âncoras e URLs externas permanecem intactos.
 for(const link of document.querySelectorAll('a[href]')){
  const href=link.getAttribute('href');
  if(href.startsWith('#')||/^[a-z][a-z0-9+.-]*:/i.test(href)||! /\.html(?:[?#]|$)/i.test(href))continue;
  const [beforeHash,...hash]=href.split('#'),[path,...query]=beforeHash.split('?');
  const params=new URLSearchParams(query.join('?'));params.set('theme',theme);
  link.setAttribute('href',path+'?'+params.toString()+(hash.length?'#'+hash.join('#'):''));
 }
}
function bind(){
 const control=document.getElementById('theme-toggle');if(!control)return;
 function label(){
  const action=theme==='dark'?'Ativar tema claro':'Ativar tema escuro';
  control.setAttribute('aria-label',action);control.title=action;
 }
 label();links();root.classList.add('appearance-ready');
 // Alternar a paleta não recarrega a página nem altera os rascunhos em edição.
 control.addEventListener('click',()=>{
  theme=theme==='dark'?'light':'dark';root.dataset.theme=theme;label();
  try{localStorage.setItem(key,theme);}catch{}
  try{const url=new URL(location.href);url.searchParams.set('theme',theme);history.replaceState(null,'',url.href);}catch{}
  links();
 });
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',bind,{once:true});else bind();
})();
