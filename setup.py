from distutils.core import setup

setup(
	name		 = 'kpype',
	packages	 = ['kpype'],
	version		 = '0.1.1',
	license		 = 'MIT',
	description  = 'A one-file-script named `kpype` that runs only-if-necessary the scripts contained in a folder named ./scripts.',
	author		 = 'kaalam',
	author_email = 'kaalam@kaalam.ai',
	url			 = 'https://github.com/kaalam/kpype',
	download_url = 'https://github.com/kaalam/kpype/dist/kpype-0.1.tar.gz',
	keywords	 = ['utilities', 'pipeline', 'etl'],
	scripts		 = ['bin/kpype'],
	classifiers  = [
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3']
)
