from pathlib import Path 

directory = Path('.').resolve() / 'bld'
if not directory.is_dir():
    directory.mkdir(parents=True, exist_ok=True)