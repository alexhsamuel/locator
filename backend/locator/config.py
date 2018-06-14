"""
Application configuration.
"""

#-------------------------------------------------------------------------------

class Config:

    # FIXME: Hard-coded for now.  

    statuses = [
        "remote",
        "sick",
        "medical",
        "vacation",
        "personal",
        "Greenwich",
        "NYC",
        "London",
    ]

    users = {
        "asamuel", 
        "ebernste", 
        "kmalyar",
        "mlumelsk",
        "mroiter", 
        "ptj",
        "scai", 
        "slevin",
        "sgorbey",
    }

    groups = {
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



# All group members should be users.
assert all( u in Config.users for g in Config.groups.values() for u in g )

