/* Editor genérico local: não executa código, cálculos ou práticas da matéria. */
(()=>{
'use strict';
const drafts=[];
const el=(tag,cls,text)=>{const node=document.createElement(tag);if(cls)node.className=cls;if(text!==undefined)node.textContent=text;return node;};
for(const host of document.querySelectorAll('.atelier[data-source]')){
 const source=document.getElementById(host.dataset.source);if(!source)continue;
 const initial=source.textContent,filename=host.dataset.filename;
 let own=initial,referenceVisible=false;
 const entry={filename,code:own,observed:'',dirty:false};drafts.push(entry);
 const details=host.closest('.workbench')?.nextElementSibling;
 const reference=details?.matches('.exercise-answer')?details.querySelector('code')?.textContent:null;
 host.classList.add('atelier--pronto');
 const head=el('div','at-cabeca');head.append(el('span','at-selo','rascunho'),el('p','at-titulo',filename));host.append(head);
 host.append(el('p','at-enunciado','Edite e baixe seu arquivo. Este editor não executa a atividade nem verifica o resultado.'));
 const body=el('div','at-corpo'),editor=el('div','at-editor'),preview=el('div','at-preview');
 const row=el('div','at-local-editor'),numbers=el('pre','at-linhas'),field=el('textarea','at-campo');
 field.value=initial;field.spellcheck=false;field.autocomplete='off';field.setAttribute('aria-label','Rascunho de '+filename);numbers.setAttribute('aria-hidden','true');
 row.append(numbers,field);editor.append(row);
 preview.append(el('h4','at-texto','Como realizar a atividade'),el('p','at-texto',host.dataset.execution));
 const label=el('label','at-texto','Resultado observado (registro manual)'),observed=el('textarea','at-observacao');
 observed.setAttribute('aria-label','Observação de '+filename);observed.placeholder='Registre o que realmente observou, sem dados pessoais.';label.append(observed);preview.append(label);
 const state=el('p','at-state');state.setAttribute('role','status');state.setAttribute('aria-live','polite');
 const actions=el('div','at-acoes');let solution=null;
 function update(){numbers.textContent=field.value.split('\n').map((_,i)=>i+1).join('\n');numbers.scrollTop=field.scrollTop;}
 function restore(){if(referenceVisible){field.value=own;referenceVisible=false;field.readOnly=false;solution.textContent='Ver solução';solution.setAttribute('aria-pressed','false');update();}}
 function button(text,fn){const b=el('button','at-btn',text);b.type='button';b.addEventListener('click',fn);actions.append(b);return b;}
 field.addEventListener('scroll',()=>numbers.scrollTop=field.scrollTop);
 field.addEventListener('input',()=>{if(referenceVisible)return;own=field.value;entry.code=own;entry.dirty=own!==initial||!!entry.observed;update();state.textContent='Rascunho nesta sessão; baixe ou exporte antes de sair.';});
 field.addEventListener('keydown',e=>{
  if(field.readOnly)return;
  if(e.key==='Tab'){e.preventDefault();field.setRangeText('    ',field.selectionStart,field.selectionEnd,'end');field.dispatchEvent(new Event('input',{bubbles:true}));}
 });
 observed.addEventListener('input',()=>{entry.observed=observed.value;entry.dirty=own!==initial||!!entry.observed;});
 if(reference){solution=button('Ver solução',()=>{
  if(referenceVisible){restore();state.textContent='Seu rascunho restaurado.';}
  else{own=field.value;field.value=reference;referenceVisible=true;field.readOnly=true;solution.textContent='Voltar ao meu';solution.setAttribute('aria-pressed','true');update();state.textContent='Referência docente; seu rascunho está preservado.';}
 });solution.setAttribute('aria-pressed','false');}
 function reset(){restore();own=initial;field.value=initial;observed.value='';entry.code=initial;entry.observed='';entry.dirty=false;update();state.textContent='Modelo inicial restaurado.';}
 button('Reiniciar',reset);
 button('Copiar meu rascunho',async()=>{try{await navigator.clipboard.writeText(own);state.textContent='Rascunho copiado.';}catch{restore();field.focus();field.select();state.textContent='Use Ctrl+C ou baixe o arquivo.';}});
 button('Baixar meu arquivo',()=>{const url=URL.createObjectURL(new Blob([own],{type:'text/plain;charset=utf-8'}));const a=el('a');a.href=url;a.download=filename;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);state.textContent='Arquivo baixado; envio não é automático.';});
 const expand=button('Expandir painel',()=>{const active=host.classList.toggle('atelier--expandido');expand.setAttribute('aria-pressed',String(active));expand.textContent=active?'Voltar ao editor':'Expandir painel';});expand.setAttribute('aria-pressed','false');
 body.append(editor,preview);host.append(body,actions,state);source.closest('pre').hidden=true;
 document.addEventListener('coursekit:presentation',e=>{if(e.detail.on)restore();});document.addEventListener('coursekit:clear',reset);
 update();state.textContent='Sem salvamento automático; baixe ou exporte antes de recarregar.';
}
window.CourseKit=window.CourseKit||{};window.CourseKit.getDrafts=()=>drafts.filter(x=>x.dirty).map(x=>({...x}));
})();
