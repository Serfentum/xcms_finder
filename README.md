# xcms finder
If you are using xcms library from R and need some old version for
experiment replication, then you may encounter a situation of the lack
of the desired version - e.g. it's not present in [bioconductor](https://www.bioconductor.org/help/search/index.html?q=xcms/). And there is no
site with list of ALL xcms releases: only [xcms repo](https://github.com/sneumann/xcms),
but it hasn't packaged releases. Because of this, I've created this repository -
small tool for obtaining xcms library of relevant version.

If you know easier way to get xcms of arbitraty obsolete version, please
let me [know](mailto:tetpapx@bk.ru). Because at least I and my friends don't know about it


# todo
* finish readme writing
* pack it into module
* wite installing part of README


# Getting Started
To get a copy of xcms_finder you just need to

`git clone https://github.com/Serfentum/xcms_finder.git`

After that you can use xcms_finder
* from its folder
* from anywhere with specifying path to it
* from anywhere just by xcms_finder if you add it to PATH or create a proper symlink


# Prerequisites
You need these things to runn xcms_finder

> python >= 3.6
> [gitpython](https://github.com/gitpython-developers/GitPython) >= 3.1.2 -
older versions could be ok, but I'm not sure


# Installing
todo


# Usage
`xcms_finder.py -p path -v version`
or
`python xcms_finder.py -p path -v version`
where
* `xcms_finder.py` - name of our program
* `path` - path on your computer where the xcms repository will be stored
* `version` - valid xcms version like 2.99.6 or 3.0.0
* `python` - just your python =)

Also you can specify xcms repo url, but it points to xcms repo - change is unlikely

After that you'll see list of passing versions until program will hit specified version, or you'll face an error
If you have an error and there is no answer about it in my repository, please [write to me about it](mailto:tetpapx@bk.ru)

After normal work you'll find tar.gz archive with desired xcms version in the specified by path directory

## What to do next?
Usually you need tar.gz of R package to install it on R locally (in case of xcms there is no other variants
to get noncommon version)
So your future steps probably will be

`R CMD INSTALL path_to_xcms.tar.gz`
where
* `R` - your R
* `CMD INSTALL` - command to install package
* `path_to_xcms.tar.gz` - path to tar.gz of xcms obtained in previous step

Or you can do it inside R
```R
> install.packages('path_to_xcms.tar.gz')
```

But it could be just a start of your sufferings - you will need xcms dependencies.
List of them will be shown to you if xcms installation failed and you can
install them via bioconductor. Though there is a possibility that old xcms
need old dependencies' versions - it depends on their backward compatability
In this case you'll need to install special versions of dependencies first

Good luck!


# Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

# Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

# Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc