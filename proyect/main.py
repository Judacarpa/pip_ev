import utils
import readcvs
import chartpro
import pandas as pd

def run():

  
  
  #segundo retos y esa una forma de hacerlo manual 
  '''
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  chartpro.generate_pie_chart(countries, percentages)
  '''
  #esta es una forma de hacerlo mas rapido con una modulo 
  df = pd.read_csv('world_population.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  chartpro.generate_pie_chart(countries, percentages)

  data = readcvs.read_csv('world_population.csv')

  #primer reto
  country = input('type country => ' )

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    chartpro.generate_bar_chart(country['Country/Territory'], labels, values)
  

  
if __name__ == '__main__':
  run()