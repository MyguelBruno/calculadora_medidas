from dataclasses import dataclass

@dataclass
class Medidas:
  largura: float
  altura: float
  valor_por_metro: float

  def calcular_metro_quadrado(self) -> float:
    return self.largura * self.altura
  
  def calcular_valor_total(self):
    metros_quadrados = self.calcular_metro_quadrado()

    return metros_quadrados * self.valor_por_metro

@dataclass
class Info:
  desc_trabalho: str
  tel_cliente: str

  def info_exibir(self)-> str:
    return self.desc_trabalho, self.tel_cliente