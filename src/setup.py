#coding:utf-8
from cx_Freeze import setup, Executable

setup(
        name = "GTN GAME",
        version = "0.1",
        options={"build_exe":{"packages":["pygame"],
                              "include_files":["data","images","songs"]}},
        description = "déclenche le Ice Walker",
        executables = [Executable("Pygame.py")]
        )