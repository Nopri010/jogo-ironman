# pip install cx_freeze
import cx_Freeze
executaveis = [
    cx_Freeze.Executable(script="main.py")]
cx_Freeze.setup(
    name = "Iron Man",
    options={
        "build_exe":{
            "packages":["pygame"],
            "inlude_files":["assets"]
        }
    }, executables = executaveis
)