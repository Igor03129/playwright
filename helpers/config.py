from pathlib import Path

from vyper import v


def load_config(domain):
    if domain.lower() == "ru":
        filename = "ru_domain"
    elif domain.lower() == "com":
        filename = "com_domain"
    else:
        raise ValueError(f"Неправельный домен: {domain}")

    configs_folder = Path(__file__).parent.parent / "configs"
    v.set_config_name(filename)
    v.set_config_type("yaml")
    v.add_config_path(configs_folder)
    v.read_in_config()

    return v
