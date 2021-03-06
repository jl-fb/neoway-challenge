class UF_Infos:
    def __init__(self):
        self.id: '' 
        self.localidade = ''
        self.faixaCep = '' 
        self.situacao = ''
        self.tipoFaixa = ''
    
    def __repr__(self):
        try:
#             return {'UF': '%s', 'faixa_cep_UF': '%s',  'localidade': '%s', 'faixa_cep_localidade': '%s', 'situacao': '%s', 'tipoFaixa': '%s'} % (self.uf, self.faixaCepUF, self.localidade, self.faixaCepLocalidade, self.situacao, self.tipoFaixa)
            return {'id':self.id ,'localidade': self.localidade, 'faixaCep': self.faixaCep, 'situacao': self.situacao, 'tipoFaixa': self.tipoFaixa}
        
        except Exception as error:
            print(f'[UF_Infos_class] Error {error}')
            
    def __out__(self):
        try:
            return self.localidade, self.faixaCep, self.situacao, self.tipoFaixa
    
        except Exception as error:
            print(f'[UF_Infos_class] Error {error}')