# dupdel
Remove duplicate files from current directory.

### Working
Its working is related to how Windows naming works.
Normally, when you have more than one file with same name,
Windows automatically renames second with `(1)` or any number
thing in the original file's name.

This program removes those files which have `(1)` (or any number)
in them and they are identical to the original one, but if the originals are not found, it renames them
to what the originals would look like.

Examples:

- Original `flower.jpg` exists and `flower (1).jpg` is identical to `flower.jpg`.
 
`flower (1).jpg` -> Deletes it.

<br>

- Original (looks like) `flower.jpg` exists and `flower (1).jpg` also exists, but is not identical to the original one.

`flower (1).jpg` -> Leaves it.

<br>

- File `flower.jpg` does not exist, but `flower (1).jpg` exists.

`flower (1).jpg` -> Renames it to `flower.jpg`.