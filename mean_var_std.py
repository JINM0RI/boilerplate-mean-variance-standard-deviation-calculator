import numpy as np

def calculate(list):
    if len(list) !=9:
        raise ValueError("List must contain nine numbers.")
    mat=np.array(list).reshape(3,3)

    #MEAN
    mean_axis0=np.mean(mat,axis=0)
    mean_axis1=np.mean(mat,axis=1)
    mean_flatt=np.mean(mat)
    #VARIANCE
    var_axis0=np.var(mat,axis=0)
    var_axis1=np.var(mat,axis=1)
    var_flatt=np.var(mat)
    #SD
    SD_axis0=np.std(mat,axis=0)
    SD_axis1=np.std(mat,axis=1)
    SD_flatt=np.std(mat)
    #MAX
    MAX_axis0=np.max(mat,axis=0)
    MAX_axis1=np.max(mat,axis=1)
    MAX_flatt=np.max(mat)
    #MIN
    MIN_axis0=np.min(mat,axis=0)
    MIN_axis1=np.min(mat,axis=1)
    MIN_flatt=np.min(mat)
    #SUM
    SUM_axis0=np.sum(mat,axis=0)
    SUM_axis1=np.sum(mat,axis=1)
    SUM_flatt=np.sum(mat)

    calculations = {
        'mean': [np.mean(mat, axis=0).tolist(), np.mean(mat, axis=1).tolist(), np.mean(mat)],
        'variance': [np.var(mat, axis=0).tolist(), np.var(mat, axis=1).tolist(), np.var(mat)],
        'standard deviation': [np.std(mat, axis=0).tolist(), np.std(mat, axis=1).tolist(), np.std(mat)],
        'max': [np.max(mat, axis=0).tolist(), np.max(mat, axis=1).tolist(), np.max(mat)],
        'min': [np.min(mat, axis=0).tolist(), np.min(mat, axis=1).tolist(), np.min(mat)],
        'sum': [np.sum(mat, axis=0).tolist(), np.sum(mat, axis=1).tolist(), np.sum(mat)]
    }

    return calculations