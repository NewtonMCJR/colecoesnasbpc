import os
import json

workspace_dir = r"c:\Users\museu\Documents\SBPC\Displays"

# Database of the 12 collections and their honored researchers
collections_data = {
    "CBPM": {
        "acronym": "CBPM",
        "collection_name": "Coleção de Biotecnologia de Plantas Medicinais",
        "category": "Botânica",
        "researcher_name": "Graziela Maciel Barroso",
        "period": "1946–2003",
        "area": "Botânica / Taxonomia e Sistemática",
        "quote": "Quando pego uma planta pra estudar é como se fosse um filho que eu visse crescer, ver a morfologia de uma flor, procurar o nome dela, saber como ele vive e cresce, o amor que sinto por aquilo é muito grande.",
        "bio": "Graziela Maciel Barroso (1912–2003) foi uma renomada botânica brasileira especialista em taxonomia vegetal. Primeira mulher a passar no concurso para naturalista do Jardim Botânico do Rio de Janeiro, teve também forte cooperação técnico-científica com instituições de pesquisa em saúde pública e meio ambiente, dedicando sua vida ao estudo da flora nacional.",
        "contribution": "Atuou de forma expressiva na curadoria e organização do Herbário do Jardim Botânico (RB). Liderou expedições científicas por diversos biomas, coletando espécimes e aprimorando técnicas de catalogação, conservação e preservação de exsicatas. Para a Fiocruz-CBPM, foi determinante na identificação de espécies medicinais de Asteraceae e Myrtaceae.",
        "importance": "Pioneira e exemplo de superação, ingressou na faculdade aos 47 anos, vencendo as barreiras de um cenário majoritariamente masculino. Consolidou a presença feminina na ciência e formou gerações de novos pesquisadores. Publicou 65 artigos científicos e escreveu livros fundamentais para ensino e pesquisa de sistemática de plantas. Uma de suas obras, 'Sistemática de Angiospermas do Brasil', tornou-se referência internacional. Os herbários para os quais identificou plantas ajudaram a mapear espécies ameaçadas de extinção e a preservar as áreas em que se encontravam.",
        "curiosity": "Foi a primeira mulher a ingressar na Academia Brasileira de Ciências na categoria de Ciências Biológicas e teve mais de 25 espécies batizadas em sua homenagem. Foi a única brasileira a receber a Medalha de Ouro Crane, concedida pelo Jardim Botânico de Chicago (EUA), um prêmio internacional voltado a grandes conservacionistas do mundo.",
        "message": "Para a ciência e para os nossos sonhos, nunca é tarde demais para florescer. Com a força de quem lança raízes profundas e a coragem de desbravar o desconhecido, cada mulher cientista deixa sua marca eterna na descoberta de um mundo novo.",
        "image_path": "../assets/images/CBPM_image2.png",
        "theme": {
            "bg_gradient": "from-emerald-600 to-teal-800",
            "accent_text": "text-emerald-600",
            "accent_bg": "bg-emerald-50",
            "accent_border": "border-emerald-500",
            "btn_bg": "bg-emerald-600 hover:bg-emerald-700",
            "shadow": "shadow-emerald-100",
            "focus_ring": "focus:ring-emerald-500"
        },
        "videos": []
    },
    "CCER": {
        "acronym": "CCER",
        "collection_name": "Coleção de Ceratopogonidae",
        "category": "Zoologia (Insetos)",
        "researcher_name": "Dra. Maria Luiza Felippe Bauer",
        "period": "1981–presente",
        "area": "Zoologia / Entomologia",
        "quote": "Em qualquer situação, o trabalho será sua salvaguarda.",
        "bio": "A Dra. Maria Luiza Felippe Bauer é bióloga, mestre e doutora em Zoologia, pesquisadora do Instituto Oswaldo Cruz (IOC/Fiocruz) e curadora da Coleção de Ceratopogonidae da Fiocruz. Ao longo de cerca de quatro décadas de atuação científica, dedicou-se à taxonomia, sistemática, biodiversidade e ecologia dos maruins.",
        "contribution": "Dra. Maria Luiza Felippe-Bauer iniciou a Coleção de Ceratopogonidae da Fiocruz (CCER), que sob sua curadoria foi ampliada e consolidada como referência científica. Seu trabalho garantiu a conservação, organização e disponibilização de espécimes do Brasil e de diversos países das Américas para pesquisas em biodiversidade e sistemática.",
        "importance": "Seu legado inclui uma expressiva produção científica, a formação de novos taxonomistas e colaborações com pesquisadores internacionais. Referência na taxonomia de maruins, tornou-se a principal especialista brasileira no grupo e uma das mais importantes da região Neotropical. Em reconhecimento às suas contribuições, duas espécies foram nomeadas em sua homenagem: Culicoides (Mataemyia) felippebauerae Spinelli e Forcipomyia (Microhelea) felippebauerae Clastrier & Wirth.",
        "curiosity": "Primeira e única curadora da Coleção de Ceratopogonidae da Fiocruz (CCER), Dra. Maria Luiza Felippe Bauer descreveu mais de 90 novos táxons, incluindo dois gêneros. Tornou-se referência em vigilância de vetores durante a expansão da Febre Oropouche nas Américas, contribuindo significativamente para o conhecimento da biodiversidade neotropical de maruins e para a valorização das coleções biológicas como patrimônio científico.",
        "message": "A ciência também é construída por mulheres que preservam, investigam e transformam o conhecimento.",
        "image_path": "../assets/images/CCER_image2.jpeg",
        "theme": {
            "bg_gradient": "from-indigo-600 to-purple-800",
            "accent_text": "text-indigo-600",
            "accent_bg": "bg-indigo-50",
            "accent_border": "border-indigo-500",
            "btn_bg": "bg-indigo-600 hover:bg-indigo-700",
            "shadow": "shadow-indigo-100",
            "focus_ring": "focus:ring-indigo-500"
        },
        "videos": []
    },
    "CCFF": {
        "acronym": "CCFF",
        "collection_name": "Coleção de Culturas de Fungos Filamentosos",
        "category": "Micologia (Fungos)",
        "researcher_name": "Pedrina Cunha de Oliveira",
        "period": "1960–1995",
        "area": "Micologia Médica e Genética de Fungos",
        "quote": "O que você faz, faz a diferença, e você precisa decidir que tipo de diferença quer fazer.",
        "bio": "Pedrina Cunha de Oliveira foi uma destacada micologista brasileira, formada em Farmácia pela Universidade do Brasil (atual UFRJ), com especialização em saúde pública. Ingressou no Instituto Oswaldo Cruz (IOC/Fiocruz) in 1960 como estagiária e, em 1962, realizou o tradicional Curso de Aplicação do IOC, onde consolidou sua formação prática em pesquisa e se especializou em micologia. Entre 1967 e 1969, realizou mestrado na Universidade de Sheffield, na Inglaterra, com foco em genética de fungos. Ao longo de toda a sua trajetória no IOC, atuou nas áreas de micologia médica e genética de fungos, tornando-se uma referência nacional pelo rigor científico e pela relevância de suas contribuições.",
        "contribution": "Atuou na Seção de Micologia e na Coleção de Fungos do IOC. Implantou a linha de pesquisa de genética de fungos (Aspergillus nidulans) e garantiu a continuidade da coleção biológica, evitando sua perda durante a crise institucional dos anos 1970. Entre 1970 e 1975, atuou como chefe e curadora eventual, mantendo praticamente sozinha as atividades científicas e o acervo, além de atuar na formação de alunos e técnicos.",
        "importance": "A trajetória de Pedrina Cunha de Oliveira revela resiliência e profundo compromisso com a ciência em um dos períodos mais difíceis da Fiocruz. Durante a ditadura militar, o 'Massacre de Manguinhos' desestruturou a instituição, impondo restrições e escassez de recursos. Nesse cenário, agravado pelas barreiras enfrentadas pelas mulheres na ciência, Pedrina afirmou sua competência e resistiu. Sua atuação discreta e decisiva garantiu a continuidade da área e formou pesquisadoras que continuaram seu legado.",
        "curiosity": "Ingressou no IOC in 1960 e construiu uma carreira de mais de 30 anos. Foi chefe do Departamento de Micologia a partir de 1978. Implantou um dos primeiros núcleos de genética de fungos do Brasil, e seu maior legado foi garantir que a micologia permanecesse activa, relevante e institucionalmente consolidada na Fiocruz.",
        "message": "O que você faz, faz a diferença, e você precisa decidir que tipo de diferença quer fazer. (Inspirado em Jane Goodall)",
        "image_path": "../assets/images/CCFF_image5.png",
        "theme": {
            "bg_gradient": "from-rose-600 to-pink-800",
            "accent_text": "text-rose-600",
            "accent_bg": "bg-rose-50",
            "accent_border": "border-rose-500",
            "btn_bg": "bg-rose-600 hover:bg-rose-700",
            "shadow": "shadow-rose-100",
            "focus_ring": "focus:ring-rose-500"
        },
        "videos": [
            {"title": "Entrevista de Pedrina Cunha de Oliveira (Base Arch - Fiocruz)", "url": "https://basearch.coc.fiocruz.br/index.php/pedrina-cunha-de-oliveira-2"}
        ]
    },
    "CCULI": {
        "acronym": "CCULI",
        "collection_name": "Coleção de Culicidae",
        "category": "Zoologia (Insetos)",
        "is_dual": True,
        "researchers": [
            {
                "name": "Dra. Teresa Fernandes Silva do Nascimento",
                "period": "1984–2023",
                "area": "Entomologia / Mosquitos Silvestres",
                "image_path": "../assets/images/CCULI_image1.png",
                "bio": "Ingressou na Fiocruz no ano de 1984 como estagiária. No ano de 1990 tornou-se pesquisadora em saúde pública. Cursou mestrado e doutorado em Biologia Parasitária no Instituto Oswaldo Cruz. Desenvolveu pesquisas na área de entomologia, dedicando-se ao estudo de mosquitos silvestres incluindo os vetores de arboviroses no Brasil.",
                "contribution": "Dra. Teresa Fernandes atuou como pesquisadora em saúde pública no Instituto Oswaldo Cruz. Dedicou-se à pesquisa e ensino na área de entomologia e parasitologia. Foi curadora adjunta da Coleção de Culicidae da Fiocruz em diferentes períodos entre 2011 e 2023. Aposentou-se no ano de 2024.",
                "legacy": "Descrição de novas espécies de mosquitos, formação de professores e profissionais na área da saúde, e estudos da fauna e a dinâmica de transmissão da malária em regiões de Mata Atlântica, Amazônia e Pantanal."
            },
            {
                "name": "Dra. Monique de Albuquerque Motta",
                "period": "1980–2024",
                "area": "Entomologia / Mosquitos e Arboviroses",
                "image_path": "../assets/images/CCULI_image3.png",
                "bio": "Ingressou na Fiocruz no ano de 1980, onde mais tarde cursou mestrado e doutorado em Biologia Parasitária. Tornou-se pesquisadora em saúde pública no ano de 1989. Desenvolveu importantes pesquisas em taxonomia e comportamento de mosquitos vetores de malária no Brasil.",
                "contribution": "Dra. Monique Motta atuou como pesquisadora em saúde pública no Instituto Oswaldo Cruz. Dedicou-se à pesquisa e ensino na área da biologia e comportamento de mosquitos silvestres. Foi curadora e curadora adjunta da Coleção de Culicidae da Fiocruz em diferentes períodos entre 2011 e 2023. Aposentou-se no ano de 2023.",
                "legacy": "Descrição de novas espécies de mosquitos, formação de professores e profissionais da área da saúde, e estudos sobre a fauna de mosquitos silvestres de diferentes regiões brasileiras."
            }
        ],
        "researcher_name": "Dras. Teresa Fernandes & Monique Motta",
        "period": "1980–2024",
        "area": "Zoologia / Entomologia",
        "quote": "Estas pesquisadoras contribuíram para o avanço da ciência brasileira e formaram novos profissionais, deixando um legado que continuará florescendo nas futuras gerações.",
        "bio": "Dra. Teresa Fernandes Silva do Nascimento e Dra. Monique de Albuquerque Motta são entomologistas renomadas que dedicaram suas carreiras à pesquisa de mosquitos silvestres e vetores de doenças tropicais. Atuando como curadoras e pesquisadoras da Coleção de Culicidae da Fiocruz, elas deixaram marcas indeléveis na saúde pública brasileira.",
        "contribution": "Sob suas curadorias (entre 2011 e 2023), a Coleção de Culicidae foi expandida, catalogada e mantida como acervo biológico estratégico de mosquitos neotropicais. Suas expedições de campo em diversos biomas enriqueceram o acervo com espécimes e tipos fundamentais para pesquisas epidemiológicas.",
        "importance": "Seus estudos revolucionaram o entendimento sobre os vetores da malária e arboviroses em regiões como a Mata Atlântica e a Amazônia. Além disso, foram fundamentais na formação de novas gerações de pesquisadores e no fortalecimento do controle de vetores.",
        "curiosity": "Ambas entraram na Fiocruz nos anos 1980 como estagiárias e completaram cerca de 40 anos de contribuição integral, passando por todos os estágios da carreira acadêmica até se aposentarem recentemente como referências nacionais em mosquitos.",
        "message": "Nossa trajetória mostra que a ciência se constrói com perseverança no campo e cuidado no laboratório, inspirando gerações a continuar desbravando a nossa biodiversidade.",
        "image_path": "../assets/images/CCULI_image_2.png",
        "theme": {
            "bg_gradient": "from-purple-600 to-indigo-800",
            "accent_text": "text-purple-600",
            "accent_bg": "bg-purple-50",
            "accent_border": "border-purple-500",
            "btn_bg": "bg-purple-600 hover:bg-purple-700",
            "shadow": "shadow-purple-100",
            "focus_ring": "focus:ring-purple-500"
        },
        "videos": []
    },
    "CEIOC": {
        "acronym": "CEIOC",
        "collection_name": "Coleção Entomológica do Instituto Oswaldo Cruz",
        "category": "Zoologia (Insetos)",
        "researcher_name": "Danielle Cerri do Nascimento",
        "period": "1997–2015",
        "area": "Entomologia e Museologia",
        "quote": "Cuidar de uma coleção biológica é cuidar da história, da biodiversidade e das próximas gerações de pesquisadores.",
        "bio": "Danielle Cerri do Nascimento é entomóloga e museóloga. Ingressou na Fiocruz em 1989, onde cursou o ensino médio na Escola Politécnica de Saúde Joaquim Venâncio. Fez Especialização em Entomologia Médica no Instituto Oswaldo Cruz e Mestrado em Museologia e Patrimônio na UNIRIO. Atuou por quase duas décadas na Coleção Entomológica do Instituto Oswaldo Cruz, com ações ligadas à curadoria, preservação do patrimônio e divulgação e popularização da ciência.",
        "contribution": "Atuou como assistente de curadoria na Coleção Entomológica (CEIOC). Entre suas principais atividades estão a implantação do sistema de gestão da qualidade, elaboração de procedimentos de curadoria, biossegurança e conservação preventiva. Também trabalhou no levantamento de espécimes-tipo, na recuperação de coleções históricas afetadas pelo 'Massacre de Manguinhos' e na preservação de acervos históricos valiosos, como as coleções Adolpho Lutz e Costa Lima.",
        "importance": "Ao atuar na preservação da maior e mais antiga coleção científica da instituição, Danielle teve grande dedicação aos cuidados de um acervo fragilizado por crises institucionais. Liderou a mudança física da coleção para novas salas entre 2008 e 2009 e ajudou a montar a Sala de Exposições Costa Lima, conectando conservação patrimonial à divulgação científica.",
        "curiosity": "Participou do Censo da CEIOC após o 'Massacre de Manguinhos', auxiliando na reorganização e informatização de centenas de milhares de espécimes. Liderou iniciativas pioneiras de gestão da qualidade, biossegurança e gestão ambiental no acervo, transformando a CEIOC em referência de infraestrutura moderna.",
        "message": "A dedicação e o cuidado com a preservação da Coleção Entomológica do Instituto Oswaldo Cruz e o entusiasmo na divulgação da sua importância para a ciência compõem o legado de Danielle Cerri para as coleções biológicas da Fiocruz.",
        "image_path": "../assets/images/CEIOC_image1.png",
        "theme": {
            "bg_gradient": "from-blue-600 to-indigo-800",
            "accent_text": "text-blue-600",
            "accent_bg": "bg-blue-50",
            "accent_border": "border-blue-500",
            "btn_bg": "bg-blue-600 hover:bg-blue-700",
            "shadow": "shadow-blue-100",
            "focus_ring": "focus:ring-blue-500"
        },
        "videos": []
    },
    "CFAS": {
        "acronym": "CFAS",
        "collection_name": "Coleção de Fungos do Ambiente e Saúde",
        "category": "Micologia (Fungos)",
        "researcher_name": "Marília Martins Nishikawa",
        "period": "1983–2020",
        "area": "Micologia, Microbiologia e Coleções de Microrganismos",
        "quote": "Sem o esforço da busca é impossível a alegria do encontro.",
        "bio": "Dra. Marília Martins Nishikawa é biomédica, mestre em Biologia Celular e Molecular e doutora em Vigilância Sanitária pela Fiocruz. Atuou de 1983 a 2020 no Instituto Nacional de Controle de Qualidade em Saúde (INCQS/Fiocruz) como Tecnologista em Saúde Pública. Sua carreira foi inteiramente dedicada à micologia, com foco na caracterização, identificação e preservação de fungos de importância médica e sanitária.",
        "contribution": "Atuou na Coleção de Fungos do Ambiente e Saúde (Fiocruz/CFAS), desenvolvendo pesquisas sobre fungos de interesse médico e ambiental. Liderou a produção, manutenção e fornecimento de fungos de referência, cruciais para controle de qualidade laboratorial, vigilância em saúde e formação de recursos humanos no INCQS.",
        "importance": "Desde 1983 estabeleceu e fortaleceu a CFAS. Desenvolveu estudos pioneiros sobre diversidade genética, epidemiologia e sensibilidade a antifúngicos de fungos patogênicos no Brasil, em especial do gênero Cryptococcus. Atuou fortemente na integração entre as coleções biológicas, pesquisa aplicada e vigilância sanitária.",
        "curiosity": "Seu doutorado foi desenvolvido a partir de fungos preservados na própria CFAS e na Coleção de Fungos Patogênicos (CFP), demonstrando como as coleções são verdadeiros laboratórios vivos. Ministrou inúmeros cursos práticos sobre preservação microbiológica, fortalecendo redes nacionais de laboratórios.",
        "message": "Sem o esforço da busca é impossível a alegria do encontro.",
        "image_path": "../assets/images/CFAS_image2.jpg",
        "theme": {
            "bg_gradient": "from-pink-600 to-rose-800",
            "accent_text": "text-pink-600",
            "accent_bg": "bg-pink-50",
            "accent_border": "border-pink-500",
            "btn_bg": "bg-pink-600 hover:bg-pink-700",
            "shadow": "shadow-pink-100",
            "focus_ring": "focus:ring-pink-500"
        },
        "videos": []
    },
    "CFAM": {
        "acronym": "CFAM",
        "collection_name": "Coleção de Fungos da Amazônia",
        "category": "Micologia (Fungos)",
        "researcher_name": "Dra. Maria Inês de Moura Sarquis",
        "period": "1980–presente",
        "area": "Micologia / Biotecnologia Fúngica",
        "quote": "Preservar a biodiversidade dos fungos da Amazônia é salvaguardar a riqueza de nossa floresta e abrir caminhos infinitos para a biotecnologia.",
        "bio": "Dra. Maria Inês de Moura Sarquis é bióloga, pesquisadora associada da Fundação Oswaldo Cruz e a idealizadora da Coleção de Fungos da Amazônia (CFAM), do Instituto Leônidas e Maria Deane – Fiocruz Amazônia.",
        "contribution": "Visionária e dedicada à ciência, foi a principal incentivadora da criação da CFAM, deixando um legado que continua impulsionando a pesquisa, a conservação da biodiversidade microbiana amazônica e a formação de novos pesquisadores.",
        "importance": "Sua trajetória científica foi marcada por importantes contribuições ao estudo da microbiologia, com destaque para as pesquisas sobre a longevidade e as alterações biomorfológicas de fungos preservados, além da prospecção de fungos Hyphomycetes para a produção de enzimas de interesse biotecnológico.",
        "curiosity": "Seu compromisso com a excelência científica, a preservação do patrimônio microbiológico e o avanço do conhecimento permanece vivo em cada amostra conservada na CFAM e em cada pesquisa desenvolvida a partir de seu trabalho. Seu legado inspira a ciência, fortalece a Fiocruz Amazônia e perpetua a missão da CFAM de preservar, conhecer e valorizar a diversidade fúngica da Amazônia.",
        "message": "Preservar a biodiversidade fúngica da Amazônia é o nosso compromisso com a ciência, com a vida e com as futuras gerações de pesquisadores que continuarão a contar essa história.",
        "image_path": "../assets/images/CFAM_Image1.png",
        "card_image_path": "../assets/images/CFAM_Image2.png",
        "theme": {
            "bg_gradient": "from-emerald-700 to-green-900",
            "accent_text": "text-emerald-700",
            "accent_bg": "bg-emerald-50",
            "accent_border": "border-emerald-500",
            "btn_bg": "bg-emerald-700 hover:bg-emerald-800",
            "shadow": "shadow-emerald-100",
            "focus_ring": "focus:ring-emerald-500"
        },
        "videos": [
            {"title": "Entrevista da Dra. Maria Inês de Moura Sarquis (Base Arch - Fiocruz)", "url": "https://basearch.coc.fiocruz.br/index.php/maria-inez-de-moura-sarquis-2"}
        ]
    },
    "CLEP": {
        "acronym": "CLEP",
        "collection_name": "Coleção de Leptospira",
        "category": "Parasitologia / Microbiologia",
        "researcher_name": "Dra. Martha Maria Pereira",
        "period": "1980–atual",
        "area": "Bióloga, com foco no estudo da Leptospirose",
        "quote": "Sua trajetória une ciência, liderança e compromisso público, fortalecendo o enfrentamento da leptospirose no Brasil e no mundo.",
        "bio": "Dra. Martha Maria Pereira desenvolveu toda sua carreira no Instituto Oswaldo Cruz/Fiocruz com o tema Leptospirose. Bióloga de formação, mestre em Biologia Parasitária e doutora em Biologia Celular e Molecular, impulsionou o conhecimento sobre a doença e seu agente etiológico. Contribuiu significativamente para a saúde pública ao atuar na estruturação de redes de diagnóstico junto ao Ministério da Saúde.",
        "contribution": "Participou do isolamento das primeiras linhagens de Leptospira spp. que compõem o acervo da Coleção de Leptospira. Em 1985, isolou e identificou o sorovar Cuica, um achado inédito no mundo. Sob sua liderança, o Laboratório de Referência Nacional foi credenciado, impulsionando o crescimento e diversificação das cepas da coleção.",
        "importance": "Liderou a estruturação do Serviço de Diagnóstico da Leptospirose do IOC, credenciado como Laboratório de Referência Nacional pelo Ministério da Saúde e, posteriormente, como Centro Colaborador da Organização Mundial da Saúde (OMS) para Leptospirose, consolidando o prestígio científico internacional da Fiocruz na área.",
        "curiosity": "Atuou como vice-diretora do Instituto Oswaldo Cruz e chefe do Departamento de Bacteriologia. Foi fundamental na formação de centenas de alunos e profissionais de Laboratórios Centrais de Saúde Pública (LACENs) de todo o Brasil, criando referências diagnósticas sólidas.",
        "message": "A ciência e a saúde pública caminham lado a lado quando dedicamos nosso esforço a levar respostas diretamente do laboratório para o bem-estar da sociedade.",
        "image_path": "../assets/images/CLEP_image1.jpg",
        "theme": {
            "bg_gradient": "from-amber-600 to-orange-900",
            "accent_text": "text-amber-600",
            "accent_bg": "bg-amber-50",
            "accent_border": "border-amber-500",
            "btn_bg": "bg-amber-600 hover:bg-amber-700",
            "shadow": "shadow-amber-100",
            "focus_ring": "focus:ring-amber-500"
        },
        "videos": []
    },
    "CLIOC": {
        "acronym": "CLIOC",
        "collection_name": "Coleção de Leishmania do IOC",
        "category": "Parasitologia / Microbiologia",
        "researcher_name": "Selma Quintella Soares",
        "period": "1987–atual",
        "area": "Técnica em Parasitologia",
        "quote": "Costumamos premiar e homenagear grandes descobertas, mas, muitas vezes, não nos lembramos de que, ao lado de quem realizou estes feitos, sempre havia muitas pessoas trabalhando, dedicada e silenciosamente.",
        "bio": "Selma Quintella Soares é técnica do Laboratório de Pesquisa em Leishmanioses (LPL) do IOC/Fiocruz, que abriga a Coleção de Leishmania (CLIOC). Ingressou em 1987 e acompanhou de perto a criação, crescimento e consolidação da coleção, prestando serviços essenciais por quase 40 anos ininterruptos.",
        "contribution": "Atua na base operacional e técnica de todos os trabalhos desenvolvidos na CLIOC. Participa na elaboração e revisão de protocolos técnicos, realiza a preparação minuciosa de meios de cultivo, reagentes e soluções comuns, além de zelar pela segurança biológica e organização dos espaços laboratoriais.",
        "importance": "A homenagem à Selma representa a valorização fundamental do papel das técnicas e técnicos de laboratório, frequentemente invisibilizados no fazer científico. Seu zelo técnico e sua dedicação diária mantêm a viabilidade das cepas vivas de Leishmania e garantem a integridade da pesquisa científica e das cooperações nacionais e internacionais.",
        "curiosity": "Cresceu vivendo a história da Fiocruz de forma muito próxima, pois quando criança acompanhava seu pai, Rui Quintella, pelo campus de Manguinhos. Além do rigor técnico metódico no trabalho, Selma é conhecida por dominar 'protocolos culinários' herdados de sua família, trazendo alegria e união para a equipe do laboratório.",
        "message": "Um trabalho exitoso, raramente, inclui apenas uma única mente pensante e duas mãos. O fazer científico constrói-se melhor coletivamente e de forma compartilhada. A ciência está repleta de mulheres imensas, intensas, persistentes e resilientes, para nos inspirar.",
        "image_path": "../assets/images/CLIOC_image1.jpg",
        "theme": {
            "bg_gradient": "from-fuchsia-600 to-pink-900",
            "accent_text": "text-fuchsia-600",
            "accent_bg": "bg-fuchsia-50",
            "accent_border": "border-fuchsia-500",
            "btn_bg": "bg-fuchsia-600 hover:bg-fuchsia-700",
            "shadow": "shadow-fuchsia-100",
            "focus_ring": "focus:ring-fuchsia-500"
        },
        "videos": []
    },
    "CMIOC": {
        "acronym": "CMIOC",
        "collection_name": "Coleção de Moluscos do Instituto Oswaldo Cruz",
        "category": "Zoologia (Moluscos)",
        "researcher_name": "Silvana Carvalho Thiengo",
        "period": "1982–atual",
        "area": "Malacologia Médica e Curadoria",
        "quote": "Entre moluscos, coleções biológicas e saúde pública, construiu uma trajetória de pioneirismo que inspira novas gerações de cientistas.",
        "bio": "Silvana Carvalho Thiengo é bióloga, mestre em Zoologia pela UFRJ e doutora em Ciências Veterinárias pela UFRRJ. Pesquisadora em Saúde Pública da Fiocruz, dedica-se desde a década de 1980 à Malacologia Médica, com ênfase no estudo de moluscos de importância epidemiológica e na transmissão de parasitos. Está vinculada à Coleção de Moluscos (CMIOC) desde 1982.",
        "contribution": "Esteve à frente da CMIOC por mais de quarenta anos como curadora, liderando a ampliação, organização, modernização e conservação preventiva do acervo. Atuou ativamente no fortalecimento das coleções biológicas da Fiocruz como infraestrutura estratégica de pesquisa e vigilância sanitária nacional.",
        "importance": "Referência na Malacologia Médica brasileira, realizou estudos de campo fundamentais sobre a distribuição de moluscos hospedeiros intermediários (como espécies de Biomphalaria, vetores da esquistossomose) em todo o território nacional, gerando mapas de distribuição vitais para subsidiar ações de vigilância epidemiológica do Ministério da Saúde.",
        "curiosity": "Dra. Silvana é uma das maiores especialistas em ampularídeos, grupo dos maiores gastrópodes dulcícolas do país (os aruás ou 'apple-snails'). Seus estudos de taxonomia e biologia desses animais fortaleceram pesquisas em biodiversidade, ecologia e controle biológico.",
        "message": "Nossa trajetória nas coleções biológicas nos ensina que observar a complexidade da natureza nos mínimos detalhes, como a concha de um molusco, é o primeiro passo para salvaguardar a saúde de toda uma população.",
        "image_path": "../assets/images/CMIOC_image2.png",
        "theme": {
            "bg_gradient": "from-cyan-600 to-teal-800",
            "accent_text": "text-cyan-600",
            "accent_bg": "bg-cyan-50",
            "accent_border": "border-cyan-500",
            "btn_bg": "bg-cyan-600 hover:bg-cyan-700",
            "shadow": "shadow-cyan-100",
            "focus_ring": "focus:ring-cyan-500"
        },
        "videos": []
    },
    "CPFERA": {
        "acronym": "CPFERA",
        "collection_name": "Coleção Paleoparasitológica e de Fezes Recentes de Animais",
        "category": "Patologia / Arqueologia",
        "researcher_name": "Dra. Niède Guidon",
        "period": "1973–2025",
        "area": "Arqueologia e Preservação de Sítios",
        "quote": "Neste instante, caro colega do futuro, estendo o meu olhar pela vastidão do que ainda é um pedaço do paraíso - um pedaço do paraíso chamado Serra da Capivara -, [....] e entrego-lhe este texto para que continue a contar como prosseguiu a nossa história, a história de todos nós....",
        "bio": "Dra. Niède Guidon foi uma das maiores arqueólogas brasileiras, formada em História Natural (USP) e doutora pela Université de Paris. Dedicou sua vida à pesquisa no Piauí, liderando expedições que desafiaram a teoria clássica de povoamento das Américas, provando a presença humana no Nordeste muito antes do postulado pelo Estreito de Bering. Faleceu em junho de 2025.",
        "contribution": "Niède foi uma parceira científica indispensável para a CPFERA. Durante suas escavações arqueológicas em abrigos sob rocha, identificava coprólitos (fezes fossilizadas) e materiais orgânicos raros, coletando-os meticulosamente e direcionando-os à coleção da Fiocruz, permitindo estudos paleoepidemiológicos inéditos de parasitos em humanos antigos.",
        "importance": "Mapeou mais de mil sítios arqueológicos no Piauí e liderou a criação do Parque Nacional Serra da Capivara (1979), declarado Patrimônio Cultural da Humanidade pela UNESCO. Fundou a FUMDHAM (Fundação Museu do Homem Americano) e idealizou os museus do Homem Americano e da Natureza, integrando pesquisa arqueológica ao desenvolvimento social da comunidade.",
        "curiosity": "Conhecida por sua bravura e apelidada de 'onça'. Em uma expedição, desceu 120 metros em uma corda para explorar um abismo onde encontrou fósseis de tigre-dente-de-sabre de 11 mil anos. Ao subir, foi severamente picada por abelhas, mas resistiu e, na manhã seguinte, insistiu em retornar. Recebeu diversas espécies batizadas em sua homenagem, como o pássaro Sakesphoroides niedeguidonae.",
        "message": "Proteger o patrimônio histórico e ambiental de uma nação só é possível quando envolvemos, educamos e oferecemos oportunidades de desenvolvimento social e econômico às populações que vivem ao seu redor.",
        "image_path": "../assets/images/CPFERA_image1.jpeg",
        "theme": {
            "bg_gradient": "from-amber-900 to-yellow-950",
            "accent_text": "text-amber-800",
            "accent_bg": "bg-amber-50",
            "accent_border": "border-amber-700",
            "btn_bg": "bg-amber-800 hover:bg-amber-900",
            "shadow": "shadow-amber-200",
            "focus_ring": "focus:ring-amber-700"
        },
        "videos": [
            {"title": "História com a Arte Rupestre (YouTube)", "url": "https://youtu.be/--4En5z8Xh8?si=ozoB3hvPL_CsJ-pE"}
        ]
    },
    "CYP_CBAS_CBP": {
        "acronym": "CYP_CBAS_CBP",
        "display_acronym": "CYP/CBAS/CBP",  # Display with slash as requested
        "collection_name": "Coleção de Culturas de Yersinia pestis",
        "category": "Parasitologia / Microbiologia",
        "researcher_name": "Dra. Alzira Maria Paiva de Almeida",
        "period": "1966–presente",
        "area": "Microbiologia e Vigilância Epidemiológica",
        "quote": "Tem que ter curiosidade, não se limitar... Estar sempre aberta a oportunidades e aquisição de conhecimento... Não ter medo de assumir riscos.",
        "bio": "Dra. Alzira Maria Paiva de Almeida é graduada em Nutrição e doutora em Microbiologia. Pesquisadora emérita da Fiocruz, atua no Instituto Aggeu Magalhães (Fiocruz PE) desde 1966. Tornou-se uma das maiores especialistas em peste (Yersinia pestis) do mundo, deixando um legado inestimável no controle e vigilância de zoonoses no Brasil.",
        "contribution": "Curadora da Coleção CYP desde sua institucionalização em 2007. Ela pessoalmente constituiu, isolou de amostras humanas e vetores, catalogou e preservou o acervo biológico desde 1966. Coordena o Serviço de Referência Nacional em Peste (SRP) desde 2002, assessorando diretamente o Ministério da Saúde.",
        "importance": "Em 1981, realizou treinamento no CDC (EUA) e implantou a fabricação nacional de insumos sorológicos para diagnóstico da peste, eliminando a dependência do Brasil de importações caras. Ingressou nas pesquisas de campo no semiárido pernambucano (Exu-PE) in 1966 como a única mulher da equipe, quebrando preconceitos e abrindo portas para a inserção acadêmica feminina na região.",
        "curiosity": "Orientou mais de 70 estudantes de pós-graduação e iniciação científica e publicou mais de 130 artigos científicos. Recebeu o título de Cidadã Exuense em 2015 em honra aos services prestados à população local. Continua ativa como pesquisadora emérita aos mais de 80 anos.",
        "message": "Com tenacidade de nordestina, aprendi que ser cientista exige coragem para ir ao campo e curiosidade incessante no laboratório, pois não há limites para quem busca transformar conhecimento em proteção da saúde.",
        "image_path": "../assets/images/CYP_CBAS_CBP_image1.png",
        "theme": {
            "bg_gradient": "from-orange-600 to-red-800",
            "accent_text": "text-orange-600",
            "accent_bg": "bg-orange-50",
            "accent_border": "border-orange-500",
            "btn_bg": "bg-orange-600 hover:bg-orange-700",
            "shadow": "shadow-orange-100",
            "focus_ring": "focus:ring-orange-500"
        },
        "videos": [
            {"title": "Trajetórias de Mulheres na Fiocruz", "url": "https://fiocruz.br/video/alzira-maria-de-paiva-almeida-mulheres-na-fiocruz-trajetorias"},
            {"title": "Histórias para Inspirar Cientistas (Fiocruz)", "url": "https://portolivre.fiocruz.br/historias-para-inspirar-futuras-cientistas"}
        ]
    },
    "MP": {
        "acronym": "MP",
        "collection_name": "Coleção de Patologia / Febre Amarela",
        "category": "Patologia / Arqueologia",
        "researcher_name": "Dra. Itália Kerr",
        "period": "1957–década de 1990",
        "area": "Patologia Experimental e Preservação de Memória",
        "quote": "A ciência se fortalece quando preservamos a memória do que já foi descoberto.",
        "bio": "Dra. Itália Kerr foi uma destacada patologista do Instituto Oswaldo Cruz (IOC), dedicando sua vida profissional entre 1957 e o fim da década de 1990 ao avanço da patologia experimental e à guarda de acervos históricos biológicos na área médica.",
        "contribution": "Teve atuação decisiva na curadoria e manutenção das Coleções de Patologia e da Coleção de Febre Amarela do IOC. Organizou lâminas histológicas, blocos de parafina e peças anatômicas fundamentais que contam a história de surtos epidêmicos e nosologias brasileiras ao longo do século XX.",
        "importance": "Seu trabalho meticuloso na catalogação e salvaguarda dessas coleções garantiu que amostras históricas valiosas permanecessem intactas para estudos contemporâneos de patógenos. Liderou atividades de ensino prático de patologia, formando gerações de técnicos de necrópsia e patologistas no IOC, reforçando o valor científico da memória em saúde pública.",
        "curiosity": "Era amplamente reconhecida pelo zelo na preservação da memória científica de Manguinhos. Defendia de forma apaixonada que o estudo retrospectivo do tecido patológico de epidemias passadas é crucial para antever e diagnosticar as emergências sanitárias do futuro.",
        "message": "Dedicou sua vida ao estudo das doenças, à preservação de coleções históricas e ao fortalecimento da ciência brasileira. Seu trabalho inspira novas gerações de cientistas.",
        "image_path": "../assets/images/MP_image1.png",
        "theme": {
            "bg_gradient": "from-red-600 to-rose-900",
            "accent_text": "text-rose-700",
            "accent_bg": "bg-red-50",
            "accent_border": "border-red-500",
            "btn_bg": "bg-red-600 hover:bg-red-700",
            "shadow": "shadow-red-100",
            "focus_ring": "focus:ring-red-500"
        },
        "videos": [
            {"title": "Entrevista da Dra. Itália Kerr (Base Arch - Fiocruz)", "url": "https://basearch.coc.fiocruz.br/index.php/italia-guarany-angiola-kerr"}
        ]
    }
}

