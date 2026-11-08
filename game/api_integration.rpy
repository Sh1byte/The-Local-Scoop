init python:
    import sys
    import os

    api_path = os.path.join(renpy.config.gamedir, "api_core")
    if api_path not in sys.path:
        sys.path.append(api_path)

    import sheetdb_client