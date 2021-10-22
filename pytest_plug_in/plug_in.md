## pytest插件：

- 内置插件 ----pytest内置的hook函数相当于一些预留的接口
- 外部插件 ----通过pip安装的插件
- 本地插件 ----fixture 自定义的插件内容，放在conftest.py文件中，pytest会自动的发现这些插件

### pytest-ordering

- --控制用例的执行顺序

### pytest-dependency

- --控制用例的依赖关系

### pytest-xdist

- --分布式并发执行测试用例

### pytest-rerunfailures

- --失败重跑

### pytest-assume

- --多重较验

### pytest-random-order

- --用例随机执行

### pytest-html

- --测试报告

### pytest_ini

---
[pytest] ini-options in the first pytest.ini|tox.ini|setup.cfg file found:

markers (linelist):   markers for test functions empty_parameter_set_mark (string):
default marker for empty parametersets norecursedirs (args): directory patterns to avoid for recursion testpaths (args):
directories to search for tests when no files or directories are given in the command line. filterwarnings (linelist):
Each line specifies a pattern for warnings.filterwarnings. Processed after -W/--pythonwarnings. usefixtures (args):
list of default fixtures to be used with this project python_files (args):  glob-style file patterns for Python test
module discovery python_classes (args):
prefixes or glob names for Python test class discovery python_functions (args):
prefixes or glob names for Python test function and method discovery
disable_test_id_escaping_and_forfeit_all_rights_to_community_support (bool):
disable string escape non-ascii characters, might cause unwanted side effects(use at your own risk)
console_output_style (string):
console output: "classic", or with additional progress information ("progress" (percentage) | "count"). xfail_strict (
bool):  default for the strict parameter of xfail markers when not given explicitly (default: False)
enable_assertion_pass_hook (bool):
Enables the pytest_assertion_pass hook.Make sure to delete any previously generated pyc cache files. junit_suite_name (
string):
Test suite name for JUnit report junit_logging (string):
Write captured log messages to JUnit report: one of no|log|system-out|system-err|out-err|all junit_log_passing_tests (
bool):
Capture log information for passing tests to JUnit report:
junit_duration_report (string):
Duration time to report: one of total|call junit_family (string):
Emit XML for schema: one of legacy|xunit1|xunit2 doctest_optionflags (args):
option flags for doctests doctest_encoding (string):
encoding used for doctest files cache_dir (string):   cache directory path. log_level (string):   default value for
--log-level log_format (string):  default value for --log-format log_date_format (string):
default value for --log-date-format log_cli (bool):       enable log display during test run (also known as "live
logging"). log_cli_level (string):
default value for --log-cli-level log_cli_format (string):
default value for --log-cli-format log_cli_date_format (string):
default value for --log-cli-date-format log_file (string):    default value for --log-file log_file_level (string):
default value for --log-file-level log_file_format (string):
default value for --log-file-format log_file_date_format (string):
default value for --log-file-date-format log_auto_indent (string):
default value for --log-auto-indent faulthandler_timeout (string):
Dump the traceback of all threads if a test takes more than TIMEOUT seconds to finish. addopts (args):       extra
command line options minversion (string):  minimally required pytest version required_plugins (args):
plugins that must be present for pytest to run automark_dependency (string):
Add the dependency marker to all tests automatically render_collapsed (bool):
Open the report with all rows collapsed. Useful for very large reports max_asset_filename_length (string):
set the maximum filename length for assets attached to the html report. rsyncdirs (pathlist): list of (relative) paths
to be rsynced for remote distributed testing. rsyncignore (pathlist):
list of (relative) glob-style paths to be ignored for rsyncing. looponfailroots (pathlist):
directories to check for changes

---
