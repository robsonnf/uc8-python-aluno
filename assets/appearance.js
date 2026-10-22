/* Só a preferência visual é guardada; tentativas e formulários continuam sem autosave. */
(()=>{
'use strict';
const root=document.documentElement,key='uc8-theme';
const valid=value=>value==='light'||value==='dark';
let saved=null;try{saved=localStorage.getItem(key);}catch{}
const requested=new URL(location.href).searchParams.get('theme');
let theme=valid(requested)?requested:valid(saved)?saved:matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
root.dataset.theme=theme;root.classList.add('appearance-ready');
function links(){
 for(const link of document.querySelectorAll('a[href]')){
  const href=link.getAttribute('href');
  if(href.startsWith('#')||/^[a-z][a-z0-9+.-]*:/i.test(href)||! /\.html(?:[?#]|$)/i.test(href))continue;
  const [beforeHash,...hash]=href.split('#'),[path,...query]=beforeHash.split('?');
  const params=new URLSearchParams(query.join('?'));params.set('theme',theme);
  link.setAttribute('href',path+'?'+params.toString()+(hash.length?'#'+hash.join('#'):''));
 }
}
function bind(){
 const control=document.getElementById('theme-select');if(!control)return;
 control.value=theme;links();
 control.addEventListener('change',()=>{
  if(!valid(control.value))return;
  theme=control.value;root.dataset.theme=theme;
  try{localStorage.setItem(key,theme);}catch{}
  try{const url=new URL(location.href);url.searchParams.set('theme',theme);history.replaceState(null,'',url.href);}catch{}
  links();
 });
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',bind,{once:true});else bind();
})();
