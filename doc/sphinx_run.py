import os


class AutoConfig:
    
    def __init__(self, osname, current_dir):
        self.osname = osname
        self.current_dir = current_dir
        
    
    def create_sphinx(self):
        """This method is used for run sphnix-quickstart command.
        """
        try:
            
            if (self.osname == 'nt' or self.osname == 'posix'):
                start_sphinx = "sphinx-quickstart"
                os.system(start_sphinx)
            else:
                print("OS not found")
        
        except (Exception, os.error) as error:
            print("OS error:\n", error)
            
    
    def create_apidoc(self):
        """This method is used for run sphnix-apidoc command on the os.
        """
        
        if (self.osname == 'nt'):
            get_folder_name = self.current_dir.split('\\')
        if (self.osname == 'posix'):
            get_folder_name = self.current_dir.split('/')
        folder_name = get_folder_name[-1]
        root_dir = self.current_dir.strip(folder_name)
        modules = 'modules'
        root = root_dir+modules
        dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
        print(dirlist)
        for modulename in dirlist:
            start_apidoc = "sphinx-apidoc -o source/ ../modules/{}/".format(modulename)
            os.system(start_apidoc)
            print("creating {} rst file".format(modulename))
            
    
    def insert_modules_indexpage(self):
        if (self.osname == 'nt'):
            sourcefile = '\source'
            index_rst = '\index.rst'
        if (self.osname == 'posix'):
            sourcefile = '/source'
            index_rst = '/index.rst'

        required_dir = self.current_dir+sourcefile
        print(type(required_dir))
        rstfiles = os.listdir(required_dir)
        index_value = 12
        for readrstfile in rstfiles:
            if (readrstfile.endswith('.rst')):
                nameofthemodule = readrstfile.split('.rst')
                names = nameofthemodule[0]
                
                # I am removing module.rst file for my implementation
                if (readrstfile == "modules.rst"):
                    os.remove("{}/modules.rst".format(required_dir))

                if ('index' not in names and 'modules' not in names):
                    
                    file_object = open('{}{}'.format(required_dir, index_rst), 'r', encoding="utf-8")
                    contents = file_object.readlines()

                    with open('{}{}'.format(required_dir, index_rst), 'r+') as fd:
                        contents = fd.readlines()
                        contents.insert(index_value, '   '+names+"\n")  # new_string should end in a newline
                        fd.seek(0)  # readlines consumes the iterator, so we need to start over
                        fd.writelines(contents)  # No need to truncate as we are increasing filesize
                        index_value = index_value+1

    
    
    def add_config(self):
        if (self.osname == 'nt'):
            windows_add_source = '\\source\\'
            required_dir = self.current_dir+windows_add_source        

            index_value = 17
            # import os, sys and append path
            with open('{}conf.py'.format(required_dir), 'r+') as fd:
                    contents = fd.readlines()

                    # Insert config in conf.py
                    data = "import os\nimport sys\nimport sphinx_rtd_theme\nsys.path.insert(0, os.path.abspath('../..'))\nroot_dir = os.getcwd()\nremove_source = root_dir.strip('source')\nremove_doc = remove_source.strip('doc\\\\')\nadd_modules = '\\\\modules'\nget_module_path = remove_doc + add_modules\n"
                    main_modules = "for r,d,f in os.walk(r'{}'.format(get_module_path)):\n    sys.path.append(r)"
                    contents.insert(index_value, data+"\n"+main_modules)  # new_string should end in a newline
                    fd.seek(0)  # readlines consumes the iterator, so we need to start over
                    fd.writelines(contents)  # No need to truncate as we are increasing filesize
                    index_value = index_value+1
            

            index_value = 47
            with open('{}conf.py'.format(required_dir), 'r+') as fd:
                    contents = fd.readlines()
                    sphix_extension = "extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.mathjax', 'sphinx.ext.ifconfig', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon']"
                    contents.insert(index_value, sphix_extension+"\n")  # new_string should end in a newline
                    fd.seek(0)  # readlines consumes the iterator, so we need to start over
                    fd.writelines(contents)  # No need to truncate as we are increasing filesize       
            
            index_value = 61
            with open('{}conf.py'.format(required_dir), 'r+') as fd:
                    contents = fd.readlines()
                    d = "html_theme = 'sphinx_rtd_theme'"
                    theme = "html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]"
                    contents.insert(index_value, d+"\n"+theme+"\n")  # new_string should end in a newline
                    fd.seek(0)  # readlines consumes the iterator, so we need to start over
                    fd.writelines(contents)  # No need to truncate as we are increasing filesize

        if (self.osname == 'posix'):
            source_file = '/source'
            required_path = self.current_dir+source_file
            print(required_path)
            index_value = 17
            # import os, sys and append path
            with open('{}/conf.py'.format(required_path), 'r+') as fd:
                    contents = fd.readlines()
                    inser_config = "import os\nimport sys\nimport sphinx_rtd_theme\nsys.path.insert(0, os.path.abspath('../..'))\ndi = os.path.abspath(os.pardir)\nremove_doc = di.strip('doc')\n"
                    append_modules = "for r,d,f in os.walk(r'{}modules'.format(remove_doc)):\n    sys.path.append(r)"
                    contents.insert(index_value, inser_config+"\n"+append_modules)  # new_string should end in a newline
                    fd.seek(0)  # readlines consumes the iterator, so we need to start over
                    fd.writelines(contents)  # No need to truncate as we are increasing filesize
                    index_value = index_value+1
            
            index_value = 95
            with open('{}/conf.py'.format(required_path), 'r+') as fd:
                    contents = fd.readlines()
                    d = "html_theme = 'sphinx_rtd_theme'"
                    theme = "html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]"
                    contents.insert(index_value, d+"\n"+theme+"\n")  # new_string should end in a newline
                    fd.seek(0)  # readlines consumes the iterator, so we need to start over
                    fd.writelines(contents)  # No need to truncate as we are increasing filesize
        
                    
    def run_sphinx(self):
        if (self.osname == 'nt'):
            makehtml_command = ".\make html"
            os.system(makehtml_command)
        if (self.osname == 'posix'):
            makehtml_command = "make html"
            os.system(makehtml_command)


# Get os name
osname = os.name
# get current working directory
current_dir = os.getcwd()


obj = AutoConfig(osname, current_dir)

# This method used for run sphinx-quickstart
obj.create_sphinx()

# This method is used for run sphinx-apidoc -o source(destination for .rst files) ../modules/modulename
obj.create_apidoc()

# This method is used for insert module names in the index.rst file in the source folder
obj.insert_modules_indexpage()

#This method used for to insert sphinx_rtd_theme and add different type of extension to make html file
obj.add_config()

#This method is used for to run sphinx documentation and make html pages
obj.run_sphinx()