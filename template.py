import os
from pathlib import Path

list_of_files=[
    "QAWithPDF/__init__.py",
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/embedding.py",
    "QAWithPDF/model_api.py",
    "Experiments/experiment.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py"
        ]

for file in list_of_files:
    filepath=Path(file)
    file_dir,file_name=os.path.split(filepath)
    
    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True
                    )
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass
        