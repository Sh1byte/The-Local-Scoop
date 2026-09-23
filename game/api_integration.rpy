# Initialize the Python environment and import Josh's script
init python:
    import sys
    import os
    
    # Add the api_core folder to Ren'Py's system path so it can find the file
    api_path = os.path.join(renpy.config.gamedir, "api_core")
    if api_path not in sys.path:
        sys.path.append(api_path)
        
    import sheetdb_client