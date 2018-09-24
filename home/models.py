from django.db import models

# Create your models here

class TipoSala(models.Model):
    tipo = models.CharField(max_length=15)

    def __str__(self):
        return self.tipo
		
class Cliente(models.Model):
	cnpj = models.IntegerField()
	inscricaoestadual = models.IntegerField()
	nome = models.CharField(max_length=30)
	email = models.EmailField(max_length=254, blank = False)
	user = models.CharField(max_length = 50)
	senha = models.CharField(max_length=200)
		
	
	def __str__(self):
		return self.nome

class Condicao(models.Model):
	condicao = models.CharField(max_length=15)
	def __str__(self):
		return self.condicao		
		
class Sala(models.Model):
	nome = models.CharField(max_length=30)
	capacidade = models.IntegerField()
	status = models.ForeignKey(Condicao, null=True, blank=True, on_delete=models.CASCADE)
	tipo = models.ForeignKey(TipoSala, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome		
		
class Pedido (models.Model):
	status = models.SmallIntegerField()
	datapedido = models.DateTimeField()
	dataagenda = models.DateTimeField()
	
	cliente = models.ForeignKey(Cliente,null = True, blank=False,  on_delete=models.CASCADE)	
	sala = models.ForeignKey(Sala,null = True, blank=False, on_delete=models.CASCADE)	
	
	def __str__(self):
		return self.status		
	
	
class Agenda (models.Model):
	dataEntrada = models.DateTimeField()
	dataSaida = models.DateTimeField()
	status = models.IntegerField()
	
	pedido = models.ForeignKey(Pedido,null = True, blank=False, on_delete=models.CASCADE)
	sala = models.ForeignKey(Sala,null = True, blank=False, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.dataEntrada
		
class Contato (models.Model):
	ddd = models.SmallIntegerField()
	telefone = models.IntegerField()
	tipo = models.CharField(max_length = 20)
	
	cliente = models.ForeignKey(Cliente,null = True, blank=False, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.ddd+self.telefone
	
class Endereco (models.Model):
	endereco = models.CharField(max_length = 100)
	numero = models.IntegerField()
	cidade = models.CharField(max_length = 80)
	estado = models.CharField(max_length = 80)
	logradouro = models.CharField(max_length = 20)
	cep = models.IntegerField()	
	bairro = models.CharField(max_length=50)
	
	cliente = models.ForeignKey(Cliente,null = True, blank=False, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.endereco
	
class MediaCliente(models.Model):
	site = models.CharField(max_length=40, null=True)
	foto = models.ImageField(upload_to='clients_photos', null=True, blank=True)
	
	cliente = models.ForeignKey(Cliente,null = True, blank=False, on_delete = models.CASCADE)

	def __str__(self):
		return self.site	
		
class Consulta_Agenda (models.Model):
	dataconsultada = models.DateTimeField(auto_now_add=True)
	dataRequisitada = models.DateTimeField()
		
	cliente = models.ForeignKey(Cliente,null = True, blank=False, on_delete = models.CASCADE)
	agenda = models.ForeignKey(Agenda,null = True, blank=False, on_delete = models.CASCADE)
	
	def __str__(self):
		return [self.cliente,self.agenda,self.datarequisitada]

		
class Servicos(models.Model):
    tiposervico = models.CharField(max_length=20)

    def __str__(self):
        return self.tiposervico
		
class Perfil(models.Model):
    perfil = models.CharField(max_length=50)

    def __str__(self):
        return self.Pefil
		
class Pagamento (models.Model):
	datapagamento = models.DateTimeField()
	valor = models.FloatField()
	formaPagamento = models.CharField(max_length = 100)
	status = models.CharField()
	
	cliente = models.ForeignKey(Cliente, blank=False,null = False,  on_delete=models.CASCADE)
	pedido = models.ForeignKey(Pedido, blank=False, null = False,  on_delete=models.CASCADE)

	def __str__(self):
		return self.status
		
class Usuario (models.Model):
	nome = models.CharField(max_length = 100)
	login = models.CharField(max_length = 50)
	
	perfil = models.ForeignKey(Perfil, blank= False, null = False,  on_delete=models.CASCADE )
	
	def __str__(self):
		return self.nome

class Reserva(models.Model):
	entrada = models.DateTimeField()
	saida = models.DateTimeField()
	descricaoReserva = models.CharField(max_length = None, null = True)

	pedido = models.ForeignKey(Pedido, blank=True,null = False,  on_delete=models.CASCADE)
	
	def __str__(self):
		return self.entrada
		
class Boleto(models.Model):
	vencimento = models.DateTimeField()
	valor = models.FloatField()
	taxa = models.FloatField()
	codigobarra = models.CharField(max_length=None)
	
	cliente = models.ForeignKey(Cliente, blank=False, null = False,  on_delete=models.CASCADE)
		
	def __str__(self):
		return self.vencimento
class Item (models.Model):
	nome = models.CharField(max_length = None)
	valor = models.FloatField()
	
	def __str__(self):
		return self.nome
class Evento(models.Model):
	titulo = models.CharField(max_length = None)
	tipo = models.CharField(max_length = None)
	
	reserva = models.ForeignKey(Reserva, blank = False, null = True,  on_delete=models.CASCADE)
	
	def __str__(self):
		return self.titulo

		
class ItensEvento(models.Model):
	item = models.ForeignKey(Item, blank= False, on_delete=models.CASCADE)
	evento = models.ForeignKey(Evento, blank = False, on_delete=models.CASCADE)
	
	def __str__(self):
		return [self.item,self.evento]
	
class Arquivo(models.Model):
	local = models.CharField(max_length = None)
	titulo = models.CharField(max_length = 30)
	formato = models.CharField(max_length = 10)	
	
	evento = models.ForeignKey(Evento, blank = None,null = False,  on_delete=models.CASCADE)
	
	def __str__(self):
		return self.titulo
		
class Orcamento(models.Model):
	valor = models.FloatField()
	datageracao = models.DateTimeField()
	
	pedido = models.ForeignKey(Pedido,blank = False, null = False,  on_delete=models.CASCADE)
