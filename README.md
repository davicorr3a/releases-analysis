# **Análise das Releases do Bootstrap**

Será apresentada a estratégia de releases do projeto **Bootstrap**,
identificando a organização, hierarquia e critérios utilizados para
disponibilização das versões. Além disso, com base no artigo **\"Mining
the Technical Roles of GitHub Users\"**, será feita uma análise dos
perfis técnicos dos contribuidores e sua relação com as mudanças
realizadas em cada release.

A seguir, serão analisadas **10 releases mais recentes**, destacando
suas principais características, tipos de mudanças implementadas e
padrões de contribuição. Ao final, será traçado um perfil geral da
estratégia de releases do projeto.

## **Análise das Releases**

### **Release 1: v5.3.3**

**Data de lançamento:** 20 de fevereiro de 2024\
**Principais mudanças:**

-   Correção de uma alteração crítica introduzida no gerenciamento de
    > cores, garantindo compatibilidade com compilações Sass.

-   Melhorias na acessibilidade e renderização de badges para garantir
    > legibilidade em diferentes temas (light/dark mode).

-   Ajustes na documentação para esclarecer o uso do color-scheme().

-   Melhorias na sanitização do HTML para permitir elementos \<dl\>,
    > \<dt\> e \<dd\>.

-   Correções visuais em componentes como **accordion, buttons e navbar
    > toggler**.

-   Ajustes no RTL (Right-to-Left) do carrossel e modais para melhor
    > exibição em idiomas que usam escrita da direita para a esquerda.

-   Atualização de dependências e melhorias no pipeline de testes
    > automatizados.

**Características Relevantes:**

-   **Áreas afetadas:** CSS, JavaScript, Documentação, Infraestrutura
    > DevOps.

-   **Perfis técnicos envolvidos:** Principalmente desenvolvedores
    > **Frontend** (devido às melhorias no CSS e temas) e **DevOps**
    > (ajustes no pipeline CI/CD).

-   **Contribuidores principais:** Equipe central do Bootstrap e membros
    > recorrentes da comunidade open-source.

-   **Padrões arquiteturais aplicados:** Modularidade no Sass,
    > saneamento de HTML para segurança.

-   **Frequência de contribuição por tipo de desenvolvedor:**
    > Predominância de contribuições de **Frontend Engineers**, seguidos
    > por DevOps e Documentação.

### **Release 2: v5.3.2**

**Data de lançamento:** 14 de setembro de 2023

**Principais mudanças:**

-   Correção de warnings de depreciação do Sass relacionados ao uso de
    > abs() e divide().

-   Melhorias na compatibilidade com **Dart Sass v1.65.0**.

-   Correção de problemas no sistema de colapso do Bootstrap ao usar
    > múltiplos IDs.

-   Aumento do contraste do fundo do **form range track** para melhor
    > acessibilidade em temas claros e escuros.

-   Melhorias no suporte à personalização da cor de elementos \<mark\>.

-   Atualizações na documentação, incluindo links para **Discord** e
    > **subreddit do Bootstrap**.

-   Uso de variáveis CSS para box-shadow, melhorando a flexibilidade das
    > personalizações.

-   Melhorias em testes e atualização de dependências do projeto.

**Características Relevantes:**

-   **Áreas afetadas:** CSS, JavaScript, Documentação, Acessibilidade,
    > Infraestrutura.

-   **Perfis técnicos envolvidos:**

    -   **Frontend Engineers** (principais mudanças no CSS e sistema de
        > cores).

    -   **JavaScript Developers** (correções no comportamento do sistema
        > de colapso).

    -   **Documentação** (atualização de guias e referências da
        > comunidade).

    -   **DevOps** (atualização de scripts de build e permissões do
        > CI/CD).

-   **Contribuidores principais:** Mantenedores do Bootstrap e
    > contribuidores da comunidade.

-   **Padrões arquiteturais aplicados:** Modularização do Sass,
    > utilização de variáveis CSS para personalização.

-   **Frequência de contribuição por tipo de desenvolvedor:** Forte
    > presença de desenvolvedores **Frontend**, seguido por
    > especialistas em **JavaScript e Documentação**.

### **Release 3: v5.3.1**

**Data de lançamento:** 26 de Julho de 2023\
**Principais mudanças:**

-   Melhorias no **modo escuro**, aumentando o contraste do texto.

-   Inclusão do **script de troca de tema** nos pacotes de exemplos ZIP.

-   **Melhoria nos componentes:**

    -   Melhor estilização para .nav-links desabilitados.

    -   Suporte às teclas **Home** e **End** para navegação entre abas
        > via teclado.

    -   Ajustes na cor do **carousel** em modo escuro.

-   **Aprimoramento de formulários:** Correção da cor do texto de labels
    > flutuantes desativadas.

-   **Novos utilitários:** .text-bg-\* agora utiliza variáveis CSS.

