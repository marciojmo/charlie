import random
import intents

greetings = [
    """Olá, {0}. Eu sou o Charlie, seu bot de utilidades. \n\nAtualmente posso lhe dizer a sorte do dia, te dar um empurrãozinho para ir treinar ou um versículo bíblico!\n\nComo posso ser útil?"""
]

daily_fortunes = [
    "Algo maior do que você imagina está para acontecer.",
    "A resposta que você busca pode estar mais próxima do que pensa.",
    "Grandes transformações começam com pequenos passos.",
    "A vida está conspirando a seu favor, mesmo em silêncio.",
    "Seus esforços estão sendo notados pelo universo.",
    "O que parecia confusão é apenas o começo de uma nova ordem.",
    "A paz começa quando você solta o que não pode controlar.",
    "Cada manhã traz novas possibilidades — aproveite.",
    "Existe um tempo certo para tudo, confie no processo.",
    "Você já está mais perto do que imagina.",
    "A calmaria de hoje prepara você para as conquistas de amanhã.",
    "Algo bom está em movimento e vai te encontrar.",
    "Seu caminho está se abrindo, mesmo que você ainda não veja.",
    "O inesperado de hoje será a história que você contará com orgulho.",
    "Quando tudo parecer parado, é porque algo está se alinhando.",
    "A mudança que você precisa começa dentro de você.",
    "Você está no ritmo certo, siga em frente.",
    "O mundo está cheio de possibilidades esperando por você.",
    "O que é verdadeiro permanece, mesmo com o tempo.",
    "O que é seu não precisa ser forçado, ele virá naturalmente.",
    "Permita-se recomeçar sempre que precisar.",
    "A próxima página da sua história será mais leve.",
    "Tudo que você precisa já está em você.",
    "A coragem de hoje trará recompensas amanhã.",
    "Mesmo sem ver, o caminho está sendo preparado.",
    "Boas notícias estão vindo em sua direção.",
    "Alguém pensa em você com carinho neste exato momento.",
    "Seu brilho não depende da opinião dos outros.",
    "O tempo vai mostrar que tudo fez sentido.",
    "Permaneça firme, algo lindo está nascendo aí dentro.",
    "A vida sempre dá um jeito de surpreender para o bem.",
    "Cada desafio é um convite ao crescimento.",
    "Você já superou o que achava impossível — continue.",
    "A sua jornada tem um propósito maior do que imagina.",
    "Sinais aparecem para quem está atento.",
    "Às vezes, tudo o que você precisa é respirar fundo.",
    "O universo te reserva encontros incríveis.",
    "Você é mais forte do que pensa e mais amado do que sabe.",
    "Não tenha pressa, o que é seu vai chegar no tempo certo.",
    "Confie na jornada, mesmo quando o caminho parecer estranho.",
    "Pequenas alegrias constroem grandes felicidades.",
    "Algumas pausas são bênçãos disfarçadas.",
    "Você tem tudo para fazer dar certo.",
    "A energia que você transmite volta para você — espalhe o bem.",
    "Você é luz, mesmo nos dias nublados.",
    "A sua intuição sabe o caminho — escute com atenção.",
    "Hoje é um bom dia para acreditar em si mesmo.",
    "Tudo que você planta com amor, florescerá.",
    "A vida retribui quem segue com o coração leve.",
    "Algo que parecia distante começa a se aproximar.",
    "Você não está perdido, está em construção.",
    "Há beleza mesmo nos momentos de espera.",
    "O silêncio às vezes é só um sinal de que algo maior está por vir.",
    "Você está exatamente onde precisa estar para crescer.",
    "Novos ventos trarão boas oportunidades.",
    "Você está sendo guiado por algo maior do que entende.",
    "Seu caminho será iluminado por dentro pra fora.",
    "Coisas boas acontecem quando você escolhe a leveza.",
    "Sinta o agora — ele está cheio de respostas.",
    "A vida está pronta para te surpreender hoje.",
    "A luz que você procura está em você.",
    "Aceitar o que é também é um passo de coragem.",
    "Tudo muda quando você muda por dentro.",
    "Você é capaz de escrever uma nova história a qualquer momento.",
    "Hoje é um convite para recomeçar com mais amor.",
    "Seu valor não depende das circunstâncias.",
    "A sorte favorece quem age com fé e gentileza.",
    "As coisas certas encontram quem está em paz.",
    "Deixe espaço para o inesperado — ele pode ser incrível.",
    "O que parece fim pode ser só um belo começo.",
    "Algo extraordinário se esconde nas coisas simples.",
    "Você é semente de futuro — cuide de si com carinho.",
    "O universo entende sua vibração melhor que suas palavras.",
    "Permita-se florescer onde estiver.",
    "O seu melhor está em construção — não desista agora.",
    "Coisas boas chegam para quem mantém o coração aberto.",
    "Seus sonhos importam — e estão sendo ouvidos.",
    "O tempo cura, transforma e ensina. Confie nele.",
    "Tudo flui melhor quando você solta o controle.",
    "Você é mais especial do que imagina.",
    "O que você busca também está te buscando.",
    "Seja gentil consigo mesmo — você está fazendo o melhor que pode.",
    "A simplicidade carrega grandes respostas.",
    "Hoje é um ótimo dia para deixar o passado no passado.",
    "Você é protagonista da sua história.",
    "Acredite: ainda há magia nos detalhes do cotidiano.",
    "Toda estação tem sua beleza — até as mais difíceis.",
    "Você está no caminho certo, mesmo que pareça lento.",
    "A serenidade é sinal de sabedoria interior.",
    "Permaneça firme: coisas boas levam tempo.",
    "As respostas vêm para quem continua caminhando.",
    "Seu coração já conhece o próximo passo.",
    "Nada é por acaso, tudo tem um porquê.",
    "A leveza é uma escolha possível todos os dias.",
    "Sinta orgulho de cada passo que já deu.",
    "Tudo que é verdadeiro encontra um jeito de permanecer.",
    "Hoje pode ser o começo de algo inesquecível.",
    "A sua presença já é uma bênção para o mundo.",
    "Onde há verdade, há caminho.",
    "Respire fundo — há beleza até no caos.",
    "Cada amanhecer traz a chance de renascer por dentro.",
    "Você já tem tudo o que precisa para ser feliz agora.",
    "Confie: a vida sabe exatamente o que está fazendo com você.",
]

