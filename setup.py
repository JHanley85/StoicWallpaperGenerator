from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["autoMeditationsWallpaper"], "excludes": ["asyncio", "email", "html", "http",
                                                                            "lib2to3", "multiprocessing", "pydoc_data",
                                                                            "test", "tkinter", "unittest", "xmlrpc"]}
executables = [Executable("runAMW.py", icon="logo.ico")]

setup(
    name="stoic_wallpaper_generator",
    version="1",
    description="cx_Freeze script to test pillow (PIL)",
    executables=executables,
    options={"build_exe": build_exe_options},
)
