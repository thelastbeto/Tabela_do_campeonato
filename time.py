from modelos.avaliacao import Avaliacao

class Time:
    
    times = []
    posicao = list(range(1, 21))
    
    def __init__(self, _nome, _vitorias,_gols):
        
        self._nome = _nome.title()
        self._vitorias = _vitorias
        self._gols = _gols
        self._rebaixado = False
        self._classificado = False
        self._avaliacao = []
        Time.times.append(self)
    
# print(dir(t1)) # verificando os métodos especiais disponíveis
# print(vars(t2)) # Verificando os atributos do método
    
    def __str__(self):
        return f'{self._nome} | {self._vitorias} | {self._gols}'
    
    @classmethod
    def posicao_time(cls):
        cls.times.sort(key=lambda time: (time._vitorias,time._gols), reverse=True)
        
    
    @classmethod
    def listar_times(cls):
        
        # Ordenando os times por vitórias:
        cls.posicao_time()
        
        # Atribuindo status de classificação e rebaixamento
        
        for i, time in enumerate(cls.times):
            if i < 4:
                time._classificado = True
            elif i >= 16:
                time._rebaixado = True
        
        print(f'{'Posição'.ljust(25)} | {'Nome do Time'.ljust(25)} | {'Vitorias'.ljust(25)} | {'Gols Marcados'.ljust(25)} | {'Avaliação dos Torcedores'.ljust(25)} | {'Status'} ')
        print('-' * 150)
        for i, time in enumerate(cls.times, start=1):
            status = "Classificado" if time._classificado else "Rebaixado" if time.rebaixado else "Neutro"
            print(f'{str(i).ljust(25)} | {time._nome.ljust(25)} | {str(time._vitorias).ljust(25)} | {str(time._gols).ljust(25)} |  {str(time.media_avaliacao).ljust(25)} | {status}')
            #   for time in cls.times(Time.times, start=1):
            #status = "Classificado" if time.classificado else "Rebaixado" if time.rebaixado else ""
            #print(f'{time._nome.ljust(25)} | {str(time._vitorias.ljust(25))} | {str(time.media_avaliacao).ljust(25)} | {time._rebaixado}')  
                     
    @property
    def rebaixado(self): 
        return self._rebaixado
        #return f'O {self._nome} está classificado para o campeonato continental' if self._classificado == True else f'O {self._nome} está rebaixado'
    
    def classificado(self):
        self._classificado

    def receber_avaliacao(self, cliente, nota):
        if nota > 0 and nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        elif nota > 5 and nota <= 10:
            nota_dividida = nota / 2
            avaliacao = Avaliacao(cliente, nota_dividida)
            self._avaliacao.append(avaliacao)

                 
    @property   
    def media_avaliacao(self):
        if not self._avaliacao:
            return f'O time {self._nome} não possui avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    
        


# Problemas:
# Não foi ordenado com base nas vitórias
# falta colher a avaliação dos torcedores