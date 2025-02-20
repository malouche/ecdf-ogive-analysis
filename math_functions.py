from utils import calculate_ecdf, calculate_ogive

def ecdf_math_function(x, y):
    cum_probs = calculate_ecdf(x, y)
    ecdf_str = r"""
    F(x) = \begin{cases}
    """
    
    for i in range(len(x)):
        if i == 0:
            ecdf_str += f"0 & \\text{{for }} x < {x[i]:.2f} \\\\"
        else:
            ecdf_str += f"{cum_probs[i-1]:.3f} & \\text{{for }} {x[i-1]:.2f} \\leq x < {x[i]:.2f} \\\\"
    
    ecdf_str += f"1 & \\text{{for }} x \\geq {x[-1]:.2f}"
    ecdf_str += r"""
    \end{cases}
    """
    return ecdf_str

def ogive_math_function(groups, frequencies):
    cum_freq = calculate_ogive(groups, frequencies)
    ogive_str = r"""
    G(x) = \begin{cases}
    """
    
    for i in range(len(groups) - 1):
        if i == 0:
            ogive_str += f"0 & \\text{{for }} x < {groups[i]:.2f} \\\\"
        else:
            ogive_str += f"{cum_freq[i-1]:.3f} & \\text{{for }} {groups[i-1]:.2f} \\leq x < {groups[i]:.2f} \\\\"
    
    ogive_str += f"1 & \\text{{for }} x \\geq {groups[-1]:.2f}"
    ogive_str += r"""
    \end{cases}
    """
    return ogive_str