from distutils.core import setup

VERSION = '0.1.1'

setup(
	name		 = 'kpipe',
	packages	 = ['kpipe'],
	version		 = VERSION,
	license		 = 'MIT',
	description  = 'A one-file-script named `kpipe` that runs only-if-necessary the scripts contained in a folder named ./scripts.',
	author		 = 'kaalam',
	author_email = 'kaalam@kaalam.ai',
	url			 = 'https://github.com/kaalam/kpipe',
	download_url = 'https://github.com/kaalam/kpipe/dist/kpipe-%s.tar.gz' % VERSION,
	keywords	 = ['utilities', 'pipeline', 'etl'],
	scripts		 = ['bin/kpipe'],
	classifiers  = [
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3']
)
