def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    if not returns:
        return []
    
    cum_returns = []
    wealth_index = 1.0  # Tracks (1 + r1) * (1 + r2) * ...
    
    for r in returns:
        wealth_index *= (1 + r)
        cum_returns.append(wealth_index - 1)
    
    return cum_returns