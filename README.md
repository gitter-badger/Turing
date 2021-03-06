[![GitHub issues](https://img.shields.io/github/issues/TuringApp/Turing.svg)](https://github.com/TuringApp/Turing/issues) [![GitHub stars](https://img.shields.io/github/stars/TuringApp/Turing.svg)](https://github.com/TuringApp/Turing/stargazers) [![GitHub license](https://img.shields.io/github/license/TuringApp/Turing.svg)](https://github.com/TuringApp/Turing/blob/master/LICENSE)

# Turing

Turing is a free and cross-platform app whose main goal is to assist the learning of algorithms and programming languages by providing easy-to-use development tools to all.

It provides a lighter alternative to the well-known Algobox, which is the currently de-facto widely used solution.

## Quid, quis, quomodo?

Turing is written in Python 3.6 and uses the PyQt5 framework for its GUI. It provides two work modes:

- Algorithm mode
  - Uses a "natural" pseudocode language similar to the one used in Algobox and school books.
  - Assisted development
- Program mode
  - Uses Python, for the more experienced

In both modes, the code can be debugged and executed step-by-step to facilitate the problem-solving side of development.

## Using Turing

Turing is cross-platform, but has only been tested on Windows and Linux-based operating systems. macOS should be supported, but no guarantee is made of that.

#### Python 3.6 required!

It uses the following libraries:

- [PyQt 5](https://riverbankcomputing.com/software/pyqt/) - UI framework
- [pyQode](https://github.com/pyQode/pyQode) - PyQt code editor with syntax highlighting
- [Pygments](http://pygments.org/) - Syntax highlighter for printing code files
- [pep8](https://pypi.python.org/pypi/pep8) - Code quality checker

First, install everything using pip:

    pip install -r requirements.txt

Note: if you have Python 2.x installed on your computer, the old `pip` may be present in `PATH` and interfere with the above command line. If that happens, try using `pip3` instead of `pip`.

Next, open the src/ folder and use `run` or `./run.sh` depending on your operating system. You may need to do `chmod +x run.sh` to be able to execute it directly.

