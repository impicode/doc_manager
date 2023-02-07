from distutils.core import setup
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('doc_manager/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name="doc_manager",
    version=main_ns['__version__'],
    description="doc_manager class for django",
    install_requires=["django==3.2.17"],
    url="https://bitbucket.org/impicode/doc-manager/",
    package_dir={"doc-manager": "doc_manager"},
    include_package_data=True,
    data_files=[(
        'templates',
        ['doc_manager/templates/admin_change_form_documents.html']
    )],
    packages=[
        "doc_manager",
    ],
)
