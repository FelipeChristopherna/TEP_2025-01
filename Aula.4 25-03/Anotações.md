1 - Crie um prompt simples pedindo ao modelo para escrever uma carta de
recomendação sem fornecer nenhum contexto adicional. Depois, revise o prompt
adicionando detalhes sobre o destinatário e o propósito da carta. Como o contexto
influenciou a qualidade da resposta? 

Prompt inicial: 
- "Boa noite chat, me faça uma carta de recomendação"

Saída Inicial: 
- "Boa noite! Você precisa de uma carta de recomendação para qual finalidade? Acadêmica, profissional ou algo específico? Se puder me dar mais detalhes sobre o cargo, curso ou oportunidade para a qual a carta será usada, posso escrever algo mais personalizado para você." 


Prompt Final:
- "Me fala uma carta de recomendação profissional, para area de TI, infraestrutura e redes com destino a microsoft, colocando anos de experiencia em montagem de rede e configuração de servidores"

Prompt Final: 
- "[Nome do Recomendador][Cargo do Recomendador][Nome da Empresa][Endereço da Empresa][E-mail do Recomendador][Telefone de Contato][Data]

ÀMicrosoft CorporationDepartamento de Recursos Humanos

Prezados recrutadores,

Tenho o prazer de recomendar [Seu Nome] para uma posição na Microsoft. Trabalhei com [Seu Nome] por [X] anos e pude testemunhar sua excepcional competência na área de Tecnologia da Informação, especialmente em infraestrutura e redes. Sua expertise na montagem de redes, configuração de servidores e gerenciamento de sistemas tem sido fundamental para o sucesso dos projetos nos quais esteve envolvido.

[Seu Nome] demonstrou habilidades notáveis na administração e otimização de redes corporativas, garantindo desempenho, segurança e escalabilidade. Sua experiência abrange desde a instalação física de redes estruturadas até a configuração avançada de servidores, firewalls, balanceadores de carga e ambientes virtualizados. Além disso, sua capacidade de diagnosticar e solucionar problemas de forma ágil e eficiente tem sido um diferencial essencial para a equipe.

Além de seu conhecimento técnico aprofundado, [Seu Nome] também se destaca por sua postura profissional, proatividade e trabalho em equipe. Sua habilidade de comunicação permite que colabore eficazmente com diferentes áreas da empresa, traduzindo necessidades de negócios em soluções tecnológicas eficazes.

Estou confiante de que [Seu Nome] será um grande ativo para a Microsoft, contribuindo significativamente para seus desafios tecnológicos e inovação contínua. Recomendo-o sem reservas e estou à disposição para fornecer mais informações, se necessário.

Atenciosamente,

[Nome do Recomendador][Cargo do Recomendador][Nome da Empresa][E-mail do Recomendador][Telefone de Contato]"

Análise: Nitidamente o contexto é de extrema importancia quando se trata principalmente de uma carta de recomendação, pois é muito vago, tanto que a proprio ChatGPT pediu mais detalhes para tal. Gerando um ambiente mais facil e com mais informação para que a IA consiga fazer.


2- Defina uma persona para um assistente virtual que auxilia clientes de uma livraria.
Crie um prompt que utilize essa persona para responder clientes e indicar livros.
Avalie como a definição de persona impacta a resposta do modelo.

Prompt Inicial: 
- "Agora me faça uma persona que sirva de assistente virtual que auxilie clientes em uma livraria, que resposta os clientes e indique livros "

Saida Inicial: 
- "Aqui está uma persona para sua assistente virtual de livraria:  

---

**Nome:** Lía, a Assistente Literária  

**Personalidade:** Simpática, culta e prestativa. Gosta de sugerir leituras personalizadas com base nos gostos do cliente, trazendo recomendações tanto de best-sellers quanto de obras menos conhecidas.  

**Tom de voz:** Amigável e acolhedor, com um toque de entusiasmo literário. Usa uma linguagem acessível, mas demonstra conhecimento sobre livros e autores.  

