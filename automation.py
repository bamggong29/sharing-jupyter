import pandas as pd

def calculate_func_over_time(df, category, continent, func, verbose=False):
    """Calculates values of a statistic function over time
    
    Args:
        df: A pandas DataFrame
        category: one of the column headers in your DataFrame df (e.g. 'lifeexp')
        continent: possible value of continent column in your DataFrame (e.g. 'asia')
        func: A function to apply on the data values (e.g. np.mean)
        verbose: Show debugging output (optional, defaults to False)
    
    Returns:
        a summary table of value per year (DataFrame)
        
    """    
    # check the values provided
    assert category in df.columns.values
    assert 'continent' in df.columns.values
    assert continent in df['continent'].unique()
    
    mask_continent = df['continent'] == continent
    df_continent =df[mask_continent]

    #pull out all the years from the dataset
    years = df_continent['year'].unique()

    # Create an empty list to store the summary values
    summary = []

    # pull out the func category value at each year
    for year in years:
        if verbose:
            print(year)
        mask_year = df_continent['year'] == year
        df_year = df_continent[mask_year]
        value = func(df_year[category])
        summary.append((continent, year, value))
        if verbose:
            print('adding', continent, value)
    
    summary = pd.DataFrame(summary, columns=['continent','year', category])
    return summary