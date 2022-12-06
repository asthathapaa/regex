Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============== RESTART: C:/Users/HP/Desktop/python astha/astha.py ==============
from datetime import datetime
import time
print("time.ctime():",time.ctime())
time.ctime(): Tue Dec  6 20:13:43 2022
print("time.ctime()+1hr:",time(hrfromnow))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("time.ctime()+1hr:",time(hrfromnow))
NameError: name 'hrfromnow' is not defined
print(datetime.today)
<built-in method today of type object at 0x00007FFACAC688E0>
print((datetime.today))
<built-in method today of type object at 0x00007FFACAC688E0>
print[(datetime.today)]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print[(datetime.today)]
TypeError: 'builtin_function_or_method' object is not subscriptable
print[(datetime.today)]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print[(datetime.today)]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print([datetime.today])
[<built-in method today of type object at 0x00007FFACAC688E0>]
>>> import sys
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_getquickenedcount', '_git', '_home', '_stdlib_dir', '_vpath', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']
>>> sys.path
['C:/Users/HP/Desktop/python astha', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\idlelib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311\\Lib', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311\\DLLs', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311', 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages']
>>> sys.version
'3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)]'
>>> sys.version_info
sys.version_info(major=3, minor=11, micro=0, releaselevel='final', serial=0)
>>> sys.exit(1)
>>> sys.exit(1)
