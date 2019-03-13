# `finally` in Python generators

Michael Kim <mkim0407@gmail.com>

TIL the `finally` clause will be triggered if a generator reaches
its end-of-life prematurely while waiting in the `try` block,
so I wrote some scripts to showcase.

I might make this a proper presentation in the future.

Please see `scripts/` folder:

* `0x.py`

    Basics about generator and `finally`.

* `1x.py`

    Showcase the behavior.

* `2x.py`

    Showcase how end-of-life changes in different situations.
