# A Minimalistic Pipeline Utility

## What is this?

This utility is a python one-file-script named `kpype` that runs only-if-necessary the scripts contained in a folder named ./scripts.

### Inspiration:

  * It is inspired but incompatible with https://github.com/JacquesBass/rpipe.
  * Unlike rpipe, it is file type agnostic.
  * Even if created for **The Tangle** (mainly .json output files), it's general purpose and intentionally minimalistic.
  * There will be no support or request for features. When it works, we move on. This is created to save time, not to waste time.

### Key idea:

  * Scripts (as relative to the working directory) match the regex `"^.*/scripts/([0-9]+)_([a-zA-Z][a-zA-Z0-9_]*)\\.py$"`
  * The first () captures a number which defines the order in which (if required) they should run.
  * The second () is a class name containing:
    * `.inputs()` returning a list of file names with all the inputs.
    * `.output()` **one** file the script generates. Can be `None` if the method is just a definition of properties or functions.
    * `.build()` the method to be run to generate the output.
    * `<anything else>` is okay. Scripts can import from other scripts. Just bear in mind `kpype` is not aware.

### Usage:

  * `kpype info` lists all the scripts and data files including hashes and recency showing what needs rebuilding, if anything.
  * `kpype fast` same and `info` without computing the file hashes.
  * `kpype make` apply a **make algorithm** to build the files if either the inputs or the scripts have smaller recency than the output.
  * `kpype build` rebuild everything in order regardless of file recency.
