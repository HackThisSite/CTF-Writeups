# Flag Collection

Here's a collection of flags! I think you're looking for a specific one, though...


## Solution

We are given a zip file flags.zip, that when unpacked contain a lot of files depicting
different flags from around the world.

There is also a Thumbs.db file, which is a file windows use to catalog thumbnails for
directory views.

We rename it on our linux machine to thumbmofo.db in order to prevent windows from 
hiding it and making it a systemfile.

We go back to windows and use the program https://thumbsviewer.github.io/ in order to
view the thumbmofo.db content. Which presents us with a lot of thumbnail images of
different flags.

In addition to the flags we already seen, it also has a thumbnail of a flag that
apparantly got deleted after the Thumbs.db got created.

This thumbnail image contains our flag, which is a QR Code.

We scan it and get the fore real flag!

*easyctf{thumbs.db_c4n_b3_useful}*

