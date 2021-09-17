from app import app
from database import model_info

@app.route('/api/models/list')
def get_all_models():
    """
    This function responds to the interal API call of obtaining
    all models currently in the inference server

    :return: Dictionary//JSON 
    """
    info = {'code':200, 
            'models':[m for m in model_info.keys()]}
    return info

@app.route('/api/info/<id>')
def get_model_info(id):
    """
    This function responds to the interal API call of obtaining
    whether a model is active in the inference server
    
    :return: Dictionary//JSON 
    """
    
    if id in model_info:
        return {id:model_info[id]}
    else:
        return {'error':'invalid model name'}