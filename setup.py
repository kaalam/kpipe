from distutils.core import setup

setup(
	name		 = 'kpipe',
	packages	 = ['kpipe'],
	version		 = '0.1.3',
	license		 = 'MIT',
	description  = 'A one-file-script named `kpipe` that runs only-if-necessary the scripts contained in a folder named ./scripts.',
	author		 = 'kaalam',
	author_email = 'kaalam@kaalam.ai',
	url			 = 'https://github.com/kaalam/kpipe',
	download_url = 'https://github.com/kaalam/kpipe/dist/kpipe-0.1.tar.gz',
	keywords	 = ['utilities', 'pipeline', 'etl'],
	scripts		 = ['bin/kpipe'],
	classifiers  = [
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3']
)
