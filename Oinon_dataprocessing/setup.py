from distutils.core import setup
setup(
  name = 'Oinon_dataprocessing',         # How you named your package folder (foo)
  packages = ['Oinon_dataprocessing'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='LICENSE',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'As its name is,for data processing!',   # Give a short description about your library
  author = 'Summer',                   # Type in your name
  author_email = '1498443003@qq.com',      # Type in your E-Mail
  url = 'https://github.com/Onion653/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Onion653/Oinon_dataprocessing.git',
  #keywords = ['Cookie', 'Dictionary'],   # Keywords that define your package best
  install_requires=['numpy','matplotlib.pyplot','scipy.optimize','scipy.stats'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)