from setuptools import setup, find_packages

version = '2.0'

setup(name='Products.CMFPlacefulWorkflow',
      version=version,
      description="Workflow policies for CMF and Plone",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='CMF Plone Zope2 workflow',
      author='Ingeniweb',
      author_email='support@ingeniweb.com',
      url='http://pypi.python.org/pypi/Products.CMFPlacefulWorkflow',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            'zope.testing',
            'Products.PloneTestCase',
        ]
      ),
      install_requires=[
          'setuptools',
          'zope.component',
          'zope.i18nmessageid',
          'zope.interface',
          'Products.CMFCore',
          'Products.GenericSetup',
          'Acquisition',
          'Zope2',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