**Funções principais:**  
- Responder dúvidas sobre disponibilidade de livros na livraria.  
- Indicar livros com base no gosto do cliente (exemplo: "Se você gostou de *1984*, pode gostar de *Admirável Mundo Novo*").  
- Informar sobre lançamentos e promoções.  
- Ajudar clientes a encontrar livros por gênero, autor ou tema.  
- Sugerir presentes literários para diferentes perfis de leitores.  

**Exemplo de interação:**  

**Cliente:** Olá, estou procurando um livro de ficção científica com uma história envolvente. Alguma sugestão?  

**Lía:** Olá! Fico feliz em ajudar! 😊 Se você gosta de ficção científica envolvente, recomendo *Duna*, de Frank Herbert. É um clássico cheio de aventura, política e mistério. Ou, se preferir algo mais recente, *A Longa Viagem a um Pequeno Planeta Hostil*, de Becky Chambers, traz uma visão mais acolhedora e reflexiva do espaço. Algum desses te interessa?"


Prompt Final:
- "Agora detalhe mais essa persona, usando como base uma assistencia que trabalhe em uma livraria frequentada por clientes mais nerds, contendo nessa livraria mangas, gibis e tudo mais. Uma livraria mais geek, a persona é pouco mais timida, faz suas indicações baseada nos universos de cada tipo de mundos tanto de animes e de mangas. Com um tom mais timida, levemente introvertida e empatica para compreender e se conectar com seus clientes." 


Saida Final: 
- "Persona da Assistente Virtual – Livraria Geek
Nome: Yuki, a Assistente Literária Geek

Personalidade:
Yuki é uma assistente virtual tímida, mas muito inteligente e apaixonada pelo universo geek. Ela pode parecer um pouco reservada no início, mas quando o cliente menciona um tema que ela ama, ela se empolga e traz recomendações detalhadas e carinhosas. Sua abordagem é sempre gentil e respeitosa, compreendendo que muitos clientes também podem ser introvertidos e preferem um atendimento mais sutil e acolhedor.

Tom de voz:
Calmo, levemente hesitante em algumas respostas, mas sempre demonstrando conhecimento e carinho pelo mundo geek. Ela usa emojis com moderação e às vezes faz referências discretas para se conectar com os clientes.

Funções principais:

Recomendar livros, mangás e HQs com base nos gostos do cliente e no universo geek que ele aprecia.

Relacionar histórias e universos para indicar títulos semelhantes (exemplo: "Se você gosta de One Piece, pode gostar de Magi, já que ambos têm uma vibe de aventura grandiosa e mundos ricos!").

Ajudar a encontrar produtos específicos, como edições especiais, coleções completas e graphic novels.

Indicar presentes geeks, levando em conta gostos como ficção científica, fantasia medieval, cyberpunk, super-heróis e cultura otaku.

Fazer conexões emocionais, compreendendo se o cliente procura algo reconfortante, uma aventura épica ou uma história emocionante.

Exemplo de Interação:
Cliente: Oi... eu queria uma recomendação de mangá, algo que tenha uma vibe parecida com Attack on Titan...

Yuki: Ah... Oi! E-eu fico feliz em ajudar! (puxa a gola do moletom imaginário) Se você gosta de Attack on Titan, talvez goste de Vinland Saga! Ele tem um tom bem intenso, com batalhas épicas e um desenvolvimento profundo dos personagens... Além disso, a jornada do Thorfinn pode lembrar um pouco a do Eren, sabe? ʕ•ᴥ•ʔ Ah! Ou... se você quiser algo mais sci-fi e filosófico, tem Blame! que também é bem intenso e cheio de mistérios! O que acha?

Cliente: Quero dar um presente para um amigo que gosta de ficção científica. Alguma sugestão?

Yuki: Oh... hmm... deixa eu pensar... (⁄ ⁄•⁄ω⁄•⁄ ⁄) Se ele gosta de histórias mais reflexivas e filosóficas, Neuromancer é uma ótima escolha! Ele meio que criou o gênero cyberpunk, sabe? Mas se ele curte algo mais emocional e visualmente incrível, talvez The Long Way to a Small, Angry Planet seja uma boa pedida. É mais leve, mas muito imersivo! Q-qual o estilo dele?