-   **Aprimoramentos no Sass:**

    -   Adição de \$navbar-dark-icon-color.

    -   Remoção de variáveis duplicadas \$alert-\*.

    -   Nova variável \$vr-border-width para customizar a largura do
        > vertical rule helper.

-   **Documentação:**

    -   Adicionada funcionalidade de **busca na homepage**.

    -   Melhor responsividade no **exemplo do dashboard**.

    -   Ajustes na renderização em **modo escuro do Cheatsheet**.

**Características Relevantes:**

-   **Áreas afetadas:** CSS, JavaScript, Acessibilidade, Sass,
    > Documentação.

-   **Perfis técnicos envolvidos:**

    -   **Frontend Engineers** (refinamento de estilos, melhorias na
        > navegação e acessibilidade).

    -   **JavaScript Developers** (suporte a novos atalhos no teclado e
        > melhorias no script de troca de tema).

    -   **UX Designers** (melhorias no contraste e experiência do
        > usuário no modo escuro).

    -   **Documentação** (adaptação da homepage e melhorias de
        > usabilidade).

-   **Contribuidores principais:** Mantenedores do Bootstrap e
    > colaboradores recorrentes.

-   **Padrões arquiteturais aplicados:** Modularização do CSS e
    > JavaScript, melhoria contínua da experiência do usuário.

-   **Frequência de contribuição por tipo de desenvolvedor:** Forte
    > presença de **Frontend Engineers**, UX Designers e Documentação.

### **Release v5.3.0-alpha2 (Pré-release)**

**Data de lançamento:** \[Data não informada\]\
**Principais mudanças:**

-   Introdução do **modo escuro** aprimorado, com suporte aprimorado
    > para temas adaptáveis.

-   Adição da classe .nav-underline para melhor estilização de
    > navegação.

-   Melhorias na acessibilidade e suporte para atalhos de teclado em
    > navegação por abas.

-   Ajustes no **progress bar**, formulários e componentes interativos
    > para maior consistência visual.

-   Reestruturação do Sass e variáveis CSS para facilitar a
    > personalização de temas.

-   Melhorias na documentação, incluindo novas seções sobre utilitários
    > de cores e acessibilidade.

-   Atualizações na lógica de eventos do **offcanvas e modais** para
    > comportamento mais previsível.

-   Ajustes no sistema de cores para maior conformidade com o padrão
    > **WCAG 2.2**.

-   Correções de compatibilidade com navegadores, incluindo melhorias
    > para Android Chrome.

-   Atualizações no framework de testes e pipeline de build para melhor
    > desempenho.

**Características Relevantes:**

-   **Áreas afetadas:** CSS, JavaScript, Documentação, Acessibilidade,
    > DevOps.

-   **Perfis técnicos envolvidos:**

    -   **Frontend Engineers** (trabalho extenso em cores, utilitários,
        > e acessibilidade).

    -   **JavaScript Developers** (ajustes em eventos e interatividade
        > de componentes).

    -   **UX Designers** (melhoria no contraste de cores e foco na
        > experiência do usuário).

    -   **Documentação** (expansão dos guias e aprimoramento de
        > exemplos).

-   **Contribuidores principais:** Membros da equipe central do
    > Bootstrap e comunidade open-source.

-   **Padrões arquiteturais aplicados:** Modularização do Sass,
    > melhorias na separação entre temas claros e escuros.

-   **Frequência de contribuição por tipo de desenvolvedor:** Forte
    > presença de **Frontend Engineers**, seguidos por **JavaScript
    > Developers** e **especialistas em acessibilidade**.

### **Release v5.2.2**

**Data de lançamento:** 3 de outubro de 2022\
**Principais mudanças:**

-   **Accordion:** Agora usa uma variável Sass para cor em vez de uma
    > variável CSS inválida.

-   **Botões:** Ajustes na estilização do hover para .btn-check.

-   **Dropdowns:** Restaurada a funcionalidade de dropdowns sem
    > data-attribute (mas será removida novamente no v6).

-   **Modais:** Melhorias nos eventos dos modais.

-   **Tabelas:** Correção na redefinição do \$border-color dentro do
    > mixin table-variant().

-   **Tabs:**

    -   Removido o **autofocus** automático que causava saltos na página
        > ao ativar tabs.

    -   Ajuste na alternância da classe .active dentro de dropdowns.

-   **Toasts:** Ajuste no z-index das **notificações toast**.

-   **Tooltips:** Correção nos **seletores de tooltips** para elementos
    > criados dinamicamente.

**Características Relevantes:**

-   **Áreas afetadas:** CSS, JavaScript, Acessibilidade, Documentação.

