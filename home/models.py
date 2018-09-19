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
	
	cliente = models.ForeignKey(Cliente,null = True, blank=False, on_delete = models.CASCADE)	
	sala = models.ForeignKey(Sala,null = True, blank=False, on_delete = models.CASCADE)	
	
	def __str__(self):
		return self.status		
	
	
class Agenda (models.Model):
	dataEntrada = models.DateTimeField()
	dataSaida = models.DateTimeField()
	status = models.IntegerField()
	
	pedido = models.ForeignKey(Pedido,null = True, blank=False, on_delete = models.CASCADE)
	sala = models.ForeignKey(Sala,null = True, blank=False, on_delete = models.CASCADE)
	
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
		
