# The Minimally Smart Package Manager

For quite a while, I have been considering "how do you package software for production deployment". It's an amusingly non-trivial problem, in that there are constraints that a normal (FSVO "normal") package manager like Yum, APT, and the like (and the packaging formats these use) tend to not actually cater for.

The result of all of this is a design (there's been a few toy implementations, but nothing production-ready written, yet) is a design I call "the Minimally Smart Package Manager" (or, in my sometimes less charitable moments, the "Maximally Stupid Package Manager").

MSPM is split in two parts, a per-host CLI binary and a central package server.

## Packages
### Packages and versions

In MSPM, a "package" is a set of versions, with a common package name. It is a bit unfortunate that both the full set of versions and a specific version of a package both fit the term "package" well.

### Upgrades and downgrades
In a production environment, you will be changing the deployed production version every so often. How often is basically a reliability question. I would aim for "no more than twice a day" and consider "less than once a month" a failure in velocity.

However, changing production version requires that you have a fast reversion path. It's OK that it takes several minutes (as in 1 - 30 minutes) to deploy a new version, as long as the old version keeps running until the last point before switching over. However, if you need to roll back, it's not really acceptable that it takes long to roll back, so it should be fast.

Neither RPMs nor DEBs are well-suited for fast rollback, since in both cases there's no fundamental difference between "upgrading" and "downgrading" and it's also the case that services won't necessarily be working while the upgarde/downgarde is happening.

MSPM solves this by explicitly catering for having multiple versions installed in parallel, as well as separating the installation and activation of a package

### Version numbers

Most package managers use human-originated version numbers (semver, if you're lucky) to identify packages. While this is fine in most cases, the choice for MSPM is to have an almost-guaranteed certainty that it's impossible to end up having two packages unintentionally getting the same version number. It does this by simply delcaring that the version is the SHA-512 of the package contents.

Since that's the sort of version number that huamsn cope badly with, MSPM also allows for attaching (dynamic) labels to packages. labels are simply strings (rather than key-value pairs) and there's only one label managed automatically by MSPM itself. Whenever a package with a given name is uploaded, it is given the label "latest" (note, "latest" does not mean "newest contents", it means "latest upoaded").

For any given package, any label can refer to at most one version. If a label already exists (like, say, "latest") when that label is applied to a version, it is removed from whatever version it was previously attached to.

### Dependencies

MSPM does not track inter-package dependencies. It is encouraged to have quite fat packages.

## Actions

MSPM has a few actions, explained below. Throughout the description, the terms "package name" and "version signifier" are used. Package name should be obvious enough. Version signifier means "an explicit hex string for the SHA-512, or a label that is set for that specific package". In most cases, the version signifer defaults to "latest".

We should probably also discuss MSPM storage. Any specific version of a package is unpacked to /mspm/<packagename>-<packageversion> and teh active version of a pakage is signified by a symlink from /mspm/<packagename> to /mspm/<packagename>-<activeversion>

Each package is expected to have two executables in the top-level directory, called "start" and "stop", used to start and stop the packaged service. If they don't exist, it just means that a package cannot be started or stopped.

### Install

The "install" action takes a package name, and a version sigifier. With that info, it requests the specific package from the serer and unpacks it to local disk.

### purge

The "purge" action takes a package name and optionally a list of version signifiers. It will then delete (from local storage) any non-active version of that package. If an explicit list of version signifiers is provided, only those versions will be considered, but again the active version will not be touched.

### activate

The "activate" action takes a package name and a version signifier (no defaulting). It will then move (if it exists) or create (if not) a symlink from /mspm/<packagename> to /mspm/<packagename>-<activeversion>. It will neither start nor stop the binary.

### start

The "start" action takes a package name and an optional version (defaulting to "the active version") and will simply execute the "start" binary (this is exepcted to daemonise...) for the specific package indicated.

### stop

The "stop" action is almost identical to "start", only it runs the 'stop" binary instead.

### deactivate

The "deactivate" action removes the symlink indicating the active package.