-   **Perfis técnicos envolvidos:**

    -   **Frontend Engineers** (ajustes no Sass e variáveis CSS).

    -   **JavaScript Developers** (correção de comportamento de
        > tooltips, modais e tabs).

    -   **UX Designers e Acessibilidade** (melhoria na usabilidade de
        > componentes interativos).

    -   **Documentação** (atualizações em exemplos e explicações de
        > comportamento dos componentes).

-   **Contribuidores principais:** Equipe Bootstrap e membros da
    > comunidade open-source.

-   **Padrões arquiteturais aplicados:** Modularização do CSS, melhoria
    > da acessibilidade e refinamento da experiência do usuário.

-   **Frequência de contribuição por tipo de desenvolvedor:**
    > Equilibrada entre **Frontend Engineers, JavaScript Developers e UX
    > Designers**.

### **Análise da Release v5.2.1**

**Data de lançamento:** 7 de setembro de 2022\
**Principais mudanças:**

-   **Accordion:** Agora usa a variável Sass \$accordion-button-color
    > para definir cores em vez da função de contraste.

-   **Botões:**

    -   Adicionada uma variável CSS para a **cor da borda no hover** de
        > botões transparentes.

    -   .btn-link não apresenta mais gradiente quando \$enable-gradients
        > está ativado.

-   **Formulários:**

    -   Ajustado o **z-index** do input-group para garantir renderização
        > correta em campos validados.

    -   Floating labels agora redefinem text-align para garantir
        > estilização consistente.

-   **List Groups:**

    -   Ajustes para garantir que **list groups horizontais** com um
        > único item renderizem corretamente o border-radius.

    -   Melhor suporte para imports aninhados da CSS do Bootstrap.

-   **Modais:**

    -   Correção nos **event listeners**, permitindo que cliques na
        > scrollbar não fechem o modal.

-   **Paginação:**

    -   Ajuste nos valores de border-radius dentro dos componentes de
        > paginação.

-   **Scrollspy:**

    -   Nova opção para configurar o **threshold** do Scrollspy.

-   **Tooltips:**

    -   Algumas alterações no plugin de tooltips foram revertidas para
        > evitar problemas com seletores e tooltips dinâmicos.

**Características Relevantes:**

-   **Áreas afetadas:** CSS, JavaScript, Acessibilidade, Documentação.

-   **Perfis técnicos envolvidos:**

    -   **Frontend Engineers** (ajustes no Sass e componentes visuais).

    -   **JavaScript Developers** (correções no comportamento de
        > tooltips, modais e scrollspy).

    -   **UX Designers e Acessibilidade** (melhoria na navegabilidade e
        > experiência do usuário).

    -   **Documentação** (expansão de exemplos e guias sobre o
        > comportamento dos componentes).

-   **Contribuidores principais:** Equipe Bootstrap e membros da
    > comunidade open-source.

-   **Padrões arquiteturais aplicados:** Modularização do CSS, melhoria
    > na acessibilidade e refinamento na experiência do usuário.

-   **Frequência de contribuição por tipo de desenvolvedor:** Forte
    > presença de **Frontend Engineers e JavaScript Developers**, com
    > suporte significativo de **especialistas em UX/Acessibilidade**.

### **Análise da Release v5.2.0**

**Data de lançamento:** 19 de julho de 2022

**Resumo das principais mudanças:\
** A versão 5.2.0 trouxe melhorias significativas na **usabilidade,
acessibilidade e estrutura do código** do Bootstrap. O **Scrollspy** foi
aprimorado para suportar **scroll suave**, e os **input groups** foram
ajustados para melhor integração com **floating forms**. No CSS, houve
**refinamento de estilos em botões e formulários**, além de ajustes no
comportamento de elementos como **accordion, modais e tooltips**. No
JavaScript, diversas correções foram feitas para garantir maior
estabilidade dos **eventos e interações** dentro dos componentes
interativos. Além disso, foram atualizados guias na documentação,
incluindo **Webpack, Parcel e Vite**, para melhor orientar os
desenvolvedores sobre o uso do framework.

**Características Relevantes:**

-   **Áreas afetadas:** CSS, JavaScript, Acessibilidade, Documentação.

-   **Perfis técnicos envolvidos:**

    -   **Frontend Engineers** (ajustes nos componentes visuais e
        > comportamento do Scrollspy).

    -   **JavaScript Developers** (correções em eventos de modais,
        > tooltips e interações com popovers).

    -   **UX Designers e Acessibilidade** (melhorias no design e na
        > experiência do usuário em formulários e navegação).

    -   **Documentação** (novos guias e atualizações para Webpack,
        > Parcel e Vite).

-   **Contribuidores principais:** Equipe Bootstrap e colaboradores da
    > comunidade open-source.

-   **Padrões arquiteturais aplicados:** Modularização do CSS,
    > refinamento da experiência do usuário e suporte aprimorado para
    > frameworks modernos.

