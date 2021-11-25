import cx_Freeze
executables = [cx_Freeze.Executable(
    script="main.py", icon="assets/mucego.ico")]

cx_Freeze.setup(
    name="Iron Man Dead",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets","game.py","lista.Vencedores"]
                           }},
    executables=executables
)
