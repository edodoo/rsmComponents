#Components of a directive
#1.) Initialization
#2.) Parse Time
#3.) Output
#-------------------------
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

#Parsing
class IFrameInsertNode(nodes.General, nodes.Element):
    #Container to hold data until it is time to render output
    def __init__(self, content):
        super(IFrameInsertNode, self).__init__()
        self.iframe_content = content

class IFrameInsert(Directive):
    required_arguments = 1
    optional_arguments = 2
    has_content = True
    option_spec = {
        "link": directives.unchanged,
        "width": directives.nonnegative_int,
        "height": directives.nonnegative_int
    }

    def run(self):
        env = self.state.document.settings.env

        if not hasattr(env, 'iframeinsertcounter'):
            env.iframeinsertcounter = 0
        env.iframeinsertcounter += 1

        self.options["divid"] = self.arguments[0]
        if self.content: #specifies if a directive has content self.content is body content of directive
            source = "\n".join(self.content)
        else:
            source = "\n"

        self.options["filecontent"] = source

        if "height" not in self.options:
            self.options['height'] = 500
        if "width" not in self.options:
            self.options['width'] = 800

        return [nodes.raw('', f'<p align="center"><iframe src="{self.options["link"]}" width="{self.options["width"]}px" height="{self.options["height"]}px"></iframe></p>', format='html')]

def setup(app):
    app.add_directive('iframeinsert', IFrameInsert)
    app.add_javascript('bookfuncs.js')
    app.add_javascript('skulpt/dist/skulpt.js')
    app.add_javascript('skulpt/dist/builtin.js')

    app.connect('doctree-resolved', process_iframeinsert_nodes)
    app.connect('env-purge-doc', purge_iframeinserts)

def process_iframeinsert_nodes(arg1, arg2,arg3):
    pass

def purge_iframeinserts(arg1, arg2, arg3):
    pass