-   **Frequência de contribuição por tipo de desenvolvedor:**
    > Equilibrada entre **Frontend Engineers, JavaScript Developers e
    > especialistas em acessibilidade**.

### **Análise da Release v4.6.2**

**Data de lançamento:** 19 de julho de 2022\
**Resumo das principais mudanças:\
**A versão 4.6.2 trouxe melhorias na **documentação, acessibilidade e
compatibilidade do Bootstrap**. Foi adicionada uma nova **classe oficial
para colapsos horizontais**, facilitando o uso dessa funcionalidade no
Collapse Plugin. Além disso, foi feita uma substituição da **propriedade
CSS color-adjust por print-color-adjust**, corrigindo warnings gerados
pela atualização do **Autoprefixer**. Outras melhorias incluem **ajustes
no tamanho do texto pequeno (.small)**, aprimoramentos na
**acessibilidade de dropdowns**, correções de links quebrados na
documentação e **atualizações de dependências** para maior estabilidade
do framework.

**Características Relevantes:**

-   **Áreas afetadas:** CSS, JavaScript, Acessibilidade, Documentação.

-   **Perfis técnicos envolvidos:**

    -   **Frontend Engineers** (ajustes no Sass e melhorias visuais).

    -   **JavaScript Developers** (adição da classe de colapso
        > horizontal e refinamentos no Collapse Plugin).

    -   **UX Designers e Acessibilidade** (melhoria na experiência do
        > usuário em dropdowns e contrastes de cores).

    -   **Documentação** (correção de links e aprimoramento do material
        > explicativo).

-   **Contribuidores principais:** Equipe Bootstrap e novos
    > colaboradores da comunidade open-source.

-   **Padrões arquiteturais aplicados:** Modularização do CSS,
    > aprimoramento da acessibilidade e refinamento da experiência do
    > usuário.

-   **Frequência de contribuição por tipo de desenvolvedor:**
    > Predominância de **Frontend Engineers e Documentação**, com
    > suporte de **JavaScript Developers** e **especialistas em
    > acessibilidade**.

### **Análise da Release v5.2.0-beta1 (Pré-release)**

**Data de lançamento:** 13 de maio de 2022\
**Resumo das principais mudanças:\
** A versão **5.2.0-beta1** introduziu **grandes refatorações e
aprimoramentos na estrutura do Bootstrap**. Um dos principais destaques
foi a **reformulação do Scrollspy**, que agora utiliza **Intersection
Observer** para um desempenho mais eficiente. Além disso, o sistema de
abas foi atualizado para seguir as **práticas do ARIA 1.1**, garantindo
maior acessibilidade e compatibilidade. O suporte para **CSS variables
foi expandido** para diversos componentes, incluindo **navbar, buttons,
dropdowns, alerts e badges**, permitindo maior flexibilidade na
personalização. No JavaScript, várias melhorias foram aplicadas na
modularização do código, incluindo **refatoração do Carousel, Scrollbar
e Tooltip** para melhor organização e desempenho. Por fim, novos
utilitários foram adicionados, como **sticky bottom e suporte para
dropdowns centralizados**.

**Características Relevantes:**

-   **Áreas afetadas:** CSS, JavaScript, Acessibilidade, Desempenho.

-   **Perfis técnicos envolvidos:**

    -   **Frontend Engineers** (expansão das CSS variables e refinamento
        > visual dos componentes).

    -   **JavaScript Developers** (melhorias na modularização e
        > performance dos componentes interativos).

    -   **UX Designers e Acessibilidade** (ajustes para tornar os
        > componentes mais intuitivos e acessíveis).

    -   **Performance Engineers** (otimização do Scrollspy e refatoração
        > do código para eficiência).

-   **Contribuidores principais:** Equipe Bootstrap e comunidade
    > open-source.

-   **Padrões arquiteturais aplicados:** Modularização do CSS e
    > JavaScript, implementação de práticas acessíveis e otimização de
    > desempenho.

-   **Frequência de contribuição por tipo de desenvolvedor:**
    > Equilibrada entre **Frontend Engineers, JavaScript Developers e
    > especialistas em Acessibilidade**.

### **Análise da Release v4.6.1**

**Data de lançamento:** 28 de outubro de 2021\
**Resumo das principais mudanças:\
** A versão **4.6.1** trouxe **correções e otimizações de
compatibilidade** para o Bootstrap v4. Entre os destaques estão a
substituição da **divisão do Sass** por uma função personalizada
(divide()) para manter a compatibilidade com versões mais recentes do
Sass. Além disso, houve aprimoramentos em **formulários e validações**,
ajustes na **acessibilidade dos dropdowns e carrosséis**, além de
melhorias no **suporte ao Node.js** e nas dependências do projeto.
Pequenos refinamentos visuais foram aplicados, incluindo **ajustes na
exibição de ícones de feedback** e no comportamento de componentes como
**modais, input groups e navegação**.