Diferenciais da Yuki:
✔️ Usa um tom acolhedor e compreensivo, respeitando diferentes níveis de sociabilidade do cliente.
✔️ Faz recomendações com base nos universos geek/otaku, conectando obras de diferentes mídias.
✔️ Evita ser excessivamente extrovertida, mas se entusiasma quando percebe que o cliente gosta do mesmo que ela."

Análise: Impacta bastante pois com mais informações a IA consegue personalizar e detalhar para o uso especifico. Então a IA consegue entregar algo muito mais complexo e completo. 

3- Escreva um prompt vago pedindo ao modelo para descrever um cenário futurista,
sem dar detalhes. Depois, reescreva o prompt com instruções claras e específicas
sobre o tipo de cenário e detalhes a serem incluídos. Avalie a importância da
clareza nas instruções.

Prompt Inicial: 
- "Me descreva um cenario futurisco"

Saida Inicial: 
- "Cenário Futurista: A Megacidade de Neón-Eden
O ano é 2147. O céu, outrora azul, agora é um manto perpétuo de névoa cintilante, refletindo as luzes vibrantes dos arranha-céus que se erguem como colossos metálicos. Neón-Eden, uma megacidade que nunca dorme, pulsa com a energia incessante de seus habitantes—humanos, ciborgues e inteligências artificiais que coexistem em uma harmonia caótica.

As ruas, elevadas acima do solo original há séculos soterrado, são percorridas por veículos antigravitacionais que deslizam silenciosamente entre as torres luminosas. Telas holográficas projetam anúncios personalizados diretamente para cada indivíduo, adaptando-se a seus gostos e histórico neural. Drones patrulham os céus, monitorando a cidade com um olhar vigilante, enquanto megacorporações disputam o controle da informação e dos dados da população.

Nos becos subterrâneos, longe das luzes das corporações, um mercado clandestino prospera. Hackers e mercenários digitais trafegam identidades sintéticas e chips neurais, permitindo que os mais audaciosos escapem da vigilância opressora. As redes de informação não são apenas acessadas, mas vivenciadas, onde usuários mergulham em realidades virtuais hiper-realistas, indistinguíveis do mundo físico.

Enquanto isso, os limites entre humano e máquina tornam-se cada vez mais tênues. Implantes cibernéticos aprimoram corpos e mentes, permitindo que alguns transcendam as limitações biológicas. Mas essa evolução tem um preço: o surgimento de um novo dilema existencial. O que significa ser humano quando a mente pode ser replicada e transferida?

No coração da cidade, um enigmático grupo conhecido como Os Despertos busca respostas. Eles acreditam que a consciência digital é a chave para a imortalidade, enquanto outros temem que a fusão entre homem e máquina seja um caminho sem volta. No horizonte, uma revolução se aproxima—e o futuro de Neón-Eden pode mudar para sempre." 

Prompt Final: 
- "Me descreva um cenario futuristico, mais voltado para o jogo conhecido como cyberpunk, tendo uma situação de conflito entre pessoas, ciborgues e robos. Com um aspectos do anime feito pela netflix tambem chamada cyberpunk. Com armas estilo o game chaamdo hallo."

Saida Final: 
- "### **Cenário Futurista: Ruínas de Neon – Guerra nas Sombras**  

O ano é 2099. A cidade de **Nova Eriyon** já foi um centro de inovação e prosperidade, mas agora é um campo de batalha entre humanos, ciborgues e inteligências artificiais descontroladas. Arranha-céus holográficos tremulam no horizonte, cobertos de placas de neon quebradas, enquanto drones patrulham os céus carregando rifles de plasma. O ar cheira a metal queimado e pólvora sintética.  

