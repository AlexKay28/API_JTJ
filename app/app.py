import json
import sys
import connexion


def sum_up_all_elements(json_info):   
    
    print(type(json_info))
    json_info = json.loads(json_info)
    
    print(type(json_info))
    print(json_info)
    
    id = json_info['calc_id']
    sum_elements = sum(json_info['elements'])
    
    
    return {'id': id, 'sum': sum_elements}

 
if __name__ == '__main__':
  app = connexion.FlaskApp(__name__, specification_dir='.')
  app.add_api('api_file.yml')
  app.run(port=8085)