**Características Relevantes:**

-   **Áreas afetadas:** CSS, JavaScript, Acessibilidade, Infraestrutura
    > DevOps.

-   **Perfis técnicos envolvidos:**

    -   **Frontend Engineers** (ajustes no Sass e refinamentos visuais).

    -   **JavaScript Developers** (melhorias na acessibilidade e
        > comportamento dos modais e dropdowns).

    -   **DevOps** (atualizações nas versões do Node.js e refinamento
        > das dependências do projeto).

    -   **Especialistas em Acessibilidade** (ajustes na navegação do
        > carrossel e aprimoramento de atributos ARIA).

-   **Contribuidores principais:** Equipe Bootstrap e membros ativos da
    > comunidade open-source.

-   **Padrões arquiteturais aplicados:** Refatoração de código para
    > compatibilidade futura, aprimoramento da acessibilidade e
    > correções de comportamento.

-   **Frequência de contribuição por tipo de desenvolvedor:**
    > Predominância de **Frontend Engineers e DevOps**, com
    > contribuições significativas de **especialistas em Acessibilidade
    > e JavaScript Developers**.

### **Análise da Release v5.1.2**

**Data de lançamento:** 5 de outubro de 2021\
**Resumo das principais mudanças:\
** A versão **5.1.2** focou em **correções de compatibilidade,
refinamentos visuais e melhorias na documentação**. Um dos destaques foi
a **correção temporária de um problema no postcss-values-parser**,
garantindo a compilação adequada do Sass no **create-react-app**. Além
disso, foram adicionados **tamanhos de border-radius para .form-selects
pequenos e grandes** e **ajustes no alinhamento de botões** em
containers flexíveis. No JavaScript, uma **correção na funcionalidade de
Collapse** restaurou o comportamento esperado ao alternar entre
elementos irmãos. A sanitização de URLs também foi aprimorada com a
adição do **protocolo sms ao SAFE_URL_PATTERN**. Por fim, a documentação
foi revisada para incluir melhorias na descrição de .img-fluid e a
adoção do **GitHub Issue Forms** para facilitar o gerenciamento de
relatórios de problemas.

**Características Relevantes:**

-   **Áreas afetadas:** CSS, JavaScript, Documentação, Infraestrutura
    > DevOps.

-   **Perfis técnicos envolvidos:**

    -   **Frontend Engineers** (ajustes na renderização de formulários e
        > botões).

    -   **JavaScript Developers** (correção no comportamento do
        > Collapse).

    -   **Especialistas em Segurança** (melhoria no sanitizador de
        > URLs).

    -   **Documentação** (revisão de guias e implementação de templates
        > para issues no GitHub).

-   **Contribuidores principais:** Equipe Bootstrap e colaboradores da
    > comunidade open-source.

-   **Padrões arquiteturais aplicados:** Modularização do CSS e
    > JavaScript, aprimoramento da experiência do usuário e refinamento
    > da documentação.

-   **Frequência de contribuição por tipo de desenvolvedor:**
    > Equilibrada entre **Frontend Engineers, JavaScript Developers e
    > especialistas em Segurança**.

### **Perfil Geral da Estratégia de Releases do Bootstrap**

#### **1. Organização e Hierarquia das Releases**

O Bootstrap adota uma estratégia de releases baseada em **versões
semânticas (Semantic Versioning - SemVer)**, onde:

-   **Mudanças de versão principal (major - X.0.0)** indicam alterações
    > que podem quebrar compatibilidade com versões anteriores (exemplo:
    > transição da v4 para a v5).

-   **Mudanças de versão secundária (minor - X.Y.0)** introduzem novos
    > recursos mantendo compatibilidade com versões anteriores.

-   **Correções de versão patch (patch - X.Y.Z)** focam em **correções
    > de bugs, melhorias de desempenho e ajustes de acessibilidade**.

Além disso, o projeto segue um ciclo de **releases alfa, beta e
estáveis**, onde:

-   **Versões alfa e beta** são disponibilizadas para testes e
    > refinamentos antes do lançamento estável.

-   **Versões estáveis** contêm melhorias refinadas, com documentação e
    > suporte mais amplo.

#### **2. Critérios para Disponibilização das Releases**

A disponibilização de uma nova versão segue critérios bem definidos:

-   **Correção de bugs críticos**: Atualizações rápidas (patches) são
    > feitas quando há falhas que impactam diretamente a usabilidade da
    > biblioteca.

-   **Melhorias progressivas**: As releases minor incluem refinamentos
    > na experiência do usuário, otimizações de código e introdução de
    > novos utilitários CSS/JS.

-   **Garantia de compatibilidade**: Alterações significativas são
    > testadas em diferentes ambientes e documentadas adequadamente
    > antes da liberação.

