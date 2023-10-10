import sys

class Cajero:
    monto = 50000
    print('Bienvenido!\n')
    
    def ingresar_pin(self):
        self.pin = int(input("Ingrese su numero de pin: "))
        if(self.pin >= 1000 and self.pin <= 9999):
            pass
        else:
            print("\nSu pin es invalido. Intentelo nuevamente\n")
            self.ingresar_pin()
        
    
    def operaciones(self):
        self.opciones = int(input(f'''---------------------------------------
        Bienvenido n° pin: {self.pin}
        INDIQUE LA OPERACION A REALIZAR:
        1. CONSULTAR SALDO
        2. DEPÓSITO
        3. RETIRO DE DINERO
        4. SALIR\n'''))
        
        self.control = 0
        while self.control == 0:
            if self.opciones == 1:
                self.consulta_balance()
            elif self.opciones == 2:
                self.depositar()
            elif self.opciones == 3:
                self.retirar()
            elif self.opciones == 4:
                self.salir()
            else:
                print("Opción inválida. Intentelo nuevamente.\n")
                self.operaciones()
                
    def consulta_balance(self):
        print(f'\nSu saldo disponible es: {self.monto}')
        print("Desea realizar otra operación?\n")
        self.operaciones()
    
    def depositar(self):
        deposito = input("Ingrese el monto de su depósito: ")
        if int(deposito) % 1000 == 0:
            self.monto += int(deposito)
            self.consulta_balance()
            print("Desea realizar otra operacion?\n")
            self.operaciones()
        else:
            print("Cantidad de efectivo inválida. Intentelo nuevamente\n")
            self.depositar()
    
    def retirar (self):
        self.retiro = int(input("Ingrese el monto a retirar en multiplos de 1000.\n"))
        if self.retiro > self.monto:
            print("Fondos insuficientes. Intente colocar una cantidad diferente.\n")
            self.retirar()
        else:
            if self.retiro % 1000 == 0:
                self.monto -= self.retiro
                self.consulta_balance()
            else:
                print("Cantidad de efectivo inválida. Intentelo nuevamente\n")
                self.retirar()
        
    def salir(self):
        print("Le deseamos un buen dia. Hasta luego.")
        sys.exit()
    
cajero = Cajero()

cajero.ingresar_pin()
cajero.operaciones()