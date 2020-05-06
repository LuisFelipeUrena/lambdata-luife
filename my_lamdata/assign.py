# helper function: checking for nan values

import pandas


def null_val(x):
    """
    Checks for null values in any given Pandas
    Dataframe Object.

    Args:
        x;A Pandas dataframe object

    Returns:
            Null value counts for each column





    """

    x = x.copy()
    nulls = pandas.Series(x.isnull().sum())
    print('Null Values in each Column')
    print('---------------------------')
    print(nulls)
    print('---------------------------')


def cat_variables(x):
    """
    Checks for categorical variables in
    any given DF

    args:
        x; Pandas Dataframe Object
    returns
        list of all categorical data




    """
    x = x.copy()
    result = x.astype('object').describe()
    return result

    if __name__ == "__main__":

        print('if you imported this function, you did,something wrong')
