import json

def get_repomanifest_data(filepath):
    """
        Parse the repo manifest file and return the product and team name
        :param filepath: path to the manifest file
        :return: product and team name
    """
    product_name = "Not defined"
    team_name = "Not defined"
    try:
        file = open(filepath)
        data = json.load(file)
        product_name = (", ".join(str(element) for element in list(filter(None,data["product_names"])))).strip()
        if not product_name:
            product_name = "NA"
        tname = list(data["teams"].keys())
        team_name = (", ".join(str(element) for element in tname)).strip()
        if not team_name:
            team_name = "NA"
        return product_name, team_name
    except Exception as err:
        print(err)
        return product_name, team_name