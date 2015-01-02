import subprocess   
class Speaker(object):
    """Wrapper around espeak"""
    opts = ["-ven+f3", "-k5", "-s130", "-g3", '--punct="<characters>"' ]
        
    def say(this, text):
        """Invoke this method to say a particular line of text"""
        import subprocess   
        args = ['espeak'] + this.opts + [ text ]
        return subprocess.call(args)

# vim: set sw=4 ts=4 et:
