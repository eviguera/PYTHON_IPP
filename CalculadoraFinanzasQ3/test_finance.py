#
# creamos el menu
def main():

    #creamos un diccionario para almacenar cuentas
    accounts = []
    create_account = []
    
    while True: 
       print(" Bienvenidosala calculada ")
       print("1. crear cuenta")
       print("2. Agregar transaccion")
       print("3. Consultar Saldo ")
       print("4. Consultar el saldo total")
       print("5. salir")
    # capturar la opcion de entrada
       option = int(input("Ingresela opcion deseada: "))
       if option == 1:
           name = input("Ingrese el nombre de la cuenta: ")
           account_type = input("Ingrese el tipo de cuenta: ")
           account_id = create_account(accounts, name, account_type)
           print(f"cuenta '{name}' creada con el id {account_id}")

       elif option == 2:
           account_id = int(input("Ingerese el id de la cuenta: "))
           add_transaction(accounts, account_id, amount)
           amount = float(input("Ingrese el monto dela transaccion: "))
           description =  input("Ingrese la descripcion de la transaccion: ")
           print(f"Transaccion de {amount} realizada en la cuenta {account_id}")
        
        #consultar saldo de cuenta
       elif option == 3:
            account_id = int(input("ingrese el id de la cuenta"))
            balance = get_acount_balance(accounts,account_id)
            print(f"El saldo de la cuenta {account_id} es {balance}")

        # consultar saldo total cuenta
       elif option == 4:
            tota_balance = get_total_balance(accounts)
            print(f"El saldo total de las cuentas es {tota_balance}")
                    
    
       elif option == 5:
           print(" Gracias por usar la calculadora")
           #salimos del ciclo
           break
       
       
       

       

        

           


    


   

