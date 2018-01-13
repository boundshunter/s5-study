
#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:summer_han

import re
>>> a=re.match("inet","inet addr:10.0.1.110  Bcast:10.0.255.255  Mask:255.255.0.0")
>>> a
<_sre.SRE_Match object; span=(0, 4), match='inet'>
>>> a=re.match("\w+","inet addr:10.0.1.110  Bcast:10.0.255.255  Mask:255.255.0.0")
>>> a
<_sre.SRE_Match object; span=(0, 4), match='inet'>

没匹配上返回none  匹配上了返回值

