# PytuX DSL (Windows/Linux)

## Requirements
- [*python*](https://www.python.org/downloads/) >= 3.6
- [*pip*](https://pip.pypa.io/en/stable/)

## Install
From project root dir: \
`pip install .` or \
`pip install . --upgrade` if installed

## Examples
- to get help messages:\
`pytux -h`\
per command:\
`pytux <command> -h`\
per task:\
`pytux <command> <task> -h`
- current logging test:\
`pytux build`\
`pytux log show`
- to suppress ***loglvl < WARNING*** msgs:\
`pytux -l warning build`\
`pytux log show`
- clear log:\
`pytux log clear`