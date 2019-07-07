import pandas as pd
from sklearn.neural_network import MLPRegressor
import pickle as pic

# =============================================================================
# LOAD DATA
# =============================================================================
    
def load_data(file_name, sep=';'):
    data = pd.read_csv(file_name, sep=sep)
    
    data_sum = [data.iloc[:,:2],
                data.iloc[:,2]]
    
    data_sub = [data.iloc[:,3:5],
                data.iloc[:,5]]
    
    data_mul = [data.iloc[:,6:8],
                data.iloc[:,8]]
    
    data_div = [data.iloc[:,9:11],
                data.iloc[:,11]]
    
    data_list = [data_sum, 
                 data_sub, 
                 data_mul, 
                 data_div]

    return data_list

# =============================================================================
# MAKE MODELS
# =============================================================================

def make_models(fl_b, fl_i, fl_a, max_iter=1000):
    MLP_bashir_sum = MLPRegressor(hidden_layer_sizes=fl_b, max_iter=max_iter)
    MLP_ivan_sum = MLPRegressor(hidden_layer_sizes=fl_i, max_iter=max_iter)
    MLP_albina_sum = MLPRegressor(hidden_layer_sizes=fl_a, max_iter=max_iter)


    MLP_bashir_sub = MLPRegressor(hidden_layer_sizes=fl_b, max_iter=max_iter)
    MLP_ivan_sub = MLPRegressor(hidden_layer_sizes=fl_i, max_iter=max_iter)
    MLP_albina_sub = MLPRegressor(hidden_layer_sizes=fl_a, max_iter=max_iter)


    MLP_bashir_mul = MLPRegressor(hidden_layer_sizes=fl_b, max_iter=max_iter)
    MLP_ivan_mul = MLPRegressor(hidden_layer_sizes=fl_i, max_iter=max_iter)
    MLP_albina_mul = MLPRegressor(hidden_layer_sizes=fl_a, max_iter=max_iter)


    MLP_bashir_div = MLPRegressor(hidden_layer_sizes=fl_b, max_iter=max_iter)    
    MLP_ivan_div = MLPRegressor(hidden_layer_sizes=fl_i, max_iter=max_iter)    
    MLP_albina_div = MLPRegressor(hidden_layer_sizes=fl_a, max_iter=max_iter)
    
    model_list_sum = [MLP_bashir_sum, 
                      MLP_ivan_sum, 
                      MLP_albina_sum]
    
    model_list_sub = [MLP_bashir_sub,
                      MLP_ivan_sub,
                      MLP_albina_sub]
    
    model_list_mul = [MLP_bashir_mul,
                      MLP_ivan_mul,
                      MLP_albina_mul]
    
    model_list_div = [MLP_bashir_div,
                      MLP_ivan_div,
                      MLP_albina_div]
        
    model_list = [model_list_sum, 
                      model_list_sub, 
                      model_list_mul, 
                      model_list_div]
    
    return model_list

# =============================================================================
# TRAINING CENTER
# =============================================================================

def train_models(model_list, data_list, data_size=100000):
    trained_model_list = []
    print('TMList was created!\n')
    
    type_operation = 0
    
    for mod, dat in zip(model_list, data_list):
        print('ToO: {}\n'.format(type_operation))
        type_operation += 1
        
        type_model = 0
        
        one_type_model_list = []
        print('OTList was created!\n')
        
        for m in mod:
            print('ToM: {}\n'.format(type_model))
            type_model += 1            
            
            m.fit(dat[0].iloc[:data_size], dat[1].iloc[:data_size])
            one_type_model_list.append(m)
            
            print('Current model was added to OTList!\n')
            print('Current model predict 50 and 10 is: {}\n\n'.format(m.predict([[50,10]])))
        
        trained_model_list.append(one_type_model_list)
    
    print('= WELL DONE! Let\'s testing! =')
    
    return trained_model_list

# =============================================================================
# SAVE OR LOAD PICKLE FILE
# =============================================================================

def pickled(data=None, filename='noname.pickle', mode='save'):
    if mode == 'save':        
        pic.dump(data, open(filename, 'wb'))
    elif mode == 'load':
        return pic.load(open(filename, 'rb'))
    
# =============================================================================
# GET ANSWER
# =============================================================================

def get_answer(trained_model_list, values=[2,2], operation=0):
    
    def who_is_winner(predict_list, values, operation):
        if operation == 0:
            true_ans = values[0] + values[1]
            
        elif operation == 1:
            true_ans = values[0] - values[1]
            
        elif operation == 2:
            true_ans = values[0] * values[1]
            
        elif operation == 3:
            true_ans = values[0] // values[1]
            
        true_ans = int(round(true_ans))
            
        min_diff = None
        winner_d = None
        diff_list = []
        
        for d in range(len(predict_list)):
            diff = abs(predict_list[d] - true_ans)
            diff_list.append(diff)
            
            if min_diff == None:
                min_diff = diff
                winner_d = d
            elif diff < min_diff:
                min_diff = diff
                winner_d = d
        
        return_hash = {'tans': true_ans, 
                       'dlist': diff_list, 
                       'idwin': winner_d}
    
        return return_hash

    def get_predict_list(trained_model_list, values, operation):
        predict_list = []    
        
        for model in trained_model_list[operation]:
            pred = model.predict([values])
            predict_list.append(pred)
            
        return predict_list 
    
    def get_nn_name(i):    
        nn_names = ['BASH', 'IVAN', 'ALBA']

        return nn_names[i]

    predict_list = get_predict_list(trained_model_list, values, operation)
    wiw_hash = who_is_winner(predict_list, values, operation)

    ans = sum(predict_list) / len(predict_list)
    ans = int(round(ans[0]))
        
    bans = round(predict_list[0][0], 2)
    ians = round(predict_list[1][0], 2)
    aans = round(predict_list[2][0], 2)
    
    return_hash = {'ans': ans, 
                   'tans': wiw_hash['tans'], 
                   'dlist': wiw_hash['dlist'], 
                   'idwin': wiw_hash['idwin'], 
                   'nwin': get_nn_name(wiw_hash['idwin']), 
                   'bans': bans, 
                   'ians': ians, 
                   'aans': aans}
    
    return return_hash