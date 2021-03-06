Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [1, 2, 3, 5]
>>> b = (2, 5, 6, 8)
>>> c = {1, 4, 7, 9}
>>> d = {"a":1, "b":2, "c":3}
>>> type(a), type(b), type(c), type(d)
(<class 'list'>, <class 'tuple'>, <class 'set'>, <class 'dict'>)
>>> dir() # 현재 메모리에 기록된 함수, 변수 등
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c', 'd']
>>> #  반복문
>>> for i in range(2, 10): # 꼭 i일 필요 X, range(a,b)면 a부터 b-1까지
	print(i)

2
3
4
5
6
7
8
9
>>> for i in range(2, 50, 7): # range(a, b, c)에서 c는 숫자간 텀
	print(i)

2
9
16
23
30
37
44
>>> k = "africa" # 문자열
>>> k
'africa'
>>> print(k), type(k)
africa
(None, <class 'str'>)
>>> k[1:4]
'fri'
>>> len(k)
6
>>> k[-1]
'a'
>>> k[-3:]
'ica'
>>> k(len(k))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    k(len(k))
TypeError: 'str' object is not callable
>>> k[len(k)]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    k[len(k)]
IndexError: string index out of range
>>> k[:len(k)]
'africa'
>>> k.rfind('a')
5
>>> k.find('a')
0
>>> k.count('a')
2
>>> k.startswith('a')
True
>>> k.endswith('a')
True
>>> k.endswith('b')
False
>>> k
'africa'
>>> k.upper() # 대문자로 만들기
'AFRICA'
>>> k # 하지만 원본이 변하진 않음
'africa'
>>> k2 = k.upper() # 변경 값을 따로 할당해주어야함
>>> k2
'AFRICA'
>>> k
'africa'
>>> s = '   seoul   '
>>> s.strip() # 공백 지우기
'seoul'
>>> s.lstrip()
'seoul   '
>>> s.rstrip()
'   seoul'
>>> for i in range(65,91): # 아스키 코드 문자와 숫자 1:1 대응
	print(chr(i), end='')

ABCDEFGHIJKLMNOPQRSTUVWXYZ
>>> for i in range(128): 
	print(i, " ==> ", chr(i))

0  ==>   
1  ==>  
2  ==>  
3  ==>  
4  ==>  
5  ==>  
6  ==>  
7  ==>  
8  ==>  
9  ==>  	
10  ==>  

