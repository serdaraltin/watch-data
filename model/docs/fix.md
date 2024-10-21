``` pip install psycopg2
Collecting psycopg2
  Using cached psycopg2-2.9.9.tar.gz (384 kB)
  Preparing metadata (setup.py) ... error
  error: subprocess-exited-with-error
  
  × python setup.py egg_info did not run successfully.
  │ exit code: 1
  ╰─> [23 lines of output]
      running egg_info
      creating /tmp/pip-pip-egg-info-8ao4o2ms/psycopg2.egg-info
      writing /tmp/pip-pip-egg-info-8ao4o2ms/psycopg2.egg-info/PKG-INFO
      writing dependency_links to /tmp/pip-pip-egg-info-8ao4o2ms/psycopg2.egg-info/dependency_links.txt
      writing top-level names to /tmp/pip-pip-egg-info-8ao4o2ms/psycopg2.egg-info/top_level.txt
      writing manifest file '/tmp/pip-pip-egg-info-8ao4o2ms/psycopg2.egg-info/SOURCES.txt'
      
      Error: pg_config executable not found.
      
      pg_config is required to build psycopg2 from source.  Please add the directory
      containing pg_config to the $PATH or specify the full executable path with the
      option:
      
          python setup.py build_ext --pg-config /path/to/pg_config build ...
      
      or with the pg_config option in 'setup.cfg'.
      
      If you prefer to avoid building psycopg2 from source, please install the PyPI
      'psycopg2-binary' package instead.
      
      For further information please check the 'doc/src/install.rst' file (also at
      <https://www.psycopg.org/docs/install.html>).
      
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.```

sudo apt-get install libpq-dev python3-dev -y