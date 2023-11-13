from pathlib import Path 
import zipfile

this_file_dir = Path(__file__).parent
bld_dir = this_file_dir / "bld"

if not bld_dir.is_dir():
    bld_dir.mkdir(parents=True, exist_ok=True)


# to untrack additional files within a subfolder, you can create another .gitignore file inside the subfolder. 
# touch .gitignore
# echo '/bld' >> .gitignore
# cat .gitignore

with zipfile.ZipFile(this_file_dir/'original_data/original_data.zip', 'r') as zip_ref:
    zip_ref.extractall(bld_dir)