import yaml


def read_config():
    with open(r"C:\Users\DELL\Desktop\集中\web_xiaoan\common\config.yml",encoding="utf-8") as f:
        config_datas=yaml.safe_load(f)
    return config_datas