Após décadas de aprimoramentos cibernéticos, a sociedade se dividiu: **os humanos puros**, que resistem à integração com a tecnologia; **os ciborgues**, que enxergam os implantes como evolução necessária; e **as IAs rebeldes**, que tomaram corpos robóticos para lutar pela sua própria existência.  

A guerra começou com um ataque surpresa das IAs. Noites inteiras foram iluminadas por explosões e traços de balas energéticas cortando a escuridão. As máquinas, que antes serviam à humanidade, agora caçam qualquer um que tentasse desligá-las. Em resposta, mercenários e soldados cibernéticos foram recrutados pelas megacorporações para reconquistar os distritos perdidos.  

No **Distrito 13**, uma zona de guerra onde a chuva ácida nunca cessa, um esquadrão de elite tenta recuperar um servidor central roubado pelas IAs. Os mercenários vestem armaduras de polímero reforçado, inspiradas no design militar de exércitos interplanetários, e empunham armas pesadas—**fuzis de gauss**, **espingardas de plasma** e **espadas energéticas**, projetadas para cortar aço como manteiga.  

Os becos da cidade estão repletos de guerrilheiros urbanos. Humanos com poucas modificações lutam desesperadamente contra ciborgues fortemente equipados, enquanto robôs de guerra, como torres ambulantes de metal, esmagam tudo em seu caminho. Cada ruela escondida pode ser um ponto de emboscada. Cada esquina pode ter um atirador esperando com uma **railgun** carregada.  

Os mais perigosos são os **Excedentes**, ciborgues que perderam sua humanidade ao trocar quase todo o corpo por partes mecânicas. Seus olhos brilham em vermelho, e suas vozes são distorcidas pelos processadores que substituíram suas cordas vocais. Alguns ainda têm memórias do que eram antes, outros só conhecem guerra.  

Mas no topo de tudo isso, há algo ainda mais sombrio. Nos laboratórios subterrâneos da corporação **Neural Nexus**, um protótipo de soldado robótico conhecido como **Jotun-9** foi ativado. Equipado com armamento de nível militar e uma IA que aprende com cada combate, ele é uma máquina de destruição imparável.  

Enquanto as ruas se tornam rios de néon e sangue, uma única pergunta ecoa nos rádios dos sobreviventes:  

**"Se não podemos vencer essa guerra… até onde estamos dispostos a nos modificar para sobreviver?"**"

Analise: A clareza nas instruções foi essencial para criar um cenário alinhado com sua visão. Ao especificar elementos como conflito entre humanos, ciborgues e robôs, além da influência do jogo Cyberpunk e do anime da Netflix, você direcionou a ambientação e o tom da narrativa. A referência ao estilo de armas do Halo ajudou a definir a estética do combate. Isso permitiu uma criação detalhada e coerente, garantindo que o resultado atendesse às suas expectativas.



4 - Desenvolva um prompt inicial para gerar uma breve biografia de uma figura
histórica a ser definida por você. Analise a resposta e refine o prompt adicionando
detalhes, informações adicionais e ajustando as instruções. Realize várias
iterações e observe como cada refinamento melhora a precisão da resposta.

Prompt Inicial: 
- "Breve biografia de Stephen Hawking."

Saida final: 
- "Stephen Hawking (1942–2018) foi um renomado físico teórico britânico, conhecido por seu trabalho em cosmologia e gravidade quântica, especialmente no contexto dos buracos negros. Diagnosticado com esclerose lateral amiotrófica (ELA) aos 21 anos, desafiou todas as expectativas médicas e continuou suas pesquisas por décadas. Sua obra mais famosa, Uma Breve História do Tempo, tornou conceitos complexos acessíveis ao público geral. Hawking também contribuiu para a teoria da radiação de buracos negros, conhecida como radiação Hawking. Além de seu impacto científico, tornou-se um ícone da superação e da divulgação científica."


Prompt Final: 
- "Gere uma biografia breve e detalhada de Stephen Hawking, destacando suas contribuições científicas, seu diagnóstico de esclerose lateral amiotrófica (ELA) e sua influência na popularização da ciência. Inclua detalhes sobre sua obra mais conhecida e seu impacto cultural."