# 1. GENERATE MAIN HOME PORTAL (index.html)
def generate_home_page():
    categories = sorted(list(set(col["category"] for col in collections_data.values())))
    
    cards_html = ""
    for acronym, col in collections_data.items():
        img_src = col.get("card_image_path", col["image_path"])
        display_acr = col.get("display_acronym", col["acronym"])
        
        cards_html += f"""
        <!-- Card for {acronym} (Entire card is clickable) -->
        <a href="{acronym.lower()}/index.html" class="collection-card group bg-white rounded-2xl overflow-hidden shadow-sm hover:shadow-xl border border-gray-150 transition-all duration-300 flex flex-col h-full" data-category="{col['category']}">
            <div class="relative overflow-hidden aspect-video bg-gradient-to-br {col['theme']['bg_gradient']} flex items-center justify-center p-3">
                <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#fff_1px,transparent_1px)] [background-size:16px_16px]"></div>
                <img src="{img_src}" alt="{col['researcher_name']}" class="h-full w-full object-cover rounded-lg group-hover:scale-103 transition-transform duration-500 shadow-md" />
                
                <span class="absolute top-3 left-3 bg-white/95 backdrop-blur text-[10px] font-bold px-2 py-0.5 rounded-full text-gray-800 shadow-sm uppercase tracking-wider">{col['category']}</span>
                <span class="absolute bottom-3 right-3 bg-black/60 backdrop-blur-sm text-[10px] font-mono font-bold px-2 py-0.5 rounded text-white tracking-widest">{display_acr}</span>
            </div>
            
            <div class="p-5 flex flex-col flex-grow">
                <h3 class="text-lg font-bold text-gray-900 group-hover:{col['theme']['accent_text']} transition-colors duration-200 line-clamp-1">{col['researcher_name']}</h3>
                <p class="text-[11px] font-bold text-gray-400 mt-0.5 uppercase tracking-wider">{col['collection_name'].replace("CYP_CBAS_CBP", "CYP/CBAS/CBP")}</p>
                
                <p class="text-xs text-gray-600 italic mt-3 flex-grow line-clamp-3">“{col['quote']}”</p>
                
                <div class="mt-5 pt-3 border-t border-gray-100 flex items-center justify-between">
                    <span class="text-[11px] font-mono text-gray-500 flex items-center">
                        <svg class="w-3.5 h-3.5 mr-1 text-gray-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                        {col['period']}
                    </span>
                    <span class="inline-flex items-center text-[11px] font-bold tracking-wider uppercase text-gray-900 group-hover:{col['theme']['accent_text']} transition-colors duration-200 font-sans">
                        Saber Mais 
                        <svg class="w-3.5 h-3.5 ml-1 transform group-hover:translate-x-0.5 transition-transform" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path></svg>
                    </span>
                </div>
            </div>
        </a>
        """
        
    # Categories filters layout with responsive wrap (no overflow breakdown)
    category_buttons_html = '<button onclick="filterCategory(\'all\')" id="btn-all" class="cat-btn px-4 py-2 text-xs sm:text-sm font-semibold rounded-full bg-blue-600 text-white shadow-md border border-blue-600 transition-all duration-300">Todas</button>'
    for cat in categories:
        safe_cat = cat.replace(" ", "_")
        category_buttons_html += f'\n<button onclick="filterCategory(\'{cat}\')" id="btn-{safe_cat}" class="cat-btn px-4 py-2 text-xs sm:text-sm font-semibold rounded-full bg-white text-gray-700 border border-gray-200 hover:border-gray-300 transition-all duration-300 shadow-sm">{cat}</button>'

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mulheres nas Coleções Biológicas - FIOCRUZ | SBPC 2026</title>
    <meta name="description" content="Portal de Homenagem às pesquisadoras das Coleções Biológicas da Fiocruz participantes da SBPC 2026.">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        outfit: ['Outfit', 'sans-serif'],
                    }},
                    colors: {{
                        fiocruz: {{
                            blue: '#00529b',
                            gold: '#c59b27',
                            dark: '#0f172a',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .font-outfit {{ font-family: 'Outfit', sans-serif; }}
        body {{
            opacity: 0;
            transition: opacity 0.4s ease-in-out;
        }}
        body.loaded {{
            opacity: 1;
        }}
    </style>
</head>
<body class="bg-slate-50 text-gray-900 font-sans min-h-screen flex flex-col antialiased loaded font-outfit">

    <!-- Header Section -->
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-gray-100 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-3.5 min-h-[44px]">
                <img src="assets/images/logo_fiocruz.png" alt="Fiocruz" class="h-10 sm:h-12 w-auto" />
                <div class="h-8 w-px bg-gray-200"></div>
                <img src="assets/images/Logo_Colecoes.jpg" alt="Coleções Biológicas" class="h-9 sm:h-11 w-auto rounded shadow-sm border border-gray-100" />
            </a>
            <div class="flex items-center gap-3 sm:gap-6">
                <!-- Programacao Page link added to Header -->
                <a href="programacao.html" class="text-xs sm:text-sm font-bold text-gray-700 hover:text-fiocruz-blue transition-colors flex items-center gap-1.5 min-h-[40px] px-2 rounded-lg hover:bg-gray-50">
                    <svg class="w-4 h-4 text-fiocruz-blue" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                    Programação
                </a>
                <span class="bg-blue-50 text-blue-700 border border-blue-100 rounded-full text-[9px] sm:text-xs font-semibold px-2.5 py-0.5 sm:px-3 sm:py-1 uppercase tracking-wider font-sans">SBPC 2026</span>
            </div>
        </div>
    </header>

    <!-- Hero / Intro -->
    <section class="relative bg-fiocruz-dark text-white py-12 sm:py-20 overflow-hidden font-sans">
        <div class="absolute -top-40 -right-40 w-96 h-96 rounded-full bg-blue-500/10 blur-3xl"></div>
        <div class="absolute -bottom-40 -left-40 w-96 h-96 rounded-full bg-emerald-500/10 blur-3xl"></div>
        
        <div class="max-w-4xl mx-auto px-4 text-center relative z-10">
            <!-- colecionarPop banner logo added in upper hero -->
            <img src="assets/images/colecionarPop.png" alt="Colecionar Pop" class="mx-auto h-20 sm:h-24 w-auto mb-6 drop-shadow-md" />
            
            <span class="inline-block bg-fiocruz-gold/20 text-fiocruz-gold border border-fiocruz-gold/30 rounded-full text-[10px] sm:text-xs font-bold px-3 py-1 uppercase tracking-widest mb-4 font-outfit">SBPC 2026 • UFF Niterói</span>
            <h2 class="font-outfit text-3xl sm:text-5xl font-extrabold tracking-tight mb-4 leading-tight">
                Mulheres nas <span class="bg-gradient-to-r from-blue-400 via-teal-400 to-fiocruz-gold bg-clip-text text-transparent font-outfit">Coleções Biológicas</span>
            </h2>
            <p class="text-sm sm:text-lg text-gray-300 font-light max-w-xl mx-auto leading-relaxed px-2 mb-6 font-sans">
                Descubra as trajetórias inspiradoras de mulheres cientistas que preservaram a biodiversidade e fortaleceram a saúde pública no Brasil.
            </p>
            <!-- Button linking directly to the new Programacao page -->
            <a href="programacao.html" class="inline-flex items-center gap-2 bg-fiocruz-blue hover:bg-blue-700 text-white font-bold text-xs uppercase tracking-wider px-5 py-3 rounded-xl transition-all shadow-md active:scale-95">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                Ver Programação das Coleções
            </a>
        </div>
    </section>

    <!-- Search & Filter Controls -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-6 sm:-mt-8 relative z-20 w-full font-sans">
        <div class="bg-white rounded-2xl shadow-lg border border-gray-150 p-5 sm:p-7">
            <div class="flex flex-col gap-5">
                <!-- Search bar -->
                <div class="relative w-full">
                    <input type="text" id="search-input" onkeyup="searchResearchers()" placeholder="Buscar por pesquisadora, coleção ou área..." class="w-full pl-11 pr-4 py-2.5 bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 focus:bg-white transition-all text-sm" />
                    <svg class="w-4 h-4 text-gray-400 absolute left-4 top-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                </div>
                
                <!-- Category Filter Pills (Wrapping dynamically on mobile) -->
                <div class="flex flex-col gap-2">
                    <span class="text-[10px] font-bold text-gray-400 uppercase tracking-widest">Filtrar por Área:</span>
                    <div class="flex flex-wrap gap-2 w-full">
                        {category_buttons_html}
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Grid Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 flex-grow font-sans">
        <div id="no-results" class="hidden text-center py-16">
            <svg class="w-12 h-12 text-gray-300 mx-auto mb-3" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z"></path></svg>
            <h3 class="text-base font-bold text-gray-900">Nenhuma pesquisadora encontrada</h3>
            <p class="text-gray-500 text-xs mt-1">Tente ajustar seus termos de pesquisa ou filtros.</p>
        </div>

        <div id="cards-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
            {cards_html}
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white mt-auto border-t border-gray-800 text-sm font-sans">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-6">
                <!-- Logo_Colecoes.jpg included next to VPPCB in footer -->
                <div class="flex items-center gap-4">
                    <img src="assets/images/Logo_Colecoes.jpg" alt="Logo Coleções" class="h-14 sm:h-16 w-auto rounded border border-gray-800 shadow-sm" />
                    <div class="h-8 w-px bg-gray-800"></div>
                    <img src="assets/images/logo_fiocruz_negativo.png" alt="Fiocruz" class="h-10 sm:h-12 w-auto" />
                </div>
                <div class="flex gap-4 text-xs text-gray-400">
                    <a href="https://fiocruz.br" target="_blank" class="hover:text-white transition-colors">Portal Fiocruz</a>
                    <a href="https://sbpc.uff.br/" target="_blank" class="hover:text-white transition-colors">SBPC 2026</a>
                </div>
            </div>
            <div class="border-t border-gray-800 mt-6 pt-6 text-center text-[11px] text-gray-500 flex flex-col sm:flex-row justify-between items-center gap-2">
                <p>© 2026 Fundação Oswaldo Cruz. Desenvolvido para a SBPC 2026 (Niterói/UFF).</p>
                <p class="italic">Reconhecendo trajetórias que inspiram a ciência.</p>
            </div>
        </div>
    </footer>

    <!-- Filter/Search Logic Javascript -->
    <script>
        document.addEventListener("DOMContentLoaded", () => {{
            document.body.classList.add("loaded");
        }});

        let activeCategory = "all";

        function filterCategory(category) {{
            activeCategory = category;
            
            const buttons = document.querySelectorAll(".cat-btn");
            buttons.forEach(btn => {{
                btn.className = "cat-btn px-4 py-2 text-xs font-semibold rounded-full bg-white text-gray-700 border border-gray-200 hover:border-gray-300 transition-all duration-300 shadow-sm";
            }});
            
            const activeId = category === "all" ? "btn-all" : "btn-" + category.replace(/ /g, "_");
            const activeBtn = document.getElementById(activeId);
            if (activeBtn) {{
                activeBtn.className = "cat-btn px-4 py-2 text-xs font-semibold rounded-full bg-blue-600 text-white shadow-md border border-blue-600 transition-all duration-300";
            }}
            
            runFiltering();
        }}

        function searchResearchers() {{
            runFiltering();
        }}

        function runFiltering() {{
            const searchVal = document.getElementById("search-input").value.toLowerCase();
            const cards = document.querySelectorAll(".collection-card");
            let visibleCount = 0;
            
            cards.forEach(card => {{
                const cat = card.getAttribute("data-category");
                const cardText = card.textContent.toLowerCase();
                
                const matchesCat = (activeCategory === "all" || cat === activeCategory);
                const matchesSearch = cardText.includes(searchVal);
                
                if (matchesCat && matchesSearch) {{
                    card.style.display = "flex";
                    visibleCount++;
                }} else {{
                    card.style.display = "none";
                }}
            }});
            
            const noResults = document.getElementById("no-results");
            if (visibleCount === 0) {{
                noResults.classList.remove("hidden");
            }} else {{
                noResults.classList.add("hidden");
            }}
        }}
    </script>
</body>
</html>
"""
    
    with open(os.path.join(workspace_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Generated responsive home portal (index.html)")

# 2. GENERATE INDIVIDUAL BIO PAGES
def generate_individual_pages():
    for acronym, col in collections_data.items():
        sub_path = os.path.join(workspace_dir, acronym.lower())
        os.makedirs(sub_path, exist_ok=True)
        
        display_acr = col.get("display_acronym", col["acronym"])
        
        audio_guide_text = f"Homenagem da Coleção {display_acr}. {col['researcher_name']}. {col['bio']} {col['contribution']} {col['importance']} {col['curiosity']} Mensagem inspiradora: {col['message']}"
        audio_guide_text_escaped = audio_guide_text.replace("'", "\\'").replace('"', '\\"').replace("\n", " ")
        
        # Build Videos section HTML (More compact)
        videos_html = ""
        if col["videos"]:
            videos_html += """
            <div class="mt-10 border-t border-gray-150 pt-8 font-sans">
                <h3 class="font-outfit text-lg font-bold text-gray-900 mb-4 flex items-center">
                    <svg class="w-5 h-5 mr-2 text-red-600" fill="currentColor" viewBox="0 0 24 24"><path d="M23 12a11 11 0 11-22 0 11 11 0 0122 0zm-13.5 5.5l7.5-5.5-7.5-5.5v11z"></path></svg>
                    Vídeos e Conteúdos Relacionados
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            """
            for vid in col["videos"]:
                embed_url = vid["url"]
                if "youtu.be/" in embed_url:
                    vid_id = embed_url.split("youtu.be/")[1].split("?")[0]
                    embed_url = f"https://www.youtube.com/embed/{vid_id}"
                elif "watch?v=" in embed_url:
                    vid_id = embed_url.split("watch?v=")[1].split("&")[0]
                    embed_url = f"https://www.youtube.com/embed/{vid_id}"
                
                if "youtube.com/embed" in embed_url:
                    videos_html += f"""
                    <div class="flex flex-col bg-gray-50 border border-gray-200 rounded-2xl overflow-hidden shadow-sm">
                        <div class="aspect-video w-full">
                            <iframe class="w-full h-full" src="{embed_url}" title="{vid['title']}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                        </div>
                        <div class="p-3 bg-white">
                            <span class="text-xs font-semibold text-gray-800 line-clamp-1">{vid['title']}</span>
                        </div>
                    </div>
                    """
                else:
                    link_label = "Acessar no YouTube" if "youtube" in embed_url or "youtu.be" in embed_url else "Acessar acervo histórico"
                    videos_html += f"""
                    <a href="{vid['url']}" target="_blank" class="flex items-center p-3.5 bg-white border border-gray-200 rounded-2xl hover:bg-gray-50 transition-colors shadow-sm gap-3 group min-h-[64px]">
                        <div class="w-9 h-9 rounded-full bg-blue-100 flex items-center justify-center text-blue-600 group-hover:bg-blue-600 group-hover:text-white transition-all duration-300 flex-shrink-0">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                        </div>
                        <div class="overflow-hidden font-sans">
                            <span class="text-xs sm:text-sm font-semibold text-gray-800 block leading-tight truncate group-hover:underline">{vid['title']}</span>
                            <span class="text-[10px] text-gray-400 mt-0.5 block">{link_label}</span>
                        </div>
                    </a>
                    """
            videos_html += "</div></div>"

        # Check if CCULI dual researcher layout
        main_content_html = ""
        portrait_card_html = ""
        
        if col.get("is_dual"):
            r1, r2 = col["researchers"][0], col["researchers"][1]
            
            # Portrait card: Shows both researchers side-by-side on desktop
            portrait_card_html = f"""
            <div class="grid grid-cols-2 gap-4 items-center">
                <div class="bg-white/5 border border-white/10 rounded-2xl p-3 flex flex-col items-center text-center shadow-lg backdrop-blur-sm">
                    <img src="{r1['image_path']}" alt="{r1['name']}" class="w-full max-w-[120px] aspect-[3/4] object-cover rounded-xl border border-white/20 shadow-md mb-3 hover:scale-103 transition-transform" />
                    <h4 class="font-outfit text-xs font-bold text-white line-clamp-1">{r1['name']}</h4>
                    <p class="text-[9px] text-purple-200 mt-0.5 uppercase tracking-wider leading-tight">{r1['area']}</p>
                    <span class="text-[9px] font-mono text-purple-300 mt-0.5">{r1['period']}</span>
                </div>
                <div class="bg-white/5 border border-white/10 rounded-2xl p-3 flex flex-col items-center text-center shadow-lg backdrop-blur-sm">
                    <img src="{r2['image_path']}" alt="{r2['name']}" class="w-full max-w-[120px] aspect-[3/4] object-cover rounded-xl border border-white/20 shadow-md mb-3 hover:scale-103 transition-transform" />
                    <h4 class="font-outfit text-xs font-bold text-white line-clamp-1">{r2['name']}</h4>
                    <p class="text-[9px] text-purple-200 mt-0.5 uppercase tracking-wider leading-tight">{r2['area']}</p>
                    <span class="text-[9px] font-mono text-purple-300 mt-0.5">{r2['period']}</span>
                </div>
            </div>
            """
            
            # Stacked Layout: One researcher description below the other
            main_content_html = f"""
            <div class="flex flex-col gap-8">
                <!-- Researcher 1: Teresa Fernandes -->
                <div class="bg-white border border-gray-150 rounded-2xl p-5 sm:p-7 shadow-sm">
                    <div class="flex flex-col sm:flex-row items-center gap-4 border-b border-gray-100 pb-4 mb-5">
                        <img src="{r1['image_path']}" alt="{r1['name']}" class="w-24 h-32 object-cover rounded-xl shadow-md border border-gray-200" />
                        <div class="text-center sm:text-left">
                            <h3 class="font-outfit text-lg sm:text-xl font-bold text-gray-900">{r1['name']}</h3>
                            <p class="text-xs text-purple-600 font-semibold uppercase tracking-wider mt-0.5">{r1['area']}</p>
                            <span class="inline-block bg-purple-50 text-purple-700 text-[10px] font-mono px-2.5 py-0.5 rounded-full mt-1.5">{r1['period']}</span>
                        </div>
                    </div>
                    
                    <div class="space-y-5">
                        <div>
                            <h4 class="font-outfit text-xs sm:text-sm font-bold text-gray-900 mb-1 flex items-center">
                                <span class="w-1 h-3.5 bg-purple-500 rounded-full mr-2"></span>
                                Quem foi?
                            </h4>
                            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-light">{r1['bio']}</p>
                        </div>
                        <div>
                            <h4 class="font-outfit text-xs sm:text-sm font-bold text-gray-900 mb-1 flex items-center">
                                <span class="w-1 h-3.5 bg-purple-500 rounded-full mr-2"></span>
                                Sua contribuição para as coleções biológicas
                            </h4>
                            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-light">{r1['contribution']}</p>
                        </div>
                        <div>
                            <h4 class="font-outfit text-xs sm:text-sm font-bold text-gray-900 mb-1 flex items-center">
                                <span class="w-1 h-3.5 bg-purple-500 rounded-full mr-2"></span>
                                Por que sua trajetória é importante? / Legado
                            </h4>
                            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-light">{r1['legacy']}</p>
                        </div>
                    </div>
                </div>

                <!-- Researcher 2: Monique Motta -->
                <div class="bg-white border border-gray-150 rounded-2xl p-5 sm:p-7 shadow-sm">
                    <div class="flex flex-col sm:flex-row items-center gap-4 border-b border-gray-100 pb-4 mb-5">
                        <img src="{r2['image_path']}" alt="{r2['name']}" class="w-24 h-32 object-cover rounded-xl shadow-md border border-gray-200" />
                        <div class="text-center sm:text-left">
                            <h3 class="font-outfit text-lg sm:text-xl font-bold text-gray-900">{r2['name']}</h3>
                            <p class="text-xs text-purple-600 font-semibold uppercase tracking-wider mt-0.5">{r2['area']}</p>
                            <span class="inline-block bg-purple-50 text-purple-700 text-[10px] font-mono px-2.5 py-0.5 rounded-full mt-1.5">{r2['period']}</span>
                        </div>
                    </div>
                    
                    <div class="space-y-5">
                        <div>
                            <h4 class="font-outfit text-xs sm:text-sm font-bold text-gray-900 mb-1 flex items-center">
                                <span class="w-1 h-3.5 bg-purple-500 rounded-full mr-2"></span>
                                Quem foi?
                            </h4>
                            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-light">{r2['bio']}</p>
                        </div>
                        <div>
                            <h4 class="font-outfit text-xs sm:text-sm font-bold text-gray-900 mb-1 flex items-center">
                                <span class="w-1 h-3.5 bg-purple-500 rounded-full mr-2"></span>
                                Sua contribuição para as coleções biológicas
                            </h4>
                            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-light">{r2['contribution']}</p>
                        </div>
                        <div>
                            <h4 class="font-outfit text-xs sm:text-sm font-bold text-gray-900 mb-1 flex items-center">
                                <span class="w-1 h-3.5 bg-purple-500 rounded-full mr-2"></span>
                                Por que sua trajetória é importante? / Legado
                            </h4>
                            <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-light">{r2['legacy']}</p>
                        </div>
                    </div>
                </div>
            </div>
            """
        else:
            # Single portrait layout
            portrait_card_html = f"""
            <div class="relative w-full max-w-[280px] mx-auto aspect-[3/4] bg-white/5 border border-white/10 rounded-2xl p-3 shadow-xl backdrop-blur-sm overflow-hidden">
                <div class="absolute inset-0 opacity-5 bg-[radial-gradient(#fff_1px,transparent_1px)] [background-size:16px_16px]"></div>
                <div class="w-full h-full border border-white/20 rounded-xl overflow-hidden relative">
                    <img src="{col['image_path']}" alt="{col['researcher_name']}" class="w-full h-full object-cover rounded-lg" />
                </div>
            </div>
            """
            
            # Single researcher: standard vertical list of 4 sections
            main_content_html = f"""
            <div class="flex flex-col gap-6">
                <!-- Section 1: Biografia -->
                <div class="bg-white border border-gray-150 rounded-2xl p-5 sm:p-7 shadow-sm transition-all hover:border-gray-300">
                    <h3 class="font-outfit text-base sm:text-lg font-bold text-gray-900 border-b border-gray-100 pb-2 mb-4 flex items-center">
                        <span class="w-1.5 h-4 bg-gradient-to-b {col['theme']['bg_gradient']} rounded-full mr-2"></span>
                        1. Quem foi?
                    </h3>
                    <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-light">{col['bio']}</p>
                </div>

                <!-- Section 2: Contribuição -->
                <div class="bg-white border border-gray-150 rounded-2xl p-5 sm:p-7 shadow-sm transition-all hover:border-gray-300">
                    <h3 class="font-outfit text-base sm:text-lg font-bold text-gray-900 border-b border-gray-100 pb-2 mb-4 flex items-center">
                        <span class="w-1.5 h-4 bg-gradient-to-b {col['theme']['bg_gradient']} rounded-full mr-2"></span>
                        2. Sua contribuição para as coleções biológicas
                    </h3>
                    <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-light">{col['contribution']}</p>
                </div>

                <!-- Section 3: Importância -->
                <div class="bg-white border border-gray-150 rounded-2xl p-5 sm:p-7 shadow-sm transition-all hover:border-gray-300">
                    <h3 class="font-outfit text-base sm:text-lg font-bold text-gray-900 border-b border-gray-100 pb-2 mb-4 flex items-center">
                        <span class="w-1.5 h-4 bg-gradient-to-b {col['theme']['bg_gradient']} rounded-full mr-2"></span>
                        3. Por que sua trajetória é importante?
                    </h3>
                    <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-light">{col['importance']}</p>
                </div>

                <!-- Section 4: Legado/Curiosidades -->
                <div class="bg-white border border-gray-150 rounded-2xl p-5 sm:p-7 shadow-sm transition-all hover:border-gray-300">
                    <h3 class="font-outfit text-base sm:text-lg font-bold text-gray-900 border-b border-gray-100 pb-2 mb-4 flex items-center">
                        <span class="w-1.5 h-4 bg-gradient-to-b {col['theme']['bg_gradient']} rounded-full mr-2"></span>
                        4. Curiosidades ou legado
                    </h3>
                    <p class="text-xs sm:text-sm text-gray-700 leading-relaxed font-light">{col['curiosity']}</p>
                </div>
            </div>
            """

        html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{col['researcher_name']} - Coleção {display_acr} | FIOCRUZ SBPC 2026</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        outfit: ['Outfit', 'sans-serif'],
                    }},
                    colors: {{
                        fiocruz: {{
                            blue: '#00529b',
                            gold: '#c59b27',
                            dark: '#0f172a',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .font-outfit {{ font-family: 'Outfit', sans-serif; }}
        body {{
            opacity: 0;
            transition: opacity 0.4s ease-in-out;
        }}
        body.loaded {{
            opacity: 1;
        }}
    </style>
</head>
<body class="bg-slate-50 text-gray-900 font-sans min-h-screen flex flex-col antialiased loaded font-outfit">

    <!-- Top Header Banner (Mobile-ready, large tap targets) -->
    <header class="bg-white border-b border-gray-150 sticky top-0 z-40 shadow-sm font-sans">
        <div class="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <div class="flex items-center gap-2">
                <a href="../index.html" class="inline-flex items-center gap-1.5 text-xs font-bold text-gray-700 hover:text-gray-900 transition-colors uppercase tracking-wider min-h-[44px] px-2 rounded-lg hover:bg-gray-50">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"></path></svg>
                    Portal SBPC
                </a>
                <div class="h-4 w-px bg-gray-200"></div>
                <a href="../programacao.html" class="inline-flex items-center gap-1.5 text-xs font-bold text-gray-700 hover:text-gray-900 transition-colors uppercase tracking-wider min-h-[44px] px-2 rounded-lg hover:bg-gray-50">
                    Programação
                </a>
            </div>
            <div class="flex items-center gap-3.5">
                <span class="text-[10px] font-semibold text-gray-400 font-mono tracking-widest uppercase">{display_acr}</span>
                <div class="h-4 w-px bg-gray-200"></div>
                <img src="../assets/images/Logo_Colecoes.jpg" alt="Coleções Biológicas" class="h-6 w-auto rounded shadow-sm border border-gray-100" />
                <div class="h-4 w-px bg-gray-200"></div>
                <img src="../assets/images/logo_fiocruz.png" alt="Fiocruz" class="h-6 w-auto" />
            </div>
        </div>
    </header>

    <!-- Researcher Hero Section (Mobile-first Layout) -->
    <section class="bg-fiocruz-dark text-white py-10 sm:py-16 relative overflow-hidden">
        <div class="absolute -top-48 -right-48 w-96 h-96 rounded-full bg-gradient-to-br {col['theme']['bg_gradient']} opacity-15 blur-3xl"></div>
        <div class="absolute inset-0 opacity-[0.03] bg-[radial-gradient(#fff_1px,transparent_1px)] [background-size:24px_24px]"></div>
        
        <div class="max-w-6xl mx-auto px-4 sm:px-6 relative z-10">
            <div class="flex flex-col lg:flex-row gap-8 lg:gap-12 items-center">
                
                <!-- Portrait / Illustration -->
                <div class="w-full lg:w-1/3 flex-shrink-0 flex justify-center">
                    {portrait_card_html}
                </div>
                
                <!-- Quick facts & Name -->
                <div class="w-full lg:w-2/3 flex flex-col">
                    <span class="inline-flex items-center gap-1.5 self-start px-2.5 py-0.5 rounded-full text-[9px] font-bold bg-white/10 text-white border border-white/10 uppercase tracking-widest mb-4 font-mono">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                        Homenageada {display_acr}
                    </span>
                    
                    <h1 class="font-outfit text-2xl sm:text-4xl font-extrabold tracking-tight mb-2 leading-tight">{col['researcher_name']}</h1>
                    <p class="text-xs sm:text-base text-gray-300 font-semibold tracking-wide uppercase font-outfit mt-0.5">{col['area']}</p>
                    <p class="text-[10px] text-gray-400 font-mono tracking-wider mt-1 font-sans">{col['collection_name'].replace("CYP_CBAS_CBP", "CYP/CBAS/CBP")} ({display_acr})</p>
                    <div class="w-16 h-1 bg-gradient-to-r {col['theme']['bg_gradient']} rounded mt-3"></div>
                    
                    <!-- Career Timeline Summary -->
                    <div class="mt-4 flex gap-4 text-[10px] font-mono text-gray-300 bg-white/5 border border-white/10 rounded-xl p-3 self-start font-sans">
                        <div>
                            <span class="block text-gray-400 uppercase text-[8px] tracking-wider">Período de atuação</span>
                            <span class="text-xs font-semibold">{col['period']}</span>
                        </div>
                        <div class="w-px bg-white/10"></div>
                        <div>
                            <span class="block text-gray-400 uppercase text-[8px] tracking-wider">Instituição</span>
                            <span class="text-xs font-semibold">Fiocruz / IOC</span>
                        </div>
                    </div>
                    
                    <!-- Quote of researcher -->
                    <p class="mt-6 text-sm sm:text-base italic text-gray-200 border-l-4 {col['theme']['accent_border']} pl-3.5 leading-relaxed font-light font-sans">
                        “{col['quote']}”
                    </p>
                </div>
                
            </div>
        </div>
    </section>

    <!-- Audio Guide (Accessible audio player bar - Static + Sticky Bottom on Mobile) -->
    <div id="audio-container" class="bg-gradient-to-r {col['theme']['bg_gradient']} text-white py-3 shadow-inner relative z-30 font-sans">
        <div class="max-w-6xl mx-auto px-4 flex items-center justify-between gap-4">
            <div class="flex items-center gap-2.5">
                <div class="w-8 h-8 rounded-full bg-white/15 flex items-center justify-center flex-shrink-0">
                    <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"></path></svg>
                </div>
                <div class="overflow-hidden">
                    <span class="text-[9px] font-semibold uppercase tracking-wider block opacity-70 leading-none">Áudio Guia Acessível</span>
                    <span class="text-xs font-bold block truncate mt-0.5">Ouça a trajetória da cientista</span>
                </div>
            </div>
            
            <div class="flex items-center gap-2 font-sans">
                <button onclick="startAudio()" id="play-btn" class="flex items-center gap-1.5 bg-white text-gray-900 text-xs font-bold uppercase tracking-wider px-4 py-2 rounded-full hover:bg-slate-100 active:scale-95 shadow-md min-h-[36px] transition-all">
                    <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"></path></svg>
                    Ouvir
                </button>
                <button onclick="stopAudio()" id="stop-btn" class="hidden flex items-center gap-1.5 bg-black/40 text-white text-xs font-bold uppercase tracking-wider px-4 py-2 rounded-full hover:bg-black/60 active:scale-95 min-h-[36px] transition-all">
                    <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"></path></svg>
                    Pausar
                </button>
            </div>
        </div>
    </div>

    <!-- Main Stacked Content Layout -->
    <main class="max-w-4xl mx-auto px-4 py-8 sm:py-12 flex-grow font-sans">
        
        {main_content_html}

        {videos_html}

        <!-- Inspiring Message Card -->
        <div class="mt-8 bg-gradient-to-br {col['theme']['bg_gradient']} rounded-2xl p-6 sm:p-10 text-white relative overflow-hidden shadow-md">
            <div class="absolute inset-0 opacity-[0.02] bg-[radial-gradient(#fff_1px,transparent_1px)] [background-size:16px_16px]"></div>
            <div class="relative z-10 font-sans">
                <span class="text-[9px] font-mono font-bold tracking-widest text-white/80 uppercase block mb-3">Mensagem Inspiradora ao Visitante</span>
                <p class="font-outfit text-sm sm:text-lg italic leading-relaxed font-light">
                    “{col['message']}”
                </p>
                <div class="mt-4 flex items-center gap-2.5 text-[10px] font-semibold text-white/80">
                    <span class="w-4 h-[1px] bg-white/40"></span>
                    <span>VPPCB Fiocruz • SBPC 2026</span>
                </div>
            </div>
        </div>

    </main>

    <!-- Navigation Hub (Touch target size min-height 44px) -->
    <section class="max-w-4xl mx-auto px-4 pb-12 text-center font-sans flex flex-col items-center justify-center gap-5">
        <img src="../assets/images/colecionarPop.png" alt="Colecionar Pop" class="h-14 sm:h-16 w-auto drop-shadow-sm" />
        <a href="../index.html" class="inline-flex items-center gap-2 bg-slate-900 text-white px-5 py-3 rounded-xl hover:bg-slate-800 transition-all font-bold text-xs uppercase tracking-wider shadow active:scale-95 min-h-[44px]">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
            Outras Homenageadas
        </a>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-950 text-white mt-auto border-t border-slate-900 font-sans">
        <div class="max-w-6xl mx-auto px-4 py-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-[10px] text-gray-500">
            <!-- Logo_Colecoes.jpg included next to VPPCB in individual page footer -->
            <div class="flex items-center gap-4 text-left font-sans">
                <img src="../assets/images/Logo_Colecoes.jpg" alt="Logo Coleções" class="h-14 sm:h-16 w-auto rounded border border-slate-800 shadow-sm" />
                <div class="h-8 w-px bg-slate-800"></div>
                <img src="../assets/images/logo_fiocruz_negativo.png" alt="Fiocruz" class="h-10 sm:h-12 w-auto" />
            </div>
            <div class="text-center sm:text-right">
                <p>© 2026 Fundação Oswaldo Cruz. SBPC 2026 (Niterói/UFF).</p>
            </div>
        </div>
    </footer>

    <!-- TTS Scripting -->
    <script>
        let speechSynth = window.speechSynthesis;
        let speechUtterance = null;
        let isSpeaking = false;

        function startAudio() {{
            if (!speechSynth) {{
                alert("Desculpe, seu navegador não suporta a síntese de voz.");
                return;
            }}

            if (speechSynth.paused && isSpeaking) {{
                speechSynth.resume();
                document.getElementById("play-btn").classList.add("hidden");
                document.getElementById("stop-btn").classList.remove("hidden");
                return;
            }}

            speechSynth.cancel();

            const textToSpeak = "{audio_guide_text_escaped}";
            speechUtterance = new SpeechSynthesisUtterance(textToSpeak);
            speechUtterance.lang = "pt-BR";
            
            const voices = speechSynth.getVoices();
            const ptVoice = voices.find(v => v.lang.startsWith("pt"));
            if (ptVoice) {{
                speechUtterance.voice = ptVoice;
            }}

            speechUtterance.onstart = () => {{
                isSpeaking = true;
                document.getElementById("play-btn").classList.add("hidden");
                document.getElementById("stop-btn").classList.remove("hidden");
            }};

            speechUtterance.onend = () => {{
                resetAudioUI();
            }};

            speechUtterance.onerror = () => {{
                resetAudioUI();
            }};

            speechSynth.speak(speechUtterance);
        }}

        function stopAudio() {{
            if (speechSynth && speechSynth.speaking) {{
                speechSynth.pause();
                document.getElementById("play-btn").classList.remove("hidden");
                document.getElementById("stop-btn").classList.add("hidden");
            }}
        }}

        function resetAudioUI() {{
            isSpeaking = false;
            document.getElementById("play-btn").classList.remove("hidden");
            document.getElementById("stop-btn").classList.add("hidden");
        }}

        window.addEventListener("beforeunload", () => {{
            if (speechSynth) {{
                speechSynth.cancel();
            }}
        }});
        
        if (speechSynth && speechSynth.onvoiceschanged !== undefined) {{
            speechSynth.onvoiceschanged = () => {{}};
        }}
    </script>
</body>
</html>
"""
        
        with open(os.path.join(sub_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated mobile-first page for: {acronym} under {sub_path}/index.html")

# 3. GENERATE PROGRAMACAO PAGE (programacao.html)
def generate_programacao_page():
    schedule_data = [
        {
            "date": "27/07/2026",
            "day": "Segunda-feira",
            "title": "Vigilância, Prevenção e Vetores da Peste no Semiárido",
            "description": "Como as bactérias crescem? Quem são os vetores da peste? Venha descobrir! Nesta atividade, o público poderá explorar modelos didáticos, observar bactérias ao microscópio, conhecer placas de cultura e modelos 3D, além de mergulhar na história da peste no Brasil. Também será possível interagir com materiais utilizados na vigilância em campo, como armadilhas para roedores, EPIs e modelos de pulgas, e conhecer como a ciência contribui para a preservação das coleções de bactérias da Fiocruz.",
            "collections": [
                {"acronym": "CYP/CBAS/CBP", "path": "cyp_cbas_cbp/index.html", "researcher": "Dra. Alzira Maria Paiva de Almeida"}
            ],
            "gradient": "from-orange-600 to-red-800"
        },
        {
            "date": "28/07/2026",
            "day": "Terça-feira",
            "title": "Mundo dos Fungos, Nutrição e Desafios Antifúngicos",
            "description": "Descubra como os fungos podem ser aliados na produção de alimentos, como os queijos Camembert e Roquefort, e conheça também espécies que contaminam alimentos. A atividade reúne modelos didáticos, culturas de fungos e observações ao microscópio para revelar esse universo invisível. Aproveite para explorar o papel dos fungos nas doenças humanas e os desafios da resistência aos antifúngicos. Por meio de modelos interativos, culturas e simulações de testes laboratoriais, descubra como a ciência atua no diagnóstico, tratamento e vigilância dessas infecções.",
            "collections": [
                {"acronym": "CCFF", "path": "ccff/index.html", "researcher": "Pedrina Cunha de Oliveira"},
                {"acronym": "CFAS", "path": "cfas/index.html", "researcher": "Marília Martins Nishikawa"},
                {"acronym": "CFAM", "path": "cfam/index.html", "researcher": "Dra. Maria Inês de Moura Sarquis"}
            ],
            "gradient": "from-rose-600 to-pink-800"
        },
        {
            "date": "29/07/2026",
            "day": "Quarta-feira",
            "title": "Insetos e Vetores: O Fascinante Universo dos Insetos",
            "description": "Descubra o fascinante universo dos insetos! Explore exemplares da coleção científica, observe estruturas ao microscópio, conheça o ciclo de vida desses animais e veja de perto os materiais utilizados pelos pesquisadores para sua coleta e estudo.",
            "collections": [
                {"acronym": "CCER", "path": "ccer/index.html", "researcher": "Dra. Maria Luiza Felippe Bauer"},
                {"acronym": "CCULI", "path": "cculi/index.html", "researcher": "Dras. Teresa Fernandes & Monique Motta"}
            ],
            "gradient": "from-indigo-600 to-purple-800"
        },
        {
            "date": "30/07/2026",
            "day": "Quinta-feira",
            "title": "Anatomia Animal, Histologia e Plantas Medicinais",
            "description": "Explore o universo da anatomia e da botânica por meio de modelos 3D de órgãos, conheça a técnica histológica e descubra o uso das plantas medicinais. Observe estruturas animais e vegetais e entenda como a ciência revela a organização e o funcionamento dos seres vivos.",
            "collections": [
                {"acronym": "CBPM", "path": "cbpm/index.html", "researcher": "Graziela Maciel Barroso"},
                {"acronym": "CEIOC", "path": "ceioc/index.html", "researcher": "Danielle Cerri do Nascimento"},
                {"acronym": "MP", "path": "mp/index.html", "researcher": "Dra. Itália Kerr"}
            ],
            "gradient": "from-emerald-600 to-teal-800"
        },
        {
            "date": "31/07/2026",
            "day": "Sexta-feira",
            "title": "Transmissão Sanitária: Leptospira, Listeria e Schistosoma",
            "description": "Explore uma maquete que ilustra a transmissão das bactérias Leptospira spp. e Listeria spp. e do trematódeo Schistosoma mansoni, agentes etiológicos da leptospirose, da listeriose e da esquistossomose, respectivamente. Descubra o papel dos corpos hídricos na transmissão dessas doenças e conheça a morfologia desses agentes. Você terá a oportunidade de observar Leptospira spp. e Listeria spp. ao microscópio, além de entender melhor porque a leptospirose é conhecida como a 'doença do xixi do rato'. Durante a atividade, você também poderá observar e manusear conchas de diferentes espécies de caramujos, comparando aquelas que participam da transmissão da esquistossomose com outras espécies terrestres e aquáticas.",
            "collections": [
                {"acronym": "CLEP", "path": "clep/index.html", "researcher": "Dra. Martha Maria Pereira"},
                {"acronym": "CMIOC", "path": "cmioc/index.html", "researcher": "Silvana Carvalho Thiengo"}
            ],
            "gradient": "from-amber-600 to-orange-900"
        },
        {
            "date": "01/08/2026",
            "day": "Sábado",
            "title": "Paleoparasitologia, Saúde Histórica e o Ciclo da Leishmania",
            "description": "Viaje ao passado e descubra como a ciência investiga a história da saúde, da alimentação e dos parasitos. Explore amostras da coleção, réplicas de coprólitos em 3D, conheça a técnica de sedimentação de Lutz e observe as diferenças entre vestígios da dieta de animais por meio de modelos e materiais expositivos. Conheça o fascinante ciclo de vida da Leishmania! Observe células infectadas ao microscópio, explore modelos 3D das diferentes fases do parasito e descubra, por meio de imagens ilustrativas, como ele interage com o organismo e causa a leishmaniose.",
            "collections": [
                {"acronym": "CPFERA", "path": "cpfera/index.html", "researcher": "Dra. Niède Guidon"},
                {"acronym": "CLIOC", "path": "clioc/index.html", "researcher": "Selma Quintella Soares"}
            ],
            "gradient": "from-fuchsia-600 to-pink-900"
        }
    ]

    timeline_html = ""
    for item in schedule_data:
        collections_links_html = ""
        for c in item["collections"]:
            collections_links_html += f"""
            <a href="{c['path']}" class="inline-flex items-center gap-2 bg-slate-50 hover:bg-slate-100 border border-gray-200 px-3 py-2 rounded-xl text-xs font-semibold text-gray-800 shadow-sm transition-all hover:border-gray-300 min-h-[40px]">
                <span class="font-mono text-fiocruz-blue font-bold">{c['acronym']}</span>
                <span class="text-[10px] text-gray-400">•</span>
                <span class="text-gray-600 font-normal">{c['researcher']}</span>
                <svg class="w-3 h-3 text-gray-400 ml-1" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"></path></svg>
            </a>
            """

        timeline_html += f"""
        <!-- Day Node -->
        <div class="relative">
            <!-- Timeline dot -->
            <div class="absolute -left-[26px] sm:-left-[42px] top-2.5 w-4 h-4 rounded-full bg-gradient-to-br {item['gradient']} border-4 border-slate-50 shadow-md"></div>
            
            <div class="bg-white border border-gray-150 rounded-2xl p-5 sm:p-7 shadow-sm transition-all hover:shadow-md hover:border-gray-300">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-2 border-b border-gray-100 pb-3 mb-4">
                    <div>
                        <span class="text-[10px] font-mono font-bold text-fiocruz-blue bg-blue-50 px-2.5 py-0.5 rounded-full uppercase tracking-wider">{item['date']}</span>
                        <h3 class="font-outfit text-base sm:text-lg font-bold text-gray-900 mt-1.5">{item['day']}</h3>
                    </div>
                    <span class="text-xs font-semibold text-gray-500 italic md:text-right">{item['title']}</span>
                </div>
                
                <p class="text-xs sm:text-sm text-gray-600 leading-relaxed font-light mb-5">
                    {item['description']}
                </p>
                
                <div class="flex flex-col gap-2">
                    <span class="text-[9px] font-bold text-gray-400 uppercase tracking-widest">Saber mais sobre as Coleções presentes:</span>
                    <div class="flex flex-wrap gap-2">
                        {collections_links_html}
                    </div>
                </div>
            </div>
        </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programação - Coleções Biológicas FIOCRUZ | SBPC Jovem 2026</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                        outfit: ['Outfit', 'sans-serif'],
                    }},
                    colors: {{
                        fiocruz: {{
                            blue: '#00529b',
                            gold: '#c59b27',
                            dark: '#0f172a',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .font-outfit {{ font-family: 'Outfit', sans-serif; }}
        body {{
            opacity: 0;
            transition: opacity 0.4s ease-in-out;
        }}
        body.loaded {{
            opacity: 1;
        }}
    </style>
</head>
<body class="bg-slate-50 text-gray-900 font-sans min-h-screen flex flex-col antialiased loaded font-outfit">

    <!-- Header Section -->
    <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-gray-150 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 sm:h-20 flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-3.5 min-h-[44px]">
                <img src="assets/images/logo_fiocruz.png" alt="Fiocruz" class="h-10 sm:h-12 w-auto" />
                <div class="h-8 w-px bg-gray-200"></div>
                <img src="assets/images/Logo_Colecoes.jpg" alt="Coleções Biológicas" class="h-9 sm:h-11 w-auto rounded shadow-sm border border-gray-100" />
            </a>
            <div class="flex items-center gap-3 sm:gap-6">
                <a href="index.html" class="text-xs sm:text-sm font-bold text-gray-700 hover:text-fiocruz-blue transition-colors flex items-center gap-1.5 min-h-[40px] px-2 rounded-lg hover:bg-gray-50 font-sans">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
                    Portal Homenagens
                </a>
                <span class="bg-blue-50 text-blue-700 border border-blue-100 rounded-full text-[9px] sm:text-xs font-semibold px-2.5 py-0.5 sm:px-3 sm:py-1 uppercase tracking-wider font-sans font-sans">SBPC 2026</span>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="relative bg-fiocruz-dark text-white py-12 sm:py-16 overflow-hidden">
        <div class="absolute -top-40 -right-40 w-96 h-96 rounded-full bg-blue-500/10 blur-3xl"></div>
        <div class="absolute -bottom-40 -left-40 w-96 h-96 rounded-full bg-emerald-500/10 blur-3xl"></div>
        
        <div class="max-w-4xl mx-auto px-4 text-center relative z-10 font-sans">
            <!-- colecionarPop logo next to Title in schedule hero -->
            <img src="assets/images/colecionarPop.png" alt="Colecionar Pop" class="mx-auto h-20 sm:h-24 w-auto mb-4 drop-shadow-md" />
            <span class="inline-block bg-fiocruz-gold/20 text-fiocruz-gold border border-fiocruz-gold/30 rounded-full text-[10px] sm:text-xs font-bold px-3 py-1 uppercase tracking-widest mb-3 font-outfit">SBPC Jovem 2026</span>
            <h2 class="font-outfit text-2xl sm:text-4xl font-extrabold tracking-tight mb-2 leading-tight">
                Programação de Atividades
            </h2>
            <p class="text-xs sm:text-base text-gray-300 font-light max-w-xl mx-auto leading-relaxed">
                Confira a programação diária e as atividades das Coleções Biológicas da Fiocruz na SBPC Jovem (UFF/Niterói).
            </p>
        </div>
    </section>

    <!-- Timeline Content -->
    <main class="max-w-3xl mx-auto px-4 py-10 sm:py-16 flex-grow w-full font-sans">
        <div class="flex flex-col gap-8 relative border-l-2 border-gray-200 pl-6 sm:pl-8 ml-2 sm:ml-4">
            {timeline_html}
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white mt-auto border-t border-gray-800 text-sm font-sans">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-6">
                <!-- Logo_Colecoes.jpg included next to VPPCB in footer -->
                <div class="flex items-center gap-4">
                    <img src="assets/images/Logo_Colecoes.jpg" alt="Logo Coleções" class="h-14 sm:h-16 w-auto rounded border border-gray-800 shadow-sm" />
                    <div class="h-8 w-px bg-gray-800"></div>
                    <img src="assets/images/logo_fiocruz_negativo.png" alt="Fiocruz" class="h-10 sm:h-12 w-auto" />
                </div>
                <div class="flex gap-4 text-xs text-gray-400">
                    <a href="https://fiocruz.br" target="_blank" class="hover:text-white transition-colors">Portal Fiocruz</a>
                    <a href="https://sbpc.uff.br/" target="_blank" class="hover:text-white transition-colors">SBPC 2026</a>
                </div>
            </div>
            <div class="border-t border-gray-800 mt-6 pt-6 text-center text-[11px] text-gray-500 flex flex-col sm:flex-row justify-between items-center gap-2">
                <p>© 2026 Fundação Oswaldo Cruz. Desenvolvido para a SBPC 2026 (Niterói/UFF).</p>
                <p class="italic">Reconhecendo trajetórias que inspiram a ciência.</p>
            </div>
        </div>
    </footer>

</body>
</html>
"""
    
    with open(os.path.join(workspace_dir, "programacao.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Generated responsive program schedule (programacao.html)")

if __name__ == "__main__":
    generate_home_page()
    generate_individual_pages()
    generate_programacao_page()
    print("All mobile-responsive pages successfully rebuilt!")