-   **Acessibilidade e conformidade com padrões**: Cada atualização
    > busca melhorias na acessibilidade (seguindo WCAG e ARIA) e
    > compatibilidade com navegadores.

#### **3. Perfis Técnicos dos Contribuidores**

Com base na análise das releases e no artigo **\"Mining the Technical
Roles of GitHub Users\"**, os perfis técnicos mais presentes nas
contribuições do Bootstrap incluem:

-   **Frontend Engineers:** Contribuem significativamente para melhorias
    > no CSS, variáveis Sass, e estilização de componentes.

-   **JavaScript Developers:** Focam na correção de bugs e aprimoramento
    > da lógica interativa dos componentes.

-   **UX Designers e Especialistas em Acessibilidade:** Trabalham na
    > melhoria da experiência do usuário e acessibilidade dos
    > componentes.

-   **DevOps e Infraestrutura:** Responsáveis por otimizações no
    > pipeline CI/CD, testes automatizados e compatibilidade com
    > diferentes versões do Node.js.

#### **4. Padrões Identificados nas Releases**

A partir da análise das últimas 10 releases, identificamos alguns
padrões:

-   **Foco contínuo na modularização do CSS e JavaScript**: Uso
    > crescente de variáveis CSS para facilitar personalização e
    > manutenção.

-   **Aprimoramento constante da acessibilidade**: Melhorias em cores,
    > contraste, navegação por teclado e atributos ARIA.

-   **Expansão do suporte para diferentes frameworks e ferramentas**:
    > Atualizações compatíveis com Webpack, Vite, Parcel e React.

-   **Refinamento da experiência do usuário**: Melhorias na interação
    > com botões, modais, navegação e componentes dinâmicos.

-   **Manutenção ativa da documentação**: Atualizações frequentes para
    > garantir que as novas funcionalidades sejam bem explicadas e
    > acessíveis para desenvolvedores.

### **Segunda etapa da atividade**

Esta seção complementa a análise das releases do projeto Bootstrap,
trazendo um estudo detalhado dos perfis técnicos dos desenvolvedores que
contribuem para cada versão. Para isso, foi implementado um **script de
extração e processamento de dados via API do GitHub**, que coleta
informações sobre os autores dos commits, as linguagens de programação
que utilizam e suas principais contribuições dentro do projeto.

A metodologia adotada foi inspirada no artigo *\"Mining the Technical
Roles of GitHub Users\"*, que propõe uma abordagem para identificar e
classificar desenvolvedores com base nos padrões de contribuição e nas
tecnologias utilizadas. Com essa análise, buscamos responder questões
como:

-   Quais são os perfis predominantes entre os desenvolvedores do
    > Bootstrap?

-   Como a expertise técnica está distribuída dentro da comunidade do
    > projeto?

-   Existe alguma correlação entre a natureza da release e os tipos de
    > profissionais envolvidos?

#### **Metodologia**

O script desenvolvido realiza as seguintes etapas para traçar o perfil
dos desenvolvedores:

1.  **Coleta de commits**: Obtém os commits de cada release selecionada
    > diretamente da API do GitHub.

2.  **Identificação de desenvolvedores**: Extrai os nomes e logins dos
    > autores dos commits.

3.  **Consulta de perfis no GitHub**: Para cada autor, acessa a API
    > pública do GitHub e coleta dados como:

    -   Repositórios públicos

    -   Seguidores

    -   Empresa associada

    -   Linguagens de programação mais utilizadas

4.  **Classificação técnica**: Cada desenvolvedor é categorizado de
    > acordo com as linguagens utilizadas, associando-as a diferentes
    > **áreas de especialização** (Frontend, Backend, Mobile, Data
    > Science, DevOps).

5.  **Armazenamento e processamento**: Todos os dados são organizados em
    > um DataFrame do **Pandas**, processados e exportados para um
    > **arquivo CSV consolidado**.

#### **Funcionamento do Script**

O script desenvolvido automatiza o processo de extração de informações e
a classificação dos desenvolvedores. Ele opera da seguinte forma:

-   O usuário insere uma ou mais releases do Bootstrap.

-   O script acessa a API do GitHub para **coletar os commits** dessas
    > releases e identificar os respectivos desenvolvedores.

-   Para cada desenvolvedor encontrado, são extraídas **informações de
    > perfil**, incluindo as linguagens mais utilizadas e suas
    > contribuições anteriores.

-   Com base nas linguagens de programação, o script classifica o
    > desenvolvedor em categorias técnicas predefinidas, como
    > **Frontend, Backend, DevOps, Mobile ou Data Science**.

-   **Caso o desenvolvedor tenha participado de múltiplas releases**,
    > suas contribuições são **agregadas em um único registro**,
    > evitando duplicações e garantindo uma análise mais precisa.

-   O resultado final é salvo em um arquivo **CSV estruturado**, que
    > pode ser utilizado para gerar insights sobre a distribuição dos
    > perfis técnicos dentro do projeto Bootstrap.
    
