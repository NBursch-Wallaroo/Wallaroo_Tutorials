import numpy
import math
import json
import pandas

def actual_postprocess(predictions):
    # turn the results of predictions into a vector
    # sklearn predictions are already a vector, so this is idempotent
#     rows = predictions.shape[0]
#     predictions = predictions.reshape((rows, ))
#     predictions = predictions.tolist()
    for i in range(len(predictions)):
        predictions[i] = int(round(predictions[i]))
    return predictions

def wallaroo_json(data):
    obj = json.loads(data)

    outputs = numpy.array(obj['outputs'][0]['Double']['data'])
    
    
    prediction = actual_postprocess(outputs).tolist()
    result = {
        'original': obj,
        'prediction': prediction
    }
    return(result)