bible_verse = [
    "O Senhor é o meu pastor, nada me faltará. – Salmos 23:1",
    "Posso todas as coisas naquele que me fortalece. – Filipenses 4:13",
    "O choro pode durar uma noite, mas a alegria vem pela manhã. – Salmos 30:5",
    "Entrega o teu caminho ao Senhor; confia nele, e ele tudo fará. – Salmos 37:5",
    "Deus é o nosso refúgio e fortaleza. – Salmos 46:1",
    "A fé é a certeza do que se espera. – Hebreus 11:1",
    "Não temas, porque eu sou contigo. – Isaías 41:10",
    "Clama a mim, e responder-te-ei. – Jeremias 33:3",
    "Aquele que habita no esconderijo do Altíssimo descansará à sombra do Onipotente. – Salmos 91:1",
    "Em paz me deito e logo adormeço. – Salmos 4:8",
    "Deleita-te também no Senhor. – Salmos 37:4",
    "Tudo tem o seu tempo determinado. – Eclesiastes 3:1",
    "Confia no Senhor de todo o teu coração. – Provérbios 3:5",
    "O Senhor é minha luz e minha salvação. – Salmos 27:1",
    "O meu socorro vem do Senhor. – Salmos 121:2",
    "Sede fortes e corajosos. – Deuteronômio 31:6",
    "Em todo o tempo ama o amigo. – Provérbios 17:17",
    "Alegrai-vos na esperança, sede pacientes na tribulação. – Romanos 12:12",
    "O Senhor pelejará por vós. – Êxodo 14:14",
    "A minha graça te basta. – 2 Coríntios 12:9",
    "Guardei a tua palavra no meu coração. – Salmos 119:11",
    "O justo viverá pela fé. – Romanos 1:17",
    "Bendize, ó minha alma, ao Senhor. – Salmos 103:1",
    "O Senhor firma os passos do homem bom. – Salmos 37:23",
    "O Senhor está perto de todos os que o invocam. – Salmos 145:18",
    "Buscai primeiro o reino de Deus. – Mateus 6:33",
    "No amor não há medo. – 1 João 4:18",
    "Cantai ao Senhor, bendizei o seu nome. – Salmos 96:2",
    "Regozijai-vos sempre. – 1 Tessalonicenses 5:16",
    "Aquele que começou boa obra em vós a completará. – Filipenses 1:6",
    "Paz vos deixo, a minha paz vos dou. – João 14:27",
    "Confiarei e não temerei. – Isaías 12:2",
    "Batalha o bom combate da fé. – 1 Timóteo 6:12",
    "O amor jamais acaba. – 1 Coríntios 13:8",
    "Esforça-te, e tem bom ânimo. – Josué 1:9",
    "Aquele que tem o Filho tem a vida. – 1 João 5:12",
    "O Senhor me sustenta. – Salmos 3:5",
    "Se Deus é por nós, quem será contra nós? – Romanos 8:31",
    "O Senhor é bom, um refúgio em tempos de angústia. – Naum 1:7",
    "O Senhor reina. – Salmos 93:1",
    "Amarás o teu próximo como a ti mesmo. – Mateus 22:39",
    "A palavra do Senhor é reta. – Salmos 33:4",
    "O Senhor te guardará de todo mal. – Salmos 121:7",
    "Tudo coopera para o bem daqueles que amam a Deus. – Romanos 8:28",
    "Deus é amor. – 1 João 4:8",
]

