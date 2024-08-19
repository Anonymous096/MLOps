import os
from pathlib import Path
import logging 
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') 
project_name = "mlops" 
list_of_files = [ ".github/workflows/.gitkeep", 
                 f"src/{project_name}/_init.py", 
                 f"src/{project_name}/components/init.py", 
                 f"src/{project_name}/utils/init.py", 
                 f"src/{project_name}/utils/common.py", 
                 f"src/{project_name}/config/init.py", 
                 f"src/{project_name}/config/configuration.py", 
                 f"src/{project_name}/pipeline/init.py", 
                 f"src/{project_name}/entity/init.py", 
                 f"src/{project_name}/entity/config_entity.py", 
                 f"src/{project_name}/constants/init_.py", "config/config.yaml", "params.yaml", "schema.yaml", "main.py", "app.py", "Dockerfile", "requirements.txt", "setup.py", "research/trials.ipynb", "templates/index.html", "test.py" 
                ] 
for filepath in list_of_files: 
    filepath = Path(filepath) 
    filedir, filename = os.path.split(filepath) 
    if filedir !="":    
        os.makedirs(filedir, exist_ok=True) 
        logging.info(f"Creating directory; {filedir} for the file: {filename}") 
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): 
            with open(filepath, "w") as f: 
                pass 
            logging.info(f"Creating empty file: {filepath}") 
        else: logging.info(f"{filename} is already exists")