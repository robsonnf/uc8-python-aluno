"""Amostra fictícia para leitura comparativa; não é o sistema original completo."""
import json

# models/: entidades e seus vínculos por ID, sem widgets.
ALUNOS = [{"id": 41, "nome": "Lia fictícia"}, {"id": 92, "nome": "Rui fictício"}]
PLANOS = [{"id": 7, "nome": "Plano de treino fictício", "valor_centavos": 10000}]
MATRICULAS = [{"id": 101, "aluno_id": 41, "plano_id": 7}]

# utils/persistencia.py: representação dos dados, sem interface gráfica.
def representar_json(dados):
    return json.dumps(dados, ensure_ascii=False, indent=2)

# controllers/: coordena uma operação com os dados fornecidos.
def consultar_matricula(codigo):
    return next((dict(m) for m in MATRICULAS if m["id"] == codigo), None)

# views/: exibiria o resultado e receberia ações; não há GUI nesta amostra.
# Para discutir: qual regra faltaria antes de permitir excluir o aluno 41?
# Se apenas o nome de Lia fosse corrigido, o vínculo precisaria de outro ID?
if __name__ == "__main__":
    print(representar_json({"alunos": ALUNOS, "planos": PLANOS, "matriculas": MATRICULAS}))
