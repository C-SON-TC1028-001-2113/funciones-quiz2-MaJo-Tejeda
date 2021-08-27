# Escribe tus funciones abajo de esta línea


    # Escribe tu código abajo de esta línea
    def pies_cm(picm)
        picm=n*30.48
        
        return picm
    
    def pulgadas_cm(pucm)
        pucm=n*2.54
        
        return pucm
        
    def yardas_cm(ycm)
        ycm=91.44

        return ycm
        
def main():        
        
     print("1. pies a cm, 2. pulgadas a cm, 3. yardas a cm")) 
     x=int(input("Introduce una opcion: ") 
           
    if x=1: 
        n=int(input("Introduce la cantidad: ") 
        if n>0        
        totalpicm=pies_cm(picm)
        print(totalpicm)      
              elif n<=0
              print("Error)    
                    
    if x=2:
        n=int(input("Introduce la cantidad: ") 
        if n>0        
        totalpucm=pulgadas_cm(pucm)
        print(totalpucm)         
              elif n<=0
              print("Error)                  
              
    if x=3:
                    
        n=int(input("Introduce la cantidad: ") 
        if n>0             
        totalycm=yardas_cm(ycm)
        print(totalycm)         
              elif n<=0
              print("Error)    
              
    else:           
        print("Error)   
              
              
              
if __name__ == '__main__':
    main()
