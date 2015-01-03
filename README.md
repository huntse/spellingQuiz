This is a simple ipython notebook to test spellings (eg for school spelling
homework).  To run it, you'll need to install ipython notebook and espeak.
Assuming you already have python, this is usually easy to install by just doing

    pip install "ipython[notebook]"

If you haven't installed python, you can find instructions at the [Python
Beginners Guide][beginners_guide]

Espeak is an open source software speech synthesizer which is available for
Linux, Mac and Windows.  When I originally wrote this notebook, I used the
built-in Apple speech synthesizer which I think gives slightly more natural
speech, however an upgrade to the OS made the python bindings break so I
changed to espeak instead.  My daughter finds the robotic nature of the speech
part of the fun.  Ymmv.  On mac you just install espeak using [homebrew][]

    brew install espeak

...on other platforms, follow the instructions to [download espeak][].

Having got espeak and ipython notebook installed, run this by typing
    
    ipython notebook

...in the directory the files are in or in one of its parents.  Then you
interact with it in a web browser, selecting "Cell/Run All".

This notebook is provided for free on the basis of the Creative Commons
Attribution-ShareAlike 4.0 [license][].  Enjoy the software!

Sean

[beginners_guide]: https://www.python.org/about/gettingstarted/ "Python Beginners Guide"
[homebrew]: http://brew.sh/ "Homebrew package manager for OS X.  Every mac owner show have this."
[download espeak]: http://espeak.sourceforge.net/download.html "Espeak download instructions"
[license]: http://creativecommons.org/licenses/by-sa/4.0/ "Get more details of the license here"