11  ==>  
12  ==>  
13  ==>  
14  ==>  
15  ==>  
16  ==>  
17  ==>  
18  ==>  
19  ==>  
20  ==>  
21  ==>  
22  ==>  
23  ==>  
24  ==>  
25  ==>  
26  ==>  
27  ==>  
28  ==>  
29  ==>  
30  ==>  
31  ==>  
32  ==>   
33  ==>  !
34  ==>  "
35  ==>  #
36  ==>  $
37  ==>  %
38  ==>  &
39  ==>  '
40  ==>  (
41  ==>  )
42  ==>  *
43  ==>  +
44  ==>  ,
45  ==>  -
46  ==>  .
47  ==>  /
48  ==>  0
49  ==>  1
50  ==>  2
51  ==>  3
52  ==>  4
53  ==>  5
54  ==>  6
55  ==>  7
56  ==>  8
57  ==>  9
58  ==>  :
59  ==>  ;
60  ==>  <
61  ==>  =
62  ==>  >
63  ==>  ?
64  ==>  @
65  ==>  A
66  ==>  B
67  ==>  C
68  ==>  D
69  ==>  E
70  ==>  F
71  ==>  G
72  ==>  H
73  ==>  I
74  ==>  J
75  ==>  K
76  ==>  L
77  ==>  M
78  ==>  N
79  ==>  O
80  ==>  P
81  ==>  Q
82  ==>  R
83  ==>  S
84  ==>  T
85  ==>  U
86  ==>  V
87  ==>  W
88  ==>  X
89  ==>  Y
90  ==>  Z
91  ==>  [
92  ==>  \
93  ==>  ]
94  ==>  ^
95  ==>  _
96  ==>  `
97  ==>  a
98  ==>  b
99  ==>  c
100  ==>  d
101  ==>  e
102  ==>  f
103  ==>  g
104  ==>  h
105  ==>  i
106  ==>  j
107  ==>  k
108  ==>  l
109  ==>  m
110  ==>  n
111  ==>  o
112  ==>  p
113  ==>  q
114  ==>  r
115  ==>  s
116  ==>  t
117  ==>  u
118  ==>  v
119  ==>  w
120  ==>  x
121  ==>  y
122  ==>  z
123  ==>  {
124  ==>  |
125  ==>  }
126  ==>  ~
127  ==>  
>>> chr(44985)
'꾹'
>>> b = banana
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    b = banana
NameError: name 'banana' is not defined
>>> b= 'banana'
>>> for i in b:
	print(i)

b
a
n
a
n
a
>>> c = '이정호'
>>> for i in c:
	print(i)

이
정
호
>>> b.endode()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    b.endode()
AttributeError: 'str' object has no attribute 'endode'
>>> a = 1234
>>> a.encode()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.encode()
AttributeError: 'int' object has no attribute 'encode'
>>> a = '1234'
>>> a.encode()
b'1234'
>>> \uabff
SyntaxError: unexpected character after line continuation character
>>> '\uabff'
'\uabff'
>>> bh = "청와대".encode()
>>> bh
b'\xec\xb2\xad\xec\x99\x80\xeb\x8c\x80'
>>> bh.decode()
'청와대'
>>> 
===== RESTART: C:/Users/user/Documents/Python/python 18_10_30 script.py =====
Traceback (most recent call last):
  File "C:/Users/user/Documents/Python/python 18_10_30 script.py", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> while True:
	dan = input("한 문자 입력 : ")
	if dan == 0:
		break
	print(dan, " 단 출력")
	for i in range(1, 10):
		print(dan, " * ", i, " = ", dan*i)

한 문자 입력 : 1
1  단 출력
1  *  1  =  1
1  *  2  =  11
1  *  3  =  111
1  *  4  =  1111
1  *  5  =  11111
1  *  6  =  111111
1  *  7  =  1111111
1  *  8  =  11111111
1  *  9  =  111111111
한 문자 입력 : 0
0  단 출력
0  *  1  =  0
0  *  2  =  00
0  *  3  =  000
0  *  4  =  0000
0  *  5  =  00000
0  *  6  =  000000
0  *  7  =  0000000
0  *  8  =  00000000
0  *  9  =  000000000
한 문자 입력 : False
False  단 출력
False  *  1  =  False
False  *  2  =  FalseFalse
False  *  3  =  FalseFalseFalse
False  *  4  =  FalseFalseFalseFalse
False  *  5  =  FalseFalseFalseFalseFalse
False  *  6  =  FalseFalseFalseFalseFalseFalse
False  *  7  =  FalseFalseFalseFalseFalseFalseFalse
False  *  8  =  FalseFalseFalseFalseFalseFalseFalseFalse
False  *  9  =  FalseFalseFalseFalseFalseFalseFalseFalseFalse
한 문자 입력 : int(0)
int(0)  단 출력
int(0)  *  1  =  int(0)
int(0)  *  2  =  int(0)int(0)
int(0)  *  3  =  int(0)int(0)int(0)
int(0)  *  4  =  int(0)int(0)int(0)int(0)
int(0)  *  5  =  int(0)int(0)int(0)int(0)int(0)
int(0)  *  6  =  int(0)int(0)int(0)int(0)int(0)int(0)
int(0)  *  7  =  int(0)int(0)int(0)int(0)int(0)int(0)int(0)
int(0)  *  8  =  int(0)int(0)int(0)int(0)int(0)int(0)int(0)int(0)
int(0)  *  9  =  int(0)int(0)int(0)int(0)int(0)int(0)int(0)int(0)int(0)
한 문자 입력 : asd
asd  단 출력
asd  *  1  =  asd
asd  *  2  =  asdasd
asd  *  3  =  asdasdasd
asd  *  4  =  asdasdasdasd
asd  *  5  =  asdasdasdasdasd
asd  *  6  =  asdasdasdasdasdasd
asd  *  7  =  asdasdasdasdasdasdasd
asd  *  8  =  asdasdasdasdasdasdasdasd
asd  *  9  =  asdasdasdasdasdasdasdasdasd
한 문자 입력 : 
===== RESTART: C:/Users/user/Documents/Python/python 18_10_30 script.py =====
Traceback (most recent call last):
  File "C:/Users/user/Documents/Python/python 18_10_30 script.py", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> while True:
	dan = int(input("한 문자 입력 : "))
	if dan == 0:
		break
	print(dan, " 단 출력")
	for i in range(1, 10):
		print(dan, " * ", i, " = ", dan*i)

한 문자 입력 : 1
1  단 출력
1  *  1  =  1
1  *  2  =  2
1  *  3  =  3
1  *  4  =  4
1  *  5  =  5
1  *  6  =  6
1  *  7  =  7
1  *  8  =  8
1  *  9  =  9
한 문자 입력 : 2
2  단 출력
2  *  1  =  2
2  *  2  =  4
2  *  3  =  6
2  *  4  =  8
2  *  5  =  10
2  *  6  =  12
2  *  7  =  14
2  *  8  =  16
2  *  9  =  18
한 문자 입력 : 3
3  단 출력
3  *  1  =  3
3  *  2  =  6
3  *  3  =  9
3  *  4  =  12
3  *  5  =  15
3  *  6  =  18
3  *  7  =  21
3  *  8  =  24
3  *  9  =  27
한 문자 입력 : 0
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> modules

Please wait a moment while I gather a list of all available modules...

__future__          atexit              hyperparser         sched
__main__            audioop             idle                scrolledlist
_abc                autocomplete        idle_test           search
_ast                autocomplete_w      idlelib             searchbase
_asyncio            autoexpand          imaplib             searchengine
_bisect             base64              imghdr              secrets
_blake2             bdb                 imp                 select
_bootlocale         binascii            importlib           selectors
_bz2                binhex              inspect             setuptools
_codecs             bisect              io                  shelve
_codecs_cn          browser             iomenu              shlex
_codecs_hk          builtins            ipaddress           shutil
_codecs_iso2022     bz2                 itertools           signal
_codecs_jp          cProfile            json                site
_codecs_kr          calendar            keyword             smtpd
_codecs_tw          calltip             lib2to3             smtplib
_collections        calltip_w           linecache           sndhdr
_collections_abc    cgi                 locale              socket
_compat_pickle      cgitb               logging             socketserver
_compression        chunk               lzma                sqlite3
_contextvars        cmath               macosx              squeezer
_csv                cmd                 macpath             sre_compile
_ctypes             code                mailbox             sre_constants
_ctypes_test        codecontext         mailcap             sre_parse
_datetime           codecs              mainmenu            ssl
_decimal            codeop              marshal             stackviewer
_distutils_findvs   collections         math                stat
_dummy_thread       colorizer           mimetypes           statistics
_elementtree        colorsys            mmap                statusbar
_functools          compileall          modulefinder        string
_hashlib            concurrent          msilib              stringprep
_heapq              config              msvcrt              struct
_imp                config_key          multicall           subprocess
_io                 configdialog        multiprocessing     sunau
_json               configparser        netrc               symbol
_locale             contextlib          nntplib             symtable
_lsprof             contextvars         nt                  sys
_lzma               copy                ntpath              sysconfig
_markupbase         copyreg             nturl2path          tabnanny
_md5                crypt               numbers             tarfile
_msi                csv                 opcode              telnetlib
_multibytecodec     ctypes              operator            tempfile
_multiprocessing    curses              optparse            test
_opcode             dataclasses         os                  textview
_operator           datetime            outwin              textwrap
_osx_support        dbm                 paragraph           this
_overlapped         debugger            parenmatch          threading
_pickle             debugger_r          parser              time
_py_abc             debugobj            pathbrowser         timeit
_pydecimal          debugobj_r          pathlib             tkinter
_pyio               decimal             pdb                 token
_queue              delegator           percolator          tokenize
_random             difflib             pickle              tooltip
_sha1               dis                 pickletools         trace
_sha256             distutils           pip                 traceback
_sha3               doctest             pipes               tracemalloc
_sha512             dummy_threading     pkg_resources       tree
_signal             dynoption           pkgutil             tty
_sitebuiltins       easy_install        platform            turtle
_socket             editor              plistlib            turtledemo
_sqlite3            email               poplib              types
_sre                encodings           posixpath           typing
_ssl                ensurepip           pprint              undo
_stat               enum                profile             unicodedata
_string             errno               pstats              unittest
_strptime           faulthandler        pty                 urllib
_struct             filecmp             py_compile          uu
_symtable           fileinput           pyclbr              uuid
_testbuffer         filelist            pydoc               venv
_testcapi           fnmatch             pydoc_data          warnings
_testconsole        formatter           pyexpat             wave
_testimportmultiple fractions           pyparse             weakref
_testmultiphase     ftplib              pyshell             webbrowser
_thread             functools           python 18_10_29     window
_threading_local    gc                  python 18_10_30     winreg
_tkinter            genericpath         python 18_10_30 script winsound
_tracemalloc        getopt              query               wsgiref
_warnings           getpass             queue               xdrlib
_weakref            gettext             quopri              xml
_weakrefset         glob                random              xmlrpc
_winapi             grep                re                  xxsubtype
abc                 gzip                redirector          zipapp
aifc                hashlib             replace             zipfile
antigravity         heapq               reprlib             zipimport
argparse            help                rlcompleter         zlib
array               help_about          rpc                 zoomheight
ast                 history             rstrip              zzdummy
asynchat            hmac                run                 
asyncio             html                runpy               
asyncore            http                runscript           

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> kewards
No Python documentation found for 'kewards'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> symbols

Here is a list of the punctuation symbols which Python assigns special meaning
to. Enter any symbol to get more help.

!=                  +                   <=                  __
"                   +=                  <>                  `
"""                 ,                   ==                  b"
%                   -                   >                   b'
%=                  -=                  >=                  f"
&                   .                   >>                  f'
&=                  ...                 >>=                 j
'                   /                   @                   r"
'''                 //                  J                   r'
(                   //=                 [                   u"
)                   /=                  \                   u'
*                   :                   ]                   |
**                  <                   ^                   |=
**=                 <<                  ^=                  ~
*=                  <<=                 _                   

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> lists
No Python documentation found for 'lists'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> Lists
No Python documentation found for 'Lists'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> list

help> List
No Python documentation found for 'List'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> help(LISTS)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    help(LISTS)
NameError: name 'LISTS' is not defined
>>> help(Lists)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    help(Lists)
NameError: name 'Lists' is not defined
>>> help(lists)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    help(lists)
NameError: name 'lists' is not defined
>>> held(LIST)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    held(LIST)
NameError: name 'held' is not defined
>>> help(LIST)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    help(LIST)
NameError: name 'LIST' is not defined
>>> help(List)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    help(List)
NameError: name 'List' is not defined
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> help('list')

>>> city = "서울"
>>> city2 = city.replace("서울", "부신")
>>> city2
'부신'
>>> city2 = city.replace("서울", "부tks")
>>> city2 = city.replace("서울", "부산")
>>> city2
'부산'
>>> print("{}에서 {}까지".format(city, city2))
서울에서 부산까지
>>> c = '서울 부산 대전 광주 인천'
>>> c.split()
['서울', '부산', '대전', '광주', '인천']
>>> c1 = c.split()
>>> c1
['서울', '부산', '대전', '광주', '인천']
>>> # split()
>>> len(c1)
5
>>> len(c)
14
>>> a = [1, 2, 3, 4, 5]
>>> # List
>>> a.append(6) # 값 추가
>>> a
[1, 2, 3, 4, 5, 6]
>>> a[-3]
4
>>> len(a)
6
>>> # List method는 원본 변수가 바뀜
>>> a.append(9)
>>> a.append(10)
>>> a
[1, 2, 3, 4, 5, 6, 9, 10]
>>> a.pop()
10
>>> a
[1, 2, 3, 4, 5, 6, 9]
>>> # pop()으로 빼낸 항목은 삭제
>>> a.insert(0,50)
>>> a
[50, 1, 2, 3, 4, 5, 6, 9]
>>> a.reverse()
>>> a
[9, 6, 5, 4, 3, 2, 1, 50]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5, 6, 9, 50]
>>> a = b
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    a = b
NameError: name 'b' is not defined
>>> b = []
>>> b = a
>>> b
[1, 2, 3, 4, 5, 6, 9, 50]
>>> a.clear()
>>> b
[]
>>> a
[]
>>> # python에서 =는 동치의 의미이므로 한쪽에 변화가 다른 쪽에도 영향을 미침
>>> 
>>> a = [2, 9, 70, 55, 43]
>>> aa = a
>>> aa
[2, 9, 70, 55, 43]
>>> b = a.copy()
>>> b
[2, 9, 70, 55, 43]
>>> a.append(6)
>>> a
[2, 9, 70, 55, 43, 6]
>>> aa
[2, 9, 70, 55, 43, 6]
>>> b
[2, 9, 70, 55, 43]
>>> # copy는 복사의 의미 따라서 원본의 변형에 영향 X
>>> a.insert(2, 88)
>>> a.insert(0, 49)
>>> a.sort()
>>> a
[2, 6, 9, 43, 49, 55, 70, 88]
>>> a.sort(reverse = True)
>>> a
[88, 70, 55, 49, 43, 9, 6, 2]
>>> a.remove(55)
>>> a
[88, 70, 49, 43, 9, 6, 2]
>>> a.count(49)
1
>>> c = [ 31, 45, 1]
>>> a.extend(c)
>>> a
[88, 70, 49, 43, 9, 6, 2, 31, 45, 1]
>>> # list는 값 변경이 되지만 tuple은 불변
>>> tu = 2, 5, 1, 3
>>> tu
(2, 5, 1, 3)
>>> tu[2] = 1
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    tu[2] = 1
TypeError: 'tuple' object does not support item assignment
>>> id(a), id(aa)
(58129704, 58129704)
>>> id(b)
58207088
>>> b
[2, 9, 70, 55, 43]
>>> len(b)
5
>>> k = [4, 6, 9]
>>> b.append(k) # list에 list를 appen 하면, 각 값이 추가되는 것이 아닌 list 자체가 값으로 추가됨
>>> b
[2, 9, 70, 55, 43, [4, 6, 9]]
>>> # 값을 추가 하려면
>>> # extend method 사용
>>> b.extend(k)
>>> b
[2, 9, 70, 55, 43, [4, 6, 9], 4, 6, 9]
>>> x = [5, 6, 7]
>>> a
[88, 70, 49, 43, 9, 6, 2, 31, 45, 1]
>>> a = [1, 2, 3]
>>> a.append(x)
>>> a
[1, 2, 3, [5, 6, 7]]
>>> x.append(9)
>>> x
[5, 6, 7, 9]
>>> a
[1, 2, 3, [5, 6, 7, 9]]
>>> a[1]
2
>>> a[3]
[5, 6, 7, 9]
>>> a[3][1]
6
>>> a[3][1:3]
[6, 7]
>>> a.remove(2)
>>> a
[1, 3, [5, 6, 7, 9]]
>>> a[2].remove(7)
>>> a
[1, 3, [5, 6, 9]]
>>> x
[5, 6, 9]
>>> # 파이썬에서의 할당은 변수의 주소에 자료값을 할당하는 것이 아닌
>>> # 변수를 자료값의 주소에 할당
>>> # 따라서 연결된 값은 하나가 변하면 유동적으로 변함 (같은 주소를 공유하고 있기 때문)
>>> a.append[2]
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    a.append[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.append(2)
>>> a.append(2)
>>> a.append(2)
>>> a
[1, 3, [5, 6, 9], 2, 2, 2]
>>> t = (2, 2, 2, 1, 3)
>>> t
(2, 2, 2, 1, 3)
>>> # list와 tuple은 중복 가능
>>> import sys
>>> sys.stdout.flush()
>>> # 메모리 비우기
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'aa', 'b', 'c', 'c1', 'city', 'city2', 'dan', 'i', 'k', 'sys', 't', 'tu', 'x']
>>> del a, aa, b, c, c1, city, city2, dan, i, k, sys, t, tu, x
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
>>> a= [1, 2, 3, 4 ,5]
>>> b = [2, 4, 6, 8, 10]
>>> a | b
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    a | b
TypeError: unsupported operand type(s) for |: 'list' and 'list'
>>> a = {1, 2, 3, 4, 5}
>>> b = {2, 4, 6, 8, 10}
>>> a | b
{1, 2, 3, 4, 5, 6, 8, 10}
>>> a & b
{2, 4}
>>> a.add(3)
>>> a
{1, 2, 3, 4, 5}
>>> # set(집합)은 중복 X
>>> a.remove(3)
>>> a
{1, 2, 4, 5}
>>> # 삭제는 가능
>>> a - b
{1, 5}
>>> c = {4, 5}
>>> c.issubset(a)
True
>>> # issubset() 부분집합 여부
>>> a.issuperset(c)
True
>>> # 반대
>>> # dict 딕셔너리 타입
>>> a = {'1' : 'one', '2' : 'two', '3' : 'three'}
>>> a['1']
'one'
>>> # index가 key값
>>> a.items()
dict_items([('1', 'one'), ('2', 'two'), ('3', 'three')])
>>> a.keys()
dict_keys(['1', '2', '3'])
>>> a.values()
dict_values(['one', 'two', 'three'])
>>> type(a)
<class 'dict'>
>>> for key, value in a.items():
	print(key, "==>", value)

1 ==> one
2 ==> two
3 ==> three
>>> a.update({'4' : 'four'})
>>> a
{'1': 'one', '2': 'two', '3': 'three', '4': 'four'}
>>> b = { '번호' : 1, '이름' : '이정호'}
>>> ㅠ
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    ㅠ
NameError: name 'ᅲ' is not defined
>>> b
{'번호': 1, '이름': '이정호'}
>>> b['번호']
1
>>> b.pop('번호')
1
>>> b
{'이름': '이정호'}
>>> a.get(3)
>>> a
{'1': 'one', '2': 'two', '3': 'three', '4': 'four'}
>>> a.get(4)
>>> a
{'1': 'one', '2': 'two', '3': 'three', '4': 'four'}
>>> a.get(5)
>>> a
{'1': 'one', '2': 'two', '3': 'three', '4': 'four'}
>>> a.get('5')
>>> a
{'1': 'one', '2': 'two', '3': 'three', '4': 'four'}
>>> c = {1 : 'one', 2 : 'two', 3 : 'three'}
>>> c
{1: 'one', 2: 'two', 3: 'three'}
>>> c.get(1)
'one'
>>> b.popitem()
('이름', '이정호')
>>> c.popitem()
(3, 'three')
>>> d = c.copy()
>>> d
{1: 'one', 2: 'two'}
>>> d is c
False
>>> e = c
>>> e
{1: 'one', 2: 'two'}
>>> e is c
True
>>> # 자료형 정리
>>> a = [1, 2, 3, 4, 5]
>>> b = (3, 5, 7, 9)
>>> c = {1, 3, 5, 7, 9}
>>> c2 = {1, 2, 3, 5}
>>> 2 in a
True
>>> 9 in b
True
>>> 3 in c
True
>>> 10 in c
False
>>> la = a
>>> la == a
True
>>> a is la
True
>>> id(a), id(la)
(59360720, 59360720)
>>> ca = a.copy()
>>> a == ca
True
>>> a is ca
False
>>> c | c2
{1, 2, 3, 5, 7, 9}
>>> c & c2
{1, 3, 5}
>>> c - c2
{9, 7}
>>> c.symmetric_difference(c2)
{2, 7, 9}
>>> ta = tuple(a)
>>> ta
(1, 2, 3, 4, 5)
>>> la = list(ta)
>>> la
[1, 2, 3, 4, 5]
>>> a
[1, 2, 3, 4, 5]
>>> a is la
False
>>> id(a)
59360720
>>> id(list(tuple(a)))
57434960
>>> # list를 tuple로 바꾸고 다시 list로 돌리면 id값이 달라진다!
>>> # 배열 : 동일한 자료형들의 모임

>>> 
