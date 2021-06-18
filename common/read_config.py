import yaml


def read_config():
    with open("../common/config.yml",encoding="utf-8") as f:
        config_datas=yaml.safe_load(f)
    return config_datas