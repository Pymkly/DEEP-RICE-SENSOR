import json

def get_global_config():
    with open("global_config.json", 'r') as file:
        global_config = json.load(file)
        return global_config

def get_config_by_key(_key):
    global_config = get_global_config()
    return global_config[_key]

def get_server_url():
    return get_config_by_key('server_url')

def get_sensor_data_url():
    return get_config_by_key('sensor_data_url')

def get_ref():
    return get_config_by_key('ref')

def on_mac_unknown(mac):
    _config = get_global_config()
    mac_unknown = _config["mac_unknown"]
    if mac not in mac_unknown:
        mac_unknown.append(mac)
        _config["mac_unknown"] = mac_unknown
        with (open("global_config.json", 'w')) as f:
            json.dump(_config, f, indent=4)
        print(f"🟡 Nouvelle MAC détectée : {mac} ajoutée dans mac_unknown")

def get_ref_from_mac(mac_address):
    """
    Retourne le 'ref' (ex: POTO#0001) associé à une adresse MAC dans le fichier global_config.json.
    """
    try:
        config = get_global_config()
        mac_map = config.get("mac_to_ref", {})
        return mac_map.get(mac_address)
    except Exception as e:
        print(f"Erreur lors de la récupération du ref pour {mac_address} : {e}")
        return None
