# Tarefa-Livre-OO
-------------------------------------------------------------------------------------------------------------------

> Sistema de Gestão de Consultas Médicas
    Este projeto é um Sistema de Gestão de Consultas Médicas que permite gerenciar médicos, consultas e pacientes. Ele foi desenvolvido com foco nos conceitos de Programação Orientada a Objetos (POO), incluindo herança, polimorfismo e encapsulamento.

* Funcionalidades Principais
- Listar médicos disponíveis: Exibe os médicos cadastrados no sistema, com suas especialidades e status de disponibilidade.
- Marcar consultas: Permite agendar uma consulta com um médico disponível.
- Cancelar consultas: Libera o médico para novos agendamentos ao cancelar uma consulta existente.
- Salvar e carregar dados: Armazena os dados de médicos em um arquivo JSON, permitindo persistência e carregamento posterior.

* Estrutura do Código
1. Classes Principais
> Pessoa (Classe Abstrata):
Classe base que define a interface comum para todas as pessoas no sistema.

- Atributos:
nome: Nome da pessoa.

- Métodos:
Métodos de acesso e modificação para o nome.

> Medico (Classe Abstrata)
Herda de Pessoa e define a interface para os médicos.

- Atributos:
    crm: Identificador único do médico.
    disponivel: Indica se o médico está disponível para consultas.

- Métodos:
    marcar_consulta: Altera a disponibilidade para indisponível.
    cancelar_consulta: Torna o médico disponível novamente.

> Especialidades Médicas
Subclasses de Medico que implementam o método especialidade:

- Cardiologista
- Dermatologista
- Pediatra
Entre outras.

2. Classe Gerenciadora

> SistemaHospital
Gerencia a lista de médicos e operações relacionadas.

- Funcionalidades:
    Listar médicos.
    Marcar consultas.
    Cancelar consultas.
    Salvar e carregar médicos do arquivo JSON.

3. Execução do Sistema
A função main inicializa o sistema e oferece um menu interativo para o usuário realizar as seguintes ações:

    Listar Médicos: Exibe a lista de médicos cadastrados.
    Marcar Consulta: Agenda uma consulta com um médico disponível.
    Cancelar Consulta: Libera o médico para novas consultas.
    Salvar Dados: Grava os dados no arquivo JSON.
    Carregar Dados: Carrega os dados do arquivo JSON.
    Sair: Encerra o programa.

> Como Executar
Certifique-se de que o Python está instalado no seu computador.
Salve o código do sistema em um arquivo chamado hospital.py.
Crie um arquivo JSON chamado dados_medicos.json com os dados iniciais dos médicos.
Execute o programa com o seguinte comando no terminal:
python hospital.py
----------------------------------------------------------------------------------------------------

Atividade livre - Encapsulamento, Herança e Polimorfismo

1. Aplicar os conceitos de OO
- Herança
- Polimorfismo
- Encapsulamento (total)

2. Recomendado: usar como rascunho a UML
- Definir com clareza o problema
- Identificar classes
- Modelar as relações
- Comparações
- Abstrações
- Associação
- Dependências (relação de dependência entre duas classes)

3. README
4. Serialização de objetos
    - Txt
    - Json

5. Utilização do terminal para IO (input/output)

6. Pode usar interfaces gráficas 

7. Tema bem definido

8. Preparar tudo em um repositório do github.
-------------------------------------------------------------------------------------------------------------------
triangulo.py : encapsulamento; interação com usuário.
medico.py : herança e polimorfismo.