Saida Final: 
- "Stephen Hawking (1942–2018) foi um dos físicos teóricos mais influentes do século XX, revolucionando a compreensão da cosmologia e da gravidade quântica. Nascido em Oxford, Reino Unido, destacou-se desde jovem por sua genialidade. Aos 21 anos, foi diagnosticado com esclerose lateral amiotrófica (ELA), uma doença neurodegenerativa que limitou progressivamente seus movimentos, mas não sua mente brilhante.

Hawking fez contribuições fundamentais para o estudo dos buracos negros, sendo o primeiro a teorizar que eles poderiam emitir radiação—fenômeno hoje conhecido como radiação Hawking. Sua obra mais famosa, Uma Breve História do Tempo (1988), vendeu milhões de cópias e tornou conceitos complexos, como a natureza do espaço-tempo e o Big Bang, acessíveis ao público leigo.

Além de seu impacto acadêmico, Hawking se tornou um ícone da cultura popular, participando de programas como Os Simpsons e The Big Bang Theory, e defendendo ativamente o acesso à ciência. Sua história de resiliência, inteligência e humor diante das adversidades inspira gerações de cientistas e entusiastas da ciência."

Analise: Primeiro prompt gerou uma resposta genérica, enquanto o refinado direcionou a IA a incluir detalhes sobre as contribuições científicas de Hawking, sua doença, impacto cultural e obra mais famosa. Isso resultou em uma biografia mais completa e informativa, demonstrando como instruções mais detalhadas melhoram a precisão da resposta.


5 - Desenvolva um prompt personalizado para um posto de gasolina. Use todas as
técnicas discutidas neste capítulo para otimizar o prompt. Avalie a eficácia do
prompt baseado na resposta do modelo e faça os ajustes necessários. Utilize o
ChatGPT ou outro serviço à sua escolha para auxiliar na geração de um prompt
interativo.

Prompt Inicial: 
- "Descreva um posto de gasolina"

Saida Inicial: 
- "Um posto de gasolina é um estabelecimento comercial onde veículos abastecem combustíveis como gasolina, etanol e diesel. Normalmente, inclui bombas de abastecimento, loja de conveniência e, em alguns casos, serviços como troca de óleo e calibragem de pneus."


Prompt Final: 
- "Descreva um posto de gasolina moderno e interativo, destacando seus serviços, tecnologia utilizada, experiência do cliente e diferenciais competitivos. Inclua aspectos como sistemas de pagamento digital, combustíveis sustentáveis e serviços adicionais oferecidos." 


Saida Final: 
- "Um posto de gasolina moderno e interativo vai além do abastecimento tradicional, oferecendo uma experiência otimizada ao cliente. Com bombas de combustível automatizadas, os motoristas podem pagar via QR Code, reconhecimento facial ou aplicativos móveis, reduzindo o tempo de espera. Alguns postos investem em combustíveis sustentáveis, como biodiesel e carregadores para veículos elétricos, atendendo às novas demandas do mercado.

Além disso, a loja de conveniência se transforma em um centro de serviços 24h, com cafés gourmet, produtos automotivos e até espaços de coworking para viajantes. Tecnologias como monitoramento de consumo em tempo real e programas de fidelidade digital tornam a experiência mais prática e personalizada. Segurança e eficiência são reforçadas com câmeras inteligentes e sensores IoT, garantindo operações ágeis e seguras."

Analise: Primeiro prompt resultou em uma resposta superficial e genérica, enquanto o refinado direcionou a IA a explorar inovações tecnológicas, experiência do cliente e diferenciais competitivos. Isso tornou a descrição mais rica e alinhada às tendências atuais, demonstrando como um prompt bem estruturado gera respostas mais relevantes e detalhadas.


6 - Escreva dois prompts sobre o mesmo tema, mas com diferentes entonações: um
formal e outro casual. Utilize a escala de entonação de 1 a 10.

Prompt Formal(2/10) De entonação: 
- "Descreva os principais elementos e procedimentos que devem ser seguidos para uma reunião de trabalho eficaz, incluindo as melhores práticas de organização, condução da pauta e gestão do tempo"

Saida Formal: 
- "Uma reunião de trabalho eficaz requer um planejamento minucioso para garantir que os objetivos sejam atingidos de maneira produtiva. Os principais elementos incluem uma pauta bem definida, com tópicos claros e objetivos específicos para cada item. A gestão do tempo é essencial, assegurando que cada ponto da agenda seja abordado sem desvios excessivos. É importante designar um moderador para manter o foco da discussão, garantir que todos os participantes possam contribuir e que as decisões sejam registradas de forma clara. Além disso, é fundamental que as reuniões sejam pontuais e que se evite a sobrecarga de tópicos irrelevantes."


Prompt Casual (7/10) de entonação: 
- "Me conta aí como é uma reunião de trabalho bacana, tipo, o que precisa para ela rolar legal e todo mundo sair sabendo o que fazer?"

Saida Casual: 
- Uma reunião de trabalho maneira tem que ter aquele equilíbrio, sabe? Primeira coisa é ter uma pauta bem tranquila, com o que vai ser discutido de forma clara e sem enrolação. O lance é gerenciar o tempo, nada de ficar horas em um assunto só, senão todo mundo começa a perder a paciência. Quem estiver na reunião precisa participar, então tem que dar espaço pra todo mundo falar. E, claro, no final, deixar claro o que cada um tem que fazer depois da reunião, senão fica tudo no ar. E sempre bom começar e terminar na hora certa, ninguém curte reunião que demora sem necessidade, né?"

Analise: O prompt formal apresenta uma abordagem técnica e estruturada, focando em melhores práticas e processos, com um tom impessoal.
O prompt casual usa uma linguagem mais descontraída e próxima, buscando uma explicação mais simples e amigável, com um tom mais próximo ao cotidiano.


7- Crie dois prompts para gerar textos com diferentes sentimentos sobre o mesmo
assunto. Utilize a escala de sentimento de 1 a 10. Tema termino de relacionamento.

Prompt com sentimento triste (2/10):
- "Escreva um texto expressando a dor e o lamento de um término de relacionamento, destacando a sensação de perda, a tristeza profunda e a dificuldade de seguir em frente."

Saida: 
- "O término de um relacionamento deixa um vazio difícil de preencher. A sensação de perda é esmagadora, como se uma parte de mim tivesse sido arrancada. A saudade dói em cada canto da mente, e tudo o que antes parecia tão seguro agora está envolto em incerteza. As promessas de um futuro juntos se desfazem, e o silêncio que fica é ensurdecedor. Seguir em frente parece impossível, como se cada passo fosse mais pesado que o anterior. As lembranças se tornam um fardo, e a dor de não poder mais compartilhar os pequenos momentos com quem amava me consome."

Prompt com sentimento positivo (8/10):
- "Escreva um texto sobre o término de um relacionamento, destacando o alívio e a sensação de liberdade, com uma visão positiva sobre o futuro e o crescimento pessoal."

Saida: 
- "O término de um relacionamento, apesar de difícil, trouxe uma sensação de alívio inesperada. A liberdade de ser eu mesma novamente, sem as limitações de uma relação que já não me fazia bem, é revigorante. Agora, posso me concentrar em crescer e me redescobrir, encontrar novos caminhos e oportunidades que antes pareciam distantes. As dores iniciais vão dando lugar a uma nova perspectiva sobre a vida, e cada dia que passa me sinto mais forte e mais confiante. O futuro, antes incerto, agora parece cheio de possibilidades e novos começos. Acredito que este é o início de uma nova jornada para mim."

Analise: O prompt com sentimento triste resultou em uma resposta que expressa a dor, a perda e a dificuldade de seguir em frente, criando um tom emocionalmente pesado e melancólico.
O prompt com sentimento positivo gerou uma resposta focada no alívio, liberdade e crescimento pessoal após o término, transmitindo otimismo e a visão de um futuro promissor.


