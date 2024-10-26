import csv 

def read_csv(path):
  with open(path, 'r') as csvfile:
    #el delimiter es como vienen separados los datos, puede ser por , o ;
    reader = csv.reader(csvfile, delimiter=',')
    '''
    el reader es un iterador, entonces vamos a iterar manual el primer elemto para que 
    nos de las llaves del diccionario y por so despues se une con row para llenar con 
    informacion adeccuada 
    '''
    header = next(reader)
    data = []

    #aqui iteramos y leemos fila a fila 
    for row in reader:
      '''
      aqui estamos uniendo el header con el row, pero como es un iteraor, lo que hace 
      es que lo convierte en una tupla, hader = key and row = value
      '''
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('world_population.csv')
  print(data[0])