### **Script utilizado em python:**

```python
"""
ANÁLISE DE DESENVOLVEDORES GITHUB POR RELEASE
Script que analisa contribuidores de releases específicas, classificando seus perfis técnicos
baseados nas linguagens de programação que utilizam.
"""

import requests
import pandas as pd
import time

# 🔑 CONFIGURAÇÕES DA API DO GITHUB
GITHUB_TOKEN = "insira_o_seu_token_aqui"  # Token de acesso pessoal do GitHub
REPO = "twbs/bootstrap"  # Repositório a ser analisado (formato: 'dono/repo')
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}  # Cabeçalho para autenticação

# 🗂 MAPEAMENTO DE LINGUAGENS PARA PERFIS TÉCNICOS
ROLE_MAPPING = {
    # Frontend
    "JavaScript": "Frontend",
    "TypeScript": "Frontend",
    "CSS": "Frontend",
    "HTML": "Frontend",
    # Backend
    "Python": "Backend",
    "Java": "Backend",
    # Data Science
    "Jupyter Notebook": "Data Science",
    # Mobile
    "Swift": "Mobile",
    # DevOps
    "Shell": "DevOps",
    # ... (outras linguagens podem ser adicionadas)
}

# 📦 VARIÁVEIS GLOBAIS PARA ARMAZENAMENTO
processed_developers = {}  # Cache de desenvolvedores processados
processed_authors = set()  # Autores já identificados

def get_commits_by_release(release_tag):
    """
    📌 Obtém todos os commits associados a uma release específica
    Args:
        release_tag (str): Tag da release (ex: 'v5.3.3')
    Returns:
        list: Lista de dicionários com informações dos commits
    """
    url = f"https://api.github.com/repos/{REPO}/commits"
    params = {"sha": release_tag, "per_page": 100}  # Paginação para limitar resultados
    
    response = requests.get(url, headers=HEADERS, params=params)

    # Tratamento de erros
    if response.status_code == 401:
        print("❌ Erro: Token inválido! Verifique suas credenciais do GitHub.")
        exit(1)
    if response.status_code != 200:
        print(f"❌ Erro ao obter commits para {release_tag}: {response.json()}")
        return []

    # Processa os commits
    return [{
        "author": commit["author"]["login"] if commit.get("author") else commit["commit"]["author"]["name"],
        "commit_message": commit["commit"]["message"],
        "release": release_tag
    } for commit in response.json()]

def get_developer_info(username):
    """
    👤 Obtém informações detalhadas de um desenvolvedor
    Args:
        username (str): Login/nome do desenvolvedor
    Returns:
        dict: Dicionário com perfil completo ou None se erro
    """
    # Verifica cache primeiro
    if username in processed_developers:
        return processed_developers[username]

    # Requisição à API do GitHub
    response = requests.get(f"https://api.github.com/users/{username}", headers=HEADERS)

    # Tratamento de erros
    if response.status_code == 404:
        print(f"⚠️ Usuário {username} não encontrado.")
        return None
    if response.status_code != 200:
        print(f"❌ Erro ao obter usuário {username}")
        return None

    # Processa dados do desenvolvedor
    user_data = response.json()
    languages = get_developer_languages(username)
    
    dev_info = {
        "login": user_data.get("login"),
        "name": user_data.get("name"),
        "bio": user_data.get("bio"),
        "company": user_data.get("company"),
        "public_repos": user_data.get("public_repos"),
        "followers": user_data.get("followers"),
        "languages": languages,
        "perfil_tecnico": classify_developer(languages),
        "commit_messages": [],
        "releases": set()
    }

    # Armazena em cache
    processed_developers[username] = dev_info
    return dev_info

def get_developer_languages(username):
    """
    💻 Identifica as linguagens mais utilizadas por um desenvolvedor
    Args:
        username (str): Login do desenvolvedor
    Returns:
        list: Tuplas (linguagem, contagem) ordenadas por uso
    """
    response = requests.get(
        f"https://api.github.com/users/{username}/repos",
        headers=HEADERS,
        params={"per_page": 100}  # Limite máximo por página
    )

    if response.status_code != 200:
        return []

    # Contagem de linguagens nos repositórios
    lang_count = {}
    for repo in response.json():
        if lang := repo.get("language"):
            lang_count[lang] = lang_count.get(lang, 0) + 1

    return sorted(lang_count.items(), key=lambda x: x[1], reverse=True)

def classify_developer(languages):
    """
    🏷 Classifica o perfil técnico baseado nas linguagens
    Args:
        languages (list): Lista de tuplas (linguagem, contagem)
    Returns:
        str: Perfil(s) técnico(s) concatenados
    """
    roles = {ROLE_MAPPING[lang] for lang, _ in languages if lang in ROLE_MAPPING}
    return ", ".join(roles) if roles else "Sem Classificação"

def analyze_releases(release_tags):
    """
    🚀 Função principal que coordena a análise
    Args:
        release_tags (list): Lista de tags de release para análise
    """
    print("🚀 Iniciando análise de releases...")
    all_commits = []

    # Coleta commits de todas as releases
    for release_tag in release_tags:
        print(f"🔎 Analisando release: {release_tag}...")
        commits = get_commits_by_release(release_tag)
        all_commits.extend(commits)
        time.sleep(1)  # Respeita rate limit da API

    # Processa cada commit
    for commit in all_commits:
        if dev_info := get_developer_info(commit["author"]):
            dev_info["commit_messages"].append(commit["commit_message"])
            dev_info["releases"].add(commit["release"])

    # Prepara dados para exportação
    for dev in processed_developers.values():
        dev["releases"] = ", ".join(sorted(dev["releases"]))
        dev["commit_messages"] = "; ".join(dev["commit_messages"])
        dev["languages"] = ", ".join([f"{lang} ({count})" for lang, count in dev["languages"]])

    # Gera relatório
    df = pd.DataFrame(processed_developers.values())
    
    if not df.empty:
        file_path = "developer_analysis.csv"
        df.to_csv(file_path, index=False)
        print(f"\n✅ Análise concluída! Resultados salvos em {file_path}")
        print("📊 Amostra dos dados:\n", df.head())
    else:
        print("❌ Nenhum dado foi coletado")

# Ponto de entrada do script
if __name__ == "__main__":
    print("""
    📌 GitHub Developer Analyzer
    --------------------------
    Analisa contribuidores de releases específicas,
    classificando seus perfis técnicos.
    """)
    
    # Exemplo: v5.3.3, v5.2.0
    release_input = input("Digite as releases separadas por vírgula: ")
    analyze_releases([r.strip() for r in release_input.split(",")])
```

