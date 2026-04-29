from django.db import models
from leiloes.models import Leilao
from datetime import date
from django.db.models import signals
from django.utils.text import slugify
from django.dispatch import receiver


class Imovel(models.Model):
    leilao = models.ForeignKey(Leilao, on_delete=models.CASCADE)
    matricula = models.CharField(
        "Matrícula",
        max_length=100,
        help_text="Número da matrícula do imóvel no cartório de registro de imóveis",
    )
    cep = models.CharField("CEP", max_length=9)
    logradouro = models.CharField("Rua/Avenida", max_length=200)
    numero = models.CharField("Número", max_length=10)
    complemento = models.CharField("Complemento", max_length=100, blank=True)
    bairro = models.CharField("Bairro", max_length=100)
    cidade = models.CharField("Cidade", max_length=100)
    estado = models.CharField("Estado", max_length=2)
    latitude = models.FloatField("Latitude", null=True, blank=True)
    longitude = models.FloatField("Longitude", null=True, blank=True)
    TIPO_IMOVEL_CHOICES = [
        ("casa", "Casa"),
        ("apto", "Apartamento"),
        ("terreno", "Terreno"),
        ("comercial", "Ponto Comercial"),
    ]
    tipo = models.CharField(
        "Tipo",
        max_length=20,
        choices=TIPO_IMOVEL_CHOICES,
        blank=True,
        null=True,
        help_text="Tipo do imóvel (casa, apartamento, terreno, ponto comercial)",
    )
    area = models.FloatField(
        "Área em m²", help_text="Área do imóvel em metros quadrados"
    )
    ESTADO_CONSERVACAO = [
        ("ruim", "Ruim"),
        ("regular", "Regular"),
        ("bom", "Bom"),
        ("otimo", "Ótimo"),
        ("novo", "Novo"),
        ("demolido", "Demolido"),
    ]
    estado_conservacao = models.CharField(
        "Estado de Conservação",
        max_length=50,
        choices=ESTADO_CONSERVACAO,
        help_text="Estado de conservação do imóvel",
    )
    SITUACAO_JURIDICA_CHOICES = [
        ("alienacao", "Alienação"),
        ("penhora", "Penhora"),
        ("inventário", "Inventário"),
        ("usucapiao", "Usucapião"),
        ("hipoteca", "Hipoteca"),
        ("outros", "Outros"),
    ]
    situacao_juridica = models.CharField(
        "Situação Jurídica",
        max_length=50,
        choices=SITUACAO_JURIDICA_CHOICES,
        help_text="Situação jurídica do imóvel",
    )
    image_imovel = models.ImageField(
        "Imagem do Imóvel", upload_to="imoveis/", blank=True, null=True
    )
    slug = models.SlugField(
        "Slug", max_length=100, blank=True, null=True, editable=False
    )

    def __str__(self):
        return self.matricula

    def custo_total(self):
        aquisicao = sum(c.valor for c in self.custoaquisicao_set.all())
        reforma = sum(r.valor_real or 0 for r in self.custoreforma_set.all())
        return aquisicao + reforma

    def dias_parado(self):
        if hasattr(self, "data_aquisicao"):
            return (date.today() - self.data_aquisicao).days
        return 0

    def custo_holding_total(self):
        return sum(h.custo_total() for h in self.custoholding_set.all())

    def custo_por_dia(self):
        dias = self.dias_parado()
        if dias == 0:
            return 0
        return self.custo_holding_total() / dias

    def alerta_holding(self):
        custo = self.custo_holding_total()

        if custo > 10000:
            return "CRÍTICO"
        elif custo > 5000:
            return "ALTO"
        elif custo > 2000:
            return "MODERADO"
        return "OK"

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"


@receiver(signals.pre_save, sender=Imovel)
def gerar_slug_imovel(sender, instance, **kwargs):
    """Gera o slug automaticamente antes de salvar o imóvel"""
    if not instance.slug and instance.matricula:
        # Gera um slug a partir da matrícula. Se o ID já existir, adiciona-o para garantir unicidade.
        base_slug = slugify(instance.matricula)
        instance.slug = f"{base_slug}-{instance.id}" if instance.id else base_slug
