import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    predictions = np.array(predictions).T
    
    result = []
    for sample_preds in predictions:
        values, counts = np.unique(sample_preds, return_counts=True)
        
        max_count = np.max(counts)
        
        candidates = values[counts == max_count]
        
        result.append(np.min(candidates))
    
    return result