workout_motivation = [
    "O treino que você faz hoje também é para envelhecer com qualidade.",
    "Essa preguiça que tá sentindo agora nunca vai passar, você tem que ir com preguiça mesmo, lá no treino melhora.",
    "Vai hoje só pra fazer uns minutinhos de esteira. O importante é não parar.",
    "BORAAAAA!!! HORA DO SHOWWWW, P****!!",
    "Você nunca vai se arrepender de ter ido, só de ter faltado.",
    "Um treino fofo vale mais do que treino nenhum.",
    "Levantar, me arrumar, não pensar, ir treinar.",
    "Não dá para outra pessoa ir à academia por você.",
    "Levanta, coloca a roupa e vai. Não quero saber de desculpa hoje!",
    "Seu corpo merece esse cuidado.",
    "Tem um monte de gente que adoraria ter a oportunidade de se exercitar e você quer ficar ai dando desculpa.",
    "Não pense, só vá.",
    "Descanse se precisar. Lá na academia, faz pouquinho, de leve, não precisa de muito, vai dar certo!",
    "Só mais um passo.",
    "Treinar não é castigo, é um presente. Aproveite que você PODE!",
    "Você não precisa treinar pesado, você só precisa ir.",
    "Cuide da sua saúde MELHOR do que cuida do seu trabalho.",
    "Já parou para pensar que tem um monte de gente querendo faltar e perder hoje? Poucos são os que vão e vencem. A qual grupo você quer pertencer?",
]

unavailable_answers = [
    "Não consigo responder a isso.",
    "Essa solicitação está fora do que consigo fazer por enquanto.",
    "Desculpe, não posso ajudar com isso no momento.",
]


def get_chit_chat_answer(intent):
    intent_to_textbases = {
        intents.IntentTypes.GREETINGS: greetings,
        intents.IntentTypes.DAILY_FORTUNE: daily_fortunes,
        intents.IntentTypes.PRAYER: bible_verse,
        intents.IntentTypes.WORKOUT_MOTIVATION: workout_motivation,
        intents.IntentTypes.OTHER: unavailable_answers,
    }
    return random.choice(intent_to_textbases[intent])
