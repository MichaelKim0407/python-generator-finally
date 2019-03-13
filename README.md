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

Related read: [PEP 342](https://www.python.org/dev/peps/pep-0342/#specification-summary)

> Add a close() method for generator-iterators,
> which raises GeneratorExit at the point where the generator was paused.
> If the generator then raises StopIteration (by exiting normally, or due to already being closed)
> or GeneratorExit (by not catching the exception),
> close() returns to its caller.
> If the generator yields a value, a RuntimeError is raised.
> If the generator raises any other exception, it is propagated to the caller.
> close() does nothing if the generator has already exited due to an exception or normal exit.
>
> Add support to ensure that close() is called when a generator iterator is garbage-collected.
>
> Allow yield to be used in try/finally blocks,
> since garbage collection or an explicit close() call would now allow the finally clause to execute.
