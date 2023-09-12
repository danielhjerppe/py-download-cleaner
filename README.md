# py-download-cleaner
Organizes your Download folder

Tested on MacOS Ventura

Goes through your files in Downloads folder and moves them into own subfolders under "Downloads".

To customize, modify the dictionary below. *Keys* represent folder names, while the *values* associated with keys indicate which file types should be moved to those folders by the program.

```python
FILE_TYPES = {"Pictures": [".png", ".jpg", ".jpeg", ".JPG"],
              "Documents": [".pdf", ".docx", ".pptx", ".txt", ".xlsx"],
              "3D": [".stl", ".f3d", ".STEP", ".stp", ".3mf"],
              "Archives": [".zip", ".dmg", ".pkg"]
              }
```