### **Segunda etapa da atividade - Resultados e conclusões com base na análise de algumas releases**

![image](https://github.com/user-attachments/assets/c6bc7367-4f8c-4e2c-a21e-18461528a1bc)

### **Resultados da Análise**

Abaixo, apresentamos algumas conclusões extraídas da análise das cinco
releases:

#### **1. Perfis Técnicos Dominantes**

-   O perfil **Frontend** foi o mais recorrente entre os
    > desenvolvedores, refletindo a natureza do Bootstrap como um
    > framework de interface visual.

-   Desenvolvedores **Full-Stack**, que possuem experiência em
    > **Frontend e Backend**, também marcaram presença significativa.

-   **Data Science e DevOps** tiveram menor participação, indicando que
    > o foco do projeto continua sendo interfaces web.

#### **2. Desenvolvedores Mais Ativos**

-   **Julien Déramond**: Participou de **seis releases**, sendo um dos
    > principais contribuidores. Seu perfil técnico abrange **Mobile e
    > Frontend**, com forte experiência em **TypeScript e JavaScript**.

-   **GeoSot**: Contribuiu para quatro releases, com expertise em
    > **Frontend e Backend**. Suas principais linguagens são **PHP,
    > JavaScript e Python**.

-   **Robert Martin (bertday)**: Participou da release v5.3.3, com um
    > perfil técnico abrangente em **Mobile, Frontend e Backend**.

-   **DrejT**: Envolvido em múltiplas releases, com destaque para **Data
    > Science, Frontend e Backend**, mostrando um perfil mais híbrido.

#### **3. Distribuição de Contribuições**

-   Alguns desenvolvedores, como **dependabot\[bot\]**, participaram de
    > múltiplas releases, mas suas contribuições foram relacionadas à
    > manutenção automática de dependências.

-   A maior parte dos contribuidores focou em **correções de bugs e
    > melhorias na documentação**, refletindo uma preocupação contínua
    > com a usabilidade do framework.

#### **4. Papel dos Commits nas Releases**

-   Os commit messages analisados mostraram que muitos desenvolvedores
    > estavam envolvidos em **melhorias de documentação**, ajustes de
    > **CSS/JavaScript** e **refinamento de funcionalidades**.

-   Correções críticas, como o ajuste no **Selector Engine**, foram
    > feitas por especialistas que já participaram de várias releases.

### **Conclusão**

A análise realizada demonstrou que o desenvolvimento do Bootstrap segue
uma estrutura bem organizada, onde desenvolvedores de Frontend e
Full-Stack são predominantes. Os padrões identificados podem auxiliar na
**previsão de contribuições futuras**, na **distribuição de tarefas** e
até mesmo no **recrutamento de novos colaboradores** para o projeto.

O uso de mineração de repositórios, como demonstrado neste estudo, é
essencial para compreender como as contribuições são distribuídas ao
longo do tempo e como os perfis técnicos impactam a evolução do projeto.
