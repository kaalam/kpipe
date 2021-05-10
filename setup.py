from distutils.core import setup

setup(
	name		 = 'pype',
	packages	 = ['pype'],
	version		 = '0.1',
	license		 = 'MIT',
	description  = 'A one-file-script named `pype` that runs only-if-necessary the scripts contained in a folder named ./scripts.',
	author		 = 'kaalam',
	author_email = 'kaalam@kaalam.ai',
	url			 = 'https://github.com/kaalam/pype',
	download_url = 'https://github.com/kaalam/pype/archive/v_01.tar.gz',
	keywords	 = ['utilities', 'pipeline', 'etl'],
	classifiers  = [
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3']
)
