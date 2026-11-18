import json
import os

ARQUIVO_DADOS = "tarefas.json"

def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON, se ele existir."""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

def salvar_tarefas(tarefas):
    """Salva a lista de tarefas atualizada no arquivo JSON."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

def listar_tarefas(tarefas):
    """Exibe todas as tarefas cadastradas com seus status."""
    if not tarefas:
        print("\n📝 Nenhuma tarefa cadastrada.")
        return
    print("\n--- LISTA DE TAREFAS ---")
    for index, tarefa in enumerate(tarefas, 1):
        status = "✅ Concluída" if tarefa["concluida"] else "⏳ Pendente"
        print(f"{index}. [{status}] {tarefa['descricao']}")

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa à lista."""
    descricao = input("\nDigite a descrição da tarefa: ").strip()
    if descricao:
        tarefas.append({"descricao": descricao, "concluida": False})
        salvar_tarefas(tarefas)
        print("✨ Tarefa adicionada com sucesso!")
    else:
        print("⚠️ A descrição não pode estar vazia.")

def concluir_tarefa(tarefas):
    """Marca uma tarefa específica como concluída."""
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        num = int(input("\nDigite o número da tarefa que deseja concluir: "))
        if 1 <= num <= len(tarefas):
            tarefas[num - 1]["concluida"] = True
            salvar_tarefas(tarefas)
            print("🎉 Tarefa marcada como concluída!")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Por favor, digite um número válido.")

def remover_tarefa(tarefas):
    """Remove uma tarefa da lista."""
    listar_tarefas(tarefas)
    if not tarefas:
        return
    try:
        num = int(input("\nDigite o número da tarefa que deseja remover: "))
        if 1 <= num <= len(tarefas):
            removida = tarefas.pop(num - 1)
            salvar_tarefas(tarefas)
            print(f"🗑️ Tarefa '{removida['descricao']}' removida com sucesso!")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Por favor, digite um número válido.")

def main():
    """Função principal que gerencia o menu do programa."""
    tarefas = carregar_tarefas()
    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("\nAté logo! Bons estudos e boa sorte no processo seletivo! 🚀")
            break
        else:
            print("❌ Opção inválida. Escolha entre 1 e 5.")

if __name__ == "__main__":
    main()