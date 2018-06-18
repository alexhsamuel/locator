"""
Application configuration.
"""

#-------------------------------------------------------------------------------

def get_config():
    # FIXME: Hard-coded for now.  
    cfg = {
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

    # All group members should be users.
    assert all( u in cfg["users"] for g in cfg["groups"].values() for u in g )

    return cfg


