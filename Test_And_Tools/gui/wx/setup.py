from cx_Freeze import setup, Executable

base = None


executables = [Executable("wxtest.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "<any name>",
    options = options,
    version = "0.0.0",
    description = '<any description>',
    executables = executables
)