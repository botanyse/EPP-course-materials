def convert_lod_to_dol(lod):
    """Transforms a list of dictionaries to a dictionary of lists.

    Args: 
        lod: list of dictionaries

    Returns:
        dol: dictionary with list values
    """
    dol = {}
    for i in range(len(lod)): # looping each dictionary in the list
        for j in lod[i]: # looping each key inside the dictionary
            if j not in dol:
                dol[j] = [lod[i][j]]
            else:
                dol[j].append(lod[i][j])
    return dol

        
def convert_dol_to_lod(dol):
    lod = []
    keys = list(dol.keys())
    for i in range(len(dol[keys[0]])): 
        dict_inside_list = {}
        for key in dol.keys():
            dict_inside_list[key] = dol[key][i]
        lod.append(dict_inside_list)
    return lod

def create_markdown_table(data):
    out = data.copy()
    if isinstance(out, dict):
        out = convert_dol_to_lod(out)
    header = str()
    table = str()
    keys = out[0].keys()
    for key in keys:
        header += " | " + key  
    for i in out:
        for key in keys:
            table += " | " + i[key]
        table += " |" + "\n" 
    header_final = header + " |\n"
    lines = " " + ("|" + "------")*2 + "|\n"

    result =  header_final + lines + table
    return result







