#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    for index, pred in enumerate(predictions):
        cleaned_data.append((ages[index][0], net_worths[index][0], (pred[0] - net_worths[index][0])**2))

    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])
    length = len(cleaned_data)
    new_length = int(length*0.9)

    return cleaned_data[:new_length]

