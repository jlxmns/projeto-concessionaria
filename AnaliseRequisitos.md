# Análise de Requisitos

## Requisitos Funcionais
#### Login / Cadastro
- Cadastro do usuário salvará informações como veículos favoritados, histórico de simulações de financiamento, histórico de buscas
- Cadastro só é obrigatório ao realizar ações específicas de usuário como adicionar aos favoritos ou seguir para pagamento
#### Página Visualização de veículos
- O usuário deve poder ver os veículos e filtrá-los por nome, tipo, cor, ano, valor, pronta-entrega, e outras características do veículo
- O usuário pode nessa tela adicionar veículos como favoritos
- O usuário pode selecionar um veículo para obter mais detalhes sobre ele para então seguir para pagamento se preferir
#### Tela de detalhes de veículos 
- Tela deve exibir todas as informações existentes sobre o veículo selecionado
- Adicionais, acessórios e alteração de cores podem ser feitos nessa página com seus valores respectivos
- É possível Estimar Pagamento nessa tela
#### Estimar Pagamento
- O sistema deve oferecer uma ferramenta para simular o financiamento do veículo, onde o usuário pode inserir o valor de entrada, taxa de juros e prazo de pagamento, e ver o valor das parcelas.
#### Página Serviços
- Nessa página é possivel verificar e agendar os serviços como revisão e test drive
#### Concessonárias próximas
- Será exibido um mapa da cidade com a localização do usuário centralizada e todas as lojas marcadas no mapa
- Ao clicar no pin da loja o usuário pode escolher agendar serviços sobre ela

## Requisitos Não Funcionais
#### Usabilidade
  - O sistema deve apresentar uma interface atrativa, que satisfaça o usuário.
  - O sistema deve ser intuitivo, com funções de fácil aprendizado e memorização.
    - Tempo de treinamento de usuário entre 15 a 30 minutos 
#### Desempenho
  - O carregamento e as trocas de telas do sistema devem ser rápidas. 
    - Intervalos de resposta menores que 5 segundos.
#### Segurança
  - O sistema deverá ser seguro e preservar a privacidade e os dados pessoais do usuário.
#### Compatibilidade
  - O sistema deverá ser compatível com as versões mais recentes dos principais navegadores:
	 - Chrome
	 - Edge
	 - Safari