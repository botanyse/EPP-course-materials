from pathlib import Path 

this_file_dir = Path(__file__).parent
bld_dir = this_file_dir / "bld"

if not bld_dir.is_dir():
    bld_dir.mkdir(parents=True, exist_ok=True)


# to untrack additional files within a subfolder, you can create another .gitignore file inside the subfolder. 
# touch .gitignore
# echo '/bld' >> .gitignore
# cat .gitignore