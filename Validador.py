class Validadores:
    @staticmethod
    def validar_numeros(novo_valor):
        if novo_valor.isdigit():
            numero = int(novo_valor)
            return 1 <= numero <= 20
        return novo_valor == ""
