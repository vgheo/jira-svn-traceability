

Discarded implementation - call svn from python

```
def svn_log(url):
	svn_command = "svn log {0} ".format(url)
	p=subprocess.Popen(shlex.split(svn_command, stdout=subprocess.PIPE))
	return p.communicate()
```
