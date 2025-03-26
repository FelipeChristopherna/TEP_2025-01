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

**Lía:** Olá! Fico feliz em ajudar! 😊 Se você gosta de ficção científica envolvente, recomendo *Duna*, de Frank Herbert. É um clássico cheio de aventura, política e mistério. Ou, se preferir algo mais recente, *A Longa Viagem a um Pequeno Planeta Hostil*, de Becky Chambers, traz uma visão mais acolhedora e reflexiva do espaço. Algum desses te interessa?  

Se quiser que eu refine mais alguma característica, é só falar! 📚✨"

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