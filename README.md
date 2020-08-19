# sphinx-autodoc-example

This repository shows an example using Sphinx `autosummary` and `autodoc` extensions for automatic Python code documentation. 
Sphinx uses reStructured Text and its `autodoc` extension generates the documentation from docstrings, which are specific 
documentation formats for both classes, functions and variables in Python. 

There are many docstring formats available and it is up to the team to decide which one to use. For an overview on some of 
these docstring formats, take a look at [this tutorial](https://www.datacamp.com/community/tutorials/docstrings-python). 
In this example, I will use the [numpydoc format](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard), 
used in the [NumPy](https://numpy.org/) package. 
Below you can see an example of a function and its docstring using the numpydoc format.

```python
def reverse_string(string):
    """Reverse a string.

    Parameters
    ----------
    string : str
        String to be reversed.

    Returns
    -------
    str
        The input string reversed.
    """
    return string[::-1]
```

# Getting started
## Prerequisites
First, you must install Sphinx. It can be done using either `pip`
```shell
pip install sphinx
```
or Anaconda
```shell
conda install sphinx
```

## Setting up Sphinx
I am assuming you have a Python project that you want to document. So navigate to your project's root folder and
create a new folder called `doc/` to store the documentation. Then, navigate into this new folder.

```shell
mkdir doc
cd doc/
```

After that, let's run Sphinx's quick-start to generate the basic files and folders. 
Run the command below and you should see an output like in the screenshot below.
```shell
sphinx-quickstart
```
![Sphinx quick-start output.](https://imgur.com/MZ7RCw8.png)

*I personally prefer to separate the `source` and `build` directories, I think it is more organized*.

After running this script, you should have two new folders (`source` and `build`) and a Makefile, along with a batch file `make.bat` in case you are using Windows.
**You should add the `build` folder to your `.gitignore`**, as you only need to commit the rest. 

The image below shows the project structure after running the quick-start. The `pypackage` is an example package 
I created for this tutorial.

![Project structure](https://imgur.com/uQxJscU.png)

## Configuring Sphinx
From the last step, notice that you now have a file called `conf.py` inside the `source` folder. This file will contain 
all Sphinx's settings for the documentation building. You can define extensions that you want to use, default values, 
themes, etc. You may need to change some stuff in the default `conf.py` file. I will present here what I changed for this example and 
why, I think it will be useful for someone later. For more information regarding this file, refer to the 
[Sphinx's documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html).

### Path setup
First, I uncommented in `conf.py` the three lines shown below and changed `os.path.abspath('.')` to `os.path.abspath('../..')` in 
order to include the project's root folder. By doing this, Sphinx will be able to locate the package that I want to 
document, called `pypackage` in this example.

```python
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
```

### Sphinx extensions
Second, I added two extensions in the `conf.py` file. Locate the list called `extensions`, which by default is empty,
and define as shown below. The first, [sphinx.ext.autosummary](http://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html), 
uses the extension [sphinx.ext.autodoc](http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) to deal 
with the documentation generation from the docstrings in the source code and creates nice summaries. The second, 
[sphinx.ext.napoleon](http://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html), adds support for the 
[NumPy's docstring](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) and 
[Google's docstring](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings) formats.
```python
extensions = [
    'sphinx.ext.autosummary', 'sphinx.ext.napoleon'
]
```

### Theme
In the HTML settings section, I decided to change the default theme to a prettier one. The default one is called 'alabaster' 
and there are other [builtin themes](https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes) that come with Sphinx.
I decided to install a custom one to show you how to do it. In the website called [https://sphinx-themes.org/](https://sphinx-themes.org/)
you can find a number of themes which can be easily installed using `pip`. I chose one called `sphinx_rtd_theme`, inspired 
in the [Read the Docs](https://readthedocs.org/) documentation theme. In order to use it, install the theme with 
`pip install sphinx_rtd_theme` and then change the variable `html_theme` in the `conf.py` file.
```python
html_theme = 'sphinx_rtd_theme'
```

### Additional settings
Below you can see some additional settings for the `autodoc`, `autosummary` and `napoleon` extensions that I added to the
`conf.py` file. 
- `autosummary_generate`: boolean indicating whether to scan all found documents for `autosummary` directives, 
and to generate documentation pages for each.
- `autodoc_default_options`: dictionary with the default options for `autodoc` directives. I wanted to ensure that all 
methods and functions of a class or module would be automatically documented.
- `napoleon_use_rtype`: I set it as False to output the return type inline with the return description. I think it is 
more legible this way.

To configure these settings, simply append the following lines to the end of the `conf.py` file.
```python
autosummary_generate = True
autodoc_default_options = {
    'members': True,
    'inherited-members': True
}

napoleon_use_rtype = False  # Make it more legible
```

# Writing the documentation
As I mentioned before, Sphinx uses reStructured Text, which is similar to Markdown but has some differences. If you don't understand 
something regarding the syntax, please refer to this 
[reStructured Text cheat sheet](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html).

## API Reference
In this example, I will use the home page just as a link to my API Reference page. So let's start by creating the API page.
Create a file inside the `doc/source` folder called `reference.rst` (you can use any other name you want).

In my file `reference.rst`, I created what I called _summary blocks_. Each summary block documents functions and classes 
of one of the modules from my package. In my case, I had three modules (`base`, `utils` and `my_module`) so I created 
three summary blocks. Some well-known libraries follow this approach too, such as 
[Pandas](https://pandas.pydata.org/docs/reference/index.html) and [scikit-learn](https://scikit-learn.org/stable/modules/classes.html).

To do this, I used the extension `sphinx.ext.autosummary` which creates not only a nice list with 
each component of the module, but also a dedicated page for each of them with more details. Below you can see an example 
of a summary block for my module `pypackage.base`, which defines a class called `BaseClass` and a function called `clone`. 
Take a look at the file [reference.rst](doc/source/reference.rst) to see the complete version with the three summary 
blocks.

```
Base class
==========
.. currentmodule:: pypackage.base
.. autosummary::
    :toctree: generated/

    BaseClass
    clone
```
First you define the current module and then you use `autosummary` with a list of the components that you 
want to document from this module. The extension will automatically identify if a given component is a function, class, variable or module 
and will create an appropriate documentation page using reStructured Text. The argument `toctree` defines the output path 
to save the generated `.rst` files. **This output folder can also be added to `.gitignore`**.
 

## Homepage
You may have noticed that a file called `index.rst` was created during the Sphinx quick-start. It is the homepage of 
your documentation, unless you configure it otherwise in the `conf.py` file using the parameter 
[master_doc](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-master-doc). If you didn't change 
anything on it yet, you should have something like this:
```
Welcome to My Package's documentation!
======================================

.. toctree::
    :maxdepth: 2
    :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

The `toctree` directive creates a table of contents based on what you provide as arguments. In the snippet above it was 
empty, so let's add a reference to the file that was created in the previous step, which I called `reference.rst`. To do 
this, skip a line after the `caption` argument and simply add 'reference', like in the code block below.
```
.. toctree::
    :maxdepth: 2
    :caption: Contents:

    reference
```

Regarding the "Indices and tables" section, the reference `genindex` will redirect to a page with an alphabetical 
index of the entire documentation and the second reference, `modindex`, links to a page with an alphabetical index of 
the modules that had been documented. The last reference `search` redirects to a search page. _Keep in mind that if the 
directive `automodule` from the `autodoc` extension was not used in any documentation file, the `modindex` link will be 
broken_.

> Note: there is a [known issue](https://github.com/sphinx-doc/sphinx/issues/6088) with the theme `sphinx_rtd_theme` where 
>the search page is not working at the version 0.4.3. However, the search bar on the left panel works fine. So feel free 
>to remove the reference to the search page from the `index.rst` file if you use this theme.

# Building the documentation
To build the documentation and generate the static HTML pages, run the command below inside the `doc/` folder:
```shell script
make html
```
If you are in a different folder, simply add the path to the `doc` folder as an argument, as shown below: 
```shell script
make -C path/to/doc/ html
```

The generated HTML pages will be located in the folder `build/html`. You can then host these pages somewhere and make it 
available for whoever wants to use your new package.

## Screenshots
#### Homepage
![List output](https://i.imgur.com/BmAN6T5.png)

#### API reference summary using `autosummary` 
![List output](https://imgur.com/BTQ2UWE.png)

#### Documentation page for the class `BaseClass` generated automatically by `autosummary`
![Page output](https://i.imgur.com/xdwr9wQ.png)
