name = 'timeWarp'

version = '2.1.0.hh.2.2.0'

authors = [
    'Adam Baker',
]

description = '''Maya plugin for time wrapping'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['HH_REZ_REPO_RELEASE_EXT']

requires = [
    "maya",
]

private_build_requires = [
]

variants = [
]

def commands():
    env.REZ_TIMEWARP_ROOT = '{root}'
    env.PYTHONPATH.append('{root}/src/python')
    env.MAYA_PLUG_IN_PATH.append('{root}/src/python/timeWarp/plugins')


build_command = 'rez python {root}/rez_build.py'
uuid = 'repository.timeWarp'
