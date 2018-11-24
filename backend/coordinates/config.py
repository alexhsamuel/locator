"""
Application configuration.
"""

import json

#-------------------------------------------------------------------------------

SAMPLE_CFG = {
    "statuses": [
        "remote",
        "sick",
        "medical",
        "vacation",
        "personal",
        "Greenwich",
        "NYC",
        "London",
    ],

    "users": {
        "asamuel", 
        "ebernste", 
        "kmalyar",
        "mlumelsk",
        "mroiter", 
        "ptj",
        "scai", 
        "slevin",
        "sgorbey",
    },

    "groups": {
        "ASD": {
            "asamuel", 
            "scai", 
            "slevin",
        },
        "Data": {
            "ebernste", 
            "kmalyar",
        },
        "IT": {
            "mroiter", 
            "mlumelsk",
        },
    }
}


def check_config(cfg):
    assert "statuses" in cfg
    assert all( isinstance(s, str) for s in cfg["statuses"] )

    assert "users" in cfg
    assert all( isinstance(u, str) for u in cfg["users"] )

    # Note: groups not currently used.
    assert "groups" in cfg
    assert all( 
            u in cfg["users"] 
            for g in cfg["groups"].values()
            for u in g
    ), "all group members must be users"


def load_config(path):
    """
    Loads a JSON config file.
    """
    with open(path, "r") as file:
        cfg = json.load(file)
    check_config(cfg)
    return cfg


